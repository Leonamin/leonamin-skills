# 웹 Storybook 구성과 상태 재현

목표는 UI를 상태별로 직접 열어 검토하고, 독립된 컴포넌트와 실제 부모 안에서의 조합을 모두 확인하는 것이다. 정적 배포 가능한 Storybook도 실행되는 UI다. 소스 분석이나 정적 build 통과만으로 렌더링 검증을 대신하지 않는다.

## 적용과 연동

- 웹 프론트엔드이면 기본 적용한다. 비웹은 생략하고, 명시적인 제외 요청은 따른다. 기존 Storybook이 있으면 확장한다.
- 프로젝트의 프레임워크, 빌더, 패키지 매니저와 설치 버전에 맞는 공식 연동을 사용한다. 특정 최신 버전이나 addon API를 고정하지 말고 적용 시 호환 문서를 확인한다.
- 개발 실행과 정적 build 명령을 제공한다. 정적 산출물에서도 필요한 폰트, 이미지, mock 리소스가 로드되게 구성한다. 외부 호스팅은 별도 요청이 있을 때 수행한다.
- 앱의 실제 토큰, 전역 스타일, 폰트와 theme/provider를 공유한다. Storybook만의 유사한 디자인 시스템이나 화면 구현을 만들지 않는다.

## 탐색 구조와 파일 소유권

기존 명명 체계가 있으면 아래 구분을 그 체계에 반영한다. 스토리는 대상 코드 가까이에 두며, sidebar 분류와 물리적 파일 경로가 반드시 같을 필요는 없다.

```text
Primitives/Button
Primitives/TextField
Shared/Layout/Container
Shared/Patterns/EmptyState
Domains/Orders/Components/OrderSummary
Domains/Orders/Components/PaymentPanel
Domains/Orders/Screens/OrderDetail
```

프리미티브는 실제 사용하는 variant와 의미 있는 상태를, 도메인 컴포넌트는 업무 데이터/상태를 보여준다. 화면은 실제 앱 레이아웃과 도메인 컴포넌트 조합을 보여준다. 내부의 모든 짧은 JSX 조각마다 스토리를 만들 필요는 없지만, 별도로 검토하는 주요 프래그먼트에는 단독 스토리와 부모에서의 재현을 함께 제공한다.

## 부모와 자식을 함께 검토하는 계약

예를 들어 주문 상세에 개요/결제/이력 탭이 있으면 다음을 모두 충족한다.

1. `OrderDetail` 화면 스토리 안에서 실제 탭을 전환해 각 프래그먼트를 볼 수 있다.
2. `Overview`, `PaymentSuccess`, `PaymentEmpty`, `PaymentError`, `HistoryLoading`처럼 탭과 의미 있는 상태를 지정한 부모 화면 스토리가 있다. 각 스토리를 직접 열면 수동 클릭 없이 해당 탭/상태가 보인다.
3. `PaymentPanel` 단독 스토리에서도 같은 결제 상태를 검토할 수 있다.
4. 부모 스토리는 실제 `OrderDetail`을 렌더링한다. header, 탭, content width, padding, scroll 영역과 주변 요소를 유지한다. 자식에 가짜 테두리를 둘러 부모 화면이라고 이름 붙이지 않는다.

**금지:** 부모 스토리에는 기본 탭만 표시하고 나머지 상태는 자식 스토리에서만 제공하기, 탭이 클릭되지 않는 부모 목업, 부모와 자식을 위해 UI 구현을 복제하기.

필요한 레이아웃/provider는 decorator나 공용 harness로 제공한다. 실제 앱이 이미 shell을 포함하면 중복으로 씌우지 않는다. 서버 렌더링 경계로 전체 route를 가져올 수 없다면 앱과 스토리가 같은 화면 조합 컴포넌트를 사용하도록 분리하고, Storybook에서 검증하지 못한 서버 경계를 명시한다.

## 상태 설정과 안정성

- 화면별로 `탭/단계 × 필요한 상태 → 부모 스토리 → 관련 자식 스토리` 대응을 간결하게 기록한다. 기존 인벤토리나 스토리 문서를 사용하며 별도 대형 관리 문서를 요구하지 않는다.
- 실제 앱의 상태 진입점을 이용한다: route/query, controlled props/args, 초기 store/provider 상태, 데이터 adapter 또는 네트워크 mock. Storybook 전용 boolean 분기로 제품 코드의 렌더링을 바꾸지 않는다.
- 숨겨진 패널을 CSS로 강제 노출하거나 문서 설명만 추가하는 것은 상태 재현이 아니다. 초기 상태 스토리와 별개로 실제 탭 클릭/단계 이동도 검증한다.
- 클릭으로만 진입 가능한 일시적 상태는 해당 버전의 interaction/play 기능 등으로 결정적으로 재현할 수 있다. 완료를 기다려 상태를 확인하고 임의의 sleep에 의존하지 않는다. 직접 초기화할 수 있는 상태는 매번 긴 클릭 시나리오를 거치지 않게 한다.
- 정상·로딩·빈 결과·오류·권한 제한·검증 오류 중 제품에서 실제 발생하는 상태를 다룬다. 모든 상태/viewport의 조합을 무조건 곱하지 말고 각 탭의 고유 상태와 레이아웃 위험을 빠뜨리지 않는다.
- 부모와 자식은 도메인 fixture와 mock 계약을 공유한다. 부모 스토리에서 자식 자체를 mock으로 대체하지 말고 데이터/외부 서비스 경계를 mock한다.
- 날짜/ID/데이터는 재현 가능하게 고정하고 router, store, query cache는 스토리마다 초기화한다. 로딩은 잠깐 보였다가 사라지는 지연 대신 유지 가능한 상태로, 오류는 항상 재현 가능한 응답으로 만든다.
- 저장 등 액션은 mock 상태에서도 결과를 갱신한다. action 로그만 남기는 것은 동작 구현을 대신하지 않는다. 실제 계정·운영 데이터·유료 요청에 의존하지 않는다.

## 검증과 인계

정적 build 후 핵심 부모 스토리의 직접 URL을 열고 각 탭과 대표 상태를 확인한다. 특히 기본 탭이 아닌 상태를 새로고침하고, 탭 전환과 좁은 viewport에서 부모/자식의 정렬·잘림·스크롤을 확인한다. 관련 단독 스토리도 같은 상태와 일치하는지 확인한다. 브라우저/interaction 도구로 확인한 것과 build로만 확인한 것을 구분한다.

실행 명령, 탐색 분류, 주요 부모 상태 스토리, mock과 미검증 범위를 최종 인계에 포함한다. Storybook은 실제 앱 route에서의 사용자 흐름 검증을 대체하지 않는다.

## 공식 참고

구현할 때 설치 버전에 맞는 문서를 읽는다.

- [Stories와 렌더링 상태](https://storybook.js.org/docs/writing-stories/index)
- [Args와 상태 입력](https://storybook.js.org/docs/writing-stories/args)
- [네트워크 요청 mock](https://storybook.js.org/docs/writing-stories/mocking-data-and-modules/mocking-network-requests)
