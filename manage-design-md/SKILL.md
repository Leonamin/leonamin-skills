---
name: manage-design-md
description: "Google Labs DESIGN.md 명세로 디자인 시스템을 생성·갱신·검증한다. 기존 제품 UI, 스크린샷, 디자인 파일, 코드, 또는 명시된 브랜드 근거에서 토큰·컴포넌트·레이아웃 규칙을 추출해 루트 DESIGN.md로 기록하고, @google/design.md lint 및 필요 시 diff를 실행할 때 사용한다. 제품의 큰 정체성·IA 재설계에는 $design-product를 함께 사용하고, 작은 기존 GUI 개선에는 $design-audit을 사용한다."
---

# Manage DESIGN.md

`DESIGN.md`를 디자인 시스템의 단일 진실 원천으로 유지한다. Google Labs 형식의 YAML front matter에는 규범적인 토큰과 컴포넌트 계약을, Markdown 본문에는 적용 이유·규칙·근거·제약을 기록한다.

## 시작 전 확인

1. 저장소 루트의 `DESIGN.md`를 먼저 읽는다. 없으면 새로 만든다.
2. 요청 범위를 확인하고, 기존 UI 코드·디자인 파일·스크린샷·명시된 URL 중 실제 근거를 수집한다.
3. 디자인 정체성이나 정보 구조를 새로 정해야 하면 `$design-product`를 함께 적용한다. 이 스킬이 근거 없이 브랜드 방향을 발명하지는 않는다.
4. Google 형식과 lint 규칙은 [references/google-design-md.md](references/google-design-md.md)를 읽는다.

## 작업 흐름

1. **근거 분류**
   - 관찰한 값: 색상, 글꼴, 크기, 간격, 반경, 컴포넌트 상태, 화면별 반복 패턴.
   - 명시된 결정: 제품 브리프나 사용자가 정한 브랜드·접근성·반응형 요구사항.
   - 미확인 사항: 추정하지 말고 `## Known Gaps`에 근거와 함께 기록한다.
2. **토큰 모델링**
   - raw 값은 YAML의 `colors`, `typography`, `rounded`, `spacing`에 한 번만 정의한다.
   - 컴포넌트는 `components`에서 토큰을 참조한다. 본문도 `{colors.ink}`, `{components.button-primary}`처럼 실제 참조를 사용한다.
   - 반복되는 상태는 `button-primary-active`처럼 별도 컴포넌트 항목으로 정의한다.
3. **문서 작성 또는 갱신**
   - YAML front matter를 파일 최상단 `---` 구분자로 유지한다.
   - 본문은 `Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts` 순서를 지킨다.
   - 필요한 경우에만 `Responsive Behavior`, `Iteration Guide`, `Known Gaps`를 뒤에 추가한다.
   - 수치, 브랜드 주장, 접근성 준수, 반응형 동작은 근거가 있을 때만 단정한다.
4. **검증**
   - `npx @google/design.md lint DESIGN.md`를 실행한다.
   - `broken-ref` 오류는 반드시 해결한다. 경고는 해결하거나, 근거상 의도된 경우에만 결과에 남긴다.
   - 이전 버전이 있고 변경 범위가 크면 `npx @google/design.md diff <before> DESIGN.md`를 실행해 의도치 않은 토큰 삭제를 확인한다.
5. **인계**
   - 변경한 토큰, 컴포넌트, 근거, lint 결과, 남은 Known Gaps를 간결히 보고한다.

## 필수 규칙

- `DESIGN.md` 외 별도 토큰 파일을 새 진실 원천으로 만들지 않는다. 구현용 산출물은 필요하면 `DESIGN.md`에서 export한다.
- 사용자가 제공하지 않은 스크린샷·URL·코드를 근거로 했다고 주장하지 않는다.
- 컴포넌트 설명으로만 값을 숨기지 않는다. 재사용되는 값은 YAML 토큰으로 올린다.
- lint가 통과해도 관찰 근거가 없는 값은 사실로 표현하지 않는다.
- `DESIGN.md` 수정만으로 UI 코드 변경을 암묵적으로 수행하지 않는다.
