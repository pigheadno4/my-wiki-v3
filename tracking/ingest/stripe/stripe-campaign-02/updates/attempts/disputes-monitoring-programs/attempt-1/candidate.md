---
title: "Stripe — Dispute and Fraud Card Monitoring Programs"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/disputes/monitoring-programs"
raw_files:
  - "stripe-disputes-monitoring-programs-2026-11-07.md"
  - "stripe-disputes-monitoring-programs-2026.md"
tags: [stripe, disputes, monitoring, vamp, merp, vsefp, ecp, ecm, hecm, efm, auspaynet, mastercard, visa, fraud, chargebacks]
---

## Overview

Stripe's May 10 and November 7, 2026 captures explain card-network dispute and fraud monitoring. The November guide adds **Visa Merchant Elevated Risk Program (MERP)**, effective October 2026 for businesses accepting Visa in Asia Pacific, and revises the VAMP dashboard and pre-dispute refund guidance. This is Stripe's **general guide**, expressly not a comprehensive or authoritative current network-rule reference. Network documentation and account communications determine current program terms and actual status.

Monitoring can lead to conditional network assessments, escalating fines in some programs, remediation, lost liability shift, or processing risk. None of these snapshots establishes this business's program identification, fine, eligibility, or processing outcome.

## Counting and calendar rules

- A monitored dispute or chargeback occurs when funds move out due to a disputed payment. Refunds and later dispute outcomes generally do not remove it from network monitoring counts. Some Stripe-handled, no-liability disputes do not show in Dashboard/API or Stripe rates, yet networks still count them; discrepancies can also arise from statement descriptors, multiple MIDs, or double-counted charges. Unescalated inquiries and non-disputed RDR movements do not count as disputes. EFWs are not disputes but count as fraud in Visa VAMP.
- The **November** guide says that after a full refund before a dispute, one can respond to that dispute and links further guidance; it does not promise removal from network monitoring. The **May** guide said Stripe could ask for removal if a full refund was issued at least 10 days before the dispute. Keep that as dated historical wording; omission alone does not prove that request route ended.
- Visa and Mastercard identify data by report month, not original transaction month. Visa's ratio uses captured payments in the same calendar month as dispute/fraud reports; Mastercard's chargeback and fraud rates use the **preceding month's** captured payments. AusPayNet measures by quarter. For manual Stripe estimates, the guide uses calendar months outside the US; for US accounts it suggests a dispute window from the 5th of a month through the 5th of the following month against calendar-month payments. These are estimate instructions, not network-final data.

## Visa programs

### VAMP: disputes and fraud

VAMP has separate disputes/fraud and enumeration tracks. VAMP count combines TC15 disputes and TC40 EFWs; volume is the USD amount; ratio is count divided by all captured-payment count. Pre-dispute resolutions and CE 3.0 qualifying TC40 fraud are excluded. A transaction in both TC15 and TC40 can be counted twice.

| Criterion | Non-compliant | Excessive outside CEMEA | Excessive CEMEA |
| --- | --- | --- | --- |
| VAMP count | 5 | 1,500 | 150 |
| VAMP ratio | 0.5% | 1.5% | 2.2% |
| VAMP volume | N/A | N/A | 75,000 USD |

These are the guide's regional criteria, not a universal single-number trigger. Visa assesses fees above Excessive and **may** assess fees above Non-Compliant; Stripe says it notifies the account if Visa assesses a fine. Exact threshold combinations and current network rules should be checked with Visa. November raw lines 84–110.

### VAMP: enumeration and dashboard

Enumeration count is processor-reaching card-testing authorizations, approved or declined; enumeration ratio divides by **all authorization transactions**, rather than captured payments. The guide says an account enters Excessive enumeration monitoring when **both** count exceeds 300,000 and ratio exceeds 20%. Visa does not assess fines for this track. November raw lines 112–126.

The November VAMP dashboard path is `dashboard.stripe.com/radar/cbmp/vamp`, with Program standing, VAMP trend chart, Visa data, Stripe data, and Resources. Visa's monthly data by statement descriptor determines compliance and arrives with a one-month delay. Stripe computes daily estimates that may differ. The May capture instead showed a test-mode dashboard URL and History/Historical-current/Projected panels; do not treat that older layout as November's page. November raw lines 128–138; May raw lines 127–135.

### MERP: Visa Merchant Elevated Risk Program

The November guide says MERP is effective **October 2026** for businesses accepting Visa in **Asia Pacific**. It targets concentrated early-life risk before portfolio-level volume thresholds, considering transaction count/volume, fraud volume/rate, **non-fraud dispute** volume/rate, and authorization count/decline rate **together**. Visa does **not publish** individual numeric identification thresholds. Do not apply VAMP count or ratio limits to MERP.

If Visa identifies a business, it notifies Stripe; Stripe contacts an active account. Response windows are short, and a prompt information response may help Stripe contest an identification where evidence supports it. **If Visa confirms** identification, possible consequences include network assessments charged to Stripe that might be passed through, a specific window for backdated fraud disputes, a remediation plan, Stripe closure in some circumstances, and possible VMSS listing with effects at other acquirers. These are conditional possibilities, not observed outcomes. November raw lines 140–164.

### VSEFP: US domestic 3DS fraud

VSEFP applies only to **US-based businesses with US-based custom accounts** and domestic Visa 3DS-authenticated transactions on US-issued cards. Both monthly thresholds must be met: **75,000 USD** TC40 EFW volume and **0.9%** EFW USD volume divided by captured 3DS Visa USD volume. The guide says no fine, but liability shift on domestic 3DS transactions is lost until full exit. The report month for EFWs can differ from the capture month of the original payment. November raw lines 166–181.

## Mastercard programs

ECP includes ECM and HECM and is described for supported countries. EFM is a separate program, excluding Germany, India, and Switzerland. The chargeback rate is current-month chargeback **count** divided by preceding-month captured-payment **count**. A chargeback belongs to the month raised. Mastercard counts chargebacks even if hidden after a refund, subject to liability shift, or later won. Three consecutive months below a program threshold are needed to exit; an HECM account that falls below HECM but remains at ECM moves to ECM. If EFM and ECP both apply, EFM identification takes precedence while both tracks continue to accrue months. November raw lines 183–204.

| Program | Both count and rate criteria | Fine timing and amounts in the guide |
| --- | --- | --- |
| ECM | 100–299 chargebacks; 1.5–2.99% | Month 1: 0 USD; 2–3: 1,000; 4–6: 5,000; 7–11: 25,000; 12–18: 50,000; 19+: 100,000 USD |
| HECM | 300+ chargebacks; 3% | Month 1: 0 USD; 2: 1,000; 3: 2,000; 4–6: 10,000; 7–11: 50,000; 12–18: 100,000; 19+: 200,000 USD |

Issuer recovery assessment is marked **Yes** in ECM months 4+ and HECM months 4+. The guide describes an additional 5 USD per chargeback **over 300** when it applies. These are dated table schedules, not proof of an assessed fee. November raw lines 206–239.

**EFM** requires **all**: at least 1,000 e-commerce Mastercard payments; net fraud volume from reason codes 4837 or 4863 **greater than** 50,000 USD, or 15,000 USD in Australia; fraud chargeback rate **greater than** 0.50%, or 0.20% in Australia, using current-month fraud chargeback count over preceding-month e-commerce transaction count; and 3DS Mastercard payment count **at or below** 10% of total Mastercard payments in non-regulated countries or 50% in regulated countries. Fine schedule: month 1 0 USD; 2 500; 3 1,000; 4–6 5,000; 7–11 25,000; 12–18 50,000; 19+ 100,000. The guide describes a one-time request for suspension of an assessed fine during an open case, with resumed assessments if the business fails to stay below exit thresholds for three months. November raw lines 241–271.

## AusPayNet FMP

For **Australian users and cardholders** in card-not-present (CNP) activity, AusPayNet FMP uses quarterly fraud chargeback **amount greater than 50,000 AUD** and fraud-amount-to-sales-value ratio **at least 0.20%**, both required. The computations exclude card-present and 3DS-authenticated transactions. After two consecutive high-fraud quarters AusPayNet reserves the option to mandate SCA; Stripe notifies accounts that exceed the preceding quarter's program thresholds. The remediation table calls for fraud controls in quarter 1, one or more risk-based/full-CNP SCA or stronger controls in quarter 2, issuer SCA for all CNP in quarter 3 with off-boarding risk, and possible off-boarding in quarter 4+. One quarter below criteria releases the FMP/SCA obligations. The guide lists recurring-first-charge, previously authenticated trusted-customer, and authenticated-wallet exemptions. November raw lines 273–312.

## Prevention and detail locators

The guide recommends reversing suspicious authorizations **before capture**, easier subscription cancellation and clear billing terms, reminders and refund policies, shipping communication/tracking/signature, accurate product descriptions, and better evidence for friendly-fraud disputes. These are practices, not a guarantee of avoiding a program. November raw lines 314–353.

## Related

- [[stripe-dispute-monitoring-programs]] — concept route for these program distinctions.
- [[stripe-high-risk-merchant-lists]] — merchant screening and listing context.
- [[source-stripe-disputes-measuring]] — Stripe dispute metrics.

## Raw Sources

- [[raw/stripe-disputes-monitoring-programs-2026-11-07|November 7, 2026 monitoring-program guide]]
- [[raw/stripe-disputes-monitoring-programs-2026|May 10, 2026 monitoring-program guide]]
