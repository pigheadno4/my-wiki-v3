<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/display-information -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Display Information
slug: /in-person/guides/display-information/
createTime: '2024-11-20T19:04:58.018Z'
updateTime: '2025-01-03T19:38:11.952Z'
---



# Display Information

This guide shows how to display information to your customers using the card reader screen.


## Getting Started

The following Graph QL API mutations can be used to display text on the reader screen for your customers. This can be used for a range of business logic from displaying cart items, showing a shipping address confirmation (Note: you can also leverage [Custom Prompts](/braintree/in-person/guides/custom-prompts/#request-confirmation-prompt) for a more automated version of this), or even a plain text welcome message.

Information Displays will not block subsequent reader interactions, meaning you can make repetitive display requests without first canceling a previous one. You can also make a requestChargeFromInStoreReader call while the reader is displaying information, and it will transition into a checkout flow.

The response of these API requests will include a contextId which can be used to cancel the information display.

**NOTE**
Information Display requests will stay on the screen for 120 seconds or until canceled or overwritten by a subsequent reader interaction.


## Request Text Display

This mutation will allow you to push plain text to the screen. This could be used for something like a shipping address confirmation, as shown in the below picture. The Braintree GraphQL API docs contain additional information about character limitations and formatting your request [Text Display](/braintree/graphql/reference/#Input--RequestPrintFromInStoreReaderInput) mutation.

**NOTE**
Up to 255 characters of text can be displayed using this mutation

**NOTE**
As of version 5.2.0 requestTextDisplay now supports the title, alignment, waitForNextRequest, displayTimeout API variable fields

![](https://braintree.gitbook.io/~gitbook/image?url=https%3A%2F%2F1330402423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M6GgIF79CNAhEDh9YbJ%252Fuploads%252FLSE8w5U5QQWAjRoXLVrp%252FTextDisplay-Static.png%3Falt%3Dmedia%26token%3D6415d81f-79e4-45ee-ac6d-13f9b6954a0c&width=768&dpr=4&quality=100&sign=877ff778&sv=1)This example image includes thetitlevariable which is supported as of version 5.2.0GraphQL MutationGraphQL VariablesSample API Responsemutation RequestTextDisplayFromInStoreReader($input: RequestTextDisplayFromInStoreReaderInput!) { requestTextDisplayFromInStoreReader(input: $input) { clientMutationId id reader { id name status } status } }{ "input": { "readerId": "your reader ID", "text": "Shipping Address:\n\n 123 Fake St.\n Newport Beach, CA \n USA" } }{ "data": { "requestTextDisplayFromInStoreReader": { "clientMutationId": null, "id": "aW5zdG9yZWNvbnRleHRfIzhjMjgxM2ZiMWUwNDRmZTRiNDFiOWVjYmVjOTExY2YxI1ZFUklGT05FLTgwMy00MTUtMTY0I3VzLWVhc3QtMg", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jaHo0YzYyeHp0OGZocjc2eSNWRVJJRk9ORS04MDMtNDE1LTE2NA", "name": "P400 Desk", "status": "ONLINE" }, "status": "PENDING" } }, "extensions": { "requestId": "57971749-2037-4421-b2ad-7c3f0a0a163a" } }
## Request Line Item Display

This mutation can be called each time the POS software adds an item to display the running cart totals to the customer.

As items are added, a scrolling container will automatically move to keep the most recently added items in view.

Adding new items to the display will require the POS to send all items in the cart and new running totals after each update.

![](https://braintree.gitbook.io/~gitbook/image?url=https%3A%2F%2F1330402423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M6GgIF79CNAhEDh9YbJ%252F-M__xltn6N67xEhHULzr%252F-M_aDit2VyeRI4OHZpFG%252FScreen%2520Shot%25202021-05-13%2520at%252010.56.40%2520AM.png%3Falt%3Dmedia%26token%3Dba878e2c-6d0a-4988-900e-45cbdfd358c0&width=768&dpr=4&quality=100&sign=f78d7c4&sv=1)**NOTE**
Up to 249 items can be displayed using this mutation.

**NOTE**
The displayItems are used for display formatting purposes only and are not passed downstream to the processors or saved in relation to the transaction. All calculations must be performed on the POS. Additional information about [character limitations and formatting your mutation](/braintree/graphql/reference/#Input--RequestItemDisplayFromInStoreReaderInput) can be found in our Braintree GraphQL API docs.

GraphQL MutationGraphQL VariablesSample API Responsemutation RequestItemDisplayFromInStoreReader($input: RequestItemDisplayFromInStoreReaderInput!) { requestItemDisplayFromInStoreReader(input: $input) { clientMutationId id reader { id name status } status } }{ "input": { "readerId": "{{BT_reader_id}}", "displayItems": [ { "kind": "CHARGE", "description": "Red shirt", "quantity": 1, "amount": "21.00" }, { "kind": "CHARGE", "description": "Khaki pants", "quantity": 2, "amount": "80.00" }, { "kind": "DISCOUNT", "description": "BOGO pants sale", "amount": "40.00" }, { "kind": "CHARGE", "description": "Blue cardigan", "quantity": 1, "amount": "22.00" }, { "kind": "CHARGE", "description": "Denim jeans", "quantity": 1, "amount": "73.00" }, { "kind": "DISCOUNT", "description": "20% off", "amount": "14.60" }, { "kind": "LINE_BREAK" }, { "kind": "TEXT", "description": "Thanks for your loyalty!" }, { "kind": "DISCOUNT", "description": "Loyalty discount", "amount": "5.00" } ], "tax": "9.89", "discountAmount": "59.60", "amount": "136.40" } }{ "data": { "requestItemDisplayFromInStoreReader": { "clientMutationId": null, "id": "aW5zdG9yZWNvbnRleHRfI2ZiNmY4MjgyMGEwODQ3NjBiNmZkNDdiNTg2MjU5NDU0I1ZFUklGT05FLTgwMy00MTUtMTY0I3VzLWVhc3QtMg", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jaHo0YzYyeHp0OGZocjc2eSNWRVJJRk9ORS04MDMtNDE1LTE2NA", "name": "P400 Desk" }, "status": "PENDING" } }, "extensions": { "requestId": "0bf49170-db13-446a-83c8-b6b6d25c8bfa" } }
## Cancel Information Display

This mutation will allow you to cancel an information display and return to the screensaver.

GraphQL MutationGraphQL VariablesSample API Responsemutation RequestCancelFromInStoreReader( $input: RequestCancelFromInStoreReaderInput! ) { requestCancelFromInStoreReader(input: $input) { id status reader { id name status } } }{ "input": { "inStoreContextId": "{{last_braintree_instore_context}}" } }{ "data": { "requestCancelFromInStoreReader": { "id": "aW5zdG9yZWNvbnRleHRfIzQ3YTJiYzc3MWMwODRjYzM4NjFlMmI1ZmE3ZGQzNmFjI1ZFUklGT05FLTgwNC03NzUtMDg1I3VzLWVhc3QtMQ", "status": "CANCELLED", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jZmFrZV9tZXJjaGFudCNWRVJJRk9ORS01NTUtNTU1LTU1NQ", "name": "POS Terminal #5", "status": "ONLINE" } } }, "extensions": { "requestId": "1c58271e-7b5d-4911-9e57-b75db5e65310" } }

[PayPal and Venmo QRC](/braintree/in-person/guides/paypal-and-venmo-qrc/)[Custom Prompts](/braintree/in-person/guides/custom-prompts/)