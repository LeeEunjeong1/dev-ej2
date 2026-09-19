---
title: "안드로이드 스튜디오 / Jetpack Compose?"
source: "https://dev-ej2.tistory.com/30"
tistory_id: "30"
published: "2022-04-26T17:16:21+09:00"
category: "IT/Android"
tags:
---
xml에 익숙한 나... Compose 사용 가능일까? (경험에 비롯한 Compose)

Jetpack Compose란 안드로이드의 선언형 UI 도구 키트이다.

Compose는 뷰를 명령형으로 변형하지 않고도 앱에 UI를 랜더링할 수 있게 하는 선언형 UI를 제공한다.

지금껏 xml에  뷰를  그리고, 접근하려면 findViewById(), dataBinding 등을 사용하였다.

레이아웃 수정을 하면서 xml은 수정하였는데, Activity에서 수정하지 못해서 오류가 난 경험이 꽤나 있다.

이러한 문제점을 해결해줄 것 같은 Compose는 뷰를 그림과 동시에 접근이 가능하다.

recyclerview를..사용안해도 된다던데.. 다음 프로젝트는 Compose를 사용해봐야겠다. 하하

<https://developer.android.com/jetpack/compose/mental-model>

[Compose 이해  |  Jetpack Compose  |  Android Developers

Compose 이해 Jetpack Compose는 Android를 위한 현대적인 선언형 UI 도구 키트입니다. Compose는 프런트엔드 뷰를 명령형으로 변형하지 않고도 앱 UI를 렌더링할 수 있게 하는 선언형 API를 제공하여 앱 UI를

developer.android.com](https://developer.android.com/jetpack/compose/mental-model)

\*------\*

![](https://blog.kakaocdn.net/dna/dWRCri/btrAK3mHkYk/AAAAAAAAAAAAAAAAAAAAAL8IvE-zFOF6T_NxOczV7eAFWlWkdg0kkyH6UjkRAYz-/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1790780399&allow_ip=&allow_referer=&signature=GI%2BMDmx9jkZhLefhSD%2FF8yhNXNw%3D)

어머 너무 신기하다!!! 코틀린파일 옆에 디자인창이 바로 뜨다니!! 어머어머!!!

당연히 되는거가 맞는데.. 코드로만 레이아웃을 만든다는 생각에 디자인 미리 못보는건줄 알았다. ㅋㅋ 바보
