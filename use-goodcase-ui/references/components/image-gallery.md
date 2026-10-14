# ImageGallery

썸네일에서 선택한 이미지로 뷰어를 여는 갤러리

## 동작 계약

- 썸네일 선택 시 해당 index부터 ImageViewer를 엽니다.
- 4:3 썸네일과 반응형 그리드를 유지합니다.
- 썸네일 로딩 실패는 개별 fallback으로 처리합니다.
- 닫기 후 실제 선택한 썸네일로 포커스를 돌립니다.
- 이미지 대체 텍스트는 데이터에서 전달합니다.

## 상태

- 그리드
- 모바일 2열
- 이미지 실패
- 동일 ID 새 src 복구
- 뷰어 열림

## 키보드

- Tab으로 썸네일 탐색
- Enter/Space로 열기
- Escape 닫기

## 직접 관련 파일

- assets/src/components/composed/index.tsx
- assets/src/styles/composed.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/index.tsx
- assets/src/components/composed/index.tsx
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

- React 19
- basic/Button
- ImageViewer
- overlays/Dialog (Radix UI)
- --gc-* 토큰

## 코드 위치

- FormField: assets/src/components/composed/index.tsx:12-50
- FormActions: assets/src/components/composed/index.tsx:51-84
- ConfirmDialog: assets/src/components/composed/index.tsx:85-159
- FilterValues: assets/src/components/composed/index.tsx:160-160
- SearchFilterBar: assets/src/components/composed/index.tsx:161-219
- AsyncContent: assets/src/components/composed/index.tsx:220-273
- DataRow: assets/src/components/composed/index.tsx:274-274
- DataColumn: assets/src/components/composed/index.tsx:275-280
- DataTable: assets/src/components/composed/index.tsx:281-463
- UploadItem: assets/src/components/composed/index.tsx:464-470
- UploadAdapter: assets/src/components/composed/index.tsx:471-474
- FileUploader: assets/src/components/composed/index.tsx:475-652
- ViewerImage: assets/src/components/composed/index.tsx:653-653
- ImageViewer: assets/src/components/composed/index.tsx:654-1359
- ImageGallery: assets/src/components/composed/index.tsx:1360-1394
- CopyField: assets/src/components/composed/index.tsx:1404-1431

## 이식

1. assets/src/components/composed/index.tsx에서 대상 컴포넌트와 관련 타입을 복사하거나 필요한 export만 추출합니다.
2. basic/Button과 overlays/Dialog 등 표시된 의존성을 함께 옮기고 import 경로를 맞춥니다.
3. assets/src/styles/composed.css에서 대상 클래스와 공통 클래스만 가져오고 --gc-*를 프로젝트 토큰에 연결합니다.
4. 데모 코드는 옮기지 않고 실제 데이터·API·파일 저장 동작을 콜백에 연결합니다.
5. 키보드, 실패, 긴 한국어 콘텐츠, 좁은 화면 상태를 프로젝트에서 다시 확인합니다.

## 사용 예제

```tsx
<ImageGallery images={[{id:"1", src:"/image.jpg", alt:"이미지 설명"}]} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
