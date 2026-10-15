# FormField

입력의 이름, 설명, 필수 여부와 오류를 연결하는 공통 필드

## 동작 계약

- 고유 id로 label과 입력을 연결합니다.
- 설명 또는 오류를 aria-describedby로 연결하고 오류가 설명보다 우선합니다.
- 오류가 있으면 aria-invalid를 전달합니다. 실제 검증은 호출부가 담당합니다.

## 상태

- 기본
- 필수
- 설명
- 30자 초과 오류

## 키보드

- Tab으로 입력에 접근
- label 클릭으로 입력 포커스

## 직접 관련 파일

- assets/src/components/composed/form-field.tsx
- assets/src/styles/composed.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/composed/form-field.tsx
- assets/src/styles/composed.css
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

- FormField: assets/src/components/composed/form-field.tsx:3-41

## 이식

1. assets/src/components/composed/form-field.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. 필요한 외부 패키지는 포함 파일의 import와 의존성 목록을 확인해 설치합니다.
3. assets/src/styles/composed.css의 대상 클래스와 공통 스타일을 가져오고 --gc-*를 프로젝트 토큰에 연결합니다.
4. 데모 코드는 옮기지 않고 실제 데이터·API·파일 저장 동작을 콜백에 연결합니다.
5. 키보드, 실패, 긴 한국어 콘텐츠, 좁은 화면 상태를 프로젝트에서 다시 확인합니다.

## 사용 예제

```tsx
import { FormField } from "./components/composed/form-field";
import { Input } from "./components/basic/input";

<FormField label="이름" error={error} isRequired>{props => <Input {...props} />}</FormField>
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
