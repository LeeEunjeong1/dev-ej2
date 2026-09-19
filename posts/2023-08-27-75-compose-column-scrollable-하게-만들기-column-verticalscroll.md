---
title: "compose / Column Scrollable 하게 만들기 (Column + verticalScroll)"
source: "https://dev-ej2.tistory.com/75"
tistory_id: "75"
published: "2023-08-27T22:28:34+09:00"
tags:
---
항목 목록을 표시하기 위해선 Column에 verticalScroll 보다 LazyColumn 이나 LazyRow가 더 효율적이다.

verticalScroll은 스크롤할 수 있는 간단한 방법을 제공한다.

scrollState를 사용하면 스크롤 위치를 변경하거나 현재 상태를 가져올 수 있다.

```
@Composable
private fun ScrollBoxesSmooth() {

    // Smoothly scroll 100px on first composition
    val state = rememberScrollState()
    LaunchedEffect(Unit) { state.animateScrollTo(100) }

    Column(
        modifier = Modifier
            .background(Color.LightGray)
            .size(100.dp)
            .padding(horizontal = 8.dp)
            .verticalScroll(state)
    ) {
        repeat(10) {
            Text("Item $it", modifier = Modifier.padding(2.dp))
        }
    }
}
```
