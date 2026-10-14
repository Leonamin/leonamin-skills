# ImageViewer

어두운 전체 화면과 썸네일 탐색을 갖춘 이미지 뷰어

## 동작 계약

- 열기·이미지 변경 시 100% 화면 맞춤과 이동 초기화입니다.
- 이미지를 두 번 탭하면 기본 배율에서 탭한 이미지 지점을 기준으로 200% 확대합니다. 확대 상태의 두 번 탭은 100% 화면 맞춤으로 초기화합니다. 이동 경계에서 초점을 제한합니다.
- 터치·펜에서 250ms 이하의 탭 두 번을 300ms·32px 이내로 인식합니다. 이미지 탭만 포함하며 드래그·스와이프·핀치·긴 누름·컨트롤 입력은 탭 기록에서 제외합니다.
- 확대는 100~400%, 버튼과 두 손가락 핀치로 조작합니다. 손가락 중심의 이미지 지점을 유지하며 이동 경계에서 제한합니다.
- 두 번째 손가락이 추가되면 페이지 이동을 취소하고 핀치로 전환합니다. 한 손가락을 떼면 남은 손가락으로 끊김 없이 이동합니다.
- 핀치 중과 같은 터치 세션의 마지막 손가락을 뗄 때는 페이지 변경·빈 공간 닫기를 하지 않습니다. 모든 손가락을 뗀 뒤 기본 배율의 새 제스처부터 스와이프를 허용합니다.
- 확대 후 pointer 드래그로 이동하고 이미지·뷰포트 크기에 맞춰 경계를 제한합니다.
- 첫·마지막에서 이전·다음 이동을 멈춥니다.
- 로딩·오류·재시도·이미지 없음 상태를 표시합니다. 같은 src의 연속 이미지와 캐시 완료도 처리합니다. 이미지 배열과 활성 index는 호출부가 소유합니다.
- 전체 화면의 어두운 표면, 상단 도구, 좌우 탐색, 캡션과 하단 썸네일을 제공합니다.
- 이미지와 컨트롤을 제외한 빈 공간 클릭·터치로 닫습니다. 이미지 클릭과 드래그 이동은 닫기로 처리하지 않습니다.
- 기본 크기에서 터치·펜으로 중앙 이미지 영역 또는 빈 공간을 좌우 스와이프하면 손가락을 따라 현재 페이지와 인접 페이지가 함께 움직입니다. 충분한 거리 또는 빠른 플릭은 이동을 확정하며 짧거나 취소된 제스처는 제자리로 돌아옵니다.
- 버튼·썸네일·키보드 이동은 즉시 전환합니다. isAnimated는 스와이프 놓기 보정만 조절하며 false 또는 모션 감소 설정에서는 보정도 즉시 처리합니다.
- 확대 상태에서는 이동만 처리하고 스와이프 페이지 전환은 하지 않습니다.
- 닫기는 실제 빈 공간에서 시작하고 끝난 탭만 처리합니다. 컨트롤에서 시작한 입력과 짧은 드래그는 닫기에서 제외합니다.
- 모달 포커스 관리와 닫기 후 호출 요소 복귀를 유지합니다.

## 상태

- 닫힘
- 로딩
- 표시
- 확대/이동
- 이미지 두 번 탭 확대·초기화
- 두 손가락 핀치·한 손가락 이동 전환
- 순서 경계
- 오류/재시도
- 이미지 없음
- 같은 src 연속 이미지
- 전체 화면·모바일
- 썸네일 선택
- 스와이프·짧은 제스처 복귀
- 스와이프 놓기 보정 켜기·끄기

## 키보드

- 좌우 키로 이미지 이동
- 확대 후 Shift+방향키로 이미지 이동
- Escape 닫기
- Tab으로 확대·초기화 접근

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
- ResizeObserver
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
<ImageViewer images={images} index={index} onIndexChange={setIndex} isOpen={isOpen} onOpenChange={setIsOpen} isAnimated={true} trigger={<Button>보기</Button>} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
