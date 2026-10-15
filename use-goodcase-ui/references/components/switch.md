# Switch

레이블이 유지되는 설정 켜짐·꺼짐

## 동작 계약

- 상태가 바뀌어도 label은 유지합니다.
- role="switch"와 checked로 설정 상태를 전달합니다.
- 저장·실패·처리 중 상태는 호출부에서 전달하며 즉시 저장을 추측하지 않습니다.
- 외부 포커스 링이 잘리거나 인접 요소를 가리지 않도록 부모 배치에 --gc-focus-clearance(기본 6px) 이상의 안전 여백·간격을 확보합니다.

## 상태

- 켜짐
- 꺼짐
- 비활성

## 키보드

- Tab으로 이동
- Space로 토글

## 직접 관련 파일

- assets/src/components/basic/switch.tsx
- assets/src/styles/basic.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/switch.tsx
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

- Switch: assets/src/components/basic/switch.tsx:1-25

## 이식

1. assets/src/components/basic/switch.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. assets/src/styles/basic.css의 해당 .gc-* 규칙과 tokens.css를 가져와 프로젝트 의미 토큰에 연결합니다.
3. 아래 사용 예제의 이벤트를 프로젝트 상태·서비스에 연결합니다. 데모 코드는 이식하지 않습니다.
4. 키보드, 긴 한국어, 비활성·오류 상태와 모바일 너비에서 동작 계약을 재확인합니다.

## 사용 예제

```tsx
import { Switch } from "./components/basic/switch";

<Switch label="이메일 알림" isChecked={isEnabled} onCheckedChange={setIsEnabled} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
