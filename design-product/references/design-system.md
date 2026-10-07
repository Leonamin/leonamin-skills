# 기존 design-product 구조 운영

**기존 체계의 관련 기준과 코드를 함께 수정한다. 별도 제안·기억 기록은 요청받았을 때만 남긴다.**

DESIGN.md가 기준인 프로젝트에서는 아래 JSON 체계를 경쟁 기준으로 운영하지 않는다.

## 필요한 근거 읽기

컨텍스트 요약이 필요하면 `python3 <skill-dir>/scripts/render_context.py --path <repo>`를 실행하고, 변경에 해당하는 원본을 읽는다.

| 변경 | 확인할 파일 |
| --- | --- |
| 정체성 | `product-brief.md`, `identity/*` |
| 토큰 | `system/design-tokens.json`, `system/token-taxonomy.md` |
| 컴포넌트 | `components/product-components.md`, `components/component-contracts.json`, `system/component-rules.md` |
| 레이아웃·패턴 | `system/layout-rules.md`, `patterns/*` |
| 운영 정책 | `system/change-workflow.md`; 기록을 요청받았다면 `memory/design-system-proposals.md` |

경로는 프로젝트의 `design-product/` 기준이다.

## 변경

1. 문제, 영향 파일과 기존 사용처를 확인한다. 실제 선택이 필요한 경우만 대안과 권장을 제시한다.
2. 상담 중에는 제안하고, 구현 요청에는 해당 범위를 적용한다. 이미 정한 결정을 다시 승인받지 않는다.
3. 토큰·계약·코드의 일치 여부와 관련 화면을 검증한다.
4. 제안 기록을 요청받았다면 `scripts/propose_design_change.py`, 기억 갱신을 요청받았다면 [memory.md](memory.md)를 사용한다.

컴포넌트 계약에는 목적·사용 조건, 구성·콘텐츠, 상태·변형, 토큰·레이아웃, 접근성·코드 매핑 중 변경에 필요한 항목을 명시한다. 토큰 계약에는 의미·허용 값·영향 컴포넌트·코드 매핑과 필요한 마이그레이션을 명시한다.

제안 상태를 사용하는 프로젝트에서는 `Proposed`(미채택), `Accepted`(적용), `Rejected`(거부 이유), `Deferred`(보류)를 실제 결정에 맞춰 갱신한다.
