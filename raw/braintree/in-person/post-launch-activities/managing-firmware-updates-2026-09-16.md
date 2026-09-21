<!-- Source URL: https://developer.paypal.com/braintree/in-person/post-launch-activities/managing-firmware-updates -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Managing Firmware Updates
slug: /in-person/post-launch-activities/managing-firmware-updates/
createTime: '2024-11-20T19:02:02.941Z'
updateTime: '2025-01-17T02:28:22.223Z'
---



# Managing Firmware Updates

There are primarily 2 ways to facilitate firmware updates to the Braintree card readers.


## Why are Firmware Updates Important?

As we release new functionality, improve performance, enhance user experience as well as fix bugs, these changes get pushed to the card readers through firmware updates. In order for this to work the card reader must be powered on and connected to the internet. It is always recommended to test these new versions in the sandbox environment before pushing to production. Click the link below to see our latest App Version Release Notes:

[Firmware Version Release Notes](/braintree/in-person/reference/app-version-release-notes/)
## 1) How to install an update to the Reader using the admin menu on the reader:

**NOTE**
The passcode referenced below is for Sandbox only. There is a different passcode for production which you can get from the PayPal support team at **eis-hw-support@paypal.com**

First, open the device settings screen by going to the PayPal branded screensaver and then **simultaneously press** **2** + **8** to display the settings screen. Before displaying the settings screen the device will prompt for a passcode. Enter 123456 followed by![](https://braintree.gitbook.io/~gitbook/image?url=https%3A%2F%2F1330402423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M6GgIF79CNAhEDh9YbJ%252F-MHC1oMiFmEstCOpDssG%252F-MHC3apwhk8GoiR07Wf2%252Fgreen_btn-inline.png%3Falt%3Dmedia%26token%3D4aee92dd-1302-4986-9fa7-cc208bdca843&width=300&dpr=4&quality=100&sign=51d0534a&sv=1) when prompted.

![](https://braintree.gitbook.io/~gitbook/image?url=https%3A%2F%2F1330402423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M6GgIF79CNAhEDh9YbJ%252F-MRXdQHH1cR1k-xKGq9b%252F-MRXdU9Uc11rkwD190-z%252Fgeneric-settings.png%3Falt%3Dmedia%26token%3D706775a5-0c0a-44ed-ae86-35c117ba09d0&width=768&dpr=4&quality=100&sign=22a0a03d&sv=1)Towards the bottom of the screen, you'll see the currently installed version number. If there's an update available to install, you'll see a button that says Install Update. After pressing the install button, the device will proceed to download and install the update. As part of the update the device will restart. Once the device returns to the PayPal branded screensaver it is ready for use.


## 2) How to install an update to the Reader using the GraphQL API:

GraphQL MutationGraphQL VariablesSample API Responsemutation RequestFirmwareUpdateFromInStoreReaderInput ($input: RequestFirmwareUpdateFromInStoreReaderInput!) { requestFirmwareUpdateFromInStoreReader(input: $input) { clientMutationId inStoreContext { id status reader { id name status softwareVersion } } } }{ "input": { "readerId": "your reader ID here" } }{ "data": { "requestFirmwareUpdateFromInStoreReader": { "clientMutationId": null, "inStoreContext": { "id": "aW5zdG9yZWNvbnRleHRfIkjfgiey79622VmNGZkNTQ2NTI5ZTc3NTUyMGEyNWZhNDJlI1ZFUklGT05FLTgwNS0wMTctNDU0I3VzLXdlc3QtMg", "status": "COMPLETE", "reader": { "id": "aW5zdG9yZX769ccl8jY3B3c2Y0Mmh3OWo1OWhjbiNWRVJJRk9ORS04MDUtMDE3LTQ1NA", "name": "POS Terminal #5", "status": "ONLINE", "softwareVersion": "3.2.1" } } } }, "extensions": { "requestId": "1f003122-112d-48f8-a6f5-8f2b58039016" } }[Reader Management System (RMS) - Available in Beta Only](/braintree/in-person/post-launch-activities/reader-management-system-rms-available-in-beta-only/)[Troubleshooting](post-launch-activities/troubleshooting/)