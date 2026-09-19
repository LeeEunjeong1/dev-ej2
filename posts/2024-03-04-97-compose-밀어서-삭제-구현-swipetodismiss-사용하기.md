---
title: "Compose / 밀어서 삭제 구현 SwipeToDismiss 사용하기"
source: "https://dev-ej2.tistory.com/97"
tistory_id: "97"
published: "2024-03-04T11:20:55+09:00"
tags:
---
Compose SwipeToDismiss를 사용하면 밀어서 삭제를 간단하게 구현할 수 있다.

```
LazyColumn(modifier = Modifier.fillMaxHeight()) {
        items(
            items = tempList,
            key = { temp -> temp.no}
        ) { item ->
            val currentItem by rememberUpdatedState(newValue = item)

            SwipeToDismiss(
                state = rememberDismissState(confirmStateChange = {
                    if(it == DismissValue.DismissedToStart){
                    // 밀었을때 액션
                    }
                    true
                }),
                directions = setOf(DismissDirection.EndToStart), 
                background = { Box(modifier = Modifier.height(0.dp))},
                dismissContent = {
                    Text(
                        text = item.contents
                        fontSize = dpToSp(dp = 16.dp),
                        color = if (item.flagRead == "N") color_0c0d0e else color_717679,
                        fontFamily = getRobotoFontFamily(),
                        fontWeight = FontWeight.Bold
                    )
                },
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(horizontal = 16.dp, vertical = 8.dp)
            )
        }
    }
```
