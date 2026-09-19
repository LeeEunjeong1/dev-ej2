---
title: "Android / 푸시알림 클릭시 PendingIntent Bundle값 전달 안되는 경우"
source: "https://dev-ej2.tistory.com/95"
tistory_id: "95"
published: "2024-02-07T15:53:04+09:00"
category: "IT/Android"
tags:
---
푸시 알림 클릭하면 PendingIntent를 이용하여 MainActivity로 이동하는 로직에서

intent로 전달된 Bundle값이 초기값으로만 이동되는 현상이 발생하였다.

반복적으로 푸시알림이 들어와 노티가 쌓이게 되면

bundle값이 캐싱되어 실시간으로 값 변동이 전달되지 않는다.

```
public static PendingIntent getActivity(Context context, int requestCode, @NonNull Intent intent, int flags, @Nullable Bundle options) {
    throw new RuntimeException("Stub!");
}
```

PendingIntent.getActivity 함수를 보면 requestCode를 인자로 받고있다.

해당 인자에 currentTime을 넣어줘, requestCode를 Intent마다 다르게 해준다.

```
val bundle = Bundle()
bundle.putString("test", "test")
   val intent = Intent(this, MainActivity::class.java).apply {
    addFlags(FLAG_ACTIVITY_NEW_TASK)
    putExtras(bundle)
}
 PendingIntent.getActivity(
    applicationContext, System.currentTimeMillis().toInt()/* Request code */, intent,
    PendingIntent.FLAG_IMMUTABLE, bundle
)
```

짜란
