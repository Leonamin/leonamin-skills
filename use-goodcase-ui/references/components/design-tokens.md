# Design Tokens

색상·타이포그래피·간격·밀도를 프로젝트에 맞게 연결하는 기준입니다.

## 동작 계약

- assets/src/styles/tokens.css가 실행 토큰의 원본입니다.
- --gc-* 의미 토큰을 프로젝트 변수에 연결해 외형을 변경합니다.
- Portal 콘텐츠도 같은 토큰을 읽도록 문서 범위 또는 Portal 컨테이너에 테마를 공급합니다.
- 테마와 밀도는 동작을 바꾸지 않습니다.

## 상태

- Blue 기본 테마
- Forest 변형
- 라이트 모드
- 다크 모드
- 기본 밀도
- 조밀한 밀도

## 키보드

- 테마·밀도 선택은 네이티브 select로 조작합니다.

## 직접 관련 파일

- assets/src/styles/tokens.css

## 포함 코드와 공유 스타일

- assets/src/styles/tokens.css

상대 import와 공유 모듈의 다른 export 때문에 직접 사용하는 컴포넌트보다 범위가 넓을 수 있습니다.

## 외부 패키지

없음 (CSS custom properties)

참조 버전은 배포본 루트 manifest.json의 packageVersions를 확인합니다.

## 카탈로그 의존성 설명

- CSS custom properties

## 코드 위치



## 이식

1. tokens.css의 --gc-* 목록을 확인합니다.
2. 의미가 같은 프로젝트 토큰을 연결합니다. 없는 토큰은 프로젝트 디자인 기준으로 정의합니다.
3. 브랜드 색상·폰트·간격·모서리를 바꾼 뒤 텍스트 대비와 포커스 가시성을 확인합니다.
4. 모달·메뉴처럼 Portal로 렌더링되는 요소에도 변경이 적용되는지 확인합니다.

## 사용 예제

```css
:root {
  --gc-accent: var(--brand-primary);
  --gc-font-sans: var(--font-body);
  --gc-radius: var(--radius-control);
}
```

예제의 import, 데이터, 상태, callback은 대상 프로젝트에서 제공합니다. 갤러리 데모는 배포본에 포함되지 않습니다.
