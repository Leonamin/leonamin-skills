# Progress

확정·불확정 진행 상태

## 동작 계약

- 유한한 value는 0~100으로 제한하여 role=progressbar와 aria-valuenow로 실제 진행률을 전달합니다.
- value 생략 또는 비유한 값은 불확정 진행이며 aria-valuenow를 생략하고 처리 중으로 안내합니다.
- size=thin은 8px, regular(기본)은 14px, thick은 32px입니다. track은 테두리 없는 토큰 기반 디자인입니다.
- thick 숫자는 실제 채움 영역 가운데에 표시합니다. 실제 글자 너비와 토큰 여백이 채움 안에 들어가지 않으면 채움 오른쪽에 표시하고, 오른쪽 공간도 부족하면 바 아래로 내려 읽을 수 있게 합니다. 고정 퍼센트 기준은 사용하지 않습니다. 다른 크기는 숫자를 label 옆에 표시합니다.
- 크기·폰트·테마 변경 시 위치를 다시 측정하며 채움과 숫자는 즉시 함께 이동합니다. 모션 감소 설정에서는 불확정 애니메이션을 멈춥니다.
- label로 진행 작업의 이름을 제공합니다.

## 상태

- thin 8px
- regular 14px
- thick 32px
- 0%
- 5%
- 35%
- 100%
- 불확정
- 모션 감소

## 키보드

- 포커스 대상 아님

## 직접 관련 파일

- assets/src/components/basic/progress.tsx
- assets/src/styles/basic.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/progress.tsx
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

- Progress: assets/src/components/basic/progress.tsx:3-134

## 이식

1. assets/src/components/basic/progress.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. assets/src/styles/basic.css의 해당 .gc-* 규칙과 tokens.css를 가져와 프로젝트 의미 토큰에 연결합니다.
3. 아래 사용 예제의 이벤트를 프로젝트 상태·서비스에 연결합니다. 데모 코드는 이식하지 않습니다.
4. 키보드, 긴 한국어, 비활성·오류 상태와 모바일 너비에서 동작 계약을 재확인합니다.

## 사용 예제

```tsx
import { Progress } from "./components/basic/progress";

<Progress label="파일 처리" value={progress} size="thick" />
<Progress label="처리 중" size="thin" />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
