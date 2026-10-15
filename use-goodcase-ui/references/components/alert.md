# Alert

문맥에 유지되는 안내와 오류

## 동작 계약

- 제목과 설명을 함께 표시하며 자동으로 사라지지 않습니다.
- onDismiss를 제공한 경우만 muted X ghost 아이콘 버튼이 생깁니다. 호버·포커스에서 표면을 표시합니다.
- 위험은 alert, 다른 상태는 status로 전달합니다.

## 상태

- 안내
- 성공
- 주의
- 오류
- 닫기 가능

## 키보드

- 내부 액션·닫기 버튼은 Tab·Enter·Space

## 직접 관련 파일

- assets/src/components/basic/alert.tsx
- assets/src/styles/basic.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/alert.tsx
- assets/src/components/basic/button.tsx
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

- Alert: assets/src/components/basic/alert.tsx:5-40

## 이식

1. assets/src/components/basic/alert.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. assets/src/styles/basic.css의 해당 .gc-* 규칙과 tokens.css를 가져와 프로젝트 의미 토큰에 연결합니다.
3. 아래 사용 예제의 이벤트를 프로젝트 상태·서비스에 연결합니다. 데모 코드는 이식하지 않습니다.
4. 키보드, 긴 한국어, 비활성·오류 상태와 모바일 너비에서 동작 계약을 재확인합니다.

## 사용 예제

```tsx
import { Alert } from "./components/basic/alert";

<Alert title="저장 실패" tone="danger">입력 내용은 유지했어요.</Alert>
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
