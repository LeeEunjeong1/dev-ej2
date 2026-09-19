---
title: "Compose / 선언형 UI(Declarative UI)란 무엇인가 (명령형 UI와의 차이)"
source: "https://dev-ej2.tistory.com/60"
tistory_id: "60"
published: "2023-07-17T23:56:44+09:00"
category: "Study/Compose"
tags:
---
## 기존 UI 방식

사용자 상호작용 등의 이유로 인해 앱의 상태가 변경되면, 현재 데이터를 표시하기 위해 UI 계층 구조를 업데이트해야 한다.

UI를 업데이트하는 가장 일반적인 방법은 [findViewById()](https://developer.android.com/reference/android/view/View?hl=ko#findViewById(int))와 같은 함수를 사용하여 트리를 탐색하고

 button.setText(String), container.addChild(View) 또는 img.setImageBitmap(Bitmap)과 같은 메서드를 호출하여 노드를 변경하는 것이다.

이 기법은 처음부터 화면 전체를 개념적으로 재생성한 후 필요한 변경사항만 적용하는 방식으로 작동한다.

데이터를 여러 위치에서 렌더링한다면 데이터를 표시하는 뷰 중 하나를 업데이트하는 것을 잊기 쉽다.

또한 두 업데이트가 예기치 않은 방식으로 충돌할 경우 잘못된 상태를 야기하기도 쉽다.

## 선언형 UI

지난 몇 년에 걸쳐 업계 전반에서 선언형 UI 모델로 전환하기 시작했으며,

이에 따라 사용자 인터페이스 빌드 및 업데이트와 관련된 엔지니어링이 크게 간소화되었다.

이 기법은 처음부터 화면 전체를 개념적으로 재생성한 후 필요한 변경사항만 적용하는 방식으로 작동한다.

이러한 접근 방식은 스테이트풀(Stateful) 뷰 계층 구조를 수동으로 업데이트할 때의 복잡성을 방지할 수 있다.

Compose는 선언형 UI 프레임워크이다.

화면 전체를 재생성하는 데 있어 한 가지 문제는 시간, 컴퓨팅 성능 및 배터리 사용량 측면에서 잠재적으로 비용이 많이 든다는 것이다.

이 비용을 줄이기 위해 Compose는 특정 시점에 UI의 어떤 부분을 다시 그려야 하는지를 지능적으로 선택한다.

## 명령형 UI와의 차이

많은 명령형 객체 지향 UI 도구 키트를 사용하여 위젯의 트리를 인스턴스화함으로써 UI를 초기화한다.

흔히 XML 레이아웃 파일을 확장하여 이 작업을 한다.

각 위젯은 자체의 내부 상태를 유지하고 앱 로직이 위젯과 상호작용할 수 있도록 하는 getter 및 setter 메서드를 노출한다.

Compose의 선언형 접근 방식에서 위젯은 비교적 스테이트리스(Stateless) 상태이며 setter 또는 getter 함수를 노출하지 않는다.

사실상 위젯은 객체로 노출되지 않는다.

동일한 구성 가능한 함수를 다른 인수로 호출하여 UI를 업데이트한다.

이렇게 하면 [앱 아키텍처 가이드](https://developer.android.com/jetpack/guide?hl=ko)에 설명된 대로 [ViewModel](https://developer.android.com/reference/androidx/lifecycle/ViewModel?hl=ko)과 같은 아키텍처 패턴에 상태를 쉽게 제공할 수 있다.

그런 다음, 컴포저블은 식별 가능한 데이터가 업데이트될 때마다 현재 애플리케이션 상태를 UI로 변환한다.

![](https://blog.kakaocdn.net/dna/buxsUN/btsn0gMma2q/AAAAAAAAAAAAAAAAAAAAAAKPkTIkyuke9exbu3yTOQKGNfVPnpROE3u9b6CpBq9U/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1790780399&allow_ip=&allow_referer=&signature=CSNcgMFLWuUpg9SxP%2FqePpfBtao%3D)

앱 로직은 최상위의 구성 가능한 함수에 데이터를 제공한다.

함수는 데이터를 사용하여 다른 컴포저블을 호출함으로써 UI를 형성하고 적절한 데이터를 해당 컴포저블 및 계층 구조 아래로 전달한다.

사용자가 UI와 상호작용할 때 UI는 onClick과 같은 이벤트를 발생시킨다.

이러한 이벤트를 앱 로직에 전달하여 앱의 상태를 변경해야 한다.

상태가 변경되면 구성 가능한 함수는 새 데이터와 함께 다시 호출된다.

이렇게 하면 UI 요소가 다시 그려진다. 이 프로세스를 재구성이라고 한다.

![](https://blog.kakaocdn.net/dna/ryAPa/btsnZg0t3jb/AAAAAAAAAAAAAAAAAAAAAFWNPDAsDdS7GgmPet2yyERuSMhSmyxCTGxCgN7X-hiZ/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1790780399&allow_ip=&allow_referer=&signature=6KvZlttHB59gJ1EFYmxpdjGm5R8%3D)

사용자가 UI 요소와 상호작용하며 이에 따라 이벤트가 트리거된다.

앱 로직이 이벤트에 응답한다. 그러면 구성 가능한 함수가 필요한 경우 새 매개변수를 사용하여 자동으로 다시 호출된다.

<https://developer.android.com/jetpack/compose/mental-model?hl=ko>

[Compose 이해  |  Jetpack Compose  |  Android Developers

Compose 이해 컬렉션을 사용해 정리하기 내 환경설정을 기준으로 콘텐츠를 저장하고 분류하세요. Jetpack Compose는 Android를 위한 현대적인 선언형 UI 도구 키트입니다. Compose는 프런트엔드 뷰를 명령

developer.android.com](https://developer.android.com/jetpack/compose/mental-model?hl=ko)
