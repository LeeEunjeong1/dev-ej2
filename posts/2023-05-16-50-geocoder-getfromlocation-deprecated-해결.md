---
title: "Geocoder - getFromLocation() deprecated 해결"
source: "https://dev-ej2.tistory.com/50"
tistory_id: "50"
published: "2023-05-16T12:23:01+09:00"
tags:
---
getFromLocation(double latitude, double longitude,  int maxResults)  메소드가 API33에서 Deprecated되었다.

getFromLocation(double latitude, double longitude,  int maxResults,  android.location.Geocoder.GeocodeListener) 를 대신 사용하면 된다.

```
//Fetch address from location
geocoder.getFromLocation(latitude,longitude,maxResult,object : Geocoder.GeocodeListener{
 override fun onGeocode(addresses: MutableList<Address>) {

    // code                      
 }
 override fun onError(errorMessage: String?) {
     super.onError(errorMessage)

 }

})
```

<https://developer.android.com/reference/android/location/Geocoder>

[Geocoder  |  Android Developers

developer.android.com](https://developer.android.com/reference/android/location/Geocoder)

<https://stackoverflow.com/questions/73456748/geocoder-getfromlocation-deprecated>

[Geocoder - getFromLocation() deprecated

I've received a message that this function (or it's constructor) has been deprecated. There's a new constructor of that function that accepts an additional parameter 'Geocoder.GeocodeListener liste...

stackoverflow.com](https://stackoverflow.com/questions/73456748/geocoder-getfromlocation-deprecated)
