---
title: "안드로이드 스튜디오 / 'constructor Handler()' is deprecated. Deprecated in Java"
source: "https://dev-ej2.tistory.com/10"
tistory_id: "10"
published: "2022-03-08T16:20:01+09:00"
category: "IT/Android"
tags:
---
Handler() 대신

```
Handler(Looper.getMainLooper())
```

 사용하자

Handler가 생성되는동안 Looper가 암묵적으로 선택되면 버그가 발생할  수 있다고 한다.

따라서 Looper를 명시적으로 선언하자!

<https://developer.android.com/reference/android/os/Handler#Handler(>)
