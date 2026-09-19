---
title: "안드로이드 스튜디오/ startActivityForResult Deprecated"
source: "https://dev-ej2.tistory.com/17"
tistory_id: "17"
published: "2022-03-23T18:47:58+09:00"
tags:
---
startActivityForResult가 Deprecated 되었다.

요즘 registerForActivityResult로 대체해서 쓰고있다.

1. intentParam() 따로  빼주기 (필수X, 편의상 )

```
fun getIntentParam(): Intent{
	val newIntent = Intent(this.context,Activity::class.java)
    newIntetn.putExtra()
    
    return newIntent
}
```

2. registerForActivityResult 사용하기

```
private var getResult = registerForActivityResult(ActivityResultContracts.StartActivityForResult()){
	if(it.resultCode == AppCompatActivity.RESULT_OK){
    	//실행하고 싶은 것 
    }
}
```

3. launch

```
val intent = getIntentParam()

getResult.launch(intent)
```

- 참고

<https://developer88.tistory.com/351>
