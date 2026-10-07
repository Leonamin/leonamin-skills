---
name: agent-browser
description: 웹 페이지·로컬 개발 서버를 agent-browser CLI로 조작·검증하거나 화면 캡처·PDF·렌더링된 내용을 추출할 때 사용한다.
---

# Agent Browser

**실제 렌더링과 주요 동작을 확인하고 URL·결과·캡처 경로를 보고한다.**

## 실행과 조작

- 첫 작업 전 `agent-browser --version`으로 설치를 확인하고 OS·런타임 설정을 살핀다. 명령이 불확실하면 `agent-browser <command> --help` 또는 `agent-browser skills get core`를 읽는다.
- 브라우저가 없으면 `agent-browser install`, Linux 공유 라이브러리가 없으면 `agent-browser install --with-deps`를 사용한다.
- 작업별 고유 세션을 정하고 모든 명령에 같은 `--session <name>`을 사용한다. 여러 사이트를 분리할 때는 세션을 나누며 `agent-browser session list`로 확인한다.

```bash
agent-browser --session <name> open <url>
agent-browser --session <name> wait --text "준비된 화면의 문구"
agent-browser --session <name> snapshot -i
agent-browser --session <name> click @e1
agent-browser --session <name> snapshot -i
```

- 준비 상태는 실제 요소·문구로 확인한다. 네트워크가 멈추는 페이지에는 `wait --load networkidle`도 사용할 수 있다.
- snapshot의 refs(`@e1` 등)로 `click`, `fill @e2 "text"`, `press Enter`를 실행한다. 이동·제출·모달·DOM 변경 뒤에는 새 snapshot을 얻는다.
- 필요하면 시맨틱 locator를 쓴다: `find label "Email" fill "user@example.com"`, `find role button click --name "Submit"`.

## 캡처와 검증

아래 명령에도 작업 세션을 지정한다.

| 목적 | 명령 |
| --- | --- |
| 화면·전체 화면·컨트롤 표시 | `screenshot <path>.png`, `screenshot --full <path>.png`, `screenshot --annotate <path>.png` |
| PDF·본문·위치 | `pdf <path>.pdf`, `get text body`, `get url`, `get title` |
| 반응형 확인 | `set viewport <width> <height>` 후 snapshot·캡처 |

- 개발 서버는 실제 화면과 주요 상호작용을 확인하고 screenshot을 남긴다. 미검증 동작과 실행 실패는 구분해 보고한다.
- 끝나면 해당 작업 세션만 `close`한다.
- 비밀번호·쿠키·인증 상태·키를 캡처·로그·커밋에 노출하지 않는다. 재사용 인증이 명시적으로 필요할 때만 상태를 저장하고, 임시 상태는 저장소 밖에 두고 사용 후 삭제한다.
- sandbox를 기본 유지한다. `No usable sandbox`는 런타임 지원을 먼저 확인하며, 명시적으로 필요한 격리 환경에서만 `--no-sandbox`를 사용한다. 설치 후에도 실행이 실패하면 정확한 오류와 환경 제약을 보고한다.
