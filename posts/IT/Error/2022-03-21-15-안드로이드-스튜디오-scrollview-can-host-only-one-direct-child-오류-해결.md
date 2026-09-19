---
title: "안드로이드 스튜디오 / ScrollView can host only one direct child 오류 해결"
source: "https://dev-ej2.tistory.com/15"
tistory_id: "15"
published: "2022-03-21T15:07:33+09:00"
category: "IT/Error"
tags:
---
Caused by: android.view.InflateException: Binary XML file line #38: ScrollView can host only one direct child   
     Caused by: java.lang.IllegalStateException: ScrollView can host only one direct child

Scrollview는 하나의 Child만 가질 수 있다.

따라서 View가 여러개라면 (ex. Recyclerview, Linearlayout 등) LinearLayout 같은 Layout으로 한 번 더 감싸주어야 한다.
