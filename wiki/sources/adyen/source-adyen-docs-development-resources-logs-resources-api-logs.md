---
title: "Adyen API logs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/logs-resources/api-logs"
raw_files:
  - "adyen/docs/development-resources/logs-resources/api-logs/2026-09-15.md"
tags: [adyen, api-logs, customer-area, troubleshooting]
---

## Overview

This Adyen Docs page explains how to inspect recent API request metadata and request/response details in Customer Area when analyzing or debugging an integration. It covers JSON API requests made in test or live during the preceding 30 days; older requests are removed from API logs. These logs describe API exchanges, not final authorization, capture, settlement, or other financial outcomes.

## Key takeaways

- API logs support only requests that use JSON. The page names **Merchant admin** or **Technical integrator** as eligible Customer Area user roles; these are user-access roles, not API credential roles. Its role label is preserved as written, separate from the Developer dashboard guide's **Merchant technical integrator** label.
- In Customer Area, open **Developers > API logs** under a company or merchant account. For APIs used in a balance platform integration, the page places logs on the company account. A log item exposes timestamp, API, PSP reference or resource ID, and request/response details; search by PSP reference or request ID, or filter by date, API, endpoint, or HTTP method.
- Request and response bodies can be inspected during troubleshooting. Because this page describes full details, handle excerpts as potentially sensitive and limit sharing to the intended audience; it does not define redaction guarantees. Its 422 invalid-input example is a debugging example, not a general payment result rule.
- The 30-day API-log window is distinct from the Developer dashboard guide's default seven-day trend view. A missing item outside this page's JSON/retention/account scope cannot by itself establish that an API call or payment never occurred.

## Detail locators

- Raw opening, lines 17–23: purpose, test/live scope, and 30-day removal.
- Raw heading **Using API logs**, lines 25–38: JSON-only support, exact user-role labels, account selection, navigation, fields, and search filters.
- Raw heading **Example**, lines 40–56: checkout debugging walkthrough, error status, request body, response body, and 422 example.
- Raw heading **See also**, lines 58–62: adjacent result-code, error-code, and response-handling routes.

## Related

- [[adyen]] — provider context
- [[adyen-developer-dashboard]] — related Customer Area technical activity and log drilldown
- [[adyen-api-access]] — distinct API credential setup

## Raw Sources

- [[raw/adyen/docs/development-resources/logs-resources/api-logs/2026-09-15|API logs (2026-09-15 snapshot)]]
