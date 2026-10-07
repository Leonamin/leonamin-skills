# 초기 파일 형식

선택한 경로·분류·인덱스 정책에 맞춰 예시를 조정한다. 기본 구조는 루트 `index.md`와 `concepts/`, `decisions/`, `references/`, `logs/` 각각의 `index.md`다.

## 프로젝트 설정

`.agents/wiki-path`는 `./wiki`처럼 경로 한 줄만 기록한다.

`.agents/wiki-structure.md` 예시:

```markdown
# Wiki Structure

- Wiki path: ./wiki
- Format: OKF v0.1 style Markdown with YAML frontmatter
- Index policy: Every wiki directory contains index.md
- Change log: ./wiki/logs/

## Directory map

- concepts/: 개념·도메인·시스템
- decisions/: 번호가 있는 ADR
- references/: 외부 자료·도구
- logs/: 날짜·주제별 변경 이력

## Rules

- 문서 하나에 한 주제를 다룬다.
- 새 문서·디렉토리는 해당 index.md에 등록한다.
- 인덱스는 바로 아래 문서와 하위 인덱스를 안내한다.
- 로그는 YYYY-MM-DD-kebab-case.md로 만들고 logs/index.md에 등록한다.
```

## 위키 frontmatter

인덱스 예시. `logs/index.md`도 같은 필드를 사용하며 제목·설명·scope를 로그에 맞춘다.

```yaml
---
type: Index
title: "Concepts"
description: "프로젝트 개념 문서의 구조와 목록"
scope: "concepts"
okf_version: "0.1"
---
```

로그 예시. `timestamp`는 실제 현재 날짜로 바꾸고 본문에 생성·변경 이유와 영향을 기록한다.

```yaml
---
type: Log
title: "Wiki Structure Update"
description: "위키 구조 변경 이력"
timestamp: YYYY-MM-DD
okf_version: "0.1"
---
```
