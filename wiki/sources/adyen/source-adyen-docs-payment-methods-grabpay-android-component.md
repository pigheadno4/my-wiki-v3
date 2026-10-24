---
title: "Adyen GrabPay Android Component integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/grabpay/android-component"
raw_files:
  - "adyen/docs/payment-methods/grabpay/android-component/2026-09-15.md"
tags: [adyen, grabpay, android, components, wallets]
---

## Overview

This [[adyen]] guide adds GrabPay to an **existing Android Components** integration using Sessions or Advanced flow. It expressly targets Components **v5.0.0** (released October 2023) and sends earlier versions to another guide. See [[adyen-online-payments]]. The 2026-09-15 snapshot does not prove current merchant eligibility, payment success, capture or settlement.

## Key takeaways

- Both flow tabs require their corresponding existing Android Components integration at **minimum v5.0.0** and adding GrabPay in Customer Area before beginning. Earlier versions have a separate guide; no Checkout API minimum is stated on this page. See raw lines 19–39.
- The guide says no **additional GrabPay fields** in the Sessions `/sessions` request or Advanced `/payments` request and no additional GrabPay Component configuration in either flow. Sessions then links to creating the checkout session; Advanced links to launching/showing the Component. These are add-ons to the respective base integration, not permission to omit its standard request or action handling. See raw lines 41–67.
- The no-extra-fields statements are unqualified by **Wallet versus PayLater** in this Android v5 guide. Other pinned GrabPay guides, including [[source-adyen-docs-payment-methods-grabpay-ios-drop-in]], explicitly require delivery address and line items for PayLater while recommending them for Wallet. Therefore this Android page alone should not be used to waive PayLater fields across integrations; the cross-guide scope is unresolved here. See this raw lines 43–49 and the linked source for the separate PayLater claim.
- For testing, the page directs merchants to request test-wallet credentials from Support, use a registered phone number and received OTP in the Grab simulator, and check test-payment status in Customer Area. Before live acceptance, it says to submit a GrabPay request in the **live Customer Area**. None of these setup or status-check steps demonstrates a real successful payment or current account enablement. See raw lines 69–78.

## Detail locators

- **Version/date and earlier-version route:** raw lines 19–21.
- **Sessions/Advanced base and Customer Area prerequisites:** raw lines 23–39.
- **Request and Component configuration statements:** raw lines 41–67.
- **TEST simulator and live request:** raw lines 69–78.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-grabpay]]
- [[source-adyen-docs-payment-methods-grabpay-ios-drop-in]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/grabpay/android-component/earlier-versions/2026-09-15|GrabPay Android Component earlier versions]] — linked historical version route; behavior separate.

## Raw Sources

- [[raw/adyen/docs/payment-methods/grabpay/android-component/2026-09-15|GrabPay Android Component guide — captured 2026-09-15]]
