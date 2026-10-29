---
title: "Adyen Walley Android Redirect Component v4.x.x guide"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/walley/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/walley/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, walley, android, redirect, components, earlier-versions]
---

## Overview

This captured Adyen page is titled **Walley Redirect Component v4.x.x integration** and describes adding Walley to an existing Android Components integration through a server `/payments` request and client Redirect Component. The requirements text separately says Walley for Android works with **all versions** of Components; treat that as the page's claim, while retaining the earlier-versions/v4.x.x title rather than using this guide as proof of current-version behavior. It says the payment form need not collect shopper information, but a redirect return and result handling are still necessary. The 2026-09-15 snapshot is not proof of present account enablement or completed live payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Availability and product split:** Contact Adyen Support to add Walley in the **test** Customer Area. Query `/paymentMethods` with country/currency pairs DK/DKK, FI/EUR, NO/NOK, or SE/SEK and `channel: android`. Its response identifies B2C as `walley` and B2B as `walley_b2b`; **Denmark or DKK is B2C only**. Do not send the B2C example type for a B2B selection. The guide's version title and its “all versions” claim coexist (raw lines 21–47).
- **Redirect request and return:** The Component provides `paymentComponentState.data.paymentMethod`. The server makes `/payments` using the selected method type and a return URL obtained from `RedirectComponent.getReturnUrl(context)`, with a stated **1024-character maximum**. The page spells the parameter `returnURL` in prose; verify the API field in the chosen base guide. Its example response is `RedirectShopper` with `action.type: redirect`, an additional action rather than final payment success. Pass the action to the app's Redirect Component. After the shopper returns, send `actionComponentData.details` in a server POST to `/payments/details` (raw lines 51–111).
- **Result finality:** Use `/payments/details.resultCode` for shopper presentation and `pspReference` as the transaction identifier. `Authorised` means payment was completed by the shopper and sent to the bank for processing; the page says funds follow in most cases and manual capture still requires a capture. `Cancelled`, `Error`, and `Refused` have distinct handling. `Pending` or `Received` means the final result is **not yet known**; wait for an AUTHORISATION webhook. The page also says to rely on notification webhooks when the shopper does not return, distinguishing AUTHORISATION `success:false` from `success:true` (raw lines 99–132).
- **Test scope:** Walley test scenarios can use `CivRegNo` as `socialSecurityNumber`; B2B testing additionally gives a company name and registration-number example. Test payment status is checked in test Customer Area. These test requirements do not change the page's general statement about the payment form collecting no shopper information and do not establish live eligibility (raw lines 19, 134–147).

## Detail locators

- Identity, existing integration and version-scope tension, test setup: pinned raw lines 15–26.
- Country/currency pairs, Android channel, B2C/B2B type and DK/DKK restriction: lines 28–47.
- Component state, server request, return URL limit, action and redirect/details handoff: lines 51–111.
- ResultCode handling and AUTHORISATION webhook finality: lines 113–132.
- CivRegNo/B2B test inputs and test Customer Area check: lines 134–147.

## Related

- [[source-adyen-docs-payment-methods-walley]] — method overview for separate scope and feature matrix
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/walley/android-component/earlier-versions/2026-09-15|Walley Android Redirect Component v4.x.x guide, captured 2026-09-15]]
