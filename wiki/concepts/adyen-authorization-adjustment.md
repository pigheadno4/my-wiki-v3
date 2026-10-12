---
title: "Adyen Authorization Adjustment"
type: concept
category: technology
tags: [adyen, authorization-adjustment, pre-authorization, capture, webhooks]
---

## Overview

Adyen authorization adjustment is an online-payments flow for changing the reserved amount on an eligible pre-authorized card or Klarna payment before final capture. It applies only to supported payment methods and Merchant Category Codes, depends on issuer acceptance, and is limited to payments acquired by Adyen.

## Card lifecycle

In the standard card sequence, the merchant pre-authorizes the payment, submits amount updates against the original payment PSP reference, and manually captures after the final intended adjustment. Asynchronous adjustment and capture outcomes are established through webhook events; a request response with a received state is not final outcome evidence. Synchronous card adjustment requires account enablement and successive use of the latest `adjustAuthorisationData` blob.

When Adyen Support has enabled multiple partial captures, a documented card exception permits a partial capture followed by an adjustment of the authorized amount. The issuer determines how many partial captures are possible and can flag multiple partial captures as fraud risk, causing capture failure. This exception does not make an unresolved asynchronous final capture evidence that another adjustment is safe.

## Card constraints and extension

- Each card update expresses the new total authorized amount rather than only the increment.
- Card adjustments cannot use a zero value, and the card-flow section permits at most 50 adjustments per payment; later adjustment requests are declined while capture remains possible up to the last successfully authorized amount.
- Card authorization validity depends on the card scheme. Extension uses an amount update equal to the current authorized balance and remains issuer-dependent. Visa and Discover support only asynchronous extension adjustments, while a Mastercard amount adjustment also extends validity.
- For normal final capture, merchants must finish all intended adjustments before starting capture and use webhook outcomes as the authoritative result; the Support-enabled multiple-partial-capture exception remains separately qualified above.

These limits and scheme-specific extension statements are documented in the card-flow section; the snapshot does not state that they apply to Klarna.

## Klarna path

Klarna is pre-authorized by default and supports only asynchronous authorization adjustment. An authorization can be adjusted while it has not been cancelled, expired or fully captured. After a partial capture, the adjusted amount cannot be below the already captured amount. Increasing the amount triggers another risk assessment or credit lookup; if that rejects the transaction, the customer must place a new order while the original authorization remains valid.

## Sources

- [[source-adyen-docs-online-payments-adjust-authorisation]] - unversioned Adyen website overview, captured 2026-09-15, for authorization types, asynchronous and synchronous adjustment models, payment-method and MCC availability, and scheme-validity warnings

- [[source-adyen-docs-online-payments-adjust-authorisation-adjust-with-preauth]] - unversioned Adyen website guide, captured 2026-09-15, for the card and Klarna pre-authorization adjustment and capture procedure
