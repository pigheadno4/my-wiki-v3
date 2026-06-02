<!-- Source URL: https://docs.paypal.ai/growth/disputes -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

A dispute or chargeback occurs when a buyer reports an issue with their transaction, such as non-receipt of an item, receiving an item significantly different from its description, discovering an unauthorized transaction, or identifying a billing error.

PayPal's dispute management provides a clear, structured process to help you resolve these issues fairly and efficiently. It enables you to communicate with buyers, provide supporting evidence, and work toward a fair resolution. This protects your business and maintains buyer trust by giving transparent outcomes.

You can manage disputes using one of these integration options:

- **Resolution Center**: A web-based dashboard where you can view, monitor, and manually respond to disputes.
- **Disputes API**: A programmatic interface that enables you to automate dispute management actions directly from your systems.

<Note>This guide applies to direct merchants and connected integrations where merchants handle disputes and chargebacks and assume financial liability.</Note>

## Key features

- **Structured dispute lifecycle**: Handle disputes efficiently through defined stages from submission to resolution with a clearly defined workflow that minimizes ambiguity and supports efficient, timely resolution.
- **No-code solution**: Simplify dispute handling with Resolution Center, a ready-to-use web interface that requires no technical integration.
- **Automated operations**: Scale dispute management, reduce manual effort, and save time with Disputes API that works seamlessly with your existing systems.
- **Amicable resolution option**: Engage directly with buyers through messaging on our platform to resolve disputes, avoiding escalation and associated fees.

## Understand disputes

You can use the information in this section to get familiar with PayPal's dispute management process. This helps you understand and manage disputes effectively.

### Parties involved in dispute management

The following table outlines the key parties involved and their roles in the dispute management process:

| **Party**           | **Role**                                                                                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Buyer               | Customer who makes a transaction for a product or service and initiates the dispute for that transaction.                                                                                                           |
| Merchant            | Seller who provides the product or service for the transaction. They monitor and respond to disputes.                                                                                                               |
| PayPal              | Payment processor that facilitates the transaction and helps you manage the dispute resolution process.                                                                                                             |
| Bank or card issuer | Bank or financial institution that issued the buyer's payment instrument (for example, debit or credit card). They manage chargebacks and ACH returns.                                                              |
| Card network        | Payment network that facilitates transactions and chargebacks between issuing and acquiring banks. It sets dispute resolution rules and timelines.<br />For example: Visa, Mastercard, American Express, and so on. |
| Partner             | Platform that uses connected integration and onboards merchants through PayPal. In connected integration, merchants assume financial liability and handle disputes and chargebacks.                                 |

### Types of disputes

PayPal classifies disputes into [internal](#internal-disputes) and [external](#external-disputes) disputes based on where they originate and who manages adjudication.

#### Internal disputes

When a buyer files a dispute using the PayPal Resolution Center, it becomes an internal dispute (or internal case). The buyer and merchant can communicate directly through PayPal's platform to resolve the dispute amicably without PayPal's intervention. If they cannot reach an agreement, either party may escalate the dispute to a claim, where PayPal reviews and adjudicates the case based on submitted evidence.

- The buyer has 180 days from the payment date to dispute a transaction.
- PayPal holds the disputed payment until resolution.
- The buyer and merchant have up to 20 days to resolve the disputes amicably. If either party escalates the dispute to PayPal, it will review the case and adjudicate within 10 days based on the evidence from both parties. Both merchants and buyers can appeal unfavorable decisions.

<Note>The buyer can also file a dispute using the PayPal chatbot, IVR, or by calling customer support.</Note>

#### External disputes

When a buyer files a dispute with their bank or card issuer, it becomes an external dispute (or external case). The bank or card issuer manages and adjudicates the outcome. PayPal acts solely as an intermediary to transmit information and evidence between the merchant and the bank or card issuer.

##### Types of external disputes

- **Chargeback**: A chargeback occurs when the buyer disputes a charge with their debit or credit card issuer, who reverses the payment and refunds the buyer.
  <Note>The merchant can also receive a pre-chargeback alert, which is a notification about a potential chargeback. Merchants can issue a refund within 20 hours without fulfilling the order to avoid the chargeback and associated fees.</Note>
- **ACH return**: A bank reversal (or ACH return) occurs when the bank requests PayPal to reverse a payment.

### Dispute lifecycle and stages

Understanding the dispute lifecycle helps you manage disputes more efficiently. Disputes typically progress through these stages:

1. **Inquiry stage**: The buyer files a dispute. PayPal provides a platform for merchants and buyers to resolve disputes directly without its intervention. If the dispute remains unresolved, either party may escalate it to a claim. Item/service not received (INR) or significantly not as described (SNAD) issues begin in the inquiry stage, and if unresolved, may escalate to the claim stage.
2. **Claim stage**: Once the dispute is escalated to a claim, PayPal requests the evidence from both parties, and reviews the submitted evidence. Issues such as billing errors, duplicate charges, or unauthorized transactions are handled directly as claims.
3. **Dispute resolution stage**: For internal disputes, PayPal adjudicates and communicates the resolution to both parties. For external disputes, the bank or card issuer adjudicates the case and communicates the resolution to PayPal.

You can track disputes through these stages, gather relevant information, and respond appropriately to resolve them.

<Note>For detailed information, see <a href="/growth/disputes/handle-disputes/use-disputes-api#understand-dispute-lifecycle-stages" target="_blank" rel="noopener noreferrer">Understand dispute lifecycle stages</a>.</Note>

### Common buyer issues

The following table summarizes the common buyer issues that lead to disputes:

| **Issue**                             | **Description**                                                                                                                                                                                     |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Item not received (INR)               | Buyer claims they ordered and paid for an item or service, but did not receive it.                                                                                                                  |
| Significantly not as described (SNAD) | Buyer received the item, but it does not match the merchant's description. It looks significantly different or has sustained damage during shipping.                                                |
| Billing or subscription errors        | Buyer claims billing or subscription errors, such as duplicate charges, multiple transactions, or incorrect amounts.                                                                                |
| Unauthorized transactions             | Buyer claims: <ul><li>They did not authorize the purchase, and the transaction occurred without their consent.</li><li>They were victims of debit or credit card fraud or identity theft.</li></ul> |
| Request for additional details        | Buyer may require additional transaction details, such as a copy of the transaction or a receipt, to resolve uncertainties or discrepancies.                                                        |
| Misdirected transactions              | Buyer claims the payment went to an incorrect recipient or account.                                                                                                                                 |

## How disputes work

This section provides an overview of the internal and external dispute workflows.

### Internal disputes

![Internal disputes workflow depicting the dispute resolution process at a high level between the buyer, merchant, and PayPal.](assets/paypal-disputes-internal-flow.png)

1. **Buyer**: Files a dispute for a transaction with PayPal.
2. **PayPal**:
   1. Creates a case for the dispute and holds the disputed payment.
   2. Notifies the merchant.
3. **Merchant**:
   1. Reviews the dispute details and gathers necessary information and evidence.
   2. Responds to the dispute. This may include full or partial refunds, offers, supporting information, or escalation of the dispute to a claim.
4. **Buyer**:
   1. Reviews the response.
   2. Accepts the offer or reviews the supporting information and closes the dispute, or rejects it and escalates the dispute to a claim.
5. **PayPal** (if escalated to claim):
   1. Requests evidence from the merchant and buyer.
   2. Adjudicates based on the evidence from both parties.
      - If resolved in the buyer's favor, PayPal refunds the transaction amount.
      - If resolved in the merchant's favor, PayPal releases the hold on the transaction amount.
   3. Updates dispute status and communicates the resolution to the merchant.
6. **Merchant | Buyer**: \[Optional] Appeals the resolution and provides additional evidence for further review.

### External disputes

![External disputes workflow depicting the dispute resolution process at a high level between the buyer, bank or card issuer, merchant, and PayPal.](assets/paypal-disputes-external-flow.png)

1. **Buyer**: Files a dispute for a transaction with the bank or card issuer.
2. **Bank | Card issuer**: Reviews the buyer's claim. If valid, sends a chargeback through the card network to PayPal.
3. **PayPal**:
   1. Creates the dispute case.
   2. Notifies the merchant.
4. **Merchant**:
   1. Reviews the dispute details.
   2. Responds to the dispute by issuing a refund or submitting evidence to PayPal.
5. **PayPal**: Forwards the merchant's response through the card network to the bank or card issuer.
6. **Bank | Card issuer**:
   1. Reviews and adjudicates based on the evidence from both parties.
      - If resolved in the buyer's favor, the bank or card issuer refunds the transaction amount.
      - If resolved in the merchant's favor, the bank or card issuer reverses the transaction amount.
   2. Communicates the resolution through the card network to PayPal.
7. **PayPal**: Updates dispute status and notifies the merchant.

## Additional information

[Article on disputes, claims, chargebacks, and bank reversals](https://www.paypal.com/brc/article/customer-disputes-claims-chargebacks-bank-reversals)
