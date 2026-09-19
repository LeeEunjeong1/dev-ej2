---
title: "android / fcm notification (background data 컨트롤, 다국어 대응)"
source: "https://dev-ej2.tistory.com/107"
tistory_id: "107"
published: "2024-06-10T16:02:51+09:00"
category: "IT/Android"
tags:
---
1. background data 컨트롤

fcm notification은 다음과 같은 형태로 값을 보낸다.

```
{
  "message":{
    "token":"bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1...",
    "notification":{
      "title":"Portugal vs. Denmark",
      "body":"great match!"
    },
    "data" : {
      "Nick" : "Mario",
      "Room" : "PortugalVSDenmark"
    }
  }
}
```

notification과 data키가 있다.

foreground 상태에서 해당 푸시를 받으면 onMessageRecieved함수에서 data값 및 푸시 알림을 컨트롤 할 수 있다.

그러나, background상태에서 notification키값이 있는 푸시 메세지를 받으면 onMessageRecieved 메서드를 타지 않는다.

백그라운드에서 푸시메세지를 받으면 notification system에서 알림을 띄워준다.

notification system 에서 알림을 받으면 푸시아이콘은 manifest에서 설정한 기본 아이콘으로 자동 설정된다.

```
<meta-data
    android:name="com.google.firebase.messaging.default_notification_channel_id"
    android:value="@string/app_name" />
<meta-data
    android:name="com.google.firebase.messaging.default_notification_icon"
    android:resource="@drawable/ic_logo_noti_full" />
<meta-data
    android:name="com.google.firebase.messaging.default_notification_color"
    android:resource="@android:color/black" />
```

푸시를 클릭했을때 data값을 받고싶다면,  intent-filter를 설정하고, 해당 Activity에서 intent값을 받아오면 된다.

```
<activity
      android:name=".activity.MainActivity"
      android:exported="true">
      <intent-filter>
          <action android:name=".activity.MainActivity" />
          <category android:name="android.intent.category.DEFAULT" />

      </intent-filter>
  </activity>
```

기본적으로는 맨 처음 접속하는 launcher Activity로 intent값이 들어온다.

만약, intent받는 Activity를 지정하고 싶다면, fcm message를 보낼때 click\_action 키값에 해당 Activity를 지정하면 된다.

```
“click_action": ".activity.MainActivity"
```

<https://firebase.google.com/docs/cloud-messaging/android/receive?hl=ko>

[Android 앱에서 메시지 수신  |  Firebase 클라우드 메시징

Google I/O 2023에서 Firebase의 주요 소식을 확인하세요. 자세히 알아보기 의견 보내기 Android 앱에서 메시지 수신 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요. F

firebase.google.com](https://firebase.google.com/docs/cloud-messaging/android/receive?hl=ko)

2. 다국어 대응

다국어 대응은 아주 간단하다.

우선, 서버에서는 다음과 같은 키값을 보내줘야 한다.

```
{
     "notification": {
            "title_loc_key" : "NOTIFICATION_TITLE",
            "body_loc_key" : "NOTIFICATION_MESSAGE",
            "title_loc_args" : ["Dominican Republic"],
            "body_loc_args" : ["Rendy"]
     }
}
```

안드로이드에서는 strings.xml 에 해당 키값을 넣기만 해주면 된다.

백그라운드인 경우 자동으로 key값을 매핑해주고, 포그라운드인 경우 onRecived메서드에서 key값을 매핑시키면 된다.

다음은 포그라운드에서 호출되는 onRecived 메서드 예제이다.

```
val title = if (notification.titleLocalizationKey != null) {
    val titleKey = notification.titleLocalizationKey
    val args = remoteMessage.notification?.titleLocalizationArgs ?: emptyArray()
    if(args.isNotEmpty()){
        applicationContext.getString(resources.getIdentifier(titleKey, "string", applicationContext.packageName), *args)
    }else{
        applicationContext.getString(resources.getIdentifier(titleKey, "string", applicationContext.packageName))
    }
} else {
    notification.title ?: ""
}

val message = if (notification.bodyLocalizationKey != null) {
    val bodyKey = notification.bodyLocalizationKey
    val args = remoteMessage.notification?.bodyLocalizationArgs ?: emptyArray()
    if(args.isNotEmpty()){
        applicationContext.getString(resources.getIdentifier(bodyKey, "string", applicationContext.packageName), *args)
    }else{
        applicationContext.getString(resources.getIdentifier(bodyKey, "string", applicationContext.packageName))
    }
} else {
    notification.body ?: ""
}
```

remoteMessage.notification.titleLocalizationKey

remoteMessage.notification.bodyLocalizationKey

위 두개는 strings.xml에 등록되어 있는 Key값이다.

remoteMessage.notification.titleLocalizationArgs

remoteMessage.notification.bodyLocaizationArgs

argument가 있다면, 해당 값으로 argument를 받을 수 있다.

<https://github.com/CrossGeeks/FirebasePushNotificationPlugin/blob/master/docs/LocalizedFirebasePushNotifications.md#android----push-notifications-localization>

[FirebasePushNotificationPlugin/docs/LocalizedFirebasePushNotifications.md at master · CrossGeeks/FirebasePushNotificationPlugin

Firebase Push Notification Plugin for Xamarin iOS and Android - CrossGeeks/FirebasePushNotificationPlugin

github.com](https://github.com/CrossGeeks/FirebasePushNotificationPlugin/blob/master/docs/LocalizedFirebasePushNotifications.md#android----push-notifications-localization)

==== 여기서 끝난줄 알았으나......

위까지 설정하면 기기의 언어에 따라 푸시가 날라오는 것을 확인할 수 있다.

그러나, 앱 자체적으로 언어 변경이 가능하다면, 앱에서 설정한 언어에 따라 푸시가 날라와야 한다.

안드로이드에서 애플리케이션의 언어를 변경하는 경우, Firebase Notification Service에서 다국어를 적용하기 위해서는 별도의 처리가 필요하다.

이는 서비스가 별도의 컨텍스트에서 실행되기 때문에, 애플리케이션의 언어 설정이 자동으로 반영되지 않을 수 있기 때문이다.

그래서.. (꼼수를 쓴게...)

메세지를 받는 시점인 handleIntent 메서드 안에서 언어 설정을 해주었다.

```
override fun handleIntent(intent: Intent?) {
    updateLocale(this)
    super.handleIntent(intent)
}

private fun updateLocale(context: Context) {
   val sharedPreference = SharedPreference()
   val languageCode = sharedPreference.getString(SharedPreference.PREFERENCE_LANG_CD, "en")
   val locale = Locale(languageCode)
   Locale.setDefault(locale)
   
   val resources = context.resources
   val config: Configuration = resources.configuration
   if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
       config.setLocale(locale)
   } else {
       config.locale = locale
   }
   resources.updateConfiguration(config, resources.displayMetrics)
}
```

처음엔 onMessageReceived에서 언어 설정을 변경하려고 했으나, 백그라운드에서 푸시알림이 날라오면 해당 메서드를 안타기 때문에..

handleIntent 메서드에서 언어 설정을 변경해주었다.

해치웠나?
