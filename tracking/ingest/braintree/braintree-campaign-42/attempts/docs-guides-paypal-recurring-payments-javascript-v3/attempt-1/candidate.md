---
title: "Braintree PayPal Recurring Payments - JavaScript v3"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/recurring-payments/javascript/v3"
raw_files:
  - "braintree/docs/guides/paypal/recurring-payments/javascript/v3-2026-09-16.md"
tags: [braintree, paypal, recurring-payments, billing-agreements, javascript-v3]
---

## Overview

This collected [[braintree]] website guide is the JavaScript v3 client-integration route for PayPal recurring payments through PayPal Billing Agreements and the Billing Without Purchase Checkout flow. It describes creating the agreement and retaining its returned Payment Token, then using that agreement-derived credential in a later merchant-initiated payment path. It is not the Braintree plan-and-subscription recurring-billing engine, a direct PayPal Orders API integration, exact-version `braintree-web` implementation evidence, proof of current account enablement, or proof that a payment was created or completed.

## Key takeaways

- The page classifies recurring billing arrangements by amount, frequency and duration, then presents the PayPal Billing Without Purchase Checkout flow as two stages: create a Billing Agreement and receive a Payment Token associated with the customer; later use the token to initiate payments against that PayPal account. This is a merchant-initiated later-payment model, not an on-page subscription scheduler.
- The recurring indicator has different Braintree fields at different stages: `plan_type` during Billing Agreement creation and `transaction_source` during subsequent transactions. The page says the chosen arrangement type represents the customer's agreement to payment networks for compliance purposes; use the exact type/value matrix in the raw locator rather than generalizing one arrangement's values to another.
- RBA plan information is creation-time checkout disclosure. Passing `plan_type` with `plan_metadata` triggers the recurring checkout experience with plan details; passing only `plan_type` triggers a generic recurring experience and leaves the merchant responsible for clearly communicating terms on its own site; passing neither produces the non-recurring experience and is not recommended by the page for recurring transactions. The page says not to send RBA plan information again in later merchant-initiated payment requests.
- The guide requires merchants to classify transactions as prepaid or postpaid and directs them to an Account Manager to enable PREPAID or POSTPAID as the recurring-billing default. This is a setup requirement stated by the snapshot, not evidence that a merchant is enabled.
- The JavaScript examples show browser-side Billing Agreement creation and approval tokenization, followed by a merchant-server handoff. The later-payment section says the customer PayPal account must first be saved, passes the returned single-use token to Braintree Payment Method Create, and uses the returned payment-method token for payment creation. These snippets and links describe the documented handoff; they do not prove vault persistence, authorization, capture, settlement or a complete runnable integration.

## Evidence boundaries

> [!warning] JavaScript v3 website snapshot
> The URL and page body are scoped to JavaScript v3 client integration, while the availability box also names other platform major versions. This 2026-09-16 collection does not establish current SDK lifecycle, an exact `braintree-web` release, merchant eligibility, PayPal runtime behavior or support for a sibling integration.

> [!warning] PayPal agreement versus Braintree subscriptions
> This page's recurring subject is a PayPal Billing Agreement plus later merchant-initiated payments. Do not treat it as evidence for Braintree plan creation, subscription scheduling, retries, proration or subscription-status transitions.

> [!warning] Example and extracted-table limits
> The page contains separate `flow: 'checkout'` and `flow: 'vault'` examples, and its final repeated subsequent-transaction table contains concatenated identifiers such as `transaction_sourcerecurring` and `recurring_firstrecurring`. Do not merge the examples into one guaranteed request or derive field values from the malformed repeated table; use the earlier RBA type table and verify current implementation requirements before coding.

## Detail locators

- Client-side availability wording and the page's comparison with Vaulted Payments: `# Recurring payments > AVAILABILITY`, lines 17-25.
- Recurring-payment definition, examples and arrangement categories: `## Overview`, lines 30-39, and `## Subscription type details`, lines 44-53.
- Billing Without Purchase Checkout identity and its agreement-creation/later-payment stages: `## Subscription type details`, lines 55-59.
- Recurring-indicator purpose, stage-specific fields and the clean arrangement type/value matrix: `#### Recurring indicator`, line 71, and `## RBA type information`, lines 76-85.
- Creation-time RBA plan-information purpose and the three checkout-experience choices: `## Recurring Billing Agreement (RBA) plan information`, lines 88-105.
- Supported plan-information categories, plan-name customer-facing guidance and the page's data-element table: `## Understanding the RBA data structure`, lines 110-140.
- Prepaid/postpaid classification and Account Manager enablement instruction: `## Integrating flow within Braintree`, lines 143-145.
- Checkout-style request example with `requestBillingAgreement`, `planType` and `planMetadata`: `## Merchant Integration`, lines 148-199.
- Vault-style Billing Agreement creation, PayPal button callbacks, approval tokenization and nonce-to-server comment: `## Create the billing agreement`, lines 201-259.
- Saving the PayPal account, later Payment Token use, single-use-token-to-Payment-Method-Create handoff and returned token role: `## Initiate a payment against the billing agreement`, lines 262-264.
- Repeated subsequent-transaction table, including its concatenated identifier text: `## RBA type information during subsequent transactions`, lines 267-276.

## Related

- Company: [[braintree]]
- Main recurring-billing route: [[braintree-recurring-billing]]
- PayPal-through-Braintree client/server boundary: [[paypal-braintree-integration]]
- JavaScript SDK context: [[braintree-web-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/recurring-payments/javascript/v3-2026-09-16|Braintree PayPal Recurring Payments - JavaScript v3]] - complete collected guide covering Billing Agreement creation, recurring checkout disclosure, client tokenization and the later merchant-initiated payment handoff
