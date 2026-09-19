---
title: "java.lang.IllegalStateException: Single return type must be parameterized as Single<Foo> or Single<? extends Foo>"
source: "https://dev-ej2.tistory.com/103"
tistory_id: "103"
published: "2024-05-16T14:18:42+09:00"
category: "IT/Error"
tags:
---
gradle을 8.0 이상으로 올리고, release로 build를 하니, 다음과 같은 에러가 떴다.

java.lang.IllegalStateException: Single return type must be parameterized as Single<Foo> or Single<? extends Foo>

gradle 8.0 이상으로 업그레이드시, android.enableR8.fullMode 가 default로 true로 적용이 되었다.

이에 따라 retrofit이 위와 같은 오류를 뱉는것..!

다행히 해당 이슈는 이미 한바탕 소동이 일어났었고, 해결책은 나와있었다.

1. proguard-ruels.pro 파일을 아래와 같이 수정 or retrofit 버전 2.10.0 이상으로 올리기

```
##### 기존 proguard 코드 ###### 
# Keep generic signature of Call, Response (R8 full mode strips signatures from non-kept items). 
 -keep,allowobfuscation,allowshrinking interface retrofit2.Call 
 -keep,allowobfuscation,allowshrinking class retrofit2.Response 
  
 # With R8 full mode generic signatures are stripped for classes that are not 
 # kept. Suspend functions are wrapped in continuations where the type argument 
 # is used. 
 -keep,allowobfuscation,allowshrinking class kotlin.coroutines.Continuation 

##### 수정한 proguard 코드 ######
 # With R8 full mode generic signatures are stripped for classes that are not 
 # kept. Suspend functions are wrapped in continuations where the type argument 
 # is used. 
 -keep,allowobfuscation,allowshrinking class kotlin.coroutines.Continuation 
  
 # R8 full mode strips generic signatures from return types if not kept. 
 -if interface * { @retrofit2.http.* public *** *(...); } 
 -keep,allowoptimization,allowshrinking,allowobfuscation class <3> 
  
 # With R8 full mode generic signatures are stripped for classes that are not kept. 
 -keep,allowobfuscation,allowshrinking class retrofit2.Response
```

<https://github.com/square/retrofit/issues/3751#issuecomment-1192043644>

[After enable R8 full mode getting ParameterizedType error · Issue #3751 · square/retrofit

Accessing hidden method Ljava/security/spec/ECParameterSpec;->setCurveName(Ljava/lang/String;)V (greylist, reflection, allowed) 16:09:29.013 W java.lang.ClassCastException: java.lang.Class cannot b...

github.com](https://github.com/square/retrofit/issues/3751#issuecomment-1192043644)

2. 위와 같이 수정했는데도 에러가 발생할 경우, 써드파티 버전을 의심하자.

나는 sandwich 버전이 낮아, 해당 이슈가 적용되지 않고 있었다.

sandwich 버전을 1.3.6 이상으로 올려주니 해결 완료.

<https://github.com/skydoves/sandwich/pull/103>

[Add proguard rules for R8 full mode by Goooler · Pull Request #103 · skydoves/sandwich

Closes #100.

github.com](https://github.com/skydoves/sandwich/pull/103)
