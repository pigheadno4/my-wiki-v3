---
title: "Japanese convenience stores API-only (econtext)"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/econtext-konbini/api-only"
raw_files:
  - "adyen/docs/payment-methods/econtext-konbini/api-only/2026-09-15.md"
tags: [adyen, econtext, konbini, japan, api-only, voucher]
---

## Overview

This 2026-09-15-captured [[adyen]] API-only add-on covers econtext payments at Japanese convenience stores and Pay-easy ATM/online. A merchant builds the payment form and uses a server-side Checkout `/payments` request. The page separates 7-Eleven redirect, other-store voucher, Pay-easy ATM voucher, and Pay-easy Online redirect paths; voucher issuance or redirect alone is not payment completion. See [[adyen-online-payments]] and the pinned raw for the method-specific steps.

## Key takeaways

- **Setup and discovery:** The page assumes an existing API-only integration and gives separate Customer Area additions: eContext Convenience Stores for Lawson, Mini Stop, Family Mart and Seicomart; eContext 7Eleven; eContext PayEasy ATM; and eContext PayEasy Online Banking. For `/paymentMethods`, it specifies `countryCode: JP`, `amount.currency: JPY`, and amount value in minor units. The types are `econtext_seven_eleven`, `econtext_stores`, `econtext_atm`, and `econtext_online` respectively (raw lines 32–71). These are documented setup/discovery paths, not proof of current merchant enablement.
- **Shopper and request data:** Collect full first and last name, telephone number and email. The `/payments` table marks `paymentMethod` (type and those shopper details), `shopperLocale`, and `returnUrl` required; it states a 1024-character maximum for `returnUrl`. The email-voucher statement excludes 7-Eleven. Examples use 1,000 JPY and `ja-JP`; keep the fields and types scoped to the chosen path rather than copying sample values as universal rules (raw lines 21–26, 42–83).
- **7-Eleven:** `/payments` can return `RedirectShopper` with a redirect action. Use the returned `action.method` and `action.url` to show the voucher on 7-Eleven's page; the shopper then pays cash at a store, with outcome learned through webhooks. This page says 7-Eleven voucher payments can only be tested in the live environment with Support-arranged penny testing (raw lines 433–455, 1021–1023). The separately captured [[raw/adyen/docs/payment-methods/econtext-konbini/2026-09-15|method overview raw]] says a **local entity is required for 7-Eleven** (overview line 25); treat that as overview-scope historical prerequisite, not current account eligibility.
- **Other stores and Pay-easy ATM:** `econtext_stores` returns `PresentToShopper` and a voucher action with expiry, reference and amount; present it and wait for the payment webhook. `econtext_atm` also uses a voucher; the page's dated change says the ATM voucher must display `collectionInstitutionNumber`, `reference`, and `alternativeReference` from `/payments`, with old payment numbers rejected from **24 February 2026 00:00 JST**. The ATM field table further identifies expiry and amount. This is the captured instruction, not proof of present-day ATM behavior (raw lines 28–30, 805–915).
- **Pay-easy Online:** `econtext_online` has a redirect response. Follow `action.url`, then submit the URL-decoded returned `redirectResult` in `/payments/details`; the page gives a `resultCode`/`pspReference` response example. Its mobile browser guidance is recommendation, not a universal mandate (raw lines 918–999).
- **Asynchronous outcome and live gate:** For 7-Eleven and other-store voucher paths, `RedirectShopper` and `PresentToShopper` mean wait for completion; the webhook table distinguishes `PENDING` success=true (voucher created, still pending), `AUTHORISATION` success=false (failed), `AUTHORISATION` success=true (completed), and `OFFER_CLOSED` success=true (expired). The page gives an econtext simulator procedure and separately says to request live Customer Area addition before live acceptance (raw lines 1001–1056). Do not treat the example `/payments/details` Authorised response as proof that a cash voucher was redeemed.

> [!warning] Captured test and example conflicts
> The page says 7-Eleven voucher payments can only be tested live with Support (raw lines 451 and 1023), yet its econtext simulator instructions also offer a 7-Eleven selection (line 1042). Confirm the applicable environment with Adyen rather than treating the simulator list as proof of 7-Eleven test availability. The other-store voucher response sample has blank currency and `totalAmount.value: 10000` after a 1,000 JPY request (raw lines 462–480, 817–837). The Pay-easy ATM field table calls `collectionInstitutionNumber` six digits, while its sample value `58091` has five digits (raw lines 883–899). The Pay-easy Online test request is followed by an example redirect URL on a `checkoutshopper-live` host (raw lines 923–956). These samples should not be used to infer production values or a complete executable recipe.

> [!warning] Source-date and base-link scope
> The raw frontmatter records `last_modified: 2020-06-12` (line 11), while its body includes the February 2026 Pay-easy ATM deadline (lines 28–30); this capture does not establish when that notice was inserted or its current operational state. The requirement's API-only base link is `/online-payments//` (line 36), while the page's `See also` section names an API-only integration guide at `/online-payments/api-only` (lines 1058–1060). Use the latter route for base integration navigation.

## Detail locators

- Four method types, setup divisions and JP/JPY discovery: raw lines 32–71.
- Required request fields, example API-library variants and 7-Eleven redirect: raw lines 73–455. Several language snippets use library-specific enum spellings; the API `type` list at lines 66–71 is the direct method identifier evidence.
- Other-store voucher, Pay-easy ATM and Online examples and handling: raw lines 457–999.
- Result-code/webhook state table, simulator, live Customer Area and base guide: raw lines 1001–1062. The simulator credentials and references are historical test fixtures, not live-payment evidence.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/econtext-konbini/api-only/2026-09-15|Japanese convenience stores API-only, captured 2026-09-15]]
- [[raw/adyen/docs/payment-methods/econtext-konbini/2026-09-15|Japanese convenience stores method overview, captured 2026-09-15; related context]]
