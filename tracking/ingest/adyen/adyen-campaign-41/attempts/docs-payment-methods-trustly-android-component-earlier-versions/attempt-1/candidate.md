---
title: "Adyen Trustly Android Redirect Component v4.x.x guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/trustly/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/trustly/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, trustly, android, components, redirect, earlier-versions]
---

## Overview

This Trustly Android Redirect Component guide is explicitly for v4.x.x earlier versions. It was captured on 2026-09-15 but carries 2019-09-06 last-modified metadata. It requires an existing Advanced-flow Android Components integration and Trustly added in Customer Area, then describes server `/payments`, app redirect and server `/payments/details` after return. This historical guide does not establish current SDK/API compatibility, merchant eligibility or a completed payment. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-trustly]].

## Key takeaways

- The guide says the merchant need not collect shopper information in the payment form. `/paymentMethods` uses a supported country, supported currency and minor-unit amount; SE/SEK are examples, not an exhaustive eligibility rule. Find `paymentMethod.type: trustly`. The server `/payments` request uses `paymentMethod.type: trustly` and a `returnUrl` obtained from `RedirectComponent.getReturnUrl(context)`. The example `/payments` URL is v68; that example does not define a universal minimum or validate today's v4.x.x SDK use.
- The illustrated `/payments` response is `RedirectShopper` with a GET redirect action. Pass that action to the Android client and use Redirect Component for a Trustly-hosted payment page. After the shopper returns to the app, send `actionComponentData.details` to server `/payments/details`; the shown details call uses v72, a different example Checkout API version from `/payments`. The guide's redirect and See also links point to Sessions Components guidance even though its prerequisite is Advanced. Preserve that mismatch rather than assuming the Sessions route is the required server flow.
- `/payments/details` supplies a `resultCode` and `pspReference` for shopper messaging. The table lists Authorised, Cancelled, Error, Pending/Received and Refused; Pending/Received still lack a final result and require an `AUTHORISATION` webhook. If the shopper fails to return to app or website, the guide says to use webhooks; its table includes `AUTHORISATION` true/false and `OFFER_CLOSED` true for a timed-out offer. `RedirectShopper` and the sample `Authorised` response are examples, not evidence of actual settlement.
- The earlier guide's Authorised row says funds arrive in three days. The Trustly overview instead says even a successful `AUTHORISATION` webhook means a bank transfer was initiated, not that funds were received, and describes possible later failure and chargeback. Do not present the three-day row as a guaranteed funding or settlement term.
- The test section points to Trustly's test environment and gives a `YYMMDD-XXXX` Login ID/Personal number format with example digits. It says to check test-payment status in Customer Area and request Trustly in live Customer Area before acceptance. These are snapshot instructions, not proof of account enablement, test outcome or live funds.

## Detail locators

- v4.x.x title, redirect purpose, Advanced prerequisite and Customer Area setup: pinned raw lines 15–28.
- `/paymentMethods` country/currency examples and method type: pinned raw lines 30–42.
- Server `/payments`, `returnUrl`, v68 request examples and redirect response: pinned raw lines 44–370.
- Redirect Component, app return, `/payments/details` v72 example and response: pinned raw lines 372–403; Sessions-link mismatch: lines 374 and 437.
- Result codes, webhook fallback and OFFER_CLOSED: pinned raw lines 405–425; test/live steps: lines 427–433.
- Cross-page funding qualification: Trustly overview pinned raw `raw/adyen/docs/payment-methods/trustly/2026-09-15.md` lines 38–53 versus this guide lines 411–416.

## Related

- [[adyen-online-payments]] — main provider online-payment concept
- [[source-adyen-docs-payment-methods-trustly]] — Trustly overview and authorized-but-unfunded risk

## Raw Sources

- [[raw/adyen/docs/payment-methods/trustly/android-component/earlier-versions/2026-09-15|Trustly Android Redirect Component v4.x.x guide, 2026-09-15]]
