---
title: Subscribe to disputes webhooks
slug: /docs/disputes/webhooks/
createTime: "2024-08-15T05:52:07.048Z"
updateTime: "2025-05-13T15:53:20.523Z"
---

# Subscribe to disputes webhooks

Merchants can subscribe to disputes webhooks.

Webhooks are HTTP callbacks that receive notification messages for events. To create a webhook at PayPal, users configure a webhook listener and subscribe it to events. A webhook listener is a server that listens at a specific URL for incoming HTTP POST notification messages that are triggered when events occur. PayPal signs each notification message that it delivers to your webhook listener.

## Notification flow

If a merchant subscribes to dispute webhooks, the following notification flow occurs:

|                                                        |                                                                                                                                                                                                                                                            |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.                                                     | When a customer files a case, the merchant is notified with aCUSTOMER.DISPUTE.CREATEDwebhook that includes the dispute ID.                                                                                                                                 |
| 2.                                                     | The merchant can use the dispute ID to[show dispute details](/docs/api/customer-disputes/v1/#disputes_get)and take appropriate action based on the allowable actions in the[HATEOAS links](/api/rest/responses/#hateoas-links)that appear in the response. |
| 3.                                                     | The merchant can either:- Provide sufficient evidence and dispute the case.                                                                                                                                                                                |
| - Accept the claim, which refunds the disputed amount. |

## Events

A merchant who subscribes to dispute webhooks receives these webhook events notifications:

| Event                     | Triggered when         |
| ------------------------- | ---------------------- |
| CUSTOMER.DISPUTE.CREATED  | A dispute is created.  |
| CUSTOMER.DISPUTE.RESOLVED | A dispute is resolved. |
| CUSTOMER.DISPUTE.UPDATED  | A dispute is updated.  |

For more information about Disputes API webhooks, see the [Disputes](/api/rest/webhooks/event-names/#disputes) webhook event names.

## Webhook details

A webhook for a disputes event includes these [details](/docs/api/customer-disputes/v1/#disputes-get-response) :

- dispute_id . The ID of the dispute.

- create_time . The date and time when the dispute was created, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6) .

- update_time . The date and time when the dispute was last updated, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6) .

- disputed_transactions . An array of transactions for which the disputes were created:

- transaction_info : - buyer_transaction_id . The ID, as seen by the customer, for this transaction.
- seller_transaction_id . The ID, as seen by the merchant, for this transaction.
- create_time . The date and time when the transaction was created, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6) . For example, yyyy-MM-ddTHH:mm:ss.SSSZ . - date_time . The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6) . Seconds are required while fractional seconds are optional. **Note:**The regular expression provides guidance but does not reject all invalid dates.

- transaction_status . The transaction status:

- COMPLETED . The transaction processing completed.
- UNCLAIMED . The items in the transaction are unclaimed. If they are not claimed within 30 days, the funds are returned to the sender.
- DENIED . The transaction was denied.
- FAILED . The transaction failed.
- HELD . The transaction is on hold.
- PENDING . The transaction is waiting to be processed.
- PARTIALLY_REFUNDED . The payment for the transaction was partially refunded.
- REFUNDED . The payment for the transaction was successfully refunded.
- REVERSED . The payment for the transaction was reversed due to a chargeback or other reversal type.
- CANCELLED . The transaction is cancelled.

- invoice_number . The ID of the invoice that is associated with the payment.
- seller . The details for the merchant who receives the funds and fulfills the order. For example, merchant ID, contact email address, and so on. - name . The name of the merchant.

- custom . A free-text field that is entered by the merchant during checkout.
- items . An array of items that were purchased as part of the transaction:

- item_id . The ID of the item.
- reason . The reason for the item-level dispute:

- MERCHANDISE_OR_SERVICE_NOT_RECEIVED . The customer did not receive the merchandise or service.
- MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED . The customer reports that the merchandise or service was not as described.
- UNAUTHORISED . The customer did not authorize purchase of the merchandise or service.
- CREDIT_NOT_PROCESSED . The refund or credit wasn't processed for the customer.
- DUPLICATE_TRANSACTION . The transaction was a duplicate.
- INCORRECT_AMOUNT . The customer was charged an incorrect amount.
- PAYMENT_BY_OTHER_MEANS . The customer paid for the transaction through other means.
- CANCELED_RECURRING_BILLING . The customer was being charged for a subscription or a recurring transaction that was canceled.
- PROBLEM_WITH_REMITTANCE . A problem occurred with the remittance.
- OTHER . Other.

- dispute_amount . The amount in the transaction that the customer originally disputed. Because customers can sometimes dispute only part of the payment, the disputed amount might be different from the total gross or net amount of the original transaction.

- currency_code . The [three-character ISO-4217 currency code](/docs/integration/direct/rest/currency-codes/) that identifies the currency.
- value . The value, which might be:

- An integer for currencies like JPY that are not typically fractional.
- A decimal fraction for currencies like TND that are subdivided into thousandths.

  For the required number of decimal places for a currency code, see [Currency codes - ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) .

- notes . Any notes provided with the item.
- partner_transaction_id . The ID of the transaction in the partner system. The partner transaction ID is returned at an item level because the partner might show different transactions for different items in the cart.

- gross_amount . The gross amount of the transaction.

- reason . The reason for the item-level dispute:

- MERCHANDISE_OR_SERVICE_NOT_RECEIVED . The customer did not receive the merchandise or service.
- MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED . The customer reports that the merchandise or service is not as described.
- UNAUTHORISED . The customer did not authorize purchase of the merchandise or service.
- CREDIT_NOT_PROCESSED . The refund or credit was not processed for the customer.
- DUPLICATE_TRANSACTION . The transaction was a duplicate.
- INCORRECT_AMOUNT . The customer was charged an incorrect amount.
- PAYMENT_BY_OTHER_MEANS . The customer paid for the transaction through other means.
- CANCELED_RECURRING_BILLING . The customer was being charged for a subscription or a recurring transaction that was canceled.
- PROBLEM_WITH_REMITTANCE . A problem occurred with the remittance.
- OTHER . Other.

  For information about the required information for each dispute reason and associated evidence type, see [dispute reasons](/docs/disputes/integration-guide/#dispute-reasons) .

- status . The status of the dispute:

- OPEN . Open.
- WAITING_FOR_BUYER_RESPONSE . The dispute is waiting for a response from the customer.
- WAITING_FOR_SELLER_RESPONSE . The dispute is waiting for a response from the merchant.
- UNDER_REVIEW . The dispute is under review.
- RESOLVED . The dispute is resolved.
- OTHER . Another reason.

- dispute_amount . The amount in the transaction that the customer originally disputed. Because customers can sometimes dispute only part of the payment, the disputed amount might be different from the total gross or net amount of the original transaction.

- currency_code . The [three-character ISO-4217 currency code](/docs/integration/direct/rest/currency-codes/) that identifies the currency.
- value . The value, which might be:

- An integer for currencies like JPY that are not typically fractional.
- A decimal fraction for currencies like TND that are subdivided into thousandths.

  For the required number of decimal places for a currency code, see [Currency codes - ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) .

- dispute_outcome . The outcome of a dispute.

- outcome_code . The outcome of a resolved dispute. The possible values are:

- RESOLVED_BUYER_FAVOUR . The dispute was resolved in the customer's favor.
- RESOLVED_SELLER_FAVOUR . The dispute was resolved in the merchant's favor.
- RESOLVED_WITH_PAYOUT . PayPal provided the merchant or customer with protection and the case is resolved.
- CANCELED_BY_BUYER . The customer canceled the dispute.
- ACCEPTED . PayPal accepted the dispute.
- DENIED . PayPal denied the dispute.
- NONE . Cases resolved without an outcome due to subsequent case on the same transaction.

- amount_refunded . The amount that either the merchant or PayPal refunds the customer.

- currency_code . The [three-character ISO-4217 currency code](/docs/integration/direct/rest/currency-codes/) that identifies the currency.
- value . The value, which might be:

- An integer for currencies like JPY that are not typically fractional.
- A decimal fraction for currencies like TND that are subdivided into thousandths.

  For the required number of decimal places for a currency code, see [Currency codes - ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) .

- dispute_life_cycle_stage . The stage in the dispute lifecycle.

The possible values are:

- INQUIRY . A customer and merchant interact in an attempt to resolve a dispute without escalation to PayPal. Occurs when the customer: - Has not received goods or a service.
- Reports that the received goods or service are not as described.
- Needs more details, such as a copy of the transaction or a receipt.

- CHARGEBACK . A customer or merchant escalates an inquiry to a claim, which authorizes PayPal to investigate the case and make a determination. Occurs only when the dispute channel is INTERNAL . This stage is a PayPal dispute lifecycle stage and not a credit card or debit card chargeback. All notes that the customer sends in this stage are visible to PayPal agents only. The customer must wait for PayPal’s response before the customer can take further action. In this stage, PayPal shares dispute details with the merchant, who can complete one of these actions: - Accept the claim.
- Submit evidence to challenge the claim.
- Make an offer to the customer to resolve the claim.

- PRE_ARBITRATION . The first appeal stage for merchants. A merchant can appeal a chargeback if PayPal's decision is not in the merchant's favor. If the merchant does not appeal within the appeal period, PayPal considers the case resolved.
- ARBITRATION . The second appeal stage for merchants. A merchant can appeal a dispute for a second time if the first appeal was denied. If the merchant does not appeal within the appeal period, the case returns to a resolved status in pre-arbitration stage.

- dispute_channel . The channel where the customer created the dispute.

The possible values are:

- INTERNAL . The customer contacts PayPal to file a dispute with the merchant.
- EXTERNAL . The customer contacts their card issuer or bank to request a refund.

- messages . An array of messages that were posted by the customer and merchant.

- posted_by . The customer or merchant who posted the message. The possible values are:

- BUYER . The customer posted the message.
- SELLER . The merchant posted the message.

- time_posted . The date and time when the message was posted, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6) .

- content The customer- or merchant-posted content.

- evidences . An array of evidence documents.

- evidence_type . The evidence type. The possible values are:

- PROOF_OF_FULFILLMENT . Proof of fulfillment.
- PROOF_OF_REFUND . Proof of refund.
- PROOF_OF_DELIVERY_SIGNATURE . Proof of delivery signature.
- PROOF_OF_RECEIPT_COPY . Proof of receipt copy.
- RETURN_POLICY . The return policy.
- BILLING_AGREEMENT . The billing agreement.
- PROOF_OF_RESHIPMENT . Proof of re-shipment.
- ITEM_DESCRIPTION . The item description.
- POLICE_REPORT . A police report.
- AFFIDAVIT . An affidavit.
- PAID_WITH_OTHER_METHOD . Paid with another method.
- COPY_OF_CONTRACT . Copy of the contract.
- TERMINAL_ATM_RECEIPT . The ATM receipt.
- PRICE_DIFFERENCE_REASON . The reason for the price difference.
- SOURCE_CONVERSION_RATE . The source conversion rate.
- BANK_STATEMENT . The bank statement.
- CREDIT_DUE_REASON . The credit due reason.
- REQUEST_CREDIT_RECEIPT . The request credit receipt.
- PROOF_OF_RETURN . Proof of return.
- CREATE . Create.
- CHANGE_REASON . The change reason.
- OTHER . Other.

- evidence_info . The evidence-related information.

- documents . An array of evidence documents.

- notes . Any evidence-related notes.

- item_id . The item ID. If the merchant provides multiple pieces of evidence and the transaction has multiple item IDs, the merchant can use this value to associate a piece of evidence with an item ID.

- buyer_response_due_date . The date and time by when the customer must respond to the dispute, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6) . If the customer does not respond by this date and time, the dispute is closed in the merchant's favor. For example, yyyy - MM - dd T HH : mm : ss . SSS Z .

- seller_response_due_date . The date and time by when the merchant must respond to the dispute, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6) . If the merchant does not respond by this date and time, the dispute is closed in the customer's favor. For example, yyyy - MM - dd T HH : mm : ss . SSS Z .

- offer . The merchant-proposed offer for a dispute.

- buyer_requested_amount . The customer-requested refund for this dispute.

- currency_code . The [three-character ISO-4217 currency code](/docs/integration/direct/rest/currency-codes/) that identifies the currency.
- value . The value, which might be:

- An integer for currencies like JPY that are not typically fractional.
- A decimal fraction for currencies like TND that are subdivided into thousandths.

  For the required number of decimal places for a currency code, see [Currency codes - ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) .

- seller_offered_amount . The merchant-offered refund for this dispute.

- currency_code . The [three-character ISO-4217 currency code](/docs/integration/direct/rest/currency-codes/) that identifies the currency.
- value . The value, which might be:

- An integer for currencies like JPY that are not typically fractional.
- A decimal fraction for currencies like TND that are subdivided into thousandths.

  For the required number of decimal places for a currency code, see [Currency codes - ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) .

- offer_type . The merchant-proposed offer type for the dispute. The possible values are:

- REFUND . The merchant must refund the customer without any item replacement or return. This offer type is valid in the chargeback phase and occurs when a merchant is willing to refund the dispute amount without any further action from customer. Omit the refund_amount and return_shipping_address parameters from the [accept claim](/docs/api/customer-disputes/v1/#disputes-actions_accept-claim) call.
- REFUND_WITH_RETURN . The customer must return the item to the merchant and then merchant will refund the money. This offer type is valid in the chargeback phase and occurs when a merchant is willing to refund the dispute amount and requires the customer to return the item. Include the return_shipping_address parameter in but omit the refund_amount parameter from the [accept claim](/docs/api/customer-disputes/v1/#disputes-actions_accept-claim) call.
- REFUND_WITH_REPLACEMENT . The merchant must do a refund and then send a replacement item to the customer. This offer type is valid in the inquiry phase when a merchant is willing to refund a specific amount and send the replacement item. Include the offer_amount parameter in the [make offer to resolve dispute](/docs/api/customer-disputes/v1/#disputes-actions_make-offer) call.
- REPLACEMENT_WITHOUT_REFUND . The merchant must send a replacement item to the customer with no additional refunds. This offer type is valid in the inquiry phase when a merchant is willing to replace the item without any refund. Omit the offer_amount parameter from the [make offer to resolve dispute](/docs/api/customer-disputes/v1/#disputes-actions_make-offer) call.

- history . An array of history information for an offer.

- communication_details . The contact details that a merchant provides to the customer to use to share their evidence documents.

- communication_details\*.email . The email address that is provided by the merchant where the customer can share the evidences.
- communication_details\*.note . The merchant provided notes that are visible to both the customer and PayPal.
- communication_details\*.time_posted The date and time when the contact details were posted, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6) .

- links . An array of request-related [HATEOAS links](/api/rest/responses/#hateoas-links) :

An array of request-related [HATEOAS links](/api/rest/responses/#hateoas-links) :

- href . The complete target URL. To make the related call, combine the method with this [URI Template-formatted](https://tools.ietf.org/html/rfc6570) link. For pre-processing, include the $ , ( , and ) characters. The href is the key HATEOAS component that links a completed call with a subsequent call.
- rel . The [link relation type](https://tools.ietf.org/html/rfc5988#section-4) , which serves as an ID for a link that unambiguously describes the semantics of the link. See [Link Relations](https://www.iana.org/assignments/link-relations/link-relations.xhtml) .
- method . The HTTP method required to make the related call.
