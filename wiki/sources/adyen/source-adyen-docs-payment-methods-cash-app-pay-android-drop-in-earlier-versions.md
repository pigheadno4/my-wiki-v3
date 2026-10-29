---
title: "Cash App Pay Android Drop-in v4.x.x guide"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-pay/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/cash-app-pay/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, cash-app-pay, android, drop-in, tokenization]
---

## Overview

This 2026-09-15-captured **Cash App Pay** guide is titled for Android Drop-in **v4.x.x** and requires at least **4.12.0** for an existing **Advanced-flow** integration. It is about Cash App Pay, not Cash App Afterpay. It covers method discovery, one-off payment results and tokenized future payments; it is historical version-scoped documentation, not proof of current SDK behavior, account enablement or a completed live payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Before starting, the guide requires Advanced-flow Android Drop-in v4.12.0+, the **Recurring tokens life cycle events** webhook, Cash App Pay added in Customer Area, and **Recurring details** selected under Developer > Additional data > Payment. `/paymentMethods` uses **US**, **USD**, and amount value in minor units. The optional Drop-in toggles `setShowStorePaymentField` (default true) and `setStorePaymentMethod` (default false) control how token storage is offered or automatic; they do not independently prove shopper permission or token creation (raw lines 14–46).
- For a one-off payment, the server sends `/payments` with `paymentMethod.type: cashapp` and a `returnUrl` the page says to obtain from `CashAppPayComponent.getReturnUrl(context)`. The example includes `shopperReference` and uses a test endpoint. The guide says `/payments/details` `resultCode` can be used to show the shopper result and an asynchronous webhook also reports the outcome. **Received** means final status is unknown and an AUTHORISATION webhook follows; **Authorised** is successful, and manual-capture users must still capture. Cancelled, Error and Refused are separate outcomes (raw lines 48–96).
- The page says Cash App Pay supports tokenization for future recurring and card-on-file payments. It **strongly recommends explicit shopper permission** for future charges and transparency about recurring schedule/amount. To create a token, send the client's `storePaymentMethod` state and a unique `shopperReference` in `/payments`; Drop-in may expose a shopper toggle, or configuration can store automatically without one. Do not turn the recommendation into an API-required consent field or infer consent merely from auto-store configuration (raw lines 98–113).
- To include a recognizable **$cashtag** on future recurring payments, the page recommends enabling **Token information for digital wallets** additional data, then reading `additionalData.cashapp.cashtag`, shopper reference and stored payment method ID from `/payments/details`. The `recurring.token.created` webhook includes token references but **not** the $cashtag. For a token payment, send `state.data.paymentMethod` and the general one-off/recurring tokenization parameters; `paymentMethod.cashtag` is **optional**. The example uses `shopperInteraction: ContAuth` and `recurringProcessingModel: CardOnFile`; it is a CardOnFile example, not a universal recurring recipe (raw lines 115–170, 172–197).
- If a shopper deletes stored details, the page says Adyen sends `recurring.token.disabled`; remove the unusable token and ask the shopper to choose another method to avoid future failed payments. Test scenarios use the Cash App Pay sandbox magic values and test Customer Area; live setup requires adding Cash App Pay in the live Customer Area (raw lines 533–559).

> [!warning] Historical snippet and route limits
> The opening Android Drop-in link uses `version=latest` despite this page's v4.x.x heading and 4.12.0 minimum (raw lines 14–24); use the version-specific base guide. The one-off curl snippet is inside a `json` fence and has no shell line continuations (raw lines 57–76), while a details response example spells `merchantRreference` with an extra `R` (lines 134–155). The Java token example contains a comma after the `.cashtag(...)` call and the Go v10.4.0 comment imports `/v9/` paths (lines 219–222, 372–377). Treat these as illustrative examples requiring verification, not copy-ready code.

## Detail locators

- Version, prerequisites, discovery and optional storage toggles: raw lines 14–46.
- One-off `/payments`, `/payments/details` results and asynchronous finality: raw lines 48–96.
- Token creation, shopper permission recommendation and $cashtag retrieval: raw lines 98–155.
- Token payment example and optional $cashtag: raw lines 157–518.
- Token-disabled webhook, test and live setup: raw lines 533–559.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-pay/android-drop-in/earlier-versions/2026-09-15|Cash App Pay Android Drop-in v4.x.x guide, captured 2026-09-15]]
