---
title: "Compose / HorizontalPager swipe/drag/scroll 막기"
source: "https://dev-ej2.tistory.com/69"
tistory_id: "69"
published: "2023-08-02T17:27:12+09:00"
tags:
---
HorizontalPager 를 사용하는데, swipe 기능을 막고 싶었다.

modifier.scrollable(enabled=false) 가 작동하지 않아.. 일시적으로 막는 방법을 따로 구현하였다. (찾았다)

```
@ExperimentalPagerApi
fun PagerState.disableScrolling(scope: CoroutineScope) {
    scope.launch {
        scroll(scrollPriority = MutatePriority.PreventUserInput) {
            // Await indefinitely, blocking scrolls
            awaitCancellation()
        }
    }
}

@ExperimentalPagerApi
fun PagerState.enableScrolling(scope: CoroutineScope) {
    scope.launch {
        scroll(scrollPriority = MutatePriority.PreventUserInput) {
            // Do nothing, just cancel the previous indefinite "scroll"

        }
    }
}

// 스와이프 막기
val coroutineScope = rememberCoroutineScope()
val pagerState = rememberPagerState()
pagerState.disableScrolling(scope = coroutineScope)

// 스와이프 허용 
pagerState.enableScrolling(coroutineScope)
delay(100)
pagerState.scrollToPage(index)
pagerState.disableScrolling(coroutineScope)
```

disableScrolling 에선 액션을 cancle하고, enableScrolling에서는 scroll 액션시 아무것도 하지 않음으로써 scroll을 허용해주었다.

필요한 곳에서 사용하되, enable한 후 다시 disable을 하여 터치 시에만 일시적으로 page이동이 되게 허용해주었다.

<https://github.com/google/accompanist/issues/756>

[HorizontalPager from 0.19 no more support dragEnabled · Issue #756 · google/accompanist

Is this what was planned? Because I have not found any mention about removing dragEnabled. For example, if im using HorizontalPager for images, which are able to zoom, i was disable dragging to pre...

github.com](https://github.com/google/accompanist/issues/756)
