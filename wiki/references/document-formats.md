# 문서 형식

기존 문서의 필드·날짜 형식과 프로젝트 구조 규칙을 우선한다. 아래 날짜는 실제 현재 날짜로 바꾼다.

## 일반 문서

`type`은 `Concept`, `Decision`, `Reference` 중 하나를 선택한다.

```yaml
---
type: Concept
title: "문서 제목"
description: "문서가 다루는 범위"
tags: [tag1, tag2]
timestamp: YYYY-MM-DD
---
```

ADR 본문은 필요한 결정 맥락과 결과를 다음 구조로 기록한다.

```markdown
# 001. 제목

## Context
왜 이 결정을 검토했는가.

## Decision
무엇을 선택했는가.

## Consequences
이점·비용·후속 작업.

## Status
Accepted, Superseded 또는 Proposed 중 현재 상태.
```

## 로그

```markdown
---
type: Log
title: "Wiki Update"
description: "위키 변경 이력"
timestamp: YYYY-MM-DD
okf_version: "0.1"
---

# Wiki Update

변경 요약과 설명.

- 추가: concepts/example.md
- 갱신: concepts/index.md, index.md
```
