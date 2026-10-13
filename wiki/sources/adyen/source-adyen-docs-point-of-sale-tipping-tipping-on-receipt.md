---
title: "Tipping on the receipt | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/tipping/tipping-on-receipt"
raw_files:
  - "adyen/docs/point-of-sale/tipping/tipping-on-receipt/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, tipping, authorization-adjustment, capture]
---

## Overview

This Adyen Docs guide describes **tipping on a printed receipt** after a cardholder completes the initial payment interaction at an Adyen terminal. The shopper writes and signs a tip after the original purchase amount has been authorized; the tip itself is **not in that initial authorization**. The merchant can pursue either a later authorization adjustment or an overcapture, then manually capture the final original-plus-tip amount. This is a Terminal API-initiated card flow with later Adyen backend modification/capture calls, not a second Terminal API payment for the tip. See [[adyen]], [[adyen-terminal-api]], and [[adyen-authorization-adjustment]].

## Key takeaways

- Adyen labels receipt tipping harder to implement and subject to limitations, recommending the broader tipping page for alternatives. The merchant must set up **manual capture** and **standard webhooks**; authorization adjustment presumes the pre-authorization flow, while overcapture calls for contacting Adyen Support. The page's examples are conditional instructions, not evidence that either path is enabled for a particular merchant or card.
- With **authorization adjustment**, the merchant first requests a new **total** authorization that includes the written tip, then manually captures. The guide says an adjustment may fail or still lead to chargeback, with slightly higher scheme fees than overcapture. For **overcapture**, the merchant captures above the authorized original amount without a prior amount increase; the guide describes lower scheme fees but greater rejection/chargeback risk under scheme rules. The receipt tip is additional merchant payment amount, not an Adyen-paid gratuity or an automatic transfer to staff.
- The terminal `PaymentRequest` uses `SaleData.SaleToAcquirerData` with `authorisationType=PreAuth` **when adjustment is intended**. Retain the initial `pspReference` for backend adjustment and capture; synchronous adjustment also requires the URL-decoded `adjustAuthorisationData` blob. The tip-percentage calculation uses original and gratuity values from `AdditionalResponse` in minor units. The guide's **over 20%** threshold is a rule of thumb, not the scheme contract.
- The **asynchronous** adjustment route is Checkout API `POST /payments/{paymentPspReference}/amountUpdates` with the new total, `reason=DelayedCharge`, and `merchantAccount`; its webhook tells whether that amount was authorized. The **synchronous** route is Payment API `POST /adjustAuthorisation` with original reference, new total, URL-decoded adjustment blob and merchant account; retain the returned updated blob for any later adjustment. The final **manual capture** is Checkout API `POST /payments/{paymentPspReference}/captures` for the original-plus-tip total, with a webhook confirming capture outcome. Request submission alone does not establish authorization, capture, or settlement.
- **Authorization-adjustment support** is limited to specific **credit-card schemes** and depends on **Merchant Category Code**; the receipt-tipping flow as a whole is **not supported for wallets or debit cards**. The page says receipt tipping is common in the US, Singapore, and Hong Kong, but does not restrict it to those markets or prove a merchant's regional eligibility. Schemes differ on the tip percentage requiring adjustment (stated range 0–20%); a tip beyond the applicable limit can be rejected or charged back. Capture should occur before pre-authorization expiry when possible. The page does not specify a refund procedure for failed or disputed tips.

## Detail locators

- `Tipping on the receipt`, lines 15–25: only-when-necessary warning, written-tip sequence, original authorization versus unauthorized tip, two choices.
- `Requirements`, lines 27–38: Terminal API/terminal scope, standard webhooks, manual capture, pre-authorization and Support prerequisites.
- `Authorization adjustment or overcapture`, lines 40–55: two-stage money flow, relative fees and risks, comparison table.
- `How it works` / `Limitations for tipping on the receipt`, lines 57–80: conditional adjustment versus capture decision, US/SG/HK context, scheme/MCC limitations, 0–20% scheme range, overcapture Support, authorization expiry, wallet/debit exclusion.
- `Pre-authorize the payment`, lines 82–107: Terminal API PreAuth field, `pspReference`, sync adjustment blob, tip calculation in minor units, nonbinding 20% rule of thumb.
- `(Optional) Adjust the pre-authorization`, lines 109–136: Checkout asynchronous amount update and webhook versus Payment API synchronous adjustment and updated blob; each amount is the **new total**.
- `Capture the payment`, lines 138–149: Checkout capture for the final original-plus-tip amount and asynchronous capture webhook.
- `See also`, lines 151–155: linked pre-authorization, adjustment, and capture guides are navigation until read for this entry.

## Related

- [[adyen]] — provider page.
- [[adyen-terminal-api]] — terminal-initiated payment route.
- [[adyen-authorization-adjustment]] — backend amount-update concept for eligible pre-authorized payments.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/tipping/tipping-on-receipt/2026-09-15|Tipping on the receipt (2026-09-15 snapshot)]]
