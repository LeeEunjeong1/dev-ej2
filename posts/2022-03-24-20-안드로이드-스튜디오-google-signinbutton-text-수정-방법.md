---
title: "안드로이드 스튜디오 / Google SignInButton Text 수정 방법"
source: "https://dev-ej2.tistory.com/20"
tistory_id: "20"
published: "2022-03-24T12:05:12+09:00"
tags:
---
구글 로그인 버튼의 Text를 바꾸고 싶었다.

조금 옛날 글이지만 역시.. 해결책은 존재했다.

<https://stackoverflow.com/questions/18040815/can-i-edit-the-text-of-sign-in-button-on-google/27838453#27838453>

[Can I edit the text of sign in button on Google?

I am integrating my application with google plus. I have installed google play services and signed in to my account. Also I could publish and plus one for what ever I want. My problem I can't cha...

stackoverflow.com](https://stackoverflow.com/questions/18040815/can-i-edit-the-text-of-sign-in-button-on-google/27838453#27838453)

이  방법을 코틀린으로 살짝 바꾸자면

```
val textView : TextView = binding.btnGoogleLogin.getChildAt(0) as TextView
textView.text = "Google 계정으로 로그인"
```

참고로 binding 사용했고, google SignIn Button의 id는 btn\_google\_login으로 지정하였다.
