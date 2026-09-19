---
title: "android / 안드로이드 webview history back 화면 스크롤 유지 방법 (activity 이동)"
source: "https://dev-ej2.tistory.com/82"
tistory_id: "82"
published: "2023-10-20T16:47:34+09:00"
tags:
---
안드로이드에서 띄운 webview에서 history back을 하면 전 화면으로 돌아가면서 refresh가 되는 현상이 생겼다.

스크롤을 내렸다가 다음 화면으로 넘어가고 뒤로 돌아왔을때, 화면이 새로고침 되어 스크롤 유지가 안됐다.

화면이 이동돼도, 이전 화면을 유지시키고 싶기 때문에

**특정 화면 이동시 새로운 액티비티를 띄우고, 뒤로 갈때는 새로운 액티비티를 finish 하는 방법을 선택했다**.

1. 다음 화면으로 넘어갈때 새로운 Activity를 만들어 Intent로 페이지 이동

```
override fun shouldOverrideUrlLoading(view: WebView, url: String): Boolean {
	Util.logMessage("shoudOverrideUrlLoading ==> $url")
	if(url.contains("새로운 페이지로 넘어가야할 url")){
	    val intent = Intent(this@MainActivity, NextActivity::class.java).apply {
	        putExtra("url", url)
	    }
		startActivity(intent)
		return true
    }
    return false
}
```

2. 웹에서 back 버튼을 누를때 네이티브 함수를 호출

3. 안드로이드에서 함수가 호출되면 새로운 Activity를 finish() 해준다.

```
finish()
```

history가 남아있어서 history.back이 가능한 것인데.. 왜 reload가 되는지 (안드로이드 웹뷰에서만) ,,,,

원인을 알게된다면 그에 맞춰서 수정해야겠다.
