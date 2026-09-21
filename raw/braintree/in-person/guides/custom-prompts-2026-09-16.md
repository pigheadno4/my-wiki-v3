<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/custom-prompts -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Custom Prompts
slug: /in-person/guides/custom-prompts/
createTime: '2024-11-20T19:03:59.743Z'
updateTime: '2025-05-19T03:17:42.550Z'
---



# Custom Prompts

This section gives an overview of the custom prompts suite of API calls within the Braintree In-Person solution.


## Custom Prompts Overview

Custom Prompts is a suite of API calls that allow you to create interactive flows on the reader outside of collecting payment. In an ever-evolving and complex world of payments, merchants strive to interact with their customers in different ways, which is why we have created custom prompts to enable and streamline these customer interactions. Some of these example use cases are Loyalty Program sign-ups, Private Label Card sign-ups, marketing opt-ins, email receipt opt-ins, and Loyal Customer Authentication with phone # or email address. The possibilities are endless with this modular and customizable feature.


- [Request Multiple Choice Prompt](/braintree/in-person/guides/custom-prompts/#request-multiple-choice-prompt)


- [Request Text Prompt](/braintree/in-person/guides/custom-prompts/#request-text-prompt)


- [Request Amount Prompt](/braintree/in-person/guides/custom-prompts/#request-amount-prompt)


- [Request Signature Prompt](/braintree/in-person/guides/custom-prompts/#request-signature-prompt)


- [Request Confirmation Prompt](/braintree/in-person/guides/custom-prompts/#request-confirmation-prompt)




## Request Multiple Choice Prompt

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Custom%20Promts_Request%20choice%20prompt.png)Example donation collection using[requestMultiChoiceSingleSelectPrompt](/braintree/graphql/reference/#Mutation--requestMultiChoiceSingleSelectPromptFromInStoreReader)The [requestMultiChoiceSingleSelectPrompt](/braintree/graphql/reference/#Mutation--requestMultiChoiceSingleSelectPromptFromInStoreReader) API call is used to display multiple buttons on the reader and allow the customer to select a single button. This can be used for common use cases such as Donations, Satisfaction Surveys, Tipping, and more. There is a maximum of 15 buttons allowed and a selection of 1 button has to occur, or alternatively the request can be cancelled. The primaryText is required in the input and the secondaryText is an optional variable. The style variable is used to determine whether a black button (PRIMARY) with white text or a white button (SECONDARY) with black text are displayed, it is also an optional input with the variables being "PRIMARY" or "SECONDARY" and the default being "PRIMARY" if style variable is not passed in the request.

**NOTE**
A PayPal/Braintree Solutions Engineer or Integration Engineer must enable this feature in both Sandbox and Production environments

**NOTE**
Request Multi Choice Single Select API mutation supported on firmware version 5.4.0

GraphQL MutationGraphQL VariablesSample API Responsemutation RequestMultiChoiceSingleSelectPromptFromInStoreReader($input: RequestMultiChoiceSingleSelectPromptFromInStoreReaderInput!) { requestMultiChoiceSingleSelectPromptFromInStoreReader(input: $input) { clientMutationId id reader { id name status location { id name address { streetAddress extendedAddress locality region postalCode countryCode } } } status } }{ "input": { "readerId": "Your reader ID", "title" : "Add a tip amount", "text" : "Please select one of the tipping options below", "alignment": "CENTER", "waitForNextRequest": "true", "displayTimeout": "1000", "choices":[{ "primaryText": "$15.00", "secondaryText": "15% of total" }, { "primaryText": "$20.00", "secondaryText": "20% of total" }, { "primaryText": "$30.00", "secondaryText": "30% of total" }, { "primaryText": "Custom Amount", "secondaryText": " Enter custom amount" }, { "primaryText": "No thanks", "style": "SECONDARY" }] } }{ "data": { "requestMultiChoiceSingleSelectPromptFromInStoreReader": { "clientMutationId": null, "id": "aW5zdG9yZWNvbnRleHRfIzIxNkMjQ1YjI5M2JlZjNjYzhlODFiZTlhI1ZFUklGT05FLTgwNS05NzEtMjE3I3VzLXdlc3QtMg" } }, "extensions": { "requestId": "fc391749-56b4-4514-a2e6-415634e390" } }Once you have initiated the [requestMultiChoiceSingleSelectPrompt](/braintree/graphql/reference/#Mutation--requestMultiChoiceSingleSelectPromptFromInStoreReader) and your application has received the InStoreContext.Id from the API response, you can now begin polling to retrieve the data input. In the example polling below, you'll notice that there are some additional data elements to include in your query in order to get the selections. The result of the node query will be a series of zeros and a single "1" where '1' signifies selected choice and '0' indicates unselected choices. The original ordering is maintained from the input.

GraphQL QueryGraphQL VariablesSample API Responsequery ID($contextId: ID!) { node(id: $contextId) { ... on RequestMultiChoiceSingleSelectPromptInStoreContext { __typename id status selections reader { id name status } } } }{ "contextId": "your context ID" }{ "data": { "node": { "__typename": "RequestMultiChoiceSingleSelectPromptInStoreContext", "id": "aW5zdG9yZWNvbnRleHmZmY5O3YzQxYjY5YjMmU0Y2VhMjkzMWI0I1ZFUklGT05FLTgwNS05NzEtMjE3I3VzLXdlc3QtMg", "status": "COMPLETE", "selections": [ 0, 0, 1, 0, 0 ], "reader": { "id": "aW5zdG9yZXJlYWRlcl8jY0Mmh3hjVJJRk9OS04MDUtOTcxLTIxNw", "name": "Your M400", "status": "ONLINE" } } }, "extensions": { "requestId": "bcfe02d0-3825-4c68-8d5a-ac03fe601c7a" } }
## Request Text Prompt

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Custom%20Prompts:Request%20Text%20Prompt.gif)Example email collection using[requestTextPrompt](/braintree/graphql/reference/#Mutation--requestTextPromptFromInStoreReader)with inputType = ALPHANUMERICThe [requestTextPrompt](/braintree/graphql/reference/#Mutation--requestTextPromptFromInStoreReader) API call allows the API caller to request customer data input on the reader screen for many use cases, such as alphanumeric input, sensitive alphanumeric input, numeric input, and sensitive numeric input. This could be used for various use cases, such as loyalty program sign-ups, private label card sign-ups, marketing email collection, emailed receipts, and many more... The request allows for the input of API variables, such as title and text to control the call-to-action messaging and the verbiage of the on-screen buttons with confirmationText and cancellationText. There are optional fields, such as inputFormat which allows you to define a desired data input format that is strictly enforced by Braintree (an error will occur if incorrect). The optional inputPlaceholder field will display placeholder text over the input box to indicate desired format to the customer. You may also determine the alignment of the text by using the alignment variable set to either "LEFT" or "CENTER". You must also specify an inputType which will indicate the type of data collection (ALPHANUMERIC, SENSITIVE_ALPHANUMERIC, NUMERIC, SENSITIVE_NUMERIC). This will determine the style of the input box and virtual keyboard.

**NOTE**
A PayPal/Braintree Solutions Engineer or Integration Engineer must enable this feature in both Sandbox and Production environments

**NOTE**
Request Text Prompt API mutation supported on firmware version 5.2.0

**NOTE**
If you would like to allow input without any format enforcement, remove the inputFormat variable from your request; it is an optional field.


#### Input Types and Example Use Cases:


- **ALPHANUMERIC** (ex: use for email collection) &gt; will display a virtual keyboard ONLY on M400


- **SENSITIVE_ALPHANUMERIC** (ex: account number entry) &gt; will display a virtual keyboard


- **NUMERIC** (ex: use for phone # collection) &gt; number pad will be used for entry


- **SENSITIVE_NUMERIC** (ex: use for SSN collection) &gt; data will be hashed as entered




#### Example Input Formats and example use cases:

| **Input Format** | **Use Case** | **Customer Input** | **API Response** |
| **/**/**** | Collect Date of Birth | 12/34/5678 | 12345678 |
| (***)***-**** | Collect Phone Number | (123)456-7890 | 1234567890 |
| ***-***-**** | Collect SSN | 123-456-7890 | 1234567890 |

GraphQL MutationGraphQL VariablesSample API Responsemutation RequestTextPromptFromReader($input: RequestTextPromptFromInStoreReaderInput!) { requestTextPromptFromInStoreReader(input: $input) { clientMutationId, id } }{ "input": { "readerId": "your reader ID", "title" : "Phone Number Collection", "text" : "Please enter your phone number", "inputType": "NUMERIC", "inputFormat": "(***) ***-****", "confirmationText": "Submit", "cancellationText": "Cancel", "waitForNextRequest": "true", "displayTimeout": 30 } }{ "data": { "requestTextPromptFromInStoreReader": { "clientMutationId": null, "id": "aW5zdG9yZWNvbnRleHRfIzIxNkMjQ1YjI5M2JlZjNjYzhlODFiZTlhI1ZFUklGT05FLTgwNS05NzEtMjE3I3VzLXdlc3QtMg" } }, "extensions": { "requestId": "fc391749-56b4-4514-a2e6-415634e390" } }Once you have initiated the [requestTextPrompt](/braintree/graphql/reference/#Mutation--requestTextPromptFromInStoreReader) and your application has received the InStoreContext.Id from the API response, you can now begin polling to retrieve the data input. In the example polling below, you'll notice that there are some additional data elements to include in your query to get the textPromptResult :

GraphQL QueryGraphQL VariablesSample API Responsequery ID($contextId: ID!) { node(id: $contextId) { ... on RequestTextPromptInStoreContext { __typename id status reader { id name status } textPromptResult inputType } } }{ "contextId": "your context ID" }{ "data": { "node": { "__typename": "RequestTextPromptInStoreContext", "id": "aW5zdG9yZWNvbnRleHmZmY5O3YzQxYjY5YjMmU0Y2VhMjkzMWI0I1ZFUklGT05FLTgwNS05NzEtMjE3I3VzLXdlc3QtMg", "status": "COMPLETE", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jY0Mmh3hjVJJRk9OS04MDUtOTcxLTIxNw", "name": "Your M400", "status": "ONLINE" }, "textPromptResult": "1234567890", "inputType": "NUMERIC" } }, "extensions": { "requestId": "bcfe02d0-3825-4c68-8d5a-ac03fe601c7a" } }
## Request Amount Prompt

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Custom%20Prompts:Request%20Amount%20Prompt.gif)Example flow from line item display, to donation screen using[requestAmountPrompt](/braintree/graphql/reference/#Mutation--requestAmountPromptFromInStoreReader), and charge requestThe [requestAmountPrompt](/braintree/graphql/reference/#Mutation--requestAmountPromptFromInStoreReader) API call allows the API caller to collect an amount input on the reader for use cases such as a custom donation amount or custom tip amount, as examples. The customer would be prompted to enter an amount using the number pad on the reader. The request allows for the input of API variables, such as title and text to control the call-to-action messaging and the verbiage of the on-screen buttons with confirmationText and cancellationText. You may also determine the alignment of the text by using the alignment variable set to either "LEFT" or "CENTER". You can define how many decimal places you would like to capture by using the decimalPlaces variable in your request, which can be set to either "ZERO", "TWO" or "THREE".

**NOTE**
A PayPal/Braintree Solutions Engineer or Integration Engineer must enable this feature in both Sandbox and Production environments.

**NOTE**
Request Amount Prompt API mutation supported on firmware version 5.2.0

GraphQL MutationGraphQL VariablesSample API Responsemutation RequestAmountPromptFromReader($input: RequestAmountPromptFromInStoreReaderInput!) { requestAmountPromptFromInStoreReader(input: $input) { clientMutationId, id } }{ "input": { "readerId": "your reader ID", "title" : "Input any text here", "text" : "Input any text here", "alignment": "CENTER", "decimalPlaces": "TWO", "cancellationText": "NO!", "confirmationText": "YES!", "waitForNextRequest": true, "displayTimeout": 30 } }{ "data": { "requestAmountPromptFromInStoreReader": { "clientMutationId": null, "id": "aW5zdG9yZWNvbnRleHRfiZmNjZDFiZ4ZWIzI1GT05FLTgwNS05NzEtMjE3I3VzLXdlc3QtMg" } }, "extensions": { "requestId": "504cf50b-e75c-4b5e-9ca1-049f9a6030" } }Once you have initiated the [requestAmountPrompt](/braintree/graphql/reference/#Mutation--requestAmountPromptFromInStoreReader) and your application has received the InStoreContext.Id from the API response, you can now begin polling to retrieve the data input. Example polling below, you'll notice that there are some additional data elements to include in your query in order to get the amountPromptResult :

GraphQL QueryGraphQL VariablesSample API Responsequery ID($contextId: ID!) { node(id: $contextId) { ... on RequestAmountPromptInStoreContext { __typename id status reader { id name status } amountPromptResult } } }{ "contextId": "your context ID" }{ "data": { "node": { "__typename": "RequestAmountPromptInStoreContext", "id": "aW5zdG9yZWNvbnRleHRfIzyM2Q3NjQ4Mzg3OWE3Y2EzMGU2Y2EzI1ZFUklGT05FLTgwNS05NzEtMjE3I3VzLXdlc3QtMg", "status": "COMPLETE", "reader": { "id": "aW5zdG9yZXJlYWRlcY0Mmh3OWo1OWhjbiNWRVJJRk9ORS04MDUtOTcxLTIxNw", "name": "Your M400", "status": "ONLINE" }, "amountPromptResult": "1234567.89" } }, "extensions": { "requestId": "563e04f5-f239-41e2-86bc-d8a1ba2ee0" } }
## Request Signature Prompt

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Custom%20Prompts_Request%20Signature%20Prompt.png)The [requestSignaturePrompt](/braintree/graphql/reference/#Mutation--requestSignaturePromptFromInStoreReader) API call allows you to initiate a request to the reader to display a signature box with a title above it. This can be used to collect a customer's signature for things like custom orders, private label card sign-ups, agreements for terms and conditions, and many more use cases. This API was created to be fully customizable and flexible for many use cases.


**NOTE**
The title input variable has a character limit of 20 characters   **Updates as of Version 4.0.0:**    ** Increased title character limit of 50 characters type="note"&gt;   ** Ability to determine the language displayed on the buttons by using the confirmationText and cancellationText input fields

**NOTE**
 **Updates as of Version 5.2.0:** ** [requestSignaturePrompt](/braintree/graphql/reference/#Mutation--requestSignaturePromptFromInStoreReader) now supports the waitForNextRequest and the displayTimeout API variable fields

GraphQL MutationGraphQL VariablesSample API Responsemutation RequestSignaturePromptFromInStoreReader($input: RequestSignaturePromptFromInStoreReaderInput!) { requestSignaturePromptFromInStoreReader(input: $input) { clientMutationId id inStoreContext { id status transaction { id orderId status customer{ id } } } } }{ "input": { "readerId": "your reader ID here", "title" : "This is what 50 characters look like on the P400:)", "confirmationText": "Accept", "cancellationText": "Decline" } }{ "data": { "requestSignaturePromptFromInStoreReader": { "clientMutationId": null, "id": "aW5zdG9yZWNvbnRleHRfI2NjljYTQWUwMTctNDU0I3VzLXdlc3QtMg", "inStoreContext": { "id": "aW5zdG9yZWNvbnRlNjljYTQxMTY51ZFgwNS0U0I3VzLXdlc3QtMg", "status": "PENDING", "transaction": null } } }, "extensions": { "requestId": "95dc9409-a5a0-44af-9a33-2f2f8558f2df" } }Once you have initiated the [requestSignaturePrompt](/braintree/graphql/reference/#Mutation--requestSignaturePromptFromInStoreReader) and your application has received the InStoreContext.Id from the API response, you can now begin polling to retrieve the signature image. Example polling below, you'll notice that there are some additional data elements to include in your query:

GraphQL QueryGraphQL VariablesSample API Responsequery ID($contextId: ID!) { node(id: $contextId) { ... on RequestSignaturePromptInStoreContext { __typename id status reader { id name status } signatureData } } }{ "contextId": "your context ID" }{ "data": { "node": { "__typename": "RequestSignaturePromptInStoreContext", "id": "aW5zdG9yZWNvbnRleHNjljYTQxMmNiNWNhZmJkFUklGT05FLTgwNS0wMTctNDU0I3VzLXdlc3QtMg", "status": "COMPLETE", "reader": { "id": "aW5zdG9yZXJlYWRlcmh3OWo1OWhRk9ORS04MDUtMDE3LTQ1NA", "name": "Test P400", "status": "ONLINE" }, "signatureData": "iVBORw0KGgoAAAANSUhEUgAAAQQAAAEcAQAAAAAJ9vdRAAABR0lEQVRoge3WMW7DMAwFUBUeMuoIOoqO5hQZOvZKLnIR5wYaNQhS7dapKZKO4QQFnOBzC/IgkfxCEFPWykBAQEBAQEBAQEBA/KPI/nXErXpxwZazY8EKAgICAuLpRHxm8clEe4ewtUj3CMeEf1xk97ggnU+Vt4sPIfyaSFyctwuS1K+4bBehMBG2iwsX4gl9rYoTFyL+w5rIlgsef3JCsHCj54LHH1ohWLhdEeJUi3cpWLiNFHV0VeOT6CtBh70K2vzwyUtBFzCM0kpRnVv/hBqlt9QogoZZgtUEXVnnNUEeVTkWTZCF5EYVZCHRqiK6uQ2nivQ3TDatKubL+7eiinkAYxdE76eW2SWzuC7SHMqCmMIIxi+J8vNVMk1ZFN04w1EcQcR4fpBH0MdixhKAijgAd1MMh8g7dvbfAQICAgICAgICYsfiGz61Fsa8dO6uAAAAAElFTkSuQmCC" } }, "extensions": { "requestId": "649ab159-feac-43b7-9241-06440979" } }You'll notice that you'll get back a field called signatureData which contains a string that is a base64 encoded PNG image file. To display this image on your application UI you would need to convert that base64 encoded string to a PNG file. Go ahead and try this with our example from the Sample API response!


## Request Confirmation Prompt

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Custom%20Prompts_Request%20Confirmation%20Prompt.png)The [requestConfirmationPrompt](/braintree/graphql/reference/#Mutation--requestConfirmationPromptFromInStoreReader) API call enables you to display a title, text and to define language displayed on 2 selectable on-screen buttons. This API call is perfect for displaying a survey question to your customer, getting a confirmation for a shipping address, or even displaying full-length terms & conditions on the reader screen display. This feature was designed to be fully customizable and flexible to meet the needs of various use cases.


**NOTE**
The title input variable has a character limit of 20 characters, but the text input variable can go up to 5,000+ characters. Use this space wisely!   You can customize the text alignment to be either CENTER or LEFT. and you can determine the language displayed on the buttons by using the confirmationText and cancellationText input fields    **Updates as of Version 4.0.0:**    ** Increased title character limit of 50 characters

**NOTE**
 **Updates as of Version 5.2.0:** ** [requestConfirmationPrompt](/braintree/graphql/reference/#Mutation--requestConfirmationPromptFromInStoreReader) now supports the waitForNextRequest and the displayTimeout API variable fields

GraphQL MutationGraphQL VariablesSample API Responsemutation RequestConfirmationFromReader($input: RequestConfirmationPromptFromInStoreReaderInput!) { requestConfirmationPromptFromInStoreReader(input: $input) { clientMutationId, id inStoreContext { id status transaction { id orderId status customer{ id } } } } }{ "input": { "readerId": "your reader ID", "title" : "Please Select Below", "text" : "How was your day today?", "confirmationText": "Fantastic", "cancellationText": "Great", "alignment": "CENTER" } }{ "data": { "requestConfirmationPromptFromInStoreReader": { "clientMutationId": null, "id": "aW5zdG9yZWNvbnRGVhMDRmYzlhNTggwNS0wMTctNDU0I3VzLXdlc3QtMg", "inStoreContext": { "id": "aW5zdG9yZWNvbnRleHRfIzDRkMS0wMTctNDU0I3VzLXdlc3QtMg", "status": "PENDING", "transaction": null } } }, "extensions": { "requestId": "58afc06c-98cf-457c-a8d4-b0b2975a" } }Once you initiate the [requestConfirmationPrompt](/braintree/graphql/reference/#Mutation--requestConfirmationPromptFromInStoreReader), you will get back an InStoreContext.Id, which you can then poll against to retrieve the boolean response of the selection that your customer chose on the reader display. See below the polling query and sample API response. You'll notice that there is a boolean response of either true or false depending on the selection on the reader display.

GraphQL QueryGraphQL VariablesSample API Responsequery ID($contextId: ID!) { node(id: $contextId) { ... on RequestConfirmationPromptInStoreContext { __typename id status reader { id name status } confirmed } } }{ "contextId": "your context ID" }{ "data": { "node": { "__typename": "RequestConfirmationPromptInStoreContext", "id": "aW5zdG9yZWNvbNGVhMDMDNjI1ZFUklGT05FLTgwNS0wMTctNDU0I3VzLXdlc3QtMg", "status": "COMPLETE", "reader": { "id": "aW5zdG9yZ3OWo1OWhjbiNWRVJJRMDE3LTQ1NA", "name": "Test P400", "status": "ONLINE" }, "confirmed": true } }, "extensions": { "requestId": "365260f0-6449-49f4-81f2-ac0faea" } }
## Create a seamless flow with multiple Custom Prompts

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Custom%20prompts_seamless%20flow%20with%20multiple%20Custom%20Prompts.png)Example of how to string multiple prompts together to create a seamless flowEach of the Custom Prompts API mutations is allowed to override the processing spinner transition screen when passing the waitForNextRequest variable set to true. This will allow you to string together multiple Custom Prompts requests to create a seamless flow for the customer without interruptions or clunky transitions. The processing spinner transition screen has a hardcoded timeout window of 120 seconds.


## Physical Button Behavior (X, &lt;, O)

When using any of the Custom Prompts API mutations, the physical buttons on the number pad are consistent with the on-screen buttons to allow for accessibility to the visually impaired. For example, pressing the red X button will result in a cancellationText on-screen button selection. Similarly, pressing the green O button will result in a confirmationText on-screen button selection. The yellow &lt; button will result in a backspace or deletion of the input data.


## Canceling an in-progress Custom Prompt

To cancel an in-progress Custom Prompt, you'll need to send a [requestTextDisplay](/braintree/in-person/guides/display-information/#request-text-display) with the displayTimeout set to "0". This will result in the cancellation of the Custom Prompt and the return to the reader screensaver display. You may also use the [requestCancelContext](/braintree/in-person/guides/making-a-transaction/#cancelling-a-charge) mutation as long as no data inputs have been submitted from the reader.


## Tips when integrating with Custom Prompts


- None of the Custom Prompts API mutations are supported for [offline processing](/braintree/in-person/guides/offline-transactions/)


- The timeout window when passing the waitForNextRequest flag set to " true " is 120 seconds


- If a lot of characters are passed in text or title in the request, the input box will be pushed down the screen display and will require scrolling to view


- Virtual keyboard is rendered only on the M400 device when using the [requestTextPrompt](/braintree/in-person/guides/custom-prompts/#request-text-prompt) with inputType set to "ALPHANUMERIC" for other input types "NUMERIC" and "SENSITIVE_NUMERIC" the number pad on the reader will be used for data input


- For [requestAmountPrompt](/braintree/in-person/guides/custom-prompts/#request-amount-prompt) the number pad on the reader will be used for data input


- When using [requestTextPrompt](/braintree/in-person/guides/custom-prompts/#request-text-prompt) and [requestAmountPrompt](/braintree/in-person/guides/custom-prompts/#request-amount-prompt), the response data tied to the context ID is retrievable for about 10 minutes


- When using [requestTextPrompt](/braintree/in-person/guides/custom-prompts/#request-text-prompt) and [requestAmountPrompt](/braintree/in-person/guides/custom-prompts/#request-amount-prompt), the response data tied to the context ID will be deleted after the first successful retrieval




## Data Processing

Please refer to [our page on PayPal Braintree Sub-processors](/braintree/in-person/reference/paypal-braintree-sub-processors/) to understand what other entities may come in contact with data collected through our Custom Prompts API


## Video Tutorials


### Creating a Loyalty Sign-Up Flow:


### Commonly Asked Questions about Custom Prompts:



[Display Information](/braintree/in-person/guides/display-information/)[Card Data Collection](/braintree/in-person/guides/card-data-collection/)