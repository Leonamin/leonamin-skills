# FormActions

중복 제출을 차단하고 실패 후 입력을 유지하는 폼 액션

## 동작 계약

- submit 버튼은 폼 제출을 실행합니다. 저장 중 취소와 제출을 비활성화합니다.
- 실패 메시지는 role=alert로 표시합니다. 입력 상태는 호출부가 소유합니다.
- 중복 실행은 제출 핸들러에서도 ref 또는 요청 잠금으로 차단해야 합니다.
- 취소 시 초기화 범위와 성공 후 이동은 호출부가 결정합니다.

## 상태

- 대기
- 처리 중
- 성공
- 실패 후 입력 유지

## 키보드

- Enter로 폼 제출
- Tab으로 취소·제출 이동

## 직접 관련 파일

- assets/src/components/composed/form-actions.tsx
- assets/src/styles/composed.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/button.tsx
- assets/src/components/composed/form-actions.tsx
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
- --gc-* 토큰

## 코드 위치

- FormActions: assets/src/components/composed/form-actions.tsx:3-36

## 이식

1. assets/src/components/composed/form-actions.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. 필요한 외부 패키지는 포함 파일의 import와 의존성 목록을 확인해 설치합니다.
3. assets/src/styles/composed.css의 대상 클래스와 공통 스타일을 가져오고 --gc-*를 프로젝트 토큰에 연결합니다.
4. 데모 코드는 옮기지 않고 실제 데이터·API·파일 저장 동작을 콜백에 연결합니다.
5. 키보드, 실패, 긴 한국어 콘텐츠, 좁은 화면 상태를 프로젝트에서 다시 확인합니다.

## 사용 예제

```tsx
import { FormActions } from "./components/composed/form-actions";

<FormActions isSubmitting={isSubmitting} error={error} onCancel={reset} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
