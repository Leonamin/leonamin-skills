---
name: conversation-snapshot
description: Export the current conversation as a structured Markdown state snapshot for continuation by another person, AI, session, or project. Use when the user asks for a conversation snapshot, context handoff, context summary, 대화 요약, 컨텍스트 저장, or 이어서 작업할 수 있는 인수인계 문서. Do not use for an ordinary short summary.
---

# Conversation Snapshot

현재 대화를 단순 요약이 아닌, 다른 사람이나 AI가 작업을 이어갈 수 있는 상태 문서로 재구성한다.

## 원칙

- Markdown으로 작성하고 시간순 나열보다 목표·논의·결정·현재 상태의 논리적 흐름을 우선한다.
- 잡담과 중복은 제거하되, 중요한 아이디어와 폐기된 이유는 보존한다.
- 확정된 사실, 가능성이 높은 판단, 검증되지 않은 가정을 구분한다.
- 완료된 일과 남은 일을 혼동하지 않는다.
- 대화에 없는 사실이나 근거를 만들지 않는다.
- 정보가 없는 필수 항목은 삭제하지 말고 `없음` 또는 `미논의`로 표시한다.
- 기본적으로 응답에 Markdown을 출력한다. 사용자가 요청한 경우에만 파일로 저장한다.

## 출력 형식

# Conversation Snapshot

## Objective
대화의 궁극적인 목표.

## Current State
현재까지 완료·확인된 내용과 남은 작업.

## Executive Summary
전체 상태를 5~10줄로 요약.

## Conversation Flow
주요 단계별로 `질문 → 논의 → 결론 → 다음 단계로 이어진 이유`를 정리. 모든 발화를 나열하지 않는다.

## Knowledge Gained
각 항목에 `[Confirmed]`, `[Likely]`, `[Assumption]` 중 하나를 표시.

## Ideas
의미 있는 아이디어마다 다음을 포함한다.

- 상태: `[Exploring]`, `[Candidate]`, `[Accepted]`, `[Deferred]`, `[Rejected]`
- 설명
- 장점
- 단점
- 남은 문제
- 현재 상태

## Decisions
확정된 결정마다 결정, 이유, 영향을 기록.

## Questions

### Solved
해결된 질문.

### Partially Solved
부분적으로 해결된 질문.

### Open
아직 해결되지 않은 질문.

## Assumptions
현재 가정과 아직 검증되지 않은 내용.

## Risks / Uncertainties
불확실성, 제약, 이후 문제가 될 수 있는 부분.

## Next Discussion Topics
후속 논의 항목마다 `High`, `Medium`, `Low` 우선순위를 표시.

## References
대화에 실제로 등장한 용어, 서비스, 기술, 제품, 링크, 논문, 법률, 문서.

## Context for Continuation
이 부분만 읽어도 작업을 재개할 수 있도록 목표, 결정, 현재 상태, 다음 행동을 10~20줄로 압축.

섹션 순서와 제목을 유지한다. 같은 정보가 여러 섹션에 필요하면 각 섹션의 목적에 맞게 짧게 표현하고 문장을 그대로 반복하지 않는다.
