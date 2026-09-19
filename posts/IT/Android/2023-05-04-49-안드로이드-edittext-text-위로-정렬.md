---
title: "안드로이드 / EditText text 위로 정렬"
source: "https://dev-ej2.tistory.com/49"
tistory_id: "49"
published: "2023-05-04T18:04:31+09:00"
category: "IT/Android"
tags:
---
![](https://blog.kakaocdn.net/dna/VEzGN/btsdXcAKXCx/AAAAAAAAAAAAAAAAAAAAAPzdPV3hhzcr9qf5WtNa2CJHiquSFcxU3OJluuyWHPwq/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1790780399&allow_ip=&allow_referer=&signature=vHZNXE7CsJIfmW6wOmkqYX%2BBu50%3D)
![](https://blog.kakaocdn.net/dna/btEPsF/btsdYOZDbfb/AAAAAAAAAAAAAAAAAAAAAInvtd7K7tdgr-omgzthZpjQlAxzK-sLHNXelOx8g4uT/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1790780399&allow_ip=&allow_referer=&signature=DBrHS2gT5hXYV0Dudw71mizYEjw%3D)

```
               <EditText
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:textSize="13sp"
                        android:inputType="textMultiLine"
                        android:hint="@string/text_hint"
                        android:lines="5"
                        android:gravity="top"/>
```

android:gravity 속성을 top으로 설정하면 multiLine인 EditText의 text를 위로 정렬할 수 있다.
