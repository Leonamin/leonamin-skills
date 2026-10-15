# TextField

레이블과 오류 설명이 연결된 한 줄 입력

## 동작 계약

- label은 입력 id와 연결하며 placeholder를 레이블로 대체하지 않습니다.
- error가 있으면 aria-invalid와 오류 설명 연결을 적용합니다.
- readOnly는 선택·포커스 가능하고 disabled는 입력·포커스 불가입니다.
- type="number"는 브라우저 기본 증감 화살표를 숨기며 숫자 입력·키보드 ArrowUp/ArrowDown 동작은 유지합니다.
- Input은 같은 입력 스타일을 제공하는 하위 primitive입니다. FormField 등 외부에서 label·설명을 공급할 때 사용합니다.
- 외부 포커스 링이 잘리거나 인접 요소를 가리지 않도록 부모 배치에 --gc-focus-clearance(기본 6px) 이상의 안전 여백·간격을 확보합니다.

## 상태

- 기본
- 입력
- 숫자·기본 화살표 없음
- 필수
- 오류
- 읽기 전용
- 비활성

## 키보드

- Tab으로 입력 이동
- 표준 텍스트 편집 단축키

## 직접 관련 파일

- assets/src/components/basic/text-field.tsx
- assets/src/styles/basic.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/field.ts
- assets/src/components/basic/input.tsx
- assets/src/components/basic/text-field.tsx
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

- TextField: assets/src/components/basic/text-field.tsx:5-32

## 이식

1. assets/src/components/basic/text-field.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. assets/src/styles/basic.css의 해당 .gc-* 규칙과 tokens.css를 가져와 프로젝트 의미 토큰에 연결합니다.
3. 아래 사용 예제의 이벤트를 프로젝트 상태·서비스에 연결합니다. 데모 코드는 이식하지 않습니다.
4. 키보드, 긴 한국어, 비활성·오류 상태와 모바일 너비에서 동작 계약을 재확인합니다.

## 사용 예제

```tsx
import { TextField } from "./components/basic/text-field";
import { Input } from "./components/basic/input";

<TextField label="이름" value={name} onChange={e => setName(e.target.value)} error={nameError} />
// FormField의 render prop 안에서는 <Input {...props} /> 사용
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
