# ConfirmDialog

취소에서 시작하며 실패 시 열린 상태를 유지하는 확인 창

## 동작 계약

- 초기 포커스는 취소 버튼입니다.
- 바깥 클릭으로 닫히지 않습니다. 처리 중 닫기 요청도 무시합니다.
- onConfirm Promise 성공 시 닫고 실패 시 내부 오류를 표시합니다.
- 동기 ref로 중복 실행을 차단합니다. 실제 삭제는 외부 콜백에만 있습니다.

## 상태

- 닫힘
- 확인
- 처리 중
- 오류
- 완료

## 키보드

- Tab 포커스 순환
- Escape로 닫기 (처리 중 제외)
- 닫은 뒤 호출 버튼 포커스 복귀

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
<ConfirmDialog trigger={<Button>삭제</Button>} title="삭제할까요?" description="설명" onConfirm={deleteItem} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
