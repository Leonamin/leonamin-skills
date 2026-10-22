# 아이콘

**아이콘 자리에는 이모지를 쓰지 않고, 제품 아이콘 세트 또는 로컬 인라인 SVG를 쓴다.**

이모지는 OS·브라우저·폰트에 따라 모양·크기·베이스라인이 달라져 같은 조건의 Before/After 캡처가 흔들리고, `currentColor`·stroke 굵기·정렬을 제품 UI와 맞출 수 없다.

## 선택 순서

1. 확인된 제품 아이콘 세트가 있으면 그 SVG·굵기·크기를 복사한다. 제품이 lucide-react·heroicons·tabler를 쓰면 같은 이름의 원본을 쓴다.
2. 세트가 없거나 확인할 수 없으면 Lucide(ISC) 원본 path를 인라인으로 넣는다. 한 화면에서 서로 다른 아이콘 세트를 섞지 않는다.
3. 제품이 실제로 이모지를 쓰는 위치(사용자 이모지·반응·카테고리 표식)는 Before에 그대로 재현한다. 작성자의 편의를 위한 이모지 대체는 하지 않는다.

After에서만 아이콘 세트를 바꿔 개선으로 보이게 하지 않는다. 아이콘 교체가 요청 범위일 때만 Before와 다르게 한다.

## 인라인 스프라이트

캡처는 `file://`로 열기 때문에 외부 `icons.svg`를 `<use href="icons.svg#id">`로 참조하면 로드되지 않는다. 문서 안에 `<symbol>`을 인라인하고 `#id`로 참조한다. 아이콘 폰트는 쓰지 않는다.

아래는 Lucide 1.61.0 원본 path다. 필요한 symbol만 남기고 `<body>` 첫 자식으로 붙인다.

```html
<svg class="icon-sprite" aria-hidden="true" focusable="false">
  <symbol id="i-search" viewBox="0 0 24 24">
    <path d="m21 21-4.34-4.34" />
    <circle cx="11" cy="11" r="8" />
  </symbol>
  <symbol id="i-x" viewBox="0 0 24 24">
    <path d="M18 6 6 18" />
    <path d="m6 6 12 12" />
  </symbol>
  <symbol id="i-plus" viewBox="0 0 24 24">
    <path d="M5 12h14" />
    <path d="M12 5v14" />
  </symbol>
  <symbol id="i-check" viewBox="0 0 24 24">
    <path d="M20 6 9 17l-5-5" />
  </symbol>
  <symbol id="i-chevron-down" viewBox="0 0 24 24">
    <path d="m6 9 6 6 6-6" />
  </symbol>
  <symbol id="i-chevron-right" viewBox="0 0 24 24">
    <path d="m9 18 6-6-6-6" />
  </symbol>
  <symbol id="i-arrow-left" viewBox="0 0 24 24">
    <path d="m12 19-7-7 7-7" />
    <path d="M19 12H5" />
  </symbol>
  <symbol id="i-external-link" viewBox="0 0 24 24">
    <path d="M15 3h6v6" />
    <path d="M10 14 21 3" />
    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
  </symbol>
  <symbol id="i-more-horizontal" viewBox="0 0 24 24">
    <circle cx="12" cy="12" r="1" />
    <circle cx="19" cy="12" r="1" />
    <circle cx="5" cy="12" r="1" />
  </symbol>
  <symbol id="i-menu" viewBox="0 0 24 24">
    <path d="M4 5h16" />
    <path d="M4 12h16" />
    <path d="M4 19h16" />
  </symbol>
  <symbol id="i-settings" viewBox="0 0 24 24">
    <path d="M9.671 4.136a2.34 2.34 0 0 1 4.659 0 2.34 2.34 0 0 0 3.319 1.915 2.34 2.34 0 0 1 2.33 4.033 2.34 2.34 0 0 0 0 3.831 2.34 2.34 0 0 1-2.33 4.033 2.34 2.34 0 0 0-3.319 1.915 2.34 2.34 0 0 1-4.659 0 2.34 2.34 0 0 0-3.32-1.915 2.34 2.34 0 0 1-2.33-4.033 2.34 2.34 0 0 0 0-3.831A2.34 2.34 0 0 1 6.35 6.051a2.34 2.34 0 0 0 3.319-1.915" />
    <circle cx="12" cy="12" r="3" />
  </symbol>
  <symbol id="i-user" viewBox="0 0 24 24">
    <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2" />
    <circle cx="12" cy="7" r="4" />
  </symbol>
  <symbol id="i-calendar" viewBox="0 0 24 24">
    <path d="M8 2v3" />
    <path d="M16 2v3" />
    <rect x="3" y="3" width="18" height="18" rx="2" />
    <path d="M3 9h18" />
  </symbol>
  <symbol id="i-filter" viewBox="0 0 24 24">
    <path d="M10 20a1 1 0 0 0 .553.895l2 1A1 1 0 0 0 14 21v-7a2 2 0 0 1 .517-1.341L21.74 4.67A1 1 0 0 0 21 3H3a1 1 0 0 0-.742 1.67l7.225 7.989A2 2 0 0 1 10 14z" />
  </symbol>
  <symbol id="i-star" viewBox="0 0 24 24">
    <path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z" />
  </symbol>
  <symbol id="i-bell" viewBox="0 0 24 24">
    <path d="M10.268 21a2 2 0 0 0 3.464 0" />
    <path d="M3.262 15.326A1 1 0 0 0 4 17h16a1 1 0 0 0 .74-1.673C19.41 13.956 18 12.499 18 8A6 6 0 0 0 6 8c0 4.499-1.411 5.956-2.738 7.326" />
  </symbol>
  <symbol id="i-pencil" viewBox="0 0 24 24">
    <path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z" />
    <path d="m15 5 4 4" />
  </symbol>
  <symbol id="i-copy" viewBox="0 0 24 24">
    <rect width="14" height="14" x="8" y="8" rx="2" ry="2" />
    <path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2" />
  </symbol>
  <symbol id="i-trash-2" viewBox="0 0 24 24">
    <path d="M10 11v6" />
    <path d="M14 11v6" />
    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6" />
    <path d="M3 6h18" />
    <path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" />
  </symbol>
  <symbol id="i-triangle-alert" viewBox="0 0 24 24">
    <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3" />
    <path d="M12 9v4" />
    <path d="M12 17h.01" />
  </symbol>
  <symbol id="i-info" viewBox="0 0 24 24">
    <circle cx="12" cy="12" r="10" />
    <path d="M12 16v-4" />
    <path d="M12 8h.01" />
  </symbol>
</svg>
```

symbol에는 `class`·`width`·`height`·`stroke-*` 속성을 넣지 않고 CSS로 제어한다. 색은 `currentColor`를 상속하므로 버튼·링크 상태 색을 그대로 따른다.

```css
.icon-sprite {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

.icon {
  width: var(--icon-size, 20px);
  height: var(--icon-size, 20px);
  flex: none;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}
```

```html
<button class="icon-button" type="button" aria-label="검색">
  <svg class="icon" aria-hidden="true" focusable="false"><use href="#i-search"></use></svg>
</button>

<!-- 텍스트 옆 장식 아이콘 -->
<span class="meta">
  <svg class="icon" style="--icon-size: 16px" aria-hidden="true" focusable="false"><use href="#i-calendar"></use></svg>
  2026-10-22
</span>
```

## 새 아이콘 추가

작성 시점에 한 번만 받아 path를 복사한다. HTML이 렌더링 시점에 네트워크를 참조해서는 안 된다.

```bash
curl -s https://unpkg.com/lucide-static@1.61.0/icons/pin.svg
# 또는 npm pack lucide-static@1.61.0 후 icons/<name>.svg
```

`<svg>` 안쪽 요소만 `<symbol id="i-<name>" viewBox="0 0 24 24">`에 넣는다. 이름은 `i-` 접두사와 케밥 표기를 유지한다.

## 일관성과 접근성

- 크기는 기준 세트의 16·20·24px 중 확인된 값을 쓰고 한 화면에서 섞지 않는다. 제품 기준이 없으면 24px·`stroke-width: 2`를 유지한다.
- 아이콘만 있는 액션에는 `aria-label`이나 숨김 텍스트로 이름을 준다. 장식 아이콘은 `aria-hidden="true"`와 `focusable="false"`를 붙인다.
- 아이콘 20px만으로 클릭 영역을 만들지 않는다. 버튼 padding으로 최소 40px 안팎의 타깃을 확보한다.
- 색·아이콘 모양만으로 상태를 전달하지 않는다. 시안에서 상태를 보여야 하면 텍스트나 배지로 함께 표기한다.
