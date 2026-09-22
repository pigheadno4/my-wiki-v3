---
title: "Braintree Recurring Billing: Manage Subscriptions (Node.js)"
type: source
date_ingested: 2026-09-22
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/recurring-billing/manage/node"
raw_files:
  - "braintree/docs/guides/recurring-billing/manage/node-2026-09-16.md"
tags: [braintree, node-js, recurring-billing, subscriptions, proration, retries, refunds]
---

## Overview

This Braintree Node.js guide is the retrieval entry for managing subscriptions after creation. It covers status-dependent update eligibility, price and payment-method consequences, proration behavior, past-due balances and retries, settlement handling for manual retries, and transaction-based refunds. Exact request shapes and worked examples remain in the pinned raw guide or the linked dedicated references.

## Key takeaways

- Pending and Active subscriptions are eligible for the guide's listed updates. Canceled and Expired subscriptions cannot be changed, while a Past Due subscription can update only fields that do not change price: subscription ID, payment method, merchant account, and descriptor.
- When a plan changes, the subscription does not inherit the new plan's price if billing frequency stays the same, but it does inherit the new price if billing frequency changes; an explicitly supplied price can override either case. Updating the merchant account may also change processing currency. EU merchants must give four weeks' notice before a recurring-plan price change and before billing after six or more months without a payment.
- Deleting a payment method by its token immediately cancels associated subscriptions and forfeits already-paid remaining days. Updating a Past Due subscription's payment method automatically retries it only when proration is enabled.
- With proration, a mid-cycle price change may charge or credit the customer, adjusts the amount based on the days remaining, and applies the newly calculated amount immediately; without it, the change begins next cycle. By default a failed proration charge prevents the subscription update, unless the merchant configures the update to continue and add the failed prorated amount to the balance.
- Past-due balances grow with failed recurring charges. Braintree attempts a charge at the start of each new billing cycle, permits configured retries between cycles, and says some decline codes are not retried. A successful manual retry always reduces the subscription balance to zero regardless of the retry amount.
- The guide says automatic submit-for-settlement on a retry is supported by the latest server SDK versions, while older versions require a separate settlement submission; it names no concrete version. Authorization returns the subscription to Active unless its billing cycles are exhausted, in which case it becomes Expired.
- A subscription refund is issued against an existing sale transaction that is Settled or Settling, and may be partial. Refunding does not itself stop future subscription charges; cancellation is a separate action.

## Detail locators

- Eligible update fields, EU notice, Node callback/Promise forms, missing-subscription route, and Canceled/Expired limits: `# Manage subscription scenarios > ## Updating subscriptions`, lines 20-62.
- Plan-price inheritance, payment-method update scope and deletion cascade: `## Updating subscriptions > ### Plans` and `### Payment methods`, lines 65-80.
- Add-on/discount add-update-remove scope, one-addition rule, and worked Node examples: `### Add-ons and discounts`, lines 83-168.
- Proration timing, Control Panel or request-option configuration, failure behavior, and add-on/discount qualifications: `### Proration`, lines 169-184.
- Merchant-account currency consequence and Past Due balance accumulation: `### Merchant accounts` through `## Past Due subscriptions`, lines 185-198.
- Past Due update restrictions, automatic/custom retry behavior, decline qualification, and balance timing: `### Updating Past Due subscriptions` and `### Retry logic`, lines 199-220.
- Negative-balance behavior: `### Negative balance`, lines 221-223.
- Manual retry amount behavior, settlement-version qualification, and resulting subscription status: `## Retrying transactions manually`, lines 224-242.
- Transaction-status requirement, partial-refund route, and separate cancellation action: `## Refunding a subscription`, lines 243-252.

## Evidence limitations

> [!warning] Guide scope and version boundary
> The page links to dedicated update, retry, decline-response, refund, cancellation, and advanced-settings authorities for request details and scenarios. Those unread references are navigation only here. The phrase `latest versions of our server SDKs` is preserved as collected wording and does not identify a Node SDK version or prove settlement completion.

## Related

- Company: [[braintree]]
- Concepts: [[recurring-payments]], [[braintree-server-sdk]]
- Existing operation routes: [[source-braintree-subscription-update-node]], [[source-braintree-subscription-retry-charge-node]], [[source-braintree-transaction-refund-node]], [[source-braintree-payment-method-delete-node]], [[source-braintree-subscription-cancel-node]]

## Raw Sources

- [[raw/braintree/docs/guides/recurring-billing/manage/node-2026-09-16|Braintree Recurring Billing Manage guide for Node.js]] - complete collected guide covering subscription updates, proration, past-due balances, retry handling and refunds

## Related raw API references

- [[raw/braintree/docs/guides/recurring-billing/overview-2026-09-16|Recurring Billing overview]] - unread navigation-only status definitions linked by the guide
- [[raw/braintree/docs/reference/request/subscription/update/node-2026-09-16|Subscription Update (Node.js)]] - unread navigation-only request reference for exact update fields and options
- [[raw/braintree/articles/guides/recurring-billing/recurring-advanced-settings-2026-09-16|Advanced recurring-billing settings]] - unread navigation-only detailed proration, retry and decline scenarios
- [[raw/braintree/docs/reference/request/subscription/retry-charge/node-2026-09-16|Subscription Retry Charge (Node.js)]] - unread navigation-only manual-retry request reference
- [[raw/braintree/docs/reference/general/processor-responses/authorization-responses-2026-09-16|Authorization responses]] - unread navigation-only rules for retrying declined recurring transactions
- [[raw/braintree/docs/reference/request/transaction/refund/node-2026-09-16|Transaction Refund (Node.js)]] - unread navigation-only refund request reference
- [[raw/braintree/docs/reference/request/payment-method/delete/node-2026-09-16|Payment Method Delete (Node.js)]] - unread navigation-only deletion operation linked by the cascade warning
- [[raw/braintree/docs/reference/request/subscription/cancel/node-2026-09-16|Subscription Cancel (Node.js)]] - unread navigation-only cancellation request reference
