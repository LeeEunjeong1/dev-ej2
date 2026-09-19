---
title: "안드로이드 스튜디오 / navigation fragment backStack 없애기 (popupTo / popUpToInclusive)"
source: "https://dev-ej2.tistory.com/56"
tistory_id: "56"
published: "2023-07-13T23:33:36+09:00"
tags:
---
navigation component를 이용하여 fragment를 이동시켰는데, 뒤로가기를 누르면 원치 않는 backstack이 남아있는 문제가 생겼다.

예를들어, 회원가입시 아이디 중복확인 -> 핸드폰 인증 -> 회원 정보 입력 -> 회원가입 완료 플로우를 framgent 이동으로 한다.

회원가입이 완료가 되어도, 뒤로가기 누르면 회원정보 입력 fragment가 그대로 남아, 회원가입이 또 요청가능해지는 경우가 생길 수 있다.

이를 해결하기 위해 회원가입 activity를 따로 띄워, 회원가입 완료시 activity를 종료하는 방법이 있다.

프로젝트가 SAA(Single Activity Architecher)로 이루어져있으면 위의 방법으로는 해결하기 곤란하다.

같은 모든 화면이 fragment로 구성되어 있기 때문이다.

그래서, navigation component로 화면 이동시 백스택을 없애면서 이동하는 방법을 찾았다.

app:popUpTo 속성을 연결된 <action> 요소에 추가한다. 

app:popUpTo는 navigate() 호출의 일부로 백 스택에서 몇 개의 대상을 팝하도록 탐색 라이브러리에 알려준다.

app:popUpToInclusive="true"를 포함하여 app:popUpTo에 지정된 대상이 백 스택에서 삭제될 수도 있다는 것을 나타내준다.

```
<action
    android:id="@+id/fragment1_to_fragment2"
    app:destination="@id/fragment2"
    app:popUpTo="@id/fragment1"
    app:popUpToInclusive="true" />
```

fragment1 에서 fragment2로 이동하는 action이다.

여기에 popUpTo에 fragment1을 남겨주고, popUpToInclusive를 true로 해주면,

fragment1에서 fragment2로 이동할때 fragment1이 백스택에 남지 않게 된다.

fragment2에서 백버튼을 누르면 fragment1 이전의 fragment로 이동하게 된다.

얏호!

<https://developer.android.com/guide/navigation/navigation-navigate?hl=ko>

[대상으로 이동  |  Android 개발자  |  Android Developers

대상으로 이동 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요. 대상으로 이동하는 것은 NavController 객체를 사용하여 실행되며 이 객체는 NavHost 내에서 앱 탐

developer.android.com](https://developer.android.com/guide/navigation/navigation-navigate?hl=ko)[대상으로 이동  |  Android 개발자  |  Android Developers

대상으로 이동 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요. 대상으로 이동하는 것은 NavController 객체를 사용하여 실행되며 이 객체는 NavHost 내에서 앱 탐

developer.android.com](https://developer.android.com/guide/navigation/navigation-navigate?hl=ko)
