# Accordion

여러 설명 영역을 독립적으로 열고 닫습니다.

## 동작 계약

- 기본은 여러 항목 동시 열기
- 제목은 실제 버튼
- 접힌 내부 요소는 탐색에서 제외
- 비활성 항목 지원

## 상태

- 열림
- 닫힘
- 여러 항목 열림
- 비활성

## 키보드

- Enter/Space: 열고 닫기
- 방향키/Home/End: 제목 이동

## 직접 관련 파일

- assets/src/components/overlays/index.tsx
- assets/src/styles/overlays.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/index.tsx
- assets/src/components/overlays/index.tsx
- assets/src/components/overlays/tabs.tsx
- assets/src/components/overlays/toast.tsx
- assets/src/styles/basic.css
- assets/src/styles/composed.css
- assets/src/styles/global.css
- assets/src/styles/overlays.css
- assets/src/styles/tabs.css
- assets/src/styles/toast.css
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

- Option: assets/src/components/overlays/index.tsx:19-19
- Select: assets/src/components/overlays/index.tsx:20-78
- Combobox: assets/src/components/overlays/index.tsx:79-254
- MenuItem: assets/src/components/overlays/index.tsx:255-260
- Menu: assets/src/components/overlays/index.tsx:261-287
- Popover: assets/src/components/overlays/index.tsx:288-314
- Tooltip: assets/src/components/overlays/index.tsx:315-335
- DialogProps: assets/src/components/overlays/index.tsx:336-348
- Dialog: assets/src/components/overlays/index.tsx:400-402
- Drawer: assets/src/components/overlays/index.tsx:403-405
- DialogClose: assets/src/components/overlays/index.tsx:406-408
- Accordion: assets/src/components/overlays/index.tsx:411-442

## 이식

1. assets/src/components/overlays/index.tsx와 assets/src/styles/overlays.css를 함께 복사합니다. 필요한 export만 남기면 묶음에서 분리할 수 있습니다.
2. react, react-dom, radix-ui, lucide-react를 설치하고 애플리케이션 진입점에서 CSS를 가져옵니다.
3. assets/src/styles/tokens.css의 --gc-* 의미 토큰을 프로젝트 토큰에 연결합니다. 브랜드별 색상·폰트·밀도를 교체합니다.
4. 상태와 이벤트를 프로젝트 데이터에 연결하고, 갤러리의 키보드·닫기·실패 계약을 이식 뒤 확인합니다.

## 사용 예제

```tsx
<Accordion items={[{value:"faq",title:"질문",content:"답변"}]} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
