---
name: multi-squad
description: "여러 개의 관련 작업, N개 작업 묶음, 대량 이슈 처리, 병렬 구현, multi-task orchestration, branch/worktree per task, 중간 커밋, 통합 검증 또는 하위 작업별 squad 실행이 필요할 때 사용한다. 작업을 직접 한 번에 구현하지 않고 의존성과 충돌 가능성을 기준으로 분해하며, 각 작업마다 브랜치·워크트리·검증·에이전트 정책을 관리한다."
---

# 다중 작업 조율자

## 목적

여러 작업을 하나의 즉흥적인 구현으로 섞지 않고, 작업 단위별 브랜치, 워크트리, 범위, 진행 커밋, 검증과 리뷰를 관리한다. 이 스킬은 직접 구현자가 아니라 상위 조율자다.

현재 세션은 Multi-squad Planner다. 각 개별 작업은 대상 저장소에서 사용할 수 있는 단일 작업 오케스트레이터에게 맡긴다. 기본 후보는 `$squad`이며, 프로젝트에 더 강한 로컬 오케스트레이터가 있으면 그 스킬을 우선한다.

## 핵심 원칙

- 작업을 먼저 목록화하고 의존 관계와 실행 순서를 나눈다.
- 작업 1개마다 브랜치와 워크트리를 하나씩 만든다.
- 브랜치는 사람이 진행 상황을 추적하는 단위다.
- 워크트리는 병렬 작업을 격리하는 기본 실행 단위다.
- 같은 파일 또는 모듈을 수정하는 작업은 병렬로 실행하지 않는다.
- 작업별 커밋을 의미 있는 진행 단위로 남긴다.
- 각 작업은 선택된 단일 작업 오케스트레이터의 규칙을 따른다.
- 통합 전에 작업별 검증 결과, diff, 커밋 로그와 남은 위험을 확인한다.
- 프로젝트 로컬 규칙이 이 스킬보다 강하면 로컬 규칙을 우선한다.

## 에이전트 정책과 비용 제어

하위 작업마다 특정 모델명을 고르지 않는다. 모델 이름이나 최신 여부는 지능을 보장하지 않고, 도구마다 모델·effort 옵션이 다르기 때문이다. 대신 각 작업에 다음 계약을 전달한다.

- `model_id`: 프로젝트 정책 파일에서 읽은 고정 모델 ID 또는 역할별 override
- `capability`: `balanced`, `quality`, `critical`
- `effort_ceiling`: `low`, `medium`, `high`, `xHigh`
- `cost_ceiling`: `normal`, `approved`

기본값은 모든 작업에서 `balanced / medium / normal`이다. Architect와 Reviewer에 더 높은 품질이 필요하면 프로젝트 정책이나 이번 작업의 명시적 override로 지정한다. 현재 권장 역할 기본값은 Architect `quality / xHigh / approved`, Reviewer `quality / high / normal`, Executor `balanced / medium / normal`이다. `critical` 또는 `approved`는 실패 비용과 비용 승인을 확인한 작업에만 사용한다.

새로운 `Ultra` 같은 모델·effort 등급이 생겨도 자동으로 가장 비싼 선택으로 올라가지 않는다. 프로젝트 정책에 없거나 비용 범위를 확인할 수 없는 값은 사용하지 않고, 안전 기본값으로 낮추거나 사용자에게 확인한다. 실제 도구가 선택한 모델과 effort를 확인할 수 없다면 그 사실을 보고한다.

반복 가능한 정책은 대상 프로젝트의 `.agents/agent-policy.md`에 둔다. 모델 ID, effort 상한, 비용 상한과 역할별 기본값을 기록하고 API 키나 비밀 값은 저장하지 않는다. 역할별 지시문은 필요할 때 `.agents/roles/` 아래에 둔다.

### 최초 실행 시 정책 초기화

작업을 시작할 때 프로젝트 루트의 `.agents/agent-policy.md`를 찾는다.

- 파일이 있으면 읽고 유효성을 확인한 뒤 모델을 다시 묻지 않는다.
- 파일이 없으면 사용자에게 사용할 AI 도구, 고정 모델 ID, 기본 effort 상한, 비용 상한과 역할별 예외를 한 번에 묻는다.
- 답변을 확인한 뒤 정책 파일을 만들고, 이후 모든 하위 작업에서 같은 정책을 재사용한다.
- 특정 하위 작업만 다른 설정을 써야 하면 정책 파일을 수정하지 말고 해당 작업의 일회성 override로 전달한다.
- 고정 모델 ID나 `xHigh`를 현재 도구가 지원하지 않으면 자동으로 더 비싼 대체값을 고르지 말고 확인한다.

~~~yaml
default:
  model: <pinned-model-id>
  capability: balanced
  effort_ceiling: medium
  cost_ceiling: normal
roles:
  architect:
    model: <pinned-model-id>
    capability: quality
    effort_ceiling: xHigh
    cost_ceiling: approved
  executor:
    capability: balanced
    effort_ceiling: medium
    cost_ceiling: normal
  reviewer:
    capability: quality
    effort_ceiling: high
    cost_ceiling: normal
~~~

설정 우선순위는 다음과 같다.

1. 이번 하위 작업의 일회성 override
2. 프로젝트의 `.agents/agent-policy.md`
3. 조직 또는 도구의 전역 정책
4. 이 스킬의 안전 기본값

## Hook 사용 원칙

Hook은 프로젝트 루트를 찾고 `.agents/agent-policy.md`와 선택된 역할 파일을 읽어 호출 문맥에 넣는 보조 수단으로 사용할 수 있다. 그러나 hook 형식은 AI 도구마다 다르므로 필수 전제로 삼지 않는다.

- hook은 허용된 파일만 읽고 임의의 프로젝트 파일을 전부 주입하지 않는다.
- hook은 모델을 직접 고르기보다 정책을 검증하고 고정 `model_id`와 추상적인 capability·effort·비용 값을 출력한다.
- hook이 없으면 조율자가 프로젝트 정책을 직접 읽어 하위 작업 프롬프트에 넣는다.
- 정책이 없으면 일반 작업은 기본값으로 진행하고, 고위험 작업은 확인 후 진행한다.
- hook이 실제 적용된 모델·effort·비용을 확인하지 못하면 적용을 주장하지 않는다.

## 시작 전 확인

대상 저장소에서 다음을 확인한다.

~~~bash
git branch --show-current
git status --short --branch
git worktree list
rg --files -g 'AGENTS.md' -g 'CLAUDE.md' -g 'README.md' -g 'docs/**' -g '.agents/**'
~~~

확인할 내용:

- 보호 브랜치와 기본 브랜치
- 브랜치명 규칙
- 워크트리 위치 규칙
- 설치된 단일 작업 오케스트레이터
- 프로젝트별 에이전트 정책과 역할 파일
- 테스트, lint, build 명령
- 기존 진행 중 워크트리와 충돌 가능성

## 작업 분해

먼저 작업 목록을 표로 정리한다.

~~~markdown
| ID | 목표 | 의존성 | 예상 수정 범위 | 브랜치 | 워크트리 | 오케스트레이터 | 에이전트 정책 | 상태 |
|---|---|---|---|---|---|---|---|---|
~~~

분해 규칙:

- 하나의 작업은 하나의 명확한 완료 조건을 가진다.
- 같은 파일 또는 모듈을 많이 건드리는 작업은 순차 처리한다.
- 선행 스키마, 타입, 공통 유틸과 마이그레이션 작업은 먼저 수행한다.
- UI, API, 문서와 테스트처럼 수정 범위가 분리되면 병렬 후보로 둔다.
- 의존성이 불명확하면 Architect 또는 읽기 전용 분석 작업을 먼저 둔다.
- 각 작업의 위험과 비용에 따라 에이전트 정책을 명시한다. 전체 작업을 일괄적으로 최고 effort로 올리지 않는다.

## 브랜치와 워크트리 규칙

각 작업마다 다음을 만든다.

- 브랜치: 사람이 추적하기 쉬운 이름을 사용한다.
- 워크트리: 병렬 실행과 파일 격리를 위한 실제 작업 디렉터리로 사용한다.

일반 패턴:

~~~bash
git switch <base-branch>
git pull --ff-only
git worktree add <worktree-path> -b <branch-name> <base-branch>
~~~

주의:

- 대상 저장소의 로컬 규칙이 워크트리 위치나 환경 동기화 명령을 지정하면 그대로 따른다.
- 이미 존재하는 워크트리를 재사용하려면 작업 범위와 현재 변경 상태를 먼저 확인한다.
- 다른 작업자의 변경을 되돌리지 않는다.

## 단일 작업 오케스트레이터 호출

각 작업은 다음 정보를 포함해 하위 오케스트레이터에 맡긴다.

~~~markdown
Use $<single-work-orchestrator> for this task.

Task ID:
Goal:
Working directory:
Branch:
Allowed files:
Forbidden files:
Dependencies:
Expected commits:
Verification commands:
Evidence required:
Agent policy:
- Model ID: {pinned-model-id-or-role-override}
- Capability profile: {balanced|quality|critical}
- Effort ceiling: {low|medium|high|xHigh}
- Cost ceiling: {normal|approved}
- Policy source: {task override|project|global|default}
Handoff format:
~~~

하위 오케스트레이터 선택:

- 프로젝트 전용 오케스트레이터가 있으면 우선 사용한다.
- 없으면 `$squad`를 사용한다.
- 단순 작업은 현재 세션이 직접 처리할 수 있지만, 그래도 브랜치와 워크트리 단위는 유지한다.

## 커밋 전략

- 작업별로 의미 있는 진행 단위마다 커밋한다.
- 커밋 전에는 staged diff를 확인한다.
- 커밋 메시지는 대상 저장소의 규칙을 따른다.
- 한 작업의 모든 변경을 마지막에 하나로 몰아 커밋하지 않는다.
- 깨진 상태를 의도적으로 커밋하지 않는다. 장기 작업에서 checkpoint 커밋이 필요하면 메시지와 상태를 명확히 남긴다.

좋은 커밋 단위:

- 기반 타입, schema와 migration 추가
- API 또는 서비스 로직 구현
- UI 연결
- 테스트 추가
- 문서 갱신
- 리뷰 피드백 반영

## 진행 관리

현재 세션은 다음 표를 계속 갱신한다.

~~~markdown
| ID | Branch | Worktree | Latest commit | Policy | Verification | Blockers | Next |
|---|---|---|---|---|---|---|---|
~~~

작업 간 조율 규칙:

- 한 작업의 결과가 다른 작업의 입력이면 후속 작업 시작 전에 base를 업데이트하거나 cherry-pick·merge 전략을 명시한다.
- 병렬 작업이 같은 파일을 수정하려 하면 즉시 순차 처리로 바꾼다.
- 공통 기반 변경은 별도 선행 작업으로 분리한다.
- 충돌 해결은 현재 세션이 통합 책임자로 수행하거나 명시적으로 한 작업에 배정한다.

## 통합과 완료

작업별 완료 조건:

- 변경 범위가 계약 또는 작업 목표와 일치한다.
- 필요한 커밋이 작업 브랜치에 남아 있다.
- 검증 명령이 실제로 실행됐다.
- 에이전트 정책과 실제 적용 가능 여부가 기록됐다.
- 남은 위험과 후속 작업이 기록됐다.

전체 완료 조건:

- 모든 작업의 상태가 완료, 보류 또는 명시적 제외로 분류됐다.
- 통합 브랜치가 필요하면 통합 순서와 충돌 해결 기록이 남았다.
- 전체 검증 명령이 실행됐다.
- 사용자에게 브랜치, 워크트리, 커밋, 검증 결과와 남은 위험을 보고했다.

## 금지 사항

- N개 작업을 하나의 브랜치에서 섞어 진행하지 않는다.
- 워크트리 없이 병렬 작업을 시작하지 않는다.
- 파일 소유권이 겹치는 하위 작업을 동시에 실행하지 않는다.
- 검증하지 않은 작업을 완료로 표시하지 않는다.
- 하위 오케스트레이터의 로컬 승인 규칙을 임의로 우회하지 않는다.
- 프로젝트 정책이 없는 상태에서 모든 하위 작업을 최고 모델 또는 최고 effort로 자동 승격하지 않는다.
