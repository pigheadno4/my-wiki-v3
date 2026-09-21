<!-- Source URL: https://developer.paypal.com/braintree/in-person/about/technical-overview -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Technical Overview
slug: /in-person/about/technical-overview/
createTime: '2024-11-20T19:04:18.049Z'
updateTime: '2025-01-20T02:34:37.501Z'
---



# Technical Overview

This section is designed to give you a high-level overview of integrating with the Braintree In-Person product and its architecture.


## Intro to Braintree GraphQL

If you're new to GraphQL, you should familiarize yourself with some basic GraphQL concepts before digging into our In-Person documentation. For a quick introduction, see the [Basic Concepts](/braintree/graphql/guides/#basic-concepts) section. To get more in-depth, there are many great resources to learn GraphQL — to start with, we recommend [Introduction to GraphQL](https://graphql.org/learn/) and [How to GraphQL](https://www.howtographql.com/).

The In-Person capabilities are simply an additional set of GraphQL Objects and Mutations. All resources in the [detailed Braintree GraphQL guides](/braintree/graphql/guides/) will be applicable and can be leveraged during your integration with Braintree In-Person.


## Understanding the In-Person GraphQL Object Relationships

The API caller will act on behalf of a [Merchant](/braintree/graphql/reference/#Object--Merchant) and can create as many [InStoreLocations](/braintree/graphql/reference/#Object--InStoreLocation) as required using the [createInStoreLocation](/braintree/graphql/reference/#Mutation--createInStoreLocation) mutation. The InStoreLocation object is designed to represent a physical location that will contain card readers. You will receive a dynamically generated InStoreLocation.id to store for future changes to this location.

[InStoreReaders](/braintree/graphql/reference/#Object--InStoreReader) are then paired to a specific [InStoreLocation](/braintree/graphql/reference/#Object--InStoreLocation) using the [pairInStoreReader](/braintree/graphql/reference/#Mutation--pairInStoreReader) mutation. Multiple readers can be paired to a single [InStoreLocation](/braintree/graphql/reference/#Object--InStoreLocation). You will receive a dynamically generated InStoreReader.id to store for initializing this reader.

[InStoreContexts](/braintree/graphql/reference/#Object--InStoreContext) are created using the **requestChargeFromInStoreReader** mutation by providing the total checkout amount and the InStoreReader.id you want to initialize the transaction. The response will return a unique InStoreContext.id to reference while your application waits for the customer to interact with the reader.

Your application will check on an interval the status of the [InStoreContext](/braintree/graphql/reference/#Object--InStoreContext), and once the customer is finished interacting with the device, you will receive a [Transaction](/braintree/graphql/reference/#Object--Transaction) object in the response.


## What Card Reader models are supported?

Braintree has partnered with Verifone to offer best-in-class payment terminal (card reader) hardware. This means that although Verifone might manufacture the hardware, most of the functionality and software running on the device is actually developed by Braintree. We currently support the below-listed hardware models. We will continue to update this documentation as we expand our hardware offering. For more information on how our hardware ordering and logistics process works, please consult your Solutions Engineer or Integration Engineer.

**NOTE**
 [Sandbox card readers](/braintree/in-person/get-started-1/get-started/) and [Production card readers](/braintree/in-person/guides/ready-for-launch/#ordering-production-card-readers) have the same behavior. However, they are not interchangeable. Only special test cards work on the sandbox card readers. Test cards do not work on production card readers. More info on the hardware specs is available [here](/braintree/in-person/reference/faq/).

| **Card Reader** | **Description** | **Availability** |
| [Verifone P400](/braintree/in-person/hardware/verifone-p400/) | The P400 card reader is a fixed lane device that is tethered to a power source. However, the device offers flexibility for network connection methods including both Ethernet and WiFi capabilities. | Available |
| [Verifone E285](/braintree/in-person/hardware/verifone-e285/) | The E285 card reader is a mobile device that does not require tethering to a power source. This device relies on WiFi network connectivity. | Available |
| [Verifone M400](/braintree/in-person/hardware/verifone-m400/) | The M400 reader is a fixed lane device that is tethered to a power source. The reader offers flexibility for network connection methods including both Ethernet and WiFi. | Available |


## High-Level Functionality Summary

| **Feature Name** | **Description** | **Link to Documentation** |
| Sale | Facilitate an auth + capture in one request from your customer using the card reader | [Initiating a Sale](/braintree/in-person/guides/making-a-transaction/) |
| Authorize | Facilitate an authorization from your customer using the card reader | [Initiating an Authorization](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/) |
| Refunds | Perform either a referenced or unreferenced refund to the customer | [Perform Refunds](/braintree/in-person/guides/making-a-transaction/#refunding-your-customer) |
| Vaulting | Retrieve a payment method token for future use or vault your customer information with Braintree | [Vaulting Payment Methods](/braintree/in-person/guides/vaulting-and-customers/) |
| Line Item Display | Display sale line items on the card reader screen during scanning | [Display Line Items](/braintree/in-person/guides/display-information/) |
| Custom Prompts | Display custom text (surveys, terms & conditions, address confirmation, etc...) and collect customer input (boolean) or signature from the card reader | [Collect Customer Input](/braintree/in-person/guides/custom-prompts/) |
| Card Data Collection | Swipe non-PCI Gift Cards or PLCC cards on the reader to collect the magstripe track data | [Read Magstripe Card Data](/braintree/in-person/guides/card-data-collection/) |
| QR Code Payments | Accept Venmo and PayPal using scannable QR codes on the card reader screen | [QR Code Based Payments](/braintree/in-person/guides/paypal-and-venmo-qrc/) |
| Offline Processing | Accept payments while your internet is down | [Offline Processing](/braintree/in-person/guides/offline-transactions/) |

[Solution Architecture](/braintree/in-person/about/solution/)[Solution Coverage](/braintree/in-person/about/solution-coverage/)