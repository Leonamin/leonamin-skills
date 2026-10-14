# Toast

테마 표면을 따르는 알림과 하나의 시계로 동기화된 자동 닫힘 타이머

## 동작 계약

- 기본 배경은 --gc-surface이며 밝은/어두운 테마에 따라 변경됩니다. tinted와 solid는 선택적 표현입니다.
- 아이콘·제목 첫 줄·닫기 버튼은 동일한 24px 행으로 정렬합니다. 설명·액션은 제목 아래에 배치합니다.
- timer는 bar/circle/none을 지원합니다. none은 시각적 표현만 숨기며 자동 닫힘은 동일합니다.
- info/success/warning은 기본 5초 후 닫힙니다. error 또는 action이 있으면 기본은 수동 닫기이며 가짜 타이머를 표시하지 않습니다.
- durationMs를 양수로 지정하면 오류·액션도 명시적으로 자동 닫힘을 선택합니다. 0·음수·Infinity는 지속 알림입니다.
- performance.now 기반 단일 시계와 종료 setTimeout이 남은 시간을 관리합니다. WAAPI 애니메이션을 같은 시계의 currentTime에 맞춰 동기화하며 프레임마다 React를 갱신하지 않습니다. 접근성 남은 시간은 DOM에서 1초마다 갱신합니다. 모션 감소 설정에서는 같은 간격으로 시각적 남은 시간도 갱신합니다.
- 개별 카드의 호버·내부 포커스만 그 카드의 시간을 일시정지합니다. document.hidden은 모든 카드에 적용합니다. 목록 전체 호버는 다른 카드의 시간을 멈추지 않습니다.
- stack은 목록 호버 또는 키보드 포커스로 펼쳐집니다. 접힌 뒤쪽 카드는 inert/aria-hidden이며 읽기 전 시간도 일시정지합니다. 펼치기 자체는 다른 카드의 타이머를 멈추지 않습니다. up은 화면 하단에서 아래→위 진입, down은 화면 상단에서 위→아래 진입입니다. 닫기는 오른쪽으로 180ms 이동하며 퇴장 완료 후 제거합니다. 모션 감소 설정은 즉시 닫습니다. 알림 생성은 포커스를 가져가지 않습니다. 닫기 버튼은 항상 접근 가능하며 원형은 호버·포커스 때 X를 보여줍니다. 터치에서는 X를 유지합니다.
- 여러 알림은 안정적인 UUID로 관리합니다. list는 전체 목록, stack은 먼저 도착한 N개만 표시하고 나머지는 FIFO 대기열로 보존하며 대기 개수 안내는 표시하지 않습니다. 카드 제거 후 남은 카드는 현재 화면 위치에서 220ms 동안 빈자리로 이동합니다. 모션 감소 설정에서는 즉시 재배치합니다.

## 상태

- info
- success
- warning
- error
- surface
- tinted
- solid
- bar
- circle
- none
- 일시정지
- 지속 알림
- 긴 제목
- 액션
- 모바일

## 키보드

- F8로 알림 목록에 포커스
- Tab으로 닫기·액션 이동
- Escape로 포커스한 알림 닫기
- 포커스 중 타이머 일시정지

## 직접 관련 파일

- assets/src/components/overlays/toast.tsx
- assets/src/styles/toast.css
- assets/src/components/basic/index.tsx

## 포함 코드와 공유 스타일

- assets/src/components/basic/index.tsx
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
- radix-ui Toast
- lucide-react
- basic/Button·IconButton compact
- --gc-* 토큰

## 코드 위치

- ToastMessage: assets/src/components/overlays/toast.tsx:14-22
- ToastLayout: assets/src/components/overlays/toast.tsx:23-23
- ToastDirection: assets/src/components/overlays/toast.tsx:24-24
- useToast: assets/src/components/overlays/toast.tsx:28-32
- ToastProvider: assets/src/components/overlays/toast.tsx:384-574
- ToastPreview: assets/src/components/overlays/toast.tsx:575-601
- Button: assets/src/components/basic/index.tsx:15-45
- IconButton: assets/src/components/basic/index.tsx:46-66
- Link: assets/src/components/basic/index.tsx:67-82
- FieldProps: assets/src/components/basic/index.tsx:83-87
- TextField: assets/src/components/basic/index.tsx:88-116
- TextArea: assets/src/components/basic/index.tsx:117-169
- Checkbox: assets/src/components/basic/index.tsx:170-200
- RadioGroup: assets/src/components/basic/index.tsx:201-233
- Switch: assets/src/components/basic/index.tsx:234-258
- Badge: assets/src/components/basic/index.tsx:259-267
- Alert: assets/src/components/basic/index.tsx:268-303
- Skeleton: assets/src/components/basic/index.tsx:304-318
- Progress: assets/src/components/basic/index.tsx:319-450
- Image: assets/src/components/basic/index.tsx:451-494
- Avatar: assets/src/components/basic/index.tsx:495-517
- Card: assets/src/components/basic/index.tsx:518-534
- Table: assets/src/components/basic/index.tsx:535-574
- Pagination: assets/src/components/basic/index.tsx:575-622
- Typography: assets/src/components/basic/index.tsx:623-637
- Stack: assets/src/components/basic/index.tsx:638-652
- Grid: assets/src/components/basic/index.tsx:653-670
- Divider: assets/src/components/basic/index.tsx:671-673

## 이식

1. toast.tsx와 toast.css를 가져오고 basic/Button·IconButton import 경로를 맞춥니다.
2. 앱 루트에 ToastProvider를 한 번 배치하고 layout·stackSize·direction을 설정하고 호출부에서 useToast().notify를 사용합니다.
3. --gc-surface/text/border와 상태별 토큰을 프로젝트의 밝은/어두운 테마 토큰에 연결합니다.
4. --gc-toast-control-size와 --gc-toast-title-line-height는 둘 다 24px로 유지합니다.
5. 기존 notify({title,description,tone,action}) 호출은 그대로 작동합니다. timer·appearance·durationMs는 선택적 확장입니다.
6. 갤러리의 정적 ToastPreview와 실제 notify 예제를 구분합니다. 업무 API는 알림 내부에 연결하지 않습니다.

## 사용 예제

```tsx
notify({ title: "저장했습니다", tone: "success", timer: "circle", appearance: "surface" });
notify({ title: "저장 실패", tone: "error", action: { label: "재시도", onClick: retry } });
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
