## What's Changed

> [!IMPORTANT]
> Adyen Android SDK 5.22.0 requires **Kotlin 2.3** (2.2.20 on Expo 54), **compileSdk and targetSdk 36**, and **Android Gradle Plugin 8.9.1** or newer.
> The minimum supported versions on Android are now **React Native 0.79** and **Expo SDK 54**.
> For the configuration your version needs, see [Compatibility](https://github.com/Adyen/adyen-react-native/blob/develop/docs/Compatibility.md#adyen-android-sdk-5220-kotlin-and-android-sdk-requirements).

  | Name | Version |
  |---|---|
  | [Kotlin Gradle plugin](https://kotlinlang.org/docs/gradle-configure-project.html) | **2.3.0**, or **2.2.20** on Expo SDK 54 |
  | [Android Gradle plugin](https://developer.android.com/build/releases/gradle-plugin) | **8.9.1** |
  | [`compileSdkVersion`](https://developer.android.com/build#module-level) | **36** |
  
  
### Changed

- Dependency versions:

  | Name | Version |
  |---|---|
  | [Android Drop-in/Components](/online-payments/release-notes/?title%5B0%5D=Android+Components%2FDrop-in&version%5B0%5D=5.22.0) | 5.20.0 -> **5.22.0** |
  | [iOS Drop-in/Components](/online-payments/release-notes/?title%5B0%5D=iOS+Components%2FDrop-in&version%5B0%5D=5.27.0) | 5.26.0 -> **5.27.0** |

### Fixed

- On Android: Your app now builds with [Android Gradle plugin 9](https://developer.android.com/build/releases/gradle-plugin) and its built-in Kotlin support.
- On iOS: The `AdyenAppearance` styling is now applied to the embedded `CardView`. Previously, the `CardView` ignored it.

## New Contributors
* @gabrieldonadel made their first contribution in https://github.com/Adyen/adyen-react-native/pull/1221

**Full Changelog**: https://github.com/Adyen/adyen-react-native/compare/2.13.0...2.14.0