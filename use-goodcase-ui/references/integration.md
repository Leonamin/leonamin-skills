# 이식 지침

이 배포본은 React 19+와 TypeScript를 기준으로 한다. 실제 외부 import와 원본 프로젝트의 의존성 버전은 `../manifest.json`에 기록되어 있다. 각 컴포넌트 문서의 외부 패키지 목록과 대상의 설치 버전을 먼저 비교한다. 스킬을 읽는 것만으로 의존성이 설치되지는 않는다.

## 소스와 스타일

코드는 `../assets/src/components/`, 스타일은 `../assets/src/styles/`에 있다. 대상 프로젝트의 공용 UI 경로에 필요한 파일을 복사하고 상대 import를 맞춘다. 배포본의 `src/` 구조를 유지하면 모듈 간 상대 import도 유지된다. 같은 파일의 다른 export가 필요하지 않다면 관련 타입과 내부 helper를 확인한 뒤 추출한다.

스타일 순서는 tokens → global → basic → overlays → tabs → toast → composed다. 컴포넌트군별로 공유하는 스타일이므로 필요한 규칙과 해당 미디어 쿼리·keyframes를 함께 옮긴다. 반복 이식 시 같은 CSS를 중복 추가하지 않는다.

`global.css`에는 html/body, 기본 요소, focus-visible, 모션 감소 규칙이 있다. 기존 앱에 전체를 무조건 import하지 말고 프로젝트 전역 스타일과 비교해 필요한 규칙을 병합한다. `--gc-*`는 컴포넌트 스타일의 토큰이다. 기존 디자인을 유지할 경우 참조 토큰보다 나중에 프로젝트 토큰 매핑을 공급한다.

```css
:root {
  --gc-accent: var(--brand-primary);
  --gc-font-sans: var(--font-body);
  --gc-radius: var(--radius-control);
}
```

위 프로젝트 변수 이름은 예시다. 대상 프로젝트에 실제로 존재하는 변수를 사용한다. 기존 테마가 있다면 `data-theme`, `data-density`, `data-color-mode` 참조 변형을 그대로 강제하지 말고 프로젝트의 테마 신호에 맞춘다. Portal 오버레이도 같은 토큰을 읽을 수 있도록 문서 범위 또는 Portal 컨테이너에 토큰을 공급한다. 외부 포커스 링을 위한 `--gc-focus-clearance` 여백도 확보한다.

## 상태와 서비스

재사용 UI는 데이터·상태·event callback을 호출부에서 받는다. 제품의 API, 라우터, 업로드 adapter를 공용 UI 내부에 결합하지 않는다. 사용 예제의 `items`, `retry`, `value` 등 변수와 컴포넌트 import는 대상에서 제공한다. Toast는 앱의 적절한 공통 범위에 ToastProvider를 배치하고 useToast를 통해 호출한다.

## 검증 범위

개별 문서의 상태·키보드·동작 계약을 기준으로 이식 후 확인한다. 원본 코드가 들어 있다는 사실은 대상의 API 연동이나 런타임 동작을 증명하지 않는다. React 외의 프레임워크로 변환하면 동일한 계약을 별도로 구현하고 검증한다.
