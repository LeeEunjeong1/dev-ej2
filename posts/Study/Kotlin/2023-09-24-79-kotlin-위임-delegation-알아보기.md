---
title: "Kotlin / 위임(delegation) 알아보기"
source: "https://dev-ej2.tistory.com/79"
tistory_id: "79"
published: "2023-09-24T16:45:29+09:00"
category: "Study/Kotlin"
tags:
---
모든 객체지향 프로그래밍 언어에서는 클래스 간의 상속관계를 기본 문법으로 제공한다.

코틀린 역시 위임관계를 문법으로 제공해서 다양한 클래스의 관계를 쉽게 처리할 수 있도록 지원한다.

## 1. 클래스 위임 알아보기

클래스 위임 : 특정 클래스에 자기 클래스가 할 일을 다른 클래스에게 맡겨 처리하는 것

코틀린에서 위임 관계를 by를 사용해서 쉽게 구성할 수 있다.

보통 하나의 클래스에는 하나의 책임을 부여해서 설계하는 방식을 사용한다.

위임은 2개의 클래스가 동일한 책임을 가지고 나눠서 처리한다.

**좋은점 : 다양한 기능을 하나의 클래스를 통해서 받고 처리할 수 있도록 구조화할 수 있다.**

```
interface Base { // 인터페이스 정의
    fun say()
}

class BaseImpl(val x: Int) : Base { // 인터페이스를 구현한 위임 클래스 정의
    override fun say() { // 메서드 정의
        println("베이스 클래스 구현 : $x")
    }
}

class Derived(val b: BaseImpl) : Base { // 인터페이스를 구현하고 위임 처리할 객체를 인자로 받음
    override fun say() { // 위임 처리할 메서드 구현
        b.say() // 실제 처리할 메서드 호출
    }
}

val b = BaseImpl(10)
Derived(b).say()


class Derived_() : Base by BaseImpl(10) //  클래스 객체를 생성해서 by로 위임
Derived_().say() // 인터페이스의 메서드 실행

// 베이스 클래스 구현 : 10
// 베이스 클래스 구현 : 10
```

동일한 일을 나눠서 처리하려면 공통된 인터페이스가 필요하다.

인터페이스 Base를 정의하고, 이를 상속한 BaseImpl을 구현한다. 이 클래스는 실제 기능을 대신 처리하는 수탁자 클래스이다.

코틀린 위임을 처리하는 클래스를 정의하고 인터페이스 다음 by 이후에 수탁자 객체를 지정하면 간단한 위임이 구성된다.

### 생성자의 매개변수 속성으로 위임 처리

하나의 인터페이스를 여러 클래스에서 위임을 처리할 수 있다.

```
interface Sayable {
    fun say()
}

class Person_(val x: String) : Sayable {
    override fun say() {
        println("안녕하세요 : $x")
    }
}

class Pet_(val x: String) : Sayable {
    override fun say() {
        println("멍멍멍 : $x")
    }
}

class Saying(val say: Sayable) : Sayable by say // 매개변수로 전달한 객체로 위임 처리

val ps = Person_("사람")
val pt = Pet_("개")

Saying(ps).say()
Saying(pt).say()

// 안녕하세요 : 사람
// 멍멍멍 : 개
```

위탁자와 수탁자 클래스가 같이 사용할 인터페이스를 정의했다.

인터페이스를 상속해서 수탁자로 사용할 수 있는 두 개의 클래스를 정의했다.

주 생성자의 속성의 자료형을 인터페이스로 정의했다. 상속한 인터페이스 다음에 by를 쓰고 속성 이름을 썼다.

객체를 만들어 수탁자 역할을 하는 객체를 전달하고 인터페이스에 있는 메서드를 호출하면 수탁자에 있는 메서드를 실행한다.

이렇게 클래스 위임의 by를 사용하면 위임관계를 간단한 코드로 작성할 수 있다.

### 상속관계 클래스 위임에서 처리 가능

실제 일을 수행하는 수탁자 클래스가 다양한 계층구조를 가져도

위탁자 클래스와 동일한 인터페이스 구현이 되면 이 인터페이스를 기준으로 위임관계를 구성할 수 있다.

```
interface Showable { // 인터페이스 정의
    fun show()
}

open class View : Showable { // 상속 가능한 구현 클래스 정의
    override fun show() { // 메서드 구현
        println("View 클래스의 show()")
    }
}

class CustomView : View() { // 클래스를 상속해서 구현 클래스 정의
    override fun show() { // 메서드 재정의
        println("CustomView 클래스의 show()")
    }
}

class Screen(val showable: Showable) : Showable by showable // 인터페이스만 위임 처리 가능

val view = View() // 베이스 클래스 객체 생성
val customView = CustomView() // 구현 클래스 객체 생성

Screen(view).show() // View.show()
Screen(customView).show() // CustomView.show()

//View 클래스의 show()
//CustomView 클래스의 show()
```

## 2. 속성 위임 알아보기

속성은 메서드를 참조해서 처리하는 방식이므로 속성에도 위임을 처리할 수 있다.

### 속성 위임 규칙

속성에도 by로 위임을 처리할 수 있다.

### 속성 위임 정의

**notNull 위임처리**

Delegates object 내의 notNull 메서드를 사용해서 null값이 들어가지 않도록 처리할 수 있다.

```
import kotlin.properties.Delegates // 코틀린 속성 지연 처리 object

lateinit var str: String // 최상위 속성 지연 초기화는 참조 객체만 가능
//lateinit var int :Int // 최상위 속성 지연 초기화할때는 기본 자료형은 불가

var str1: String by Delegates.notNull<String>()
var int1: Int by Delegates.notNull<Int>()

str = "초기화 처리"
str1 = "초기화 처리"
int1 = 100

println("lateinit 처리 = $str")
println("notNull 처리 = $str1")
println("notNull Int 처리 = $int1")

// lateinit 처리 = 초기화 처리
// notNull  String 처리 = 초기화 처리
// notNull Int 처리 = 100//
```

속성의 지연초기화는 lateinit 예약어로 처리할 수 있다.

속성 위임을 by로 사용하고 Delegates.notNull 메서드를 사용하면 프리미티브도 위임을 통한 지연초기화가 가능하다.

**속성 변경 관찰**

속성 위임을 처리하면 이 속성이 변경되는 상태를 관찰할 수 있다.

```
var observed = false
var max: Int by Delegates.observable(0) { _, oldValue, newValue ->
    println("변경전 : $oldValue 변경후 : $newValue")
    observed = true
}

println(max)
println("관찰상태  = $observed")

max = 10
println(max)
println("관찰상태  = $observed")

// 0
// 관찰상태  = false
// 변경전 : 0 변경후 : 10
// 10
// 관찰상태  = true
```

최상위 속성을 정의하고, Delegates.observable 메서드로 속성 위임을 처리했다.

람다표현식으로 현재 상태와 변경 상태를 처리하는 로직을 인자로 전달했다.

**속성을 변경하면서 출력하면 변경 상태를 확인할 수 있다.**

```
var vetoableField: Int by Delegates.vetoable(0) { _, old, new ->
    println("변경 전 : $old, 변경 후 : $new")
    new % 2 == 0 // 조건이  참인 경우 : 짝수 값일 경우만 갱신
}

println(vetoableField)
vetoableField = 1 // 홀수일 때는 변경되지 않음
println(vetoableField)
vetoableField = 2 //짝수일때만 변경됨
println(vetoableField)

// 0
// 변경 전 : 0, 변경 후 : 1
// 0
// 변경 전 : 0, 변경 후 : 2
// 2
```

특정 값이 참일 경우에는 Delegates.vetoable 메서드로 속성 위임을 통해 값을 변경할 수 있다.

**속성과 지역변수 지연초기화**

속성 위임을 사용하면 지연처리는 val 속성과 val 변수에서 가능하다.

```
val a: Int by lazy { 0 } // 최상위 속성 val 지연처리

class LazyVar {
    val lazya: String by lazy { "초기값" } // 클래스 내의 속성 val 지연처리
    lateinit var lateb: String // 클래스 내의 속성
}

println(a)
val lz = LazyVar()

println(lz.lazya) // val 지연은 처음 조회활 때 초깃값 처리
lz.lateb = "지연 초기화" // var 지연 처리 초기화
println(lz.lateb) // 갱신값 확인
lz.lateb = "값 갱신" // var 값 갱신
println(lz.lateb) // 갱신값 확인

// 0
// 초기값
// 지연 초기화
// 값 갱신
```
