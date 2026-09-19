---
title: "안드로이드 스튜디오 / koin 으로viewModel 의존성 주입 시 viewModel을 공유할 경우"
source: "https://dev-ej2.tistory.com/24"
tistory_id: "24"
published: "2022-04-13T11:28:45+09:00"
tags:
---
2개 이상의 View가 1개의 ViewModel을 공유할 경우 by **sharedViewModel**()로 주입한다.

단, Fragment에서만 사용. 부모 Activity에서는 by viewModel() 사용하면 된다.
