---
title: "Stripe: Bank Redirects Overview"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/bank-redirects"
raw_files:
  - "stripe-payments-bank-redirects-2026-11-07.md"
  - "stripe-bank-redirects-2025.md"
tags: [stripe, bank-redirects, bancontact, blik, eps, fpx, ideal, p24, twint, pay-by-bank]
---

## Summary

Stripe's bank-redirect overview compares product and API support by method. Its **May 3, 2026** capture has seven product-table rows and eight API-table rows; the **November 7, 2026** capture has six product rows and seven API rows. TWINT appears in May but not November, and Pay by Bank appears only in the API table in both. This is a change in captured table coverage, not evidence that TWINT was withdrawn. The usual flow redirects a customer to the bank for authentication and returns them to the merchant, with BLIK marked as the no-browser-redirect exception. A return or support cell does not establish payment success or merchant capability activation. See [[stripe]] and [[stripe-bank-redirects]].

## Product support and dated matrix scope

All **six listed November product rows** (Bancontact, BLIK, EPS, FPX, iDEAL|Wero, P24) mark Connect, Checkout, Payment Links, Payment Element and Mobile Payment Element supported, and Express Checkout Element unsupported. The prior source's claim that **all eight** methods have those product cells overreached even the May table: Pay by Bank has no product row in either capture. The November matrix does not provide a TWINT product row, so its May row remains dated rather than erased. The matrix's broad cells are documentation labels, not account- or UI-variant guarantees.

- **BLIK:** May's product row marked Subscriptions, Invoicing and Customer Portal unsupported and attached Checkout setup/subscription exclusions. November marks all three products supported and omits those two Checkout footnotes. Both captures' BLIK Payment Element row still excludes collecting details before a PaymentIntent and **Elements with the Checkout Sessions API**. The November overview says Mobile Payment Element supported, while the same-date BLIK method overview marks an "in-app payments" category unsupported. The labels need integration-specific resolution; do not flatten them to a universal mobile claim. The November BLIK page describes reusable off-session mandate setup with bank-app approval, a 2,000 PLN per-charge recurring cap and account/bank qualifications; Connect requires active `blik_payments` and, for recurring, `blik_recurring_payments` on the platform and relevant connected accounts. See [[source-stripe-blik]].
- **Bancontact, EPS, FPX, P24:** November Subscriptions cells carry `send_invoice`-only footnote 7. Bancontact/EPS/P24 Invoicing is invite-only; FPX Invoicing is supported. EPS/FPX/P24 Checkout cells retain footnotes 1 and 2, excluding subscription and setup modes. These support cells do not imply automatic recurring charges.
- **iDEAL|Wero:** The November subscription cell is limited to Checkout subscription mode and carries the `send_invoice` footnote; footnote 6 excludes `charge_automatically` for subscriptions or invoices. Its Invoicing support also carries footnote 6. Preserve these separate conditions instead of treating it as generic subscription support.
- **TWINT:** May's product row listed Connect, Checkout, Payment Links, Payment Element and Mobile Payment Element supported, Express Checkout Element, Subscriptions, Invoicing and Customer Portal unsupported, and Checkout setup/subscription mode excluded. November does not include a TWINT row. Omission alone does not prove a runtime support change.

## API support and method-page conflicts

Every method **listed in each captured API table** supports PaymentIntents and excludes manual capture. BLIK is marked no browser redirect; the other listed methods require one. The general footnote says a `return_url` may be required for methods that redirect. EPS, FPX, P24 and Pay by Bank remain SetupIntents and `setup_future_usage` unsupported in the November table. iDEAL|Wero remains supported for both. TWINT's May API row said both supported but it has no November API row. Do not project May's TWINT row into the November table.

- **BLIK:** May's API row marked SetupIntents and `setup_future_usage` unsupported; November marks both supported, retaining the deferred-intent creation exclusion. The same-date November BLIK overview documents `setup_future_usage=off_session` on a PaymentIntent or `usage=off_session` on a SetupIntent with bank-app-authorized mandate, not universal account eligibility or a successful future charge. There is also a **May 3 same-date contradiction**: the May bank-redirect matrix said BLIK SetupIntents unsupported, while the separate May BLIK setup guide explicitly described Checkout `setup` mode and a BLIK SetupIntent without an initial charge. The May accept-payment guide's one-time Checkout path said payment mode only; that path does not erase the separate setup guide. The setup guide says bank support can vary and final setup/payment outcomes require webhooks. See [[source-stripe-blik-set-up-payment]], [[source-stripe-blik-accept-payment]] and [[source-stripe-blik-save-during-payment]].
- **Bancontact:** May's API row marked SetupIntents and future usage supported. November marks SetupIntents **unsupported** but future usage **supported**, with a footnote saying Bancontact can save bank details as a **SEPA Direct Debit** payment method. The same-date November Bancontact method overview marks both PaymentIntents with `setup_future_usage` and SetupIntents unsupported. Preserve this overview-versus-method-page conflict: native single-use Bancontact, a generated SEPA future-use route, and the method-page API cells are not interchangeable. Neither page alone resolves a merchant's exact setup path. See [[source-stripe-bancontact]] and [[stripe-bancontact]].

The November API footnote distinguishes card/bank-debit types that can support `on_session` and `off_session` from other methods that either do not support future usage or only support `off_session`. The matrix does not prove an exclusive `off_session` value for every listed method. Nor do these method labels demonstrate mandate completion, Checkout mode availability, or a live payment.

## Related method guides

- [[source-stripe-blik]] — BLIK overview and account/mandate conditions
- [[source-stripe-bancontact]] — Bancontact overview and same-date API conflict
- [[source-stripe-blik-set-up-payment]] — May 3, 2026 no-charge SetupIntent guide; conflicts with May matrix BLIK SetupIntents cell
- [[source-stripe-blik-accept-payment]] — May 3, 2026 one-time payment-mode guide
- [[source-stripe-blik-save-during-payment]] — May 3, 2026 recurring save-during-payment guide

## Raw Sources

- [[raw/stripe-payments-bank-redirects-2026-11-07|Bank-redirect overview — November 7, 2026 full capture]]
- [[raw/stripe-bank-redirects-2025|Bank-redirect overview — May 3, 2026 capture; filename retains 2025 suffix]]

## Related raw guide

- [[raw/stripe-blik-set-up-payment-2025|BLIK setup guide — May 3, 2026; same-date matrix conflict]]
