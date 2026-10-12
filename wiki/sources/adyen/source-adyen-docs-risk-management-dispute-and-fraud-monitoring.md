---
title: "Adyen Risk and Dispute Analytics Monitoring"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/dispute-and-fraud-monitoring"
raw_files:
  - "adyen/docs/risk-management/dispute-and-fraud-monitoring/2026-09-15.md"
tags: [adyen, risk-management, fraud, disputes, analytics]
---

## Overview

This Adyen documentation snapshot describes the Customer Area **Risk & dispute analytics** dashboard for reviewing risk performance, chargeback and fraud trends, dispute handling, and refunds across online and/or in-person payments. Its Overview, Card monitoring programs, Disputes, and Refund activity tabs serve different purposes. See [[adyen]] and [[adyen-risk-management]].

## Key takeaways

- The dashboard requires an eligible Customer Area role. Dashboard filters such as date range, merchant account, issuer region, and payment method apply to Overview, Disputes, and Refund activity; the risk-performance section has additional filters.
- The **Card monitoring programs** tab is limited to Visa and Mastercard scheme programs at the **company account** level. The page separately documents monitoring criteria for other schemes, including Cartes Bancaires, Elo, Pulse, and UnionPay; those entries do not expand the tab's stated coverage. The **Disputes** tab excludes Requests for Information (RFIs).
- Scheme program calculations and thresholds differ by network, region, metric, and effective date. This snapshot describes monthly monitoring and dated Visa VAMP thresholds, plus Mastercard and other scheme criteria. Reaching a scheme threshold can place a merchant in a monitoring program, with possible fines and, in the worst case, consequences for payment processing. Treat the listed thresholds as snapshot evidence, not current scheme-policy or account-status verification.
- The US-specific Visa Secure Excessive Fraud Program concerns fraudulent transactions successfully authenticated with 3D Secure 2, issued in the US and processed through Visa US acquiring. The page says program entry makes Visa reason-code `10.5` fraud disputes non-defendable by the merchant, with a 120-calendar-day issuer filing window from identification. This consequence is conditional on that program, not a general result of using 3D Secure 2.
- The Disputes tab groups metrics by chargeback type, defense method, status, issuer, and reason code, with Amount or Count views. Its status and defense-method labels have specific definitions in the raw; do not equate a pending dispute with a loss or an automatically defended dispute with a win.
- Refund activity covers online and in-person payments, including referenced and unreferenced point-of-sale refunds. **Top refund contributors** can route to shopper DNA, but shopper DNA requires Protect premium and role-gated access; shopper attributes are masked by default, with **Merchant View PII** needed to see unmasked details.

## Detail locators

- Dashboard purpose, tabs, integration types, roles, and limitations: lines 15–43.
- Navigation and filter scope: `## Risk & dispute analytics dashboard`, lines 45–59; Overview and risk-performance drill-down at lines 60–89.
- Company-account Card monitoring tab and Visa/Mastercard program list: lines 90–104. Scheme metric definitions and monthly consequences: lines 106–127.
- Visa VAMP definitions, dated thresholds, count/region criteria, and RDR/CDRN treatment: lines 129–170; US-only Visa Secure Excessive Fraud Program and reason-code `10.5` consequence: lines 171–190.
- Mastercard ECP/EFM criteria, including Australian distinction: lines 192–225. Other scheme sections: Cartes Bancaires lines 226–243, Elo lines 244–277, Pulse lines 278–292, UnionPay lines 293–316.
- Disputes filters, defense/status definitions, and breakdown: `## Disputes`, lines 317–379.
- Refund coverage, metrics, shopper DNA access, and industry context: `## Refund activity`, lines 380–431.

## Related

- [[adyen]] — provider context.
- [[adyen-risk-management]] — provider risk-management concept and reciprocal source route.
- [[disputes]] — cross-provider dispute concept.

## Raw Sources

- [[raw/adyen/docs/risk-management/dispute-and-fraud-monitoring/2026-09-15|Adyen monitor risk performance (2026-09-15)]]
