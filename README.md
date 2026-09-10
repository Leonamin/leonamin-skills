# leonamin-skills

Reusable skills for AI agentic coding tools.

## Skills

- `agent-browser`: 브라우저 조작과 실제 화면 검증.
- `code-review`: 동작·언어·구조·테스트·네이밍 관점을 통합한 코드 리뷰.
- `conversation-snapshot`: 작업을 이어가기 위한 간결한 상태 인계.
- `design-audit`: 기존 GUI를 화면과 코드 근거로 감사.
- `design-product`: 기존 문서를 활용한 제품 정체성·디자인 시스템 설계.
- `explain`: 예시와 시각화로 개념 설명.
- `figma-design`: 기존 디자인 근거를 편집 가능한 Figma 구조로 구현.
- `git-workflow`: 프로젝트 정책에 맞는 Git 작업과 한국어 작성 규칙.
- `manage-design-md`: DESIGN.md 작성과 형식 검증.
- `ui-before-after-sketch`: 구현 전 HTML/CSS Before·After 비교 시안.
- `wiki-read`: 관련 위키 지식 탐색.
- `wiki-setup`: 위키 위치와 구조 초기 설정.
- `wiki-update`: 확정 지식과 결정의 위키 반영.

## Layout

각 스킬은 루트의 `<skill-name>/SKILL.md`에 둔다. 필요한 참조 문서, 스크립트와 UI 메타데이터는 해당 스킬 디렉터리 안에 둔다.

## Install

`./install.sh codex`, `./install.sh claude`, `./install.sh reasonix`, `./install.sh opencode` 또는 `./install.sh all`을 실행한다.

- Codex / OpenCode: `~/.agents/skills/`
- Claude Code: `~/.claude/skills/`
- Reasonix: `~/.reasonix/skills/`

설치 시 폐기한 이 저장소의 스킬은 설치 경로 밖의 백업 디렉터리로 이동한다. 이름이 같은 다른 스킬은 원본 식별 문구가 일치할 때만 이동한다. 그 외 설치 스킬은 보존한다.
