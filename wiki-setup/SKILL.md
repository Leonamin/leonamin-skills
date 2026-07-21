---
name: wiki-setup
description: "프로젝트 위키를 처음 설정하거나 기존 위키 구조를 재설계할 때 사용한다. 사용자에게 위키 위치, 최상위 분류, 하위 구조, 문서화 범위와 인덱스 정책을 확인한 뒤 프로젝트 루트에 .agents/wiki-path와 .agents/wiki-structure.md를 기록하고 OKF 기반 위키 디렉토리와 각 디렉토리의 index.md를 초기화한다. 변경 이력은 logs/index.md와 날짜·주제별 로그 문서로 구성한다."
---

# Wiki Setup — OKF 위키 초기 설정

## 역할

프로젝트 위키의 위치와 구조를 처음 정하고 초기 파일을 만드는 전용 스킬이다. 이미 작성된 내용을 갱신하거나 작업 중 지식을 읽는 역할은 맡지 않는다.

OKF(Open Knowledge Format) v0.1 스타일의 Markdown + YAML frontmatter 구조를 사용한다. 위키 루트뿐 아니라 모든 위키 디렉토리에 index.md를 두어 각 단계에서 하위 구조를 탐색할 수 있게 한다.

## 초기 확인

1. 프로젝트 루트를 확인한다.
   - 가능하면 git rev-parse --show-toplevel을 사용한다.
   - git 저장소가 아니면 현재 작업 디렉토리를 프로젝트 루트로 본다.
2. 다음 파일을 확인한다.
   - <project-root>/.agents/wiki-path
   - <project-root>/.agents/wiki-structure.md
   - <project-root>/.env의 WIKI_PATH
3. 기존 설정과 위키가 있으면 덮어쓰지 말고 현재 상태와 충돌을 설명한다.

경로 우선순위는 다음과 같다.

1. 작업 요청에서 직접 지정한 경로
2. <project-root>/.agents/wiki-path
3. <project-root>/.env의 WIKI_PATH
4. 사용자에게 확인한 경로

상대 경로는 프로젝트 루트를 기준으로 해석한다.

## 사용자에게 확인할 내용

설정을 시작할 때 다음을 한 번에 묻는다. 이미 설정된 값은 다시 묻지 말고 확인만 받는다.

- 위키 위치: 기본값은 ./wiki
- 최상위 분류: 기본값은 concepts, decisions, references
- 프로젝트에만 필요한 추가 분류나 하위 디렉토리
- 기존 문서가 있다면 유지·이관할 범위
- 모든 디렉토리에 index.md를 둘지 여부: 이 스킬의 기본값은 항상 둔다

사용자가 세부 구조를 정하지 못하면 다음 기본안을 제안하고 확인받는다.

- concepts: 기획, 도메인, 시스템과 기능 개념
- decisions: ADR 형식의 기술·제품 의사결정
- references: 외부 문서, 도구와 플랫폼 참고 자료

구조는 처음부터 완벽하게 확정하지 않는다. 자주 함께 읽는 문서를 같은 하위 디렉토리에 묶고, 새 디렉토리를 만들 때도 index.md를 추가하는 원칙을 우선한다.

## 프로젝트 설정 파일

사용자 확인 후 .agents 디렉토리를 만들고 다음 파일을 기록한다.

### .agents/wiki-path

파일에는 위키 경로만 기록한다. 주석과 비밀 값은 넣지 않는다.

~~~text
./wiki
~~~

### .agents/wiki-structure.md

위키의 대략적인 구조와 운영 규칙을 사람이 읽을 수 있는 문서로 기록한다.

~~~markdown
# Wiki Structure

- Wiki path: ./wiki
- Format: OKF v0.1 style Markdown with YAML frontmatter
- Index policy: Every wiki directory contains index.md
- Change log: ./wiki/logs/

## Directory map

- concepts/: 프로젝트 개념, 도메인과 시스템 설명
- decisions/: 기술·제품 의사결정 기록
- references/: 외부 자료와 도구 참고 문서
- logs/: 날짜·주제별 위키 변경 이력

## Rules

- 문서 하나에는 하나의 주제를 둔다.
- 새 문서와 새 디렉토리는 해당 디렉토리의 index.md에 등록한다.
- index.md는 하위 구조를 안내하는 지도이며 일반 지식 문서와 구분한다.
- logs/ 문서는 YYYY-MM-DD-kebab-case.md 형식을 사용하고, logs/index.md에 등록한다.
- decisions/ 문서는 번호가 있는 ADR로 관리한다.
~~~

사용자가 선택한 분류와 경로로 이 내용을 조정한다. 이 파일은 위키 문서가 아니라 프로젝트별 위키 운영 설정이다.

## 위키 구조 초기화

기본 구조는 다음과 같다.

~~~text
<wiki-path>/
├── index.md
├── logs/
│   └── index.md
├── concepts/
│   └── index.md
├── decisions/
│   └── index.md
└── references/
    └── index.md
~~~

사용자가 추가 분류를 선택하면 각 디렉토리에도 index.md를 만든다. 더 깊은 하위 디렉토리를 만들 때도 같은 규칙을 재귀적으로 적용한다.

### index.md 규칙

각 index.md는 자신이 있는 디렉토리의 범위를 설명하고, 바로 아래 문서와 하위 디렉토리의 index.md만 링크한다. 전체 위키의 모든 문서를 한 index.md에 나열하지 않는다.

예시 frontmatter:

~~~yaml
---
type: Index
title: "Concepts"
description: "프로젝트 개념 문서의 구조와 목록"
scope: "concepts"
okf_version: "0.1"
---
~~~

### logs/index.md 규칙

logs/index.md도 YAML frontmatter를 사용한다. 로그 목록은 최신 문서부터 정렬하며, logs/ 바로 아래의 로그 문서만 링크한다.

~~~markdown
---
type: Index
title: "Wiki Logs"
description: "위키 초기화와 변경 이력의 탐색 지도"
scope: "logs"
okf_version: "0.1"
---

# Wiki Logs
~~~

### 로그 문서 규칙

로그 문서도 YAML frontmatter를 사용하며 파일명은 `YYYY-MM-DD-kebab-case.md` 형식을 사용한다.

~~~markdown
---
type: Log
title: "Wiki Structure Update"
description: "위키 구조 변경 이력"
timestamp: 2026-01-01
okf_version: "0.1"
---

# Wiki Structure Update

위키 구조를 생성하거나 변경한 이유와 영향을 기록한다.
~~~

날짜는 실제 현재 날짜를 사용한다.

## 실행 안전성

- 위키 경로나 구조 설정이 이미 있으면 사용자 확인 없이 변경하지 않는다.
- wiki-path가 가리키는 디렉토리에 index.md가 이미 있으면 기존 내용을 덮어쓰지 않는다.
- 누락된 index.md를 추가할 때도 기존 문서 링크를 먼저 읽어 보존한다.
- 프로젝트 파일과 기존 위키 문서를 삭제하거나 자동 이동하지 않는다.
- 기존 루트 log.md가 있으면 삭제하거나 자동 이동하지 않는다. 새 로그 구조를 만들고 logs/index.md에서 기존 log.md를 레거시 기록으로 안내할 수 있다.
- 초기화가 끝나면 생성·변경한 파일과 이후 사용할 $wiki-update, $wiki-read 호출을 보고한다.
