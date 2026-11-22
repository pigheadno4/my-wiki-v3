---
title: "Bank Redirects (Stripe)"
type: concept
category: technology
tags: [stripe, bank-redirects, bancontact, blik, eps, fpx, ideal, p24, twint, pay-by-bank]
---

## Definition

Bank redirects let customers pay online through bank authorization and usually return to the merchant after a browser redirect; BLIK is the no-browser-redirect exception. The May 3, 2026 overview covered seven product rows and eight API rows, including TWINT and API-only Pay by Bank. The November 7, 2026 capture has six product rows (Bancontact, BLIK, EPS, FPX, iDEAL|Wero, P24) and seven API rows (those six plus Pay by Bank), omitting TWINT from both. This is dated table coverage, not proof that TWINT support ended. See [[source-stripe-bank-redirects]].

Subscription and recurring support is method- and route-specific. The November 7, 2026 matrix marks BLIK Subscriptions supported, while the BLIK method page requires an authorized recurring mandate and capability activation. Bancontact/EPS/FPX/P24 subscription cells are `send_invoice` only; iDEAL|Wero is Checkout-subscription-mode-only and excludes `charge_automatically` for subscriptions or invoices. A matrix support cell does not prove a particular merchant's capability or a completed off-session payment.

## Methods and API Enums

| Method | Enum | SetupIntents | setup_future_usage | Redirect |
| --- | --- | --- | --- | --- |
| Bancontact | `bancontact` | No in November matrix (May: Yes) | Yes in November matrix, with generated SEPA Direct Debit footnote; same-date Bancontact page says no | Yes |
| BLIK | `blik` | Yes in November matrix (May: No; May setup guide: Yes) | Yes in November matrix (May: No); off-session recurring path in BLIK guide | No |
| EPS | `eps` | No | No | Yes |
| FPX | `fpx` | No | No | Yes |
| iDEAL\|Wero | `ideal` | Yes | Yes | Yes |
| P24 | `p24` | No | No | Yes |
| Pay by Bank | `pay_by_bank` | No | No | Yes |
| TWINT | `twint` | May 3 matrix: Yes; no November row | May 3 matrix: Yes; no November row | May 3 matrix: Yes; no November row |

The May Bancontact setup/save guides separately document generated SEPA Direct Debit paths. November's hub future-use checkmark with a generated-SEPA footnote conflicts with the same-date method overview's unsupported future-use cell; it does not establish current account eligibility or completed mandate setup. The API footnote does not impose an exclusive `off_session` value on every listed method.

BLIK is the only bank redirect that does **not** require a browser redirect.

## Product Support Notes

- **Express Checkout Element**: unsupported for every method listed in both captured product tables; Pay by Bank has no product row and TWINT has no November row.
- **Checkout modes**: November EPS/FPX/P24 retain footnotes excluding setup and subscription modes. The May BLIK row also had those footnotes, but November BLIK does not. Its separate May accept-payment guide covered a one-time payment-mode path while its same-date setup guide documented Checkout setup mode; no single row resolves all guide routes. TWINT has only a May row with those exclusions.
- **Subscriptions**: November BLIK supported, with mandate/capability conditions in its method page; Bancontact/EPS/FPX/P24 `send_invoice` only; iDEAL|Wero Checkout subscription mode only plus `send_invoice`, excluding `charge_automatically`. TWINT's May row was unsupported and is absent in November.
- **Invoicing and portal**: November BLIK Invoicing and Customer Portal supported; May row marked both unsupported. November Bancontact/EPS/P24 Invoicing invite-only, FPX supported, iDEAL|Wero supported without `charge_automatically`; TWINT's May row said unsupported and November omits it.
- **BLIK Payment Element**: November footnotes still exclude collecting details before PI creation and Elements with the Checkout Sessions API. The bank-redirects table says Mobile Payment Element supported, while the same-date BLIK method overview says its in-app category unsupported; keep this apparent terminology/scope conflict visible. BLIK's deferred-intent creation path remains excluded in the November API footnote.

**Method-page conflicts**: November's hub marks Bancontact/EPS/P24 Invoicing invite-only. The November Bancontact method overview lists `send_invoice` collection without resolving account-specific gating. The EPS method overview lists Invoicing supported with a `send_invoice` footnote whose attachment is unclear and marks recurring and off-session payments unsupported. The same-date P24 method overview marks Billing and Invoicing supported and prints a `send_invoice`-only note after its matrix. The P24 hub row preserves invite-only Invoicing and Checkout setup/subscription-mode exclusions. Per-invoice collection does not establish automatic recurring charging or an invitation waiver. See [[source-stripe-bancontact]], [[source-stripe-eps]] and [[source-stripe-p24]].

The May FPX legacy Elements guide said Billing and recurring/additional payments were unsupported, despite the May hub's `send_invoice` subscription cell. The November FPX overview marks Billing/Invoicing supported with a `send_invoice` footnote while recurring, off-session, SetupIntents and future usage remain unsupported. Its November acceptance capture is only variant navigation. Keep the route-specific conflict; the broad Billing cell does not authorize automatic recurring charges. See [[source-stripe-fpx]] and [[source-stripe-fpx-accept-payment]].

## Sources

- [[source-stripe-bank-redirects]] — May 3 and November 7, 2026 product/API matrices: method-specific footnotes, BLIK and Bancontact changes, and TWINT's November row omission
- [[source-stripe-bancontact]] — Bancontact overviews (2026-05-03 and 2026-11-07): updated refund and eligibility boundaries and dated setup conflict
- [[source-stripe-blik]] — May 3 and November 7, 2026 BLIK overviews: reusable mandate path, operational limits, and route-specific support qualifications
- [[source-stripe-fpx]] — May 3 and November 7, 2026 FPX overviews: MY/MYR, dated refund change, B2C/B2B bounds, send_invoice-only Billing scope
