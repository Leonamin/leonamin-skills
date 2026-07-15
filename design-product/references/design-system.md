# 디자인 시스템 변경 흐름

토큰, 컴포넌트, 패턴, 시각 언어, 레이아웃과 코드 매핑을 논의·수정·추가·삭제·이름 변경하거나 관리할 때 사용한다.

## 기본 규칙

논의와 구현을 구분한다. 사용자가 탐색하거나 결정하는 중이면 결정이 명시되기 전까지 제품 UI 또는 토큰 파일을 수정하지 않는다.

## 필수 읽기

압축 컨텍스트를 렌더링한다.

~~~bash
python3 <skill-dir>/scripts/render_context.py --path <repo>
~~~

그 다음 변경 유형에 맞는 파일을 읽는다.

- 정체성 변경: product-brief.md, identity/*
- 토큰 변경: system/design-tokens.json, system/token-taxonomy.md
- 컴포넌트 변경: components/product-components.md, components/component-contracts.json, system/component-rules.md
- 레이아웃·패턴 변경: system/layout-rules.md, patterns/*
- 거버넌스 변경: system/change-workflow.md, memory/design-system-proposals.md

## 변경 흐름

1. 변경 유형을 분류한다.
   - identity
   - token
   - component
   - pattern
   - layout
   - code-mapping
   - governance
2. 문제를 제품 관점의 언어로 표현한다.
3. 영향을 받는 파일과 코드 컴포넌트를 확인한다.
4. 트레이드오프가 있는 2~3개 선택지를 제시한다.
5. 하나를 권장한다.
6. scripts/propose_design_change.py로 제안을 기록한다.
7. 사용자가 아직 결정 중이면 기다린다.
8. 승인된 범위만 적용한다.
9. 승인된 변경을 적용한다.
10. memory와 제안 상태를 갱신하고, 세부 GUI 감사가 필요하면 `$design-audit`으로 넘긴다.

## 컴포넌트 변경 명세

제품 컴포넌트 제안에는 다음을 정의한다.

- 목적
- 사용할 때
- 사용하지 않을 때
- 구성
- 콘텐츠 모델
- 상태와 변형
- 토큰 연결
- 레이아웃 동작
- 접근성 요구사항
- 코드 매핑
- 안티패턴

## 토큰 변경 명세

토큰 제안에는 다음을 정의한다.

- 의미상 역할
- 교체·확장할 기존 토큰
- 영향을 받는 컴포넌트
- 허용 값
- 금지된 일회성 값
- 코드 매핑
- 마이그레이션 메모

## 결정 상태

- Proposed: 기록되었지만 채택하지 않음
- Accepted: 진실의 원천 파일과 memory에 적용
- Rejected: 거부 이유를 기록
- Deferred: 알려진 질문으로 유지

## 응답 형식

디자인 시스템 논의에는 다음 형식을 사용한다.

~~~text
변경 유형
component

문제
현재 제품 카드가 원시 Card 조합이라 제품 언어로 재사용되지 않는다.

선택지
1. 이름만 바꾼다.
2. 제품 컴포넌트 경계를 만든다.
3. 전체 패턴을 다시 설계한다.

권장
2번.

영향 파일
- design-product/components/product-components.md
- design-product/components/component-contracts.json
- 관련 UI 컴포넌트 파일

결정 필요
구현 전에 2번을 채택할지 확인한다.
~~~

사용자가 직접 구현을 요청하면 결정을 수락한 것으로 보고 변경과 memory 갱신까지 진행한다. 기존 GUI의 세부 검토는 `$design-audit`, Figma 구현은 `$figma-design`으로 넘긴다.
