---
title: "Report webhooks v1 overview | Adyen"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/report-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/report-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, reporting, webhooks, balance-platform]
---

## Overview

This 2026-09-15 captured **Report webhooks v1** overview says [[adyen]] sends notifications when reports have been generated and are ready for download. The catalog lists one incoming `POST balancePlatform.report.created` event, summarized as “Report generated.” The URL segment `latest` is a captured route label; the page heading explicitly identifies v1, and the snapshot does not prove current version or availability. [[adyen-reporting]] [[adyen-webhooks]]

## Key takeaways

- Reports may be downloaded programmatically by HTTP GET or manually in the Balance Platform Customer Area. This overview does not supply the GET URL, authentication, report contents or event payload.
- The listed POST is an incoming report-creation webhook, not a merchant request to generate a report. It signals report readiness as described by this catalog; it does not establish successful download, financial booking, settlement, reconciliation or bank receipt.
- This short overview has no request/response schema or claims about webhook delivery, ordering, retries, deduplication, signatures or finality. Consult the event-specific reference for its payload and acknowledgment contract.

## Detail locators

- API family/version and purpose: raw lines 5–7.
- Download routes: raw line 9.
- Event catalog row: raw lines 11–16.

## Related

- [[adyen]] — provider.
- [[adyen-reporting]] — report and reconciliation context.
- [[adyen-webhooks]] — general webhook context.

## Raw Sources

- [[raw/adyen/api-explorer/report-webhooks/latest/overview/2026-09-15|Captured Report webhooks v1 overview]]
