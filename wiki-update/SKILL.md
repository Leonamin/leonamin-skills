---
name: wiki-update
description: >
  OKF(Open Knowledge Format) 위키 관리 스킬.
  `/wiki-update` — 대화 내용을 위키에 기록/갱신.
  `/wiki-setup` — 기본 OKF 위키 구조를 초기화.
  위키 경로는 `<project-root>/.agents/wiki-path` 또는 `.env`의 `WIKI_PATH`로 설정한다.
---

# Wiki Update — OKF 지식 관리

OKF(Open Knowledge Format) v0.1 기반 프로젝트 위키를 관리한다.
구글 Cloud가 제안한 벤더 중립적 지식 표현 형식으로,
마크다운 + YAML frontmatter의 디렉토리 트리 구조를 사용한다.

## 1. 위키 경로 확인

다음 우선순위로 위키 경로를 결정한다:

1. `<project-root>/.agents/wiki-path` 파일 (1순위)
   - 파일 내용: 위키 디렉토리 경로 (절대경로 또는 프로젝트 루트 기준 상대경로)
   - 예: `./wiki` 또는 `/home/user/my-project/docs/wiki`
2. `<project-root>/.env` 파일의 `WIKI_PATH` 변수 (2순위)
   - 예: `WIKI_PATH=./wiki`
3. 위 둘 다 없으면 **사용자에게 직접 질문**한다
   - "위키 디렉토리 경로를 입력해주세요. (예: `./wiki` 또는 `/absolute/path/to/wiki`)"
   - 응답을 받으면 해당 경로를 `.agents/wiki-path`에 저장한다 (`.agents/` 디렉토리 자동 생성)
4. **세션 캐시**: 한 번 확인한 경로는 세션 내 `wiki-path` 메모리에 저장해 재사용한다

### `.agents/wiki-path` 파일 형식

```
# 위키 경로 설정 파일 (선행 #은 주석)
./wiki
```

### `.env` 설정 예시

```env
WIKI_PATH=./wiki
```

## 2. 명령어: `/wiki-setup`

기본 OKF 위키 구조를 초기화한다.
위키 경로를 먼저 확인한 후, 해당 경로에 다음 구조를 생성한다:

```
<wiki-path>/
├── index.md              # OKF 루트 인덱스 (필수)
├── log.md                # 변경 이력 (필수)
├── concepts/             # 기획 개념 디렉토리
├── decisions/            # 의사결정 기록 (ADR)
└── references/           # 외부 레퍼런스
```

### 생성되는 기본 `index.md`

```markdown
---
okf_version: "0.1"
title: "{프로젝트명} Wiki"
description: "OKF v0.1 기반 프로젝트 지식 베이스"
---

# {프로젝트명} Wiki

> OKF v0.1 준수. 사람과 AI 에이전트 모두가 읽을 수 있는 지식 베이스.

## Concepts

(프로젝트 기획 개념을 여기에 링크합니다)

## Decisions

(ADR을 여기에 링크합니다)

## References

(외부 레퍼런스를 여기에 링크합니다)
```

### 생성되는 기본 `log.md`

```markdown
# Log

## {오늘 날짜}

**Wiki initialized** — OKF v0.1 구조 생성.
```

### 실행 규칙

- 위키 경로가 이미 존재하고 `index.md`가 있으면 **아무것도 하지 않고 종료**한다
- `index.md`가 없으면 위 구조를 생성한다
- 각 디렉토리에 `.gitkeep` 파일을 생성할 수도 있다 (선택)
- 완료 시 `log.md`에 초기화 기록을 추가한다

## 3. 명령어: `/wiki-update`

대화 내용을 위키에 기록하거나 갱신한다.

### 실행 흐름

1. 위키 경로 확인 (1번 절차와 동일)
2. 사용자가 기록/갱신하려는 내용 파악
3. 적절한 카테고리(concepts / decisions / references)와 파일명 결정
4. 기존 파일이 있으면 읽어서 병합/갱신, 없으면 신규 생성
5. `log.md`에 변경 이력 추가

### 파일 작성 규칙

- **모든 파일**은 OKF YAML frontmatter로 시작한다
  ```markdown
  ---
  type: Concept | Decision | Reference
  title: "..."
  description: "..."
  tags: [tag1, tag2]
  timestamp: {YYYY-MM-DD}
  ---
  ```
- **Concepts**: 기획 개념, 게임 디자인, 시스템 설명 등
  - 파일명: kebab-case (예: `core-loop.md`, `difficulty-system.md`)
  - `type: Concept`
- **Decisions**: ADR (Architecture Decision Record)
  - 파일명: `{3자리번호}-{제목}.md` (예: `001-tech-stack.md`)
  - `type: Decision`
  - 내용: Context → Decision → Consequences 구조 권장
- **References**: 외부 기술, 플랫폼, 도구 레퍼런스
  - 파일명: kebab-case (예: `phaser-3.md`, `okf-spec.md`)
  - `type: Reference`
- **index.md 갱신**: 새 파일을 추가했다면 `index.md`의 해당 섹션에 링크를 추가한다
- **log.md 기록**: 변경 시마다 날짜별 항목을 추가한다
  ```markdown
  ## {YYYY-MM-DD}

  **{변경 요약}** — {상세 설명}:
  - 추가/갱신/삭제한 파일 목록
  ```

### 판단 기준

- **concepts vs decisions vs references**:
  - "왜"에 대한 결정 → `decisions/` (ADR)
  - "무엇"에 대한 설명 → `concepts/`
  - "어디서 봤는지" 외부 정보 → `references/`
- **파일 분할**: 하나의 파일에 하나의 주제. 너무 큰 주제는 하위 섹션으로 분리
- **병합**: 기존 파일이 있으면 기존 내용을 유지하면서 추가/수정한다. 기존 내용을 덮어쓰지 않는다

## 4. OKF v0.1 스펙 요약

| 항목 | 내용 |
|---|---|
| 형식 | 마크다운 파일 + YAML frontmatter의 디렉토리 트리 |
| 필수 필드 | `type` 하나만 |
| 권장 필드 | `title`, `description`, `tags`, `timestamp` |
| 예약 파일 | `index.md` (디렉토리 맵), `log.md` (변경 이력) |
| 링크 | 표준 마크다운 링크 (`[text](./path.md)`) |
| 철학 | Minimally opinionated, Composes with existing tools, Format not platform |

## 5. 예시 워크플로

### 새 Concept 추가하기

```
User: /wiki-update 코어 루프 문서를 작성해줘
→ AI: wiki-path 확인 → concepts/core-loop.md 읽기(없으면 신규)
→ AI: OKF frontmatter + 내용 작성 → index.md에 링크 추가 → log.md 기록
```

### ADR 추가하기

```
User: /wiki-update 기술 스택 결정을 ADR로 기록해줘
→ AI: wiki-path 확인 → decisions/ 디렉토리에서 다음 번호 계산
→ AI: 001-xxx.md 형식으로 생성 → index.md 갱신 → log.md 기록
```
