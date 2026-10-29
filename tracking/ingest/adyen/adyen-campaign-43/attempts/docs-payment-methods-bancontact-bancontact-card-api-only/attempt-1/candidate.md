---
title: "Adyen Bancontact card API-only"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-card/api-only"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-card/api-only/2026-09-15.md"
tags: [adyen, bancontact, card, api-only, pci, 3d-secure, recurring]
---

## Overview

Adyen's Bancontact card API-only guide was last modified in 2019 and captured on 2026-09-15. It describes a merchant-built Web checkout that collects raw Bancontact card data, submits a server-side card payment, redirects for mandatory 3D Secure, and optionally uses the separately enabled Bancontact Wallet Initiated Program (WIP) for tokenized recurring payments. It is a card route, not Bancontact mobile app or QR guidance. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Raw card collection requires the merchant to be fully PCI compliant and to have an API-only Advanced integration and Bancontact card added in test Customer Area. The page directs merchants without full PCI compliance to Web or Android Bancontact card Components. Card number and expiry month/year are required in the form; holder name is shown as optional there. Bancontact itself has no CVC, although one can appear for co-badged cards. 3D Secure is mandatory and separate captures are unsupported (raw lines 19-49).
- For method discovery, the page says call `/paymentMethods` with `countryCode: BE` and `amount.currency: EUR`; required fields appear under method type `bcmc` (raw lines 51-56). For the server-side `/payments` request, prose instead says `paymentMethod.type: scheme` with `paymentMethod.brand: bcmc`, plus card number/expiry/holder name, Web `browserInfo` and a post-3DS return URL (raw lines 60-82). The principal TEST payment examples show `type: scheme` but omit `brand: bcmc`, while the later decline example uses `type: bcmc`; do not treat either snippet as a complete authoritative replacement for the prose or assume routing from the examples alone (raw lines 86-110, 915-932).
- The payment response is shown as `RedirectShopper` with a `redirect` action. Redirect the shopper for 3D Secure, then use `/payments/details` resultCode for shopper messaging and an asynchronous webhook for the payment outcome. The page lists `Authorised`, `Cancelled`, `Error` and `Refused` result handling; a redirect action is not authorization or capture (raw lines 468-505).
- WIP provides Bancontact One-Click Pay and merchant-initiated recurring/subscription routes only after signup and Support enablement; the page says not every company is eligible and amount limits apply. It describes first-transaction shopper consent and SCA, with subsequent transactions not requiring SCA, and states issuer liability for that first transaction. Treat these as WIP-scoped source claims, not general Bancontact card or current issuer guarantees (raw lines 507-535).
- For WIP token creation, the page instructs `storePaymentMethod: true` and `shopperReference` in `/sessions` or `/payments`; the `recurring.token.created` webhook containing `storedPaymentMethodId` arrives when the initial payment has settled. Later `/payments` use the stored ID, same shopper reference, `ContAuth`, and `Subscription` or `UnscheduledCardOnFile`. The example uses `paymentMethod.type: bcmc` for the stored-token payment; that is a later WIP path, not the initial raw-card request shape (raw lines 537-587).
- TEST co-badged fixtures can route to Bancontact or Visa depending on payment-method setup; a forced-decline fixture is also shown. Live Bancontact card must be added separately in live Customer Area. TEST examples, historic library snippets and the captured page do not establish current merchant eligibility, PCI compliance or live payment operation (raw lines 903-936).

## Detail locators

- Card/PCI prerequisites, CVC, 3DS and capture limitations: raw lines 19-49.
- Discovery versus initial `/payments` field instructions and raw-card examples: raw lines 51-466.
- Redirect, details result and asynchronous outcome: raw lines 468-505.
- WIP eligibility, first SCA/consent, token settlement and subsequent request: raw lines 507-901.
- TEST cards, route-dependent co-badge, forced decline and live setup: raw lines 903-936.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-card/api-only/2026-09-15|Bancontact card API-only guide (2019-modified, 2026-09-15 capture)]]
