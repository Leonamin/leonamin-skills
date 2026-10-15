# Pagination

경계와 처리 상태를 지키는 페이지 탐색

## 동작 계약

- 처음·이전·다음·마지막을 제공하며 경계를 넘는 이동을 차단합니다.
- 페이지 상태는 외부 소유이며 onPageChange는 요청만 전달합니다.
- isLoading 중 탐색을 차단하며 조회 성공 전 페이지 확정은 호출부 책임입니다.
- 외부 포커스 링이 잘리거나 인접 요소를 가리지 않도록 부모 배치에 --gc-focus-clearance(기본 6px) 이상의 안전 여백·간격을 확보합니다.

## 상태

- 처음
- 중간
- 마지막
- 처리 중

## 키보드

- Tab으로 버튼 이동
- Enter·Space로 페이지 요청

## 직접 관련 파일

- assets/src/components/basic/pagination.tsx
- assets/src/styles/basic.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/button.tsx
- assets/src/components/basic/pagination.tsx
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

- Pagination: assets/src/components/basic/pagination.tsx:3-50

## 이식

1. assets/src/components/basic/pagination.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. assets/src/styles/basic.css의 해당 .gc-* 규칙과 tokens.css를 가져와 프로젝트 의미 토큰에 연결합니다.
3. 아래 사용 예제의 이벤트를 프로젝트 상태·서비스에 연결합니다. 데모 코드는 이식하지 않습니다.
4. 키보드, 긴 한국어, 비활성·오류 상태와 모바일 너비에서 동작 계약을 재확인합니다.

## 사용 예제

```tsx
import { Pagination } from "./components/basic/pagination";

<Pagination page={page} totalPages={totalPages} onPageChange={loadPage} isLoading={isLoading} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
