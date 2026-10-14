# FileUploader

파일 선택과 실제 업로드를 분리하고 파일별 실패를 복구

## 동작 계약

- 기본 PNG/JPEG/SVG, 최대 3개·파일당 2MB를 선택 전에 검증합니다.
- 선택·드롭은 업로드하지 않습니다. 명시적 업로드 버튼으로 시작합니다.
- 파일별 진행률, 성공, 실패, 재시도, 제거를 지원합니다.
- 제거·unmount 시 AbortSignal로 요청 취소를 전달합니다.
- onUpload 외부 어댑터가 실제 저장을 수행하며 서버에서도 파일 검증이 필요합니다.

## 상태

- 선택 전
- 선택됨
- 검증 오류
- 업로드 중
- 성공
- 실패/재시도
- 취소

## 키보드

- Tab으로 파일 선택·업로드·제거 접근
- 네이티브 파일 선택창 사용

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
- 디자인 토큰 --gc-*

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
<FileUploader onUpload={async (file, {signal,onProgress}) => upload(file, signal, onProgress)} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
