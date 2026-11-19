---
title: "Stripe — Incremental Authorization (Online)"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/incremental-authorization"
raw_files:
  - "stripe-incremental-authorization-2026.md"
tags: [stripe, incremental-authorization, capture, payment-intents, checkout, ic-plus, sca, visa, mastercard]
---

## Summary

[[stripe]] incremental authorization increases the authorized amount on a **confirmed, uncaptured PaymentIntent** before capture. The detailed workflow and constraints below come from the 2026-05-11 three-variant guide; the 2026-11-07 base-URL capture is only an index of Stripe-hosted, full embedded, and advanced web variants. The linked November variants were not captured here, so this index does not renew the May eligibility, sample code, or API claims. See [[stripe-incremental-authorization]].

## Statement Behavior

- Before capture, each successful increment appears as a separate pending card statement entry (for example, a 10 USD authorization incremented to 15 USD appears as 10 USD plus 5 USD pending entries).
- After capture, the pending entries are removed and one final captured-amount entry appears. This describes statement presentation, not settlement or funds availability.

## Availability (2026-05-11 guide)

Stripe describes this as an **IC+ pricing** feature; standard-pricing users are directed to contact support for access. Card network, merchant country, payment type, category, and issuer conditions apply. Requesting the feature does not establish account eligibility.

| Network | Merchant country | Payment type | Merchant categories or qualification |
| --- | --- | --- | --- |
| Visa | Global | All card payment types | All categories |
| Mastercard | Global except MX users and JPY transactions for JP users | All card payment types | All categories |
| American Express | Global | All card payment types | All categories; some issuers return `unavailable` |
| Discover | Global | All card payment types | Listed travel, transportation, grocery, EV charging, dining, rental, parking, amusement, and recreation categories |
| Discover | Global | Card not present | Taxicabs and limousines |
| Diners Club (beta, through Discover) | US, CA, UK | Card present | Listed travel and entertainment categories |
| Diners Club (beta, through Discover) | Global | Card not present | Listed categories including taxicabs and limousines |
| UnionPay and JCB (beta, through Discover) | Global | Card not present | Listed categories including taxicabs and limousines |

The detailed category inventory is in the May raw at `raw/stripe-incremental-authorization-2026.md:28-55,605-632`. The guide says an attempt outside its criteria errors. Its leading bullet lists only Visa, Mastercard, American Express, and Discover, followed by the separate limited-support beta rows; do not treat the beta rows as universal current access.

## Prerequisites and integration paths (2026-05-11 guide)

- For **Stripe-hosted Checkout**, the guide requires a server-created Checkout Session with `mode=payment` and `capture_method=manual`, requests `payment_method_options.card.request_incremental_authorization=if_available`, then redirects to the Session URL. Its hosted example also includes embedded mount/return material; keep those UI instructions scoped to their respective variants.
- For **full embedded Checkout**, the guide again requires `mode=payment` and manual capture, sets `ui_mode=embedded_page`, returns the Session `client_secret` from the server, and mounts Checkout with Stripe.js or React. The return page can retrieve Session status (`complete` or `open` in the example), but a return or completed Session is not evidence of a later increment or capture.
- For the **advanced/Elements path**, the guide creates and confirms a card PaymentIntent with `capture_method=manual` and `request_incremental_authorization=if_available`. Increment only after confirmation while it remains uncaptured; use the PaymentIntent update method instead to adjust amount before confirmation. The guide also describes `never` as disabling future increments.
- **Internal sample conflict**: the May prose explicitly requires `capture_method=manual` for Checkout, while its hosted and embedded Checkout Session creation snippets omit that parameter. Preserve the prose prerequisite; the snippets do not demonstrate that automatic capture works.

After the Checkout Session or PaymentIntent confirmation, check the **latest Charge** at `latest_charge.payment_method_details.card.incremental_authorization.status` for `available` or `unavailable`. The May guide says it is `unavailable` if the feature was not requested. `if_available` is a request, not proof of support.

## Increment and capture (2026-05-11 guide)

Call `POST /v1/payment_intents/{id}/increment_authorization` on the confirmed, uncaptured PaymentIntent with `amount` equal to the **new total authorization**, not the increment delta. The May guide allows a maximum of **10 incremental authorization attempts per PaymentIntent**, including failed attempts; it does not promise ten successful increments. Each individual increment is capped at the greater of 500 USD (or local equivalent) above, or 500% above, the previously authorized amount.

A successful increment returns a PaymentIntent with the increased amount. On `card_declined`, the previous authorized amount remains capturable and accompanying updates to fields such as metadata, application fee, transfer data, description, and descriptor are not saved. Capture separately with the PaymentIntent capture endpoint before the **original** authorization expires; increments do not extend its validity period. Neither a feature-availability status nor an increased authorization demonstrates capture, settlement, or funds availability.

## SCA and customer disclosure (2026-05-11 guide)

When both business and cardholder are in SCA countries, the May guide says requesting the feature at initial authorization configures the payment method for future off-session use. Initial authorization requires 3DS; later increments are merchant-initiated and may be SCA-exempt, but merchant-initiated transactions do not benefit from the described 3DS liability shift. Disclose saved off-session use during the initial transaction. The guide separately discusses customer agreement, records, estimated-amount notice, and network-rule compliance; these remain dated guidance, not a current legal determination.

## Related

- [[stripe-terminal-incremental-authorizations]] — separate in-person Terminal variant.
- [[stripe-extended-authorization]] — separate feature for a longer authorization window.

## Raw Sources

- [[raw/stripe-incremental-authorization-2026|2026-05-11 detailed guide]] — full historical capture of all three UI variants (771 lines); factual source for this page.

## Related raw API references

- [[raw/stripe-payments-incremental-authorization-2026-11-07|2026-11-07 base-URL variant index]] — navigation-only capture listing Stripe-hosted, full embedded, and advanced web URLs; the variant pages themselves were not read and this index supplies no refreshed behavior or API evidence.
