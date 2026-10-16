---
title: "Peak-season refunds and payouts | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/industries/peak-season/refunds"
raw_files:
  - "adyen/docs/industries/peak-season/refunds/2026-09-15.md"
tags: [adyen, refunds, point-of-sale, omnichannel, payouts, peak-season]
---

## Overview

This 2026-09-15 [[adyen]] Docs guide gives peak-season preparation advice for refund funding, ecommerce/POS/omnichannel refund paths and payout scheduling. Its reserve and timing suggestions are recommendations for a possible volume spike, while channel-specific identifiers and asynchronous refund events are operational distinctions. No refund request, notification or payout-schedule setting in this page proves shopper-bank credit or merchant-bank receipt. [[adyen-refunds]]

## Key takeaways

- Adyen recommends considering a refund reserve because peak-season refunds and chargebacks may exceed the usual payable balance and refunds can fail. A merchant can set or temporarily raise a reserve threshold and fund it by auto-funding, a bank-transfer payment-link top-up or a transfer between merchant accounts. The guide says a bank transfer can take a day or two. These are options, not a blanket reserve mandate or proof funds are available for a specific refund.
- **Ecommerce:** Checkout `/payments/{paymentPspReference}/refunds` is a referenced refund against the original payment PSP reference; partial refund support varies by method and is below the captured amount. A `REFUND` webhook gives asynchronous request outcome/validation reason, and a rare later `REFUND_FAILED` can follow successful validation. Request acceptance or validation is not final shopper-bank credit.
- **POS:** A referenced refund connects to the original payment through both terminal tender reference and Adyen PSP reference, with `REFUND` outcome. An unreferenced refund can send an amount to a card presented at the terminal and uses `REFUND_WITH_DATA`; it carries fraud/error risk, so the guide suggests delay/cancellation time and checking card identity, not as universal permission to refund any card. While offline, only unreferenced refunds are supported, with a recommended maximum amount; later referenced refund of an offline payment must account for a missing PSP reference in its offline response.
- **Omnichannel:** These returns are always referenced and use the merchant account that processed the original payment for the in-process funds deduction. The guide directs use of webhooks for the reference; ecommerce-to-POS refunds need original PSP reference, date and currency because no terminal tender reference exists for that ecommerce payment. A return location does not shift the original merchant-account funding identity.
- **Payouts:** Adyen advises against changing payout frequency or payout accounts during peak season and suggests doing needed changes beforehand. For direct merchants, frequency changes take effect at the start of the next period of the original schedule; for platforms/marketplaces, push-sweep changes are described as immediate, although the page still advises avoiding peak-season changes. Neither schedule configuration nor a payout initiation proves bank receipt.

## Detail locators

- **Seasonal reserve recommendations and funding options:** raw lines 19–38.
- **Ecommerce request references, asynchronous and later-failure events:** raw lines 48–54.
- **POS referenced/unreferenced identifiers, fraud safeguards and offline limits:** raw lines 56–72.
- **Omnichannel original-account/reference rules:** raw lines 74–80.
- **Direct-merchant versus platform payout timing and advice:** raw lines 82–94.

## Related

- [[adyen]]
- [[adyen-refunds]] — online refund lifecycle context; this guide also covers POS and omnichannel
- [[adyen-payouts]] — separate payout schedule and funding context
- [[adyen-unified-commerce]] — separate omnichannel context

## Raw Sources

- [[raw/adyen/docs/industries/peak-season/refunds/2026-09-15|Adyen peak-season refunds and payouts — collected 2026-09-15]]
