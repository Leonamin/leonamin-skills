# React 소스 감사 도구

Node.js와 TypeScript 5.x의 JavaScript compiler API가 필요하다. `.tsx`와 `.jsx`의 직접 JSX 속성을 검사한다. Vue, Svelte, HTML, prop spread 내부 값, 컴포넌트 구현을 통한 간접 동작과 실제 DOM/CSS는 분석하지 않는다.

```bash
node <skill-dir>/scripts/audit-interactive-components.mjs \
  --root <repo> --source src --json
```

`--source`는 반복 가능하다. 경로는 저장소 루트 기준이며 디렉터리여야 한다. 대상이 없거나 검사할 파일이 0개이면 종료 코드 2로 실패한다. 중복 경로는 파일 단위로 중복 제거한다. node_modules, .git, dist, build, .next와 test/spec/stories 파일은 제외한다.

TypeScript는 대상 저장소의 `package.json` 위치에서 resolve한다. 워크스페이스의 다른 위치에만 설치됐다면 `--typescript <absolute-path-to-typescript.js>`로 compiler 파일을 명시한다. 대상 프로젝트가 다른 compiler API를 사용한다면 별도 도구용 디렉터리에 TypeScript 5.x를 설치하고 해당 파일을 지정한다. 도구가 의존성을 자동 설치하지는 않는다.

## 프로젝트 설정

`--config <repo-relative-json-path>`로 다음 설정을 읽는다. CLI의 `--source`는 설정의 sourceRoots를 대체한다. 설정 파일은 명시했을 때만 읽는다.

```json
{
  "sourceRoots": ["src"],
  "failCategories": ["non-semantic-action", "raw-action-input"],
  "exceptions": [
    {
      "file": "src/ui/Checkbox.tsx",
      "category": "raw-action-input",
      "reason": "공용 checkbox의 native input 구현"
    },
    {
      "file": "src/ui/Dialog.tsx",
      "category": "non-semantic-action",
      "marker": "backdrop-dismiss",
      "reason": "키보드 닫기를 별도 제공하는 backdrop"
    }
  ]
}
```

예외는 정확한 파일과 카테고리로 제한한다. `marker`가 있으면 해당 요소의 리터럴 `data-interaction-exception` 값까지 일치해야 한다. marker 없는 예외는 파일 내 해당 카테고리 전체에 적용하므로 primitive 내부 구현에만 좁게 사용한다. 주석이나 `stopPropagation` 문자열은 자동 예외가 아니다. 예외 처리된 후보도 JSON의 findings에 이유와 함께 남는다.

카테고리:

- `non-semantic-action`: 비시맨틱 태그에 직접 click/mouse/pointer 액션 속성
- `raw-button`, `raw-anchor`, `raw-action-input`: 공용 컴포넌트로의 이전 검토 후보
- `direct-next-link`: `next/link` 직접 import 검토 후보
- `clickable-abstraction`: `clickable` 또는 `onTap` 속성 검토 후보

기본 failCategories는 `non-semantic-action`만 포함한다. raw HTML이나 clickable API는 프로젝트 계약에 따라 유효할 수 있으므로 자동 위반으로 강제하지 않는다. `--check`는 선택한 카테고리의 비예외 후보가 있으면 종료 코드 1을 반환한다. 일반 감사는 후보가 있어도 0, 설정·파싱·의존성 오류는 2다.

JSON에는 filesScanned, summary, findings, violations가 포함된다. cursor, 키보드 동작, 접근성 이름과 중첩 액션은 실제 렌더링에서 별도로 확인한다.

## 유지보수와 CI

프로젝트의 경로·예외·정책은 프로젝트에 남긴다. CI에서는 개인 홈의 설치본에 의존하지 말고 이 도구를 특정 커밋으로 고정해 가져오거나 저장소에 버전 관리한 사본으로 실행한다.

스크립트 회귀 검사는 다음과 같이 실행한다. compiler 경로를 생략하면 현재 작업 디렉터리에서 TypeScript를 resolve한다.

```bash
INTERACTION_TYPESCRIPT_PATH=<absolute-path-to-typescript.js> \
  node --test <skill-dir>/scripts/audit-interactive-components.test.mjs
```
