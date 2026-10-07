# React 소스 감사 도구

**직접 JSX 속성에서 조사 후보를 찾는다. 실제 DOM·스타일·접근성 판정은 별도로 수행한다.**

## 실행

Node.js와 TypeScript compiler API(5.x에서 검증)가 필요하다. 대상 프로젝트에서 resolve하며 다른 위치의 compiler는 `--typescript <absolute-path-to-typescript.js>`로 지정한다. 필요하면 별도 도구 디렉터리에 호환 compiler를 준비하며 자동 설치하지 않는다.

```bash
node <skill-dir>/scripts/audit-interactive-components.mjs \
  --root <repo> --source src --json
```

`--source`는 저장소 기준 디렉터리이며 반복 가능하고 파일은 중복 제거한다. `--config <repo-relative-json-path>`를 지정해야 설정을 읽으며 CLI source가 `sourceRoots`를 대체한다.

## 설정과 예외

```json
{
  "sourceRoots": ["src"],
  "failCategories": ["non-semantic-action"],
  "exceptions": [
    {
      "file": "src/ui/Dialog.tsx",
      "category": "non-semantic-action",
      "marker": "backdrop-dismiss",
      "reason": "키보드 닫기를 별도 제공하는 backdrop"
    }
  ]
}
```

예외는 정확한 파일·카테고리·이유로 제한한다. marker가 있으면 요소의 리터럴 `data-interaction-exception`까지 일치해야 한다. marker가 없으면 해당 파일의 카테고리 전체를 제외하므로 primitive 내부 구현에만 좁게 사용한다. 주석·`stopPropagation`은 자동 예외가 아니다. 예외 후보도 JSON findings에 이유와 함께 남는다.

카테고리는 `non-semantic-action`(비시맨틱 태그의 직접 click/mouse/pointer), `raw-button`·`raw-anchor`·`raw-action-input`(공용화 후보), `direct-next-link`(직접 import), `clickable-abstraction`(`clickable`·`onTap`)이다. 기본 실패 대상은 `non-semantic-action`만이다. 나머지는 프로젝트 계약에 맞춰 판단한다.

## 범위와 종료 코드

`.tsx`·`.jsx`만 검사하고 node_modules·.git·dist·build·.next 및 test/spec/stories를 제외한다. Vue·Svelte·HTML, prop spread, 컴포넌트 간접 동작과 실제 DOM/CSS는 분석하지 않는다. cursor·키보드·접근성 이름·중첩 액션은 실제 화면에서 확인한다.

일반 감사는 후보가 있어도 0, `--check`는 선택 카테고리의 비예외 후보가 있으면 1이다. 설정·파싱·의존성 오류, 대상 부재·검사 파일 0개는 2다. JSON에는 `filesScanned`, `summary`, `findings`, `violations`가 포함된다.

## CI와 도구 회귀 검사

프로젝트 정책·경로·예외는 프로젝트에 둔다. CI는 개인 홈 설치본 대신 특정 커밋이나 저장소에 버전 관리한 도구 사본을 사용한다.

```bash
INTERACTION_TYPESCRIPT_PATH=<absolute-path-to-typescript.js> \
  node --test <skill-dir>/scripts/audit-interactive-components.test.mjs
```

compiler 경로를 생략하면 현재 작업 디렉터리에서 TypeScript를 resolve한다.
