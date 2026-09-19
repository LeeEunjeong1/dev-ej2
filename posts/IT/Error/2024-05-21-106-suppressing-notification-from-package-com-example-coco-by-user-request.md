---
title: "Suppressing notification from package com.example.coco by user request"
source: "https://dev-ej2.tistory.com/106"
tistory_id: "106"
published: "2024-05-21T11:00:00+09:00"
category: "IT/Error"
tags:
---
android13 알림 권한 설정 문제

Suppressing notification from package com.example.coco by user request

앱 설정 > 알림 > 허용

사용자가 Android 13 이상을 실행하는 기기에 앱을 설치하면 앱의 **알림이 기본적으로 사용 중지된다.**

**따라서, 앱 설치시 혹은 알림이 필요한 경우 권한을 따로 요청해야한다.**

```
<manifest ...>
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>
    <application ...>
        ...
    </application>
</manifest>
```

manifest에 추가 뿐만 아니라 런타임 권한도 추가해야함

<https://developer.android.com/develop/ui/views/notifications/notification-permission?hl=ko>

[알림 런타임 권한  |  Views  |  Android Developers

이 페이지는 Cloud Translation API를 통해 번역되었습니다. 알림 런타임 권한 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요. Android 13(API 수준 33) 이상에서는 앱

developer.android.com](https://developer.android.com/develop/ui/views/notifications/notification-permission?hl=ko)
