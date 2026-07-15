# 화면·컴포넌트 워크플로

제품의 큰 화면 구조, 페이지, 플로우 또는 컴포넌트 계획을 정리할 때 사용한다.

## 필수 읽기

먼저 압축 컨텍스트를 읽는다.

~~~bash
python3 <skill-dir>/scripts/render_context.py --path <repo>
~~~

그 다음 필요에 따라 다음 파일을 읽는다.

- design-product/manifest.json
- design-product/product-brief.md
- design-product/identity/visual-language.md
- design-product/system/design-principles.md
- design-product/system/design-tokens.json
- design-product/system/ai-anti-patterns.md
- design-product/system/layout-rules.md
- design-product/system/component-rules.md
- design-product/components/product-components.md
- design-product/patterns/의 관련 파일

## 작성 전 계획

구현을 시작하기 전에 다음 내용을 포함한 짧은 계획을 만든다.

- 화면 유형
- 사용자 목표
- 주요 행동
- 보조 행동
- 콘텐츠 계층
- 레이아웃 패턴
- 사용할 제품 컴포넌트
- 제품 컴포넌트 내부에서 사용할 원시 컴포넌트
- 명시적으로 사용하지 않을 컴포넌트와 패턴
- 안티패턴 위험과 완화 방법

아주 작은 작업은 계획을 짧게 해도 되지만 계획 자체는 생략하지 않는다.

## 디자인 제약

- design-product 토큰 또는 기존 프로젝트 토큰을 사용한다.
- 토큰 파일 밖에서 원시 hex를 사용하지 않는다.
- 카드 안에 카드를 넣지 않는다.
- 모든 섹션을 떠 있는 카드로 만들지 않는다.
- 정체성이 명시적으로 허용하지 않는 한 장식용 그라디언트, 글래스모피즘, 큰 소프트 그림자와 과도한 radius를 피한다.
- Powerful Features, Everything You Need, 가짜 후기와 가짜 수치 같은 일반적인 문구를 피한다.
- 고정 형식 UI에는 안정적인 반응형 치수를 사용한다.
- UI 문구는 제품에 맞게 구체적으로 작성한다.
- 제품 컴포넌트 이름은 시각적 컨테이너가 아니라 도메인 개념으로 정한다.

## 제품 컴포넌트 규칙

원시 UI 이름이 제품 언어를 결정하게 하지 않는다.

약한 예:

~~~tsx
<Card>
  <CardHeader>Private Van</CardHeader>
  <CardContent>...</CardContent>
</Card>
~~~

강한 예:

~~~tsx
<TransportRouteSummary
  origin="인천공항"
  destination="서울 호텔"
  vehicle="전용 밴"
/>
~~~

TransportRouteSummary 내부에서 원시 Card를 사용할 수는 있다.

## 마무리

큰 화면 구조를 확정한 뒤 중요한 결정은 memory에 추가한다. 기존 GUI의 세부 개선은 `$design-audit`, Figma 구현은 `$figma-design`으로 넘긴다.
