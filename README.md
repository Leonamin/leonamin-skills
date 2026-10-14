# leonamin-skills

Reusable skills for AI agentic coding tools.

## Skills

- `agent-browser`: 브라우저 조작과 실제 화면 검증.
- `code-review`: 동작·언어·구조·테스트·네이밍 관점을 통합한 코드 리뷰.
- `component-inventory`: 프로젝트별 공용 UI 컴포넌트 범위와 누락 점검, 인벤토리 유지.
- `conversation-snapshot`: 작업을 이어가기 위한 간결한 상태 인계.
- `design-audit`: 기존 GUI를 화면과 코드 근거로 감사.
- `design-product`: 기존 문서를 활용한 제품 정체성·디자인 시스템 설계.
- `explain`: 예시와 시각화로 개념 설명.
- `figma-design`: 기존 디자인 근거를 편집 가능한 Figma 구조로 구현.
- `git-workflow`: 프로젝트 정책에 맞는 Git 작업과 한국어 작성 규칙.
- `make-prototype`: 구조·디자인·공유 컴포넌트·기능 구현·검수를 연결하는 프로토타입 제작.
- `manage-design-md`: DESIGN.md 작성과 형식 검증.
- `standardize-interactive-components`: 웹 인터랙션 컴포넌트 통합과 프로젝트 정책 기반 재발 방지 검사.
- `ui-before-after-sketch`: 구현 전 HTML/CSS Before·After 비교 시안.
- `ui-design-concept`: 이미지 기반 화면 시안과 필요한 예외 상태 설계, 구현 기준 인계.
- `use-goodcase-ui`: 동봉된 Goodcase UI 컴포넌트·스타일·토큰·동작 계약을 프로젝트에 적용.
- `wiki-read`: 관련 위키 지식 탐색.
- `wiki-setup`: 위키 위치와 구조 초기 설정.
- `wiki-update`: 확정 지식과 결정의 위키 반영.

## Layout

각 스킬은 루트의 `<skill-name>/SKILL.md`에 둔다. 필요한 참조 문서, 스크립트와 UI 메타데이터는 해당 스킬 디렉터리 안에 둔다.

## Install

다른 프로젝트의 폴더에서 Goodcase UI만 설치하려면:

```sh
pnpm dlx skills add Leonamin/leonamin-skills --skill use-goodcase-ui -a codex -y
```

전체 프로젝트에서 사용하려면 `-g`를 추가한다. 설치한 Codex 세션에서 `$use-goodcase-ui`로 사용한다. 컴포넌트 코드와 참조 문서까지 함께 설치되므로 Goodcase 원본 프로젝트 경로를 제공할 필요가 없다. [Skills CLI 옵션](https://github.com/vercel-labs/skills#options)

`use-goodcase-ui`는 [Leonamin/goodcase](https://github.com/Leonamin/goodcase)에서 생성한 배포본이다. 이 폴더를 직접 수정하지 말고 Goodcase 원본을 수정한 뒤 `pnpm build:skill --output <이 저장소 경로>/use-goodcase-ui`로 갱신한다. 버전·내용 해시는 `use-goodcase-ui/manifest.json`에서 확인한다.

`./install.sh codex`, `./install.sh claude`, `./install.sh reasonix`, `./install.sh opencode`, `./install.sh antigravity` 또는 `./install.sh all`을 실행한다.

- Codex / OpenCode: `~/.agents/skills/`
- Claude Code: `~/.claude/skills/`
- Reasonix: `~/.reasonix/skills/`
- Antigravity: `~/.gemini/config/skills/`

설치 시 폐기한 이 저장소의 스킬은 설치 경로 밖의 백업 디렉터리로 이동한다. 이름이 같은 다른 스킬은 원본 식별 문구가 일치할 때만 이동한다. 그 외 설치 스킬은 보존한다.
