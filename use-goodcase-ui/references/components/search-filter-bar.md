# SearchFilterBar

작성 중 조건과 실제 적용된 조건을 구분하는 검색 패널

## 동작 계약

- 입력 중 조건은 draft이며 Enter 또는 적용 버튼으로만 반영합니다.
- 적용된 조건은 별도 요약으로 보여줍니다.
- 초기화는 검색어와 상태 전체를 초기화하고 즉시 적용합니다.
- value 변경 시 draft를 동기화합니다. 프로젝트 필터 모델은 필요에 따라 확장합니다.

## 상태

- 미적용 입력
- 적용
- 조건 초기화
- 외부 값 변경

## 키보드

- Enter로 적용
- Tab으로 필터·버튼 이동
- Select 방향키 탐색·Enter 확정·Escape 취소

## 직접 관련 파일

- assets/src/components/composed/search-filter-bar.tsx
- assets/src/styles/composed.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/button.tsx
- assets/src/components/basic/field.ts
- assets/src/components/basic/input.tsx
- assets/src/components/basic/text-field.tsx
- assets/src/components/composed/search-filter-bar.tsx
- assets/src/components/overlays/select.tsx
- assets/src/components/overlays/types.ts
- assets/src/styles/basic.css
- assets/src/styles/composed.css
- assets/src/styles/global.css
- assets/src/styles/overlays.css
- assets/src/styles/tokens.css

상대 import와 공유 모듈의 다른 export 때문에 직접 사용하는 컴포넌트보다 범위가 넓을 수 있습니다.

## 외부 패키지

lucide-react, radix-ui, react, react-dom

참조 버전은 배포본 루트 manifest.json의 packageVersions를 확인합니다.

## 카탈로그 의존성 설명

- react
- assets/src/components/basic/button.tsx
- assets/src/components/basic/text-field.tsx
- assets/src/components/overlays/select.tsx
- react-dom
- radix-ui
- lucide-react
- --gc-* 토큰

## 코드 위치

- FilterValues: assets/src/components/composed/search-filter-bar.tsx:6-6
- SearchFilterBar: assets/src/components/composed/search-filter-bar.tsx:7-65

## 이식

1. assets/src/components/composed/search-filter-bar.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. 필요한 외부 패키지는 포함 파일의 import와 의존성 목록을 확인해 설치합니다.
3. assets/src/styles/composed.css의 대상 클래스와 공통 스타일을 가져오고 --gc-*를 프로젝트 토큰에 연결합니다.
4. 데모 코드는 옮기지 않고 실제 데이터·API·파일 저장 동작을 콜백에 연결합니다.
5. 키보드, 실패, 긴 한국어 콘텐츠, 좁은 화면 상태를 프로젝트에서 다시 확인합니다.

## 사용 예제

```tsx
import { SearchFilterBar } from "./components/composed/search-filter-bar";

<SearchFilterBar value={filters} onApply={setFilters} statusOptions={[{value:"all",label:"전체"}]} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
