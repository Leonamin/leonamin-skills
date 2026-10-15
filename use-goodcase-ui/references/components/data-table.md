# DataTable

정렬, 현재 페이지 선택, 상태 처리를 갖춘 데이터 목록

## 동작 계약

- 안정적인 row.id로 선택 상태를 관리합니다.
- 이름 정렬 변경 시 첫 페이지로 이동하고 선택을 해제합니다.
- 전체 선택은 현재 페이지에만 적용되며 일부 선택 상태를 표시합니다.
- 행·전체 선택은 공용 Checkbox를 사용하며 숨긴 라벨과 일부 선택 상태를 동일하게 지원합니다.
- 페이지 이동 또는 rows 변경 시 선택을 해제합니다. pageSize 변경 시 첫 페이지로 돌아가고 선택을 해제합니다.
- 최초 로딩·빈 결과·오류·재시도·기존 내용 유지 새로고침을 지원합니다.
- columns의 render/compare와 getRowId로 다른 데이터 모델에 이식합니다. isSortable/isSelectable 기본 true로 기능을 끌 수 있습니다.
- 기본 DataRow(id/name/status) 모델은 columns/getRowId를 생략할 수 있습니다. 다른 행 모델은 columns와 getRowId를 함께 제공해야 하며 타입으로 확인합니다. 클라이언트 정렬·페이지네이션이며 서버형은 별도 확장이 필요합니다.

## 상태

- 로딩
- 기본
- 일부/전체 선택
- 정렬
- 페이지 경계
- 빈 결과
- 오류/재시도
- 재조회

## 키보드

- Tab으로 정렬·선택·페이지 버튼 이동
- Space로 체크박스 선택

## 직접 관련 파일

- assets/src/components/composed/data-table.tsx
- assets/src/styles/composed.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/button.tsx
- assets/src/components/basic/checkbox.tsx
- assets/src/components/basic/pagination.tsx
- assets/src/components/basic/skeleton.tsx
- assets/src/components/composed/async-content.tsx
- assets/src/components/composed/data-table.tsx
- assets/src/styles/basic.css
- assets/src/styles/composed.css
- assets/src/styles/global.css
- assets/src/styles/tokens.css

상대 import와 공유 모듈의 다른 export 때문에 직접 사용하는 컴포넌트보다 범위가 넓을 수 있습니다.

## 외부 패키지

react, react-dom

참조 버전은 배포본 루트 manifest.json의 packageVersions를 확인합니다.

## 카탈로그 의존성 설명

- react
- assets/src/components/basic/button.tsx
- assets/src/components/basic/checkbox.tsx
- assets/src/components/basic/pagination.tsx
- assets/src/components/composed/async-content.tsx
- --gc-* 토큰

## 코드 위치

- DataRow: assets/src/components/composed/data-table.tsx:7-7
- DataColumn: assets/src/components/composed/data-table.tsx:8-13
- DataTableProps: assets/src/components/composed/data-table.tsx:26-29
- DataTable: assets/src/components/composed/data-table.tsx:56-56
- DataTable: assets/src/components/composed/data-table.tsx:57-57
- DataTable: assets/src/components/composed/data-table.tsx:58-67

## 이식

1. assets/src/components/composed/data-table.tsx와 상대 import로 연결된 공용 컴포넌트·타입을 함께 가져옵니다.
2. 필요한 외부 패키지는 포함 파일의 import와 의존성 목록을 확인해 설치합니다.
3. assets/src/styles/composed.css의 대상 클래스와 공통 스타일을 가져오고 --gc-*를 프로젝트 토큰에 연결합니다.
4. 데모 코드는 옮기지 않고 실제 데이터·API·파일 저장 동작을 콜백에 연결합니다.
5. 키보드, 실패, 긴 한국어 콘텐츠, 좁은 화면 상태를 프로젝트에서 다시 확인합니다.

## 사용 예제

```tsx
import { DataTable } from "./components/composed/data-table";

<DataTable rows={rows} isLoading={isLoading} error={error} onRetry={reload} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
