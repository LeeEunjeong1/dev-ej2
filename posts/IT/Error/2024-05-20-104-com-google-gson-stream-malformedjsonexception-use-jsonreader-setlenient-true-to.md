---
title: "com.google.gson.stream.MalformedJsonException: Use JsonReader.setLenient(true) to accept malformed JSON at line 1 column 1 path $"
source: "https://dev-ej2.tistory.com/104"
tistory_id: "104"
published: "2024-05-20T11:20:44+09:00"
category: "IT/Error"
tags:
---
com.google.gson.stream.MalformedJsonException: Use JsonReader.setLenient(true) to accept malformed JSON at line 1 column 1 path $  
  
다음과 같은 에러는 gson에서 json을 처리할때 Json형식의 RFC 4627를 지키지 않았을때 발생한다고 한다.

```
val gsonBuilder = GsonBuilder()
gsonBuilder.setLenient().create()   
      
GsonConverterFactory.create(gsonBuilder)
```

해결방법은 다음과같이 setLenient()를 추가해주면 된다.

<https://3edc.tistory.com/52>
