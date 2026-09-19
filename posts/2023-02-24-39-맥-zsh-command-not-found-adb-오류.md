---
title: "맥 zsh: command not found: adb 오류"
source: "https://dev-ej2.tistory.com/39"
tistory_id: "39"
published: "2023-02-24T23:45:06+09:00"
tags:
---
안드로이드스튜디오에서 adb 명령어가 안먹는 경우

**vi ~/.zshrc**

-> **export ANDROID\_HOME=/Users/$USER/Library/Android/sdk/**

**export PATH=$PATH:$ANDROID\_HOME**

**export PATH=$PATH:$ANDROID\_HOME/tools**

**export PATH=$PATH:$ANDROID\_HOME/platform-tools**

**:wq** 후 엔터

**source ~/.zshrc** -> 적용

**adb** -> 정상작동 확인
