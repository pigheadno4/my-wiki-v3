# Fixed-query probes — Adyen Developer dashboard

## Q1 — purpose, scope, and non-inference

**Question:** What is Adyen's Developer dashboard for, who can access it, and what can its metrics not prove?

**Answer:** The captured guide presents a Customer Area dashboard for technical health of an Adyen integration: API-request and webhook activity, success/failure trends, errors, and log drilldown. It states any Adyen integration as the integration type and requires a **Merchant admin** or **Merchant technical integrator** Customer Area user role. The dashboard covers only specific APIs and webhooks, but the retained page's `#included` link has no target coverage list; do not assume every API or event appears. A successful request/webhook count is an integration signal, not proof of payment authorization, capture, settlement or fulfillment. Read [[source-adyen-docs-development-resources-developer-dashboard]] and [[adyen-developer-dashboard]]; evidence is [[raw/adyen/docs/development-resources/developer-dashboard/2026-09-15|Developer dashboard raw snapshot]] lines 15–38, 88–107.

## Q2 — central capability, prerequisites, and warnings

**Question:** Which dashboard panels and drilldowns help monitor an integration, and what account or environment limits apply?

**Answer:** The captured page says the default activity/error window is the past seven days, with selectable time range and interval. The **Integration activity** panel shows server API requests and Adyen-to-server webhooks, with success-rate or successful/failed-count views. **Errors** entries and graph points link to API or webhook event logs. The **Integration types** panel classifies account use across APIs, libraries, plugins and Checkout SDKs, while account details, company contacts and resources appear elsewhere. The **Live URL prefix** panel is live-Customer-Area only. Access requires one of the two specified **Customer Area user roles**; this is distinct from an API credential's roles. The listed integration types do not establish a complete monitoring coverage inventory, and dashboard observations do not establish a payment's financial outcome or current account access. Read [[source-adyen-docs-development-resources-developer-dashboard]] and [[adyen-developer-dashboard]]; evidence is [[raw/adyen/docs/development-resources/developer-dashboard/2026-09-15|Developer dashboard raw snapshot]] lines 21–30, 32–86 and 88–107.
