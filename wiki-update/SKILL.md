---
name: wiki-update
description: "대화에서 확인된 지식, 구현 내용, 기술 결정, 장애 원인과 변경 사항을 프로젝트 위키에 기록하거나 기존 문서를 갱신할 때 사용한다. 위키 초기 설정은 하지 않으며, 위키 경로와 구조가 없으면 $wiki-setup을 안내한다. 새 문서나 하위 디렉토리를 만들 때 관련 index.md와 logs/index.md 및 날짜·주제별 로그 문서도 함께 갱신한다."
---

# Wiki Update — OKF 위키 기록·갱신

## 역할

대화와 작업에서 확정된 내용을 OKF 기반 프로젝트 위키에 기록하거나 기존 문서를 갱신한다. 위키를 처음 설정하거나 작업 전에 위키를 읽는 역할은 맡지 않는다.

## 위키 경로와 구조 확인

프로젝트 루트를 확인한 뒤 다음 우선순위로 위키 경로를 찾는다.

1. 작업 요청에서 직접 지정한 경로
2. <project-root>/.agents/wiki-path
3. <project-root>/.env의 WIKI_PATH
4. 세션에서 이미 확인한 경로

상대 경로는 프로젝트 루트를 기준으로 해석한다.

위 경로가 없으면 직접 새 경로를 만들거나 .agents/wiki-path를 생성하지 않는다. 사용자에게 먼저 $wiki-setup을 실행하도록 안내하고, 현재 업데이트는 멈춘다.

경로를 찾은 뒤 <project-root>/.agents/wiki-structure.md를 읽어 프로젝트별 분류와 중첩 규칙을 따른다. 구조 파일이 없으면 위키 루트 index.md와 각 상위 디렉토리 index.md를 기준으로 판단하고, 새 구조를 임의로 넓히지 않는다.

## 실행 흐름

1. 대화에서 위키에 남길 확정 사실, 결정, 설명, 근거와 미확정 내용을 구분한다.
2. 변경 대상 문서의 유형과 위치를 결정한다.
   - concepts: 무엇인지, 어떻게 동작하는지 설명
   - decisions: 왜 그렇게 결정했는지와 결과를 남기는 ADR
   - references: 외부 자료, 도구와 플랫폼 정보
3. 대상 디렉토리의 index.md와 기존 문서를 먼저 읽는다.
4. 기존 문서가 있으면 내용을 보존하면서 갱신하고, 없으면 새 문서를 만든다.
5. 새 문서·새 하위 디렉토리·이름 변경이 생기면 대상 디렉토리부터 위키 루트까지 각 index.md를 갱신한다.
6. logs/ 디렉토리의 날짜·주제별 로그 문서를 만들고 logs/index.md에 등록한다.
7. 기존 구조가 아직 루트 log.md만 사용하는 경우에는 기존 log.md를 보존하고, 구조 설정에 따라 logs/로 점진적으로 전환한다.
8. 변경 파일, 링크와 frontmatter를 확인한다.

## 파일 규칙

모든 Markdown 위키 파일은 YAML frontmatter로 시작한다. 위키 운영 설정 파일인 .agents/wiki-structure.md는 예외다.

### 일반 문서 frontmatter

~~~yaml
---
type: Concept | Decision | Reference
title: "문서 제목"
description: "문서가 다루는 범위"
tags: [tag1, tag2]
timestamp: 2026-01-01
---
~~~

- concepts 문서는 kebab-case 파일명을 사용하고 type은 Concept으로 한다.
- decisions 문서는 3자리 번호의 ADR 파일명을 사용한다. 예: 001-tech-stack.md
- references 문서는 kebab-case 파일명과 type Reference를 사용한다.
- 기존 문서의 frontmatter 키와 날짜 형식을 유지한다.
- 확정되지 않은 내용은 결정된 사실처럼 쓰지 말고 가정·질문·후속 과제로 표시한다.

### Decision 문서

decisions 문서는 다음 구조를 권장한다.

~~~markdown
# 001. 제목

## Context

왜 이 결정을 검토했는가.

## Decision

무엇을 선택했는가.

## Consequences

어떤 이점, 비용과 후속 작업이 생기는가.

## Status

Accepted, Superseded 또는 Proposed
~~~

번호는 decisions/index.md와 기존 파일을 확인해 다음 번호를 정한다. 파일을 삭제하거나 번호를 재사용하지 않는다.

### index.md 갱신

각 디렉토리의 index.md는 해당 디렉토리의 바로 아래 항목만 링크한다.

- 문서: ./file.md
- 하위 디렉토리: ./subdirectory/index.md

새 문서를 concepts/example/topic.md에 만들었다면 다음을 갱신한다.

1. concepts/example/index.md
2. concepts/index.md
3. 위키 루트 index.md

중간 디렉토리의 index.md가 없으면 먼저 만들되, 기존 구조와 링크를 보존한다. index.md 안에 자신을 링크하거나 전체 위키 문서를 중복 나열하지 않는다.

### 로그 갱신

`logs/`가 있으면 새 변경 묶음마다 `YYYY-MM-DD-kebab-case.md` 로그 문서를 만든다. 같은 날짜와 주제의 로그가 이미 있으면 기존 내용을 덮어쓰지 말고 순번을 붙이거나 기존 로그에 병합한다. 새 로그는 `logs/index.md`의 최신 항목에 등록한다.

~~~markdown
<!-- logs/2026-01-01-wiki-update.md -->
---
type: Log
title: "Wiki Update"
description: "위키 변경 이력"
timestamp: 2026-01-01
okf_version: "0.1"
---

# Wiki Update

**변경 요약** — 상세 설명:
- 추가: concepts/example.md
- 갱신: concepts/index.md, index.md
~~~

`logs/index.md`에는 logs/ 바로 아래 문서만 링크한다. 기존 루트 `log.md`만 있는 위키에서는 기존 파일을 삭제하거나 자동 이동하지 않고, 새 로그를 만들 때 전환 사실을 함께 기록한다.

## 변경 원칙

- 한 문서에는 하나의 주제를 둔다.
- 기존 내용을 삭제하거나 덮어쓰지 말고 필요한 부분만 병합한다.
- 대화에 없는 사실, 출처와 결정을 만들어내지 않는다.
- 링크 대상이 존재하는지 확인한다.
- 관련 index.md와 logs/index.md 및 로그 문서를 갱신하지 못했다면 완료로 보고하지 않는다.
- 단순히 위키를 읽거나 요약해 달라는 요청에는 이 스킬을 사용하지 말고 $wiki-read를 사용한다.
- 위키 초기화나 구조 변경 요청에는 이 스킬을 사용하지 말고 $wiki-setup을 사용한다.

## 예시

~~~text
사용자: $wiki-update 코어 루프와 난이도 결정을 기록해줘
처리:
1. wiki-path와 wiki-structure.md 확인
2. concepts/core-loop.md 또는 기존 문서 읽기
3. 내용 병합
4. concepts/index.md와 루트 index.md 갱신
5. logs/2026-01-01-core-loop-update.md 생성
6. logs/index.md에 변경 기록 링크 추가
~~~
