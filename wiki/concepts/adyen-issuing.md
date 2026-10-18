---
title: "Adyen Issuing"
type: concept
category: technology
tags: [adyen, issuing, cards, balance-platform]
---

## Definition

Adyen Issuing is a platform-facing card program for creating virtual and physical cards for users. The 2023-modified overview captured 2026-09-15 describes a balance-platform model with an `accountHolder`, a funds-holding `balanceAccount`, and a card `paymentInstrument` associated with that balance account. It also describes platform-side authorization decisions or optional automatic transaction rules, plus a company liable balance account for loading cards and balance transfers. [[source-adyen-docs-issuing]]

## Evidence boundary

The overview says an Issuing integration must accept and handle webhooks for asynchronous events, including payments, captures and refunds. Its EEA, UK and US support list is a dated snapshot; the page does not establish current availability, a particular platform's eligibility, PCI scope for a particular use case, an active issued card, successful authorization, capture or settled funds. Keep Issuing separate from Business accounts and Capital; their own guides govern those products.

## Sources

- [[source-adyen-docs-business-accounts-compliance-guidelines-account-statements]] — 2023-modified, 2026-09-15-captured statement-template guidelines including Issuing's pre-issuance sample review and EU UI versus UK durable-download rule; not legal advice.


- [[source-adyen-docs-issuing-get-started]] — Adyen Issuing get-started webpage (captured 2026-09-15): contact-led design, test integration, and separate live-account setup.


- [[source-adyen-docs-issuing]] — 2023-modified, 2026-09-15-captured Issuing overview for card-program purpose, core balance-platform resources, authorization options, webhooks and conditional PCI scope.

## Related

- [[adyen-financial-products]] — umbrella product family.
- [[adyen-platforms]] — platform context.
- [[adyen]] — provider context.
