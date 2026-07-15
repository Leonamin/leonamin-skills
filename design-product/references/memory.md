# Memory 워크플로

디자인 memory는 대화가 아니라 저장소에 둔다.

## 파일

- design-product/memory/current-design-state.md: 세션 재개를 위한 현재 상태 요약
- design-product/memory/decision-log.md: 날짜별 결정과 근거
- design-product/memory/approved-patterns.md: 재사용할 패턴
- design-product/memory/rejected-patterns.md: 피할 패턴과 이유

## 기록할 내용

다음처럼 미래 디자인에 영향을 주는 결정을 기록한다.

- 정체성 보완
- 토큰 변경
- 컴포넌트 이름 결정
- 재사용할 페이지·플로우 패턴
- 명시적인 안티패턴
- 감사 발견 사항에 대한 의도적인 예외
- 디자인 산출물 인계에 필요한 결정

일상적인 구현 세부사항은 향후 디자인 작업에 영향을 줄 때만 기록한다.

## 스크립트 사용

다음처럼 항목을 추가한다.

~~~bash
python3 <skill-dir>/scripts/update_memory.py --path <repo> \
  --decision "상품 선택에는 편집형 비교 행을 사용한다." \
  --approved "문맥에 맞는 신뢰 문구에는 LocalNote를 사용한다." \
  --rejected "제품 페이지의 일반적인 3열 기능 그리드는 피한다."
~~~

긴 메모는 표준 입력으로 전달한다.

~~~bash
printf '%s\n' "결정 내용" | python3 <skill-dir>/scripts/update_memory.py --path <repo>
~~~

같은 작업을 계속한다면 memory를 갱신한 뒤 컨텍스트를 다시 렌더링한다.
