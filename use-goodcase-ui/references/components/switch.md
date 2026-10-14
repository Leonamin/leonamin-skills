# Switch

레이블이 유지되는 설정 켜짐·꺼짐

## 동작 계약

- 상태가 바뀌어도 label은 유지합니다.
- role="switch"와 checked로 설정 상태를 전달합니다.
- 저장·실패·처리 중 상태는 호출부에서 전달하며 즉시 저장을 추측하지 않습니다.
- 외부 포커스 링이 잘리거나 인접 요소를 가리지 않도록 부모 배치에 --gc-focus-clearance(기본 6px) 이상의 안전 여백·간격을 확보합니다.

## 상태

- 켜짐
- 꺼짐
- 비활성

## 키보드

- Tab으로 이동
- Space로 토글

## 직접 관련 파일

- assets/src/components/basic/index.tsx
- assets/src/styles/basic.css
- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/components/basic/index.tsx
- assets/src/styles/basic.css
- assets/src/styles/composed.css
- assets/src/styles/global.css
- assets/src/styles/overlays.css
- assets/src/styles/tabs.css
- assets/src/styles/toast.css
- assets/src/styles/tokens.css

상대 import와 공유 모듈의 다른 export 때문에 직접 사용하는 컴포넌트보다 범위가 넓을 수 있습니다.

## 외부 패키지

lucide-react, react, react-dom

참조 버전은 배포본 루트 manifest.json의 packageVersions를 확인합니다.

## 카탈로그 의존성 설명

- react (hooks, DOM rendering)
- lucide-react (Alert 닫기 아이콘; 다른 컴포넌트만 복사할 때 제거 가능)

## 코드 위치

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

1. assets/src/components/basic/index.tsx에서 필요한 export와 해당 타입을 복사하거나 전체 기본 컴포넌트 모듈을 가져옵니다.
2. assets/src/styles/basic.css의 해당 .gc-* 규칙과 tokens.css를 가져와 프로젝트 의미 토큰에 연결합니다.
3. 아래 사용 예제의 이벤트를 프로젝트 상태·서비스에 연결합니다. 데모 코드는 이식하지 않습니다.
4. 키보드, 긴 한국어, 비활성·오류 상태와 모바일 너비에서 동작 계약을 재확인합니다.

## 사용 예제

```tsx
<Switch label="이메일 알림" isChecked={isEnabled} onCheckedChange={setIsEnabled} />
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
