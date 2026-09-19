---
title: "Circular dependency between the following tasks: :app:dataBindingGenBaseClassesDebug"
source: "https://dev-ej2.tistory.com/102"
tistory_id: "102"
published: "2024-05-13T15:18:01+09:00"
category: "IT/Error"
tags:
---
<https://github.com/firebase/firebase-android-sdk/issues/5925>

[Circular dependency between the following tasks: :app:dataBindingGenBaseClassesDebug · Issue #5925 · firebase/firebase-android

[REQUIRED] Step 2: Describe your environment Android Studio version: \_\_\_\_\_ Firebase Component: Crashlytics Gradle Plugin Component version: 3.0.0 [REQUIRED] Step 3: Describe the problem After upgra...

github.com](https://github.com/firebase/firebase-android-sdk/issues/5925)

### 

### Firebase Android BoM (Bill of Materials) version 31.0.0 이후

Could not find com.google.firebase:firebase-core:22.0.0.

->>

**BREAKING CHANGE:** With this release, the BoM no longer contains the following deprecated libraries:  
firebase-appindexing, firebase-core, and firebase-iid. Use the following alternatives instead:

- Instead of firebase-appindexing, use one of the options described in the [documentation](https://firebase.google.com/docs/app-indexing).
- Instead of firebase-iid, use [firebase-installations](https://firebase.google.com/docs/reference/android/com/google/firebase/installations/FirebaseInstallations) or [firebase-installations-ktx](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/installations/ktx/package-summary).
- Instead of firebase-core, use firebase-analytics or [firebase-analytics-ktx](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/ktx/package-summary).

<https://firebase.google.com/support/release-notes/android>
