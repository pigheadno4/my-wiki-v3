---
title: "Stripe — Fraud Insights"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/radar/analytics/fraud-insights
raw_files:
  - "stripe-radar-analytics-fraud-insights-2026-11-07.md"
  - "stripe-radar-fraud-insights-2026.md"
tags: [stripe, radar, fraud-insights, fraud-teams, pivot-chart, analytics, investigation]
---

## Summary

Both guides describe the Radar Insights tab in the [[stripe]] Dashboard for viewing fraud patterns, inspecting matching payments and deciding how to respond. The May 10, 2026 guide names Radar for Fraud Teams for access. The November 7 guide names Radar Plus and adds analysis of payments that triggered fraud alerts.

The separate November plan table marks transaction fraud alerts supported on Lite, Standard, Plus and Pro. It marks agentic insights supported on Plus and Pro. Those plan rows leave historical plan mapping and merchant-specific entitlement unresolved. [[raw/stripe-radar-how-radar-works-2026-11-07|November plan table, lines 15–45]]

## Default view and filters

The initial view shows the prior three months in near real time. It uses successful payment status, risk score strictly greater than 65 and more than 10 charges per card number per hour. These are the Insights view filters (May lines 15–37, November lines 17–39).

- Set a preset or custom date range and apply it.
- **All payments** includes successful, blocked and declined outcomes. **Successful payments** shows successful payments only.
- **All fraud** includes fraud disputes, early fraud warnings and payments refunded as fraud. **Disputes** includes any category. **Early fraud warnings** is a separate status filter.
- Use attribute filters such as risk score, card BIN, card brand, card country or IP country. The Dashboard offers additional account-specific Radar attributes.

## Review filtered payments

Insights shows fraud volume and the disputed-payment count for the selected data. Its pivot chart groups transaction counts by day, week, month or attributes such as card brand, card country or risk score ranges. The transaction list shows the risk score, amount and currency, status, customer, payment method and creation time. Select a row to open the payment details (May lines 44–74, November lines 46–76).

Merchants can consider refunding an individual high-risk payment from its row menu, enabling risk controls for a pattern, or writing a custom rule for identified attributes. Changing a filter or finding a pattern does not itself change a payment or a rule (May lines 76–87, November lines 78–89).

## Alert-triggered analysis

November describes Radar analyzing payments that triggered a fraud alert. An alert can produce one or more insights, each describing a candidate pattern in those payments. Examples include a common email domain, transactions without 3D Secure authentication or an unusual concentration of a card attribute. Patterns depend on the payments behind the alert (November lines 91–97).

Open an insight to review fraud volume, disputed-payment counts and individual transactions, and pivot by time or a payment attribute. The merchant can use the pattern to decide whether to create or adjust a custom rule or change risk settings. The insight gives the operator a pattern to investigate. Fraud verification and any action are separate (November lines 99–108).

The separate transaction fraud alert guide describes email and Dashboard bell notifications linking to a dedicated investigation page, with actions depending on the plan. That delivery and investigation route is distinct from agentic pattern display in Insights. [[source-stripe-radar-fraud-alerts|Transaction fraud alerts]] · [[raw/stripe-radar-analytics-transaction-fraud-alerts-2026-11-07|November alert guide, lines 9–38]]

## Related Pages

- [[stripe-radar]] — Radar concept and related workflows
- [[source-stripe-radar-analytics]] — Radar Analytics Center
- [[source-stripe-radar-fraud-alerts]] — separate fraud alert investigation
- [[source-stripe-radar-risk-settings]] — risk controls
- [[source-stripe-radar-rules]] — custom rules
- [[source-stripe-radar-how-it-works]] — plan comparison

## Raw Sources

- [[raw/stripe-radar-analytics-fraud-insights-2026-11-07|Fraud Insights, captured 2026-11-07]] — full 108-line guide with agentic alert analysis.
- [[raw/stripe-radar-fraud-insights-2026|Fraud Insights, captured 2026-05-10]] — full 87-line guide with May plan wording and the filtered analysis workflow.
