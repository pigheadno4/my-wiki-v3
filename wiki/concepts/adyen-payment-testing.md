---
title: "Adyen Payment Testing"
type: concept
category: technology
tags: [adyen, testing, online-payments, payment-modifications, webhooks]
---

## Overview

Adyen's payment-testing guide provides test credentials, values, and scenario-specific triggers for checking whether an integration handles ordinary payments and payment modifications before going live. Its coverage spans redirect return and authorization status, capture and cancellation, refunds and reversals, authorization adjustments, encrypted card details, third-party authentication data, and Level 2/3 data.

## Simulation and outcome boundary

These fixtures exercise test integration behavior; they do not prove production availability, merchant or payment-method eligibility, or a live authorization, capture, refund, settlement, or funding outcome. In particular, the guide demonstrates later `CAPTURE_FAILED` and `REFUND_FAILED` events after successful modification webhooks and says either failed-modification simulation can take up to 24 hours. A single partial manual capture cancels the remaining amount, while multiple partial manual captures require Adyen Support enablement.



## White POS test card v1 boundary

Adyen's white physical POS test card v1 has currency-selected Mastercard/Maestro applications and amount/currency-selected CVM or decline simulations. It cannot test contactless payments or mobile Tap to Pay; the guide points to green-blue v2.4+ for those. Repeated incorrect PIN attempts can make the test card unusable. Simulation tables and raw refusal details are test fixtures, not live issuer or card-network behavior. The pinned v1 page does not state that the card is retired. [[source-adyen-docs-point-of-sale-testing-pos-payments-test-card-v1]]
## Sources

- [[source-adyen-docs-point-of-sale-testing-pos-payments-b2-test-cards]] — Adyen Docs 2026-09-15 guide to B2 physical Europe/North America POS test-card sets, card-edition caveat, offline/CVM limits, and MKE expiration rule.


- [[source-adyen-docs-point-of-sale-testing-pos-payments-test-card-v1]] — 2026-09-15 Adyen white POS test-card v1 guide for applications, CVM/decline simulations, contactless exclusion, card-blocking, and refusal-field warnings.


- [[source-adyen-docs-point-of-sale-testing-pos-payments-test-card-v3]] — Adyen Docs 2026-09-15 guide to physical white-green v3 POS test-card applications, CVM and decline simulations, and its offline-test limit.


- [[source-adyen-docs-point-of-sale-testing-pos-payments-test-card-v2]] — 2026-09-15 Adyen webpage guide to the physical blue-green POS test card v2, application/currency and CVM triggers, offline counters, and simulated decline conditions; version 2.4+ for contactless/Tap to Pay.


- [[source-adyen-docs-point-of-sale-testing-pos-payments]] — Adyen Docs website guide to POS test cards, gift-card and QR simulators, and live-only wallet test limits (2026-09-15 snapshot).


- [[source-adyen-docs-online-payments-donations-testing]] — Giving-specific test-card and environment verification guide (webpage snapshot, 2026-09-15), with separate live campaign and donation checks.


- [[source-adyen-docs-development-resources-testing-3d-secure-2-authentication]] — Adyen 3DS2 test-scenario and card fixture guide (webpage snapshot, 2026-09-15) for browser/native challenges, Advanced-flow actions, standalone-authentication webhooks, and no-liability-shift simulation.


- [[source-adyen-docs-risk-management-disputes-api-test-applicable-dispute-reasons]] — test-environment chargeback simulation through `holderName`, capture, dispute webhooks, and test accept/defend actions, with scenario and timing limits (webpage snapshot, 2026-09-15)


- [[source-adyen-docs-development-resources-test-cards-and-credentials-test-card-numbers]] — Adyen test-platform card-number catalog, server-side `test_` fixture route, and 3D Secure 2 enrolled-card table (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-development-resources-test-cards-and-credentials-alternative-payment-method-credentials]] — webpage snapshot (2026-09-15) with alternative-method test credentials and simulator routes, including method-specific TEST limits and live-only penny-test qualifications for iDEAL | Wero and MobilePay.


- [[source-adyen-docs-development-resources-testing]] — webpage snapshot (2026-09-15) routing prerequisites and client/server/webhook coverage for full online-payments integration testing before live acceptance

- [[source-adyen-docs-development-resources-testing-payments-and-modifications]] — webpage snapshot (2026-09-15) routing test payment and modification scenarios, prerequisites, expected webhooks, and simulation warnings
