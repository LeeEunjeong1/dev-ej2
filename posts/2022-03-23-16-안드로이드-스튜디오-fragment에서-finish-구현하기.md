---
title: "안드로이드 스튜디오 / fragment에서 finish() 구현하기"
source: "https://dev-ej2.tistory.com/16"
tistory_id: "16"
published: "2022-03-23T18:17:24+09:00"
tags:
---
```
activity?.finish()
```

Activity에서는 finish() 하면 된다.

Fragment 에서는 finish()메서드를 바로 호출하지 못하기 때문에

```
activity?.supportFragmentManager
    ?.beginTransaction()
    ?.remove(this@ProfileFragment)
    ?.commit()
```

or

```
activity?.finish()
```

fragment내에서 'activity.'를 해주면 이 framgment가 현재 연결되어있는 FragmentActivity 를 반환해준다.

-> finish 사용 가능
