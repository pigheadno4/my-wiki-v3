---
title: "Adyen Alma payment-method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alma"
raw_files:
  - "adyen/docs/payment-methods/alma/2026-09-15.md"
tags: [adyen, alma, buy-now-pay-later, redirect, installments]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] snapshot introduces Alma as a France-focused buy now, pay later method with three or four shopper installments. The page says Alma checks shopper risk before approval and, if successful, takes full fraud risk and pays the merchant up front. See [[adyen-online-payments]]. These statements describe this captured method overview, not present account eligibility, a completed transaction or an unconditional approval guarantee.

## Key takeaways

- The capability matrix lists Buy Now Pay Later, redirect, France (FR) and EUR. It marks recurring unsupported; refunds, partial refunds and multiple partial refunds supported; partial captures supported; and multiple partial captures unsupported. Separate captures has a checkmark with a `See note` qualifier, while chargebacks has an `x` with a `See note` qualifier. This captured page does not expand either note, so those two cells should not be presented as unconditional capabilities or exclusions.
- The product description says shoppers can use three or four installments. Alma performs risk checks before approving and takes full fraud risk and pays the merchant up front if successful. This page does not describe settlement timing, the risk decision criteria or authorization/capture sequence.
- An external Alma widget is linked as a way to show method availability on a product page. This is a presentation option, not evidence of merchant account enablement or shopper eligibility.
- Integration navigation covers Web, iOS, Android, React Native, Flutter, API only and Pay by Link. The API-only route is described as building one's own UI for a website or iOS/Android app. The route labels do not define implementation fields or prove supported live account configuration.

## Detail locators

- Alma method description, installments, shopper risk and merchant payout wording: pinned raw lines 15–25.
- Country/currency and lifecycle capability matrix, including unresolved `See note` cells: pinned raw lines 27–29.
- Integration routes and platform descriptions: pinned raw lines 31–73. General See also links: lines 75–80.

## Related

- [[adyen-online-payments]] — provider integration concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/alma/2026-09-15|Alma overview, captured 2026-09-15]]
