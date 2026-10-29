---
title: "Adyen EPS overview"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/eps"
raw_files:
  - "adyen/docs/payment-methods/eps/2026-09-15.md"
tags: [adyen, eps, austria, online-banking, redirect, payment-methods]
---

## Overview

This 2026-09-15 Adyen overview describes **Electronic Payment Standard (EPS)** as an Austrian online-banking method operated by Stuzza, the Austrian Banking Association. It sketches the shopper's bank-selection and redirect journey, a historical capability table, and links to channel-specific integration guides. The snapshot does not prove present bank coverage, merchant enablement or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Shopper journey:** The shopper selects EPS and a bank, is redirected to the bank website to enter bank details, confirms there, and is redirected back to the merchant website. This is a **bank redirect**, not account data collection by the merchant page in the described flow. Return to the merchant website is not by itself proof of a completed authorization or settled funds. The page calls EPS a “guaranteed payment method,” but supplies no guarantee terms or settlement timing here. (raw lines 23–31)
- **Capability snapshot:** The table labels EPS **Online Banking**, **redirect**, **AT** and **EUR**. It marks refunds, partial refunds and multiple partial refunds with checkmarks; separate, partial and multiple partial captures and chargebacks with x marks. Recurring has a checkmark with **“See note”**, but no explanatory note appears in this captured page. Do not infer the eligible recurring product, token request, conditions or current merchant-specific capability from that mark. (raw lines 33–35)
- **Integration routes:** Web, iOS, Android, React Native and Flutter link to pre-built UI routes; an API-only route says to build a UI for a website, iOS or Android app. These are navigation choices. The overview provides no Checkout API/SDK version, request fields, redirect action payload, webhook outcome, refund operation, recurring setup or go-live gate; use the selected child guide for implementation. (raw lines 37–73)

## Detail locators

- EPS identity, source-stated guarantee and bank redirect journey: pinned raw lines 15–31.
- AT/EUR feature matrix and unresolved recurring “See note”: pinned raw lines 33–35.
- Web/native/cross-platform and API-only child routes: pinned raw lines 37–73; generic see-also links: lines 75–80.

## Related

- [[adyen-online-payments]] — provider online-payment method context
- [[adyen]] — provider

## Raw Sources

- [[raw/adyen/docs/payment-methods/eps/2026-09-15|EPS overview, 2026-09-15]]
