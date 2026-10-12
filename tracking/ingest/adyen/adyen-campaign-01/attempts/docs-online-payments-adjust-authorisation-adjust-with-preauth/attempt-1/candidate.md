---
title: "Adyen Docs: Adjust an authorization with pre-authorization"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/adjust-authorisation/adjust-with-preauth"
raw_files:
  - "adyen/docs/online-payments/adjust-authorisation/adjust-with-preauth/2026-09-15.md"
tags: [adyen, authorization-adjustment, pre-authorization, capture, webhooks, klarna]
---

## Overview

This Adyen online-payments guide describes how to pre-authorize, adjust and manually capture card payments, plus the distinct asynchronous adjustment path for Klarna. It is a procedural website snapshot collected on 2026-09-15; the exact request fields, response examples and SDK snippets remain in the pinned raw page.

The snapshot does not prove current availability, issuer approval, Merchant Category Code eligibility, account configuration, authorization extension, adjustment success or capture success.

## Key takeaways

- The card flow begins with a pre-authorization, uses the original payment PSP reference for later amount-update and capture requests, and requires manual capture after the final adjustment. The merchant must decide when to use the flow and calculate each new amount.
- An amount update supplies the new total authorized amount, not merely the increment. Asynchronous adjustment returns a received request state and requires an `AUTHORISATION_ADJUSTMENT` webhook for the result. Synchronous adjustment requires account enablement and the latest `adjustAuthorisationData` blob for each successive update.
- Capture remains asynchronous and must be confirmed from webhook events. Completing a capture request or receiving its immediate response does not establish that funds were captured.
- Adjustment support is limited by payment method, MCC, issuer decision and Adyen acquisition. Authorizations expire according to card-scheme validity; adjustment requests cannot use a zero value and are capped at 50 per payment.
- Authorization extension uses an amount update equal to the current authorized balance. Adyen recommends the asynchronous path for extension because Visa and Discover only support asynchronous extension adjustments; issuer refusal ends the initially authorized payment, while Mastercard amount adjustment also extends validity.
- Klarna is pre-authorized by default and supports only asynchronous authorization adjustment. Increasing its authorization triggers another risk assessment or credit lookup; rejection requires a new order while the original authorization remains valid.

## Material boundaries

> [!warning] Eligibility and issuer outcome
> The guide limits authorization adjustment to supported payment methods and MCCs, payments acquired by Adyen, and issuer acceptance. Documentation of the flow is not proof that a particular merchant, payment or issuer supports it.

> [!warning] Webhook-authoritative outcomes
> Use the required webhook events to determine asynchronous adjustment and capture outcomes. Immediate request acceptance or a `received` response is not final authorization or capture proof.

> [!warning] Capture sequencing
> Finish all intended adjustments before capture. Because capture is asynchronous, an apparently still-adjustable authorization must not be treated as permission to submit another adjustment after capture has started.

## Detail locators

- Scope, webhook reliance and merchant-owned decision/amount logic: opening guidance, raw lines 26-34.
- Integration, webhook, availability, expiry and Adyen-acquisition requirements: `## Requirements`, raw lines 36-48.
- Synchronous account enablement, manual capture and multiple-partial-capture setup: `## (Optional) Configure your account`, raw lines 50-56.
- Pre-authorization request markers and values retained for adjustment/capture: `## 1. Pre-authorize a payment`, raw lines 58-135.
- Asynchronous and synchronous amount-update request/response paths: `## 2. Adjust the pre-authorized amount`, raw lines 137-703.
- Fifty-adjustment limit, zero-value restriction and extension behavior: `### Limitations` and `### Extend the authorization`, raw lines 705-723.
- Manual capture sequencing, request/response and webhook outcome: `## 3. Capture the payment`, raw lines 725-1030.
- Multiple partial-capture issuer/fraud qualification: `### Partial captures`, raw lines 1032-1040.
- Klarna-specific asynchronous adjustment, risk reassessment and capture path: `## Adjust a Klarna authorization`, raw lines 1042-2043.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-authorization-adjustment]]

## Raw Sources

- [[raw/adyen/docs/online-payments/adjust-authorisation/adjust-with-preauth/2026-09-15|Adyen Docs: Adjust an authorization]] - complete collected guide for card and Klarna pre-authorization adjustment and capture
