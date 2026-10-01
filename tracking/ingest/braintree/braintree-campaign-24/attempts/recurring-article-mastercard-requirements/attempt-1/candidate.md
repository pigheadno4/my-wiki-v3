---
title: "Braintree Mastercard Requirements for Negative Option Billing and Subscriptions"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/recurring-billing/mastercard-requirements"
raw_files:
  - "braintree/articles/guides/recurring-billing/mastercard-requirements-2026-09-16.md"
tags: [braintree, recurring-billing, subscriptions, mastercard, negative-option-billing]
---

## Overview

This collected Braintree article summarizes Mastercard requirements effective September 22, 2022 for certain negative-option billing merchants and merchants using a subscription model. It is an article-level compliance route, not a Braintree SDK or API reference, and its requirements must be applied only to the merchant, trial, product and billing conditions the article states.

## Key takeaways

- The article's pre-expiration reminder rule is limited to negative-option billing merchants who enroll cardholders after a free or low-cost trial longer than seven days for a digital good. Those merchants must send a notice three to seven days before the trial ends, with basic subscription details and cancellation steps.
- For subscription-model merchants offering a service, membership, physical product or digital good, the article requires subscription terms at the point of payment, express cardholder acceptance, and visible price and billing frequency. For negative-option billing, it additionally calls for trial terms, initial charges, trial length, and post-trial price and frequency; the article says these terms cannot be hidden behind a link, embedded in a message box, or made visible only by scrolling.
- After enrollment, the article requires an email or other electronic communication containing the subscription terms and cancellation instructions, plus an electronic receipt after each billing with cancellation instructions. It also requires an online cancellation capability or online cancellation instructions.
- The article warns that Mastercard Standards prohibit subsequent authorization requests for the same primary account number when certain response codes occurred in the original authorization request. It does not enumerate those codes and instead links to Mastercard Standards for details.
- When cardholders are billed less frequently than every six months, the article requires a notice seven to thirty days before the billing date containing the subscription terms and cancellation instructions.

## Applicability and evidence boundaries

> [!warning] Do not generalize the trial reminder
> The three-to-seven-day reminder applies only to the article's defined negative-option billing scenario: enrollment after a free or low-cost trial longer than seven days for a digital good. This source does not state that every subscription or every trial has that reminder window.

> [!warning] Keep external Mastercard details external
> The article states the same-PAN subsequent-authorization restriction only for certain original-authorization response codes and does not list them. Consult the linked Mastercard Standards authority for the applicable codes; do not infer a blanket ban on subsequent authorization requests.

> [!warning] Marketplace and implementation scope
> This article does not address Braintree Marketplace compatibility, SDK methods, request fields, response objects, or merchant enablement. It cannot resolve the existing Marketplace recurring-billing conflict or replace implementation references.

## Detail locators

- Effective date and qualified merchant scope: `# Mastercard Requirements for Negative Option Billing and Subscriptions`, line 16.
- Digital-good negative-option trial definition, longer-than-seven-day condition, reminder window and notice contents: `# Mastercard Requirements for Negative Option Billing and Subscriptions`, line 18.
- Subscription categories covered by the additional requirements: `# Mastercard Requirements for Negative Option Billing and Subscriptions > NOTE`, lines 21-22.
- Point-of-payment terms, express acceptance, disclosure contents and presentation restrictions: `# Mastercard Requirements for Negative Option Billing and Subscriptions`, line 26.
- Post-enrollment communication and per-billing electronic receipt: `# Mastercard Requirements for Negative Option Billing and Subscriptions`, line 28.
- Same-PAN subsequent-authorization warning and external Mastercard Standards route: `# Mastercard Requirements for Negative Option Billing and Subscriptions > NOTE`, lines 31-32.
- Online cancellation or online cancellation-instruction requirement: `# Mastercard Requirements for Negative Option Billing and Subscriptions`, line 36.
- Less-frequent-than-six-month billing notice window and contents: `# Mastercard Requirements for Negative Option Billing and Subscriptions`, line 38.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-recurring-billing]]
- Generic concept: [[recurring-payments]]

## Raw Sources

- [[raw/braintree/articles/guides/recurring-billing/mastercard-requirements-2026-09-16|Braintree Mastercard requirements article]] - complete collected article covering qualified negative-option trial reminders and subscription disclosure, communication, cancellation, authorization-response and infrequent-billing requirements
