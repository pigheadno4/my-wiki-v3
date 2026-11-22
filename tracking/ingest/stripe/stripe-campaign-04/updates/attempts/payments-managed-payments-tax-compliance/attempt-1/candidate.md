---
title: "Tax Compliance with Managed Payments"
type: source
date_ingested: 2026-04-23
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/managed-payments/tax-compliance"
raw_files:
  - "stripe-payments-managed-payments-tax-compliance-2026-11-07.md"
  - "stripe-managed-payments-tax-compliance-2025.md"
tags: [stripe, managed-payments, merchant-of-record, tax-compliance, vat, gst, sales-tax, stripe-tax, japan, singapore]
---

## Summary

[[stripe]]’s April 23 and November 7, 2026 guides describe how [[stripe-managed-payments]] handles indirect taxes such as sales tax, VAT and GST on covered digital-product sales in more than 80 countries. On covered sales, Stripe calculates and collects tax and issues tax invoices where required, registers and files with local authorities, and remits collected tax. The seller has no indirect-tax compliance action for the covered sale described. Country coverage, supported seller locations and individual account eligibility are separate.

## November 2026 — Thresholds and Tax Responsibility

The November guide adds that local sales and volume thresholds can yield `taxability_reason: not_subject_to_tax` in a covered country while Managed Payments still handles that sale’s indirect-tax compliance. See November raw lines 20-24. The example leaves the specific threshold, API object and version unstated. It describes one outcome among covered transactions, without assigning that reason to every zero-tax result.

## Domestic Sales Exceptions

Both captures describe domestic digital-product coverage in supported business locations with these exceptions.

- **Japan:** The Japan-based seller is responsible for tax calculation, collection, filing and remittance on domestic sales of digital goods.
- **Singapore:** The Singapore-based seller remains responsible on domestic business-to-business sales. The customer identifies as a business at checkout.

Japan and Singapore also appear in the cross-border destination list. For supported seller locations and digital-product eligibility, see [[source-stripe-managed-payments-eligibility]]. See April raw lines 19-29 and November raw lines 20-32 for the domestic and cross-border scope.

## Cross-Border Tax Coverage

The two dated captures list the same 82 destination codes, including 27 in the EU. These are destinations for the stated digital-product tax coverage.

| Region | Codes |
| --- | --- |
| Africa (9) | CM, EG, GH, KE, NG, UG, ZA, ZM, ZW |
| Asia Pacific (28) | AM, AU, AZ, BN, GE, HK, ID, IL, IN, JP, KG, KR, KW, KZ, LA, MO, MY, NP, NZ, PH, QA, SA, SG, TH, TJ, TR, TW, VN |
| Europe outside the EU (11) | AL, BY, CH, GB, GI, IS, LI, MD, NO, RS, UA |
| European Union (27) | AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HR, HU, IE, IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK |
| Latin America and the Caribbean (5) | BB, BM, KY, MX, VG |
| North America (2) | CA, US |

Cross-border sales to customers in Serbia qualify for the described coverage only when the seller is not VAT-registered in Serbia. See April raw lines 27-131 and November raw lines 30-134.

## Seller-Responsible Tax and Optional Stripe Tax

Where Managed Payments cannot assume indirect-tax liability, the seller remains responsible for local registration, calculation, collection, filing and remittance. Managed Payments can still serve as merchant of record for payments, fraud prevention, disputes and transaction-level support for those sales.

[[stripe-tax]] is the only compatible integrated tax solution for Managed Payments. The guides describe no additional Stripe Tax calculation fees **on Managed Payments transactions**. The fee statement covers those calculations. The optional workflow can monitor country registration thresholds and offers third-party partner assistance with registration, filing and remittance. This assistance runs through the Stripe Tax workflow. Compliance remains the seller’s responsibility.

1. Enable Stripe Tax under **Dashboard → Settings → Tax → Integrations**.
2. After local registration, upload the registration on the Dashboard **Tax** page to begin automatic tax calculation and collection. Enabling Stripe Tax or registering locally completes only part of this documented workflow.

See April raw lines 133-151 and November raw lines 136-155.

## Invoice and Receipt Identity

Managed Payments sends the invoice to the customer. For a seller-responsible tax transaction, the invoice displays the seller’s business name and tax details. A separate receipt email and PDF include **Sold through Link** details. Keep the seller information current under **Dashboard → Settings → Billing → Invoices**. The setting controls invoice details. See [[source-stripe-managed-payments-how-it-works]] for Link as the sender of customer communications and for the boundary on Dashboard receipt settings. See April raw lines 153-157 and November raw lines 157-161.

## Raw Sources

- [[raw/stripe-payments-managed-payments-tax-compliance-2026-11-07|Stripe’s November 7, 2026 Managed Payments tax compliance guide]]
- [[raw/stripe-managed-payments-tax-compliance-2025|Stripe’s April 23, 2026 Managed Payments tax compliance guide]] — verbatim tax compliance guide, 157 lines.
