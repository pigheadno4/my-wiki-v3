<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/card-data-collection -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Card Data Collection
slug: /in-person/guides/card-data-collection/
createTime: '2024-11-20T19:03:11.728Z'
updateTime: '2025-01-17T02:07:31.162Z'
---



# Card Data Collection

This page discusses using the Card Data Collection feature, which allows you to collect raw card track data for Non-PCI cards that adhere to ISO-7813 format.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Card%20data%20collection:requestTextDisplay%20mutation.gif)Example flow using[requestNonPCICard mutation](/braintree/graphql/reference/#Mutation--requestNonPciCardDataFromInStoreReader)+ requestTextDisplay mutation
## Feature Overview

The Card Data Collection feature is designed to allow merchants to use Braintree card readers to read magstripe track data from non-PCI scoped cards. For example, these would include 3rd party (non-cobranded) gift cards (ex: SVS, Givex, Valuelink, etc...) and (non-cobranded) closed-loop private label cards (ex: Bread Financial/ADS, Synchrony, CitiBank, etc...) as long as they adhere to ISO 7813 format. This feature is architected to give full control of the flow and experience to the API caller (typically a POS system). Braintree does not send the collected card data to any 3rd party card issuer, it is up to the API caller to do so from the POS or another system.

**NOTE**
Braintree will never return PCI card data if a PCI-scoped card is swiped on the Braintree reader.


## Setup and Configuration

To use this feature, Braintree must have your non-PCI card BIN ranges configured on the Braintree gateway account. Please work with your Braintree Solutions Engineer or Integration Engineer to configure this before use.

**NOTE**
For sandbox testing purposes, we will require the full card numbers of your non-PCI cards used for testing or at least the first 8 digits of the test cards.


## Initiate a request to collect card data

To begin this flow, you would first use the [requestNonPCICardDataFromInStoreReader](/braintree/graphql/reference/#Mutation--requestNonPciCardDataFromInStoreReader) API mutation to initialize the reader for a card swipe. Within this request, you can control the messaging displayed on the reader swipe prompt by using the title, textAreaOne, and textAreaTwo API variable fields. This is where you would indicate the transaction type (ex: Gift Card or Private Label Credit Card, etc...) as well as the amount to be charged/redeemed and any other call to action for your customer, such "please swipe". You may also use the waitForNextRequest variable to indicate whether you want to display a processing spinner screen after the swipe. Once Braintree reads the card data, it is checked to make sure the card is not within a known PCI BIN range (if it is, an error will be returned). As long as the card is recognized as a non-PCI card and falls within the merchant account configured BIN ranges, Braintree will allow for the API caller to retrieve the entire track 1 and track 2 card data.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Card%20data%20collection_Initiate%20a%20request%20to%20collect%20card%20data.png)
#### Example card data collection request:

GraphQL MutationGraphQL VariablesSample API Responsemutation RequestNonPciCardDataFromInStoreReader($input: RequestNonPciCardDataFromInStoreReaderInput!) { requestNonPciCardDataFromInStoreReader(input: $input) { clientMutationId id } }{ "input": { "readerId": "your reader ID", "title": "Please swipe your card", "textAreaOne": "$20.00", "textAreaTwo": "Extra discount", "waitForNextRequest": true, "displayTimeout": 15 } }{}After the reader is initialized, your application must wait for the customer to interact with it (i.e. swipe a card) and card data to be read. Your application should use [the node query](/braintree/graphql/reference/#Query--node) to poll on a 2-second interval between responses for the current status of the payment using the Context.id received at request initialization and monitor the InStoreContext.status field as the request goes through the lifecycle. The result of this polling will be to retrieve the track 1 and track 2 data read from the swiped card.


#### Example card data collection query:

GraphQL QueryGraphQL VariablesSample API Responsequery ID($contextId: ID!) { node(id: $contextId) { ... on RequestNonPciCardDataInStoreContext { __typename id status cardData { ... on NonPciFinancialCardMagneticStripeData { track1 track2 } } reader { id name status } } } }{ "contextId": "your context ID from card data collection request" }{ "data": { "node": { "__typename": "RequestNonPciCardDataInStoreContext", "id": "aW5zdG9yZWNvbnRllkMWM2NyMmM3OTBjZNzY0I1ZFUklGT05FLTgwNS05NzEtMjE3I3VzLXdlc3QtMg", "status": "COMPLETE", "cardData": { "track1": "%B4580971078292373^TESTCARD/MERCHANT ^4506101001000000000000000000000?", "track2": ";4580971041292373=45061010010000000000?" }, "reader": { "id": "aW5zdG9yZXlcl8jY3B3ch3OWo1OWJJRk9ORS04MDUtOTcxLTIxNw", "name": "Your M400", "status": "ONLINE" } } }, "extensions": { "requestId": "fbc987a2-7d66-4884-9bfe-892a7934c859" } }**NOTE**
Note that magstripe track data returned in the response may vary depending on the card formatting. Braintree returns whatever track data is retrievable from the card.


## Displaying the transaction result

Since Braintree is not actually processing the transaction, it is up to the API caller to display the transaction result for the customer. You may do this by utilizing the [requestTextDisplay](/braintree/in-person/guides/display-information/#request-text-display) API mutation using the title and text API variable fields. For example, you may choose to display a title with Approved or Thank You for Your Purchase! and a text with You have redeemed $44 from your gift card for today's purchase. This messaging is entirely customizable by the API caller according to the use case and the operation being performed, this includes any error messaging that you want to display to your customer.

**NOTE**
When showing the transaction result, it is suggested to avoid displaying any customer PII data.


## Tips when Integrating Card Data Collection


- [Card Data Collection](/braintree/in-person/guides/card-data-collection/#card-data-collection) is NOT supported for [offline processing](/braintree/in-person/guides/offline-transactions/)


- The cards being swiped must be ISO 7813 formatted


- The cards being swiped must not conflict with a known PCI-scoped BIN range


- You'll need to have your Braintree account configured with your defined card BIN ranges


- When using [Card Data Collection](/braintree/in-person/guides/card-data-collection/#card-data-collection), the response data tied to the context ID is retrievable for about 10 minutes


- When using [Card Data Collection](/braintree/in-person/guides/card-data-collection/#card-data-collection), the response data tied to the context ID will be deleted after the first successful retrieval




## Data Processing

Please refer to [our page on PayPal Braintree Sub-processors](/braintree/in-person/reference/paypal-braintree-sub-processors/) to understand what other entities may come in contact with data collected through our Card Data Collection feature

[Custom Prompts](/braintree/in-person/guides/custom-prompts/)[GraphQL Error Handling](/braintree/in-person/guides/graphql-error-handling/)