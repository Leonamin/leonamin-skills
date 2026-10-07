---
name: git-workflow
description: 브랜치·커밋·push·PR·병합 작업에 저장소 정책과 한국어 작성 규칙을 적용할 때 사용한다.
---

# Git 작업 규칙

**사용자 변경을 보존하고 저장소 정책에 맞춰 변경을 커밋·전달한다.**

- 현재 브랜치·작업 트리와 로컬 AGENTS.md/CLAUDE.md를 확인하고 무관한 변경을 보존한다.
- 브랜치 이름·보호·PR base·병합 방식은 사용자 지시와 저장소 문서·설정을 따른다. 중요한 모호함만 확인하며 squash·merge를 일괄 강제하지 않는다. 별도 정책이 없으면 main/master/develop 대신 작업 브랜치와 PR을 사용한다.
- 커밋 전 staged diff를 확인하고 목적에 맞는 Conventional Commits 타입을 선택한다: `feat`, `fix`, `refactor`, `chore`, `docs`, `test`, `ci`, `build`, `perf`, `revert`. 영역이 명확하면 짧은 scope를 쓴다.
- 커밋·PR은 한국어로 작성하고 제목은 명사형으로 끝낸다. 예: `refactor(review): 리뷰 관점 통합`.
- PR 제목은 최종 범위를, 본문은 문제·변경된 동작·검증·남은 위험을 설명한다. 저장소 템플릿과 환경에 맞는 생성 도구를 사용한다.
- 브랜치·파일 격리가 필요할 때 워크트리를 사용한다. 작업 수만으로 워크트리나 중간 커밋을 늘리지 않는다.
- Git 작업 권한을 배포·운영 데이터 변경 권한으로 확대하지 않는다.
