---
title: "Stripe Billing — Customer Tax IDs"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/customer/tax-ids"
raw_files:
  - "stripe-billing-customer-tax-ids-2026-11-07.md"
  - "stripe-billing-customer-tax-ids-2026.md"
tags: [stripe, billing, tax, tax-ids, vat, eu-vat, invoices, customers, validation]
---

## Overview

Stripe Billing's customer tax ID guide covers storing, validating, and rendering customer tax IDs. The 2026-11-07 capture adds an explicit format-versus-government validation comparison and separate verification-event paths for v1 Customers and customer-configured Accounts. The 2026-05-13 capture remains below as historical evidence. Neither capture establishes account-specific availability or a tax outcome for a particular customer.

## Key takeaways

- Customer tax IDs appear in invoice and credit note PDF headers in both captures. The dated supported-type tables, enums, examples, and "Impact in Tax Calculation" column are in the raw pages; the November table adds types including `au_acn`, `au_wpn`, `cz_dic`, `fr_siren`, `fr_siret`, and `fr_spi`. The row examples do not establish account eligibility.
- The table's "Yes" flag carries a legal-condition footnote. The November guide says Stripe Tax applies reverse charge or zero rate according to applicable laws when the number has the required format, regardless of the government verification result. A "Yes" row alone is not an unconditional B2B exemption or proof of government verification.
- Stripe checks AU ABNs against the Australian Business Register, EU VAT numbers against VIES, and GB VAT numbers against HMRC. These checks establish tax ID validity, not a match of the customer's name and address; for ABNs, GST registration matching is also the user's responsibility. Other types receive format checks only, without government-database validation. The customer remains responsible for information accuracy, an invoice can show an invalid ID, and Stripe does not keep validating IDs over time.
- For a tax ID saved to a v1 Customer, the November guide says to listen for the `customer.tax_id.updated` snapshot event and inspect `data.object.verification.status`. For a customer-configured Account, it says to listen for the `v1.customer.tax_id.updated` thin event, retrieve the Tax ID through `related_object`, then inspect `verification.status`. It says an event is sent when verification finishes; it does not establish an event for every status transition. The Account event reference linked in the capture uses `api-version=preview`; availability and rollout are not established here.
- The listed verification statuses are `pending`, `verified`, `unverified`, and `unavailable`. Handle `unverified` according to your compliance requirements; if automatic validation is `unavailable`, manually verify the ID.
- IDs can be managed through the Dashboard, customer portal, or Tax ID API. Updating an ID means deleting the old ID and creating another. The captured API examples distinguish `owner[customer]={{CUSTOMER_ID}}` for Customers v1 from `owner[customer_account]={{CUSTOMERACCOUNT_ID}}` for Accounts v2; the latter concerns a customer-configured Account.

## Detail locators

- Supported types and tax-impact footnote: November raw lines 13–182; May raw lines 12–162. The November examples include a changed `ng_tin` example (line 132 versus May line 117); treat examples as examples.
- Validation scope, government checks, responsibility, and noncontinuous validation: November lines 184–219; May lines 164–184.
- Sandbox magic IDs `000000000` (successful), `111111111` (unsuccessful), and `222222222` (pending indefinitely) apply to AU ABN, EU VAT, or GB VAT types: November lines 221–229; May lines 186–194. They do not demonstrate a live tax result.
- Object-specific events, statuses, unavailable handling, and conditional Stripe Tax treatment: November lines 231–242. The May page's earlier Customer webhook wording is at lines 196–205.
- Dashboard, portal, API management and the two owner-specific creation examples: November lines 249–295; May lines 207–253.
- For additional tax ID types, the May capture points to `stripe-tax@stripe.com` (line 8); the November capture points to Stripe support (line 9). The change of guide text does not establish that the old address stopped working.

## Related

- [[stripe-tax]] — Stripe Tax concept and reciprocal source route
- [[stripe-tax-id-element]] — Tax ID Element UI component
- [[stripe-subscriptions]] — subscriptions concept
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-customer-tax-ids-2026-11-07|Stripe Billing Customer Tax IDs, captured 2026-11-07]] — full guide, 295 lines
- [[raw/stripe-billing-customer-tax-ids-2026|Stripe Billing Customer Tax IDs, captured 2026-05-13]] — prior full guide, 253 lines
