---
title: "안드로이드 스튜디오 / Gradle sync failed: Unable to start the daemon process."
source: "https://dev-ej2.tistory.com/33"
tistory_id: "33"
published: "2022-07-01T15:27:21+09:00"
tags:
---
Error:Unable to start the daemon process.

This problem might be caused by incorrect configuration of the daemon.

For example, an unrecognized jvm option is used.

Please refer to the user guide chapter on the daemon at https://docs.gradle.org/2.14.1/userguide/gradle\_daemon.html

Please read the following process output to find out more:

-----------------------

Error occurred during initialization of VM

Could not reserve enough space for 1572864KB object heap

-- 해결방법

gradle.properties 파일에서

```
org.gradle.jvmargs=-Xmx512m -Dfile.encoding=UTF-8
```

Xmx???m -> Xmx512m 으로 변경
