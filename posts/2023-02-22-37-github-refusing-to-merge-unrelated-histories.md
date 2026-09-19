---
title: "Github / refusing to merge unrelated histories"
source: "https://dev-ej2.tistory.com/37"
tistory_id: "37"
published: "2023-02-22T18:43:20+09:00"
tags:
---
말그대로 머지하려는 브랜치가 서로 연관없다는 뜻

머지하려는 브랜치에서

git merge dev --allow-unrelated-histories 

명령어 입력해준 후 push하면 된다. (명령어가 직관적이어서 좋다 ㅎㅎ )
