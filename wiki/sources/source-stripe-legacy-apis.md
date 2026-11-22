---
title: "Stripe Legacy APIs"
type: source
date_ingested: 2026-04-20
date_updated: 2026-11-22
canonical_url: "https://docs.stripe.com/payments/charges-api"
original_format: webpage
raw_files:
  - "stripe-payments-older-apis-2026-11-07.md"
  - "stripe-payments-payment-intents-migration-2026-11-07.md"
  - "stripe-payments-payment-intents-migration-charges-2026-11-07.md"
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

[[stripe]] reference for legacy Charges, Tokens and Sources and migration to Payment Intents, Setup Intents and Payment Methods. The gateway is the dedicated Charges guide. The three separately captured routes below have their own dates and scopes.

## Key Takeaways

The [Older APIs overview](https://docs.stripe.com/payments/older-apis) captured 2026-04-20 and 2026-11-07 gives the same general guidance. It says Stripe stopped updating documentation for some replaced APIs, recommends the current Intent and Payment Methods APIs, and groups them as broader in payment-method coverage with SCA readiness, Terminal and future development. The comparison lists cards and ACH for the Charges, Tokens and Sources group. These are group-level comparisons. The separate April Charges comparison describes a broader historical Charges route for cards and all methods available through Sources.

- **Charges.** Both Older APIs captures say unsupported Charges can still be used pending upgrade. The April Charges comparison also says Charges was not being deprecated. The dedicated Charges guide and [Charges versus Payment Intents comparison](https://docs.stripe.com/payments/payment-intents/migration/charges), both captured 2026-11-07, deprecate **using Charges to create card payments**, state a plan to remove that support and bar new integrations from creating payments through Charges. New integrations are directed to Checkout or Payment Intents. The creation notice gives no removal date or general shutdown for Charge retrieval and refunds.
- **Sources for local methods.** Both Older APIs captures describe deprecated acceptance through Sources, a planned shutoff, required migration and more details by email. Local-payment-method availability through current APIs is a separate question.
- **Sources for cards and legacy Cards.** Both Older APIs captures describe Sources card acceptance as deprecated with no then-current shutoff plan. The separate [November transition guide](https://docs.stripe.com/payments/payment-methods/transitioning) instead plans to stop Sources card acceptance and legacy Cards support, requires migration for Sources card payments and says Stripe will send email. The dedicated [November Sources guide](https://docs.stripe.com/sources) broadly requires existing Sources users to migrate and bars new integrations from using Sources. The [detailed November card migration](https://docs.stripe.com/payments/payment-methods/migrate-from-legacy-cards-sources) separately covers ending creation of Card or Source objects, including creation through Tokens, and their use for payments. These notices leave specific timing, email delivery and account enforcement unverified.
- **Legacy ACH.** Both Older APIs captures describe older ACH as usable by existing users pending upgrade. The dedicated [November ACH with Charges guide](https://docs.stripe.com/ach-deprecated) blocks new legacy onboarding, directs new integrations to current ACH Direct Debit and recommends Payment Intents migration for existing integrations. The separate November card Charges guide does not cover ACH.

## Card-payment flow in the dedicated Charges guide

| Step | Charges API (legacy) | Payment Intents API |
| --- | --- | --- |
| 1 | Collect payment info via Elements | Create PaymentIntent server-side |
| 2 | Tokenize via Stripe.js → token | Send client_secret to client |
| 3 | Send token to server | Collect payment info via Elements |
| 4 | Create Charge server-side | Handle 3DS client-side via Stripe.js |
| 5 | Fulfill on success | Fulfill via webhook on success |

Charges API does **not** support: SCA, India businesses, bank-requested card authentication. In the legacy flow, browser Elements data is tokenized by Stripe.js; the token goes to the merchant server for Charge creation, and fulfillment follows **successful payment**, not mere token or Charge request creation. PaymentIntents are created server-side, the client receives a client secret and handles 3DS with Stripe.js/mobile SDK, and the dedicated guide directs fulfillment from success webhooks. These are actor and outcome boundaries, not executable authorization for a new Charges integration.

## Other Details (Charges API)

- **Refunds**: the April Node example uses `stripe.refunds.create({ charge: id, amount?: cents })`; November shows equivalent server-side secret-key curl to `POST /v1/refunds` with a Charge ID and optional integer `amount` in the currency's minor unit. A refund request example is not evidence of successful refund.
- **Apple Pay (legacy)**: `PKPayment → createToken → Charge` (new path uses PaymentIntent)
- **Dynamic statement descriptor**: 22 char limit; dynamic portion appended with `*` separator; Stripe allots 10 chars each side; use Dashboard "shortened descriptor" (2–10 chars) to give more room to dynamic portion
- **Metadata**: supported; use with Radar rules; do not store PII or card details in metadata or Charge `description`. For PaymentIntents, read/update `metadata` and `description` on the **PaymentIntent**: the corresponding Charge fields are not guaranteed to stay consistent. A Charge metadata value is not a substitute for PaymentIntent state.
- **Declines**: inspect the failed-payment API error and, where provided, its Charge ID to retrieve `outcome`; `charge.failed` webhooks signal unsuccessful charges. Do not infer success from tokenization or an attempted request.

**Example surface:** November changes the refunds, descriptor and metadata illustrations from April Node SDK snippets to curl with a secret key; it does not say the SDK is deprecated. The Apple Pay legacy example still converts a `PKPayment` through `createTokenWithPayment` into a Token and then a server Charge. That example does not override the new-integration bar.

## Charges vs Payment Intents: Historical comparison

The use-case table comes from the 2026-04-20 Charges versus Payment Intents comparison. It describes an existing simpler cards use case for merchants with mainly US or Canadian customers, lists both APIs on Web, iOS and Android, and describes legacy Charges as supporting cards and all methods on Sources. The 2026-11-07 capture of that comparison replaces the table with the card-creation deprecation and new-integration bar, names India businesses, bank-requested authentication and SCA as unsupported on Charges, and describes hosted, embedded and Elements-backed Checkout. The historical table supplies no new-integration permission.

| | Charges API | Payment Intents API |
| --- | --- | --- |
| Use case | Simple card acceptance for mainly US/Canada customers | Multiple methods and cards requiring authentication |
| SCA ready | No | Yes |
| Terminal (in-person) | No | Yes |
| New features | No | Yes (only here) |

**Charge object read migration.** Both comparison captures advise updating existing Charge readers before incrementally changing payment creation flows. The guide says the two top-level fields `charge.payment_method_details` and `charge.billing_details` are available across API versions for Charges created through either API. The method identifier is the separate `charge.payment_method` field. Availability of those top-level fields establishes neither nested schema parity across versions nor non-null data on a particular Charge.

| Old card/bank-account shape | Old Sources shape | Common Charge read |
| --- | --- | --- |
| `charge.source` | `charge.source` | `charge.payment_method_details` |
| `charge.source.id` | `charge.source.id`, or `charge.source.three_d_secure.card` for a 3DS Source | `charge.payment_method` |
| `charge.source.name` | `charge.source.owner.name` | `charge.billing_details.name` |
| `charge.source.address_zip` | `charge.source.owner.address.postal_code` | `charge.billing_details.address.postal_code` |
| `charge.source.brand: "MasterCard"` | `charge.source.card.brand: "MasterCard"` | `charge.payment_method_details.card.brand: "mastercard"` |
| `charge.source.tokenization_method: "android_pay"` | `charge.source.card.tokenization_method: "android_pay"` | `charge.payment_method_details.card.wallet.type: "google_pay"` |

**Historical 3DS row.** Both comparisons place `charge.source.object == 'source' && charge.source.type == 'three_d_secure'` beside `charge.payment_method_details.card.three_d_secure.succeeded`. The former tests the legacy object shape and type. The latter is a historical boolean. The separate [3DS Charge changelog](https://docs.stripe.com/changelog/2020-08-27/updates-3d-scure-charge-object) says `succeeded` and `authenticated` were removed in favor of `result`, and links Charge and SetupAttempt REST definitions for API version `2024-06-20`. See [[source-stripe-3d-secure-authentication-flow]] for the November enum evidence. The Source type check does not establish authentication or equate to `three_d_secure.result=authenticated`. The enum reports authentication outcome. Payment authorization, capture, success and settlement are separate.

## Sources → Payment Methods Migration

**Key conceptual shift**: `Source` is stateful (has `status`); `PaymentMethod` is stateless — the PaymentIntent owns the state.

**April local-method transition paths** (complexity order):

| Path | Complexity | Server | Client |
| --- | --- | --- | --- |
| Stripe Checkout | Low | Create CheckoutSession | Not needed |
| Payment Element | Medium | Create PaymentIntent | Render Payment Element with client_secret |
| Own form | High | Create PaymentIntent | Custom form + JS SDK |

**Key details:**

- The 2026-04-20 local-payment-method transition says incomplete customer authorization after 48 hours moves the PaymentIntent from `requires_action` to `requires_payment_method` and permits another confirmation attempt. The 2026-11-07 card-oriented transition describes incomplete authorization and requires server retrieval or server webhook verification, with no 48-hour rule stated there. A browser return alone does not verify status.
- Webhook: `source.chargeable/failed/canceled` → not applicable; `charge.succeeded` still fires (no forced update), also listen to `payment_intent.succeeded`
- **Reusable local Sources**. The April local-method guide describes migration through its Dashboard data migration tool for reusable legacy methods such as Alipay, Bacs Direct Debit and SEPA Direct Debit.
- **Saved legacy cards**. The 2026-04-20 transition describes a compatible saved Card as a Payment Methods view of the same object and shows its ID in `payment_method` with the matching Customer. The separate November detailed card migration says unmigrated Card/Source IDs can no longer be passed in `payment_method`, and describes the transitional PaymentIntent `source` parameter, explicitly undocumented, plus `customer` if attached. Its tool for migrating existing Cards to PaymentMethods is private preview. This differs from the April reusable local Sources process.
- Store both `Charge ID` and `PaymentIntent ID` going forward (fetch Charge ID from `latest_charge`)

## Integration Upgrade Map

| Legacy | Recommended | Key benefit |
| --- | --- | --- |
| Card Element | Payment Element | 100+ payment methods; dynamic presentment by location/currency |
| Legacy Checkout | Checkout or Payment Links | Adaptive Pricing, Dynamic payment methods, embed or redirect |
| Payment Request Button | Express Checkout Element | Apple Pay + Amazon Pay + Google Pay + Link + PayPal simultaneously |
| Manual payment methods | Dynamic payment methods | Dashboard-managed; Stripe selects eligible methods per transaction |

The 2026-11-07 [Payment Request Button page](https://docs.stripe.com/stripe-js/elements/payment-request-button) marks the Element deprecated and directs readers to Express Checkout Element and its migration guide. The [2026-09-30 Endive changelog](https://docs.stripe.com/changelog/endive/2026-09-30/deprecate-payment-request-button) says Stripe.js through Dahlia supports the Element and that `elements.create('paymentRequestButton')` throws starting with Endive, including React `PaymentRequestButtonElement` integrations. The change concerns the Element. See [[stripe-express-checkout-element#Migrating from Payment Request Button Element|Express Checkout Element migration]].

## Related Pages

- [[stripe]] — Stripe company page (API Deprecations table)
- [[source-stripe-payment-intents]] — current Payment Intents API
- [[stripe-payment-intents]] and [[stripe-payment-methods]] — payment and instrument contexts
- [[stripe-ach-direct-debit]] — current ACH Direct Debit and migration routes

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

The [migration guide](https://docs.stripe.com/payments/payment-intents/migration) captured 2026-04-20 and 2026-11-07 describes parallel adoption while transitioning an existing cards/Charges integration. It recommends upgrading the API version and client SDK, updating Charge reads where applicable, migrating the payment flow and saved-card handling, and validating authentication in a sandbox. Before API version 2019-02-11, `requires_source` and `requires_source_action` correspond to `requires_payment_method` and `requires_action`. The iOS and Android links route to separate guides. The November quickstart link is for Checkout Sessions with Payment Element and its own confirmation flow. Parallel adoption guidance does not extend to new Charges payment creation.

- **One-time Elements card payment.** The server creates the PaymentIntent and passes its client secret. Stripe.js `confirmCardPayment` initiates the Charge. For automatic confirmation, fulfill server-side after `payment_intent.succeeded`. Legacy Checkout can migrate to Checkout or Elements. The Stripe.js v2 route first moves collection to Elements.
- **Historical Payment Request Button.** The two migration captures pass the token event's ID into `confirmCardPayment` and invoke the completion callback after its promise resolves. Use the server success webhook to establish paid fulfillment. This Element path is version-limited by the through-Dahlia and Endive warning above. The version notice does not remove lower-level Payment Request or `confirmCardPayment`.
- **Save in the payment flow.** Supply the Customer identity and `setup_future_usage` on the PaymentIntent. Use `on_session` for reuse only with the customer present or `off_session` for reuse outside or in both contexts. Both migration captures describe attachment after confirmation and any required actions, then include a separate attach instruction. The November create and confirm references clarify automatic attachment with the qualifying customer and setup, and separate attachment after completion where no Customer was given. The create reference distinguishes `customer` and `customer_account`.
- **Save without charging.** Create a SetupIntent server-side and confirm using its client secret and `confirmCardSetup` instead of `createToken` or `createSource`. Customer action may be required. On successful setup use `setupIntent.payment_method`. A supplied Customer or Account identity attaches the method on success per the November SetupIntent create reference. Where separate attachment is needed, use the Payment Methods API. Bare attachment without either setup flow does not optimize the instrument for future use. Successful setup does not establish a paid transaction.
- **Charge later and list saved methods.** The migration guide asks for the Customer and selected saved Card, Source or PaymentMethod ID, with the legacy parameter qualification above and an off-session flag when applicable. The [November PaymentIntent create reference](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method) documents a migration fallback specifically when `confirm=true` and `payment_method` is omitted: it attaches `customer.default_source`. Provide the chosen instrument explicitly. List via the Payment Methods API, since new PaymentMethods are not duplicated in `customer.sources`.
- **Sandbox fixtures.** The test cases cover authentication on setup or first use (`4000002500003155`), always required (`4000002760003184`), authentication followed by `insufficient_funds` (`4000008260003178`), and optional 3DS2 unless sandbox Radar requests it (`4000000000003055`). These are simulated outcomes.

## Companion evidence locators

- November Sources transition lines 5–17 and 39–49 cover planned card-route changes and server verification. November detailed card migration lines 15–21, 39–64 and 474–484 cover legacy object creation, transitional card IDs and the private-preview migration tool.
- November PaymentIntent create lines 432–444, 647–650 and 672–685 and confirm lines 639–654 cover attachment and the conditional default-source fallback. SetupIntent create lines 378–386, confirm lines 5–11 and PaymentMethod attach lines 5–11 cover the no-charge setup and attach boundaries.
- The November Charges comparison lines 31–68 retain the Charge read table. The 3DS changelog lines 7–21 and November authentication guide lines 73–80 and 499–505 define the separate authentication result.

## Raw Sources

- [[raw/stripe-payments-older-apis-2026-11-07|November 2026 Older APIs overview]] — same-route full capture and grouped comparison.
- [[raw/stripe-payments-payment-intents-migration-2026-11-07|November 2026 Payment Intents migration]] — existing integration migration and the historical Payment Request Button procedure.
- [[raw/stripe-payments-payment-intents-migration-charges-2026-11-07|November 2026 Charges versus Payment Intents comparison]] — scoped write-side deprecation and Charge read mappings.
- [[raw/stripe-payments-charges-api-2026-11-07]] — 2026-11-07 full Charges page (160 lines); scoped card-payment-creation deprecation and new-integration bar.
- [[raw/stripe-older-apis-2025]] — 2026-04-20 overview and grouped comparison. See the dated Sources, Charges and ACH qualifications above.
- [[raw/stripe-charges-api-legacy-2025]] — Charges API: flow comparison, refunds, Apple Pay, statement descriptors, metadata, declines
- [[raw/stripe-payment-intents-migration-2025]] — Charges→PaymentIntents migration: incremental approach, confirmCardPayment, setup_future_usage, confirmCardSetup, off-session flagging, test cards
- [[raw/stripe-sources-api-2025]] — Sources API concepts: 4 characteristics (pull/push, flow, usage, sync/async), 4 flow types, single-use vs reusable, async pending→webhook pattern; deprecated local-payment-method acceptance is scoped to the Sources API route
- [[raw/stripe-sources-to-payment-methods-migration-2025]] — Sources/Tokens→PaymentMethods migration: 3 paths (Checkout/Element/own form), stateless PaymentMethod vs stateful Source, 48h requires_action timeout, webhook mapping, reusable legacy method migration tool, legacy card backward-compat
- [[raw/stripe-charges-vs-payment-intents-2025]] — Charges vs PaymentIntents: 3 API options, Charges = US/Canada simple cards not SCA-ready, PI = all methods + SCA + Terminal; charge object read migration field mapping; brand/Google Pay rename
- [[raw/stripe-upgrade-integration-2025]] — Integration upgrade map: Card Element→Payment Element, Legacy Checkout→Checkout/Payment Links, Payment Request Button→Express Checkout Element, Manual→Dynamic payment methods
