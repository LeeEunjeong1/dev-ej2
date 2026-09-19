---
title: "안드로이드 스튜디오 / Configuration cache problems found in this build.1 problem was found storing the configuration cache.-"
source: "https://dev-ej2.tistory.com/58"
tistory_id: "58"
published: "2023-07-17T17:03:23+09:00"
category: "IT/Error"
tags:
---
프로젝트 배포 aab 파일을 만들다가 다음과 같은 처음 보는 에러가 발생했다.

Configuration cache problems found in this build.   
  
1 problem was found storing the configuration cache.   
- Task `:app:collectReleaseDependencies` of type `co[m.android.build.gradle.internal.tasks.PerModuleReportDependenciesTask](http://m.android.build.gradle.internal.tasks.PerModuleReportDependenciesTask)`: invocation of 'Task.project' at execution time is unsupported.   
  See <https://docs.gradle.org/7.3.3/userguide/configuration_cache.html#config_cache:requirements:use_project_during_execution>

이러한 문제를 무시하게 위해서는 gradle.properties에 'org.gradle.unsafe.configuration-cache-problems=warn 추가해주면 된다.

```
org.gradle.unsafe.configuration-cache-problems=warn
```

<https://stackoverflow.com/questions/68127791/configuration-cache-enabled-causes-build-to-fail>
