---
title: "안드로이드 스튜디오 / Appsflyer onelink 적용방법"
source: "https://dev-ej2.tistory.com/45"
tistory_id: "45"
published: "2023-04-06T12:44:58+09:00"
tags:
---
앱내 게시물 링크를 공유해서 링크를 클릭하면 해당 게시물로 들어오게 하기 위해서는 deeplink를 사용해야한다.

Appsflyer onelink를 사용하여 구현하였다.

![](https://blog.kakaocdn.net/dna/v0xAt/btr8fZG7FqN/AAAAAAAAAAAAAAAAAAAAAB3Luwy9kwZrPrVI-dpSTEw3ZLC2Z0i9UXmaOYV7xUmd/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1790780399&allow_ip=&allow_referer=&signature=9QvkQInnJ7SyFbOxPJ5EIBpFcr0%3D)

1. Appsflyer sdk 설치

1-1. 모듈단위 gradle

```
dependencies {
    // Get the latest version from https://mvnrepository.com/artifact/com.appsflyer/af-android-sdk
    implementation 'com.appsflyer:af-android-sdk:6.9.0' 
}
```

1-2. manifest

```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="com.google.android.gms.permission.AD_ID"
 tools:node="remove"/>
```

![](https://blog.kakaocdn.net/dna/Wc16J/btr8jO5BjOh/AAAAAAAAAAAAAAAAAAAAABy3lZ4N1K1NdwVP2uwcRfGKjp0RQuJfYk-BMsGTcmui/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1790780399&allow_ip=&allow_referer=&signature=Y1yPZwP29%2BIWtuOM0JxxSeiodnc%3D)
![](https://blog.kakaocdn.net/dna/dcgnOO/btr8hmWzmPS/AAAAAAAAAAAAAAAAAAAAAC7C1RmM0J2bYgRhXqmQlX33XgKK-iMlY_4QYmEp8aI1/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1790780399&allow_ip=&allow_referer=&signature=jzGlWcoQQHHjHUYIeTTZvtpDd6o%3D)

Appsflyer 에서 링크가 생성되면,

2. Manifest에서 intent-filter를 추가해준다. 이때, onelink intent-filter와 Appsflyer에 등록한 scheme를 같이 등록해주어야 한다.

```
<activity
...
    <intent-filter android:autoVerify="true">
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="https" android:host="${등록한값}.onelink.me" />
    </intent-filter>

    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="${등록한값}" />
    </intent-filter>
</activity>
```

3. Appsflyer SDK 시작하기.

```
AppsFlyerLib.getInstance().init("${키값}", null, this)
AppsFlyerLib.getInstance().start(this)
```

이러면 준비 끝!

나의 경우, 링크뒤에 파라미터를 붙여 파라미터 값에 따라 페이지 이동을 해주었다.

딥링크를 통해 앱에 들어오면, 하단 코드에 걸리게 되어 분기처리를 해주면 된다.

```
AppsFlyerLib.getInstance().subscribeForDeepLink(object : DeepLinkListener{
    override fun onDeepLinking(deepLinkResult: DeepLinkResult) {
        when (deepLinkResult.status) {
            DeepLinkResult.Status.FOUND -> {
                Log.d(
                    LOG_TAG,"Deep link found"
                )
            }
            DeepLinkResult.Status.NOT_FOUND -> {
                Log.d(
                    LOG_TAG,"Deep link not found"
                )
                return
            }
            else -> {
                // dlStatus == DeepLinkResult.Status.ERROR
                val dlError = deepLinkResult.error
                Log.d(
                    LOG_TAG,"There was an error getting Deep Link data: $dlError"
                )
                return
            }
        }
        var deepLinkObj: DeepLink = deepLinkResult.deepLink
        try {
            Log.d(
                LOG_TAG,"The DeepLink data is: $deepLinkObj"
            )
        } catch (e: Exception) {
            Log.d(
                LOG_TAG,"DeepLink data came back null"
            )
            return
        }

        // An example for using is_deferred
        if (deepLinkObj.isDeferred == true) {
            Log.d(LOG_TAG, "This is a deferred deep link");
        } else {
            Log.d(LOG_TAG, "This is a direct deep link");
        }

        try {
            val fruitName = deepLinkObj.deepLinkValue
            Log.d(LOG_TAG, "The DeepLink will route to: $fruitName")
        } catch (e:Exception) {
            Log.d(LOG_TAG, "There's been an error: $e");
            return;
        }
    }
})
```

<https://dev.appsflyer.com/hc/docs/install-android-sdk>

<https://dev.appsflyer.com/hc/docs/dl_android_unified_deep_linking>
