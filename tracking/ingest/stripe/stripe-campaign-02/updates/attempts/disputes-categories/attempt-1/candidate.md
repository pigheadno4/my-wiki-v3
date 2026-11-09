---
title: "Stripe — Dispute Reason Code Categories"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/disputes/categories"
raw_files:
  - "stripe-disputes-categories-2026-11-07.md"
  - "stripe-disputes-categories-2026.md"
tags: [stripe, disputes, chargebacks, dispute-categories, reason-codes, evidence, visa, mastercard, amex, discover, klarna, paypal, cash-app-pay, instant-bank-payments]
---

## Overview

Stripe's dispute category guide maps the listed card, wallet, and Buy now, Pay Later reason codes to category-specific defense guidance. The 2026-05-09 capture covers Visa, Mastercard, American Express, Discover, Klarna, PayPal, and Cash App Pay. The 2026-11-07 capture adds a distinct Instant Bank Payments mapping and Mastercard code 4999. Use the tables in the dated raw captures for individual network codes and evidence fields; the mapped categories are not present for every listed method. See [[stripe]] and [[disputes]].

> [!warning] Category scope across captures
> The 2026-05-09 guide's opening describes an eight-category mapping broadly. The 2026-11-07 guide explicitly excepts Instant Bank Payments: all its disputes use `debit_not_authorized` and show an ACH return as the network reason code. Do not apply the card/wallet/BNPL category count to this method. [[disputes]]

## Category mapping

The listed methods use these category names where their tables contain a mapping: `credit_not_processed`, `duplicate`, `fraudulent`, `general`, `product_not_received`, `product_unacceptable`, `subscription_canceled`, and `unrecognized`. Visa additionally has `noncompliant` for certain Visa network-rule compliance disputes; it is not an additional category shown for all methods. In the 2026-11-07 tables, Visa has no `unrecognized` row code, Mastercard's `noncompliant` row says None, and Discover has no `product_unacceptable` or `unrecognized` mapping. Check the specific method's table rather than inferring a code from the category names. [[raw/stripe-disputes-categories-2026-11-07#Reason code categories|Reason code tables]]

| Method in the assigned captures | Scope locator |
| --- | --- |
| Visa, Mastercard, American Express, Discover | [[raw/stripe-disputes-categories-2026-11-07#Reason code categories|Card network tables]] |
| Klarna, PayPal, Cash App Pay | [[raw/stripe-disputes-categories-2026-11-07#Reason code categories|Other payment method tables]] |
| Instant Bank Payments (added 2026-11-07) | [[raw/stripe-disputes-categories-2026-11-07#Instant Bank Payments|ACH return mapping]] |

For Instant Bank Payments, the 2026-11-07 table lists R10 (unauthorized), R07 (authorization revoked), R08 (payment stopped), R11 (not per terms), R29 (corporate not authorized), R05 (unauthorized consumer debit using a corporate SEC code), and R31 (permissible return for corporate CCD/CTX accounts). These are underlying ACH network reason codes under the single Stripe dispute reason `debit_not_authorized`; the linked Disputed Instant Bank Payments page is a separate evidence guide and is not evidence of response requirements here. [[raw/stripe-disputes-categories-2026-11-07#Instant Bank Payments|Instant Bank Payments table]]

The 2026-11-07 Mastercard General table adds `4999 Domestic Chargeback Dispute (Europe Region Only)`, absent from the matched 2026-05-09 table. The Mastercard `Noncompliant | None` row makes its lack of that Visa-specific mapping explicit. [[raw/stripe-disputes-categories-2026-11-07#Mastercard|Mastercard table]]

## Evidence guidance

The category defense sections distinguish physical products, digital products or services, and offline services. Their tables suggest evidence and Dashboard/API fields by claim and product type: for example, refund or cancellation policy and disclosure, a rebuttal, customer communication when available, shipping documents and tracking for physical products, access/activity logs for digital products, and service dates or documents for offline services. These are context-specific suggestions, not a universal set of mandatory fields or proof of a successful challenge. [[raw/stripe-disputes-categories-2026-11-07#Category defense guidelines|Defense guidelines]]

Useful field locators include `refund_policy`, `refund_policy_disclosure`, `refund_refusal_explanation`, `cancellation_policy`, `cancellation_policy_disclosure`, `cancellation_rebuttal`, `customer_communication`, `uncategorized_text`, `uncategorized_file`, `shipping_carrier`, `shipping_tracking_number`, `customer_name`, `shipping_address`, `customer_purchase_ip`, `access_activity_log`, `service_date`, and `service_documentation`. The specific table and circumstance determine relevance. Where the guide asks whether a customer contacted the business before filing, it says to state that fact, including when there was no contact; it does not establish a universal prior-contact obligation. [[raw/stripe-disputes-categories-2026-11-07#Category defense guidelines|Evidence tables]]

For a fraudulent claim, the guide suggests showing that the legitimate cardholder or an authorized representative made the payment, or that successful 3D Secure authentication supports liability shift; it says Stripe provides the ECI automatically. It also points to Visa Compelling Evidence and suggests product-specific fields. These captures do not state Visa CE 3.0 eligibility, required or pre-populated CE 3.0 fields, an edit restriction, or automatic population of 3DS data. See [[source-stripe-disputes-visa-ce3]] for that separate topic. Visa reason code 10.5 is described here as having no evidence remedy. [[raw/stripe-disputes-categories-2026-11-07#Fraudulent|Fraudulent guidance]]

The guide's prevention advice is category-specific: clear refund/cancellation terms and timely entitled refunds for credit-not-processed claims; distinguish separate payments and correct accidental duplicates; recognizable statement descriptors and receipts for fraud or unrecognized claims; accurate delivery expectations and saved shipping proof for nonreceipt; accurate product descriptions for unacceptable-product claims; and prompt, clearly communicated subscription cancellation. These are the guide's suggestions, not guarantees of prevention or dispute outcomes. [[raw/stripe-disputes-categories-2026-11-07#Category defense guidelines|Prevention sections]]

## Visa compliance disputes

The guide describes Visa-only `noncompliant` disputes when an issuer believes a transaction violates network rules. If unresolved between parties, the network resolves the case for a fee. In these dated captures, contesting such a dispute incurs a 500 USD (or local equivalent) network cost in addition to applicable Stripe dispute fees, refunded if the dispute is won. This is a documented fee condition, not a current account quote or outcome promise. [[raw/stripe-disputes-categories-2026-11-07#Noncompliant|Noncompliant section]]

## Related

- [[disputes]] — Stripe category framework and dispute context
- [[source-stripe-disputes-responding]] — evidence submission process
- [[source-stripe-disputes-how-disputes-work]] — dispute lifecycle
- [[source-stripe-disputes-visa-ce3]] — separate Visa CE 3.0 authority
- [[stripe-3d-secure]] — 3DS context

## Raw Sources

- [[raw/stripe-disputes-categories-2026-11-07|Stripe dispute categories and evidence guidelines, captured 2026-11-07]]
- [[raw/stripe-disputes-categories-2026|Stripe dispute categories and evidence guidelines, captured 2026-05-09]]
