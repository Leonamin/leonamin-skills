---
name: ui-before-after-sketch
description: 기존 UI의 개선안을 HTML/CSS Before·After 시안과 브라우저 캡처로 비교할 때 사용한다. 제품 소스 수정 전 시각적 합의를 위한 작업이다.
---

# UI Before/After Sketch

**확인한 현재 화면과 요청된 개선안을 같은 데이터·상태·viewport로 비교한다.**

제품 소스·디자인 시스템·데이터·배포 환경은 수정하지 않는다. 시안은 의사결정 자료이며 실제 구현이나 운영 검증 결과가 아니다.

## 진행

1. 대상·상태·viewport와 해결할 문제를 정한다. 실제 화면·스크린샷은 구조와 상태, 코드는 동작·접근성 이름, 토큰·공용 컴포넌트는 제품 일관성의 근거로 사용한다. 사용자 설명의 미확인 내용은 가정으로 구분한다. 핵심 구조를 확인할 수 없으면 필요한 근거를 요청한다.
2. Before는 확인한 데이터·문구·상태·주요 동작·정보 구조를 재현한다. After는 요청된 개선만 반영하며 데이터 의미·권한·동작을 임의로 바꾸지 않는다. 문구 개선에는 [UI 문구 절제 기준](../design-product/references/ui-copy.md)을 적용한다.
3. [시안 작성 형식](references/sketch-format.md)에 따라 HTML/CSS를 만든다. 플랫폼의 시각화 디렉터리를 사용하고 없으면 저장소 밖에 `mktemp -d`로 만든다. `assets/minimal-sketch/`를 복사해 근거로 교체하거나 제품 구조에 맞게 작성한다.
4. `agent-browser --version`을 확인하고 아래 명령으로 렌더링·캡처한다. 반응형 문제가 범위에 있으면 데스크톱·모바일을 각각 확인한다.

   ```bash
   <skill-dir>/scripts/capture_html_screenshot.sh \
     <index.html> <output.png> [width] [height] [full|viewport]
   ```

5. 캡처 이미지를 직접 확인해 잘림·overflow·겹침·비교 불균형을 수정하고 다시 캡처한다. CLI가 없거나 캡처가 실패하면 원인과 미검증 범위를 알리고 검증되지 않은 PNG로 대체하지 않는다.

## 완료

Before/After PNG와 HTML/CSS 절대 경로, 주요 변경과 해결할 문제, 확인한 viewport·상태·남은 가정을 전달한다. 실제 구현에서 제외할 시안 전용 요소를 표시한다.

확인하지 않은 기능·데이터·문구·신뢰 표식을 제품 사실로 만들지 않는다. 비교 설명은 제품 UI 밖에 두고, 정적 시안으로 확인하지 못한 상호작용·접근성 동작은 구현 검증 대상으로 남긴다.
