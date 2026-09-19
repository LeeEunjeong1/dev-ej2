---
title: "안드로이드 스튜디오 / koin - Retrofit에 로그 및 헤더 추가"
source: "https://dev-ej2.tistory.com/8"
tistory_id: "8"
published: "2022-03-07T12:24:55+09:00"
tags:
---
```
//네이버 api
var retrofitNaverPart = module{
    httpLoggingInterceptor.apply {
        httpLoggingInterceptor.level = HttpLoggingInterceptor.Level.BODY
    }
    single<PapagoService>{
        Retrofit.Builder()
            .baseUrl("https://openapi.naver.com/")
            .client(get<OkHttpClient>((named("retrofitNaverPart"))))
            .addCallAdapterFactory(RxJava3CallAdapterFactory.create())
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(PapagoService::class.java)
    }
    single<OkHttpClient>(named("retrofitNaverPart"))  {
        OkHttpClient.Builder()
            .connectTimeout(120, TimeUnit.SECONDS)
            .readTimeout(120, TimeUnit.SECONDS)
            .writeTimeout(120, TimeUnit.SECONDS)
            .addInterceptor(httpLoggingInterceptor)
            .addInterceptor { chain ->
                val originalRequest = chain.request()
                val builder = originalRequest.newBuilder()
                    .header("X-Naver-Client-Id","blah")
                    .header("X-Naver-Client-Secret","blah")
                val newRequest = builder.build()
                chain.proceed(newRequest)
            }
            .build()
    }
}
```

```
.client(get<OkHttpClient>((named("retrofitNaverPart"))))
```

Retrofit single 부분에 .client로 okHttpClient 추가해주어야한다,,,,^^;
