---
title: "Braintree PayPal Recurring Payments (Android v5)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/recurring-payments/android/v5"
raw_files:
  - "braintree/docs/guides/paypal/recurring-payments/android/v5-2026-09-16.md"
tags: [braintree, paypal, android, android-v5, recurring-payments, billing-agreements]
---

## Overview

This collected Android v5-routed [[braintree]] website guide documents client-side creation of a PayPal recurring Billing Agreement through PayPal's Billing Without Purchase Checkout flow and the later Braintree token route for merchant-initiated payments. The page describes merchant-initiated charging based on a schedule or other service-usage criteria and distinguishes subscription, recurring, unscheduled and installment arrangements.

This is a captured Braintree Android v5 website route, not evidence for a sibling platform, a current Android package implementation or support state, the standalone PayPal Android SDK, a direct PayPal Orders API integration, or any successful authorization, charge, settlement or funding outcome. Its PayPal Billing Agreement flow is also distinct from Braintree's separate plan-and-subscription recurring-billing product.

## Key takeaways

- The guide presents a two-stage Billing Without Purchase Checkout flow. After customer checkout creates the Billing Agreement, the returned Payment Token is described as a proxy for the PayPal Billing Agreement ID and should be stored against that customer's account. A later merchant-initiated payment uses that token against the customer's PayPal account.
- The recurring classification must represent the customer's arrangement. During Billing Agreement creation the guide sets the Recurring Indicator through Braintree `plan_type`; during later transactions it uses Braintree `transaction_source`. The clean classification matrix for subscription, recurring, unscheduled and installment arrangements, including first-versus-later transaction values, remains at the verified raw locator rather than being reconstructed here.
- RBA plan information is sent through `plan_metadata` to show a key-information summary on PayPal's Checkout review page. The guide says it is only required during Billing Agreement creation and should not be sent on later merchant-initiated payment requests. Passing `plan_type` without `plan_metadata` still triggers the recurring checkout experience without plan details, and the merchant remains required to communicate the plan terms clearly on its own site before signup completes.
- Merchants must classify transactions as prepaid or postpaid for card-network compliance and contact their Account Manager to enable PREPAID or POSTPAID as the recurring-billing default. This is an account-configuration prerequisite, not proof that a merchant is enabled.
- The Android v5 example constructs `PayPalVaultRequest` with `PayPalRecurringBillingDetails` and a `PayPalRecurringBillingPlanType`. Its dates, amounts, currency, product data, cycle counts and enum comments are illustrative example inputs, not universal requirements or guarantees.
- If the merchant wants to collect a payment and create a Billing Agreement in one checkout session, the page directs it to the separate Checkout with Vault flow. For later payments, the page describes a server-side continuation: save the customer's PayPal account, pass the returned single-use token to Braintree Payment Method Create, and use the returned payment-method token for payment creation. Those handoffs do not themselves prove a completed payment.

> [!warning] Client/server and outcome boundary
> `PayPalVaultRequest` constructs the Android-side Billing Agreement request. The stored Payment Token and later single-use/payment-method-token handoffs cross into Braintree server operations; none of these states alone proves a successful merchant-initiated transaction, settlement or funding. The page's linked JavaScript vault and Ruby request references are navigation, not Android or server implementation evidence fully read for this entry.

> [!warning] Malformed duplicate subsequent-transaction table
> The final table at raw lines 195-200 contains concatenated strings such as `transaction_sourcerecurring`, `recurring_firstrecurring`, `recurring_firstunscheduled` and `recurring_firstinstallment`. Do not infer those strings as literal API values. Use the earlier RBA matrix at lines 76-81 for the page's legible `plan_type` and `transaction_source` classifications, and verify exact request fields against the applicable API reference before implementation.

> [!warning] Product boundary
> This source concerns PayPal Billing Agreements and merchant-initiated PayPal payments. It does not establish Braintree plan/subscription creation, monthly billing-cycle behavior, retry policy or Marketplace compatibility; those belong to the separate [[braintree-recurring-billing]] evidence route.

## Detail locators

- Client-side availability list naming Android v5+: `# Recurring payments > **AVAILABILITY**`, raw lines 17-25.
- Merchant-initiated recurring-payment definition and example categories: `## Overview`, raw lines 30-39.
- Amount, frequency and duration classification table: `## Subscription type details`, raw lines 42-49.
- Two-stage Billing Without Purchase Checkout flow, returned Payment Token storage and later-payment action: paragraph and bullets before `## Create a billing agreement.`, raw lines 51-55.
- Recurring-indicator purpose and creation-versus-subsequent Braintree fields: `#### Recurring indicator`, raw lines 65-67.
- Legible RBA type matrix with `plan_type` and `transaction_source` values: `## RBA type information`, raw lines 72-81.
- RBA plan-information purpose, creation-only condition, `plan_metadata` transport and three presentation choices: `## Recurring Billing Agreement (RBA) plan information`, raw lines 84-101.
- Supported plan-information elements and plan-name customer-comprehension guidance: `## Understanding the RBA data structure` through `## Data element information`, raw lines 106-132.
- Prepaid/postpaid classification and Account Manager enablement condition: `## Integrating flow within Braintree`, raw lines 135-137.
- Illustrative Android `PayPalVaultRequest`, billing-cycle, pricing and recurring-plan-type construction: `## Create the billing agreement > ### kotlin`, raw lines 140-179.
- Separate combined charge-and-agreement route: `## Checkout with Vault`, raw lines 181-183.
- Later-payment server handoff through saved PayPal account, single-use token, Payment Method Create and payment-method token: `## Initiate a payment against the billing agreement:`, raw lines 186-188.
- Duplicate malformed subsequent-transaction table: `## RBA type information during subsequent transactions`, raw lines 191-200.

## Related

- Company: [[braintree]]
- Main integration concept: [[paypal-braintree-integration]]
- Android SDK concept: [[braintree-android-sdk]]
- Separate Braintree subscription concept: [[braintree-recurring-billing]]

## Related raw API references

- [[raw/braintree/docs/guides/paypal/checkout-with-vault/android/v5-2026-09-16|Braintree PayPal Checkout with Vault - Android v5]] - navigation-only route for the combined charge-and-agreement flow; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/paypal/recurring-payments/android/v5-2026-09-16|Braintree PayPal recurring payments for Android v5]] - fully read pinned website snapshot covering Billing Agreement creation, recurring classifications, plan metadata, Android request construction and subsequent-payment handoff
