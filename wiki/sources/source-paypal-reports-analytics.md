---
title: "PayPal Reports & Analytics"
type: source
date_ingested: 2026-04-18
original_format: webpage
raw_files:
  - "paypal-reports-analytics-overview-2025.md"
  - "paypal-reports-analytics-how-it-works-2025.md"
  - "paypal-reports-get-started-2025.md"
  - "paypal-reports-dashboard-download-2025.md"
  - "paypal-reports-transaction-api-2025.md"
  - "paypal-reports-automate-2025.md"
  - "paypal-reports-testing-2025.md"
  - "paypal-reports-troubleshooting-2025.md"
tags: [paypal, reporting, analytics, transaction-search, webhooks, business-intelligence]
---

## Summary

Overview of PayPal's Reports & Analytics suite — the landing page for business reporting tools covering both no-code dashboard options and pro-code API integrations.

## Key Takeaways

- **Two tracks**: No-code (Dashboard Downloads, Scheduled Reports via email/SFTP, Basic Analytics) and Pro-code (Transaction Search API, Reporting APIs, Webhook Integration)
- **Output formats**: CSV, PDF, JSON
- **Prerequisites**: active PayPal Business account + developer/API credentials for programmatic access
- **Decision factors**: technical expertise, data volume, automation needs, integration complexity

## Report Types

| Type | Description |
| --- | --- |
| Transaction Reports | Individual payment details |
| Settlement Reports | Batch processing summaries |
| Activity Reports | Comprehensive business activity |
| Balance Reports | Account balance history |

## Integration Options

| Track | Options |
| --- | --- |
| No-code | Dashboard Downloads (manual), Scheduled Reports (email/SFTP), Basic Analytics (built-in charts) |
| Pro-code | Transaction Search API (real-time), Reporting APIs (automated generation/retrieval), Webhooks (event-driven) |

## Related Pages

- [[paypal]] — company page

## Raw Sources

- [[paypal-reports-analytics-overview-2025]] — verbatim Reports & Analytics overview from docs.paypal.ai
- [[paypal-reports-troubleshooting-2025]] — Troubleshooting: 4 error codes (INTERNAL_SERVICE_ERROR/INVALID_REQUEST/INVALID_RESOURCE_ID/RESULTSET_TOO_LARGE); HTTP 401→check token via GET /v1/identity/oauth2/userinfo; HTTP 429→read Retry-After header + exponential backoff; date range max 31 days; health check: GET /v1/reporting/transactions?page_size=1; 30s timeout recommended
- [[paypal-reports-testing-2025]] — Testing guide: sandbox URL `https://api-m.sandbox.paypal.com`; webhook events dashboard via Developer Dashboard → "Webhooks Events" (resend available); 6-item testing checklist
- [[paypal-reports-automate-2025]] — Automate reports: SFTP Transaction Detail Report available by 12:00 PM daily (CSV); schedule types DAILY/WEEKLY/MONTHLY via /v1/reporting/templates/schedule; SFTP delivery_method; webhook trigger pattern (PAYMENT.CAPTURE.COMPLETED); manage schedules via PATCH/DELETE /v1/reporting/schedules/{id}
- [[paypal-reports-transaction-api-2025]] — Transaction Search API: GET /v1/reporting/transactions; 3-hour latency before transactions appear; 3-year history; key params: start_date, end_date, transaction_status, page_size; store transaction IDs for deduplication
- [[paypal-reports-dashboard-download-2025]] — Dashboard download guide: 5-step flow (Reports → Activity Download); CSV or PDF; daily download limits exist; large date ranges slower; historical data availability may be limited
- [[paypal-reports-get-started-2025]] — Get started: 5-step onboarding; 4 report types: Transaction (individual payments), Settlement (batch summaries), Activity (comprehensive), Balance (account history)
- [[paypal-reports-analytics-how-it-works-2025]] — architecture: 4-step data flow; 3 delivery mechanisms (synchronous API / asynchronous scheduled / event-driven webhooks); pull vs push patterns
