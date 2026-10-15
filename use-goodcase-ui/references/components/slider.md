# Slider

범위 안의 숫자를 트랙과 키보드로 연속 조절합니다.

## 동작 계약

- value/onValueChange 제어형. min=0, max=100, step=1이 기본이며 숫자 범위를 명시할 수 있습니다.
- label과 native range 입력을 연결하며 valueText를 보이는 현재 값과 aria-valuetext에 사용합니다.
- isDisabled는 포커스와 조작을 차단. description·error는 입력과 연결합니다.
- 트랙·thumb·선택 구간은 --gc-* 토큰을 사용해 Blue·Forest·다크·밀도에 대응합니다.
- 외부 포커스 링이 잘리거나 인접 요소를 가리지 않도록 부모 배치에 --gc-focus-clearance(기본 6px) 이상의 안전 여백·간격을 확보합니다.

## 상태

- 기본
- 최소·최대
- 사용자 지정 범위·단위
- 비활성
- 키보드 포커스

## 키보드

- Tab: 포커스
- 방향키: step 단위 증감
- Home/End: 최소·최대
- PageUp/PageDown: 브라우저 기본 범위 이동

## 직접 관련 파일

- assets/src/components/basic/slider.tsx
- assets/src/styles/basic.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/field.ts
- assets/src/components/basic/slider.tsx
- assets/src/styles/basic.css
- assets/src/styles/global.css
- assets/src/styles/tokens.css

상대 import와 공유 모듈의 다른 export 때문에 직접 사용하는 컴포넌트보다 범위가 넓을 수 있습니다.

## 외부 패키지

react, react-dom

참조 버전은 배포본 루트 manifest.json의 packageVersions를 확인합니다.

## 카탈로그 의존성 설명

- react
- --gc-* 토큰

## 코드 위치

- SliderProps: assets/src/components/basic/slider.tsx:4-12
- Slider: assets/src/components/basic/slider.tsx:13-60

## 이식

1. assets/src/components/basic/slider.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. assets/src/styles/basic.css의 해당 .gc-* 규칙과 tokens.css를 가져와 프로젝트 의미 토큰에 연결합니다.
3. 아래 사용 예제의 이벤트를 프로젝트 상태·서비스에 연결합니다. 데모 코드는 이식하지 않습니다.
4. 키보드, 긴 한국어, 비활성·오류 상태와 모바일 너비에서 동작 계약을 재확인합니다.

## 사용 예제

```tsx
import { Slider } from "./components/basic/slider";

<Slider label="볼륨" value={volume} onValueChange={setVolume} valueText={`${volume}%`} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
