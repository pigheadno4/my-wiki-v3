---
title: Disputes Acceptance Test Criteria
slug: /docs/disputes/acceptance-test-criteria/
createTime: "2024-08-15T07:55:48.589Z"
updateTime: "2024-09-23T18:35:32.526Z"
---

# Disputes Acceptance Test Criteria

Learn about the acceptance test criteria to [test your Disputes API integration](/docs/disputes/testing/) .

For concepts, see the [Disputes Overview](/docs/disputes/) .

Terminology:

- **SNAD** . Not as described.
- **NR** . Non-receipt.

## Dispute created webhook

### 1. PayPal SNAD case

The customer chooses a completed transaction to open an SNAD case.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Log in to the [PayPal resolution center](https://sandbox.paypal.com) .

- Open an SNAD case.
- Seller opted in the dispute phase. | The action succeeds and the dispute created webhook is sent. | - The client receives the dispute created webhook.
- The show dispute details call returns the dispute details with the MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED reason.
- The dispute lifecycle stage is INQUIRY . |

### 2. PayPal NR case

The customer chooses a completed transaction to open an NR case.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Log in to the [PayPal resolution center](https://sandbox.paypal.com) .

- Open an NR case.
- Seller opted in the dispute phase. | The action succeeds and the dispute created webhook is sent. | - The client receives the dispute created webhook.
- The show dispute details call returns dispute details with the MERCHANDISE_OR_SERVICE_NOT_RECEIVED reason.
- The dispute lifecycle stage is INQUIRY . |

### 3. PayPal SNAD case

The customer chooses a completed transaction to open an SNAD case.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Log in to the [PayPal resolution center](https://sandbox.paypal.com) .

- Open an SNAD case.
- Seller opts out of dispute phase. | The action succeeds and the dispute created webhook is sent. | - The client receives the dispute created webhook.
- The show dispute details call returns dispute details with MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED reason.
- Dispute lifecycle stage is CHARGEBACK . |

### 4. PayPal NR case

The customer chooses a completed transaction to open an NR case.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Log in to the [PayPal resolution center](https://sandbox.paypal.com) .

- Open an NR case.
- Seller opts out of dispute phase. | The action succeeds and the dispute created webhook is sent. | - The client receives the dispute created webhook.
- The show dispute details call returns dispute details with the MERCHANDISE_OR_SERVICE_NOT_RECEIVED reason.
- Dispute lifecycle stage is CHARGEBACK . |

### 5. PayPal unauthorized dispute case

The customer chooses a completed transaction to open an unauthorized case.

**Note** : When testing unauthorized disputes, the merchant can file the dispute as the buyer. In this case, the buyer and merchant receive different dispute IDs. For merchants, the format and identifiers of the notifications stay the same as other dispute types.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Log in to the [PayPal resolution center](https://sandbox.paypal.com) .

- Open an unauthorized case. | The action succeeds and the dispute created webhook is sent. | - The client receives the dispute created webhook.
- The show dispute details call returns dispute details with the UNAUTHORISED reason. |

### 6. PayPal transaction error dispute case

Six different reason codes apply. The customer opens a transaction error dispute case.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Log in to the [PayPal resolution center](https://sandbox.paypal.com) .

- Open a case with the CREDIT_NOT_PROCESSED , DUPLICATE_TRANSACTION , INCORRECT_AMOUNT , PAYMENT_BY_OTHER_MEANS , CANCELED_RECURRING_BILLING , or OTHER reason code on the completed transaction. | The action succeeds and the dispute created webhook is sent. | - The client receives the dispute created webhook.
- The show dispute details call returns dispute details with CREDIT_NOT_PROCESSED , DUPLICATE_TRANSACTION , INCORRECT_AMOUNT , PAYMENT_BY_OTHER_MEANS , CANCELED_RECURRING_BILLING , or OTHER reason code. |

### 7. The customer cannot open a duplicate dispute for a transaction

The customer cannot open a duplicate dispute for a transaction. After a dispute case is closed, The customer cannot open a dispute on the same transaction again.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute.

- Close the dispute.
- Check whether the buyer can open a dispute for the transaction. | The customer cannot open dispute for the closed transaction. | The customer cannot open a dispute for the closed transaction. |

## Dispute updated webhook

### 8. The customer updates the NR reason code to SNAD

The customer can update the reason code from NR to SNAD.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute NR case on the PayPal side.

- Update the NR reason code to SNAD. | PayPal sends the dispute updated webhook with new reason code. | The client receives the dispute updated webhook from PayPal and updates the reason code accordingly. |

### 9. The customer updates the NR reason code to unauthorized

The customer can update the NR reason code to unauthorized.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute NR case on the PayPal side.

- Update the NR reason code to unauthorized. | PayPal sends the dispute updated webhook with new reason code. | The client receives the dispute updated webhook from PayPal and updates the reason code accordingly. |

### 10. The customer sends message or offer to merchant for NR or SNAD dispute in INQUIRY phase

The dispute lifecycle stage is inquiry. The customer sends a message or offer to the merchant through the resolution center.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute NR case on the PayPal side.

- Send a message or offer through the resolution center. | PayPal sends dispute updated webhook with message or offer details. | The client receives the latest message and or offer details from PayPal and updates its internal system accordingly. |

## Dispute resolved webhook

### 11. The customer cancels dispute

The customer cancels a dispute in resolution center.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Log in to the [PayPal resolution center](https://sandbox.paypal.com) .

- Open a dispute.
- Close the dispute. | The action succeeds and PayPal sends the dispute resolved webhook. | The client receives the dispute resolved webhook. |

### 12. Dispute case close (customer win)

The PayPal agent settles the case in the customer's favor.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Call settle dispute in the sandbox. To settle the case in the customer's favor, set adjudication_outcome to BUYER_FAVOR .

- The show dispute details call returns the outcome. | The action succeeds. | The client receives the dispute resolved webhook. |

### 13. Dispute case close (merchant win)

The PayPal agent settles the case in the merchant's favor.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Call settle dispute in the sandbox. To settle the case in the customer's favor, set adjudication_outcome to SELLER_FAVOR .

- The show dispute details call returns outcome. | The action succeeds. | The client receives the dispute resolved webhook. |

## Provide evidence

### 14. Provide multiple photos, materials with provide evidence API

The client calls provide evidence to provide evidence and materials and upload files for all reason types.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute.

- Call provide evidence to provide materials.

The supported file sizes and formats are:

- The merchant can upload up to 10 MB of files for a case.
- Individual files must be smaller than 5 MB.
- The supported file formats are JPG, GIF, PNG, and PDF. | Each API call succeeds. | Each API call succeeds. |

### 15. Check actions allowed through HATEAOS links and due date based on merchant response due

To determine whether to call provide evidence, accept claim, or appeal dispute, client must check seller response due date in show dispute details.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute.

- Show dispute details. | Each API call succeeds. | If the date exceeds the merchant response due date, the update provides error message. |

### 16. Provide evidence with PROOF_OF_REFUND

PayPal enables the client to provide tracking information for all reason codes.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute on the PayPal side.

- Call provide evidence and update the refund ID to PROOF_OF_REFUND . | Each API call succeeds. | Each API call succeeds. |

### 17. Provide evidence with PROOF_OF_SHIPMENT

PayPal enables the client to provide tracking information for non-receipt, unauthorized, and other cases.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute on the PayPal side.

- Call provide evidence and update tracking information as PROOF_OF_SHIPMENT . | Each API call succeeds. | Each API call succeeds. |

## Accept claim

### 18. The client accepts claim to refund customer requested dispute amount

If the client decides to not dispute the case, client can call accept claim to refund the customer.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute and check whether accept claim is allowed as an action.

- The client calls accept claim. | Each API call succeeds and returns the expected response. | Each API call succeeds and returns the expected response. The client receives the dispute resolved webhook. Refund amount is available in outcome. |

### 19. The client accepts claim to refund customer if customer returns item to specified address (for SNAD) in INQUIRY phase

If case is SNAD, client can call accept claim to make a refund.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute on PayPal Resolution Center.

- Client calls accept claim with return shipping address.
- The customer provides the tracking number through the PayPal Resolution Center.
- The dispute updated webhook is triggered.
- To get tracking information, the client calls show dispute details. | The tracking information is returned in show dispute details. | Client can get tracking information in show dispute details and update the case on their end. |

### 20. The client accepts claim to refund customer if customer returns item to specified address (for SNAD) in CHARGEBACK phase

If case is SNAD, client calls accept claim to make the refund.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute on PayPal Resolution Center and escalate the case to chargeback as a merchant by calling escalate claim.

- Client calls accept claim with return shipping address.
- The customer provides the tracking number through PayPal Resolution Center.
- The dispute updated webhook is triggered.
- Client calls show dispute details to get tracking information. | The show dispute details call shows the tracking information. | The client gets tracking information through the show dispute details call and updates the case on their end. |

### 21. The client accepts to refund customer different amount from dispute amount (partial refund)

If the case is SNAD and the client decides to replace the item to satisfy the customer, client must replace the items and the customer must confirm receipt of the replacement item (no return required from customer)

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute and check whether accept claim is allowed as an action.

- Client calls accept claim with explicit refund amount. | Each API call succeeds and returns expected response. | Each API call succeeds.

If the refund amount is greater or equal to customer-requested dispute amount, the case is resolved and the client receives the dispute resolved webhook.

If the amount is less than customer-requested dispute amount, it triggers an email to customer seeking his or her consent in the resolution center. |

## Appeal dispute

### 22. Call appeal dispute to provide multiple photos, materials

The client calls appeal dispute to provide evidence and materials and upload files for all reason types.

| Test steps      | PayPal actions          | Client actions          |
| --------------- | ----------------------- | ----------------------- |
| Open a dispute. | Each API call succeeds. | Each API call succeeds. |

### 23. Check actions allowed through HATEAOS links and due date based on merchant response due

The client must check merchant response due date in show dispute details to determine whether they must call provide evidence, accept claim, or appeal dispute.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute.

- Call show dispute details. | Each API call succeeds. | If the date exceeds the merchant response due date, update provides error message. |

### 24. Appeal with PROOF_OF_REFUND

PayPal enables client to provide tracking information for all reason codes.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute.

- Resolve the case as BUYER_FAVOR .
- Check whether appeal dispute is allowed in HATEOAS Links.
- Call appeal dispute and upload refund ID under PROOF_OF_REFUND . | Each API call succeeds. | Each API call succeeds. |

### 25. Appeal with PROOF_OF_SHIPMENT

PayPal enables the client to provide tracking information for non receipt, unauthorized, and other cases.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute.

- Resolve the case as BUYER_FAVOR .
- Check whether appeal dispute is allowed in HATEOAS links.
- Call appeal dispute and upload tracking details under PROOF_OF_SHIPMENT . | Each API call succeeds. | Each API call succeeds. |

## Send message

### 26. PayPal SNAD case

The customer chooses a completed transaction to open an SNAD case. The merchant can reply to the customer through
"
send message
"
for that dispute.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Prerequisite. Opt in dispute phase as a merchant.

- Log in to the [PayPal resolution center](https://sandbox.paypal.com) .
- Open an SNAD case.
- Check that send message action is allowed in HATEOAS Links.
- Client calls send message. | Each API call succeeds and the merchant message is visible in show dispute details. | Each API call succeeds and merchant message is visible in show dispute details. |

### 27. PayPal NR case

The customer chooses a completed transaction to open a non receipt case. Merchant can reply to the customer through
"
send message
"
for that dispute.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Prerequisite. Opt in dispute phase as a merchant.

- Log in to the [PayPal resolution center](https://sandbox.paypal.com) .
- Open an SNAD case.
- Check that send message action is allowed in HATEOAS links.
- Client calls send message. | Each API call succeeds and merchant message is visible in show dispute details and message is visible in the resolution center. | Each API call succeeds and merchant message is visible in show dispute details. |

## Make offer

### 28. PayPal SNAD case and refund offer

The customer chooses a completed transaction to open an SNAD case. The merchant can make an offer to the customer to amicably resolve the dispute. Offer type: REFUND only

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Prerequisite. Opt in dispute phase as a merchant.

- Log in to the [PayPal resolution center](https://sandbox.paypal.com) .
- Open an SNAD case.
- Verify that make offer action is allowed in HATEOAS links.
- Client makes offer and shares the amount merchant is willing to refund to the customer as seller_offered_amount and offer type as REFUND . | Each API call succeeds andseller_offered_amountand offer type is visible in show dispute details. | Each API call succeeds andseller_offered_amountis visible in show dispute details. |

### 29. PayPal SNAD case and refund with return offer (no replacement)

The customer chooses a completed transaction to open an SNAD case. The merchant can make an offer to the customer to amicably resolve the dispute. Offer type: REFUND WITH RETURN

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Prerequisite. Opt in dispute phase as a merchant.

- Log in to the [PayPal resolution center](https://sandbox.paypal.com) .
- Open an SNAD case.
- Make offer action is allowed in HATEOAS links.
- Client makes offer and shares the amount merchant is willing to refund to the customer as seller_offered_amount and offer type as REFUND WITH RETURN . | Each API call succeeds andseller_offered_amountand offer type is visible in show dispute details. | Each API call succeeds andseller_offered_amountis visible in show dispute details. |

### 30. PayPal SNAD case and refund with replacement (no return)

The customer chooses a completed transaction to open an SNAD case. Merchant can make an offer to the customer to amicably resolve the dispute. Offer type: REFUND WITH REPLACEMENT

| Test steps                                        | PayPal actions                                                                                    | Client actions                                                                     |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Prerequisite. Opt in dispute phase as a merchant. | Each API call succeeds andseller_offered_amountand offer type is visible in show dispute details. | Each API call succeeds andseller_offered_amountis visible in show dispute details. |

### 31. PayPal NR case

The customer chooses a completed transaction to open a non receipt case. Merchant can make an offer to the customer to amicably resolve the dispute. Offer type: REFUND .

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Prerequisite. Opt in dispute phase as a merchant.

- Log in to the [PayPal resolution center](https://sandbox.paypal.com) .
- Open an SNAD case.
- Make offer action is allowed in HATEOAS links.
- Client makes offer and shares the amount merchant is willing to refund to the customer as seller_offered_amount and the only offer type allowed for NR is REFUND . | Each API call succeeds andseller_offered_amountand offer type is visible in show dispute details. | Each API call succeeds andseller_offered_amountis visible in show dispute details. |

## Escalate claim

### 32. PayPal SNAD case

The customer chooses a completed transaction to open an SNAD case. Merchant escalates the case as he or she cannot come to an amicable resolution with the customer.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Prerequisite. Opt in dispute phase as a merchant.

- Log in to the [PayPal resolution center](https://sandbox.paypal.com) .
- Open an SNAD case.
- Escalate is allowed in HATEOAS links.
- Client escalates claim and shares the merchant's notes with PayPal to view for further action. | Each API call succeeds and dispute lifecycle stage is updated fromINQUIRYtoCHARGEBACKand is visible in show dispute details. Dispute updated webhook is also triggered in the system. | Each API call succeeds and dispute lifecycle stage is updated fromINQUIRYtoCHARGEBACKand is visible in show dispute details. |

### 33. PayPal NR case

The customer chooses a completed transaction to open an SNAD case. The merchant escalates the case as he or she cannot come to an amicable resolution with the customer.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Prerequisite. Opt in dispute phase as a merchant.

- Log in to the [PayPal resolution center](https://sandbox.paypal.com) .
- Open an SNAD case.
- Escalate is allowed in HATEOAS links.
- Client escalates claim and shares the merchant's notes with PayPal to view for further action. | Each API call succeeds and dispute lifecycle stage is updated fromINQUIRYtoCHARGEBACKand is visible in show dispute details. Dispute updated webhook is also triggered in the system. | Each API call succeeds and dispute lifecycle stage is updated fromINQUIRYtoCHARGEBACKand is visible in show dispute details. |

## Other

### 34. Identify unique webhook through webhook ID

Client can use webhook ID in dispute webhook to identify whether this is a duplicated webhook.

| Test steps | PayPal actions | Client actions |
| ---------- | -------------- | -------------- |

| - Open a dispute.

- Listen to dispute webhook. | Each API call succeeds. | Client can identify unique webhook through webhook ID. |
