# 디자인 기억 기록

**기억 갱신을 요청받았을 때, 이후 디자인 판단에 영향을 주는 결정과 근거만 기록한다.**

기록 위치는 프로젝트의 기존 `design-product/memory/` 체계를 따른다.

- `current-design-state.md`: 현재 기준과 재개에 필요한 상태
- `decision-log.md`: 결정·날짜·근거
- `approved-patterns.md`, `rejected-patterns.md`: 재사용하거나 피할 패턴과 이유

일상적인 구현 세부사항이나 대화 전문은 제외한다. 확인한 정체성·토큰·컴포넌트·패턴 결정과 의도적인 예외를 필요한 파일에만 반영한다.

```bash
python3 <skill-dir>/scripts/update_memory.py --path <repo> \
  --decision "결정과 근거" \
  --approved "재사용할 패턴" \
  --rejected "피할 패턴과 이유"
```

이번 기록에 필요한 인자만 사용한다. 긴 결정은 표준 입력으로 전달할 수 있다. 후속 작업에 요약이 필요하면 `render_context.py`로 갱신된 컨텍스트를 확인한다.
