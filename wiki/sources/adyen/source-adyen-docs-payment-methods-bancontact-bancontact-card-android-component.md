---
title: "Bancontact card Android Component v5.0.0 | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-card/android-component"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-card/android-component/2026-09-15.md"
tags: [adyen, bancontact, card, android, components, tokenization]
---

## Overview

This 2026-09-15-captured Bancontact **card** Android Component page explains how to add the method to an existing Android Components integration. It describes itself as the guide for **v5.0.0** (released October 2023) and points earlier SDK users to a separate guide. It is not the Bancontact Mobile app-switch/QR path, and this snapshot does not establish current SDK behavior or merchant eligibility (raw lines 5–21).

## Key takeaways

- Both **Sessions** and **Advanced** paths require an existing Android Components integration at minimum version **5.0.0** and Bancontact card added in Customer Area. The base `/sessions` or `/payments` request needs no Bancontact-card-specific additional fields, and the Component needs no additional configuration. Sessions proceeds to create the checkout session; Advanced launches and shows the Component (raw lines 23–67). These steps describe setup, not a successful authorization or capture.
- A separate recurring route is through **Bancontact Wallet Initiated Program (WIP)**. The page strongly recommends explicit shopper permission for future charges. WIP requires signup, eligibility and Support enablement, with transaction amount limits; first consent transaction uses SCA, subsequent WIP transactions do not, and the source states no liability shift on the first transaction because the issuer remains liable. Support is also needed to configure recurring tests (raw lines 69–98). None of this implies ordinary Bancontact card merchants have WIP enabled.
- To create a recurring token, send `storePaymentMethod: true` and a shopper reference of at least three characters in `/sessions` or `/payments`. **After settlement**, the `recurring.token.created` webhook supplies `storedPaymentMethodId`; the server must receive token lifecycle events. Later `/payments` use that ID and the same shopper reference with `ContAuth` and `Subscription` or `UnscheduledCardOnFile` (raw lines 99–124). The v72 TEST subscription request and language-specific library snippets are illustrative, not proof of a live charge or current compatibility (raw lines 126–463).
- The test section includes co-badged test cards, a `holderName: DECLINED` refusal fixture and a note that the Visa Debit example can route to Bancontact **or Visa depending on payment-method setup**. It separately directs readers to inspect test payments in Customer Area and add Bancontact card in the live Customer Area. Test credentials and examples do not establish live account setup or an actual payment outcome (raw lines 465–504).

## Detail locators

- Android card identity, v5.0.0 scope and earlier-guide pointer: raw lines 15–21.
- Sessions/Advanced prerequisites and base request/Component configuration: raw lines 23–67.
- WIP consent, enrollment, limits, first SCA, token creation and later token payment: raw lines 69–124.
- v72 TEST recurring examples by server language: raw lines 126–463.
- Test fixtures, conditional co-badged routing and live Customer Area setup: raw lines 465–504.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-bancontact|Bancontact card/mobile overview]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-card/android-component/2026-09-15|Bancontact card Android Component, fetched 2026-09-15]]
