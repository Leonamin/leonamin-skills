# CopyField

표시된 전체 원본값을 실제 클립보드에 복사

## 동작 계약

- navigator.clipboard.writeText가 성공한 뒤에만 성공을 표시합니다.
- 실패 시 직접 선택·복사할 수 있는 안내를 제공합니다.
- 읽기 전용 input으로 전체 원본값을 선택할 수 있습니다.
- 처리 중 중복 복사를 차단하고 이후 반복 복사를 허용합니다.

## 상태

- 기본
- 긴 값
- 복사 중
- 성공
- 권한 실패

## 키보드

- Tab으로 값·복사 버튼 접근
- 입력에서 전체 선택하여 수동 복사

## 직접 관련 파일

- assets/src/components/composed/copy-field.tsx
- assets/src/styles/composed.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/button.tsx
- assets/src/components/basic/field.ts
- assets/src/components/basic/input.tsx
- assets/src/components/basic/text-field.tsx
- assets/src/components/composed/copy-field.tsx
- assets/src/styles/basic.css
- assets/src/styles/composed.css
- assets/src/styles/global.css
- assets/src/styles/tokens.css

상대 import와 공유 모듈의 다른 export 때문에 직접 사용하는 컴포넌트보다 범위가 넓을 수 있습니다.

## 외부 패키지

react, react-dom

참조 버전은 배포본 루트 manifest.json의 packageVersions를 확인합니다.

## 카탈로그 의존성 설명

- react
- assets/src/components/basic/button.tsx
- assets/src/components/basic/text-field.tsx
- Clipboard API (HTTPS 또는 localhost)
- --gc-* 토큰

## 코드 위치

- CopyField: assets/src/components/composed/copy-field.tsx:5-32

## 이식

1. assets/src/components/composed/copy-field.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. 필요한 외부 패키지는 포함 파일의 import와 의존성 목록을 확인해 설치합니다.
3. assets/src/styles/composed.css의 대상 클래스와 공통 스타일을 가져오고 --gc-*를 프로젝트 토큰에 연결합니다.
4. 데모 코드는 옮기지 않고 실제 데이터·API·파일 저장 동작을 콜백에 연결합니다.
5. 키보드, 실패, 긴 한국어 콘텐츠, 좁은 화면 상태를 프로젝트에서 다시 확인합니다.

## 사용 예제

```tsx
import { CopyField } from "./components/composed/copy-field";

<CopyField label="식별자" value={id} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
