---
title: "Braintree Subscription Retry Charge (Node.js)"
type: source
date_ingested: 2026-09-21
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/subscription/retry-charge/node"
raw_files:
  - "braintree/docs/reference/request/subscription/retry-charge/node-2026-09-16.md"
tags: [braintree, node-js, subscriptions, retry-charge, settlement]
---

## Overview

This Braintree Node.js request reference documents manually retrying a charge for a past-due subscription through `gateway.subscription.retryCharge()`. Its displayed callback and Promise variants show an explicit amount and two settlement-handling shapes.

## Key takeaways

- The page scopes this operation to manually retrying charges for subscriptions that are past due. It does not establish automatic retry behavior, a schedule, a subscription status transition, or a successful billing lifecycle.
- The displayed calls pass `subscription.id` and the explicit string amount `"24.00"`. The page does not state a currency, whether another amount is permitted, whether the amount may be omitted or defaulted, or whether it represents the complete past-due balance.
- The opening callback and Promise examples also pass an unlabeled third argument of `true` and show `result.success` as `true`. This page does not define that boolean in prose or state that the success flag proves settlement or payment finality.
- Under **Manually submit transaction for settlement**, the examples call `retryCharge()` without the third argument. Only after `retryResult.success` is true do they pass `retryResult.transaction.id` to `gateway.transaction.submitForSettlement()`; the nested result again shows `success` as true. This documents the displayed manual-submission sequence, not eventual settlement completion or any further subscription lifecycle effect.

## Detail locators

- Past-due and manual-retry scope plus the linked managing-subscriptions guide: `# Subscription: Retry Charge`, lines 13-17.
- Callback form with explicit amount, unlabeled `true`, and displayed result flag: `### Callback`, lines 18-28.
- Promise form with the same explicit arguments and displayed result flag: `### Promise`, lines 30-39.
- Separate callback settlement submission using the retry transaction ID: `## Examples > ### Manually submit transaction for settlement > ### Callback`, lines 41-63.
- Separate Promise settlement submission using the retry transaction ID: `## Examples > ### Manually submit transaction for settlement > ### Promise`, lines 65-79.

## Evidence limitations

> [!warning] Example-only argument and outcome semantics
> The collected page does not label the third `retryCharge()` argument, define an amount default or currency, show a failure response, provide transaction fields beyond the ID used in the settlement call, or state a final settlement status. Consult the linked raw page and dedicated transaction/subscription authorities for details not established here.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/request/subscription/retry-charge/node-2026-09-16|Braintree Node.js subscription retry-charge reference]] - complete page covering the past-due manual-retry scope, explicit example amount, result access, and displayed settlement-submission sequence
