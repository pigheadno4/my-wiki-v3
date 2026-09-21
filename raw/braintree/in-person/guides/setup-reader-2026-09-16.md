<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/setup-reader -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Setup Reader
slug: /in-person/guides/setup-reader/
createTime: '2024-11-20T19:02:48.949Z'
updateTime: '2025-01-22T08:27:25.094Z'
---



# Setup Reader

Here are the steps to connect your Dev Kit reader to the internet and to pair it with your Braintree Sandbox Account.


## What you will need to get started


- [Braintree Dev Kit P400 including:](/braintree/in-person/get-started-1/get-started/)


- Verifone P400 Reader


- Verifone P400 Power Cable


- Verifone P400 Multi-Port Cable


- Verifone RS232 Cables (for debugging only)


- 3 Braintree Test Cards




- [Braintree Sandbox Account](https://www.braintreepayments.com/sandbox) configured for [Dev Kit testing](/braintree/in-person/get-started-1/configure-sandbox/)


- [Braintree GraphQL Docs](/braintree/graphql/)


- WiFi or Ethernet Network


- To get up and running quickly, we recommend using the [Postman API Client](https://www.postman.com/product/api-client/) with our **Braintree GraphQL - In-Person Postman Collection**. You can find the In-Person Collection and setup instructions [here](/braintree/in-person/get-started-1/configure-sandbox/#link-id3.makeabraintreegraphqlrequest).


- A cup of coffee and a comfortable desk



![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Setup%20Reader:Dev%20Kit%20.png)
## Step 1: Install the Hardware

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Setup%20Reader:Install%20the%20Hardware.png)**Assembly**


- Step 1 - Remove the Back Cover


- Step 2 - Connect the Multi-Port Cable as shown


- Step 3 - Install the Back Cover


- Step 4 - Connect the Power Adaptor


- Step 5 - Wait until the device starts up


- Step 6 (Optional) - Connect an Ethernet cable



After the power is connected, the reader will power up automatically and cycle through a few screens during startup. Wait until the black and white "Start Setup" screen shows up.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Setup%20Reader_Start%20Setup.png)When you are ready, tap the "Start Setup" button.


## Step 2: Network Configuration Requirements

For the card readers to function properly in an online setting, they need to have a connection to the internet. This means that if you have a restrictive firewall on your LAN, you will need to ensure that there are rules in place to allow for both incoming and outgoing communication traffic to and from the reader. If needed, you can whitelist the domain endpoints that communicate with the reader.


### Braintree Domains to Whitelist

Following is a list of domains to whitelist on your onsite location network. This ensures your firewall does not interfere with incoming or outgoing communication to and from the card reader. There may be additional domains added in future releases. If this does happen, we will update this documentation.

| **Domain to Whitelist** | **Environment** |
| payments.sandbox.braintree-api.com | Sandbox |
| reader.sandbox.braintree-api.com | Sandbox |
| reader-websocket.sandbox.braintree-api.com | Sandbox |
| payments.braintree-api.com | Production |
| reader.braintree-api.com | Production |
| reader-websocket.braintree-api.com | Production |
| pool.ntp.org | Both |
| time.google.com | Both |
| time.cloudflare.com | Both |
| s3.us-east-1.amazonaws.com | Both |


### Connect to the Internet

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Setup%20Reader:Select%20a%20Network.png)
#### Select a Network

The reader will automatically scan for available WiFi networks and display a list when ready to connect. If an Ethernet cable is plugged into the device via the Multi-Port Cable, an option to connect over Ethernet will also be available on-screen. Tap the touchscreen to select a Network.

You may press the **yellow back button**![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/BackYellowButton.png) at any time during the WiFi setup to return to the previous screen.


#### Enter WiFi Password

If connecting over WiFi, use the keypad to enter your WiFi password when prompted. Use the key map below as a guide to enter characters with the numeric keypad, then press "Connect to WiFi" to continue.


#### Key Map

Repeatedly pressing a number on the keypad will cycle through the available character options. Following is a table view of all available characters.

| **KEYPAD NUMBER** | **CHARACTERS** |
| 0 | SP 0 |
| 1 | q z. Q Z 1 |
| 2 | a b c A B C 2 |
| 3 | d e f D E F 3 |
| 4 | g h i G H I 4 |
| 5 | j k l J K L 5 |
| 6 | m n o M N O 6 |
| 7 | p r s P R S 7 |
| 8 | t u v T U V 8 |
| 9 | w x y W X Y 9 |
| * | ! " $ % & ' ( ) * +, - / : ; &lt; = &gt;? @ [ \ ] ^ _ ` { | } ~ |
| # | # |


#### IP Address Assignment

While connecting to the network, you may assign IP address automatically using DHCP or manually using Static IP. Static IP addresses allow network devices to always retain the same IP address. A network administrator must keep track of each statically assigned device to avoid using that IP address again. If you do not intend to use the Braintree terminal in the offline mode, you should use DHCP.


#### Configuring Static IP

On the previous screen, if you choose Static IP, you will need to provide the following information -


- IP Address


- Subnet Mask


- Default Gateway


- DNS Server 1


- DNS Server 2 (Optional)



Each Field must be an IPv4 IP address. Once you have populated above fields, hit the OK button to finish configuring the Static IP Address.

If the device is unable to connect to the internet, a screen will show, giving options to restart the device or reset the network configuration. Resetting the network configuration will cause the device to enter the network pairing flow again upon reboot, allowing you to update connection settings if they were entered incorrectly.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Setup%20Reader:Switching%20Networks.png)
#### Switching Networks

​If you need to switch networks, you can always access the Device Settings screen after setup. To access this screen, **simultaneously press**  2 + 8  **while on the PayPal-branded screensaver.**

**NOTE**
The admin password for a test device is 123456. This will be different for production devices.

**Viewing Network Status**

Network status is displayed at the top of the screen, along with a battery indicator if applicable. Following are four possible status bars you may see:

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Setup%20Reader_battery%20indicator.png)Four possible status bars for the e285. For the P400, there will be no battery indicator.

The first status bar shows a reader that is not connected and at a battery level of 100%. The second status bar shows a reader connected to Ethernet and at a battery level of 100%. The third status bar shows a reader connected to Ethernet and at a battery level of 5%. The battery level is critically low, so it is red. The fourth status bar shows a reader is connected to WiFi, at a battery level of 23%, and charging.



On P400 and M400 devices, there are no rechargeable batteries, so status bars will have no battery indicator but will have a network connectivity indicator.


## Step 3: Check for Reader Update

Please make sure your reader is on the latest available version. See [available versions](/braintree/in-person/reference/app-version-release-notes/).

First, open the device settings screen by going to the PayPal branded screensaver and then **simultaneously press**  **2** + **8** to display the settings screen.

**NOTE**
The admin password for a test device is 123456. This will be different for production devices.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Setup%20Reader:Reader%20setting.png)

In the middle of the screen, you'll see the available-to-update version number instead of the New version placeholder.

Towards the bottom of the screen, you'll see the installed version number instead of the Installed Software Version placeholder. If you're already on the latest version, you're ready to move on to the next step. If there's an update available to install, you'll see a button that says Install Update. Press that button and follow the on-screen prompts to update your reader.


## Step 4: Connect to Sandbox

To get up and running quickly, we recommend using the [Postman API Client](https://www.postman.com/product/api-client/) with our **Braintree GraphQL - In-Person Postman Collection**. You can find the In-Person Collection and setup instructions [here](/braintree/in-person/get-started-1/configure-sandbox/#link-id3.makeabraintreegraphqlrequest). If you don't plan to integrate these APIs for reader management you may also use the [Reader Management System (RMS)](/braintree/in-person/post-launch-activities/reader-management-system-rms-available-in-beta-only/) tool in the Braintree Control Panel.

**NOTE**
 **Please Note:** A Dev Kit Reader may only be **paired to one Sandbox Account.**

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Setup%20reader:Connect%20to%20Sandbox.png)For advanced setups, please contact a solutions engineer to enable additional features like " [multi-merchant account](/braintree/articles/control-panel/important-gateway-credentials/#merchant-account-id) " if needed.


### Create Location ID

Before pairing a reader, you must have at least one location defined. A location can have any number of readers attached, and you can reassign readers to new locations at any time.

Do not lose your location.id. We suggest saving it in a safe place immediately.

GraphQL MutationGraphQL VariablesSample API Responsemutation CreateInStoreLocation($input: CreateInStoreLocationInput!) { createInStoreLocation(input: $input) { location { id name internalName address { streetAddress region locality postalCode countryCode } geoCoordinates { latitude longitude } } } }{ "input": { "location": { "name": "Sample Brand", "internalName": "0036", "address": { "streetAddress": "18 West Side Avenue", "extendedAddress": "Unit b", "locality": "Beverly Hills", "region": "California", "postalCode": "90210", "countryCode": "USA" }, "geoCoordinates": { "latitude": 34.0736, "longitude" : 118.4004 } , "enableQRCodePayments": false } } }{ "data": { "createInStoreLocation": { "location": { "id": "aW5zdG9yZWxvY2F0aW9uXyM2NzdhNDM2Mjc2OTg0ZDBjODM3ZTZlN2MwYTk3YzEzYg", "name": "Sample Brand", "internalName": "0036", "address": { "streetAddress": "18 West Side Avenue", "region": "California", "locality": "Beverly Hills", "postalCode": "90210", "countryCode": "USA" }, "geoCoordinates": { "latitude": 34.0736, "longitude": 118.4004 } } } }, "extensions": { "requestId": "db65b61c-7a85-4f0d-88c9-554c4978f9e2" } }**NOTE**
If you are planning on enabling PayPal and Venmo payment methods via [QR code](/braintree/in-person/guides/paypal-and-venmo-qrc/), then you should not use more than 64 characters in the internalName field when creating your location ID


### Pair Reader to a Location ID

Once you are connected to WiFi, you will see the "Pair your Reader" screen. The reader is now in pairing mode and checking for a response from the Braintree Platform.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Setup%20Reader:Pair%20Reader%20screen.gif)To use a reader with your account, you need to pair the device to your Braintree Sandbox Account and assign the reader to a location.id. During this initial setup, your reader will pair with your Sandbox Merchant Account via the location.id you created. The code example below will require a userCode, which is the 6 characters displayed at the bottom of the reader screen.


**NOTE**
The userCode displayed at the bottom of the reader screen will refresh every 5 minutes until the reader is paired.


#### We suggest using Postman and the GraphQL code example below to pair your reader

[Try Postman](/braintree/in-person/get-started-1/configure-sandbox/#link-id3.makeabraintreegraphqlrequest)GraphQL MutationGraphQL VariablesSample API Responsemutation PairInStoreReader($input: PairInStoreReaderInput!) { pairInStoreReader(input: $input) { clientMutationId reader { id name vendor { ... on VerifoneVendor { model osVersion } } location { id name address { streetAddress extendedAddress locality region postalCode countryCode } } status } } }{ "input": { "userCode": "enter user code shown on reader display", "reader": { "locationId": "input your location Id here", "name": "input your reader name here" } } }{ "data": { "pairInStoreReader": { "clientMutationId": "xyz123", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jZmFrZV9tZXJjaGFudCNWRVJJRk9ORS01NTUtNTU1LTU1NQ", "name": "POS Terminal #5", "vendor": null, "location": { "id": "aW5zdG9yZWxvY2F0aW9uXyM2NzdhNDM2Mjc2OTg0ZDBjODM3ZTZlN2MwYTk3YzEzYg", "name": "Sample Brand", "address": { "streetAddress": "18 West Side Avenue", "extendedAddress": "Unit b", "locality": "Beverly Hills", "region": "California", "postalCode": "90210", "countryCode": "USA" } }, "status": "OFFLINE" } } }, "extensions": { "requestId": "815ac9e8-85f7-4d1a-b7ae-d3d69436f61e" } }
### Update an Existing Location (Optional)

If you would like to update an existing location, you can use the below GraphQL mutation. Remember that you can only update an existing location if you have already [created an in-store location](/braintree/in-person/guides/setup-reader/#link-createlocationid). See our documentation for more details on available [API inputs for updating an existing location](/braintree/graphql/reference/#Input--UpdateInStoreLocationInput).

GraphQL MutationGraphQL VariablesSample API Responsemutation UpdateInStoreLocation($input: UpdateInStoreLocationInput!) { updateInStoreLocation(input: $input) { clientMutationId location { id internalName geoCoordinates { latitude longitude } qrCodePaymentsEnabled payerId name address { streetAddress extendedAddress locality region postalCode countryCode } } } }{ "input": { "clientMutationId": "999", "locationId": "your location ID", "location": { "address": { "streetAddress": "18 West Side Avenue", "extendedAddress": "Unit b", "locality": "Beverly Hills", "region": "California", "postalCode": "90210", "countryCode": "USA" }, "payerId": "your payer ID", "enableQRCodePayments": true } } }{ "data": { "updateInStoreLocation": { "clientMutationId": "999", "location": { "id": "your location ID", "internalName": "02045", "geoCoordinates": { "latitude": 34.0736, "longitude": 118.4004 }, "qrCodePaymentsEnabled": true, "payerId": "your payer ID", "name": "Test Retail Location", "address": { "streetAddress": "18 West Side Avenue", "extendedAddress": "Unit b", "locality": "Beverly Hills", "region": "California", "postalCode": "90210", "countryCode": "US" } }
### Update Reader Location Pairing (optional)

If you would like to move a card reader pairing from one existing location to another, you can use the GraphQL API [UpdateInStoreReader](/braintree/graphql/reference/#Mutation--updateInStoreReader) mutation. See the example Below.

GraphQL MutationGraphQL VariablesSample API Responsemutation UpdateInStoreReader($input: UpdateInStoreReaderInput!) { updateInStoreReader(input: $input) { clientMutationId reader { id name vendor { ... on VerifoneVendor { model osVersion } } location { id name address { streetAddress extendedAddress locality region postalCode countryCode } } status } } }{ "input": { "readerId": "your reader ID", "locationId": "your location ID - where you would like to re-pair your reader to", "name": "your reader name" } }{ "data": { "updateInStoreReader": { "clientMutationId": null, "reader": { "id": "aW5zdG9yZX3OWo19ORS00MDEtOTIzLTYwNg", "name": "your reader name", "vendor": { "model": "E285", "osVersion": "ADK 4.6.4" }, "location": { "id": "aW5zdMy1iMmFjY5YS1hNzc2ZDRjMzc1NjE", "name": "Test location Update", "address": { "streetAddress": "18 West Side Avenue", "extendedAddress": "Unit b", "locality": "Beverly Hills", "region": "California", "postalCode": "90210", "countryCode": "US" } }, "status": "ONLINE" } } }, "extensions": { "requestId": "f7b55e2f-eb6f-4afc-bdf0-1ab9fda" } }
## Success!

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Setup%20reader:successfully%20paired.png)**NOTE**
Once you have successfully paired your reader, it's best practice to save the unique generated reader.id from the response in your database, as it will be required to be used in future reader initialization API requests.

Your reader will automatically redirect to a PayPal-branded splash screen on success. Your reader is now connected to your Braintree Sandbox Account!

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Setup%20Reader_connected%20to%20sandbox.png)Your Reader is setup and connected to sandbox.
## All set!

Continue reading through our integration guides section to see how to [make a transaction](/braintree/in-person/guides/making-a-transaction/) on your reader.


## Failed to Configure?

Most issues with setup can be quickly remedied by restarting the app. Please review our [troubleshooting](/braintree/in-person/post-launch-activities/troubleshooting/) section for additional help.

[API Authentication](/braintree/in-person/guides/api-authentication/)[Initiate a Sale or Refund](/braintree/in-person/guides/making-a-transaction/)