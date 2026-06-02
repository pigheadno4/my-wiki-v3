---
title: Disputes Integration Guide
slug: /docs/disputes/integration-guide/
createTime: "2024-08-15T05:56:42.702Z"
updateTime: "2025-12-17T01:02:16.674Z"
---

# Disputes Integration Guide

PayPal merchants, partners, and external developers can use the PayPal Disputes API to manage disputes.

For concepts, see the [Disputes Overview](/docs/disputes/) .

## Integration steps

| Step | Required | Stage                                                     | Description                                                                                                                                                                                                    |
| ---- | -------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.   | Required | Prerequisite                                              | [Set up your development environment](#set-up-your-development-environment).                                                                                                                                   |
| 2.   | Optional | [Gather dispute information](#gather-dispute-information) | You can[list disputes](#list-disputes)and[show details for a single dispute](#show-dispute-details).                                                                                                           |
| 3.   | Optional | [Inquiry](#inquiry-stage)                                 | You can[send message to the other party](#send-message-to-other-party),[make an offer to resolve the dispute](#make-offer-to-resolve-dispute), and[escalate a dispute to a claim](#escalate-dispute-to-claim). |
| 4.   | Optional | [Claim](#claim-stage)                                     | You can[provide evidence](#provide-evidence),[accept the claim](#accept-claim), or[appeal the dispute](#appeal-dispute)if it was resolved in favor of the counter party.                                       |
| 5.   | Optional | [Settlement](#sandbox-only-methods)                       | In the sandbox, you can update the dispute status and settle the dispute. See[Disputes and Integration Testing](/docs/integration/direct/customer-disputes/testing/).                                          |

## Set up your development environment

Before you can integrate Disputes, you must set up your development environment. After you get a token that lets you access protected REST API resources, you create sandbox accounts to test your web and mobile apps.

When you create an app, enable **Disputes** in the **App feature options** section.

For details, see [Get Started](/api/rest/) .

Then, return to this page to integrate Disputes.

## Gather dispute information

You can gather dispute information during any dispute lifecycle stage. You can [list disputes](#list-disputes) and [show details for a single dispute](#show-dispute-details) .

### List disputes

Merchants can list disputes. When you list disputes, the response shows the dispute_id , reason , status , dispute_amount , create_time , and update_time fields for each dispute.

To filter the disputes in the response, specify one or more optional query parameters in the request URI.

For a full list of query parameters and additional information, see [list disputes](/docs/api/customer-disputes/v1/#disputes_list) in the API reference.

### Show dispute details

To show details for a dispute, you include the dispute ID in the request URI. The [response](/docs/api/customer-disputes/v1/#disputes_get) shows dispute details and [HATEOAS links](/api/rest/responses/#hateoas-links) that enable you to complete other actions for the dispute.

**Note:** The fields that appear in the response depend on whether you access this call through first- or third-party access. For example, if the merchant shows dispute details through third-party access, the customer's email ID does not appear.

For additional information, see [show dispute details](/docs/api/customer-disputes/v1/#disputes_get) in the API reference.

### Acknowledge returned item

At any stage in the dispute lifecycle, merchants can request that the customer return a MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED item or service for a full refund. Until the merchant calls [provide evidence](#provide-evidence) to provide PROOF_OF_RETURN , the dispute has the WAITING_FOR_SELLER_RESPONSE status.

For additional information, see [acknowledge returned item](/docs/api/customer-disputes/v1/#disputes_acknowledge-return-item) in the API reference.

## Inquiry stage

In the inquiry stage, the dispute status must be INQUIRY .

In this stage, you can [send a message to the other party](#send-message-to-other-party) , [make an offer to resolve the dispute](#make-offer-to-resolve-dispute) , and [escalate a dispute to a claim](#escalate-dispute-to-claim) .

### Send message to other party

To [send a message to the other party](/docs/api/customer-disputes/v1/#disputes_send-message) , you include the dispute ID in the request URI.

You must also include a message to the other party in the JSON request body.

A successful request returns the HTTP 200 OK status code and a JSON response body that includes a link to the dispute.

### Make offer to resolve dispute

A merchant can make these types of offers to a customer:

| Offer type                          | Description                                                                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Refund only                         | The merchant agrees to refund a specific amount to the customer.                                                                |
| Refund with return from customer    | The merchant agrees to refund the full dispute amount but expects the customer to return the item to a specific return address. |
| Refund with replacement to customer | The merchant agrees to refund a specific amount and agrees to send the customer a replacement item.                             |

To [make an offer to resolve a dispute](/docs/api/customer-disputes/v1/#disputes_make-offer) , you include the dispute ID in the request URI.

You must also include a note about the offer and the offer amount. You can optionally include a return shipping address for the item and the ID of the invoice for the refund:

|                         |        |          |                                             |
| ----------------------- | ------ | -------- | ------------------------------------------- |
| note                    | string | Required | The notes about the offer.                  |
| offer_amount            | object | Required | The amount proposed to resolve the dispute. |
| return_shipping_address | object | Optional | The return address for the item.            |
| invoice_id              | string | Optional | The ID of the invoice for the refund.       |

A successful request returns the HTTP 200 OK status code and a JSON response body that includes a link to the dispute.

### Escalate dispute to claim

You can escalate a dispute by ID to a PayPal claim to resolve the dispute.

You specify the dispute ID in the URI and include a note about the escalation in the JSON request body:

curl "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-KPE-22563488/escalate" \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS_TOKEN" \
 -d '{
"note": "Escalating to PayPal claim for resolution."
}'A successful request returns the HTTP 200 OK status code and a JSON response body that includes a link to the dispute:

{
"links": [{
"rel": "self",
"method": "GET",
"href": "https://api-m.sandbox.paypal.com/v1/customer/disputes/PP-R-KPE-22563488"
}]
}## Claim stage
In the claim stage, you can [provide evidence](#provide-evidence) , [accept a claim](#accept-claim) , and [appeal a dispute](#appeal-dispute) .

### Provide evidence

Customers and merchants can provide evidence for a dispute by ID. Merchants can provide evidence for disputes that have the WAITING_FOR_SELLER_RESPONSE status while customers can provide evidence for disputes that have the WAITING_FOR_BUYER_RESPONSE status.

Evidence can be a proof of delivery or proof of refund document or notes, which can include logs. A proof of delivery document includes a tracking number while a proof of refund document includes a refund ID.

- The maximum length of notes can be 2000 characters.
- For constraints and rules regarding documents, see [documents](#documents) .

Each dispute reason requires certain information for various evidence types. See [dispute reasons](#dispute-reasons) .

To make this request, specify the dispute ID in the URI and specify the evidence in the JSON request body. For information about dispute reasons that are associated with evidence types, see [dispute reasons](#dispute-reasons) .

The response provides a [HATEOAS links](/api/rest/responses/#hateoas-links) that enables you to get more information about the dispute.

For additional information, see [provide evidence](/docs/api/customer-disputes/v1/#disputes_provide-evidence) in the API reference.

### Accept claim

When you accept a claim for a dispute, the dispute closes in the customer's favor and you refund the customer's money from your merchant's account.

In addition to specifying the ID of the dispute in the URI, specify one or more optional [parameters](/docs/api/customer-disputes/v1/#disputes_accept-claim) in the JSON request body:

- Your notes for acceptance of the customer's claim.
- Your reason for acceptance of the customer's claim. See [dispute reasons](#dispute-reasons) .
- The ID of the invoice for the refund.

For additional information, see [accept claim](/docs/api/customer-disputes/v1/#disputes_accept-claim) in the API reference.

### Appeal dispute

You can appeal a lost dispute by ID.

To appeal a dispute, use the appeal link in the HATEOAS links from the show dispute details response. If this link does not appear, you cannot appeal the dispute.

Specify the dispute ID in the URI, and submit new evidence as a document or notes in the JSON request body. Evidence can be a proof of delivery or proof of refund document or notes, which can include logs. A proof of delivery document includes a tracking number while a proof of refund document includes a refund ID.

- The maximum length of notes can be 2000 characters.
- For constraints and rules regarding documents, see [documents](#documents) .

If the seller appeals after a dispute has been resolved in the buyer's favor, the dispute is open again. The DISPUTE.UPDATED webhook is sent. This type of appeal can result in a win or loss for the seller.

If the seller wins this appeal, the seller gets money from PayPal, and the CASE.RESOLVED webhook is sent. There is no payment webhook, but there is an entry in the settlement report with the code T0805.

If the seller loses this appeal, there is no money movement, and the case is closed. The CASE.RESOLVED webhook is sent.

For additional information about dispute reasons, see [dispute reasons](#dispute-reasons) .

For additional information, see [appeal dispute](/docs/api/customer-disputes/v1/#disputes_appeal) in the API reference.

## Sandbox-only methods

In the sandbox, you can use create dispute , update dispute status , or settle dispute . To create a dispute in the sandbox, you must set up buyer-side credentials. To update the dispute status or settle a dispute, you do not need to set up the buyer-side credentials. Refer to API documentation for more information about [update dispute status](/docs/api/customer-disputes/v1/#disputes_require-evidence) and [settle dispute](/docs/api/customer-disputes/v1/#disputes_adjudicate) .

## Enable buyer disputes in sandbox

To create a dispute in the sandbox, you must enable the buyer using the following steps.

### 1. Get permission from the buyer

To get permission from the buyer to create disputes on their behalf, complete the steps 1 Enable Log in with PayPal and 2 Add Log in with PayPal button from the [Log in with PayPal integration](/docs/log-in-with-paypal/integrate/) guide to create a Log in with PayPal button.
For simplicity in step 2 you can choose the [Generate button](/docs/log-in-with-paypal/integrate/generate-button/) option which generates a button for you, using your application ID (client ID). You can have the scope as openid and the return URL should be the same you set for your application in step 1 of the guide.
Create a personal sandbox account to be used as buyer's account. Use this account to log in once you click on the generated button and provide the consent after login.

### 2. Generate access token

Use the following code to generate an access token. Use the CLIENT_ID and secret access token for the merchant to access the PayPal Dispute API.

curl -v -X POST "https://api-m.sandbox.paypal.com/v1/oauth2/token" \
 -u "CLIENT_ID:CLIENT_SECRET" \
 -H "Content-Type: application/x-www-form-urlencoded" \
 -d "grant_type=client_credentials"### 3. Generate JSON web token for PayPal Authorization Assertion
Use the following HTML code to generate the JSON web token. You can use any HTML sandbox environment to execute this or create a simple HTML file to open it in a browser. Replace the CLIENT_ID and BUYER_EMAIL before execution.

The CLIENT_ID is from the merchant's REST API. The BUYER_EMAIL is the buyer's email address. The JSON web token is given as output.

&lt;span id='cwppButton'&gt;&lt;/span&gt;
&lt;html&gt;
&lt;script&gt;
function base64url(source) {
var encodedSource = btoa(source);
encodedSource = encodedSource.replace(/=+$/, '');
encodedSource = encodedSource.replace(/\+/g, '-');
encodedSource = encodedSource.replace(/\//g, '-');
return encodedSource;
}
function generateJWT() {
var header = {"alg": "none", "typ": "JWT"};
var data = {"iss":"CLIENT_ID", "email" : "BUYER_EMAIL" };
document.write(base64url(JSON.stringify(header)) + "." +
base64url(JSON.stringify(data)) + ".");
}
&lt;/script&gt;
&lt;body onload="generateJWT()"/&gt;
&lt;html&gt;### 4. Create a transaction using the buyer's account
Login to the buyer account you created in step 2 and use it to perform a send money action to the business account you have used for creating the application. This is the transaction you will be using to create a dispute.
Head to the sandbox [activity](https://www.sandbox.paypal.com/myaccount/activities/) page for the personal account and make note of the transaction ID for the transaction you just performed. Use this transaction ID to create a dispute in the next step.

### 5. Create the dispute

Use the following cURL code to create the dispute replacing the ACCESS_TOKEN , JWT-TOKEN and BUYER-TRANSACTION-ID with their respective values.
The ACCESS_TOKEN is the access token from step 2, JWT-TOKEN is the JSON web token from step 3 and the BUYER-TRANSACTION-ID is the buyer transaction ID from step 5.

curl -X POST "https://api-m.sandbox.paypal.com/v1/customer/disputes" \
-H "Authorization: Bearer ACCESS_TOKEN" \
-H 'Content-Type: multipart/form-data' \
-H "PayPal-Auth-Assertion: JWT-TOKEN" \
-F 'input={"disputed_transactions": [{
"buyer_transaction_id": "BUYER-TRANSACTION-ID"
}],
"reason": "MERCHANDISE_OR_SERVICE_NOT_RECEIVED",
"dispute_amount": { "currency_code":"USD", "value": "7.50" },
"extensions": {
"merchant_contacted": true,
"merchant_contacted_outcome": "NO_RESPONSE",
"merchandize_dispute_properties": {
"issue_type": "PRODUCT"
}
}
};type=application/json'### 6. Creating a chargeback
Using the following code, pass the access token, and the seller transaction ID to create a chargeback.
The &lt;ACCESS_TOKEN&gt; is the access token from step 2 and &lt;SELLER_TRANSACTION_ID&gt; can be found on the activity page of your business account which you used in step 5 to send the money to. Make sure that the send money operation was performed via credit card for the transaction to be eligible for a chargeback.
Login via the business account and head on to the [activities](https://www.sandbox.paypal.com/activities/) page to find the transaction ID.
Note: update the receive_date and money_movement_date to the current value, and response_date to a future value.

curl -X POST "https://api-m.sandbox.paypal.com/v2/customer-support/process-chargeback" \
-H "Authorization: Bearer &lt;ACCESS_TOKEN&gt;" \
-H "Content-Type: application/json" \
--data-raw '{
"adjacency": "PAYPAL",
"file_layout": "ATCK_CB",
"financial_institution": {
"processor": "FDMS"
},
"transaction": {
"id_enc": "&lt;SELLER_TRANSACTION_ID&gt;",
"amount": {
"currency_code": "EUR",
"value": "100"
}
},
"instrument": {
"card_brand": "VISA",
"credit_card_transaction_id": "",
"external": false
},
"dispute": {
"id": null,
"stage": "CHARGEBACK",
"response_date": "2023-07-16T12:05:22.544Z",
"status": "2",
"amount": {
"currency_code": "EUR",
"value": "15"
},
"receive_date": "2023-06-16T12:05:22.544Z",
"event_code": "CHARGEBACK_INITIATED",
"money_movement_date": "2023-06-16T12:05:22.544Z",
"event_type": "DEBIT",
"chargeback_type": "REPORTED_TO_PROCESSOR",
"processor_info": {
"reference_number": "31639435342702423793399",
"reason_code": "4853",
"notes": "TEST_MEMO",
"additional_info": []
}
},
"processor_auxiliary_info": {}
}'## Negative testing for disputes
You can use simulation to test your disputes. For more information, see [Disputes and Integration Testing](/docs/integration/direct/customer-disputes/testing/) .

## Dispute reasons

The information required from the seller to contest a dispute or chargeback varies depending on the dispute [reason](/docs/api/customer-disputes/v1/#definition-dispute_reason) .
While the tables below offer a broad overview of the information typically sought initially, it's crucial to confirm the specific evidence_type under [evidence](/api/customer-disputes/v1/#definition-evidence) requested by PayPal before submission.
Kindly review the evidences with source as REQUESTED_FROM_SELLER to identify the evidences that have been requested from the seller.

It's important to note that PayPal may request for additional information from the seller multiple times throughout the disputes lifecycle.
In instances where further clarification is required, the case [status](/docs/api/customer-disputes/v1/#definition-status) will transition to WAITING_FOR_SELLER_RESPONSE and details about the sought after information will be communicated through the evidence_type with the source being REQUESTED_FROM_SELLER . See [evidence](/api/customer-disputes/v1/#definition-evidence) .

### MERCHANDISE_OR_SERVICE_NOT_RECEIVED

The customer did not receive the merchandise or service.

| Evidence type        | Required      |
| -------------------- | ------------- |
| PROOF_OF_FULFILLMENT | tracking_info |

- tracking_number
- carrier_name

ornoteor[document](#documents). For example, a document can be a proof of delivery signature or a proof of receipt copy. |
| PROOF_OF_REFUND | refund_ids |

### MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED

The customer reports that the merchandise or service was not as described.

| Evidence type   | Required                                                                                                                                           |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| OTHER           | A note or [document](#documents) . For example, a document can be a description, item URL, return policy, or a copy of a contract or an affidavit. |
| PROOF_OF_REFUND | A set of refund_ids .                                                                                                                              |

### UNAUTHORISED

The customer did not authorize purchase of the merchandise or service.

| Evidence type        | Required                                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| PROOF_OF_FULFILLMENT | - tracking_number                                                                                                           |
| - carrier_name       |
| PROOF_OF_REFUND      | The refund ID.                                                                                                              |
| OTHER                | A note or [document](#documents) . For example, a document can be a proof of delivery signature or a proof of receipt copy. |

### CREDIT_NOT_PROCESSED

The credit transaction was not processed for the customer.

| Evidence type   | Required                                                                               |
| --------------- | -------------------------------------------------------------------------------------- |
| PROOF_OF_REFUND | The refund ID.                                                                         |
| OTHER           | A note or [document](#documents) . For example, a document can be a credit due reason. |

### DUPLICATE_TRANSACTION

The transaction was a duplicate.

| Evidence type   | Required                           |
| --------------- | ---------------------------------- |
| PROOF_OF_REFUND | The refund ID.                     |
| OTHER           | A note or [document](#documents) . |

### INCORRECT_AMOUNT

The customer was charged an incorrect amount.

| Evidence type   | Required                                                                                     |
| --------------- | -------------------------------------------------------------------------------------------- |
| PROOF_OF_REFUND | The refund ID, for the difference in amount.                                                 |
| OTHER           | A note or [document](#documents) . For example, a document can be a price difference reason. |

### PAYMENT_BY_OTHER_MEANS

The customer paid for the transaction through other means.

| Evidence type   | Required                                     |
| --------------- | -------------------------------------------- |
| PROOF_OF_REFUND | The refund ID, for the difference in amount. |
| OTHER           | A note or [document](#documents) .           |

### CANCELED_RECURRING_BILLING

The customer was incorrectly charged because he or she canceled recurring billing.

| Evidence type   | Required                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------- |
| PROOF_OF_REFUND | The refund ID, for the difference in amount.                                                |
| OTHER           | A note or [document](#documents) . For example, a document can be a subscription agreement. |

### OTHER

| Evidence type   | Required                           |
| --------------- | ---------------------------------- |
| PROOF_OF_REFUND | The refund ID.                     |
| OTHER           | A note or [document](#documents) . |

### Documents

The following rules apply to document file types and sizes:

- The party can upload up to 50 MB of files per request.
- Individual files must be smaller than 10 MB.
- The supported file formats are JPG, JPEG, GIF, PNG, and PDF.

## Additional information

- [Disputes Frequently Asked Questions (FAQ)](/docs/disputes/faq/)
- [Disputes and Webhooks](/docs/disputes/webhooks/)
- [Disputes and Integration Testing](/docs/disputes/testing/)
- [Disputes, claims, chargebacks, and bank reversals](https://www.paypal.com/us/brc/article/customer-disputes-claims-chargebacks-bank-reversals)
- [Disputes API reference](/api/customer-disputes/v1/)
