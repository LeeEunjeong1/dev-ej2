---
title: "Android / Version Catalog 적용 - 안드로이드 버전관리"
source: "https://dev-ej2.tistory.com/99"
tistory_id: "99"
published: "2024-04-27T14:42:29+09:00"
tags:
---
1. gradle/libs.versions.toml 파일 생성

```
[versions]
coreKtx = "1.9.0"
androidApplication = "8.1.0"

[libraries]
core-ktx = { group = "androidx.core", name = "core-ktx", version.ref = "coreKtx" }

[plugins]
android-application = { id = "com.android.application", version.ref = "androidApplication" }
```

2. app/build.gradle.kt 에 적용

```
implementation(libs.core.ktx)
```

3. build.gradle.kt에 적용

```
plugins {
    alias(libs.plugins.android.application) apply false
}
```

'val Project.libs: LibrariesForLibs' can't be called in this context by implicit receiver. Use the explicit one if necessary

-> 실행은 잘 되지만, libs에 IDE경고가 떴다. (IDE 버그)

4. File > Project Structure > Project > Gradle Version

gradle version을 8.1 이상으로 올리면 완료.

<https://github.com/gradle/gradle/issues/22797>

[Version catalog accessors for plugin aliases shown as errors in IDE kotlin script editor · Issue #22797 · gradle/gradle

Expected Behavior No error should be shown in the IDE kotlin script editor. Current Behavior Workaround You can install the Gradle Libs Error Suppressor IntelliJ Plugin or add the @Suppress("DSL\_SC...

github.com](https://github.com/gradle/gradle/issues/22797)

<참고>

<https://two22.tistory.com/81>

[Android - BuildSrc + Version Catalog ( 안드로이드 버전 관리하기 )

안드로이드에서 버전을 관리하는 방법이 점점 많아지고 있다. 간단하게 정리하자면, 1. ext를 통한 관리 Gradle에서 라이브러리 업데이트 가능 정보가 노출된다. 2. buildsrc를 통한 관리 플러그인들

two22.tistory.com](https://two22.tistory.com/81)
