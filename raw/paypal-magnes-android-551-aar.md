<!-- Source: android-magnessdk-5.5.1.aar -->
<!-- Downloaded from: https://paypalobjects.com/magnes-repository/Android/android-magnessdk-5.5.1.zip -->
<!-- Password: mLhZzwNwJoQz -->
<!-- Checksum (SHA-512): 117d252575564f1a1793a120c0b86c6fe1a7c855fc1fcdb3a64c4bf74302e5aedeb630caeb9e94cc6976679c22cc66a9d9bdbc44f5fc2909d95c4f6f56724b27 -->
<!-- Reviewed: 2026-04-15 -->
<!-- Detail directory: raw/magnes-android-551/ -->
<!-- Files saved (read directly from these paths):
  raw/magnes-android-551/AndroidManifest.xml
  raw/magnes-android-551/aar-metadata.properties
  raw/magnes-android-551/classes/MagnesSDK.javap.txt
  raw/magnes-android-551/classes/MagnesSettings$Builder.javap.txt
  raw/magnes-android-551/classes/MagnesSettings.javap.txt
  raw/magnes-android-551/classes/MagnesSource.javap.txt
  raw/magnes-android-551/classes/Environment.javap.txt
  raw/magnes-android-551/classes/MagnesResult.javap.txt
  raw/magnes-android-551/classes/InvalidInputException.javap.txt
-->
<!-- Deep-dive fallback: re-extract android-magnessdk-5.5.1.aar from ~/Downloads (no password needed for .aar) -->

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/magnes-android-551/AndroidManifest.xml` | Package name `lib.android.paypal.com.magnessdk`; minSdkVersion 16 |
| `raw/magnes-android-551/aar-metadata.properties` | AAR format v1.0; minCompileSdk=1; minAndroidGradlePluginVersion=1.0.0 |
| `raw/magnes-android-551/classes/MagnesSDK.javap.txt` | Public API: `getInstance()` singleton, `setUp(MagnesSettings)`, `collect()`, `collectAndSubmit()`, `collectTelemetryData()`, `collectTouchData()` |
| `raw/magnes-android-551/classes/MagnesSettings$Builder.javap.txt` | Builder API: all setter methods including new `setHasUserLocationConsent(boolean)` and `disableBeacon(boolean)` |
| `raw/magnes-android-551/classes/MagnesSettings.javap.txt` | Settings fields + getters: `hasUserLocationConsent()`, `isDisableBeacon()`, `getEnvironment()`, etc. |
| `raw/magnes-android-551/classes/MagnesSource.javap.txt` | Enum: DEFAULT, PAYPAL, EBAY, BRAINTREE, SIMILITY, VENMO; each has `getVersion()` |
| `raw/magnes-android-551/classes/Environment.javap.txt` | Enum: LIVE, SANDBOX |
| `raw/magnes-android-551/classes/MagnesResult.javap.txt` | `getDeviceInfo()` → JSONObject; `getPaypalClientMetaDataId()` → String |
| `raw/magnes-android-551/classes/InvalidInputException.javap.txt` | Checked exception thrown by `setAppGuid()`, `collect()` advanced, `collectAndSubmit()` advanced |

## AAR structure

```
android-magnessdk-5.5.1.aar
├── AndroidManifest.xml        — package + minSdkVersion 16
├── classes.jar                — compiled bytecode (obfuscated a/b/c... + public API classes)
├── annotations.zip            — annotation metadata
├── R.txt                      — resource declarations (empty)
└── META-INF/
    └── .../aar-metadata.properties
```

## Public API (from javap decompilation)

### MagnesSDK (singleton)

```java
public final class MagnesSDK {
    public static synchronized MagnesSDK getInstance();
    public MagnesSettings setUp(MagnesSettings settings);
    public MagnesResult collect(Context context);
    public MagnesResult collect(Context context, String cmid,
                                HashMap<String, String> additionalData)
                                throws InvalidInputException;
    public MagnesResult collectAndSubmit(Context context);
    public MagnesResult collectAndSubmit(Context context, String cmid,
                                         HashMap<String, String> additionalData)
                                         throws InvalidInputException;
    // Telemetry (undocumented)
    public void collectTelemetryData(Context context, EditText editText,
                                     String viewId, String cmid, boolean flag);
    public void setTelemetryFocusChanged(Context context, EditText editText,
                                         String viewId, String cmid, boolean flag);
    public void collectTouchData(MotionEvent event, Context context, String cmid);
}
```

### MagnesSettings.Builder

```java
public class MagnesSettings.Builder {
    public Builder(Context context);
    public Builder setMagnesEnvironment(Environment env);
    public Builder setAppGuid(String appGuid) throws InvalidInputException;
    public Builder setMagnesSource(MagnesSource source);
    public Builder setNotificationToken(String token);
    public Builder disableRemoteConfig(boolean disable);
    public Builder enableNetworkOnCallerThread(boolean enable);
    public Builder setMagnesNetworkingFactory(MagnesNetworkingFactoryImpl factory);
    public Builder setHasUserLocationConsent(boolean consent);  // NEW in 5.5.1
    public Builder disableBeacon(boolean disable);              // undocumented
    public MagnesSettings build();
}
```

### MagnesSource enum

```java
public enum MagnesSource {
    DEFAULT, PAYPAL, EBAY, BRAINTREE, SIMILITY, VENMO;  // SIMILITY + VENMO undocumented
    public int getVersion();
}
```

### MagnesResult

```java
public final class MagnesResult {
    public JSONObject getDeviceInfo();
    public String getPaypalClientMetaDataId();
}
```

## Key findings vs documentation

| Aspect | Documentation | Binary (v5.5.1) |
| --- | --- | --- |
| Min SDK | Not stated | 16 (AndroidManifest) |
| `MagnesSource` values | PAYPAL/EBAY/BRAINTREE/DEFAULT | Adds `SIMILITY`, `VENMO` (same as iOS) |
| `setHasUserLocationConsent` | Documented in 5.5.1 release notes | Confirmed present |
| `disableBeacon` | Not documented | Present as Builder method |
| Telemetry APIs | Not documented | `collectTelemetryData`, `setTelemetryFocusChanged`, `collectTouchData` |
| `MagnesResult.getPaypalClientMetaDataId()` | Docs show camelCase variations | Method name: `getPaypalClientMetaDataId` (lowercase 'p' in 'paypal') |
| Obfuscation | N/A | Internal classes obfuscated as single letters (a, b, c...); public API unobfuscated |
