---
title: Disputes lifecycle stages reference
slug: /docs/disputes/disputes-reference/
createTime: "2024-08-15T07:50:36.678Z"
updateTime: "2025-05-12T11:12:02.483Z"
---

# Disputes lifecycle stages reference

## Dispute lifecycle stages

To understand the dispute management flow, learn about the dispute lifecycle stages:

- [Dispute lifecycle stages](#dispute-lifecycle-stages) - [Inquiry stage](#inquiry-stage)
- [Claim stage](#claim-stage)
- [Settlement

                     stage](#settlementstage)

- [Dispute management flow](#dispute-management-flow)
- [Available actions by stage](#available-actions-by-stage)

### Inquiry stage

The inquiry stage occurs immediately after a customer initiates a dispute by reporting a problem in the Resolution Center. The customer and merchant attempt to resolve the dispute for a 20-day period without escalation to PayPal.

The dispute_lifecycle_stage is INQUIRY .

### Claim stage

If the customer and merchant cannot resolve the dispute within the 20-day inquiry period, the customer or merchant can escalate the dispute to PayPal. The dispute then enters the claim stage.

The dispute_lifecycle_stage is one of these values:

- CHARGEBACK . A customer or merchant escalates an inquiry to a claim, which authorizes PayPal to investigate the case and make a determination.

After the dispute enters this phase, all notes that the customer sends are visible to PayPal agents only. The customer must wait for PayPal’s response before he or she can take further action. PayPal shares dispute details with the merchant, who can accept the customer's claim, submit evidence to challenge the customer's claim, or make an offer to resolve the dispute.

**Note:** The chargeback stage is a PayPal dispute lifecycle stage and is not a credit card or debit card chargeback.

- PRE_ARBITRATION . The first appeal stage for merchants. A merchant can appeal a chargeback if a decision is not in the merchant's favor. If the merchant does not appeal within the appeal period, the case is considered resolved.

- ARBITRATION . The second appeal stage for merchants. A merchant can appeal a dispute for a second time if the first appeal was denied. If the merchant does not appeal within the appeal period, the case returns to a resolved status in pre-arbitration stage.

### Settlement

     stage

To resolve the claim, PayPal considers the submitted evidence and settles the dispute in either the customer's or merchant's favor and communicates the outcome of the dispute to the bank, if involved, and the merchant and customer.

The dispute_lifecycle_stage is one of these values: INQUIRY , CHARGEBACK , PRE_ARBITRATION , or ARBITRATION .

- OPEN . The dispute is open. The buyer actions available are validate-eligibility , send-message , escalate , cancel , and change reason . After the seller has provided an offer, the buyer actions available are accept-offer and deny-offer . The seller actions available are send-message , make-offer , accept-claim , escalate , and partial-update .

- UNDER_REVIEW . The dispute is under review with PayPal. In this case, the buyer and seller do not have any actions available.

- RESOLVED . The dispute is resolved. In this case, the buyer and seller do not have any actions available.

- WAITING_FOR_BUYER_RESPONSE . The dispute is waiting for a response from the buyer. The buyer actions available are provide-evidence and cancel .

- WAITING_FOR_SELLER_RESPONSE . The dispute is waiting for a response from the seller. The seller actions available are provide-evidence , accept-claim , and acknowledge-return-item .

## Dispute management flow

A dispute can be resolved in the inquiry stage or the claim stage. When a dispute is resolved, it enters the settlement stage.

![Dispute,management,flow](assets/paypal-disputes-state-machine.svg)

## Available actions by stage

The actions that are available to the seller and buyer vary during the stages of a dispute. The following table shows the actions that are available to the buyer and seller during the stages of a dispute. Refer to the [HATEOAS links](/api/rest/responses/#hateoas-links) to determine actions available for the dispute.

**Important:** These actions are available only in the [sandbox](/docs/disputes/integration-guide/#sandbox-only-methods) : settle dispute , create dispute , and update dispute status .

| Stage                                                                            | Seller actions                                                                                 | Buyer actions |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------- |
| Gathering information                                                            | - [List disputes](/docs/disputes/integration-guide/#list-disputes)                             |
| - [Show dispute details](/docs/disputes/integration-guide/#show-dispute-details) | - [List disputes](/docs/disputes/integration-guide/#list-disputes)                             |
| - [Show dispute details](/docs/disputes/integration-guide/#show-dispute-details) |
| Inquiry                                                                          | - [Send message to other party](/docs/disputes/integration-guide/#send-message-to-other-party) |

- [Make offer to resolve dispute](/docs/disputes/integration-guide/#make-offer-to-resolve-dispute)
- [Escalate dispute to a claim](/docs/disputes/integration-guide/#escalate-dispute-to-claim)
- [Acknowledge returned item](/docs/api/customer-disputes/v1/#disputes-actions_acknowledge-return-item) | - [Send message to other party](/docs/disputes/integration-guide/#send-message-to-other-party)
- [Accept offer to resolve dispute](/docs/api/customer-disputes/v1/#disputes-actions_accept-offer)
- Cancel a dispute
- Change the reason for a dispute
- [Deny an offer to resolve a dispute](/docs/api/customer-disputes/v1/#disputes-actions_deny-offer)
- [Escalate dispute to a claim](/docs/disputes/integration-guide/#escalate-dispute-to-claim) |
  | Claim | - [Accept claim](/docs/disputes/integration-guide/#accept-claim)
- [Provide evidence](/docs/disputes/integration-guide/#provide-evidence)
- [Provide supporting information for dispute](/docs/api/customer-disputes/v1/#disputes-actions_provide-supporting-info)
- [Appeal dispute](/docs/disputes/integration-guide/#appeal-dispute) | - [Accept offer to resolve dispute](/docs/api/customer-disputes/v1/#disputes-actions_accept-offer)
- [Provide evidence](/docs/disputes/integration-guide/#provide-evidence)
- [Provide supporting information for dispute](/docs/api/customer-disputes/v1/#disputes-actions_provide-supporting-info)
- Cancel a dispute
- Change the reason for a dispute
- [Deny an offer to resolve a dispute](/docs/api/customer-disputes/v1/#disputes-actions_deny-offer) |
