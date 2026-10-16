---
title: "Adyen Oracle Xstore"
type: concept
category: technology
tags: [adyen, oracle-xstore, pos, eftlink, opi]
---

## Definition

Adyen's Oracle Xstore integration connects Oracle's retail POS/back-office platform to Adyen payment terminals through EFTLink and Oracle Payment Interface (OPI) messages. The captured guide states Xstore version 15+ and EFTLink/OPI version 17+, with Xstore Mobile as a separate Android-terminal application route. [[source-adyen-docs-plugins-oracle-xstore]]

## Scope and evidence boundary

EFTLink maps an Xstore transaction to a selected terminal; the guide lists terminal models and in-person features, including sale, limited same-settlement-day void, refund and partial-authorization routes. Model support differs for Xstore Mobile, and the V240m Plus listing is Brazil-only. Setup points to an Adyen test account, Support-enabled OPI, stores, assigned/boarded terminals and extra app/certificate deployment for Xstore Mobile. These are documented capabilities and setup routes in a 2023-modified page captured in 2026, not current merchant eligibility, a live payment result, refund outcome, settlement proof or a full implementation contract.

## Sources

- [[source-adyen-docs-plugins-oracle-xstore]] — Adyen Oracle Xstore POS orientation, compatibility matrix, EFTLink/OPI flow, features and setup links (2026-09-15 snapshot).

## Related

- [[adyen]]
- [[adyen-payment-terminals]]
