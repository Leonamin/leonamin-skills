# leonamin-skills

코드 리뷰, UI 설계·검증, Git 작업과 위키 관리를 위한 재사용 가능한 AI 에이전트 스킬 모음.

## Skills

- `agent-browser`: 브라우저 조작과 실제 화면 검증.
- `code-review`: 동작·언어·구조·테스트·네이밍 관점을 통합한 코드 리뷰.
- `component-inventory`: 프로젝트별 공용 UI 컴포넌트 범위와 누락 점검, 인벤토리 유지.
- `conversation-snapshot`: 작업을 이어가기 위한 간결한 상태 인계.
- `design-audit`: 기존 GUI를 화면과 코드 근거로 감사.
- `design-playground`: 레퍼런스 기반 화면의 규칙·구조를 직접 조정·비교하고 선택값을 구현에 전달.
- `design-product`: 기존 문서를 활용한 제품 정체성·디자인 시스템 설계.
- `explain`: 예시와 시각화로 개념 설명.
- `figma-design`: 기존 디자인 근거를 편집 가능한 Figma 구조로 구현.
- `git-workflow`: 프로젝트 정책에 맞는 Git 작업과 한국어 작성 규칙.
- `make-prototype`: 구조·디자인·공유 컴포넌트·기능 구현·검수를 연결하는 프로토타입 제작.
- `manage-design-md`: DESIGN.md 작성과 형식 검증.
- `manage-storybook`: Storybook 생성과 스토리 분류·상태·인터랙션·실행 환경 관리.
- `standardize-interactive-components`: 웹 인터랙션 컴포넌트 통합과 프로젝트 정책 기반 재발 방지 검사.
- `ui-before-after-sketch`: 구현 전 HTML/CSS Before·After 시안, 상태별 보기와 모션 배속 재생.
- `use-goodcase-ui`: 동봉된 Goodcase UI 컴포넌트·스타일·토큰·동작 계약을 프로젝트에 적용.
- `wiki`: 위키 지식 탐색과 요청된 기록·갱신·초기 설정.

## Install

Node.js 22.20 이상과 pnpm이 필요하다. [Skills CLI](https://github.com/vercel-labs/skills)로 설치한다.

프로젝트 폴더에서 실행하면 설치할 스킬과 사용할 에이전트를 선택할 수 있다.

```sh
pnpm dlx skills add Leonamin/leonamin-skills
```

Codex에서 모든 프로젝트에 사용할 스킬을 한 번에 설치하려면:

```sh
pnpm dlx skills add Leonamin/leonamin-skills -g -a codex --skill '*' -y
```

특정 스킬만 설치하려면 `--skill`에 이름을 지정한다.

```sh
pnpm dlx skills add Leonamin/leonamin-skills -g -a codex --skill code-review wiki -y
```

`-g`를 빼면 현재 프로젝트에만 설치한다. 다른 도구는 `-a`에 `claude-code`, `opencode`, `reasonix`, `antigravity` 등을 지정한다. 여러 도구를 함께 지정할 수도 있다. 설치 후 에이전트에 스킬 이름과 수행할 작업을 요청한다.

## Maintain

각 스킬은 루트의 `<skill-name>/SKILL.md`에 둔다. 필요한 참조 문서, 스크립트와 UI 메타데이터는 해당 스킬 디렉터리 안에 둔다.

이 저장소에서 로컬 스킬 목록을 확인하려면:

```sh
pnpm dlx skills add . --list
```

로컬 변경을 설치하려면 저장소 경로를 사용한다.

```sh
pnpm dlx skills add . -g -a codex --skill '*' -y
```

기존 `install.sh`의 설치본도 위 명령으로 다시 설치할 수 있다. 폐기한 스킬을 자동으로 정리하는 기존 스크립트의 기능은 제공하지 않으므로, 불필요한 설치본은 별도로 확인해 제거한다.
