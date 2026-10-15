# Button / IconButton

명확한 액션과 중복 실행을 막는 처리 상태

## 동작 계약

- 기본 type은 button이며 폼 제출은 type="submit"으로 지정합니다.
- isLoading은 버튼 비활성화·aria-busy·공간 유지를 함께 적용합니다.
- 활성 Button·IconButton을 누르면 중심을 유지한 채 기본 96% 크기로 80ms ease-out 축소하고 놓으면 원래 크기로 돌아옵니다. 독립 scale 속성으로 배치용 transform을 유지하며 press 토큰으로 조정할 수 있습니다. 모션 감소 설정에서는 축소와 전환을 제거합니다.
- IconButton은 label로 접근 가능한 이름을 필수 제공하며 이벤트의 업무 처리는 호출부 책임입니다.
- size=default는 control-height(기본 40px·조밀한 밀도 34px)를 유지하고 일반·주요 터치 액션에 사용합니다. size=compact는 24px 정사각형에 16px 아이콘을 배치하며 토스트·조밀한 보조 액션에 사용합니다. 두 크기 모두 키보드 포커스와 ghost 동작을 유지합니다.
- IconButton은 control-height와 같은 정사각형입니다. appearance=ghost가 기본이며 호버·포커스에서만 표면을 표시합니다. filled는 Button variant의 기본·보조·위험 외형을 사용합니다.
- 외부 포커스 링이 잘리거나 인접 요소를 가리지 않도록 부모 배치에 --gc-focus-clearance(기본 6px) 이상의 안전 여백·간격을 확보합니다.

## 상태

- 기본
- 보조
- 위험
- ghost 아이콘
- filled 아이콘
- compact 24px 아이콘
- 호버·포커스
- 비활성
- 처리 중

## 키보드

- Tab으로 포커스
- Enter·Space로 실행

## 직접 관련 파일

- assets/src/components/basic/button.tsx
- assets/src/styles/basic.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/button.tsx
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

- Button: assets/src/components/basic/button.tsx:3-33
- IconButton: assets/src/components/basic/button.tsx:34-54

## 이식

1. assets/src/components/basic/button.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. assets/src/styles/basic.css의 해당 .gc-* 규칙과 tokens.css를 가져와 프로젝트 의미 토큰에 연결합니다.
3. 아래 사용 예제의 이벤트를 프로젝트 상태·서비스에 연결합니다. 데모 코드는 이식하지 않습니다.
4. 키보드, 긴 한국어, 비활성·오류 상태와 모바일 너비에서 동작 계약을 재확인합니다.

## 사용 예제

```tsx
import { Button, IconButton } from "./components/basic/button";
import { Star, X } from "lucide-react";

<Button isLoading={isSaving} onClick={save}>저장</Button>
<IconButton label="즐겨찾기" onClick={toggleFavorite}><Star size={20} aria-hidden="true" /></IconButton>
<IconButton label="닫기" size="compact" onClick={close}><X size={16} aria-hidden="true" /></IconButton>
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
