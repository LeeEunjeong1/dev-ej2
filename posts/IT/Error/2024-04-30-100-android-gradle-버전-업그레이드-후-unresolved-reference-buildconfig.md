---
title: "Android / gradle 버전 업그레이드 후 unresolved reference buildconfig"
source: "https://dev-ej2.tistory.com/100"
tistory_id: "100"
published: "2024-04-30T10:05:23+09:00"
category: "IT/Error"
tags:
---
gradle 버전을 업그레이드 한 이후 빌드를 했더니 ( Android Gradle 플러그인(AGP) 8.0이상으로 업그레이드 )

unresolved reference buildconfig 에러가 떴다.

gradle.properties 파일에 아래 코드를 추가해주면 된다.

```
android.defaults.buildfeatures.buildconfig=true
```

<https://medium.com/androiddevelopers/5-ways-to-prepare-your-app-build-for-android-studio-flamingo-release-da34616bb946>

[5 ways to prepare your app build for Android Studio Flamingo release

When you upgrade to Android Studio Flamingo and Android Gradle Plugin (AGP) 8.0, you need to update your app build files to accommodate…

medium.com](https://medium.com/androiddevelopers/5-ways-to-prepare-your-app-build-for-android-studio-flamingo-release-da34616bb946)
