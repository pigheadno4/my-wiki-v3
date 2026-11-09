---
title: "Stripe Glossary"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/glossary"
raw_files:
  - "stripe-glossary-2026-11-07.md"
  - "stripe-glossary-2025.md"
tags: [stripe, glossary, reference, terminology, payments]
---

## Summary

Dated Stripe terminology reference. The 2026-04-20 capture has 240 two-line entries; the 2026-11-07 capture has 286 one-line entries. The later capture expands some definitions and adds terms across payment APIs, Connect, billing, event delivery, crypto, release phases, and authorization/capture. The format replacement, label normalization, or absence of an older label does not by itself establish deprecation or changed product availability. Use product-specific documentation for implementation and eligibility.

## Key Payment API Terms

| Term | Glossary meaning |
| --- | --- |
| PaymentIntent | API object tracking charge attempts and payment-state changes |
| Setup Intents API | Collects payment-method details for future payments; tracks setup flow and can require authentication |
| PaymentMethods | Customer payment instruments used with Payment Intents or Setup Intents APIs |
| ConfirmationTokens | Capture client-side payment-instrument and shipping data used to confirm a PaymentIntent or SetupIntent |
| client secret | Unique key used with the publishable key to access a single object; object-specific PI, SI, and AccountSession secrets have distinct scopes |
| delayed notification payment method | Cannot immediately return payment status; an order commonly stays pending until success |

The glossary does not make every confirmation a successful charge. The April capture's general webhook definition describes HTTPS JSON delivery; the November event-type entries below add separate payload and version semantics.

## Key Regulatory / Network Terms

| Term | Glossary meaning |
| --- | --- |
| SCA | Strong Customer Authentication; described as affecting many European online payments since September 14, 2019 |
| 3DS / 3DS2 | Card authentication layer; 3DS2 is a main method for European SCA and a mechanism for requesting exemptions |
| liability shift | With some 3DS transactions, fraudulent chargeback liability shifts to the issuer |
| ECI | Code indicating 3DS authentication method and result; may inform liability-shift eligibility |
| e-mandate | Cardholder authorization to issuer for recurring card payments, with registration and authentication requirements in the glossary |
| merchant-initiated transaction | An off-session payment with a properly authenticated saved card **can qualify** for an SCA exemption |
| chargeback | Cardholder's bank debits a business account in response to a dispute, pending resolution |
| dispute inquiry | Issuer's pre-dispute information request, which may or may not escalate |
| AVS | Billing-address information passed to issuers for verification when available |
| CVC | Three- or four-digit card verification code |
| hard / soft decline | Glossary distinguishes an issuer rejection that cannot be retried from one that can; soft decline specifically includes authentication-required cases |

## Key Billing Terms

| Term | Glossary meaning |
| --- | --- |
| billing period | Invoice frequency, independent of service period |
| service period | Usage-measurement period, independent of billing period |
| service interval | Usage-measurement interval resetting independently of billing cadence; present in **both** captures (old lines 590–591; new line 234) |
| metered billing | Subscription billing based on consumption during the billing cycle |
| usage-based billing | Pricing based on usage in a billing period |
| dimensional pricing | In the November glossary, one meter tracks events with attributes such as model type or region, with rates by attribute combination |
| credit based pricing | November definition: credits provide a fixed monetary amount of usage across usage-based products |
| MRR | Monthly Recurring Revenue |
| dunning email | Payment reminder asking a customer to update their payment method |
| minor currency unit | API amount in the currency's smallest unit, for example 1099 for USD 10.99 and 10 for JPY 10 |

## Key Connect Terms

| Term | Glossary meaning |
| --- | --- |
| Connect | Stripe's multi-party routing solution for platforms and marketplaces |
| direct charge | Customer transacts with connected account, which is merchant of record |
| destination charge | Customer transacts with platform for a connected account's goods/services; platform pays Stripe fees and transfers funds |
| separate charges and transfers | Platform charge with separate transfers to one or more connected accounts |
| on_behalf_of | Parameter making connected account merchant of record on an indirect payment |
| merchant of record | Legal entity responsible for facilitating sale and applicable obligations |
| application fee | April glossary: fee a Connect platform collects from a connected account for each payment received. November definition expands this to **each payment or payout**; it does not say every integration collects both fee types. New raw line 24; old raw lines 53–54. |

## Event Delivery Terms (2026-11-07 glossary)

| Term | Definition and limit |
| --- | --- |
| snapshot event | Complete Event object with point-in-time related-resource snapshot. Payload follows the event destination API version and can be stale by processing time (new line 244). |
| thin event | Lightweight notification with event type and IDs of Event and related resource. Retrieve complete event or latest resource state when more data is needed; thin notifications are not API-version-bound (new line 273). |
| webhook | General HTTPS JSON push notification, retained from the older glossary (old lines 719–720; new line 292). This transport definition alone does not define snapshot or thin event behavior. |

## Stablecoin and Other New Vocabulary (2026-11-07 glossary)

The April definition called a stablecoin a cryptocurrency pegged to fiat or another asset to limit volatility (old lines 623–624). The November glossary says Stripe balances use OUSD or USDC while Tempo transfers use USDC.e (new line 248), and distinguishes a stablecoin asset from a balance, custody, and issuance (new lines 249–252). Assets representing the same currency are not necessarily interchangeable because issuers, reserves, availability, and networks can differ. These are dated glossary statements, not independent verification of account or geographic availability.

Other November terms include partial capture (collect part of held amount and release the rest, line 41), frontier APIs (Dashboard opt-in, lower interoperability/extensibility and likely breaking changes, line 116), and Orchestration (Dashboard processor-selection rules, retries, analytics, lines 171 and 260). The glossary is a definition reference and does not replace detailed feature-status or processor-constraint evidence in [[stripe-orchestration]].

## Other Notable Terms

- **IC+**: Network cost plus Stripe fee rather than a flat transaction rate.
- **interchange fee**: Generally paid by the acquiring bank to the issuing bank for card acceptance.
- **payout**: Transfer to an external account, usually a bank account; country and schedule affect timing.
- **settlement currency**: Currency used by the bank account, distinct from presentment currency.
- **Radar**: Stripe fraud detection; Radar for Fraud Teams is described separately.
- **Link**: Stripe digital wallet for saved and autofilled payment/address information.
- **sandbox**: Isolated test environment without effects on the live integration.
- **requires_action / requires_payment_method**: Older API versions before 2019-02-11 used `requires_source_action` / `requires_source`.

## Related Pages

- [[stripe]] — Stripe company page
- [[source-stripe-payment-intents]] — PaymentIntent + SetupIntent lifecycle
- [[source-stripe-payment-methods]] — PaymentMethod API
- [[stripe-orchestration]] — feature-specific Orchestration scope and constraints

## Raw Sources

- [[raw/stripe-glossary-2026-11-07|2026-11-07 glossary, 286 entries]]
- [[raw/stripe-glossary-2025|2026-04-20 glossary, 240 entries]]
