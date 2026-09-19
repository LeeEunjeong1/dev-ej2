---
title: "Compose / TopAppBar Title 가운데 정렬 - CenterAlignedTopAppBar"
source: "https://dev-ej2.tistory.com/61"
tistory_id: "61"
published: "2023-07-18T01:19:10+09:00"
tags:
---
Material3의 CneterAlignedTopAppBar - TopAppBar Title을 가운데 정렬할 수 있다

```
@ExperimentalMaterial3Api
@Composable
fun CenterAlignedTopAppBar(
    title: @Composable () -> Unit,
    modifier: Modifier = Modifier,
    navigationIcon: @Composable () -> Unit = {},
    actions: @Composable RowScope.() -> Unit = {},
    windowInsets: WindowInsets = TopAppBarDefaults.windowInsets,
    colors: TopAppBarColors = TopAppBarDefaults.centerAlignedTopAppBarColors(),
    scrollBehavior: TopAppBarScrollBehavior? = null
): Unit
```

![](https://blog.kakaocdn.net/dna/cFsrHu/btsnZBDh33G/AAAAAAAAAAAAAAAAAAAAAH1vGTCH4MLAe67AzA5xrxGFZLLnoT579ufSpQsb1TSu/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1790780399&allow_ip=&allow_referer=&signature=lq8xQs40zyT5Bk1%2B1Uasql7p6rE%3D)

<https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary>

[androidx.compose.material3  |  Android Developers

androidx.car.app.managers

developer.android.com](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary)
