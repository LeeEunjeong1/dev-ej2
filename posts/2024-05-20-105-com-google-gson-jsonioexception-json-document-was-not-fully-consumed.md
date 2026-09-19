---
title: "com.google.gson.JsonIOException: JSON document was not fully consumed."
source: "https://dev-ej2.tistory.com/105"
tistory_id: "105"
published: "2024-05-20T11:26:13+09:00"
tags:
---
com.google.gson.JsonIOException: JSON document was not fully consumed.

다음과 같은 에러는 응답값이 JSON형식이 아닌, String이라서 생기는 에러다.

해결방법은 아래와 같이 ScalersConverter를 추가해주면 된다.

```
retrofit-converter-scalars = { group = "com.squareup.retrofit2", name = "converter-scalars", version.ref = "retrofit" }
implementation(libs.retrofit.converter.scalars)


Retrofit.Builder()
.client(okHttpClient)
.baseUrl(url)
.addConverterFactory(ScalarsConverterFactory.create())
.addConverterFactory(GsonConverterFactory.create())
.addCallAdapterFactory(CoroutineCallAdapterFactory())
.build()
```

<https://square.github.io/retrofit/2.x/converter-scalars/retrofit2/converter/scalars/ScalarsConverterFactory.html>

[ScalarsConverterFactory (scalars API)

retrofit2.Converter requestBodyConverter(java.lang.reflect.Type type, java.lang.annotation.Annotation[] parameterAnnotations, java.lang.annotation.Annotation[] methodAnnotations, retrofit2.Retrofit retrofit)

square.github.io](https://square.github.io/retrofit/2.x/converter-scalars/retrofit2/converter/scalars/ScalarsConverterFactory.html)

<https://devuryu.tistory.com/403>

[Retrofit2 이슈 - com.google.gson.JsonIOException: JSON document was not fully consumed.

이슈 retrofit2.DefaultCallAdapterFactory$ExecutorCallbackCall@dffd7f3 com.google.gson.JsonIOException: JSON document was not fully consumed. 원인 REST API 의 Response 형태가 json 형태가 아닌 String 형태로 내려올 경우에 발생한다.

devuryu.tistory.com](https://devuryu.tistory.com/403)
