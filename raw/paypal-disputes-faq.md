---
title: Disputes frequently asked questions
slug: /docs/disputes/faq/
createTime: "2024-08-15T05:58:06.505Z"
updateTime: "2025-05-12T14:34:24.254Z"
---

# Disputes frequently asked questions

This document answers these common questions from developers:

- [What is the Disputes API?](#what-is-the-disputes-api)
- [Who can create disputes with PayPal?](#who-can-create-disputes-with-paypal)
- [How can a customer file a dispute for a PayPal transaction?](#how-can-a-customer-file-a-dispute-for-a-paypal-transaction)
- [What is the purpose of the Disputes API for merchants?](#what-is-the-purpose-of-the-disputes-api-for-merchants)
- [Are additional fees required to integrate with the Disputes API?](#are-additional-fees-required-to-integrate-with-the-disputes-api)
- [Does the API handle multiple currencies?](#does-the-api-handle-multiple-currencies)
- [Who arbitrates when a customer and merchant cannot reach agreement?](#who-arbitrates-when-a-customer-and-merchant-cannot-reach-agreement)
- [Do merchants need separate logins?](#do-merchants-need-separate-logins)
- [Can a merchant see customer-submitted evidence?](#can-a-merchant-see-customer-submitted-evidence)
- [Is the dispute history retained and accessible?](#is-the-dispute-history-retained-and-accessible)
- [When will the Disputes API be available for all PayPal merchants?](#when-will-the-disputes-api-be-available-for-all-paypal-merchants)
- [Is the dispute phase supported?](#is-the-dispute-phase-supported)
- [How does a merchant know the outcome of a dispute?](#how-does-a-merchant-know-the-outcome-of-a-dispute)
- [Can the dispute lifecycle move to a previous stage?](#can-the-dispute-lifecycle-move-to-a-previous-stage)
- [Is it possible to miss some webhook notifications?](#is-it-possible-to-miss-some-webhook-notifications)
- [Does the return shipping address work for external chargebacks?](#does-the-return-shipping-address-work-for-external-chargebacks)
- [How many disputes or chargebacks can be in a transaction?](#how-many-disputes-or-chargebacks-can-be-in-a-transaction)
- [Does Seller Protection cover chargeback fees?](#does-seller-protection-cover-chargeback-fees)
- [I want to request that the buyer return an item in exchange for a refund. How can I do this with the API?](#i-want-to-request-that-the-buyer-return-an-item-in-exchange-for-a-refund-how-can-i-do-this-with-the-api)
- [Can a dispute or chargeback amount be more than the transaction amount?](#can-a-dispute-or-chargeback-amount-be-more-than-the-transaction-amount)
- [Does the Seller Protection flag in a transaction guarantee Seller Protection for that purchase?](#does-the-seller-protection-flag-in-a-transaction-guarantee-seller-protection-for-that-purchase)
- [What lifecycle stage is a chargeback in?](#what-lifecycle-stage-is-a-chargeback-in)
- [What types of disputes can be escalated?](#what-types-of-disputes-can-be-escalated)
- [Does the dispute ID ever change?](#does-the-dispute-id-ever-change)
- [Who can view evidence submitted?](#who-can-view-evidence-submitted)
- [Where can merchants get the due dates associated with a dispute?](#where-can-merchants-get-the-due-dates-associated-with-a-dispute)
- [Can a closed dispute be reopened?](#can-a-closed-dispute-be-reopened)
- [Where is the final amount of a dispute resolution?](#where-is-the-final-amount-of-a-dispute-resolution)

## What is the Disputes API?

The Disputes API is a REST API that you use to list cases, see dispute details, provide evidence, accept claims, and appeal cases for your PayPal account.

## Who can create disputes with PayPal?

Customers can create and file disputes with PayPal.

## How can a customer file a dispute for a PayPal transaction?

Customers have three ways of filing disputes. For details, see [Disputes, claims, chargebacks, and bank reversals](https://www.paypal.com/us/brc/article/customer-disputes-claims-chargebacks-bank-reversals) .

## What is the purpose of the Disputes API for merchants?

The Disputes API is real time, robust, and supports RESTful-based integrations to search, list, and respond to disputes. Merchants can use the API to list all disputes with PayPal, show details for a dispute, and respond to a dispute. Merchants can use the API to build contextual dispute resolution experiences.

## Are additional fees required to integrate with the Disputes API?

No additional fees are required to integrate with the API as a PayPal customer.

## Does the API handle multiple currencies?

Yes, the API can handle all currencies in countries where PayPal operates.

## Who arbitrates when a customer and merchant cannot reach agreement?

In these situations, PayPal intervenes, adjudicates the case, and applies appropriate seller protection policies. The decision-making process does not change with the Disputes API integration and is consistent across PayPal.

## Do merchants need separate logins?

No. However, you need PayPal REST API application credentials to integrate with PayPal public APIs.

## Can a merchant see customer-submitted evidence?

No. For legal and privacy reasons, a merchant cannot see this information.

## Is the dispute history retained and accessible?

Yes. The PayPal back end maintains this information. However, the merchant cannot access it. If a merchant needs dispute history, the merchant can pull API responses into their systems.

## When will the Disputes API be available for all PayPal merchants?

The Disputes API is available to all merchants as of May 3, 2018.

## Is the dispute phase supported?

Yes. The Disputes API supports both dispute and claim phases.

## How does a merchant know the outcome of a dispute?

The outcome of a resolved dispute is available as the value of the [dispute_outcome](/docs/api/customer-disputes/v1/#definition-dispute_outcome) object.

The following table maps the dispute_outcome value to a win or a loss for a merchant.

| Value                 | Win or loss                                                                                                           |
| --------------------- | --------------------------------------------------------------------------------------------------------------------- |
| RESOLVED_BUYER_FAVOR  | Loss                                                                                                                  |
| RESOLVED_SELLER_FAVOR | Win                                                                                                                   |
| RESOLVED_WITH_PAYOUT  | Win                                                                                                                   |
| CANCELED_BY_BUYER     | Win                                                                                                                   |
| ACCEPTED              | Loss                                                                                                                  |
| DENIED                | Win                                                                                                                   |
| NONE                  | Neither. A dispute was created for the same transaction ID, and the previous dispute was closed without any decision. |
| Empty value           | Neither. The dispute is not resolved yet.                                                                             |

## Can the dispute lifecycle move to a previous stage?

Yes. In most cases, the value of dispute_lifecycle_stage moves from INQUIRY to CHARGEBACK to PRE_ARBITRATION to ARBITRATION . The following scenarios cause the dispute_lifecycle_stage to move to a previous stage:

- When a customer files an external case with their bank or credit card issuer on a dispute, the dispute is updated with a new lifecycle stage.
- When a customer changes the dispute_reason , the dispute is updated with a new lifecycle stage. For example, if the dispute_reason is MERCHANDISE_OR_SERVICE_NOT_RECEIVED and the customer later receives a broken item, the customer can change the dispute_reason to MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED . In that case, the lifecycle stage is reset to CHARGEBACK .

## Is it possible to miss some webhook notifications?

Yes. You must configure a webhook listener and subscribe to all Disputes webhook events. You can subscribe to these dispute-related events:

- CUSTOMER.DISPUTE.CREATE
- CUSTOMER.DISPUTE.RESOLVED
- CUSTOMER.DISPUTE.UPDATED

If you do not subscribe to an event, you do not receive notifications for that event.

For more information about how to configure a webhook listener and subscribe to Disputes webhooks, see [Disputes and Webhooks](/docs/disputes/webhooks/#webhook-details) .

## Does the return shipping address work for external chargebacks?

The return_shipping_address parameter is available in make-offer and accept-claim and works only for PayPal internal MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED cases. The return_shipping_address is not available for external MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED cases. The dispute-channel property indicates whether the case is internal or external.

## How many disputes or chargebacks can be in a transaction?

A transaction can include only one dispute or one chargeback.

## Does Seller Protection cover chargeback fees?

Seller Protection does not cover chargeback fees. See [Seller Protection](https://www.paypal.com/us/brc/article/seller-protection) for more information.

## I want to request that the buyer return an item in exchange for a refund. How can I do this with the API?

Use [make_offer](/docs/api/customer-disputes/v1/#definition-make_offer) to propose an offer to the buyer. To request that the buyer return an item, use REFUND_WITH_RETURN . Do not use provide-evidence to propose offers to the buyer.

**Note:** This is available only for MERCHANDISE_OR_SERVICE_SIGNIFICANTLY_NOT_AS_DESCRIBED cases.

## Can a dispute or chargeback amount be more than the transaction amount?

The dispute or chargeback amount must be equal to or less than the transaction amount.

## Does the Seller Protection flag in a transaction guarantee Seller Protection for that purchase?

A Seller Protection flag in a transaction does not guarantee Seller Protection for that purchase. See the [PayPal User Agreement](https://www.paypal.com/us/webapps/mpp/ua/useragreement-full) for more details about PayPal purchase protection.

## What lifecycle stage is a chargeback in?

A chargeback, by default, is in the claim stage. See [Dispute Lifecycle Stages](/docs/disputes/disputes-reference) for more information about dispute stages.

## What types of disputes can be escalated?

MERCHANDISE_OR_SERVICE_NOT_RECEIVED and MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED disputes are eligible for escalation. UNAUTHORISED disputes are filed as claims, and no escalation is available.

## Does the dispute ID ever change?

No. The same dispute ID is maintained through the life of a transaction for all disputes (internal and external) and for all chargebacks.

## Who can view evidence submitted?

For security reasons, the evidence submitted is viewable only by the party who submitted the evidence. You can view evidence you submitted in the Resolution Center.

## Where can merchants get the due dates associated with a dispute?

To see due dates associated with a dispute, always use the buyer_response_due_date and seller_response_due_date strings in Show_dispute_details .

## Can a closed dispute be reopened?

Yes. A closed dispute can be opened for several reasons, such as the buyer filing an external chargeback.

## Where is the final amount of a dispute resolution?

The final amount of a dispute resolution is available as amount_refunded in the [dispute_outcome](/docs/api/customer-disputes/v1/#definition-dispute_outcome) object.
