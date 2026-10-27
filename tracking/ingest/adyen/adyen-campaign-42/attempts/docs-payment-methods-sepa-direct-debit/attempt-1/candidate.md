---
title: "Adyen SEPA Direct Debit overview and mandate guidance"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/sepa-direct-debit"
raw_files:
  - "adyen/docs/payment-methods/sepa-direct-debit/2026-09-15.md"
tags: [adyen, sepa-direct-debit, mandate, iban, chargebacks, refunds]
---

## Overview

This 2026-09-15 captured Adyen overview covers SEPA Direct Debit Core for EUR bank debits, including one-off and recurring use, mandate collection, pre-debit notification, chargebacks, refunds and platform routes. It says Adyen supports Core, not the separate B2B scheme, although Core accepts business and personal bank accounts. This is a provider snapshot, not proof of current bank/merchant eligibility, mandate validity or successful debit/settlement. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The page supports one-off and recurring payments but advises against one-off use or physical goods because of chargeback risk; that is a recommendation, not a prohibition. It states a 500 EUR per-transaction limit and directs higher-limit requests to Support, while the FAQ says applicable limits ultimately depend on the customer's bank and business model. Its capability table labels Direct Debit/direct, International/EUR and marks recurring, refunds, partial/multiple partial refunds, capture variants and chargebacks supported. These marks and amounts do not establish present account-specific coverage or an approved higher limit.
- Before debiting, the merchant must collect customer name and IBAN and obtain an accepted mandate. The mandate procedure adds billing address for a stated list of country codes, creditor details, standardized authorization text, customer-entered data, an explicit active signing action, and a confirmation containing the exact mandate details, UMR and signing date. Adyen says it can generate and present the mandate on the merchant's behalf. The section's template introduction calls signing "implicit" even though the procedure requires explicit authorization and an active action; retain the stronger procedural requirement rather than interpreting the template as passive consent. The sample checkbox and button wording are examples, not fixed UI strings.
- A shopper can ask the bank to cancel a mandate at any time; future debits under it become invalid and further collection needs a new mandate. The page says Adyen learns of a canceled mandate only when a payment is charged back. Stored SEPA details can also be deleted through API or Customer Area; deletion is not described as replacing bank-side cancellation. Adyen uses its creditor ID by default, while use of a merchant's own creditor ID and creditor-name changes require Support configuration.
- The page attributes a pre-debit notification to the SEPA Direct Debit rulebook: notify the customer for each debit at least one day before initiating it. The listed notification contents are recommendations to improve recognition, not separately stated mandatory fields. A bank chargeback may be sought within eight weeks without a reason or within thirteen months for unauthorized/incorrect payments with evidence; Adyen says SEPA chargebacks cannot be defended. Other return reasons include insufficient funds, inactive/blocked accounts and technical errors. Authorization and notification do not prove settled funds.
- Refunds are described as available only after the original payment settles. The page warns that a shopper may dispute even after a merchant refund, causing two credits. It recommends refunding only for a trusted/verified shopper, after confirmation with them, and at least seven days after the original payment; separately it says Adyen applies a one-week refund hold **post-settlement**. Those are distinct clocks, and the post-settlement hold should not be replaced by the seven-day recommendation. The text says "full or partial payments" in the refund paragraph, apparently a wording error; do not infer a separate payment operation from it.
- The zero-value FAQ says such an authorization may store an IBAN without sending anything to the issuer to validate it. It recommends an authenticated IBAN-based payment method where possible, a fallback IBAN/name enrollment route, or a minimum 0.1 EUR charge later refundable once funds have been paid out; these are recommendations rather than universal verification guarantees. The page links Web, iOS, Android, React Native, Flutter, API-only and Pay by Link routes; child guides own channel-specific APIs and outcomes.

## Detail locators

- Core-versus-B2B scope, one-off/recurring advice, 500 EUR statement and capability marks: pinned raw lines 23–35; bank-dependent limit FAQ: lines 153–155 and Core B2B account distinction: lines 167–169.
- Mandate data, conditional billing address, contents, active signing and confirmation/UMR: pinned raw lines 37–67; bank cancellation and stored-detail deletion: lines 69–73.
- Creditor ID/name setup and pre-debit notification rule versus recommended contents: pinned raw lines 75–98.
- Chargeback deadlines, nondefensibility and return reasons: pinned raw lines 100–119.
- Refund settlement prerequisite, double-credit risk, recommended seven days and separate post-settlement hold: pinned raw lines 121–145.
- SEPA geography, zero-value IBAN-validation boundary and advised alternatives: pinned raw lines 147–169; integration routes: lines 171–220.

## Related

- [[adyen-online-payments]] — main provider online-payment concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/2026-09-15|SEPA Direct Debit overview, 2026-09-15]]
