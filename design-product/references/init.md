# 초기화 워크플로

scripts/init_design_product.py를 실행한 뒤 사용한다.

## 목표

기존 UI 스택을 교체하지 않고 저장소 안에 디자인 운영 레이어를 초기화한다. 시작은 제품 정체성과 IA를 확인하느라 느려질 수 있지만, 이후 AI 디자인 작업의 안전성과 일관성을 높이는 것이 목표다.

정체성을 먼저 정하고, 시각화 전에 IA를 만들며, 원시 컴포넌트보다 제품 컴포넌트를 우선하고, 중요한 결정 후 memory를 갱신한다.

## 절차

1. 스크립트가 출력한 프로젝트 탐색 결과를 확인한다.
2. design-product/manifest.json을 연다.
3. 사용자가 제품 맥락을 제공하면 다음 파일을 채우거나 다듬는다.
   - design-product/product-brief.md
   - design-product/identity/positioning.md
   - design-product/identity/visual-language.md
   - design-product/identity/anti-identity.md
4. 모르는 내용은 TBD 또는 낮은 확신 메모로 남긴다. 확실한 척하지 않는다.
5. 프로젝트에 이미 UI 시스템이 있으면 원시 레이어로 매핑한다.
6. 제품 컴포넌트가 없다면 화면을 만들기 전에 제품 특화 컴포넌트 3~7개를 제안한다.
7. 초기 설정이 끝나면 다음 작업에 넘길 수 있도록 제품 정체성, IA, 토큰과 컴포넌트 결정을 정리한다.

## 브랜드 인터뷰

현재 작업에 필요한 질문만 한다. 전체 인터뷰를 요청받지 않았다면 질문을 모두 쏟아내지 않는다.

1. 제품을 한 문장으로 설명하면 무엇인가?
2. 대안보다 사용자가 이 제품을 선택해야 하는 이유는 무엇인가?
3. 이 제품은 명확히 무엇이 아닌가?
4. 첫 화면에서 어떤 감정을 만들어야 하는가?
5. 어떤 디자인 레퍼런스는 허용하고 무엇은 복사하면 안 되는가?
6. 주요 전환 행동은 무엇인가?
7. 어디에서 인터페이스가 신뢰를 만들어야 하는가?
8. 어떤 일반적인 AI UI 패턴을 피해야 하는가?

## 권장 저장소 형태

design-product/는 영속적인 디자인 기억 레이어다. 가장 중요한 파일은 다음과 같다.

- manifest.json
- product-brief.md
- identity/visual-language.md
- system/design-tokens.json
- system/ai-anti-patterns.md
- system/component-rules.md
- system/layout-rules.md
- components/product-components.md
- memory/current-design-state.md
- memory/decision-log.md

사용자에게 요청받지 않은 추가 사용자 문서는 만들지 않는다.
