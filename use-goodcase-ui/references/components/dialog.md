# Dialog

배경을 차단하고 하나의 작업에 집중합니다.

## 동작 계약

- 제목과 접근 가능한 닫기 버튼 제공
- 포커스는 내부에 유지, 닫으면 호출 요소로 복귀
- 내부 검색 선택창을 닫는 동안에도 Tab/Shift+Tab은 처음·마지막 요소 사이에서 즉시 순환. 비활성·숨김·inert 요소는 제외하고 포털로 열린 하위 패널은 자체 키보드 탐색 유지
- 본문은 포커스 링용 안전 여백을 갖고 자식 사이 간격을 제공합니다. 내부 폼 그룹에도 --gc-focus-clearance 이상의 패딩과 간격을 두며 overflow로 링을 자르지 않습니다.
- 기본은 Escape·바깥 클릭 닫기
- shouldCloseOnOutsideClick, shouldCloseOnEscape로 닫기 규칙 지정
- initialFocusRef로 처음 포커스를 지정, isOpen/onOpenChange로 제어

## 상태

- 닫힘
- 열림
- 긴 본문
- 폼 입력

## 키보드

- Tab/Shift+Tab: 모달 내부 이동
- Escape: 닫기

## 직접 관련 파일

- assets/src/components/overlays/dialog.tsx
- assets/src/styles/overlays.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/overlays/dialog.tsx
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

- DialogProps: assets/src/components/overlays/dialog.tsx:5-17
- Dialog: assets/src/components/overlays/dialog.tsx:107-109
- Drawer: assets/src/components/overlays/dialog.tsx:110-112
- DialogClose: assets/src/components/overlays/dialog.tsx:113-115

## 이식

1. assets/src/components/overlays/dialog.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 복사합니다.
2. 필요한 외부 패키지는 포함 파일의 import와 의존성 목록을 확인해 설치합니다.
3. assets/src/styles/overlays.css와 tokens.css를 가져오고 --gc-* 토큰을 프로젝트 토큰에 연결합니다.
4. 상태와 이벤트를 프로젝트 데이터에 연결하고, 키보드·닫기·실패 계약을 이식 뒤 확인합니다.

## 사용 예제

```tsx
import { Dialog } from "./components/overlays/dialog";
import { Button } from "./components/basic/button";

<Dialog trigger={<Button>열기</Button>} title="제목" description="설명" footer={actions}>{content}</Dialog>
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
