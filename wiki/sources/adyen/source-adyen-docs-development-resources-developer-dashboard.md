---
title: "Adyen Developer dashboard"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/developer-dashboard"
raw_files:
  - "adyen/docs/development-resources/developer-dashboard/2026-09-15.md"
tags: [adyen, developer-dashboard, monitoring, api-logs, webhooks]
---

## Overview

This [[adyen]] guide describes the Customer Area **Developer dashboard** for monitoring an integration's technical performance. It shows API-request and webhook activity, success/failure trends, and errors that can be opened in API or webhook event logs. The dashboard is an observability route through [[adyen-developer-dashboard]], not evidence of a payment's financial outcome.

## Key takeaways

- The page states an Adyen integration of any type as its integration prerequisite and requires a **Merchant admin** or **Merchant technical integrator** Customer Area user role to access **Developers > Dashboard**. This user-role gate is distinct from API-credential roles. See **Requirements** and **Monitor your integration's performance**, raw lines 21–30 and 88–95.
- The dashboard shows API-request and webhook activity/errors for the past seven days by default, with selectable time range and interval. Integration activity can show success rate or counts of successful and failed requests and webhooks; errors lead to API or webhook event logs for inspection. See **Integration and account information** and **Monitor your integration's performance**, raw lines 32–45 and 95–107.
- The **Integration types** panel classifies account integrations as APIs, libraries, plugins, or Checkout SDKs and lists possible online, in-person and omnichannel types. Its **Live URL prefix** panel is available only in the **live Customer Area**. Account details, company contacts and resource links are also described. See raw lines 40–86.
- The page says the dashboard includes only **specific APIs and webhooks**, but this retained raw has no section resolving its `#included` anchor or complete coverage inventory. Avoid treating listed integration types as a complete monitored-API/webhook list. A request/webhook success count is a technical signal; it does not by itself establish payment authorization, capture, settlement or fulfillment.

## Detail locators

- Purpose and recommended monitoring use: **Developer dashboard**, raw lines 15–19.
- Integration and Customer Area user-role requirements plus coverage limitation: **Requirements**, raw lines 21–30.
- Activity, error, integration-type and account panels: **Integration and account information**, raw lines 32–86.
- Access path, trend controls and log drilldowns: **Monitor your integration's performance**, raw lines 88–107.

## Related

- Company: [[adyen]]
- Concept: [[adyen-developer-dashboard]]
- Adjacent webhook behavior: [[adyen-webhooks]]
- Adjacent API credentials and roles: [[adyen-api-access]]

## Raw Sources

- [[raw/adyen/docs/development-resources/developer-dashboard/2026-09-15|Adyen Developer dashboard]] — full pinned 2026-09-15 snapshot; page metadata says last modified 2024-01-29
