---
title: iOS Objective-C SDK Integration of Magnes
slug: /limited-release/magnes/integrate/ios-objective-c/
createTime: "2024-08-15T05:59:08.521Z"
updateTime: "2024-08-15T05:59:08.770Z"
---

# iOS Objective-C SDK Integration of Magnes

## Before you begin

The following table lists prerequisite information for integrating Magnes on the iOS platform:

| Prerequisite           | Description                                                                                                                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OS version             | Using the latest iOS version is recommended.                                                                                                                                              |
| Software configuration | Magnes iOS Objective-C library supports apps written in Objective-C. PPRMOCMagnesSDK is the central interface for Objective-C library. It provides the singleton access for the host app. |

## Designate frameworks

Before you initialize Magnes, you must set several frameworks as **required** so that Magnes can access essential mobile data for risk assessment. For example, by setting CoreLocation.framework as required, Magnes can access the current location of the mobile device. This is not mandatory from Xcode 14.

Set the following frameworks as **required** .

- Security.framework
- CFNetwork.framework
- SystemConfiguration.framework
- MessageUI.framework
- CoreLocation.framework
- Foundation.framework
- CommonCrypto.framework
- UIKit.framework

For more information about setting up required frameworks, visit [https://developer.apple.com](https://developer.apple.com) .

### Import the library

You must add the library to the application for accessing the APIs in the app. The library is contained in a framework you can add. To import the Objective-C library, link libPPRiskMagnesOC.a to the app, then go to **Build Phases** and select **Link Binaries with Libraries** . Import the following files from the Objective-C library: PPRMOCMagnesSDK.h , PPRMOCMagnesSDKResult.h

## Set up Magnes for Objective-C

Magnes must be set up at app startup. The **SetUp** call is executed only once per lifecycle of a Magnes Singleton Instance. The Setup Parameters below are optional. You can set up with empty string values.

The **SetUp** call either passes the merchant app’s app_guid , or Magnes creates an app_guid to identify the app. An app_guid is a unique installation identifier of the app for a particular mobile device. If the app is reinstalled, a new app_guid is generated.

### Magnes setup – simple

PPRMOCMagnesSDK \*PPRMOCMagnesSDK = [PPRMOCMagnesSDK shared];### Magnes setup – advanced

- (void)setUpOptionalAppGuid:(NSString _)appGuid
  withOptionalAPNToken:(NSString _)apnToken
  disableRemoteConfiguration:(Boolean)isDisabled
  forMagnesSource:(MagnesSourceFlow)magnesSource;

PPRMOCMagnesSDK \*PPRMOCMagnesSDK = [PPRMOCMagnesSDK shared];
[_PPRMOCMagnesSDK setOptionalAppGuid: "YOUR-APPGUID",
withOptionalAPNToken:"YOUR-APP-NOTIFICATION-TOKEN",
disableRemoteConfiguration: false,
forMagnesSource: MAGNES_SOURCE_DEFAULT];### Setup parameters and methods
| Parameter Name | Data Type | Description |
| --- | --- | --- |
| setEnviroment | Environment | Setting the environment for Magnes. Please pass EnvironmentLIVE for production release. EnvironmentSANDBOX ,if we need to verify prior to production release |
| setOptionalAppGuid | String | Sets an application's globally unique identifier, which identifies the merchant application that sets up Magnes on the mobile device. If the merchant app does not pass anAppGuid, Magnes creates one to identify the app. If the app is installed or reinstalled, it receives a newAppGuid. Maximum length: 36 characters. |
| withOptionalAPNToken | String | Use an Apple Push Notification Service (APNS) token to send notifications to the mobile device. |
| disableRemoteConfiguration | Boolean | Enables the consumer app to receive the latest Magnes configuration settings. The default isfalse. |
| forMagnesSource | MagnesSource | Integration defined sources:MAGNES_SOURCE_PAYPAL=10,MAGNES_SOURCE_EBAY=11,MAGNES_SOURCE_BRAINTREE=12,MAGNES_SOURCE_DEFAULT=-1 |

## Collect and submit the payload

When the user launches the mobile app, Magnes remains active only while the setup, Collect, and CollectAndSubmit methods are called. It does not passively collect data in the background.

You can turn on the debugging log to ensure that Magnes is running successfully.

Magnes generates and returns a new PayPal-Client-Metadata-Id , which is a unique 32-character string. Upon collecting the core and dynamic data, Magnes triggers the library , which transmits an asynchronous payload to PayPal Risk Services.

Ordinarily, Magnes generates the PayPal-Client-Metadata-Id , but you can pass in a value to be used as the ID.

### Collect data from Objective-C app

Execute the following code snippets in order to trigger the Objective-C library to collect the payload data.

#### Collect data – simple

//PPRMOCMagnesSDK *magnesSDK = [PPRMOCMagnesSDK shared];
PPRMOCMagnesSDKResult *magnesResult = [magnesSDK collect];#### Collect data – advanced
//PPRMOCMagnesSDK *magnesSDK = [PPRMOCMagnesSDK shared];
PPRMOCMagnesSDKResult *magnesResult =
[magnesSDK collectWithPayPalClientMetadataId:"YOUR-PAYPAL-CLIENT-METADATA-ID"
withAdditionalData:@{}];### Collect and submit data from Objective-C app
Execute the following code snippet in order to trigger the library to collect the payload data and send it to the PayPal server.

#### Collect and submit – simple

//PPRMOCMagnesSDK *magnesSDK = [PPRMOCMagnesSDK shared];
PPRMOCMagnesSDKResult *magnesResult = [magnesSDK collectAndSubmit];#### Collect and submit – advanced
//PPRMOCMagnesSDK *magnesSDK = [PPRMOCMagnesSDK shared];
PPRMOCMagnesSDKResult *magnesResult =
[magnesSDK
collectAndSubmitWithPayPalClientMetadataId:@"YOUR-PAYPAL-CLIENT-METADATA-ID"
withAdditionalData:@{}];### Specifying additional data
The merchant can include any additional wanted key-value pair data in the Magnes payload. To pass additional data as a dictionary of key-value pairs, execute the following code snippets.

| Parameter                     | Data Type        | Description                                                                                                                                                              |
| ----------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| withPaypalClientMetaDataId id | String           | Your own unique identifier for the payload. If you do not pass in this value, a newPayPal-Client-Metadata-Idis generated per method call. Maximum length: 32 characters. |
| withAdditionalData data       | [String: String] | Any key-value pair in this dictionary is injected into the payload submitted to the PayPal server.                                                                       |

## Get the Magnes result

In every data collection call, the Magnes Library returns back to the caller a MagnesResult containing the latest device information and the PayPal-Client-Metadata-Id :

### Get the MagnesResult from Objective-C app

// cached the MagnesResult from previous collectAndSubmit call.
PPRMOCMagnesSDK *magnesSDK = [PPRMOCMagnesSDK shared];
PPRMOCMagnesSDKResult *magnesResult = [magnesSDK collectAndSubmit];

NSString *payPalClinetMetaDataId = [magnesResult getPayPalClientMetaDataId];
NSDictionary *deviceInfo = [magnesResult getDeviceInfo];The following table lists methods you can use in a data collection call.

| Method                      | Data Type  | Description                                                                                                 |
| --------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------- |
| getPaypalClientMetaDataId() | String     | The newly generated (or passed in)PayPal-Client-Metadata-Idfrom the latest API call.                        |
| getDeviceInfo()             | JSONObject | A full device information payload. This payload is identical to the payload submitted to the PayPal server. |

## Send the PayPal-Client-metadata-ID from the merchant server to PayPal

The PayPal-Client-Metadata-Id pairs the Magnes payload in the context of a PayPal transaction payment, login, or consent, or other PayPal activity.

When the merchant server makes a call to PayPal Payment or other APIs, that payment call must include the most recent PayPal-Client-Metadata-Id that Magnes (or the merchant app) provided. For most REST APIs, you must include in the call header the PayPal-Client-Metadata-Id key with the ID’s most recent value as that key’s value.

For other APIs, refer to the API documentation or integration details provided by your PayPal representative.
