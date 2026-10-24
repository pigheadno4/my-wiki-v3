---
title: "Adyen Boost Wallet overview"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boost"
raw_files:
  - "adyen/docs/payment-methods/boost/2026-09-15.md"
tags: [adyen, boost, wallet, malaysia, redirect]
---

## Overview

This [[adyen]] Boost Wallet page is an online-payment method overview. It identifies **Boost Wallet** as a Malaysia digital wallet offered through **Razer Merchant Services (RMS, formerly MOLPay)** and shows an **MY/MYR redirect-wallet** capability row. It provides Web, iOS, Android and API-only child routes. The overview gives no shopper redirect steps, endpoint schema, SDK/API version or asynchronous payment-status sequence; its matrix is a 2026-09-15 documentation snapshot, not current merchant eligibility or transaction proof. [[adyen-online-payments]]

## Key takeaways

- **Provider and geographic scope:** The text says Boost Wallet is available in Malaysia and that Adyen offers it **via RMS**. RMS is the intermediary identified in the source; the page does not describe direct Boost onboarding, merchant credentials or contractual roles. See raw lines 21–25.
- **Method capability matrix:** The row labels the method a **wallet** with **redirect** flow in **MY/MYR**. It marks refunds available, but recurring, partial or multiple partial refunds, separate/partial/multiple partial captures and chargebacks unavailable. These marks are method-level snapshot statements; refund completion or eligibility for a particular merchant is not shown. See raw lines 27–29.
- **Integration navigation:** The child links cover Web, iOS, Android and API-only. API-only is described as building one's own UI for a website or iOS/Android app. The overview does not specify any of those child integrations' fields or result handling. See raw lines 31–55.

## Detail locators

- Method identity and RMS wording: raw lines 15–25.
- MY/MYR capability matrix: raw lines 27–29.
- Channel and API-only child routes: raw lines 31–55.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boost/2026-09-15|Adyen Boost Wallet overview snapshot]]
