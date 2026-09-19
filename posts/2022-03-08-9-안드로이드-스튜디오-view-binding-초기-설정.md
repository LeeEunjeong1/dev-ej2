---
title: "안드로이드 스튜디오 / View Binding 초기 설정"
source: "https://dev-ej2.tistory.com/9"
tistory_id: "9"
published: "2022-03-08T16:15:10+09:00"
tags:
---
1. build.gradle(app)

```
buildFeatures{
    viewBinding = true
}

dependencies {
    implementation 'androidx.databinding:databinding-runtime:7.1.2'
}
```

2. Binding할 Activity

```
class SplashActivity :AppCompatActivity() {
    private lateinit var binding: ActivitySplashBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivitySplashBinding.inflate(layoutInflater)
        setContentView(binding.root)
    }
}
```

참 쉽죵
