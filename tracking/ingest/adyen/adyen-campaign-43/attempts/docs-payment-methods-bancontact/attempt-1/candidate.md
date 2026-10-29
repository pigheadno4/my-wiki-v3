---
title: "Bancontact payment method overview"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact"
raw_files:
  - "adyen/docs/payment-methods/bancontact/2026-09-15.md"
tags: [adyen, bancontact, belgium, debit-card, wallet, redirect]
---

## Overview

This Adyen Bancontact overview, captured 2026-09-15 with page `last_modified` 2019-12-17, separates **Bancontact card** from **Bancontact mobile** and routes readers to their own guides. Its capability table is a historical BE/EUR snapshot, not proof of current merchant eligibility, bank/app coverage, live success or settlement. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Bancontact card:** the page describes a card-like payment without a security code, with **mandatory 3D Secure** and **automatic capture**. Its table labels the method Debit Card and Redirect in **Belgium/EUR**. These are card-specific statements; do not transfer them to the mobile wallet path. See raw lines 25–32.
- **Bancontact mobile:** the shopper goes to Payconiq by Bancontact or an integrated banking app, directly on mobile or by scanning a desktop QR code. The table labels it Wallet and Redirect or Additional action in **Belgium/EUR**. This page does not define exact QR/action payload, app return, expiry or server flow; use the linked mobile child guide. See raw lines 25–28 and 30–33.
- For **both** variants, the table marks refunds and partial refunds supported but separate captures, partial captures and chargebacks unavailable. It marks recurring with footnote **Bancontact Wallet Initiated Program (WIP)**; the footnote is the qualification, not a general saved-card/token recurring guarantee. These table marks are method-level historical capabilities, not an account-specific feature decision or operational result. See raw lines 30–35.
- The page offers separate **card** and **mobile** acceptance routes and a separate in-person link. Card, mobile wallet and in-person implementation instructions are not interchangeable. See raw lines 37–49.

## Detail locators

- Card security-code, 3DS and capture distinction; mobile app/QR handoff: raw lines 23–28.
- BE/EUR, flow, refund/capture/chargeback feature table and WIP footnote: raw lines 30–35.
- Child method and in-person navigation: raw lines 37–49.

## Related

- [[adyen-online-payments]] — online-payment method route.
- [[source-adyen-docs-payment-methods-bancontact-bancontact-card]] — Bancontact card child.
- [[source-adyen-docs-payment-methods-bancontact-bancontact-mobile]] — Bancontact mobile child.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/2026-09-15|Bancontact overview, captured 2026-09-15]]
