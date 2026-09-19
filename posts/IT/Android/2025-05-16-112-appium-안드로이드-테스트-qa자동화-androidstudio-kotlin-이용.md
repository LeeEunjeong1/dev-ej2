---
title: "Appium - 안드로이드 테스트 QA자동화 (AndroidStudio+kotlin 이용)"
source: "https://dev-ej2.tistory.com/112"
tistory_id: "112"
published: "2025-05-16T13:50:17+09:00"
category: "IT/Android"
tags:
---
안드로이드 개발자가 QA 자동화 툴을 직접 다룰 일은 흔치 않지만.. QA팀에서 자동화 R&D 요청이 들어와 오픈소스인 Appium을 적용해봤습니다.

## **Appium이란?**

**Appium**은 모바일 앱 테스트를 자동화할 수 있는 오픈소스 프레임워크입니다.  
Android뿐 아니라 iOS도 지원하며, Selenium 기반으로 작동합니다.

> 💡 안드로이드는 내부적으로 UiAutomator2를 활용해 실제 기기에서 동작하게 됩니다.

## 

## **Appium의 장점**

|  |  |
| --- | --- |
| 크로스 플랫폼 지원 | Android와 iOS 모두 테스트 가능 |
| 다양한 언어 지원 | Kotlin, Java, Python, JS 등 사용 가능 |
| 실제 기기 테스트 | 실기기 또는 에뮬레이터에서 테스트 가능 |
| GUI 검사 도구 제공 | Appium Inspector를 통해 UI 요소 파악 가능 |

## **Appium 아키텍처**

Appium은 다음 구성 요소로 이루어져 있습니다:

- **Appium Server**  
  Node.js 기반 서버로 클라이언트 요청을 받아 모바일 디바이스에서 자동화 명령을 실행합니다.
- **Appium Client**  
  Python, Java 등으로 작성된 테스트 스크립트가 Appium 서버와 통신하는 역할을 합니다.
- **Driver (ex. UiAutomator2, XCUITest)**  
  플랫폼(Android, iOS)에 따라 각각의 드라이버가 실제 디바이스 또는 에뮬레이터와 상호작용합니다

## **사전 준비**

안드로이드에서 Appium을 사용하려면 다음 준비가 필요합니다:

### 1. Node.js 설치

```
# 설치 (macOS/Linux)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# 터미널 재시작 후:
nvm install node
nvm use node
```

2. Appium 설치

```
npm install -g appium
```

### 3. Appium Inspector 설치

Appium 요소를 시각적으로 확인할 수 있는 GUI 툴입니다.  
→ [Appium Inspector 다운로드](https://github.com/appium/appium-inspector/releases)

[Releases · appium/appium-inspector

A GUI inspector for mobile apps and more, powered by a (separately installed) Appium server - appium/appium-inspector

github.com](https://github.com/appium/appium-inspector/releases)

```
appium plugin install --source=npm appium-inspector-plugin
```

### 4. Android 환경 세팅

- Android sdk, jdk 설치 후 환경변수에 설정 추가

```
touch ~/.zshrc
open -e ~/.zshrc     # macOS 기본 텍스트 편집기로 열기

# Android SDK (본인 경로 설정, 아래는 예시)
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools

# Java JDK (버전에 따라 다름, 아래는 예시)
export JAVA_HOME=$(/usr/libexec/java_home -v11)
export PATH=$JAVA_HOME/bin:$PATH

# 저장후 
source ~/.zshrc
```

- uiAutomator2 드라이버 설치

```
# 설치
appium driver install uiautomator2
# 설치 검증
appium driver doctor uiautomator2
```

## **Android Studio에서 Appium 설정하기 (Kotlin 기준)**

Kotlin 또는 Java 기반의 Appium 테스트 프로젝트를 안드로이드 스튜디오에서도 작성할 수 있습니다.

### 프로젝트 타입 설정

- 새 프로젝트 생성 시 Gradle > Kotlin/JVM 또는 Gradle > Java로 생성
- Android 프로젝트로 만들면 불필요한 Android SDK 설정과 충돌이 생길 수 있습니다

## 필요한 의존성 (build.gradle.kts 기준)

```
dependencies {
    // Appium Java Client (Android 지원 포함)
    implementation("io.appium:java-client:8.5.1")

    // Selenium (Appium 내부적으로 사용)
    implementation("org.seleniumhq.selenium:selenium-java:4.20.0")

    // Kotlin Coroutines (선택사항)
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.7.3")

    // Logging (선택사항)
    implementation("org.slf4j:slf4j-simple:2.0.9")
}
```

### 빌드 설정 예시 (build.gradle.kts)

```
plugins {
    kotlin("jvm") version "1.9.0"
    application
}

repositories {
    mavenCentral()
}

application {
    mainClass.set("com.example.appium.MainKt") // your main class
}
```

> 💡 Gradle 버전이 낮을 경우 Appium Java Client 8.x에서 오류가 날 수 있으니 최소 Gradle 7 이상을 권장합니다.

## Kotlin Appium 테스트 코드

- main() 함수에서 AndroidDriver 생성 후 테스트 시작
- 테스트 실행은 일반 콘솔 앱처럼 Run 버튼으로 수행

```
fun main() {
	val capabilities = DesiredCapabilities().apply {
	    setCapability("platformName", "Android")
	    setCapability("automationName", "UiAutomator2")
	    setCapability("deviceName", "Android QA Emulator")
	    setCapability("appPackage", "com.example.myapp")
	    setCapability("appActivity", "com.example.myapp.MainActivity")
	}
	
	// 테스트 시나리오 실행
	val wait = WebDriverWait(driver, Duration.ofSeconds(10))
	
	val loginBtn = wait.until(
	    ExpectedConditions.elementToBeClickable(AppiumBy.accessibilityId("btnLogin"))
	)
	loginBtn.click()
}
```

## **Appium 테스트를 위한 contentDescription 설정하기**

자동 UI 테스트에서 **버튼이나 뷰를 정확하게 찾기 위한 식별자**로 가장 흔히 사용하는 것이 contentDescription입니다.

Jetpack Compose에서는 이 값을 Modifier.semantics로 설정할 수 있어요.

### Jetpack Compose에서 contentDescription 지정 방법

#### 일반적인 View 시스템 (XML 기반)

```
<Button android:id="@+id/btnLogin" android:contentDescription="btnLogin" ... />
```

#### Jetpack Compose

```
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics

Button(
    onClick = { /* 로그인 로직 */ },
    modifier = Modifier.semantics {
        contentDescription = "btnLogin"
    }
) {
    Text("로그인")
}
```

> testTag는 Appium의 accessibilityId로 접근되지 않습니다.  
> Appium은 contentDescription 기반인 accessibilityId를 통해 UI 요소를 찾습니다.

## Appium에서 contentDescription으로 요소 찾기

Appium 코드에서는 이렇게 접근합니다:

```
val loginBtn = wait.until(
    ExpectedConditions.elementToBeClickable(AppiumBy.accessibilityId("btnLogin"))
)
loginBtn.click()
```

- accessibilityId("btnLogin")는 Android에서 contentDescription="btnLogin"인 요소를 찾습니다.
- Jetpack Compose에서는 반드시 semantics { contentDescription = "..." }로 설정해줘야 작동합니다.

[Appium 공식 사이트](https://appium.io/)

[Redirecting

appium.io](https://appium.io/)

[Appium Inspector](https://github.com/appium/appium-inspector)

[GitHub - appium/appium-inspector: A GUI inspector for mobile apps and more, powered by a (separately installed) Appium server

A GUI inspector for mobile apps and more, powered by a (separately installed) Appium server - appium/appium-inspector

github.com](https://github.com/appium/appium-inspector)
