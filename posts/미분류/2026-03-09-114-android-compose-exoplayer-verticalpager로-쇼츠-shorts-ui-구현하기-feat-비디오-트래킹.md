---
title: "[Android/Compose] ExoPlayer + VerticalPager로 쇼츠(Shorts) UI 구현하기 (feat. 비디오 트래킹)"
source: "https://dev-ej2.tistory.com/114"
tistory_id: "114"
published: "2026-03-09T16:13:03+09:00"
category: "미분류"
tags:
---
최근 많은 앱에서 사용되는 '세로 스와이프형 비디오 피드'는 구현을 해보겠습니다.

Jetpack Compose의 VerticalPager와 ExoPlayer를 결합하여 비디오 피드 구현과 비디오 정보 트래킹을 해보겠습니다.

### 1. 전체 구조: VerticalPager 활용

쇼츠 UI의 핵심은 무한히 스와이프되는 페이지 구조입니다. Compose의 VerticalPager를 사용하면 이를 쉽게 구현할 수 있습니다.

Kotlin

```
VerticalPager(
    state = pagerState,
    modifier = Modifier.fillMaxSize().background(Color.Black),
    // 💡 핵심: 현재 페이지 앞뒤를 미리 로드하여 로딩 지연을 최소화합니다.
    beyondViewportPageCount = 1 
) { page ->
    ShortsVideoView(
        video = videoList[page],
        isActive = pagerState.currentPage == page, // 현재 화면에 보이는지 여부
        // ... 생략
    )
}
```

---

### 2. 비디오 플레이어의 생명주기와 리소스 관리

비디오 플레이어는 메모리와 코덱 자원을 많이 소모합니다. 따라서 컴포저블의 생명주기에 맞춰 자원을 확실히 해제하는 것이 중요합니다.

- **remember { ExoPlayer }**: 화면이 다시 그려질 때(Recomposition) 플레이어 객체가 계속 새로 생성되는 것을 방지합니다.
- **DisposableEffect**: 컴포저블이 화면에서 완전히 사라질 때(Dispose) exoPlayer.release()를 호출하여 자원을 반납합니다.
- **LifecycleEventObserver**: 사용자가 앱을 백그라운드로 보냈을 때 영상을 멈추고 트래킹 데이터를 정산하도록 라이프사이클을 감시합니다.

---
