---
title: "안드로이드 스튜디오 / To get local formatting use getDateInstance(), getDateTimeInstance(), or getTimeInstance(), or use new SimpleDateFormat(String template, Locale locale) with for example Locale.US for ASCII dates."
source: "https://dev-ej2.tistory.com/25"
tistory_id: "25"
published: "2022-04-14T12:31:50+09:00"
tags:
---
```
val date = SimpleDateFormat("yyyyMMdd").parse(value)
```

To get local formatting use getDateInstance(), getDateTimeInstance(), or getTimeInstance(), or use new SimpleDateFormat(String template, Locale locale) with for example Locale.US for ASCII dates.

현재날짜를 받고싶었는데, 해당 경고가 뜬다.

Locale 클래스는 해당 지역의 정보를 담고 있는  클래스. 해당 지역의 정보를 추가해주면 경고가 사라진다.

```
val date = SimpleDateFormat("yyyyMMdd", Locale.getDefault()).parse(value)
```

Locale.getDefault() 추가해줌.
