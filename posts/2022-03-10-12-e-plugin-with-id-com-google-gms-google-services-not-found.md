---
title: "E/ Plugin with id 'com.google.gms.google-services' not found."
source: "https://dev-ej2.tistory.com/12"
tistory_id: "12"
published: "2022-03-10T10:53:17+09:00"
tags:
---
firebase를 gradle에 추가하고싶은데 못하고 있는 상황 발생..

예제에는 apply plugin: 'com.google.gms.google-services' 하라고 했으나, 내 코드는 plugins{} 이렇게 되어 있는 상황.

plugins{ id 'com.google.gms.google-services' } 해보니 

Plugin with id 'co[m.google.gms.google-services'](http://m.google.gms.google-services') not found. 에러가 떴다.

```
plugins {
    id 'com.google.gms.google-services' version '4.3.2'
}
```

다음과 같이 뒤에 version을 명시해주니 해결 ㅎㅎ;

<https://github.com/google/play-services-plugins/tree/master/google-services-plugin>
