---
title: "안드로이드 스튜디오 / setOnNavigationItemSelectedListener Deprecated"
source: "https://dev-ej2.tistory.com/4"
tistory_id: "4"
published: "2022-01-10T15:22:44+09:00"
category: "IT/Android"
tags:
---
<https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/bottomnavigation/BottomNavigationView.java#L223>

[GitHub - material-components/material-components-android: Modular and customizable Material Design UI components for Android

Modular and customizable Material Design UI components for Android - GitHub - material-components/material-components-android: Modular and customizable Material Design UI components for Android

github.com](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/bottomnavigation/BottomNavigationView.java#L223)

```
  bnv_main.run { setOnItemSelectedListener {
            when(it.itemId) {
                R.id.tab1 -> {
                    val firstFragment = FirstFragment()
                    supportFragmentManager.beginTransaction().replace(R.id.main_layout, firstFragment).commit()
                }
            }
            true
        }
            selectedItemId = R.id.tab1
        }
```

setOnNavigationItemSelectedListener 대신 setOnItemSelectedListener 사용
