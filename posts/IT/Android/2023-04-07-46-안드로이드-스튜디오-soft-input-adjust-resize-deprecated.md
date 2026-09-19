---
title: "안드로이드 스튜디오 / SOFT_INPUT_ADJUST_RESIZE deprecated"
source: "https://dev-ej2.tistory.com/46"
tistory_id: "46"
published: "2023-04-07T22:23:37+09:00"
category: "IT/Android"
tags:
---
SOFT\_INPUT\_ADJUST\_RESIZE를 맨 하단에 있는 editText를 클릭했을때 soft keybord가 올라오면서 editText가 안가려지게 하기 위해 사용하고 싶었으나, 안드로이드30이상부터 deprecated 되었다.

30 이상은 **setDecorFitsSystemWindows** 를 제공한다고 한다.

이렇게 분기처리를 해주면 된다.

```
   if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
                binding.root.setOnApplyWindowInsetsListener { _, windowInsets ->
                    val imeHeight = windowInsets.getInsets(WindowInsets.Type.ime()).bottom
                    binding.root.setPadding(0, 0, 0, imeHeight)
                    val insets =
                        windowInsets.getInsets(WindowInsets.Type.ime() or WindowInsets.Type.systemGestures())
                    insets
                    windowInsets
                }
            }else{
                requireActivity().window.setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_STATE_ALWAYS_HIDDEN or WindowManager.LayoutParams.SOFT_INPUT_ADJUST_RESIZE)
            }
```

<https://stackoverflow.com/questions/68003131/soft-input-adjust-resize-deprecated-starting-android-30>

[SOFT\_INPUT\_ADJUST\_RESIZE deprecated starting android 30

I used SOFT\_INPUT\_ADJUST\_RESIZE in order to show all content when keyboard pops up. Following documentation, I added new code pieces: if (Build.VERSION.SDK\_INT >= Build.VERSION\_CODES.R) {

stackoverflow.com](https://stackoverflow.com/questions/68003131/soft-input-adjust-resize-deprecated-starting-android-30)
