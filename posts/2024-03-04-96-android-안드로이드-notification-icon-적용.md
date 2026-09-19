---
title: "Android / 안드로이드 notification Icon 적용"
source: "https://dev-ej2.tistory.com/96"
tistory_id: "96"
published: "2024-03-04T11:15:06+09:00"
tags:
---
안드로이드 푸시메세지를 받았을때 뜨는 notification의 icon은

svg, 흰색, 24dp <- 이 조건이 충족되어야 함

아이콘 지정 : setSmallIcon()

아이콘 배경색 지정 : setColor

배경없는 흰색 svg여야 배경색과 아이콘이 잘 지정된다.
