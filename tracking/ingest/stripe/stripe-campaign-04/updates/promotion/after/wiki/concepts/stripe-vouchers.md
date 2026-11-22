---
title: "Cash Vouchers (Stripe)"
type: concept
category: technology
tags: [stripe, vouchers, boleto, konbini, multibanco, oxxo, cash, in-person, brazil, japan, portugal, mexico]
---

## Definition

Voucher payment methods let customers complete online purchases using a digital voucher. Payment channels vary by method. Customers can pay cash vouchers in person, and Multibanco vouchers can be paid through online banking or at an ATM. Stripe supports four voucher methods.

## Supported Methods

| Method | API enum | Country | Currency | Subscriptions | Invoicing | SetupIntents |
| --- | --- | --- | --- | --- | --- | --- |
| Boleto | `boleto` | Brazil | BRL | Yes | Yes | Yes |
| Konbini | `konbini` | Japan | JPY | send_invoice only | send_invoice only | No |
| Multibanco | `multibanco` | Portugal | EUR | send_invoice only | send_invoice only | No |
| OXXO | `oxxo` | Mexico | MXN | No | No | No |

**No manual capture.** Voucher presentation depends on the method and integration. In the dated Boleto guide, Checkout redirects to `hosted_voucher_url`; live Elements/Checkout Sessions API and Elements/Payment Intents API Pay flows redirect to the Boleto website; Direct API `stripe.confirmBoletoPayment()` opens a voucher modal by default. See [[source-stripe-boleto-accept-payment]].

## Payment Flow

1. Customer selects voucher payment at checkout
2. Customer receives digital voucher with reference code (email or app)
3. Customer pays through a channel supported by the method, such as in-person cash payment for a cash voucher or online banking or an ATM for Multibanco.
4. Merchant receives payment notification after the customer pays; timing differs by method. For Konbini, voucher issuance is provisional, while Stripe confirms asynchronously and marks the PaymentIntent succeeded after store cash payment (November 7, 2026 guide).

## Use Cases and Limitations

**Best for**: customers without cards or bank accounts; markets with low card authorization rates (e.g., Mexico).

**Not suitable for**: delivery before payment confirmation, since voucher issuance is not payment. Confirmation timing varies by method; Konbini confirms asynchronously after store cash payment, not after a universal one-business-day delay. Refund support also varies: Konbini supports full and partial bank-transfer refunds with customer action.

## Connect Notes

- Boleto, Multibanco, OXXO: standard Connect support
- Konbini Connect: the May 7, 2026 guide described an invite for charges made `on_behalf_of` other accounts. The November 7, 2026 guide separately describes a Japanese platform settling destination charges or separate charges and transfers on its own account with its own activation and no `on_behalf_of`; the connected account need not activate Konbini. The own-account route does not establish the current status of the earlier on-behalf-of invite.

## Boleto Details

**Regulated by Central Bank of Brazil**. BR merchants only. BRL only.

**Timing (dated):** The 2026-11-07 overview says confirmation takes **up to one business day**, typically the next business day after payment, and labels settlement **up to two business days (T+2)** without defining its start event. The 2026-05-07 overview says funds become available for payout two business days **after confirmation**. Voucher issue and provisional method access are not paid status; settlement, payout availability and payout arrival are separate.

**Amount limits**: 5.00 – 49,999.99 BRL.

**Refunds and disputes:** Stripe Boleto full/partial refund capability is unsupported; the 2026-05-07 page advises a separate customer-credit process. Customers cannot file standard Boleto chargebacks. Bank-side mishandling can still occur, and Stripe **contacts the merchant with next steps**; the captures do not promise Stripe handles resolution alone.

**Recurring and setup:** Billing/subscriptions, Invoicing, Customer Portal, SetupIntents and PaymentIntents with `setup_future_usage` are listed as supported, but the 2026-11-07 overview excludes **off-session Boleto payments**. The 2026-05-07 subscription guide's `charge_automatically` plus `off_session: true` is a Subscription creation example, not proof of off-session voucher collection; its invoice guide says the customer still must pay each voucher. The overview does not resolve whether that older request remains accepted.

**Integration (2026-05-07 guide)**: 4 paths (Checkout, Elements/Checkout Sessions API, Elements/Payment Intents API, Direct API). Checkout redirects to `hosted_voucher_url` rather than `success_url`; `checkout.session.completed` means voucher creation, `checkout.session.async_payment_succeeded` means payment, and `checkout.session.async_payment_failed` includes expiry or another failure. Both live Elements variants say Pay redirects to the Boleto website; the Payment Intents API client call uses `stripe.confirmPayment` with a `return_url`. Direct API recommends client `stripe.confirmBoletoPayment()` with a voucher modal, permits optional server confirmation, and requires name, email, CPF/CNPJ and Brazilian address. `expires_after_days` is 0–60 days (default 3), expiring at 23:59 America/Sao_Paulo. For a voucher already paid, Direct API says `payment_intent.succeeded` arrives next business day, Monday-Friday excluding Brazilian holidays; funds are not immediately available. The 2026-11-07 capture is variant navigation only. [[source-stripe-boleto-accept-payment]]

**Subscriptions and invoices**: both `send_invoice` and `charge_automatically` are documented. For automatic collection, the Boleto PaymentMethod must be attached and set as the default on a Customers v1 Customer or a customer-configured Accounts v2 Account; the customer name, Brazilian address and tax ID must be available. Accounts v2 uses `customer_account` and `configuration.customer.billing.default_payment_method`, while Customers v1 uses `customer` and `invoice_settings.default_payment_method` (2026-11-07 guide; Accounts v2 preview/version access remains conditional). In `send_invoice`, customers re-enter details and the invoice has a due date; voucher expiration is separate and defaults to three days. Even with `charge_automatically`, Boleto is not an auto-debit: the customer must pay the voucher for success. See [[source-stripe-boleto-invoices]] and [[source-stripe-boleto-subscription]]. The recurring guide requires fresh full name, address and tax ID for each send-invoice period. Its generic Dashboard option to refund a last subscription payment does not establish Boleto refund support; [[source-stripe-boleto]] documents no Boleto refunds.

## Konbini Details

**Japan-only** cash voucher, JPY only, JP merchants only. Pay at FamilyMart, Lawson, Ministop, Seicomart.

**Payment state**: instructions give instant provisional access; payment confirmation is delayed until cash is paid at the store. Stripe then confirms asynchronously and marks the PaymentIntent `succeeded`. The November guide says funds are available for payout after four business days, with settlement on the standard payout schedule; it does not promise an actual payout on day four.

**Amount limits**: 120 JPY – 300,000 JPY.

**Refunds**: full and partial bank-transfer refunds are supported, but cash cannot return to the original source. Stripe emails the customer for bank details; processing waits for the customer's response. Track `Refund.status` and final `refund.updated` or `refund.failed` events; on failure the amount returns to Stripe balance and another refund method is required.

**Billing**: `send_invoice` only (no `charge_automatically`).

**Connect**: the May guide's invite was scoped to `on_behalf_of` charges for other accounts. The November guide adds a Japanese platform own-account destination-charge or separate-charge-and-transfer route using its own Konbini activation without `on_behalf_of`; the connected account need not activate Konbini. Customer Portal remains unsupported in the November product matrix.

**Integration and product scope (May and November 2026)**. The May [[source-stripe-konbini-accept-payment|acceptance guide]] details Checkout and Direct API. The November capture routes to those two variants. The separate November [[source-stripe-konbini|method overview]] lists Payment Element support and excludes Express Checkout Element.

Checkout sends customers to `hosted_voucher_url`. `checkout.session.completed` means the voucher was generated. `checkout.session.async_payment_succeeded` means it was paid, and `checkout.session.async_payment_failed` reports expiry or another failure. The May Checkout guide documents `expires_after_days` (1–60 days, default 3, 23:59:59 JST cutoff). Direct API also documents a mutually exclusive bounded `expires_at`, `stripe.confirmKonbiniPayment()` and store-specific `next_action.konbini_display_details`. A valid slip issued before the kiosk deadline may still be paid at the register afterward. The 45-day bank-refund deadline applies if the refund still has `requires_action` status 45 days after creation.

**Prohibited categories (dated scope)**: the May 7, 2026 guide listed sole proprietors in business under three years and dating sites, plus RMT, gambling, information selling, MLM, gore, unscientific offerings, prohibited medical products, public-order offenses, import forwarding, transfers, loans, vaping and fortune-telling. The November 7, 2026 guide does not repeat the broad under-three-year or dating-site prose; it instead requires a sole proprietor's website to show a physical-premises exterior photo and lists Dating and Escort Services MCC 7273 as prohibited, alongside a table of other prohibited MCCs. Do not infer that omitted categories became eligible. Financial partner and store chains may still reject an application.

## Multibanco Details

**Portugal customers only, EUR only**. 33 merchant countries (Europe + US, includes Gibraltar).

**Two flows**: online banking (entity + reference → log in → pay) and ATM (entity + reference → pay at ATM).

**Confirmation delay**: several days, especially over weekends. The November Multibanco overview shows a seven-day voucher and up to four days of `processing` after expiry. Fulfill after asynchronous `succeeded`. The May `hosted_voucher_url` displays instructions. The November overview describes no return redirect after payment. The deprecated Sources API's return URL could occur without funds sent. Konbini also waits for customer action: its voucher instructions give provisional access, and Stripe confirms asynchronously after the customer pays cash at a store; the November guide says notification follows that store payment, not voucher issuance.

**Amount limits**: €0.50 – €99,999.

**Refunds**: May 2026 documents 365 days from the original payment. November documents 456 days and noncancelable submission. Bank credit typically takes one day, varying by bank. Share `destination_details.multibanco.reference` only after the Refund succeeds and when the reference is available. A failed refund returns the amount to the Stripe balance and requires another refund method. See [[source-stripe-multibanco]].

**Dispute scope**: The Multibanco overviews describe no dispute process that can result in a chargeback withdrawing funds from the merchant's Stripe account.

**Billing**: Invoices and subscriptions use `send_invoice` only. The November overview marks recurring and off-session payments unsupported.

**Connect**: May lists direct, destination, and separate charges and transfers. November documents provisional access with possible follow-up review. Express or external-Dashboard connected accounts must have an active `multibanco_payments` capability before accepting the method. See [[source-stripe-multibanco]].

**Integration (2026-05-07 acceptance guide)**: Checkout, web Direct API, iOS and Android. Checkout uses one-time EUR line items in payment mode. The `send_invoice` billing path is separate. Checkout and the optional Direct API server path redirect to `hosted_voucher_url`. The web Direct API requires billing email and uses a Stripe.js modal by default with `stripe.confirmMultibancoPayment()`, while iOS and Android use webviews. Voucher issuance precedes payment and fulfillment. `next_action.multibanco_display_details` contains `entity`, `reference`, `expires_at` and `hosted_voucher_url`. After seven-day voucher expiry, a pending PaymentIntent can process for up to four days for delayed transfer notification. It returns to `requires_payment_method` if payment fails to complete within the window. Stripe initiates a refund if funds arrive after the window or against a canceled voucher.

## OXXO Details

**Customer scope** — OXXO is a single-use cash voucher in MXN for customers in Mexico, payable at OXXO stores. The May 2026 overview listed MX Stripe accounts. The November overview lists eligible CA, MX, SG and US accounts, plus private preview. The headline names EEA and UK, and the named preview list includes Switzerland (CH).

**Confirmation and settlement** — November 2026 separates confirmation by the next business day after store payment from settlement up to T+4. It lists Tuesday–Thursday payments settling the following Monday and Friday–Monday payments settling the following Wednesday. Voucher issuance and the cashier receipt are distinct from Stripe `payment_intent.succeeded`. The May overview paired confirmation with settled funds and separately mentioned standard payout timing. Merchant payout and bank arrival are separate.

**Amount and features** — 10–10,000 MXN per voucher payment. OXXO has no native refunds or standard dispute process, and the November overview lists subscriptions and invoicing as unsupported. A merchant can choose to offer separate credits.

**Access and Connect** — the November overview lists merchant accounts and Connect platforms or marketplaces, with provisional access and possible review after activation. Check the dated eligibility route for account and category scope.

**Integration.** The November product overview lists Checkout Sessions, Payment Intents, Payment Element and in-app payments. The May acceptance guide covers Checkout, Elements with Checkout Sessions or Payment Intents, Direct API, iOS, Android and React Native. See its dated Mexico-business conditions for Checkout and Direct API. Checkout redirects to `payment_intent.next_action.oxxo_display_details.hosted_voucher_url`. Mobile can show the voucher in an in-app webview. The voucher hub’s separate method-level redirect property has its own scope. The May Legacy Direct API opens a voucher modal with `stripe.confirmOxxoPayment()`. Collected data requires full billing name and email, with each name at least two characters. The helper can use an existing PaymentMethod ID or omit additional data when a PaymentMethod is already attached. The May guide recommends the newer path and says Legacy support could end if deprecated.

**Expiry.** May documents a three-day default for Checkout Session and PaymentIntent paths and illustrates 23:59 America/Mexico_City. The November product overview gives a five-day PaymentIntent default. Both describe a 1–7 day `expires_after_days` option. The response field is `next_action.oxxo_display_details.expires_after`. The November acceptance capture links variants, while their detailed defaults and conditions remain outside that selector. See [[source-stripe-oxxo-accept-payment]].

**Categories** — the May 2026 overview named four unsupported categories. November lists prohibited MCCs and separate restricted MCCs that may qualify after providing additional information. See the dated eligibility table in [[source-stripe-oxxo]].

## Sources

- [[source-stripe-vouchers]] — hub page: 4 methods, product/API support matrices
- [[source-stripe-boleto]] — Boleto overview: Brazil BRL voucher, provisional access, asynchronous up-to-one-business-day confirmation, November T+2 settlement versus dated May payout-availability wording, no Stripe refunds or off-session payments
- [[source-stripe-boleto-accept-payment]] — 2026-05-07 Boleto integration guide: four distinct UI/API paths, voucher creation versus paid state, expiry, Direct API billing/tax ID and cancellation limits; 2026-11-07 capture is variant navigation only
- [[source-stripe-boleto-subscription]] — Boleto subscriptions: both send_invoice + charge_automatically, tax ID required for auto-charge, setup flow
- [[source-stripe-boleto-invoices]] — Boleto invoice guide (2026-05-07 and 2026-11-07): send_invoice versus charge_automatically, Customers v1 and preview-qualified customer-configured Accounts v2 examples, invoice finalization versus voucher payment
- [[source-stripe-konbini]] — Konbini: Japan JPY cash voucher, delayed payment until store cash, asynchronous PaymentIntent success, funds available for payout after four business days; dated eligibility and Connect route differences between May and November 2026
- [[source-stripe-konbini-accept-payment]] — May 2026 Checkout and Direct API guide for voucher issuance, paid state, expiry and refunds. November 2026 acceptance selector links both variants.
- [[source-stripe-multibanco]] — May and November 2026 EUR voucher overviews with delayed payment, dated 365- and 456-day refund windows, noncancelable submission, provisional review and `send_invoice` scope.
- [[source-stripe-multibanco-accept-payment]] — May 2026 integration guide for Checkout, Direct API, iOS and Android. November 2026 capture is a variant directory.
- [[source-stripe-oxxo]] — May and November 2026 OXXO overviews with merchant eligibility, voucher references, status and dated expiry and settlement boundaries.
- [[source-stripe-oxxo-accept-payment]] — May 2026 OXXO integration guide for Checkout, Elements, Direct API and iOS, Android and React Native. November 2026 capture is a variant directory.
