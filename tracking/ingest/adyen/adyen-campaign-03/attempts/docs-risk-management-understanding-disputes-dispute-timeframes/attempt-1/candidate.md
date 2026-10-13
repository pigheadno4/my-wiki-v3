---
title: "Adyen dispute timeframes"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/understanding-disputes/dispute-timeframes"
raw_files:
  - "adyen/docs/risk-management/understanding-disputes/dispute-timeframes/2026-09-15.md"
tags: [adyen, risk-management, disputes, chargebacks, timeframes]
---

## Overview

This [[adyen]] dispute-timeframes page maps calendar-day windows for cardholder disputes, requests for information (RFIs), chargeback defense, selected pre-arbitration flows, and later decisions across schemes and payment methods. Issuer timelines and the available response stage differ. The table and notes are a 2026-09-15 documentation snapshot, not a current deadline guarantee for an individual case; consult the case's scheme, reason code, processing region, opened date, and notices.

## Key takeaways

- The page describes a general maximum of 120 calendar days from transaction date for a cardholder to dispute, and a possible maximum of 540 calendar days for some Visa and Mastercard cases, such as delayed delivery or travel. The table then gives scheme-specific windows and starting events. Do not apply either maximum or a table value across every payment method or dispute reason.
- The main table distinguishes an RFI response measured from RFI date, issuer chargeback initiation measured from transaction date, merchant chargeback response measured from Notice of Chargeback (NoC) date, eligible pre-arbitration windows, and later decisions measured from defense date. The rows contain `n/a` cells, ranges, alternatives, and footnotes; they are not one universal sequence.
- The Visa chargeback response entry is 9 or 18 calendar days from NoC. The note limits the 9-day window to disputes opened from 21 July 2025 on payments processed locally in the United States or Canada; earlier such disputes and all other countries or regions have 18 days in this snapshot.
- Klarna can be answered only at the RFI stage: 14 days for consumer reason codes, 7 days for `unauthorized_purchase`, or 96 hours for `high_risk_order`. If the dispute is lost or documents are not uploaded, the chargeback is booked and cannot be defended. Other method-specific exceptions include an optional `ChargebackReversed` status and possible reopening for American Express, a PULSE 4868 pre-arbitration loss path, reason-code-dependent Accel/STAR initiation windows, and Mastercard pre-arbitration timing that can shorten if escalated to scheme arbitration.
- The requirements table routes dispute management through Customer Area or the Disputes API, lists Customer Area roles, and says Standard webhook dispute events must be enabled to follow disputes by webhook. It recommends understanding the dispute flow and cases Adyen automatically handles. These setup routes do not establish eligibility to defend any particular case.

## Detail locators

- `# Dispute timeframes`, raw lines 15–19 — page purpose and issuer-dependent response framing.
- `## Requirements`, raw lines 21–33 — online integration, Customer Area roles, Standard webhook dispute-event setup, management routes, and recommendations.
- `## Timeframes`, raw lines 35–49 — general 120/possible 540-day statement and complete calendar-day scheme/payment-method table, with the starting event in each row.
- `### Notes`, raw lines 53–62 — Klarna RFI-only defense, three reason-code windows, and final lost-chargeback behavior.
- `### Notes`, raw lines 64–83 — American Express, PULSE, Accel/STAR, Visa local-processing date exception, and Mastercard pre-arbitration qualifications.

## Related

- [[adyen]] — provider page.
- [[adyen-risk-management]] — provider risk and disputes source routes.
- [[disputes]] — general dispute concept.

## Raw Sources

- [[raw/adyen/docs/risk-management/understanding-disputes/dispute-timeframes/2026-09-15|Adyen dispute timeframes (2026-09-15 snapshot)]]
