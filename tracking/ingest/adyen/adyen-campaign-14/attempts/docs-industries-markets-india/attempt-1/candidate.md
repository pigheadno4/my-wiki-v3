---
title: "Adyen domestic payments in India overview"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/industries/markets/india"
raw_files:
  - "adyen/docs/industries/markets/india/2026-09-15.md"
tags: [adyen, india, domestic-payments, recurring, compliance]
---

## Overview

This 2026-09-15-captured Adyen overview presents conditions and child-guide routes for **domestic payments in India**. It says a merchant needs an Indian local entity and integration, and should contact its Adyen account manager for India onboarding and an India Customer Area before starting. It summarizes stored-card/recurring conditions, selected methods and a BillDesk dispute route. This is a provider snapshot, not current legal advice, onboarding approval or proof of payment readiness. See [[adyen-online-payments]] and [[adyen]].

## Key takeaways

- **Domestic and account boundary:** The page is expressly about domestic processing in India; it does not set rules for cross-border transactions or define a merchant-of-record arrangement. It requires a local entity and local integration and describes Adyen-assisted onboarding/India Customer Area setup. It does not itself grant credentials, acquiring enablement, payment-method eligibility or live status.
- **Stored-card and recurring conditions:** The guide says only last four PAN digits and issuer name may be stored for domestic payments; it maps one-off, subscription and automatic top-up use to `CardOnFile`, `Subscription` and `UnscheduledCardOnFile` respectively. Before subscription/automatic-top-up charges, it calls for shopper mandate consent, pre-debit notification and a 48-hour wait. Initial requests include `mandate` parameters; later recurring charges require POST `/notifyShopper` and a reference to the resulting notification. Detailed implementation belongs to the linked India card and UPI guides; this overview does not define every exception or token storage schema.
- **Method and conditional threshold:** It lists global card schemes supported in India alongside RuPay, Online banking India, UPI and Wallets India. It says gross receipts **exceeding 50 crore INR** trigger a requirement to offer RuPay and UPI (UPI Collect and UPI QR). The page does not make those methods universally enabled for each merchant or assert a payment-currency requirement. It says domestic recurring is available only through UPI, RuPay and supported global card schemes in the snapshot.
- **Dispute route:** For card/UPI transactions, the overview describes BillDesk sending a Notification of Chargeback, then a seven-day merchant response window. It says that after 60 days without a booked chargeback a defense can be considered won, **but** issuer pre-arbitration can still follow. These are dispute-stage descriptions, not irrevocable financial finality.

## Detail locators

- Lines 15–21: domestic scope, local entity/integration and account-manager/India Customer Area onboarding.
- `## Compliance`, lines 23–44: RBI card-data, stored-credential models, mandate/notification/48-hour summary and child routes.
- `## Payment methods`, lines 46–89: conditional 50-crore-INR RuPay/UPI claim and local method navigation.
- `## Recurring payments`, lines 91–104: method set, initial mandate, `/notifyShopper` and notification reference.
- `## Chargebacks`, lines 106–116: BillDesk NoC, seven-day response and qualified 60-day defense status.

## Related

- [[adyen-online-payments]] — primary online-payments concept and India-specific route.
- [[source-adyen-docs-online-payments-payments-india-compliance-guide]] — detailed domestic/local-acquiring and recurring compliance guide.
- [[source-adyen-docs-online-payments-payments-india-compliance-guide-go-live-india]] — India live-preparation checklist.
- [[source-adyen-docs-risk-management-chargeback-guidelines-billdesk-chargebacks]] — India BillDesk dispute detail.

## Raw Sources

- [[raw/adyen/docs/industries/markets/india/2026-09-15|Domestic payments in India overview, captured 2026-09-15]]
