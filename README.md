# dev-ej2 Tistory backup

[`dev-ej2.tistory.com`](https://dev-ej2.tistory.com/)의 공개 글을 GitHub에 자동 백업합니다.

- GitHub Actions가 30분마다 RSS를 확인합니다.
- 새 글과 수정된 글을 `posts/`에 Markdown으로 저장합니다.
- **Actions → Backup Tistory posts → Run workflow**에서 즉시 실행할 수도 있습니다.

## 티스토리 설정

티스토리 관리 화면의 RSS 설정을 **전체 공개**로 유지해야 본문 전체가 백업됩니다.

## 제한 사항

티스토리 RSS에 포함된 공개 글만 동기화됩니다. RSS 목록에서 사라진 오래된 글은 이미 백업된 상태로 유지되며, 티스토리에서 삭제한 글도 GitHub에서는 자동 삭제하지 않습니다.
