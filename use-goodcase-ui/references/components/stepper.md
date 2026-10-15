# Stepper

줄이기·직접 입력·늘리기로 수량과 숫자를 조절합니다.

## 동작 계약

- value/onValueChange 제어형. min은 기본 0, step은 기본 1이며 max로 상한을 지정합니다.
- 기존 IconButton과 숫자 입력을 한 컨트롤로 조합. 최소·최대값에서는 해당 증감 버튼만 비활성화합니다.
- 직접 입력 중에만 draft를 유지합니다. Enter·포커스 이동·증감 조작은 변경을 요청하고 확정 표시는 부모 value를 따릅니다. 부모가 요청을 거절하거나 지연하면 미승인 값은 표시하지 않습니다. 빈 입력은 부모 값으로 복원합니다.
- 소수·지수 step은 십진 정밀도를 유지합니다. step은 양수, value/min/max는 유효한 숫자로 전달합니다. 상한이 step에 맞지 않으면 min 기준으로 max 이하의 마지막 step 값이 유효 상한입니다(0~10, step=3이면 9). 직접 입력·버튼·End가 같은 정책을 사용합니다.
- label과 입력·설명을 연결하며 error는 aria-invalid로 안내. isReadOnly는 값 확인·선택 가능, isDisabled는 모든 조작 차단.
- 입력의 기본 증감 화살표를 숨기고 양옆 버튼에 읽을 수 있는 이름을 제공합니다. 브랜드·밀도·다크 모드는 --gc-* 토큰을 따릅니다.
- 외부 포커스 링이 잘리거나 인접 요소를 가리지 않도록 부모 배치에 --gc-focus-clearance(기본 6px) 이상의 안전 여백·간격을 확보합니다.

## 상태

- 기본
- 최소·최대
- 직접 입력
- 소수 단위
- 읽기 전용
- 비활성
- 오류

## 키보드

- Tab: 줄이기·숫자 입력·늘리기 이동
- 버튼 Enter/Space: 증감
- 입력 ArrowUp/ArrowDown: 증감
- Home/End: 최소·최대값(상한이 있을 때)
- Enter: 입력 확정

## 직접 관련 파일

- assets/src/components/basic/stepper.tsx
- assets/src/styles/basic.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/button.tsx
- assets/src/components/basic/field.ts
- assets/src/components/basic/input.tsx
- assets/src/components/basic/stepper-value.ts
- assets/src/components/basic/stepper.tsx
- assets/src/styles/basic.css
- assets/src/styles/global.css
- assets/src/styles/tokens.css

상대 import와 공유 모듈의 다른 export 때문에 직접 사용하는 컴포넌트보다 범위가 넓을 수 있습니다.

## 외부 패키지

lucide-react, react, react-dom

참조 버전은 배포본 루트 manifest.json의 packageVersions를 확인합니다.

## 카탈로그 의존성 설명

- react
- lucide-react
- --gc-* 토큰

## 코드 위치

- StepperProps: assets/src/components/basic/stepper.tsx:8-18
- Stepper: assets/src/components/basic/stepper.tsx:20-134

## 이식

1. assets/src/components/basic/stepper.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. assets/src/styles/basic.css의 해당 .gc-* 규칙과 tokens.css를 가져와 프로젝트 의미 토큰에 연결합니다.
3. 아래 사용 예제의 이벤트를 프로젝트 상태·서비스에 연결합니다. 데모 코드는 이식하지 않습니다.
4. 키보드, 긴 한국어, 비활성·오류 상태와 모바일 너비에서 동작 계약을 재확인합니다.

## 사용 예제

```tsx
import { Stepper } from "./components/basic/stepper";

<Stepper label="수량" value={quantity} onValueChange={setQuantity} min={0} max={10} />
<Stepper label="간격" value={amount} onValueChange={setAmount} step={0.1} max={2} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
