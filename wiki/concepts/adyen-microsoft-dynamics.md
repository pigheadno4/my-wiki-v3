---
title: "Adyen Microsoft Dynamics 365 Commerce"
type: concept
category: technology
tags: [adyen, microsoft-dynamics, dynamics-365-commerce, point-of-sale, ecommerce]
---

## Definition

Adyen's Dynamics 365 Payment Connector guide covers Dynamics 365 **Commerce** channels: MPOS and CPOS use local and cloud Terminal API communications respectively, while e-Commerce and Call Center use Checkout API. The 2023-modified, 2026-09-15-captured page requires separate merchant accounts and API credentials for each channel when several channels are used. It is a connector setup guide, not a general Dynamics ERP integration claim. [[source-adyen-docs-plugins-microsoft-dynamics]]

## Evidence boundary

Support-side roles, back-office configuration and tokenization enablement, plus test/live terminal and account setup, are separate from creating credentials. This guide does not establish an actual merchant's current eligibility, seller or merchant-of-record identity, successful payment/refund/capture, settlement or bank receipt. Channel-specific roles, Optional Domain and V002 Origin Key instructions remain in the source page.

## Sources

- [[source-adyen-docs-plugins-microsoft-dynamics]] — 2023-modified Adyen Dynamics 365 Commerce channel, credential, terminal, tokenization and test-to-live setup guide captured 2026-09-15.

## Related

- [[adyen-terminal-api]]
- [[adyen]]
