# Accordion

여러 설명 영역을 독립적으로 열고 닫습니다.

## 동작 계약

- 기본은 여러 항목 동시 열기
- 제목은 실제 버튼
- 접힌 내부 요소는 탐색에서 제외
- 비활성 항목 지원
- hasAnimation은 기본 true. 높이와 투명도를 240ms로 전환하고 false는 즉시 열고 닫기. prefers-reduced-motion에서는 애니메이션 제거

## 상태

- 열림
- 닫힘
- 여러 항목 열림
- 비활성
- 애니메이션 켜기·끄기
- 모션 감소

## 키보드

- Enter/Space: 열고 닫기
- 방향키/Home/End: 제목 이동

## 직접 관련 파일

- assets/src/components/overlays/accordion.tsx
- assets/src/styles/overlays.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/overlays/accordion.tsx
- assets/src/styles/global.css
- assets/src/styles/overlays.css
- assets/src/styles/tokens.css

상대 import와 공유 모듈의 다른 export 때문에 직접 사용하는 컴포넌트보다 범위가 넓을 수 있습니다.

## 외부 패키지

lucide-react, radix-ui, react, react-dom

참조 버전은 배포본 루트 manifest.json의 packageVersions를 확인합니다.

## 카탈로그 의존성 설명

- react
- react-dom
- radix-ui
- lucide-react

## 코드 위치

- Accordion: assets/src/components/overlays/accordion.tsx:5-41

## 이식

1. assets/src/components/overlays/accordion.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 복사합니다.
2. 필요한 외부 패키지는 포함 파일의 import와 의존성 목록을 확인해 설치합니다.
3. assets/src/styles/overlays.css와 tokens.css를 가져오고 --gc-* 토큰을 프로젝트 토큰에 연결합니다.
4. 상태와 이벤트를 프로젝트 데이터에 연결하고, 키보드·닫기·실패 계약을 이식 뒤 확인합니다.

## 사용 예제

```tsx
import { Accordion } from "./components/overlays/accordion";

<Accordion items={[{value:"faq",title:"질문",content:"답변"}]} hasAnimation />
<Accordion items={items} hasAnimation={false} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
