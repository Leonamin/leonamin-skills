# DESIGN.md 형식과 명령

**YAML에는 규범적 토큰을, 본문에는 적용 이유와 규칙을 둔다.**

[공식 명세](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md)는 alpha 형식이므로 형식·도구 호환 문제가 생기면 현재 명세와 사용하는 CLI 버전을 확인한다.

## 토큰

명세에서 YAML은 선택 사항이며, 이 스킬로 기계 판독 가능한 토큰을 관리할 때는 파일 최상단의 `---` 블록을 사용한다.

```yaml
version: alpha
name: Product name
colors: {}
typography: {}
rounded: {}
spacing: {}
components: {}
```

`description`은 선택 항목이다. 참조는 `{path.to.token}`을 사용하고, 기본 토큰은 값으로 연결한다. 컴포넌트 안에서는 `{typography.label}` 같은 복합 참조도 가능하다. 필요한 상태는 `button-primary-active`처럼 별도 컴포넌트로 정의한다.

## 본문

`##` 섹션은 `Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts` 순서로 둔다. 해당하지 않는 섹션은 생략하며 일반론으로 채우지 않는다. 선택적인 `omitted`에 생략 섹션과 이유를 기록할 수 있다. 추가 설명·`Known Gaps`는 뒤에 둔다.

## 명령

```sh
npx @google/design.md lint DESIGN.md
npx @google/design.md diff DESIGN-before.md DESIGN.md
npx @google/design.md export --format dtcg DESIGN.md
```

끊긴 참조는 해결하고 대비·미사용 토큰·타이포·섹션 순서 경고는 실제 근거와 대조한다. 형식 검증은 UI 구현이나 실제 접근성·반응형 동작의 검증을 대체하지 않는다.
