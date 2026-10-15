# Tooltip

짧은 보조 설명을 호버와 포커스로 제공합니다.

## 동작 계약

- content는 문자열만 지원하여 내부 액션 금지
- 필수 설명은 Tooltip에만 숨기지 않음
- 포커스를 이동시키지 않음
- Trigger는 자식 요소를 재사용합니다. 아이콘 안내 예제는 실제 button인 ghost IconButton을 사용합니다.
- Trigger 주변과 overflow 컨테이너 안쪽에 --gc-focus-clearance(기본 6px) 이상의 포커스 안전 여백을 확보합니다.

## 상태

- 호버
- 키보드 포커스
- 닫힘

## 키보드

- Tab: 설명 표시
- Escape: 닫기

## 직접 관련 파일

- assets/src/components/overlays/tooltip.tsx
- assets/src/styles/overlays.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/overlays/tooltip.tsx
- assets/src/styles/global.css
- assets/src/styles/overlays.css
- assets/src/styles/tokens.css

상대 import와 공유 모듈의 다른 export 때문에 직접 사용하는 컴포넌트보다 범위가 넓을 수 있습니다.

## 외부 패키지

radix-ui, react, react-dom

참조 버전은 배포본 루트 manifest.json의 packageVersions를 확인합니다.

## 카탈로그 의존성 설명

- react
- react-dom
- radix-ui

## 코드 위치

- Tooltip: assets/src/components/overlays/tooltip.tsx:4-24

## 이식

1. assets/src/components/overlays/tooltip.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 복사합니다.
2. 필요한 외부 패키지는 포함 파일의 import와 의존성 목록을 확인해 설치합니다.
3. assets/src/styles/overlays.css와 tokens.css를 가져오고 --gc-* 토큰을 프로젝트 토큰에 연결합니다.
4. 상태와 이벤트를 프로젝트 데이터에 연결하고, 키보드·닫기·실패 계약을 이식 뒤 확인합니다.

## 사용 예제

```tsx
import { Tooltip } from "./components/overlays/tooltip";
import { IconButton } from "./components/basic/button";

<Tooltip content="추가 설명"><IconButton label="도움말"><Info size={20} aria-hidden="true" /></IconButton></Tooltip>
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
