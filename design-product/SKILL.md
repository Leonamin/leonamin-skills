---
name: design-product
description: "프로젝트의 제품 정체성과 디자인 시스템을 처음 구축하거나 크게 다시 설계할 때 사용한다. 제품 브리프, 디자인 토큰, 제품 컴포넌트, 레이아웃 규칙, 디자인 거버넌스와 저장소 기반 기억을 초기화·재정의한다. 기존 GUI의 세부 조정에는 $design-audit, Figma 구현에는 $figma-design을 사용한다."
---

# 제품 디자인 시스템

## 역할

프로젝트를 디자인 가능한 제품 시스템으로 초기화하거나 큰 방향을 다시 세운다.

- 제품 정체성과 포지셔닝
- 정보 구조와 핵심 사용자 흐름
- 디자인 토큰과 시각 언어
- 제품 맥락을 가진 컴포넌트
- 레이아웃과 콘텐츠 규칙
- 디자인 변경 제안·결정·기억

이 스킬은 저장소 안에 지속되는 디자인 운영 기반을 만든다. 대화 기억은 임시적이며 프로젝트의 진실의 원천이 아니다.

## 다른 디자인 스킬과의 경계

- 기존 GUI를 세밀하게 검토하거나 작은 범위로 개선: $design-audit
- 디자인 시스템과 감사 결과를 바탕으로 Figma에서 구현: $figma-design
- 단순한 CSS 한 줄 수정이나 제품 맥락이 없는 임시 화면: 필요한 규칙만 읽고 이 스킬의 전체 초기화는 실행하지 않는다.

의존 방향은 다음과 같다.

~~~text
design-product ──────┐
                     ├→ figma-design
design-audit ────────┘
~~~

실제 사용에서는 design-audit과 figma-design이 design-product의 결과물을 읽는다. design-product 자체는 Figma나 특정 디자인 도구를 필수로 요구하지 않는다.

## 주요 작업

다음 작업에는 이 스킬을 사용한다.

- 새 프로젝트의 제품 정체성과 디자인 운영 기반 초기화
- 기존 디자인 시스템을 큰 방향으로 재정의
- 여러 화면에 걸쳐 사용할 토큰과 제품 컴포넌트 설계
- 제품의 핵심 IA와 사용자 흐름 재구성
- 디자인 시스템의 변경 제안과 채택 여부 기록
- 세션이 바뀌어도 유지해야 할 디자인 결정과 금지 패턴 정리

## 첫 단계

스크립트 경로는 이 SKILL.md를 기준으로 해석한다.

- 새 프로젝트 설정: scripts/init_design_product.py --path <repo> 실행 후 references/init.md 읽기
- 기존 design-product/ 사용: 작업 전에 scripts/render_context.py --path <repo> 실행
- 디자인 시스템 논의·변경: references/design-system.md를 읽고 scripts/propose_design_change.py로 제안 기록
- 작은 화면·컴포넌트 개선: 직접 구현하지 말고 필요하면 $design-audit으로 넘긴다.
- 디자인 기억 업데이트: scripts/update_memory.py --path <repo> 사용 후 references/memory.md 읽기

## 권장 흐름

1. **프로젝트와 제품 맥락 확인**
   - 기존 UI 스택, 주요 사용자, 제품 목적과 현재 디자인 문제를 확인한다.
2. **정체성 정의**
   - 제품 브리프, 포지셔닝, 시각 언어와 반정체성 규칙을 정리한다.
3. **IA와 제품 컴포넌트 계획**
   - 화면을 만들기 전에 사용자 목표, 주요 행동, 콘텐츠 계층과 제품 컴포넌트를 정의한다.
4. **시스템화**
   - 토큰, 컴포넌트 계약, 레이아웃과 콘텐츠 규칙을 저장소에 기록한다.
5. **변경 승인**
   - 큰 변경은 2~3개 선택지와 트레이드오프를 제시하고, 승인된 범위만 적용한다.
6. **인계**
   - 세부 GUI 조정은 $design-audit으로, Figma 구현은 $figma-design으로 넘길 수 있도록 결과물과 결정 사항을 정리한다.

## 필수 운영 규칙

- 모든 디자인 시스템 작업 전에 design-product/manifest.json을 읽는다. 아직 없으면 초기화 명령을 먼저 실행한다.
- 작업과 관련된 진실의 원천 파일만 읽는다.
- IA·컴포넌트 계획을 만들기 전에는 UI 코드를 수정하지 않는다.
- 원시 UI 조합보다 제품 맥락을 가진 컴포넌트를 우선한다.
- shadcn, Radix, MUI, Chakra, Tailwind 같은 라이브러리는 원시 재료이지 제품의 디자인 언어 자체가 아니다.
- 기존 프로젝트 관례를 따르되, 명시된 하드 룰과 충돌하면 충돌을 설명한다.
- 가짜 후기, 수치, 브랜드, 목적지, 인증·규정 준수 주장과 신뢰 표식을 만들지 않는다.
- 실제 제품이 SaaS가 아니라면 일반적인 SaaS 페이지 구조를 사용하지 않는다.
- 오래 유지할 결정은 design-product/memory/에 기록한다.
- 사용자가 논의 중인 변경은 제안과 결정이 분명해지기 전까지 적용하지 않는다.
- 디자인 감사와 시각적 검증은 별도 스킬의 책임으로 구분하고, 필요한 경우 결과를 인계한다.

## 명령

초기화:

~~~bash
python3 <skill-dir>/scripts/init_design_product.py --path .
~~~

압축 컨텍스트 렌더링:

~~~bash
python3 <skill-dir>/scripts/render_context.py --path .
~~~

디자인 시스템 변경 제안:

~~~bash
python3 <skill-dir>/scripts/propose_design_change.py --path . \
  --type component \
  --title "일반 제품 카드를 RouteSummary로 교체" \
  --problem "운송 상세 페이지가 원시 Card 조합에 의존한다." \
  --option "RouteSummary를 제품 컴포넌트 경계로 만든다." \
  --recommendation "RouteSummary를 채택하고 Card는 내부 원시 컴포넌트로 둔다."
~~~

디자인 기억 추가:

~~~bash
python3 <skill-dir>/scripts/update_memory.py --path . \
  --decision "가격 중심 제품 카드에는 컴팩트한 비교 행을 사용한다." \
  --approved "운송 상세 페이지에는 route-summary 컴포넌트를 사용한다." \
  --rejected "상세 페이지 안에 마케팅 카드를 중첩하지 않는다."
~~~

## 완료 결과

의미 있는 작업은 다음을 포함해 마무리한다.

- 생성·수정한 파일
- 적용한 제품 정체성·토큰·컴포넌트·레이아웃 결정
- 추가한 디자인 기억 항목
- $design-audit 또는 $figma-design으로 넘길 후속 작업
