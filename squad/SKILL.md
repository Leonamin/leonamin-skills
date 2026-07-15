---
name: squad
description: "복잡하거나 중요한 작업을 Planner, Read-only Architect, Executor, Reviewer 역할로 나누어 계획·구현·검증·리뷰한다. 사용자가 중요한 작업, 구현 위임, 여러 에이전트, 병렬 작업, 설계 검토, read-only 리뷰, evidence, handoff 또는 reviewer report를 요청할 때 사용한다. 하위 에이전트에는 특정 모델명을 강제하지 않고 프로젝트와 작업에서 정한 역량·effort·비용 정책을 전달한다."
---

# Squad 오케스트레이터

## 목적

복잡하거나 위험한 작업을 명확한 역할, 작업 범위, 검증 증거와 리뷰 단계로 나누어 진행한다. 모든 작업에 하위 에이전트를 쓰는 것이 목적은 아니다.

현재 세션은 Planner다. Planner가 범위, 완료 조건, 역할 배정, 통합, 검증과 최종 보고를 책임진다.

## 핵심 원칙

- 대상 저장소의 로컬 규칙을 먼저 확인하고 따른다.
- Architect와 Reviewer는 읽기 전용으로 유지한다.
- Executor마다 파일·모듈·워크트리 단위의 좁은 소유 범위를 준다.
- 수정 범위가 겹치는 작업은 동시에 실행하지 않는다. 통합이 필요하면 Planner가 직접 조정한다.
- 승인된 범위 밖의 파일을 수정하도록 요청하지 않는다.
- 검증 증거를 만들고 확인하기 전에는 작업을 완료로 표시하지 않는다.
- 저장소의 `AGENTS.md`, `CLAUDE.md` 또는 기타 로컬 규칙이 이 스킬보다 강하면 로컬 규칙을 우선한다.

## 모델·effort·비용 정책

하위 에이전트 호출문에 특정 모델명을 하드코딩하지 않는다. 모델 이름이나 최신 여부만으로 지능·품질·비용을 판단할 수 없고, 도구마다 지원하는 모델과 effort 값도 다르다.

호출에는 다음과 같은 추상적인 작업 계약만 전달한다.

- `model_id`: 프로젝트 정책 파일에서 읽은 고정 모델 ID. 스킬 본문에 하드코딩하지 않는다.
- `capability`: `balanced`, `quality`, `critical` 중 하나
- `effort_ceiling`: `low`, `medium`, `high`, `xHigh` 중 하나
- `cost_ceiling`: `normal` 또는 `approved`

의미는 다음과 같다.

- `balanced`: 일반적인 구현과 분석에 사용하는 기본 수준
- `quality`: 프로젝트 정책에서 허용한 더 높은 품질 프로필. 자동으로 최신 또는 최고가 모델을 뜻하지 않는다.
- `critical`: 장애, 보안, 데이터, 배포처럼 실패 비용이 큰 작업에만 사용한다. 작업별 명시적 선택과 비용 승인이 필요하다.
- `effort_ceiling`: 해당 작업에서 허용하는 최대 추론 effort다. 도구가 지원하지 않으면 요청값을 무시하지 말고 실제 적용 여부를 보고한다.
- `cost_ceiling`: `normal`이면 프로젝트가 허용한 일반 비용 범위를 넘기지 않는다. `approved`는 이번 작업에서 별도 승인을 받은 경우에만 사용한다.

기본값은 `balanced / medium / normal`이다. `quality`, `critical`, `high`, `xHigh`를 자동으로 선택하지 않는다. 새로운 `Ultra` 같은 모델·effort 등급이 생겨도 프로젝트 정책에 명시되지 않았거나 비용 범위를 확인할 수 없으면 자동으로 사용하지 않고, 안전한 기본값으로 낮추거나 사용자에게 확인한다.

## 프로젝트별 에이전트 정책

반복 가능한 팀 규칙은 대상 프로젝트의 `.agents/agent-policy.md`에 둔다. 모델 이름이 아니라 프로필, 고정된 모델 ID, effort 상한, 비용 상한과 역할별 기본값을 기록한다. 역할별 지시문이 필요하면 `.agents/roles/planner.md`, `.agents/roles/architect.md`, `.agents/roles/executor.md`, `.agents/roles/reviewer.md`처럼 별도 파일로 둔다. API 키나 비밀 값은 저장하지 않는다.

### 최초 실행 시 정책 초기화

작업을 시작할 때 프로젝트 루트의 `.agents/agent-policy.md`를 먼저 찾는다.

- 파일이 있으면 읽고 유효성을 확인한다. 매번 모델을 다시 묻지 않는다.
- 파일이 없으면 사용자에게 한 번에 다음을 묻는다: 사용할 AI 도구, 고정 모델 ID, 기본 effort 상한, 비용 상한, 역할별 예외 설정.
- 사용자 답변을 받은 뒤 확인을 거쳐 `.agents/agent-policy.md`를 생성한다.
- 초기 정책을 만든 뒤에는 해당 파일을 기준으로 사용한다. 이번 작업에만 다른 모델이나 effort가 필요하면 파일을 덮어쓰지 말고 일회성 override로 전달한다.
- 고정 모델 ID가 현재 도구에서 제공되지 않으면 다른 모델로 자동 승격하지 말고 사용자에게 대체 모델을 확인한다.

Architect에 `xHigh`를 사용하려면 정책 파일에 명시적으로 기록한다. 도구가 `xHigh`를 다른 대소문자로 요구하면 파일에는 도구가 요구하는 정확한 값을 기록하되, 이 스킬의 예시 표기는 `xHigh`로 통일한다.

예시:

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

1. 이번 작업 요청에 명시한 일회성 설정
2. 프로젝트의 `.agents/agent-policy.md`
3. 조직 또는 도구의 전역 정책
4. 이 스킬의 안전 기본값

정책 파일이 없으면 최초 실행 절차로 사용자에게 확인한다. 파일 형식이 불명확하면 모델·effort·비용을 추측하지 말고 다시 확인한다. 잘못된 값을 임의로 가장 비싼 옵션으로 해석하지 않는다.

## Hook 사용 원칙

Hook은 프로젝트 정책을 자동으로 읽어 간단한 에이전트 호출 문맥으로 변환하는 보조 수단으로 사용할 수 있다. 다만 hook은 AI 도구마다 형식과 실행 시점이 달라 이 스킬의 필수 전제가 아니다.

- hook은 프로젝트 루트를 안전하게 찾고 허용된 정책·역할 파일만 읽는다.
- 임의의 파일을 전부 프롬프트에 주입하지 말고, 선택된 역할에 필요한 내용만 전달한다.
- hook이 모델을 직접 고르기보다 정책을 검증하고 고정 `model_id`, `capability`, `effort_ceiling`, `cost_ceiling`을 출력하게 한다.
- 정책이 없거나 검증에 실패한 경우 일반 작업은 안전 기본값으로, 고위험 작업은 사용자 확인으로 처리한다.
- hook이 실제로 선택된 모델·effort·비용을 확인할 수 없다면 그렇게 보고하고, 선택이 적용되었다고 주장하지 않는다.

## 시작하기

작업을 배정하기 전에 다음을 확인한다.

~~~bash
git branch --show-current
git status --short --branch
git worktree list
rg --files -g 'AGENTS.md' -g 'CLAUDE.md' -g 'README.md' -g 'docs/**' -g '.agents/**'
~~~

사용자가 제공한 이슈, 티켓, 계약, 명세 또는 PR 링크도 확인한다. 브랜치명, 워크트리 위치, 패키지 관리자, 테스트 명령과 산출물 경로를 추측하지 말고 저장소에서 확인한다.

## 워크플로 선택

다음처럼 작고 명확한 작업은 현재 세션에서 직접 처리한다.

- 질문 또는 분석만 필요한 작업
- 문서 오탈자 수정
- 동작이 분명한 단일 파일 수정
- 실패 영향이 작고 검증이 쉬운 로컬 변경

다음 중 하나라도 해당하면 역할을 분리한다.

- 사용자가 squad, sub-agent, 역할 분리, 위임, 병렬 작업, Architect, Executor 또는 Reviewer를 요청했다.
- 데이터, 인증, 결제, 권한, 배포, 마이그레이션, 인프라 또는 운영 동작을 건드린다.
- 여러 앱, 패키지, 서비스, 저장소 또는 담당 영역에 걸친다.
- 티켓, 계약, acceptance criteria 또는 중요한 명세를 만족해야 한다.
- UI 변경에 스크린샷, 브라우저 검증 또는 사용자 흐름 검증이 필요하다.
- 사용자가 중요, 긴급, 위험, 증거 또는 리뷰 보고서를 명시했다.

자세한 판단 기준은 `references/decision-rules.md`를 읽는다.

## 표준 워크플로

1. **범위 수집**
   - 목표, 비목표, 제약, 허용·금지 범위, 검증 명령, 완료 조건을 정리한다.
   - 저장소 규칙과 작업을 통제하는 티켓·명세·계약을 확인한다.
2. **계획 게이트**
   - 고위험 작업이면 간단한 계약을 만들거나 기존 계약을 찾는다.
   - 목표, 비목표, 범위, 검증, 증거, 승인 기준을 포함한다.
   - 요청이 계약이나 규칙과 충돌하면 멈추고 확인한다.
3. **Architect 검토**
   - 설계 위험, 낯선 패턴 또는 영향 범위가 크면 읽기 전용 Architect를 사용한다.
   - 구현 형태, 기존 패턴, 위험, 예상 파일과 검증 계획을 요청한다.
   - Architect가 파일을 수정하거나 포맷터·커밋·장기 실행 서비스를 시작하게 하지 않는다.
4. **실행**
   - 범위와 소유권이 정해진 뒤에만 구현을 배정한다.
   - 강하게 결합된 작업은 Executor 하나를 사용한다.
   - 여러 Executor는 수정 범위가 서로 겹치지 않을 때만 사용한다.
   - 각 Executor에게 변경 파일, 검증 명령과 결과, 남은 위험을 보고하게 한다.
5. **리뷰**
   - 중요·위험·UI·PR 대상 작업이나 사용자가 리뷰를 요청한 작업에는 읽기 전용 Reviewer를 사용한다.
   - 계약, 저장소 규칙, diff, 테스트, 스크린샷과 증거를 기준으로 리뷰한다.
   - 차단 수준의 발견 사항은 완료 전에 Planner 작업으로 되돌린다.
6. **완료**
   - 필요한 산출물이 있고 검증이 실제로 실행되었는지 확인한다.
   - 최종 상태, 변경 파일, 테스트, 증거, 리뷰 결과와 남은 위험을 보고한다.

산출물 기준은 `references/artifacts.md`, 역할별 복사 가능한 프롬프트는 `references/role-prompts.md`를 읽는다.

## 하위 에이전트 규칙

- 사용자가 요청했거나 작업 위험이 오버헤드를 정당화할 때만 하위 에이전트를 사용한다.
- 숨겨진 결론을 사실처럼 전달하지 말고 원본 작업 맥락, 경로, 제약과 출력 형식을 전달한다.
- 읽기 전용 역할은 읽기 전용으로 유지하고 파일 변경이 없었는지 확인한다.
- 각 Executor에 작업 디렉터리, 브랜치·워크트리, 허용·금지 범위와 검증 명령을 명시한다.
- 모든 역할에 이번 작업의 에이전트 정책과 비용 상한을 전달한다.
- 같은 광범위한 프롬프트를 여러 에이전트에게 보내지 않는다. 독립적인 검토가 목적일 때만 동일한 자료를 사용한다.
- 에이전트가 돌아온 뒤 파일시스템, diff와 명령 출력으로 보고 내용을 확인한다.

## 참고 파일

- `references/decision-rules.md`: 역할 분리, 생략, 중단과 모델 정책 기준
- `references/artifacts.md`: 계약, 증거, 리뷰와 인계 산출물
- `references/role-prompts.md`: Architect, Executor, Reviewer와 인계용 프롬프트
