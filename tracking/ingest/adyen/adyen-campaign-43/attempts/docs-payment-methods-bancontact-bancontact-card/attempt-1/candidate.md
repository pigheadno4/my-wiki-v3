---
title: "Adyen Bancontact card overview"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-card"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-card/2026-09-15.md"
tags: [adyen, bancontact, card, belgium, redirect, 3d-secure]
---

## Overview

This Bancontact card method overview was captured 2026-09-15 and carries a 2023-04-11 last-modified timestamp. It describes Bancontact card acceptance in Belgium, the card-specific security and capture distinctions, a historical BE/EUR capability table, and navigation to Web, iOS, Android, API-only and in-person guides. It is distinct from Bancontact mobile; the table and route links do not establish current merchant eligibility or a successful payment. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-bancontact|the Bancontact parent overview]].

## Key takeaways

- A Bancontact card payment is described as similar to a regular card payment, except there is no CVC for Bancontact cards; a CVC field can still appear for co-badged cards. 3D Secure authentication is mandatory, separate captures are unsupported, and the integration must comply with European co-badged card regulations. Authentication is not itself proof of authorisation, capture or settlement. The separate Bancontact app/mobile path is linked, not detailed here.
- The captured feature table labels Bancontact card a Debit Card with Redirect flow for Belgium (`BE`) and euro (`EUR`). It marks refunds and partial refunds available, and separate captures, partial captures and chargebacks unavailable. These are page-level historical capability marks, not a current account-specific entitlement or operational outcome. The table's recurring checkmark is footnoted to the Bancontact Wallet Initiated Program (WIP), so it is not an unconditional recurring-card guarantee. The page does not provide tokenization steps, WIP signup criteria or eligibility limits; use implementation-specific child guides for those details.
- Integration choices on this page are Web and prebuilt UI, iOS and Android prebuilt UI, API-only for a merchant-built website or app UI, and a separate in-person card route. These links select implementation guides; they do not make mobile-wallet QR/app flow interchangeable with card entry.

## Detail locators

- Page identity, historical last-modified timestamp and card-specific CVC, mandatory 3DS, capture and co-badging conditions: pinned raw lines 5–33.
- BE/EUR Debit Card and Redirect feature table, including refund/capture/chargeback marks and WIP recurring footnote: pinned raw lines 35–39.
- Web, iOS, Android, API-only and in-person route links: pinned raw lines 41–71.

## Related

- [[adyen-online-payments]] — primary provider method route
- [[source-adyen-docs-payment-methods-bancontact]] — Bancontact parent overview for card/mobile distinction
- [[source-adyen-docs-payment-methods-bancontact-bancontact-card-api-only]] — implementation-specific API-only card guide

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-card/2026-09-15|Bancontact card overview, captured 2026-09-15]]
