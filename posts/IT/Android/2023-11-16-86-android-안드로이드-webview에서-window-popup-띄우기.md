---
title: "android / 안드로이드 webview에서 window.popup() 띄우기"
source: "https://dev-ej2.tistory.com/86"
tistory_id: "86"
published: "2023-11-16T18:01:36+09:00"
category: "IT/Android"
tags:
---
웹뷰에서 window.popup()으로 새 창을 띄우는 코드가 있었는데, 안드로이드 앱에서는 새 창이 안뜨는 현상이 발견됐다.

window.popup() 으로 새 창이 뜨면, 안드로이드 내에서 dialog가 뜨게 하여 새로운 webview를 띄우는 방법으로 해결했다.

popup이 뜨는 것을 감지하는 곳은 webChromClient의 onCreateWindow였다.

```
webView.webChromeClient = object:WebChromeClient(){
            override fun onCreateWindow(
                view: WebView?,
                isDialog: Boolean,
                isUserGesture: Boolean,
                resultMsg: Message?
            ): Boolean {
                val popupWebView = WebView(view?.context)
                popupWebView.settings.apply {
                    javaScriptEnabled = true
                    javaScriptCanOpenWindowsAutomatically = true
                    domStorageEnabled = true
                    setSupportMultipleWindows(true)
                }

                val dialog = Dialog(view.context)
                dialog.setContentView(popupWebView)                
                
                dialog.show()

                dialog.setOnKeyListener { _, keyCode, event ->
                    if (keyCode == KeyEvent.KEYCODE_BACK) { 
                        if (popupWebView.canGoBack()) {
                            popupWebView.goBack()
                        } else {
                            dialog.dismiss()
                            popupWebView.destroy() // 팝업 닫힐때 webview destroy
                        }
                        true
                    } else {
                        false
                    }
                }


                popupWebView.webViewClient = WebViewClient()
                popupWebView.webChromeClient = object : WebChromeClient() {
                    override fun onCloseWindow(window: WebView) {
                        dialog.dismiss()
                        window.destroy() // 팝업 닫힐때 window destroy
                    }
                }

                val transport = resultMsg?.obj as WebView.WebViewTransport
                transport.webView = popupWebView
                resultMsg.sendToTarget()
                return true
            }
        }
```

1. onCreateWindow를 오버라이드하여 새로운 webview를 만들어 dialog에 띄웠다.

2. dialog가 닫힐때는 webview destory를 꼭 !!!! 해줘야 한다.

dialog만 닫고, webview destory를 안해주면 다시 window.popup()을 했을때 onCreateWindow가 실행되지 않는다.

\*\* 그밖에 웹뷰 설정

```
newWebView.settings.apply {
    // 컨텐츠 화면에 꽉 차게 표시
    loadWithOverviewMode = true 
    useWideViewPort = true
    // 줌 컨트롤 설정
    builtInZoomControls = true
    displayZoomControls = false
}
```
