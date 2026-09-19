---
title: "안드로이드 / android 13 photo picker 사용방법"
source: "https://dev-ej2.tistory.com/80"
tistory_id: "80"
published: "2023-10-05T15:32:08+09:00"
tags:
---
### 사용 배경

기존에 사용하던 Image picker+crop 라이브러리가 android13의 일부 기종에서만 갤러리를 못가지고 왔다.

android13 대응이 되어있지 않은 라이브러리라, 해당 라이브러리 사용이 더이상 힘들었다.

원하는 Image picker+crop 라이브러리가 딱히 없어서,

android13부터 등장한 photo picker를 적용하고, crop라이브러리를 따로 사용했다.

---

crop 라이브러리 적용기는 하단 링크에서~

<https://dev-ej2.tistory.com/81>

[안드로이드 / image crop 라이브러리 사용

Android Image Cropper Android Image Cropper는 쉽게 이미지를 크롭하는 라이브러리이다. https://github.com/CanHub/Android-Image-Cropper GitHub - CanHub/Android-Image-Cropper: Image Cropping Library for Android, optimised for Camera / Gallery

dev-ej2.tistory.com](https://dev-ej2.tistory.com/81)

### 

### photo picker

![](https://blog.kakaocdn.net/dna/bb5Hcn/btswP1Hw8XX/AAAAAAAAAAAAAAAAAAAAAOH2t_RKjaPr4lgEbzsyhGhRZXxKLxAlncouA_i9xc-K/img.gif?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1790780399&allow_ip=&allow_referer=&signature=5frPfKjqh%2F5bTHaKgOKtBWxmhH0%3D)

이렇게 ui까지 제공해주는 갤러리내 photo picker이다.

바텀시트로 되어있어 UI가 따로 놀지 않고, 사용도 간편하다.

### 사용방법

1. app 수준 gradle에 androidx.anctivity를 추가해준다.

```
// build.gradle
implementation "androidx.activity:activity-ktx:1.7.0"
```

2. registerForAcitivityResult를 사용하여 이미지 선택 결과를 콜백받는다.

이미지를 하나만 선택하면 돼서, PickVisualMedia.ImageOnly를 사용했다.

uri를 받아와서, 원하는 로직대로 사용하면 된다.

```
private val pickMedia = registerForActivityResult(ActivityResultContracts.PickVisualMedia()) { uri ->
      // Callback is invoked after the user selects a media item or closes the
      // photo picker.
      if (uri != null) {
          // uri 사용
      } else {
          Log.d("PhotoPicker", "No media selected")
      }
}
```

3. 안드로이드13 이상일 경우에만 해당 이미지피커를 사용하기 위해 조건문을 추가해주었다.

```
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
    pickMedia.launch(PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))
}else{
   // 다른 picker 사용
}
```

### ++) 비디오 선택, 여러 항목 미디어 선택 방법

이미지와 비디오를 선택할 경우는 다음과 같이 사용하면 된다.

```
// Include only one of the following calls to launch(), depending on the types
// of media that you want to let the user choose from.

// Launch the photo picker and let the user choose images and videos.
pickMedia.launch(PickVisualMediaRequest(PickVisualMedia.ImageAndVideo))

// Launch the photo picker and let the user choose only videos.
pickMedia.launch(PickVisualMediaRequest(PickVisualMedia.VideoOnly))

// Launch the photo picker and let the user choose only images/videos of a
// specific MIME type, such as GIFs.
val mimeType = "image/gif"
pickMedia.launch(PickVisualMediaRequest(PickVisualMedia.SingleMimeType(mimeType)))
```

여러 미디어 항목을 선택할 경우는 PickMultipleVisualMedia()안에 원하는 숫자를 넣어주면 된다.

```
// Registers a photo picker activity launcher in multi-select mode.
// In this example, the app lets the user select up to 5 media files.
val pickMultipleMedia =
        registerForActivityResult(PickMultipleVisualMedia(5)) { uris ->
    // Callback is invoked after the user selects media items or closes the
    // photo picker.
    if (uris.isNotEmpty()) {
        Log.d("PhotoPicker", "Number of items selected: ${uris.size}")
    } else {
        Log.d("PhotoPicker", "No media selected")
    }
}

// For this example, launch the photo picker and let the user choose images
// and videos. If you want the user to select a specific type of media file,
// use the overloaded versions of launch(), as shown in the section about how
// to select a single media item.
pickMultipleMedia.launch(PickVisualMediaRequest(PickVisualMedia.ImageAndVideo))
```

공식문서도 잘 나와있고, 사용법도 간단해서 금방 적용할 수 있었다.

<https://developer.android.com/training/data-storage/shared/photopicker?hl=ko>

[사진 선택 도구  |  Android 개발자  |  Android Developers

DataStore는 로컬 데이터를 저장하는 최신 방법을 제공합니다. SharedPreferences 대신 DataStore를 사용해야 합니다. 자세한 내용은 DataStore 가이드를 참고하세요. 사진 선택 도구 컬렉션을 사용해 정리하

developer.android.com](https://developer.android.com/training/data-storage/shared/photopicker?hl=ko)
