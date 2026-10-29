---
title: "Pay by Bank Europe API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pay-by-bank-europe/api-only"
raw_files:
  - "adyen/docs/payment-methods/pay-by-bank-europe/api-only/2026-09-15.md"
tags: [adyen, pay-by-bank-europe, api-only, open-banking, redirect, sepa-direct-debit]
---

## Overview

This Pay by Bank (Europe) API-only guide, last modified 2023-08-28 and captured 2026-09-15, describes a custom payment form, optional issuer preselection, a `paybybank` redirect through Tink, result/webhook handling, SEPA Direct Debit token-based future payments, and test/live steps. It is a dated integration source, not evidence of current country or bank availability, merchant onboarding approval, completed settlement, or live operation. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- An existing API-only integration and Support-assisted method setup in Customer Area are prerequisites in this child guide (raw lines 21–26). The separate Pay by Bank (Europe) overview says **onboarding requires approval** and names Germany, France and UK in prose, while its capability matrix also includes Finland; use that overview's dated geography and approval claims with the present availability checks, not as current eligibility proof (overview pinned raw lines 23–27, 41–43).
- Issuer list display is optional and market-dependent. In Germany, the guide says the shopper selects a bank after redirect to Tink; in the UK, the merchant may let the shopper preselect a bank or leave selection to Tink. Where supported, obtain issuer IDs from a `/paymentMethods` request with appropriate countryCode and amount.currency; the object type is `paybybank`. UK test/live issuer lists are examples, not current bank coverage (raw lines 28–83).
- The server-side `/payments` table marks countryCode, returnUrl (maximum 1024 characters) and `paymentMethod.type: paybybank` required. `paymentMethod.issuer` is unmarked and supported only where issuer list display is available; shopperLocale is unmarked and controls Tink's redirect language (raw lines 87–98). The sample GB/GBP request and demo issuer are examples (raw lines 99–120).
- Check the `/payments` action, redirect to its `action.url`, and after website return send the URL-decoded `redirectResult` in `/payments/details`. The GET/browser recommendations are for app/mobile contexts (raw lines 427–482). `Pending`/`Received` is not final: await AUTHORISATION webhook; the guide says an offer closes if not authorised within **30 minutes**, with optional OFFER_CLOSED webhook. For no shopper return, rely on webhook outcome (raw lines 484–503). The Refused row points to **Pay by Bank US** raw responses for risk refusals, a cross-region link that should not be treated as Europe-specific evidence (raw line 496).
- The child guide's Authorised row calls the payment successful and says funds arrive in **2–3 days** (raw line 492). The separate method overview warns that a successful AUTHORISATION webhook means checks passed and transfer initiated, yet funds may still fail to arrive because of bank cancellation or delayed processing; Adyen may not be told of that failure, and the overview describes an eight-weekday chargeback path that cannot be defended (overview pinned raw lines 45–60). Do not treat authorization as guaranteed settlement.
- Future recurring transactions are described **through SEPA Direct Debit**, not a reusable `paybybank` redirect. The page recommends explicit shopper permission, says to create a shopper token and use it for later payments, and describes a `recurring.token.created` webhook with storedPaymentMethodId. Tokenized payments are limited in the guide to shopper-absent Subscription and UnscheduledCardOnFile cases (raw lines 505–520, 870–880, 1219–1245). The “Create a SEPA token” example already contains a `storedPaymentMethodId` and `sepadirectdebit` type; it cannot by itself demonstrate the initial consent/credential creation sequence (raw lines 522–546).
- Test guidance covers approved, authentication-error and shopper-cancelled scenarios with Tink test credentials for UK, Germany, France and Finland. Before live use, add Pay by Bank (Europe) in live Customer Area; those examples do not establish live bank coverage (raw lines 1845–1904).

## Detail locators

- Scope/setup, optional Tink issuer selection and country-specific examples: raw `## Requirements` lines 21–26 and `## Build your payment form` lines 28–85.
- Payment request, redirect and result finality: raw `## Make a payment` lines 87–441, `## Handle the redirect` lines 443–482, and `## Present the payment result` lines 484–503.
- SEPA Direct Debit token creation and shopper-absent subsequent payments: raw `## Recurring payments` lines 505–1843. In particular, the token webhook is at line 870 and Received result at line 1843; these are not settled-payment proof.
- Test and live gates: raw `## Test and go live` lines 1845–1904.
- Related method overview authority: separate pinned raw `raw/adyen/docs/payment-methods/pay-by-bank-europe/2026-09-15.md` lines 23–60 for onboarding approval, region/matrix tension, and post-authorization funds/chargeback limits. This child page's raw_files field intentionally names only its own pinned child raw.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/pay-by-bank-europe/2026-09-15|Pay by Bank Europe method overview]] — separate method-level approval, geography and settlement qualifications; read for those claims

## Raw Sources

- [[raw/adyen/docs/payment-methods/pay-by-bank-europe/api-only/2026-09-15|Pay by Bank Europe API-only guide, captured 2026-09-15]]
