# Spinner

원형 선과 속도가 다른 여러 원으로 불확정 로딩을 표시합니다.

## 동작 계약

- variant="ring"(기본)은 둥근 끝의 원형 선이 800ms 주기로 회전합니다. variant="orbit"은 작은 원 4개가 각각 1200·1600·2100·2700ms 주기로 공전합니다.
- size는 small=16px, medium=32px(기본), large=48px. tone은 accent(기본), muted, inherit이며 --gc-* 토큰을 사용합니다.
- 기본은 role=status와 label(기본 불러오는 중)로 작업 상태를 안내합니다. 진행률·남은 시간을 추정하지 않으며 표시 여부는 호출부가 결정합니다.
- isDecorative=true는 role과 안내 텍스트를 제외하고 aria-hidden을 적용합니다. 버튼·다른 상태 안내 안에 중복 배치할 때 사용합니다.
- 포커스나 사용자 조작이 없는 표시 요소입니다. prefers-reduced-motion에서는 회전을 멈추고 원형 선·각 원의 정적인 배치와 상태 안내를 유지합니다.

## 상태

- 원형 선
- 여러 원의 독립 회전
- 16px·32px·48px
- 강조·보조·상속 색상
- 장식형
- 모션 감소

## 키보드

- 포커스 대상 아님

## 직접 관련 파일

- assets/src/components/basic/spinner.tsx
- assets/src/styles/basic.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/spinner.tsx
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

- SpinnerProps: assets/src/components/basic/spinner.tsx:1-7
- Spinner: assets/src/components/basic/spinner.tsx:9-53

## 이식

1. assets/src/components/basic/spinner.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. assets/src/styles/basic.css의 해당 .gc-* 규칙과 tokens.css를 가져와 프로젝트 의미 토큰에 연결합니다.
3. 아래 사용 예제의 이벤트를 프로젝트 상태·서비스에 연결합니다. 데모 코드는 이식하지 않습니다.
4. 키보드, 긴 한국어, 비활성·오류 상태와 모바일 너비에서 동작 계약을 재확인합니다.

## 사용 예제

```tsx
import { Spinner } from "./components/basic/spinner";
import { Button } from "./components/basic/button";

<Spinner label="목록을 불러오는 중" />
<Spinner variant="orbit" size="large" label="이미지를 준비하는 중" />
<Button disabled><Spinner size="small" tone="inherit" isDecorative /> 처리 중</Button>
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
