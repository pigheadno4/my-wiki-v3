---
title: "Stripe Legacy APIs"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-older-apis-2025.md"
  - "stripe-charges-api-legacy-2025.md"
  - "stripe-payment-intents-migration-2025.md"
  - "stripe-sources-api-2025.md"
  - "stripe-sources-to-payment-methods-migration-2025.md"
  - "stripe-charges-vs-payment-intents-2025.md"
  - "stripe-upgrade-integration-2025.md"
tags: [stripe, legacy, charges-api, sources-api, payment-intents, migration]
---

## Summary

Stripe's legacy payment APIs (Charges, Tokens, Sources) and their migration paths to current APIs. Thin reference — captured for completeness and raw file linkage.

## Key Takeaways

- **Sources API** (local payment methods): deprecated + **being turned off** — migration required
- **Sources API** (card payments): deprecated but not being turned off
- **Charges + ACH APIs**: unsupported but not being removed; no future development
- **Current APIs**: Payment Intents + Setup Intents + Payment Methods — SCA-ready, Terminal support, all future features

## Charges API vs Payment Intents API

| Step | Charges API (legacy) | Payment Intents API |
| --- | --- | --- |
| 1 | Collect payment info via Elements | Create PaymentIntent server-side |
| 2 | Tokenize via Stripe.js → token | Send client_secret to client |
| 3 | Send token to server | Collect payment info via Elements |
| 4 | Create Charge server-side | Handle 3DS client-side via Stripe.js |
| 5 | Fulfill on success | Fulfill via webhook on success |

Charges API does **not** support: SCA, India businesses, bank-requested card authentication.

## Other Details (Charges API)

- **Refunds**: `stripe.refunds.create({ charge: id, amount?: cents })`
- **Apple Pay (legacy)**: `PKPayment → createToken → Charge` (new path uses PaymentIntent)
- **Dynamic statement descriptor**: 22 char limit; dynamic portion appended with `*` separator; Stripe allots 10 chars each side; use Dashboard "shortened descriptor" (2–10 chars) to give more room to dynamic portion
- **Metadata**: supported; use with Radar rules; do not store PII

## Charges vs Payment Intents: When to Use Which

| | Charges API | Payment Intents API |
| --- | --- | --- |
| Use case | US/Canada simple card-only integrations | All products, all payment methods |
| SCA ready | No | Yes |
| Terminal (in-person) | No | Yes |
| New features | No | Yes (only here) |

**Charge object read migration** — `charge.payment_method_details` + `charge.billing_details` provide a consistent read path for charges from either API:

| Old | New |
| --- | --- |
| `charge.source` | `charge.payment_method_details` |
| `charge.source.id` | `charge.payment_method` |
| `charge.source.name` | `charge.billing_details.name` |
| `charge.source.address_zip` | `charge.billing_details.address.postal_code` |
| `charge.source.brand: "MasterCard"` | `charge.payment_method_details.card.brand: "mastercard"` |
| `tokenization_method: "android_pay"` | `card.wallet.type: "google_pay"` |
| `charge.source.type == 'three_d_secure'` | `charge.payment_method_details.card.three_d_secure.succeeded` |

## Sources → Payment Methods Migration

**Key conceptual shift**: `Source` is stateful (has `status`); `PaymentMethod` is stateless — the PaymentIntent owns the state.

**3 migration paths** (complexity order):

| Path | Complexity | Server | Client |
| --- | --- | --- | --- |
| Stripe Checkout | Low | Create CheckoutSession | Not needed |
| Payment Element | Medium | Create PaymentIntent | Render Payment Element with client_secret |
| Own form | High | Create PaymentIntent | Custom form + JS SDK |

**Key details:**

- `requires_action` → 48h timeout → auto-transitions to `requires_payment_method`
- Webhook: `source.chargeable/failed/canceled` → not applicable; `charge.succeeded` still fires (no forced update), also listen to `payment_intent.succeeded`
- **Reusable legacy methods** (Alipay, Bacs DD, SEPA DD): don't auto-migrate — use Dashboard data migration tool
- **Legacy cards/tokens saved to Customer**: backward-compatible with Payment Methods API — same underlying object, no migration needed
- Store both `Charge ID` and `PaymentIntent ID` going forward (fetch Charge ID from `latest_charge`)

## Integration Upgrade Map

| Legacy | Recommended | Key benefit |
| --- | --- | --- |
| Card Element | Payment Element | 100+ payment methods; dynamic presentment by location/currency |
| Legacy Checkout | Checkout or Payment Links | Adaptive Pricing, Dynamic payment methods, embed or redirect |
| Payment Request Button | Express Checkout Element | Apple Pay + Amazon Pay + Google Pay + Link + PayPal simultaneously |
| Manual payment methods | Dynamic payment methods | Dashboard-managed; Stripe selects eligible methods per transaction |

## Related Pages

- [[stripe]] — Stripe company page (API Deprecations table)
- [[source-stripe-payment-intents]] — current Payment Intents API

## Sources API Concepts

4 characteristics classify every Source object:

| Characteristic | Values | Notes |
| --- | --- | --- |
| Pull vs Push | Pull = merchant debits customer; Push = customer sends funds | Cards = pull; iDEAL/Sofort/ACH Credit = push |
| Flow | none / redirect / code verification / receiver | Determines customer action required before source is chargeable |
| Usage | `single_use` / `reusable` | Single-use → `consumed` after charge; reusable must be attached to Customer |
| Confirmation | synchronous / asynchronous | Async charge starts `pending`; webhook required for fulfillment |

**Receiver flow detail**: if not fully charged, funds credited to balance after 60 days. If source becomes chargeable but no charge is made, source is canceled and payment refunded automatically.

All push payment methods (Alipay, Bancontact, giropay, iDEAL, Przelewy24, WeChat Pay, Sofort, Multibanco) are now **deprecated**.

## Migration Guide (Charges → Payment Intents)

- **Incremental migration** is safe — run both APIs in parallel during transition
- **API version rename** (pre-2019-02-11): `requires_source` → `requires_payment_method`; `requires_source_action` → `requires_action`
- **Elements migration**: server creates PI → client calls `confirmCardPayment` → fulfill via `payment_intent.succeeded` webhook
- **Saving cards in checkout**: set `setup_future_usage` (`on_session` / `off_session`) on the PaymentIntent
- **Saving cards outside checkout**: use SetupIntent + `confirmCardSetup` instead of `createToken`/`createSource`
- **Off-session payments**: must explicitly flag + pass payment method ID (no default source fallback)
- **Access saved methods**: use `list payment methods` API — `customer.sources` won't include new PaymentMethods
- **Regulatory test cards**: 4000002500003155 (auth on first), 4000002760003184 (always), 4000008260003178 (auth then insufficient_funds), 4000000000003055 (supports but not required)

## Raw Sources

- [[stripe-older-apis-2025]] — migration notice: Sources/Charges/ACH deprecation status
- [[stripe-charges-api-legacy-2025]] — Charges API: flow comparison, refunds, Apple Pay, statement descriptors, metadata, declines
- [[stripe-payment-intents-migration-2025]] — Charges→PaymentIntents migration: incremental approach, confirmCardPayment, setup_future_usage, confirmCardSetup, off-session flagging, test cards
- [[stripe-sources-api-2025]] — Sources API concepts: 4 characteristics (pull/push, flow, usage, sync/async), 4 flow types, single-use vs reusable, async pending→webhook pattern; all push methods deprecated
- [[stripe-sources-to-payment-methods-migration-2025]] — Sources/Tokens→PaymentMethods migration: 3 paths (Checkout/Element/own form), stateless PaymentMethod vs stateful Source, 48h requires_action timeout, webhook mapping, reusable legacy method migration tool, legacy card backward-compat
- [[stripe-charges-vs-payment-intents-2025]] — Charges vs PaymentIntents: 3 API options, Charges = US/Canada simple cards not SCA-ready, PI = all methods + SCA + Terminal; charge object read migration field mapping; brand/Google Pay rename
- [[stripe-upgrade-integration-2025]] — Integration upgrade map: Card Element→Payment Element, Legacy Checkout→Checkout/Payment Links, Payment Request Button→Express Checkout Element, Manual→Dynamic payment methods
