---
title: FraudNet payloads reference
slug: /limited-release/fraudnet/reference/
createTime: "2024-08-15T07:03:38.770Z"
updateTime: "2024-08-15T07:03:39.053Z"
---

# FraudNet payloads reference

FraudNet delivers several payloads. This section describes the variables for each payload and provides further information about FraudNet payloads.

## Payload P1 (POST 1)

| Field Name                           | Source                  | Description                                                                                                                                                                                                               |
| ------------------------------------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| appId                                | (client-generated)      | Client-generated source ID passed to FraudNet                                                                                                                                                                             |
| correlationId                        | (client-generated)      | Client-randomly-generated sequence passed to FraudNet. Identical to CMID, and must be unique per session, with the CMID in the Fraudnet payloads matching the CMID in the payment API call. Maximum length: 32 characters |
| **Category: payload**                |                         |                                                                                                                                                                                                                           |
| referer                              | document.referrer       | Header indicating the URL of the page where FraudNet is embedded                                                                                                                                                          |
| URL                                  | document.URL            | Returns the location of the current document                                                                                                                                                                              |
| rvr                                  | (generated)             | Version of the FraudNet JavaScript                                                                                                                                                                                        |
| activeXDefined                       | window.ActiveXObject    | (IE only) Returns if an ActiveX is defined for Internet Explorer                                                                                                                                                          |
| tz                                   | (generated)             | Browser’s time zone (utc_offst_ms_cnt/3600000)                                                                                                                                                                            |
| tzName                               | (generated)             | Browser’s time zone, in long format                                                                                                                                                                                       |
| time                                 | new Date().getTime()    | Current time returned by the FraudNet JavaScript                                                                                                                                                                          |
| **Category: payload.navigator**      |                         |                                                                                                                                                                                                                           |
| appName                              | window.navigator        | Name of the browser                                                                                                                                                                                                       |
| appVersion                           | window.navigator        | Version of the browser                                                                                                                                                                                                    |
| cookieEnabled                        | window.navigator        | Returns whether cookies are enabled in the browser                                                                                                                                                                        |
| language                             | window.navigator        | Language of the browser application                                                                                                                                                                                       |
| onLine                               | window.navigator        | Returns whether the browser is working online                                                                                                                                                                             |
| platform                             | window.navigator        | Name of the operating system platform                                                                                                                                                                                     |
| product                              | window.navigator        | String containing information about the browser engine                                                                                                                                                                    |
| productSub                           | window.navigator        | String containing the development build number of the browser engine                                                                                                                                                      |
| userAgent                            | window.navigator        | String representing the user agent header                                                                                                                                                                                 |
| vendor                               | window.navigator        | String specifying the name of the browser vendor                                                                                                                                                                          |
| vendorSub                            | window.navigator        | String specifying the name of the browser sub-vendor                                                                                                                                                                      |
| **Category: payload.screen**         |                         |                                                                                                                                                                                                                           |
| colorDepth                           | window.screen           | Number of bits used to represent the color of a single pixel on the screen, or in the buffer when off-screen buffering is enabled                                                                                         |
| pixelDepth                           | window.screen           | Screen pixel depth bit count                                                                                                                                                                                              |
| height                               | window.screen           | Vertical resolution of the screen, in pixels                                                                                                                                                                              |
| width                                | window.screen           | Horizontal resolution of the screen, in pixels                                                                                                                                                                            |
| availHeight                          | window.screen           | Returns the height of the working area of the system’s screen, excluding the Windows taskbar                                                                                                                              |
| availWidth                           | window.screen           | Returns the width of the working area of the system’s screen, excluding the Windows taskbar                                                                                                                               |
| **Category: payload.window**         |                         |                                                                                                                                                                                                                           |
| outerHeight                          | window.outerHeight      | Returns the height of the outside of the browser window                                                                                                                                                                   |
| outerWidth                           | window.outerWidth       | Returns the width of the outside of the browser window                                                                                                                                                                    |
| innerHeight                          | window.innerHeight      | Returns the height of the content area of the browser window including, if rendered, the horizontal scrollbar                                                                                                             |
| innerWidth                           | window.innerWidth       | Returns the width of the content area of the browser window including, if rendered, the vertical scrollbar                                                                                                                |
| devicePixelRatio                     | window.devicePixelRatio | Returns the ratio between physical pixels and device independent pixels of the existing display                                                                                                                           |
| **Category: payload.flashVersion**   |                         |                                                                                                                                                                                                                           |
| major                                | navigator.plugin        | Major version number of the Flash plugin                                                                                                                                                                                  |
| minor                                | navigator.plugin        | Minor version number of the Flash plugin                                                                                                                                                                                  |
| release                              | navigator.plugin        | Release version of the Flash plugin                                                                                                                                                                                       |
| **Category: payload.pt1**            |                         |                                                                                                                                                                                                                           |
| cd1                                  | performance.now()       | Time taken to collect data for the first post (P1)                                                                                                                                                                        |
| pp1                                  | performance.now()       | Time taken from FraudNet start until pre post (P1)                                                                                                                                                                        |
| i                                    | performance.now()       | Time taken for FraudNet to load iFrame (P1)                                                                                                                                                                               |
| ph1                                  | (generated)             | Checksum generated value                                                                                                                                                                                                  |
| sf                                   | (generated)             | Four digit spoof-flag. Checks user agent, global properties, outer width/height, Selenium                                                                                                                                 |
| tb                                   | (generated)             | Sets thetrueBrowserproperty. Corresponds to an enum of the browser: Chrome, Safari, Firefox, IE                                                                                                                           |
| **Category: payload.asynchk**        |                         |                                                                                                                                                                                                                           |
| ph2                                  | (generated)             | Checksum generated based on properties within the payload                                                                                                                                                                 |
| o                                    | (generated)             | Order based on which the checksum string is generated. Last digit being random generated number between 1 - 5                                                                                                             |
| **Category: payload.connectionData** |                         |                                                                                                                                                                                                                           |
| effectiveType                        | (generated)             | Effective connection type                                                                                                                                                                                                 |
| downlink                             | FN Internal             | Effective bandwidth estimate in mbps                                                                                                                                                                                      |
| type                                 | FN Internal             | Connection type                                                                                                                                                                                                           |
| downlinkMax                          | FN Internal             | Upper bound on the downlink speed of the first network hop                                                                                                                                                                |
| rtt                                  | FN Internal             | round-trip time estimate in ms                                                                                                                                                                                            |

## Payload P2 (POST 2)

| Field Name                            | Source                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| appId                                 | Client-generated                          | Source ID of the FraudNet application                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| correlationId                         | Client-generated                          | Client-randomly-generated sequence passed to FraudNet                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| fsoError (deprecated)                 | (generated)                               | Returnstrueif Flash fails to load.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| fsold (deprecated)                    | (generated)                               | PayPal FSO. Only present if the user has logged in previously to paypal.com                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Category: payload.data**            |                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| fonts (deprecated)                    | Flash -enumerateFonts()                   | The fonts in a comma-delimited list sorted in ascending order                                                                                                                                                                                                                                                                                                                                                                                                                                |
| dom                                   | (generated)                               | Returns a string of the DOM tree HTML elements                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Category: payload.data.plugins**    |                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| n                                     | navigator.plugins[x]                      | Returns the name of the plugin created by the application creator                                                                                                                                                                                                                                                                                                                                                                                                                            |
| v                                     | navigator.plugins[x]                      | Returns the version of the plugin. This does not populate for the Chrome or Safari browsers                                                                                                                                                                                                                                                                                                                                                                                                  |
| fn                                    | navigator.plugins[x]                      | Returns the name of the current plugin, including the extension                                                                                                                                                                                                                                                                                                                                                                                                                              |
| d                                     | window.navigator                          | Returns the description supplied by the plugin creator                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| t                                     | (generated)                               | Returns the name of the MIME type associated to the plugin                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| s                                     | (generated)                               | Returns a string value that contains a comma-separated list of possible file extensions for the current MIME type                                                                                                                                                                                                                                                                                                                                                                            |
| **Category : payload.data.vm**        |                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| cores                                 | navigator.hardwareConcurrency             | Number of logical processors available to run threads on the user’s device                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Category: payload.data.vm.gpu**     |                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| vendor                                | WebGL                                     | Vendor string of the graphics driver                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| renderer                              | WebGL                                     | Renderer string of the graphics driver                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Category: payload.data.vm.jsMem**   |                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| usedJSHeapSize                        | window.performance.memory                 | Amount of memory in bytes currently being used. Chrome only. Based on the entire Chrome process.                                                                                                                                                                                                                                                                                                                                                                                             |
| totalJSHeapSize                       | window.performance.memory                 | Amount of memory in bytes that the JS heap has allocated, including free space. Chrome only. Based on the entire Chrome process.                                                                                                                                                                                                                                                                                                                                                             |
| jsHeapSizeLimit                       | window.performance.memory                 | Amount of memory in bytes to which the JS heap is limited. Chrome only. Based on the entire Chrome process.                                                                                                                                                                                                                                                                                                                                                                                  |
| **Category: payload.data.vm.perfNav** |                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| navigationStart                       | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the prompt to unload terminates on the previous document in the same browsing context. If there is no previous document, this value is the same asPerformanceTiming.fetchStart.                                                                                                                                                                                                               |
| unloadEventStart                      | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that theunloadevent has been thrown. This indicates the time at which the previous document in the window began to unload. If there is no previous document, or if the previous document or one of the needed redirects is not of the same origin, the value returned is0.                                                                                                                         |
| unloadEventEnd                        | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the unload event handler finishes. If there is no previous document, or if the previous document, or one of the needed redirects, is not of the same origin, the value returned is0.                                                                                                                                                                                                          |
| redirectStart                         | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the first HTTP redirect starts. If there is no redirect, or if one of the redirects is not of the same origin, the value returned is0.                                                                                                                                                                                                                                                        |
| redirectEnd                           | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the last HTTP redirect is completed. This is when the last byte of the HTTP response has been received. If there is no redirect, or if one of the redirects is not of the same origin, the value returned is0.                                                                                                                                                                                |
| fetchStart                            | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the browser is ready to fetch the document using an HTTP request. This moment is before the check to any application cache.                                                                                                                                                                                                                                                                   |
| domainLookupStart                     | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the domain lookup starts. If a persistent connection is used, or the information is stored in a cache or a local resource, the value will be the same asPerformanceTiming.fetchStart.                                                                                                                                                                                                         |
| domainLookupEnd                       | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the domain lookup is finished. If a persistent connection is used, or the information is stored in a cache or a local resource, the value will be the same asPerformanceTiming.fetchStart.                                                                                                                                                                                                    |
| connectStart                          | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the request to open a connection is sent to the network. If the transport layer reports an error, and the connection establishment is started again, the last connection establishment start time is given. If a persistent connection is used, the value is the same asPerformanceTiming.fetchStart.                                                                                         |
| connectEnd                            | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the connection is opened network. If the transport layer reports an error, and the connection establishment is started again, the last connection establishment end time is given. If a persistent connection is used, the value is the same asPerformanceTiming.fetchStart. A connection is considered as opened when all secure connection handshake or SOCKS authentication is terminated. |
| secureConnectionStart                 | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the secure connection handshake starts. If no such connection is requested, it returns0.                                                                                                                                                                                                                                                                                                      |
| requestStart                          | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the browser sent the request to obtain the document from the server or from a cache. If the transport layer fails after the start of the request, and the connection is reopened, this property is set to the time corresponding to the new request.                                                                                                                                          |
| responseStart                         | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the browser received the first byte of the response from the server, from a cache, or from a local resource.                                                                                                                                                                                                                                                                                  |
| responseEnd                           | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the browser received the last byte of the response or that the connection is closed (if this happens first) from the server, from the cache, or from a local resource.                                                                                                                                                                                                                        |
| domLoading                            | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the parser started its work. That is when itsDocument.readyStatechanges to loading, and the corresponding readystate change event is thrown.                                                                                                                                                                                                                                                  |
| domInteractive                        | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the parser finished its work on the main document. That is when itsDocument.readyStatechanges to interactive, and the corresponding readystate change event is thrown.                                                                                                                                                                                                                        |
| domContentLoadedEventStart            | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that is just before the parser sent theDOMContentLoadedevent. That is just after all the scripts that must be executed immediately after parsing has been executed.                                                                                                                                                                                                                                |
| domContentLoadedEventEnd              | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, just after all the scripts that must be executed as soon as possible (in order or not) have been executed.                                                                                                                                                                                                                                                                                         |
| domComplete                           | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the parser finished its work on the main document. That is when itsDocument.readyStatechanges to complete, and the corresponding readystate change event is thrown.                                                                                                                                                                                                                           |
| loadEventStart                        | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the load event was sent for the current document. If this event has not yet been sent, it returns0.                                                                                                                                                                                                                                                                                           |
| loadEventEnd                          | window.performance.timing                 | An unsigned long long that represents the duration in milliseconds, since the UNIX epoch, that the load event handler terminated. That is when the load event is completed. If this event has not yet been sent or is not yet completed, it returns0.                                                                                                                                                                                                                                        |
| **Category: payload.data.vm.timing**  |                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| cores                                 | (internal timing)                         | Time taken to get the cores data                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| gpu                                   | (internal timing)                         | Time taken to get the GPU data                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| jsMem                                 | (internal timing)                         | Time taken to get the JS Memory data                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| perfNav                               | (internal timing)                         | Time taken to get the performance navigation timing data                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| total                                 | (internal timing)                         | Total time to get the VM attributes                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Category: payload.sc**              |                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| sc-lst (deprecated)                   | (generated)                               | Supercookie using browser’s local storage                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| sc-flash                              | (generated)                               | Supercookie using the Flash plugin’s Local Storage Object                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| httpCookie                            | (generated)                               | Indicates whether to set the HTTP supercookie. Controlled by the client.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Category: payload.pt2**             | Collects the FraudNet performance timings |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| flash (deprecated)                    | performance.now()                         | Returns the time taken to load the Flash (.swf)                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| cp                                    | performance.now()                         | Returns the time taken to collect the plugins                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| cd                                    | performance.now()                         | Returns the time taken to collect the data for the second post (p2)                                                                                                                                                                                                                                                                                                                                                                                                                          |
| cd2                                   | performance.now()                         | Returns the time taken to collect the data for the second post (p2)                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Payload P3 and w

| Field Name       | Source      | Description                                                                                                                                                                                                                                             |
| ---------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Category: p3** |             |                                                                                                                                                                                                                                                         |
| ipV6             | (generated) | The ipV6 address captured at c6.paypal.com, from Akamai.                                                                                                                                                                                                |
| rDT              | (generated) | The mouse movement on the page is captured. Refer to the mouse movement parametermmunder[Configuration Parameters](/limited-release/fraudnet/integrate/add-parameter-block/#configuration-parameters).                                                  |
| **Category: w**  |             |                                                                                                                                                                                                                                                         |
| ts1              | (generated) | The typing speed of the first field, without capturing the actual keys that are being pressed. Refer to the typing speed parametertsunder[Configuration Parameters](/limited-release/fraudnet/integrate/add-parameter-block/#configuration-parameters). |
| ts2              | (generated) | The typing speed of the second field, without capturing the actual keys that are being pressed. Refer to the typing speed parametertsunder Configuration Parameters.                                                                                    |

## Sample P1 data

{
"appId": "test",
"correlationId": "041f755b3eba437e8922b9228a62f85a",
"payload": {
"navigator": {
"appName": "Netscape",
"appVersion": "5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
"cookieEnabled": true,
"language": "en-US",
"onLine": true,
"platform": "MacIntel",
"product": "Gecko",
"productSub": "20030107",
"userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
"vendor": "Google Inc.",
"vendorSub": ""
},
"screen": {
"colorDepth": 24,
"pixelDepth": 24,
"height": 1440,
"width": 2560,
"availHeight": 1373,
"availWidth": 2560
},
"window": {
"outerHeight": 1291,
"outerWidth": 1133,
"innerHeight": 0,
"innerWidth": 0,
"devicePixelRatio": 1
},
"referer": "",
"URL": "https://www.stage2mb044.stage.paypal.com/FDRegression/fn2/new.html?f=041f755b3eba437e8922b9228a62f85a&amp;s=test",
"rvr": "20180123",
"activeXDefined": false,
"flashVersion": {
"major": 0,
"minor": 0,
"release": 0
},
"tz": -28800000,
"tzName": "America/Los_Angeles",
"dst": true,
"time": 1517263821249,
"pt1": {
"i": "131.00",
"pp1": "168.00",
"cd1": "3.00",
"ph1": "11784.00",
"sf": "0000",
"tb": 1
},
"connectionData": {
"effectiveType": "4g",
"rtt": "50",
"downlink": "8.75"
},
"asynchk": {
"ph2": "b2a57fe0702a790eb44e702dc0aaee29badec4e5f2d2e1f99de34a2380b7c658",
"o": [
"ua",
"colorDepth",
"width",
"tz",
"time",
"appId",
"correlationId",
"1"
]
}
}
}## Sample P2 data
{
"appId": "test",
"correlationId": "041f755b3eba437e8922b9228a62f85a",
"fsoError": true,
"fsoId": null,
"payload": {
"data": {
"plugins": [
{
"mT": [
{
"t": "application/x-google-chrome-pdf",
"s": "pdf"
}
],
"n": "Chrome PDF Plugin",
"fn": "internal-pdf-viewer",
"d": "Portable Document Format"
},
{
"mT": [
{
"t": "application/pdf",
"s": "pdf"
}
],
"n": "Chrome PDF Viewer",
"fn": "mhjfbmdgcfjbbpaeojofohoefgiehjai",
"d": ""
},
{
"mT": [
{
"t": "application/x-nacl",
"s": ""
},
{
"t": "application/x-pnacl",
"s": ""
}
],
"n": "Native Client",
"fn": "internal-nacl-plugin",
"d": ""
},
{
"mT": [
{
"t": "application/x-ppapi-widevine-cdm",
"s": ""
}
],
"n": "Widevine Content Decryption Module",
"fn": "widevinecdmadapter.plugin",
"d": "Enables Widevine licenses for playback of HTML audio/video content. (version: 1.4.8.1030)"
}
],
"dom": "&lt;DIV &lt;H2 INPUT INPUT BR BR BR BUTTON BR BR BR BUTTON &gt;SCRIPT SCRIPT IFRAME IFRAME &gt;",
"vm": {
"cores": 8,
"gpu": {
"vendor": "ATI Technologies Inc.",
"renderer": "AMD Radeon Pro 460 OpenGL Engine"
},
"jsMem": {
"usedJSHeapSize": 35100000,
"totalJSHeapSize": 37300000,
"jsHeapSizeLimit": 2190000000
},
"perfNav": {
"navigationStart": 1517264089791,
"unloadEventStart": 0,
"unloadEventEnd": 0,
"redirectStart": 0,
"redirectEnd": 0,
"fetchStart": 1517264089792,
"domainLookupStart": 1517264089792,
"domainLookupEnd": 1517264089792,
"connectStart": 1517264089792,
"connectEnd": 1517264089792,
"secureConnectionStart": 0,
"requestStart": 1517264089798,
"responseStart": 1517264089837,
"responseEnd": 1517264089842,
"domLoading": 1517264089843,
"domInteractive": 1517264089939,
"domContentLoadedEventStart": 1517264089939,
"domContentLoadedEventEnd": 1517264089940,
"domComplete": 1517264089940,
"loadEventStart": 1517264089940,
"loadEventEnd": 1517264089940
},
"timing": {
"cores": "0.00",
"gpu": "16.00",
"jsMem": "0.00",
"perfNav": "0.00",
"total": "17.00"
}
}
},
"sc": {
"sc-flash": null,
"sc-lst": "TaNucHr3uGN3LHNQXMxoteKkRXW715L30h2z5T1Uey5kEKqK6shq5duQCGGXxhh9nxTe8o7Q6rPmsDkT6AyxsGlcqhQZLFrgb-kL6W",
"httpCookie": true
},
"pt2": {
"cd2": "19.00",
"cp": "0.00",
"flash": "0.00"
}
}
}
