---
title: "Stripe: Supported Payment Methods"
type: concept
category: technology
tags: [stripe, payment-methods, cards, bank-debits, bank-redirects, bnpl, wallets, vouchers]
---

## Definition

Stripe supports 8 categories of payment methods, each with its own regional availability, integration pattern, and customer experience. Within a category, adding a second payment method requires minimal integration changes.

## Categories

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

Direct bank-to-bank — common for large B2B payments.

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
- **Advanced (PaymentIntents)**: most coding; custom payment methods supported; Appearance API

**Dynamic payment methods** (recommended): manage via Dashboard, 40+ methods, Stripe handles eligibility. **Manual**: specify `payment_method_types` explicitly.

Wallet methods require domain registration for Elements/Advanced integrations.

See [[stripe-dynamic-payment-methods]] for the AI-driven dynamic selection system.

## Sources

- [[source-stripe-payment-methods-overview]] — primary source: all 8 categories, regional availability tables
- [[source-stripe-payment-method-integration-options]] — integration paths comparison, dynamic vs manual, domain registration for wallets
- [[source-stripe-automatic-payment-methods]] — Aug 2023 API change: omit payment_method_types → Dashboard methods; allow_redirects: never option; Elements migration
- [[source-stripe-cards]] — Cards detail: brand capabilities table, Amex/CUP/JCB/CB/eftpos restrictions, SCA/3DS, EU co-badged card choice, India RBI
- [[source-stripe-how-cards-work]] — How cards work: 4-step flow, manual update limits, change default payment method, automatic card updates + fingerprint change
- [[source-stripe-card-product-codes]] — Card product codes: brand_product field, Visa (41 codes) + Mastercard (200+ codes) reference tables, test cards
- [[source-stripe-bank-debits]] — Bank debits: 6 methods (ACH/Bacs/AU-BECS/NZ-BECS/ACSS/SEPA), API enums, product/API support matrices, caveats
- [[source-stripe-ach-direct-debit]] — ACH Direct Debit: T+4/T+2 settlement, mandates, disputes (final), blocked accounts, 180-day refunds, Connect cloning
- [[source-stripe-secure-remote-commerce]] — SRC/Click to Pay: US only, replaces Visa Checkout + Masterpass, card.masterpass PM type, Masterpass deprecated
- [[source-stripe-payment-method-support]] — comprehensive reference: country/currency table (36 PMs), product support matrices by category, API support (setup_future_usage, return_url) per PM; also covers new BNPL: Billie, Kriya, Mondu, Scalapay, SeQura, Sunbit
- [[source-stripe-payment-method-connect-support]] — Connect-specific reference for 31 PMs: capability names, MoR/descriptor tables, notable restrictions (Alma/PayPal marketplace-only, ACH cloning, Cash App no cross-account clone, iDEAL business name compliance, bank transfers no on_behalf_of)
