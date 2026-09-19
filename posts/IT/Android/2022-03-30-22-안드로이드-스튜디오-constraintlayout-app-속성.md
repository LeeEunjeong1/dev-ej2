---
title: "안드로이드 스튜디오 / Constraintlayout app 속성"
source: "https://dev-ej2.tistory.com/22"
tistory_id: "22"
published: "2022-03-30T11:31:12+09:00"
category: "IT/Android"
tags:
---
layout\_constraint방향\_to방향of속성을 이용해서 각 위젯간 관계를 설정해줄 수 있다.

top 위

bottom 아래

start 왼쪽

end  오른쪽

ex)

android:id="@+id/text\_view1"

app:layout\_constraintBottom\_toTopOf="@+id/text\_view2"

-> text\_view1의 Bottom(아래부분)을 text\_view2의 Top(위)에 위치시킨다.

android:id="@+id/text\_view2"

app:layout\_constraintTop\_toBottomOf="@+id/text\_view1"

-> text\_view2의 Top(위)을 text\_view1의 Bottom(아래)에 위치시킨다.

!!

constraintBottom\_

cosntraintTop\_

constraintStart\_

constraintEnd\_

를 기본으로 깔고 뒤에 to~Of는 상황에 맞게 설정하기

![](https://blog.kakaocdn.net/dna/OxMHR/btryspUOFrE/AAAAAAAAAAAAAAAAAAAAAGVfYIPY1eqWWoUgQwWhICraFHzz6V0IcnPyPpwQ6K4l/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1790780399&allow_ip=&allow_referer=&signature=rn%2FKNDQYAavpeunzKtEM5ozcKxM%3D)
