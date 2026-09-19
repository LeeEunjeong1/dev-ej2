---
title: "[Android/Compose] ExoPlayer + VerticalPager로 쇼츠(Shorts) UI 구현하기 (feat. 비디오 트래킹)"
source: "https://dev-ej2.tistory.com/114"
tistory_id: "114"
published: "2026-03-09T07:13:03"
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
    //   핵심: 현재 페이지 앞뒤를 미리 로드하여 로딩 지연을 최소화합니다.
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

### 3. 정교한 시청 트래킹(Tracking) 로직

단순히 "영상을 봤다"가 아니라, "실제로 얼마나 노출되었는가"와 "실제로 얼마나 재생되었는가"를 구분하여 측정하는 로직을 구현했습니다.

#### 측정 항목:

1. **Exposure Time(노출 시간)**: 영상이 화면에 머무른 총 시간 (일시정지 상태 포함).
2. **Total Play Time(재생 시간)**: 비디오가 실제로 재생된 시간.
3. **Completion Rate(완주 여부)**: 영상 끝까지 시청했는지 여부.

Kotlin

```
val processAndSend = {
    val now = System.currentTimeMillis()
    // 1. 노출 시간 계산: 화면 활성화 시점부터 현재까지
    if (trackingData.activeStartTime > 0) {
        trackingData.exposureTime += (now - trackingData.activeStartTime)
        trackingData.activeStartTime = 0L 
    }
    // 2. 재생 시간 계산: 실제 재생 버튼(isShowing)이 활성화된 기간
    if (trackingData.lastPlayStartTime > 0) {
        trackingData.totalPlayTimeMs += (now - trackingData.lastPlayStartTime)
        trackingData.lastPlayStartTime = 0L
    }
    // 3. 데이터 전송 (노출 시간이 있는 경우에만)
    if (trackingData.exposureTime > 0) {
        onTrackingResult(trackingData.copy())
        trackingData.reset()
    }
}
```

---

### 4. 성능 최적화: 인터넷이 느린 환경 대응

네트워크 환경이 좋지 않은 곳에서도 영상이 빨리 시작되도록 LoadControl을 커스텀하게 설정했습니다.

Kotlin

```
val exoPlayer = remember {
    ExoPlayer.Builder(context)
        .setLoadControl(
            DefaultLoadControl.Builder()
                // 재생 시작 전 최소 버퍼를 줄여 응답 속도를 높임 (단위: ms)
                .setBufferDurationsMs(
                    2500, // minBuffer
                    5000, // maxBuffer
                    1000, // bufferForPlayback (1초만 모이면 바로 재생!)
                    1500  // bufferForPlaybackAfterRebuffer
                ).build()
        ).build()
}
```

### 5. 주요 구현 팁

- **key 활용**: key(video.id, retryKey)를 사용하여 영상 아이템이 바뀌거나 재시도할 때 플레이어 상태를 명확히 초기화합니다.
- **beyondViewportPageCount = 1**: 이 설정을 통해 다음 영상을 유저 몰래 미리 로딩(Prepare)하여, 스와이프 시 딜레이 없이 영상이 터지도록 UX를 개선했습니다.
- **AndroidView 사용**: Compose 환경에서 기존 View 기반인 PlayerView를 사용하기 위해 AndroidView로 브릿지를 구현하고, update 블록을 통해 컨트롤러 노출 여부를 동적으로 제어했습니다.
