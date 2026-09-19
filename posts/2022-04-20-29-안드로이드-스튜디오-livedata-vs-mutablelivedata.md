---
title: "안드로이드 스튜디오 / LiveData vs MutableLiveData"
source: "https://dev-ej2.tistory.com/29"
tistory_id: "29"
published: "2022-04-20T18:34:13+09:00"
tags:
---
**LiveData : get만 가능**

**MutableLiveData : get,set 가능**

view와 viewModel의 역할 분리를 명확히 하기 위해서 위와 같이 사용한다.

viewModel 내에서는 데이터를 수정할 수 있도록 하고, view는 바뀌는 데이터를 읽을 수만 있도록 한다.

```
//viewModel
private val _isError = MutableLiveData<String>()
val isError: LiveData<String> get() = _isError

_isError.postValue(e.message)
```

```
//view
isError.observe(viewLifecycleOwner){
  Toast.makeText(context,it,Toast.LENGTH_SHORT).show()
}
```

예외상황이 발생 시 viewMdoel에서 \_isError에 예외상황 메세지를 입력하고,

\_isError에 메세지가 입력된 것을 감지하면 \_isError를 get하는 isError를 view에서 뿌려준다.

다음과 같이 mutableLiveData인 \_isError는 viewModel 내에서 사용하며 데이터를 바꿔주고,

LiveData인 isError는 바뀌는 \_isError를 받아서 view에 보여줄때 view에서 사용한다.
