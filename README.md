# dev-ej2 Tistory backup

[`dev-ej2.tistory.com`](https://dev-ej2.tistory.com/)의 공개 글을 GitHub에 자동 백업합니다.

- GitHub Actions가 매주 월요일 오전 3시(KST)에 사이트맵을 확인합니다.
- 사이트맵에 포함된 모든 공개 글 페이지를 백업합니다.
- 새 글과 수정된 글을 `posts/대분류/소분류/`에 Markdown으로 저장합니다.
- 카테고리가 없는 글은 `posts/미분류/`에 저장합니다.
- 카테고리가 변경되면 기존 파일을 새 카테고리 폴더로 이동합니다.
- **Actions → Backup Tistory posts → Run workflow**에서 즉시 실행할 수도 있습니다.

## 티스토리 설정

별도의 RSS 공개 범위 설정 없이 공개 글을 백업합니다.

## 제한 사항

티스토리 사이트맵에 포함된 공개 글만 동기화됩니다. 티스토리에서 삭제하거나 비공개로 전환한 글도 GitHub에서는 자동 삭제하지 않습니다.
