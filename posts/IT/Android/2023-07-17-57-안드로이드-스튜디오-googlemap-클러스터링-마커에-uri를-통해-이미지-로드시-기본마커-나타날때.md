---
title: "안드로이드 스튜디오 / GoogleMap 클러스터링 마커에 uri를 통해 이미지 로드시 기본마커 나타날때"
source: "https://dev-ej2.tistory.com/57"
tistory_id: "57"
published: "2023-07-17T11:49:11+09:00"
category: "IT/Android"
tags:
---
구글맵 클러스터링 마커에 glide를 이용하여 이미지를 표시하려고 했는데,

이미지를 로드하기 전에 마커가 먼저 찍혀버려서 기본 마커가 표시되고 난 다음에 이미지 마커가 표시되는 현상이 생겼다.

>>>

마커render가 완료되기 전에는 마커를 안보이게 하고, 마커render가 완료된 시점에 마커를 보이게 해야 한다.

onBeforeClusterItemRendered에서 marker visible을 false로 해주고,

onClusterItemRenedred에서 marker visible을 true로 해주었다.

```
override fun onBeforeClusterItemRendered(
    item: MyItem,
    markerOptions: MarkerOptions
) {
    super.onBeforeClusterItemRendered(item, markerOptions)
    markerOptions.visible(false)
}

override fun onClusterItemRendered(clusterItem: MyItem, marker: Marker) {
    super.onClusterItemRendered(clusterItem, marker)
    val uri = clusterItem.getBitmap()
    Glide.with(context)  .asBitmap() .load(uri)
    .into(object : CustomTarget<Bitmap>() {
        override fun onResourceReady(resource: Bitmap, transition: Transition<in Bitmap>?) {
            marker.setIcon(BitmapDescriptorFactory.fromBitmap(resource))
            marker.isVisible = true
        }

        override fun onLoadCleared(placeholder: Drawable?) {
        }
    })

}
```

위 코드는 클러스터 아이템 마커 ( == 기본 마커) 예시인데,

클러스터링 마커도 onBeforeClusterRendered / onClusterRendered에서  똑같이 해주면된다.

<https://stackoverflow.com/questions/33663992/google-map-cluster-with-url>

[Google map Cluster with Url

I work with Google Map cluster using Android-map-utils library from google. In my case, I use Glide to load image from URL: @Override protected void onBeforeClusterItemRendered(final Feeds...

stackoverflow.com](https://stackoverflow.com/questions/33663992/google-map-cluster-with-url)
