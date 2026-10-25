---
title: "Adyen Napas card Android Redirect Component earlier versions"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/napas-card/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/napas-card/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, napas-card, android, redirect, components, earlier-versions]
---

## Overview

This historical Adyen page, titled “Napas card Redirect Component v4.x.x integration,” adds a redirect payment route to an existing **Advanced-flow Android Components** integration. It describes server-owned payment requests, Android redirect handling, return details and provisional versus final results. The page metadata says last modified 2019-09-06; the 2026-09-15 capture does not establish current availability, merchant eligibility or a successful payment. See [[adyen]] and [[adyen-android-sdk]].

## Key takeaways

- The stated prerequisites are an existing Advanced Android Components integration and Napas card added in Customer Area. The payment form need not collect extra shopper details for this method. The server's `/paymentMethods` request specifies `countryCode: VN`, VND amount currency and amount value.
- **Method-identity conflict:** although the page calls this Napas card, it names the discovered `paymentMethod.type` as `momo_atm` and repeats `momo_atm` in `/payments` prose, request examples and redirect response. Preserve this exact historical text; the page alone cannot resolve whether the type is correct for NAPAS or a copied MoMo ATM value. Verify against authoritative, version-matched method data before implementing.
- From the merchant server, the page says to send `paymentMethod.type: momo_atm` and a `returnUrl` obtained through `RedirectComponent.getReturnUrl(context)` in `/payments`. Pass the response `action` to the Android client; the Redirect Component handles the redirect. After the shopper returns, the server posts `actionComponentData.details` to `/payments/details`. The Redirect Component hyperlink at line 177 targets a Sessions-flow Android Components guide even though this page requires Advanced flow at line 30; the link does not establish Sessions support here. The curl `/payments` body is syntactically JSON, but its literal `{hint:...}paymentMethod{/hint}` property at lines 69–70 is not the ordinary `paymentMethod` request field and should not be copied as a valid `/payments` request; the Node/Python/Ruby examples use the ordinary key.
- `/payments/details` supplies a `resultCode` to present, but `Pending` or `Received` means the final result is unknown and requires an `AUTHORISATION` webhook. If the shopper never returns, the page says to await webhooks; it distinguishes `AUTHORISATION` success true/false from `OFFER_CLOSED` success true for an incomplete timed-out offer. A redirect or shopper return is not proof of authorization, capture or settlement.
- Test fixtures cover successful, blocked-card, insufficient-funds and amount-limit scenarios. The page says to check test status in Customer Area and submit a separate live Customer Area request before accepting live Napas card payments. Test cards and OTPs are historical fixtures, not evidence of live provider operation.

## Detail locators

- Scope, prerequisites and VN/VND discovery: pinned raw lines 15–45.
- `/payments` fields, examples and redirect action: pinned raw lines 47–173. The curl sample targets test v68; its syntactically valid but incorrect hinted request property is at lines 69–70.
- Android return and server `/payments/details`: pinned raw lines 175–208. The example uses test v72 for details while the payment example uses test v68; the page does not explain this version difference.
- Result codes and webhook outcome handling: pinned raw lines 210–229. Its no-return sentence says “website” despite the Android app context (line 223); use the stated webhook principle without treating that noun as platform guidance.
- Test fixtures and live request: pinned raw lines 231–244.

## Related

- [[adyen-android-sdk]] — native Components, redirect and merchant-server boundaries
- [[adyen-online-payments]] — broader Checkout and outcome concepts

## Raw Sources

- [[raw/adyen/docs/payment-methods/napas-card/android-component/earlier-versions/2026-09-15|Napas card Android Redirect Component v4.x.x guide, 2026-09-15]]
