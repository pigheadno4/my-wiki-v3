---
title: "Stripe: Supported Payment Methods"
type: concept
category: technology
tags: [stripe, payment-methods, cards, bank-debits, bank-redirects, bnpl, wallets, vouchers]
---

## Definition

The May 1, 2026 overview groups eight payment method families. The November 7, 2026 overview lists ten, with separate stablecoin and closed-loop gift card families. The regional tables describe common use, and each method has its own eligibility and integration requirements. Adding another method in the same family usually needs minimal changes. See [[source-stripe-payment-methods-overview]].

## May 2026 family examples

The regional examples below preserve the May 1, 2026 classification. See [[source-stripe-payment-methods-overview]] for November's family placement, dated preview labels and common-use tables.

### Cards

Global: Visa, Mastercard, American Express, Diners. US/CA: Discover, Interac (in-person only). Europe: Cartes Bancaires. APAC: eftpos (AU), JCB, China Union Pay, South Korean cards.

### Bank Debits

Direct bank account debits — lower fees than cards.

- US/CA: ACH Direct Debit, Instant Bank Payments (Link), Canadian PADs
- EU: Bacs Direct Debit (UK), SEPA Direct Debit
- APAC: AU BECS Direct Debit, NZ BECS Direct Debit

### Bank Redirects

Secure online bank payment flows — popular in EU and Asia.

- EU: Bancontact, BLIK, EPS, iDEAL/Wero, P24, TWINT
- APAC: FPX (MY), PayNow (SG), UPI (IN)

### Bank Transfers

Bank transfers are common for large business payments and for consumers in certain countries. The May overview describes sending funds directly to the merchant's bank account. The November overview says the merchant gives the payer a virtual account number, the payer pushes funds, and Stripe reconciles using the virtual number without exposing the merchant's account details. See [[source-stripe-payment-methods-overview]].

- USD Bank Transfer, SEPA Bank Transfer, UK Bank Transfer, Japan Furikomi, Mexico Bank Transfer

### Buy Now Pay Later (BNPL)

Merchant paid upfront; customer pays in installments.

| Method | Regions |
| --- | --- |
| Affirm | US/CA |
| Afterpay / Clearpay | US/CA, EU, APAC |
| Klarna | US/CA, EU, APAC |
| Meses sin intereses | Mexico |
| Zip | US, APAC (AU) |

### Real-Time Payments

Instant account-to-account transfers via intermediary.

- EU: Swish (invite only, SE)
- APAC: PayTo (AU), PayNow (SG), PromptPay (TH)
- LATAM: Pix (BR)

### Vouchers

Digital voucher → customer pays in-person at local stores.

- EU: Multibanco (PT)
- Asia: Konbini (JP)
- LATAM: OXXO (MX), Boleto (BR)

### Wallets

Fast checkout with saved cards or stored balances.

- **Global**: Apple Pay (not India), Google Pay (not India), Link, Secure Remote Commerce, Stablecoins/crypto
- **US**: Cash App Pay
- **EU**: PayPal, MobilePay, Revolut Pay, Satispay
- **APAC**: Alipay, WeChat Pay, GrabPay, Kakao Pay, Naver Pay, Samsung Pay, PayCo

## Integration Options

5 paths from no-code to advanced (see [[source-stripe-payment-method-integration-options]]):

- **Payment Links / Hosted Checkout / Embedded**: Checkout Sessions API; limited UI customization
- **Elements + Checkout Sessions**: more coding; Appearance API
- **Advanced (PaymentIntents)**: most coding, with Appearance API. The May 2026 comparison listed custom payment methods only on the advanced web path. The November comparison says support varies by integration. The separate product guide lists Checkout support, Express Checkout Element private preview and Payment Links unsupported. See [[source-stripe-custom-payment-methods]].

**Dynamic payment methods.** In the November 2026 overview, merchants using dynamic Checkout, Payment Element, Payment Links or hosted invoices can enable most methods in the Dashboard without code changes. Stripe displays eligible methods, and individual methods can have additional prerequisites. An integration that explicitly lists `payment_method_types` must change its code to add a method.

The May 2026 comparison described “40+” dynamically displayed methods and used writable `payment_method_types` in its manual examples. The November guide uses the `allowed_payment_method_types` request allowlist for Checkout Session and PaymentIntent creation and returns eligible types in the computed `payment_method_types` response. See [[source-stripe-payment-method-integration-options]] for earlier GA Checkout, Dahlia Intent and Endive endpoint conditions.

Some wallets, such as Apple Pay, require domain registration for Elements or embedded Checkout. See [[source-stripe-pmd-registration]].

See [[stripe-dynamic-payment-methods]] for the AI-driven dynamic selection system.

## Sources

- [[source-stripe-payment-methods-overview]] — May and November payment method families, regional use and dated Dashboard activation, with exact eligibility routed to method guides
- [[source-stripe-payment-methods]] — April and November Payment Methods API guides on PaymentMethod roles, customer actions, immediate versus delayed outcomes, and verified webhook handling
- [[source-stripe-payment-method-integration-options]] — Dated web comparison, Dashboard and code boundaries, versioned allowlists, compatibility, order and wallet registration
- [[source-stripe-automatic-payment-methods]] — Aug 2023 API change: omit payment_method_types → Dashboard methods; allow_redirects: never option; Elements migration
- [[source-stripe-legacy-apis]] — April and November 2026 legacy Sources, Cards and Tokens migration scopes. The paired transition guides cover April local methods and November's planned Sources card and legacy Cards cutoff. The detailed November legacy card migration is separate.
- [[source-stripe-cards]] — May and November 2026 cards guide: account-country and customer-country brand matrix, conditional SCA/3DS, EU co-badged choice, and November's qualified UnionPay Apple Pay on the web, eftpos Apple Pay in AUD without manual capture, and Payment Element brand/funding filter
- [[source-stripe-how-cards-work]] — How cards work: 4-step flow, manual update limits, change default payment method, automatic card updates + fingerprint change
- [[source-stripe-card-product-codes]] — Card product codes: brand_product field, Visa (41 codes) + Mastercard (200+ codes) reference tables, test cards
- [[source-stripe-bank-debits]] — Bank debits: 6 methods (ACH/Bacs/AU-BECS/NZ-BECS/ACSS/SEPA), API enums, product/API support matrices, caveats
- [[source-stripe-ach-direct-debit]] — ACH Direct Debit: T+4/T+2 settlement, mandates, disputes (final), blocked accounts, 180-day refunds, Connect cloning
- [[source-stripe-secure-remote-commerce]] — SRC/Click to Pay: US only, replaces Visa Checkout + Masterpass, card.masterpass PM type, Masterpass deprecated
- [[source-stripe-payment-method-support]] — May and November 2026 matrices for geography and currency, product and Checkout modes, and Intent, capture, saving and redirect support. Compare method-specific qualifications and documented disagreements.
- [[source-stripe-payment-method-connect-support]] — May and November 2026 Connect reference for method-specific activation, charge types, descriptors and mandates. See dated BLIK, SEPA, ACH and PayPal qualifications.
