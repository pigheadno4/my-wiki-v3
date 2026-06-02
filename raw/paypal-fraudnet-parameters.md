---
title: FraudNet configuration parameters
slug: /limited-release/fraudnet/integrate/add-parameter-block/
createTime: "2024-08-15T07:19:43.535Z"
updateTime: "2025-10-27T10:21:00.930Z"
---

# FraudNet configuration parameters

## Configuration parameters

Add the following parameters as needed to your parameter block:

| Identifier | Name                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                  | Constraints                                                       | Required? |
| ---------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------- |
| f          | FraudNet Session Identifier  | The integration developer provides the identifier. It must be unique and random to the current transaction (or session) that FraudNet is monitoring. It must be unique and random each time the webpage is loaded. During the transaction, the session identifier must be passed to the PayPal Server via the REST API header PAYPAL-CLIENT-METADATA-ID.                                                                     | Maximum length: 32 characters                                     | Yes       |
| s          | Source Website Identifier    | This string identifies the source website of the FraudNet request. If your app has Fraudnet integration on multiple pages, each web page must have a different source identifier. Each web page you integrate with FraudNet must have a different source identifier. Recommended format is&lt;MERCHANT_NAME_FLOW_NAME&gt;or&lt;MERCHANT_NAME_PAGE_NAME&gt;. Examples:PAYPAL_LOGIN_USERNAME,PAYPAL_LOGIN_PASSWORD, and so on. | Maximum length: 32 characters                                     | Yes       |
| cb1        | Callback function            | The callback function called on completion of FraudNet p1 (POST 1) execution.                                                                                                                                                                                                                                                                                                                                                | String (a function name defined on the page)                      | No        |
| cb2        | Callback function            | A callback function called on completion of FraudNet p2 (POST 2) execution.                                                                                                                                                                                                                                                                                                                                                  | String (a function name defined on the page)                      | No        |
| fp         | First Party Cookie           | The first-party cookie from the merchant that is passed to FraudNet.                                                                                                                                                                                                                                                                                                                                                         | Maximum length: 32 characters                                     | No        |
| mm         | Enable mouse movement        | Enables mouse movement collection.                                                                                                                                                                                                                                                                                                                                                                                           | Boolean, Default: true                                            | No        |
| ts         | Enable & Config Typing Speed | Enables and configures typing speed collection, specifying the flow and fields (one or multiple) that the client wants monitored. The fields are the IDs of the html elements. See the Typing Speed Configuration section below.                                                                                                                                                                                             | Object                                                            | No        |
| b          | Beacon URL                   | A custom URL for the Beacon endpoint.                                                                                                                                                                                                                                                                                                                                                                                        | Do not set this value unless you have a specific use case for it. | String    |
| cd         | Cache FraudNet Data          | Caches the FraudNet payload for a certain amount of time to prevent re-submission of same payloads. Do not set this value unless you have a specific use case for it.                                                                                                                                                                                                                                                        | Boolean, Default:false                                            | No        |
| sandbox    | Sandbox                      | Enables or disables sandbox environment.                                                                                                                                                                                                                                                                                                                                                                                     | Boolean, Default:false                                            | No        |
| bu         | Beacon                       | Enables or disables Beacon.                                                                                                                                                                                                                                                                                                                                                                                                  | Boolean, Default:true                                             | No        |

### Typing speed parameters

Configure FraudNet to capture typing speed data in order to detect bot data entry.

| Parameter | Details                                                                                                                                                                                                                                                                  | Required? |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- |
| Type      | String. Provides(Source Website Identifier) parameter.                                                                                                                                                                                                                   | Required  |
| Fields    | Array of strings. Thefieldsare the IDs of the html elements.                                                                                                                                                                                                             | Required  |
| Min       | Number. The length of characters for the last field. Defaults to 8                                                                                                                                                                                                       | Optional  |
| Delegate  | Boolean. If set to true, then the Typing Speed event listeners will be delegated. If set to false, then the Typing Speed event listeners will be attached to each field. Defaults to false. If you aren't sure what value this should be set to, please reach out to us. | Optional  |

Typing speed example:

{
"type": "UL",
"fields": ["email", "password"]

// OPTIONAL CONFIG
"min": 8
"delegate": false
}
