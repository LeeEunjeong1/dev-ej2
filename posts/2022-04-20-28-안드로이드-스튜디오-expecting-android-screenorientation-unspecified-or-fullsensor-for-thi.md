---
title: "안드로이드 스튜디오 / Expecting android:screenOrientation=\"unspecified\" or \"fullSensor\" for this activity so the user can use the application in any orientation and provide a great experience on Chrome OS devices"
source: "https://dev-ej2.tistory.com/28"
tistory_id: "28"
published: "2022-04-20T10:58:15+09:00"
tags:
---
```
tools:ignore="LockedOrientationActivity"
```

manifest에 "LockedOrientationActivity" 추가하면 된다.

<https://stackoverflow.com/questions/60396601/expecting-androidscreenorientation-unspecified-or-fullsensor-for-this-a>
