# design-product 체계 초기화

**별도 `design-product/` 운영 체계의 초기화를 요청한 경우에만 사용한다. 기존 DESIGN.md가 기준이면 해당 문서를 갱신한다.**

1. `python3 <skill-dir>/scripts/init_design_product.py --path <repo>`를 실행하고 탐색 결과와 생성된 `design-product/manifest.json`을 확인한다.
2. 사용자·제품 목표·주요 행동과 기존 브랜드 자료로 `product-brief.md`, `identity/positioning.md`, `identity/visual-language.md`, `identity/anti-identity.md`를 채운다. 모르는 내용은 미확정으로 남긴다.
3. 기존 UI 스택·토큰·컴포넌트를 매핑하고 정보 구조를 정한다. 부족한 제품 컴포넌트는 실제 화면에 필요한 만큼 제안한다.
4. 초기 기준과 코드의 관계, 결정된 내용과 남은 질문을 정리한다. 별도 기억 기록은 요청받은 경우에만 남긴다.

제품 맥락이 부족하면 결과를 바꿀 질문만 한다: 제품의 목적·사용자, 대안과의 차이, 주요 행동, 유지할 브랜드·참고 자료, 피할 패턴. 질문 목록 전체를 고정 인터뷰로 요구하지 않는다.
