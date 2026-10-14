---
title: "Adyen Autonomous Stores"
type: concept
category: technology
tags: [adyen, point-of-sale, autonomous-stores, pre-authorization]
---

## Definition

Adyen's autonomous-store guide describes an unattended-store entry and payment flow: a shopper presents a card at a payment terminal, the merchant's system uses Terminal API card acquisition and pre-authorization to decide entry, computes the basket after exit, optionally adjusts the authorization through an Adyen backend API, and manually captures. The merchant implements door and basket logic; the source does not define a separate seller or merchant-of-record model.

## Evidence boundary

Card alias is a recognition identifier, not a payment token. Adjustment remains eligibility-dependent. The asynchronous amount-update `received` response needs an `AUTHORISATION_ADJUSTMENT` webhook, while the enabled synchronous `/adjustAuthorisation` route returns `Authorised` for the new amount and uses the latest blob for later adjustments. Manual capture is separate and its `received` response needs `CAPTURE`/`CAPTURE_FAILED` webhook outcome handling. The dated guide's terminal examples and test requests do not establish current account enablement or a successful store deployment.

## Related

- [[adyen-terminal-api]] — terminal messages and card acquisition
- [[adyen-authorization-adjustment]] — backend amount updates
- [[adyen-payment-capture]] — final capture and webhooks

## Sources

- [[source-adyen-docs-point-of-sale-autonomous-stores]] — 2026-09-15 Adyen autonomous-store guide for card recognition, entry pre-authorization, backend amount adjustment, manual capture and conditional recovery.
