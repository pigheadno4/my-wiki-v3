---
title: "ACH Direct Debit Flutter Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ach-direct-debit/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/ach-direct-debit/flutter-drop-in/2026-09-15.md"
tags: [adyen, ach, direct-debit, flutter, drop-in, sessions, advanced]
---

## Overview

This 2026-09-15 page is a **short ACH-specific add-on** for existing Flutter Drop-in Sessions and Advanced integrations. It supplies flow prerequisites, no-extra-method-parameter/configuration statements and TEST bank/return fixtures. It does not describe the full Flutter integration, ACH bank validation, shopper mandate, final authorization or settlement. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions** requires an existing Flutter Drop-in Sessions flow, Checkout API **v68 or later**, and asking Adyen Support to add ACH Direct Debit in Customer Area. Its Sessions prerequisite link is actually an **Advanced-flow** Flutter URL; the later session-creation link targets Sessions. This mismatch should not redirect implementation to Advanced. See raw lines 25–41.
- For the **Sessions** ACH add-on, no additional `/sessions` parameters or Drop-in configuration are specified. That means no **ACH-specific** additions here, not an empty base session request or waiver of ACH consumer bank verification and mandate obligations in the related [[source-adyen-docs-payment-methods-ach-direct-debit]] and [[source-adyen-docs-payment-methods-ach-direct-debit-verification-with-giact]]. See raw lines 39–47.
- **Advanced** requires an existing Flutter Drop-in Advanced flow and ACH addition in Customer Area. It states no ACH-specific Drop-in configuration or additional `/payments` parameters; the Advanced section gives no Checkout API minimum of its own. Base Advanced fields and ACH rules remain separate. See raw lines 67–88.
- Both flow sections give TEST details: any correctly formatted bank account and ACH routing number with any owner name, plus `ownerName=chargeback:<ACH return reason>` (for example `chargeback:R01`) to simulate a chargeback. The page delegates reason codes and chargeback instructions to a separate guide. TEST fixtures are not live-bank validation or payment success. See raw lines 49–65 and 90–106.
- This page does **not** state a bank-authorization time or webhook outcome. Use the reviewed ACH overview and channel-specific outcome guides for asynchronous debit/return lifecycle; do not infer immediate success from this minimal add-on. See the page's complete implementation/outcome scope at raw lines 15–106.

## Detail locators

- Sessions prerequisite/version/support and mismatched link: raw lines 25–35.
- Sessions no-extra-fields/configuration: raw lines 37–47.
- Sessions TEST payment and chargeback simulation: raw lines 49–65.
- Advanced prerequisites and no-extra-config/request fields: raw lines 67–88.
- Advanced repeated TEST fixtures: raw lines 90–106.

## Related

- [[adyen-online-payments]] — Flutter online-payment route.
- [[source-adyen-docs-payment-methods-ach-direct-debit]] — ACH entity, SEC, mandate and return context.
- [[source-adyen-docs-payment-methods-ach-direct-debit-verification-with-giact]] — consumer bank-account validation.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ach-direct-debit/flutter-drop-in/2026-09-15|ACH Direct Debit Flutter Drop-in, captured 2026-09-15]]
