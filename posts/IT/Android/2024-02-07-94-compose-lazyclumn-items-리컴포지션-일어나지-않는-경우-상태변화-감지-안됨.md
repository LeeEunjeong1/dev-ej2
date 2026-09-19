---
title: "Compose / LazyClumn items 리컴포지션 일어나지 않는 경우 (상태변화 감지 안됨)"
source: "https://dev-ej2.tistory.com/94"
tistory_id: "94"
published: "2024-02-07T15:39:15+09:00"
category: "IT/Android"
tags:
---
items에 넣은 List의 해시값이 변해도 이미 그려놓은 리스트는 해시값이 변경된걸 모른다.

리컴포지션일 일어나게 하기 위해서는 items에 key값을 지정해줘서, 리스트가 변경될때 키값 변경이 감지되도록 해야한다.

items 함수를 살펴보자.

```
inline fun <T> LazyListScope.items(
    items: List<T>,
    noinline key: ((item: T) -> Any)? = null,
    noinline contentType: (item: T) -> Any? = { null },
    crossinline itemContent: @Composable LazyItemScope.(item: T) -> Unit
) = items(
    count = items.size,
    key = if (key != null) { index: Int -> key(items[index]) } else null,
    contentType = { index: Int -> contentType(items[index]) }
) {
    itemContent(items[it])
}
```

items 함수에서 Key값을 인자로 받는걸 알 수 있다.

```
/* Compose */
val tempList = remember { viewModel.tempList }
LazyColumn(modifier = Modifier.fillMaxHeight()) {
        items(
            items = tempList,
            key = { temp -> temp.no} // key값 지정 
        ) {
        
        }
 }
 
/* viewModel*/
var tempList = mutableStateListOf(Temp())
   private set
   
// delete
tempList.remove(item)

// update
val position = tempList.indexOf(temp)
tempList[position] = temp.copy(flag = "Y")
```

items에 list와 key값을 넘겨주었다.

이제 list 안의 아이템을 delete, update 하면 주소값이 바뀌게 되어 변경값을 감지할 수 있다.

update 할때는 객체 자체를 변하게 하기 위해 copy한 후에 업데이트를 해주었다.
