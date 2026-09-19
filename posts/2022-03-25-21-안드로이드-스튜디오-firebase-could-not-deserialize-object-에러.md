---
title: "안드로이드 스튜디오 / Firebase Could not deserialize object 에러"
source: "https://dev-ej2.tistory.com/21"
tistory_id: "21"
published: "2022-03-25T11:42:26+09:00"
tags:
---
~~~ does not define a no-rgument constructor. If you are using ProGuard, make sure these constructors are not stripped.

해당 오류는 Firebase의 객체를 역직렬화 하려면 DTO 클래스에 빈 생성자가 필요해서 발생한 것이다.

따라서, DTO클래스의 멤버 변수에 default  값을 주는 것으로 해결 가능하다.

```
data class User (
    val email : String = "",
    val name : String ="",
    val image : String = "",
    val uid : String = ""
)
```

객체 데이터 초기화해주기~
