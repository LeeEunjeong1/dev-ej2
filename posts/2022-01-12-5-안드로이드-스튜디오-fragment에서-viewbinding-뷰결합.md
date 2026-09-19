---
title: "안드로이드 스튜디오 / Fragment에서 ViewBinding (뷰결합)"
source: "https://dev-ej2.tistory.com/5"
tistory_id: "5"
published: "2022-01-12T11:21:20+09:00"
tags:
---
build.gradle에 viewBinding 허용해준다.

```
android {
        ...
        viewBinding {
            enabled = true
        }
    }
```

**onCreateView** 메서드에서

1. 정적 inflate()메서드 호출한다. 프래그먼트에서 사용할 결합 클래스 인스턴스가 생성된다.'

2. getRoot() 메서드를 호출하거나 Kotlin 속성 구문을 사용하여 루트 뷰 참조를 가져온다.

3. onCrateView(). 메서드에서  루트 뷰를 반환한다.

```
	private var lBinding: FragmentMainReservationBinding? = null
    private val binding get() = lBinding!!

    override fun onCreateView(inflater: LayoutInflater,container: ViewGroup?,savedInstanceState: Bundle?): View {
        lBinding = FragmentMainReservationBinding.inflate(inflater, container, false)
        return binding.root
        //return inflater.inflate(R.layout.fragment_main_reservation, container, false)

    }
    override fun onDestroy() {
        super.onDestroy()
        lBinding = null
    }
```

**onViewCreated**에서 Binding 사용할 수 있다.

```
override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        binding.btnCheck.setOnClickListener{
        //버튼 클릭하면 할 동작
        }
    }
```

![](https://blog.kakaocdn.net/dna/bjAJfQ/btrqwuBkWkY/AAAAAAAAAAAAAAAAAAAAADG-94VUOrBV_OkpfTkRwirsCW9TVsijfqhRd2CJjgAN/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1790780399&allow_ip=&allow_referer=&signature=btRKt0NMXwa33uB3%2BTUlj%2FKVKG8%3D)

갑자기 Fragment 생명주기가 왜 나오나 싶겠지만...

onCreate에서 binding.btn은 대뜸 하려는 바보같은 시도는 다시 하지 않길 바라며..

activity에서 흔히 쓰는 onCreate에서 binding하면 당연히 될 줄 알았는데..

onCreateView에서(뷰가 생성될때) 바인딩 연결 해놓고, 해당 메서드 실행도 전에 onCreate에서(프래그먼트 생성될떄, 뷰 생성 전) 바인딩 쓰려고 하니 당연히 안된다.

https://developer.android.com/topic/libraries/view-binding?hl=ko
