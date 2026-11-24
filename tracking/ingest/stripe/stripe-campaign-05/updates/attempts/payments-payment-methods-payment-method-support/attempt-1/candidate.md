---
title: "Stripe Docs — Payment method support"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/payment-methods/payment-method-support"
raw_files:
  - "stripe-payments-payment-methods-payment-method-support-2026-11-07.md"
  - "stripe-payment-method-support-2025.md"
tags: [stripe, payment-methods, integration-matrix, product-support, api-support, bnpl, wallets, bank-debits]
---

## Summary

Stripe's May 8 and November 7, 2026 support matrices compare presentment currencies, business locations and customer countries, product and Checkout mode, and API capabilities. A method can have additional requirements in its own documentation or payment terms. A connected account's eligibility can differ from its platform's. Stripe describes Link as a reusable payment network and routes missing-method questions to the Dashboard troubleshooting tool.

## Country and currency

The May geography table has 41 data rows and the November table has 44. The counts describe these tables. A list of currencies and countries does not imply that every listed combination works.

- **Pay by Bank** changes from GBP and GB in May to EUR and GBP with FI, IE and GB business and customer columns in November. The separate November method profile names FI, IE and GB customer bank accounts as generally available and Belgium, France and Germany as private preview.
- **November additions** include PayTo (AUD and Australia), Revolut Pay (EUR, GBP, RON, HUF, PLN and DKK for listed European and UK locations), and UPI (INR for India customers and the listed business locations).
- Both dated geography tables list stablecoin payments as USD for US businesses and worldwide customers, Pix as BRL with BR invite-only and US businesses for BR customers, and Zip with invite-only USD/US wording alongside AUD/AU. Alma, Konbini, PayNow, PromptPay and FPX have their own currency and location rows.

## Product and Checkout mode

Checkout modes are payment, subscription and setup. Read the method row together with its footnotes.

| Group | November matrix changes and important scope |
| --- | --- |
| Bank debits | The combined Instant Bank Payments/ACH row changes Mobile Payment Element to Unsupported. The separate November Link guide still lists an iOS-linked Mobile Payment Element route for eligible US transactions, with risk constraints and no display when ACH Direct Debit is enabled for the transaction. Bacs uses Checkout setup mode for the documented SetupIntent route. ACSS excludes Checkout subscription mode, deferred Intent creation and Elements with Checkout Sessions. |
| Bank redirects and transfers | BLIK adds unqualified Checkout, Subscriptions, Invoicing and Customer Portal, while its two Elements limitations remain. The matrix still marks BLIK Mobile Payment Element Supported, while the November BLIK profile marks in-app payments Unsupported. For Bancontact, EPS, FPX and P24 the matrix's `send_invoice` footnote marker is on Subscriptions. Bancontact, EPS and P24 Invoicing separately says Invite only. FPX Invoicing is Supported and Customer Portal Unsupported in both matrices. The November FPX profile also lists Invoicing, a `send_invoice` limitation and B2C-only mobile Payment Sheet. iDEAL/Wero uses the `ideal` enum and its own subscription mode, collection and per-payment authentication qualifications. Bank transfer Checkout remains payment mode and November expressly marks both Subscriptions and Invoicing `send_invoice`. |
| BNPL | Affirm moves to Subscriptions Unsupported and Customer Portal Supported, while retaining Terminal. Klarna Checkout gains a buyer-country/payment-option qualification in place of the May mode exclusions, Subscriptions loses its `send_invoice` marker, and Terminal becomes private preview. Klarna retains the `send_invoice` Invoicing qualification and the Express Checkout Element saving exclusion. Scalapay and SeQura list Mobile Payment Element, and SeQura adds `send_invoice` Invoicing. Afterpay/Clearpay Invoicing remains private preview. Consult the individual Billie, Kriya, Mondu, Scalapay, SeQura and Sunbit source records for method scope. |
| Real-time payments | Pay by Bank Mobile Payment Element becomes Supported and UPI gets a product row. The separate Pay by Bank method profile describes preview recurring through Elements and Payment Intents as an initial Pay by Bank payment with a Bacs mandate. Its direct matrix SetupIntent and future-use cells remain Unsupported. |
| Wallets | Alipay Invoicing changes from Invite only to Supported. Its separate November profile distinguishes one-time Hosted Invoice Page from invitation-only recurring Invoicing or setup and explicitly excludes Mobile Payment Element PaymentSheet despite the support matrix listing it as Supported. Custom native integrations are separate. MB WAY adds Mobile Payment Element and `send_invoice` Subscriptions/Invoicing. Samsung Pay adds Checkout payment mode and retains Terminal. The separate South Korea capture links Checkout and Direct API variants. TWINT moves from bank redirects to wallets and adds all Checkout modes, Subscriptions, Invoicing and Customer Portal. WeChat Pay lists private-preview `send_invoice` Subscriptions and Terminal outside Japan. |
| Wallet regional footnotes | The May Apple Pay and Google Pay entries refer to Indian IP addresses. November Google Pay refers to India-based Stripe accounts, and the Apple Pay row drops that marker while retaining the embedded-page Safari 17+ and iOS 17+ condition. |
| Custom methods | The separate custom-method matrix adds Checkout and private-preview Express Checkout Element, while Payment Links remains Unsupported. The method guide describes external processing with separate Stripe records for reporting. |

## API support and differences

The API matrices list method identifier where applicable, PaymentIntents, SetupIntents, manual capture, `setup_future_usage` and whether redirect is required. The footnote says confirmation might need a `return_url`. It also distinguishes cards and named bank debits supporting both `on_session` and `off_session` from other methods that either lack the feature or support `off_session` only. API cells and redirects describe compatibility, not payment completion.

- **Bank methods.** Bacs PaymentIntent confirmation uses a mandate collected through a Stripe-owned flow, and the SetupIntent footnote points to Checkout setup mode despite the generic SetupIntents cell. November marks Bancontact SetupIntents Unsupported and describes saving customer bank details as a SEPA Direct Debit PaymentMethod. BLIK adds SetupIntents and off-session future usage with a continuing deferred-creation exclusion. Its November profile requires active `blik_payments` followed by active `blik_recurring_payments` on the platform and each accepting account for recurring use.
- **BNPL and real-time.** November marks SeQura `setup_future_usage` Unsupported where May listed support. The cross-method Sunbit row says manual capture Unsupported while the November Sunbit profile lists manual capture with limits. UPI adds `upi`, PaymentIntents, SetupIntents, future usage and redirect, with manual capture Unsupported.
- **Wallets.** November adds `samsung_pay` with PaymentIntents and redirect. Alipay and WeChat Pay change to redirect required. WeChat Pay adds private-preview SetupIntents and future usage. Its own November profile marks general recurring, future usage, SetupIntents and off-session Unsupported and separately describes a private-preview off-session recurring path. The TWINT API row moves categories with the same enum, supported PaymentIntents, SetupIntents and future usage, unsupported manual capture and redirect Yes.
- **Stablecoins.** In both captures the dedicated `crypto` row lists manual capture Supported and SetupIntents/future usage Private preview. The wallets row for the same enum and URL says manual capture Unsupported and SetupIntents/future usage Invite only. Product labels differ too, including private-preview versus invite-only Subscriptions and Customer Portal labeling. Keep the two tables distinct.
- **Connect.** Bank transfers through `customer_balance` have limited `on_behalf_of` support. PayPal does not support it. The matrix describes private-preview `on_behalf_of` for Alipay and WeChat Pay. Use the separate Connect matrix for account capabilities and charge-type rules.

## Detail locators

| Topic | May raw lines | November raw lines |
| --- | --- | --- |
| Country, currency and connected account scope | 22–72 | 23–76 |
| Product tables and Checkout modes | 74–204 | 78–209 |
| API tables, redirects and Connect scope | 206–336 | 211–343 |
| Custom method matrix | 338–344 | 345–353 |

## Related

- [[stripe-payment-methods]] — Payment Methods concept and integration selection
- [[stripe-wallets]] — Wallet-specific routes and conditions
- [[stripe-bnpl]] — BNPL product and API support
- [[source-stripe-payment-methods-overview]] — Payment method catalog
- [[source-stripe-payment-method-connect-support]] — Separate Connect support matrix
- [[source-stripe-bank-debits]] — Bank debits guide
- [[source-stripe-custom-payment-methods]] — External payment methods
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-payment-methods-payment-method-support-2026-11-07|November 7, 2026 full matrix]]
- [[raw/stripe-payment-method-support-2025|May 8, 2026 full matrix]]
