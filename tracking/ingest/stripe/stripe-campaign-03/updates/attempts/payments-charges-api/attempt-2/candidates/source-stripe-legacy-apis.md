---
title: "Stripe Legacy APIs"
type: source
date_ingested: 2026-04-20
date_updated: 2026-11-15
canonical_url: "https://docs.stripe.com/payments/charges-api"
original_format: webpage
raw_files:
  - "stripe-payments-charges-api-2026-11-07.md"
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

[[stripe]] reference to legacy Charges, Tokens and Sources APIs and migration paths. The 2026-11-07 Charges page now deprecates **card-payment creation** on Charges, says Stripe plans to remove that support and bars new integrations from creating payments through Charges. It gives no removal date or general shutdown of Charge retrieval/refunds. Other API status claims below retain their separate April 2026 sources.

## Key Takeaways

- **Sources API** (local payment methods): deprecated + **being turned off** — migration required
- **Sources API** (card payments): deprecated but not being turned off
- **Charges API (dated conflict)**: the 2026-04-20 older-APIs page said Charges remained available and was not going away; a separate April comparison said Charges was not being deprecated. The 2026-11-07 Charges page instead deprecates **creating card payments** on Charges, plans to remove that support, and says **new integrations cannot use Charges to create payments**. No date or fate of existing read/refund operations is given. These claims have different dates and scopes.
- **ACH (old) API**: the 2026-04-20 older-APIs page said it remained available without future development; the November Charges page does not address ACH
- **Current APIs**: Payment Intents + Setup Intents + Payment Methods — SCA-ready, Terminal support, all future features

## Charges API vs Payment Intents API

| Step | Charges API (legacy) | Payment Intents API |
| --- | --- | --- |
| 1 | Collect payment info via Elements | Create PaymentIntent server-side |
| 2 | Tokenize via Stripe.js → token | Send client_secret to client |
| 3 | Send token to server | Collect payment info via Elements |
| 4 | Create Charge server-side | Handle 3DS client-side via Stripe.js |
| 5 | Fulfill on success | Fulfill via webhook on success |

Charges API does **not** support: SCA, India businesses, bank-requested card authentication. In the legacy flow, browser Elements data is tokenized by Stripe.js; the token goes to the merchant server for Charge creation, and fulfillment follows **successful payment**, not mere token or Charge request creation. PaymentIntents are created server-side, the client receives a client secret and handles 3DS with Stripe.js/mobile SDK, and the comparison directs fulfillment from success webhooks. These are actor and outcome boundaries, not executable authorization for a new Charges integration.

## Other Details (Charges API)

- **Refunds**: the April Node example uses `stripe.refunds.create({ charge: id, amount?: cents })`; November shows equivalent server-side secret-key curl to `POST /v1/refunds` with a Charge ID and optional integer `amount` in the currency's minor unit. A refund request example is not evidence of successful refund.
- **Apple Pay (legacy)**: `PKPayment → createToken → Charge` (new path uses PaymentIntent)
- **Dynamic statement descriptor**: 22 char limit; dynamic portion appended with `*` separator; Stripe allots 10 chars each side; use Dashboard "shortened descriptor" (2–10 chars) to give more room to dynamic portion
- **Metadata**: supported; use with Radar rules; do not store PII or card details in metadata or Charge `description`. For PaymentIntents, read/update `metadata` and `description` on the **PaymentIntent**: the corresponding Charge fields are not guaranteed to stay consistent. A Charge metadata value is not a substitute for PaymentIntent state.
- **Declines**: inspect the failed-payment API error and, where provided, its Charge ID to retrieve `outcome`; `charge.failed` webhooks signal unsuccessful charges. Do not infer success from tokenization or an attempted request.

**Example surface:** November changes the refunds, descriptor and metadata illustrations from April Node SDK snippets to curl with a secret key; it does not say the SDK is deprecated. The Apple Pay legacy example still converts a `PKPayment` through `createTokenWithPayment` into a Token and then a server Charge. That example does not override the new-integration bar.

## Charges vs Payment Intents: Historical comparison

The following use-case table comes from the separate 2026-04-20 Charges-versus-PaymentIntents guide. It describes legacy/existing Charges integrations; it is **not** a recommendation or permission for a new US/Canada Charges integration after the 2026-11-07 card-payment-creation deprecation notice.

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

The 2026-04-20 Sources API guide marks **accepting local payment methods through the Sources API route** as deprecated and planned for removal; migrate that route to the Payment Methods API. Its push-method table names Alipay, Bancontact, giropay, iDEAL, Przelewy24, WeChat Pay, Sofort and Multibanco in the Sources context. This notice does not say those payment methods themselves are unavailable through current APIs.

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

- [[raw/stripe-payments-charges-api-2026-11-07]] — 2026-11-07 full Charges page (160 lines); scoped card-payment-creation deprecation and new-integration bar.
- [[raw/stripe-older-apis-2025]] — migration notice: Sources/Charges/ACH deprecation status
- [[raw/stripe-charges-api-legacy-2025]] — Charges API: flow comparison, refunds, Apple Pay, statement descriptors, metadata, declines
- [[raw/stripe-payment-intents-migration-2025]] — Charges→PaymentIntents migration: incremental approach, confirmCardPayment, setup_future_usage, confirmCardSetup, off-session flagging, test cards
- [[raw/stripe-sources-api-2025]] — Sources API concepts: 4 characteristics (pull/push, flow, usage, sync/async), 4 flow types, single-use vs reusable, async pending→webhook pattern; deprecated local-payment-method acceptance is scoped to the Sources API route
- [[raw/stripe-sources-to-payment-methods-migration-2025]] — Sources/Tokens→PaymentMethods migration: 3 paths (Checkout/Element/own form), stateless PaymentMethod vs stateful Source, 48h requires_action timeout, webhook mapping, reusable legacy method migration tool, legacy card backward-compat
- [[raw/stripe-charges-vs-payment-intents-2025]] — Charges vs PaymentIntents: 3 API options, Charges = US/Canada simple cards not SCA-ready, PI = all methods + SCA + Terminal; charge object read migration field mapping; brand/Google Pay rename
- [[raw/stripe-upgrade-integration-2025]] — Integration upgrade map: Card Element→Payment Element, Legacy Checkout→Checkout/Payment Links, Payment Request Button→Express Checkout Element, Manual→Dynamic payment methods
