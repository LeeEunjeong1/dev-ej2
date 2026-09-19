---
title: "안드로이드 스튜디오/ Retrofit/OkHttpClient 로그 찍는 방법"
source: "https://dev-ej2.tistory.com/18"
tistory_id: "18"
published: "2022-03-23T18:50:44+09:00"
category: "IT/Android"
tags:
---
Retrofit에서 모든 통신을 로그찍어서 보고 싶다면 addInterceptor를 해주면 된다.

//설명추가 예정

```
val httpLoggingInterceptor = HttpLoggingInterceptor()
	httpLoggingInterceptor.apply{
    	httpLoggingInterceptor.level = HttpLoggingInterceptor.Level.BODY
    }

OkHttpClient.Builder()
			.addInterceptor(httpLoggingInterceptor)
            .build()
```
