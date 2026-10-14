# Tabs

밑줄·확장형·분할형·하단형으로 같은 콘텐츠 전환 계약을 제공합니다.

## 동작 계약

- underline(기본), adaptive, segmented, bottom 네 가지 시각 변형 제공
- 방향키 이동과 선택 확정을 분리하는 수동 활성화: Enter·Space로 확정
- value/onValueChange 제어형과 defaultValue 비제어형 모두 지원
- adaptive는 아이콘을 유지하고 활성 탭의 실제 라벨 너비를 측정해 180ms로 확장. 아이콘이 없는 항목은 이름을 항상 표시
- 숫자 배지는 접근 가능한 이름에 개수를 포함하며, 비활성 항목은 탐색·선택에서 제외
- 좁은 화면·긴 한국어는 탭 줄만 가로 스크롤. 화면보다 긴 활성 이름은 말줄임 처리하며 접근 가능한 전체 이름 유지. 포커스 여백 확보, 키보드 탐색한 탭을 시야 안으로 이동
- 모션 감소 설정에서는 너비 애니메이션 제거
- bottom도 탭 패널 전환. 별도 페이지 탐색은 Link 기반 navigation으로 구현

## 상태

- 네 가지 변형
- 활성·비활성·키보드 포커스
- 아이콘·개수 배지
- 긴 한국어
- 320px 좁은 화면
- 모션 감소
- 제어형·비제어형

## 키보드

- 좌우 방향키/Home/End: 사용 가능한 탭으로 포커스 이동
- Enter/Space: 포커스한 탭 활성화
- Tab: 활성 패널로 이동
- 활성화 전에는 현재 패널 유지

## 직접 관련 파일

- assets/src/components/overlays/tabs.tsx
- assets/src/styles/tabs.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/overlays/tabs.tsx
- assets/src/styles/basic.css
- assets/src/styles/composed.css
- assets/src/styles/global.css
- assets/src/styles/overlays.css
- assets/src/styles/tabs.css
- assets/src/styles/toast.css
- assets/src/styles/tokens.css

상대 import와 공유 모듈의 다른 export 때문에 직접 사용하는 컴포넌트보다 범위가 넓을 수 있습니다.

## 외부 패키지

radix-ui, react, react-dom

참조 버전은 배포본 루트 manifest.json의 packageVersions를 확인합니다.

## 카탈로그 의존성 설명

- react
- react-dom
- radix-ui

## 코드 위치

- TabsItem: assets/src/components/overlays/tabs.tsx:10-17
- TabItem: assets/src/components/overlays/tabs.tsx:18-18
- TabsVariant: assets/src/components/overlays/tabs.tsx:19-19
- TabsProps: assets/src/components/overlays/tabs.tsx:20-27
- Tabs: assets/src/components/overlays/tabs.tsx:94-190

## 이식

1. assets/src/components/overlays/tabs.tsx와 assets/src/styles/tabs.css를 복사하고 React·Radix UI를 설치합니다.
2. 진입점에서 tabs.css를 가져오고 --gc-* 토큰을 프로젝트 디자인 토큰에 연결합니다. --gc-focus-clearance는 최소 6px을 권장합니다.
3. items의 value는 안정적인 식별자, label은 읽을 수 있는 이름으로 지정합니다. icon은 프로젝트 아이콘을 ReactNode로 전달하며 특정 아이콘 패키지 의존성은 없습니다.
4. variant를 선택합니다. adaptive 아이콘 항목만 활성 이름이 확장되고, 아이콘 없는 항목은 전체 이름을 유지합니다.
5. 외부 상태가 필요하면 value와 onValueChange를 함께 연결합니다. 기존 defaultValue·items 호출은 그대로 사용 가능합니다.
6. 긴 한국어·disabled·320px·키보드 포커스·prefers-reduced-motion을 원본 데모와 비교합니다.

## 사용 예제

```tsx
<Tabs items={items} defaultValue="overview" />
<Tabs variant="adaptive" label="작업 탭" items={items} value={tab} onValueChange={setTab} />
// item: { value, label, content, icon?, badge?, isDisabled? }
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
