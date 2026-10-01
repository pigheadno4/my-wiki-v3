---
title: "Braintree Recurring Billing Advanced Settings"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/recurring-billing/recurring-advanced-settings"
raw_files:
  - "braintree/articles/guides/recurring-billing/recurring-advanced-settings-2026-09-16.md"
tags: [braintree, recurring-billing, subscriptions, retries, proration]
---

## Overview

This Braintree article is the retrieval entry for Control Panel advanced settings that govern automatic retries of failed recurring-billing transactions and proration of mid-cycle subscription price changes. It preserves the conditions and consequential balance, retry, charge and credit effects needed to select the right section, while leaving the full decline-code table, worked calculations and setup steps in the pinned raw page.

## Key takeaways

- For a transaction with status `FAILED`, the article describes three built-in automated retries before the subscription is marked `Past Due`, with up to two days before all three finish. A transaction rendered as `PROCESSOR*DECLINED` or `GATEWAY_REJECTED` in the collected page instead changes the subscription to `Past Due` immediately. After that status, Braintree tries billing at least twice more; the Control Panel can set the interval for those retries and choose whether later failure cancels the subscription, continues retries, or leaves it past due.
- Choosing to leave the subscription past due stops additional retries and transaction attempts while the past-due balance continues to accrue each billing cycle. The first two post-`Past Due` retries apply only in the cycle when that status begins; choosing continued retries produces one attempt per later billing cycle on the usual billing date.
- A successful manual retry, regardless of its amount, reduces the subscription balance to zero. A failed manual retry does not count as an automatic retry attempt, so scheduled automatic retry logic still runs. Separately, the article warns that processor-declined transactions are not all automatically retried; the complete excluded-code table remains in the raw page.
- Proration can immediately charge or credit a customer for a mid-cycle subscription price change according to the days remaining; without proration, the change begins with the next cycle. The elapsed-day count updates daily at midnight in the gateway account's Control Panel time zone.
- Applying an add-on or discount mid-cycle with proration enabled affects the specified subsequent cycles and also charges or discounts the prorated remainder of the current cycle. The per-subscription Control Panel option overrides the gateway's general recurring-billing proration settings.
- For an upgrade, enabled proration immediately charges the prorated increase. If that charge fails, a Control Panel option determines whether the subscription and balance remain unchanged or the new subscription price is kept and the failed prorated amount is added to the balance. A prorated downgrade instead creates a subscription-balance credit; it does not refund the payment method. If the downgrade creates a negative balance, the payment method is not charged until the balance exceeds $0.

## Detail locators

- Initial retry sequence, immediate `Past Due` conditions and post-`Past Due` retry policy: `## Automatic retries`, lines 19-21.
- Control Panel setup steps and the two 1-to-10-day interval settings: `### Setting up retry logic` through `#### If above retry fails, try again after...`, lines 24-49.
- Final-failure choices, balance accrual, billing-cycle timing and manual-retry consequences: `#### If above retries have failed...`, lines 52-73.
- Complete worked retry chronology: `Retry logic example`, lines 77-119.
- Non-retried decline qualification and full code table: `### Handling declines`, lines 124-213.
- General proration timing, account-time-zone boundary, and upgrade-versus-downgrade definitions: `## Proration`, lines 215-225.
- Add-on and discount duration, current-cycle caution, avoidance options and per-subscription override: `### Proration with add-ons and discounts`, lines 228-244.
- Upgrade configuration, immediate prorated charge and worked calculation: `### Enable proration on upgrades`, lines 249-321.
- Failed-upgrade-proration setting and its two subscription/balance outcomes: `### If the charge for a prorated amount fails`, lines 326-334.
- Downgrade credit behavior, no-payment-method-refund warning and worked balance chronology: `### Enable proration on downgrades`, lines 337-477.

## Evidence limitations

> [!warning] Retry and applicability boundaries
> Do not treat the configured retry sequence as a guarantee that every decline is retried or that collection eventually succeeds. The article excludes some processor decline codes and routes their complete table from the raw page. It documents recurring-billing settings but does not establish Braintree Marketplace compatibility, current merchant enablement, or behavior outside the stated subscription and Control Panel conditions.

> [!warning] Balance effects are not refunds
> A successful manual retry can zero the subscription balance even when the retry amount is smaller than the amount owed. A downgrade proration is applied as a gateway subscription-balance credit rather than a refund to the customer's payment method; a refund requires a separate transaction.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-recurring-billing]]
- Generic concept: [[recurring-payments]]
- Existing guide route: [[source-braintree-recurring-billing-manage-node]]
- Existing decline authority: [[source-braintree-authorization-responses]]

## Raw Sources

- [[raw/braintree/articles/guides/recurring-billing/recurring-advanced-settings-2026-09-16|Braintree Advanced Settings article]] - complete collected page covering automatic retry configuration, excluded decline codes, proration controls, failure handling, and upgrade and downgrade examples

## Related raw API references

- [[raw/braintree/articles/guides/recurring-billing/subscriptions-2026-09-16|Subscriptions article]] - unread navigation-only route for direct subscription updates
- [[raw/braintree/articles/guides/recurring-billing/add-ons-discounts-2026-09-16|Add-ons and discounts article]] - unread navigation-only route for recurring-billing add-on and discount behavior
- [[raw/braintree/docs/reference/general/processor-responses/authorization-responses-2026-09-16|Authorization responses]] - unread navigation-only processor-response and recurring-transaction retry authority
- [[raw/braintree/articles/control-panel/transactions/create-2026-09-16|Create transactions in the Control Panel]] - unread navigation-only route for a separate transaction outside a subscription
