---
title: "Adyen Platforms online donations using Giving"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/donations-online"
raw_files:
  - "adyen/docs/platforms/online-payments/donations-online/2026-09-15.md"
tags: [adyen, platforms, giving, donations, online-payments]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes an **API-only online** Giving integration in which platform users offer shoppers a donation to a nonprofit alongside an original purchase. The donation is a **separate transaction**: Adyen says it covers donation fees and transfers the donation in full to the nonprofit, while splits and fees may be set on the original purchase but **not** the donation (raw lines 15–25). [[adyen-giving]] is the main product route; [[adyen-platforms]] supplies the platform/user context.

## Key takeaways

- The guide requires a platform-model Adyen for Platforms integration with API-only online payments on Checkout API v67 or later; an Adyen Giving merchant webhook; supported method, region and currency; and a configured, active account-holder donation campaign (raw lines 27–50). The supported lists and campaign-management steps are linked to other pages, so this snapshot alone does not establish eligibility.
- The platform can show fixed amounts or a round-up option before or after checkout. Query POST `/donationCampaigns` from the server with merchant account, currency and user-store reference; `locale` is optional. The response supplies campaign ID, donation type/amounts and nonprofit presentation data (raw lines 52–114, 326–341, 368–377, 589–604). The round-up formula excludes the donation from `commercialTxAmount` (lines 648–659).
- Even for a pre-checkout donation choice, the server first requests the original `/payments` transaction and sends `/donations` only when the payment is authorized and the response has `donationToken`. For post-checkout, the token comes from the original `/payments` or iDEAL `/payments/details` response (raw lines 56–101, 669–675). The donation request includes its own amount, campaign ID, original payment PSP reference, token, reference, merchant account and user-store reference; method type differs for card/wallet versus iDEAL (lines 676–689, 721–734).
- The UI must identify and link to the nonprofit and its terms; fixed-amount UI also includes description, banner/logo and a decline option (raw lines 631–667). iDEAL donation appearance and webhook delivery may take a day or more (lines 646, 667, 768).
- The `/donations` response can report `completed`, `pending` or `refused` and a separate donation PSP reference, but the guide says the Giving merchant `DONATION` webhook is the donation-outcome route. Its `originalReference` associates the donation with the original purchase (raw lines 715–719, 760–775).

## Detail locators

- Fixed/round-up campaign request fields, response data and versioned test snippets: raw lines 96–629. Curl examples use Checkout test v72, while library snippets identify their own versions; live setup needs its own endpoint configuration.
- Donation form and round-up display rules: lines 631–667.
- Fixed/round-up POST `/donations` fields and example response statuses: lines 669–765. The round-up curl example appears to omit a comma after its `reference` value (lines 752–756); do not paste it unreviewed.
- Donation webhook example and test route: lines 766–809.

## Evidence boundary

Campaign setup, request construction, response fields and test webhook examples do not prove a particular shopper donated, the nonprofit received funds, or a platform or user is eligible in any current region. The sample charity account code is a test example, not a merchant-of-record or legal-ownership determination. This API-only platform route does not define Web Components, Sessions or in-person implementation.

## Related

- [[adyen-giving]] — Giving transaction and outcome model.
- [[adyen-platforms]] — platform and user context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/donations-online/2026-09-15|Pinned Platforms Giving online guide, captured 2026-09-15]]
