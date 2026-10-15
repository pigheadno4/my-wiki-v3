---
title: "Adyen Developer dashboard"
type: concept
category: technology
tags: [adyen, developer-dashboard, observability, api-logs, webhooks]
---

## Definition

The Adyen Customer Area Developer dashboard presents technical activity and errors for an integration's API requests and webhooks. It shows recent success/failure trends and allows drilldown to API or webhook event logs; the retained guide says its default window is the past seven days and users can select other ranges and intervals. Access requires the **Merchant admin** or **Merchant technical integrator** Customer Area user role. [[source-adyen-docs-development-resources-developer-dashboard]]

## Scope and evidence boundary

The guide says dashboard coverage is limited to specific APIs and webhooks, but its retained `#included` anchor does not resolve to a coverage list. The Integration types panel is an account classification, not proof of complete monitoring coverage. The **Live URL prefix** panel appears only in the live Customer Area. Activity and webhook success rates are technical observations; they do not prove payment authorization, capture, settlement, current account access, or a live integration's health. This is a 2024-last-modified page captured 2026-09-15. Dashboard user roles are distinct from [[adyen-api-access|API credential roles]], and underlying webhook delivery behavior belongs to [[adyen-webhooks]].

## Sources

- [[source-adyen-docs-development-resources-logs-resources]] — 2026-09-15 Logs landing page linking webhook event logs and API logs for testing/troubleshooting; navigation only.


- [[source-adyen-docs-development-resources-logs-resources-api-logs]] — 2026-09-15 API Logs guide for JSON request/response diagnostics, 30-day retention, Customer Area access roles and account placement; technical logs do not establish financial outcomes.


- [[source-adyen-docs-development-resources-developer-dashboard]] — Adyen Developer dashboard access, technical activity/error panels, log drilldowns and account/environment qualifications (2026-09-15 snapshot).
