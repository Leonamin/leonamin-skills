# Avatar

프로필 이미지와 이름 fallback

## 동작 계약

- 이미지 없음·실패 시 이름 앞 두 글자를 표시합니다.
- 이름을 접근 가능한 대체 텍스트로 제공합니다.
- size 변경 시에도 원형 영역을 유지합니다.

## 상태

- 사진
- 사진 없음
- 실패
- 크기 변경

## 키보드

- 포커스 대상 아님

## 직접 관련 파일

- assets/src/components/basic/avatar.tsx
- assets/src/styles/basic.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/avatar.tsx
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

- Avatar: assets/src/components/basic/avatar.tsx:3-25

## 이식

1. assets/src/components/basic/avatar.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. assets/src/styles/basic.css의 해당 .gc-* 규칙과 tokens.css를 가져와 프로젝트 의미 토큰에 연결합니다.
3. 아래 사용 예제의 이벤트를 프로젝트 상태·서비스에 연결합니다. 데모 코드는 이식하지 않습니다.
4. 키보드, 긴 한국어, 비활성·오류 상태와 모바일 너비에서 동작 계약을 재확인합니다.

## 사용 예제

```tsx
import { Avatar } from "./components/basic/avatar";

<Avatar name={user.name} src={user.photoUrl} size={44} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
