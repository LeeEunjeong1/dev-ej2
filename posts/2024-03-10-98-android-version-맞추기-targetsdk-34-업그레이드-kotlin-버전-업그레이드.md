---
title: "Android version 맞추기 (targetSdk 34 업그레이드/kotlin 버전 업그레이드)"
source: "https://dev-ej2.tistory.com/98"
tistory_id: "98"
published: "2024-03-10T23:37:24+09:00"
tags:
---
1. 라이브러리 모듈과 프로젝트의 코틀린 버전의 충돌이 남.

Module was compiled with an incompatible version of Kotlin. The binary version of its metadata is 1.8.0, expected version is 1.6.0.

1. targetSdk를 34로 업그레이드 하고(내친김에), 코틀린 버전을 1.8.0으로 올림

targetSdk 33 -> 34

compileSdk 33 -> 34

'com.android.tools.build:gradle:7.2.1' -> 'com.android.tools.build:gradle:7.2.2'        
'org.jetbrains.kotlin:kotlin-gradle-plugin:1.6.21' ->   'org.jetbrains.kotlin:kotlin-gradle-plugin:**1.8.0**'

-> 코틀린 버전과 Hilt 버전 충돌이 남.

Unsupported metadata version. Check that your Kotlin version is >= 1.0: java.lang

2. hilt 버전을 2.44로 올림

'com.google.dagger:hilt-android-gradle-plugin:2.40.1' -> 'com.google.dagger:hilt-android-gradle-plugin:**2.44**'

-> 다음과 같은 오류 발생 : 찾아보니 해당 fragment버전에서 hilt 지원X

Caused by: java.lang.IllegalArgumentException: CreationExtras must have a value by `SAVED\_STATE\_REGISTRY\_OWNER\_KEY`

3. fragment 버전 1.4.1에서 1.5.4로 올림

androidx.fragment:fragment-ktx:1.4.1 -> androidx.fragment:fragment-ktx:**1.5.4**

힘....들다....
