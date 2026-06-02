---
title: Android Integration of Magnes
slug: /limited-release/magnes/integrate/android/
createTime: "2024-08-15T06:13:17.898Z"
updateTime: "2024-08-15T06:13:18.298Z"
---

# Android Integration of Magnes

## Before you begin

The following table lists prerequisite information for integrating Magnes on the Android platform:

| Prerequisite           | Description                                                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| OS version             | Use the latest Android version, if possible.                                                                                   |
| Software configuration | The central class for Magnes islib.android.paypal.com.magnessdk.MagnesSDK. This class provides single access for the host app. |

## Adding permissions

Before initializing the Magnes library, you must add permissions and metadata settings in the app's manifest file so Magnes can access essential mobile data for risk assessment. Add the following in AndroidManifest.XML :

&lt;manifest&gt;
&lt;!-- following permissions are optional --&gt;
&lt;uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" /&gt;
&lt;uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" /&gt;
&lt;uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" /&gt;
&lt;uses-permission android:name="android.permission.ACCESS_WIFI_STATE" /&gt;
&lt;uses-permission android:name="android.permission.GET_ACCOUNTS" /&gt;
&lt;uses-permission android:name="android.permission.INTERNET" /&gt;
&lt;uses-permission android:name="android.permission.READ_PHONE_STATE" /&gt;
&lt;!-- for reading GSF ID --&gt;
&lt;uses-permission
android:name="com.google.android.providers.gsf.permission.READ_GSERVICES" /&gt;
&lt;/manifest&gt;## Setting up Magnes
Magnes must be set up at app startup. The setUp call is executed only once per lifecycle of a Magnes Singleton Instance. The Setup parameters and methods listed below are optional. You can set Magnes to use either simple or advanced setup. Advanced setup gives more customizability and the option to pass in more parameters. Most developers will opt for the simple setup. Use those with which you are familiar, otherwise build a default setup without using any parameters.

### Magnes setup – simple

MagnesSettings magnesSettings = new MagnesSettings.Builder(context).build();
MagnesSDK.getInstance().setUp(magnesSettings);### Magnes setup – advanced
magnesSettings = new MagnesSettings.Builder(@NonNull Context context)
.setAppGuid(@Size(max = APPGUID_MAXLENGTH) String appGuid)
.setMagnesEnvironment(Environment.LIVE)
.setMagnesSource(@MagnesSource.SourceFlow int sourceFlow)
.setNotificationToken(String notificationToken)
.setMagnesNetworkingFactory
(MagnesNetworkingFactoryImpl magnesNetworkingFactoryImpl)
.enableNetworkOnCallerThread(boolean networkOnCallerThread)
.disableRemoteConfig(boolean disableRemoteConfig)
.build();
MagnesSDK.getInstance().setUp(magnesSettings);### Setup parameters and methods
| Parameter or Method | Data Type | Description |
| --- | --- | --- |
| context | Context | Android application context |
| setAppGuid() | String | Sets an application's globally unique identifier, which identifies the merchant application that sets up Magnes on the mobile device. If the merchant app does not pass anAppGuid, Magnes creates one to identify the app. If the app is installed or reinstalled, it receives a newAppGuid. Maximum length: 36 characters. |
| setMagnesEnvironment | enum Environment | Setting the environment for Magnes. Please passEnvironment.LIVE , for production release. Environment.SANDBOX for sandbox environment, if a verification has to be done prior to production release |
| SetMagnesSource() | IntDef | Integration defined sources:MagnesSource.PAYPAL,MagnesSource.EBAY, andMagnesSource.BRAINTREE. If none of these apply to your integration, either useMagnesSource.DEFAULTor do not set a source. |
| disableRemoteConfig() | Boolean | Toggle to trigger a remote configuration networking call. It triggers once per application lifecycle. The default isfalse. |
| enableNetworkOnCallerThread() | Boolean | Enable a network call on the current caller thread. **Note:**It might throw aNetworkOnMainThreadExceptionif your caller thread is the main thread. |
| setMagnesNetworking Factory() | MagnesNetworkingFactoryImpl | Magnes uses this custom networking factory instead of the Magnes default one in order to trigger the networking call. You must implementMagnesNetworkingandMagnesNetworkingFactory. |

## Collect and submit the payload

When the user launches the mobile app, Magnes remains active only while the Setup , Collect , and CollectAndSubmit methods run. It does not passively collect data in the background.

You can turn on the debug log to ensure that Magnes is running successfully.

Magnes generates and returns a new PayPal-Client-Metadata-Id , which is a unique 32-character string. Upon collecting the core and dynamic data, Magnes causes the library to submit an asynchronous payload to PayPal Risk Services.

Ordinarily, Magnes generates the PayPal-Client-Metadata-Id , but you can pass in a value to be used as the ID.

### Magnes CollectAndSubmit - simple

MagnesResult magnesResult = MagnesSDK.getInstance()
.collectAndSubmit(@NonNull Context context)### Magnes CollectAndSubmit - advanced
MagnesResult magnesResult = MagnesSDK.getInstance()
.collectAndSubmit(Context context, String paypalClientMetaDataId,
HashMap&lt;String, String&gt;
additionalData)The following table lists parameters you can pass in the payload, including additional wanted data as key-value pairs.

| Parameter              | Data Type                     | Description                                                                                                                                                              |
| ---------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| context                | Context                       | Android application context.                                                                                                                                             |
| PaypalClientMetaDataID | String                        | Your own unique identifier for the payload. If you do not pass in this value, a newPayPal-Client-Metadata-Idis generated per method call. Maximum length: 32 characters. |
| additionalData         | HashMap&lt;String, String&gt; | Any key-value pair in this HashMap is injected into the payload submitted to the PayPal server.                                                                          |

## Get the Magnes result

In every data collection call, the Magnes Library returns back to the caller a MagnesResult containing the latest device information and the PayPal-Client-Metadata-Id :

### MagnesResult

// cached the MagnesResult from previous collectAndSubmit call.
// MagnesResult magnesResult =
// MagnesSDK.getInstance().collectAndSubmit(@NonNull Context context)
//
String paypalcmid = magnesResult.getPaypalClientMetaDataId()
JSONObject deviceInfo = magnesResult.getDeviceInfo()The following table lists methods you can use in a data collection call.

| Method                      | Data Type  | Description                                                                                                 |
| --------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------- |
| getPaypalClientMetaDataId() | String     | The newly generated (or passed in)PayPal-Client-Metadata-Idfrom the latest API call.                        |
| getDeviceInfo()             | JSONObject | A full device information payload. This payload is identical to the payload submitted to the PayPal server. |

## Send the PayPal-Client-Metadata-ID from the merchant server to PayPal

The PayPal-Client-Metadata-Id pairs the Magnes payload in the context of a PayPal transaction payment, login, or consent, or other PayPal activity.

When the merchant server makes a call to PayPal Payment or other APIs, that payment call must include the most recent PayPal-Client-Metadata-Id that Magnes (or the merchant app) provided. For most REST APIs, you must include in the call header the PayPal-Client-Metadata-Id key with the ID’s most recent value as that key’s value.

For NVP/SOAP or other APIs, refer to the API documentation or integration details provided by your PayPal representative.
