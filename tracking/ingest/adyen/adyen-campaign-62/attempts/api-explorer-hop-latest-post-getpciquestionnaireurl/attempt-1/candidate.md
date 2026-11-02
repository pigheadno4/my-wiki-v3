---
title: "Adyen Classic HOP v6 POST /getPciQuestionnaireUrl"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Hop/latest/post/getPciQuestionnaireUrl"
raw_files:
  - "adyen/api-explorer/Hop/latest/post/getPciQuestionnaireUrl/2026-09-15.md"
tags: [adyen, classic-platforms, hop, pci, questionnaire]
---

## Overview

This 2026-09-15 API Explorer `Hop/latest` page describes Classic HOP POST /getPciQuestionnaireUrl, returning a link that a partner platform can send to its account holder for a PCI compliance questionnaire. It explicitly limits use to a partner platform setup and lists only the `cal-test.adyen.com/cal/services/Hop/v6` server base. The `latest` documentation route and captured Hop v6 service URL should not be treated as a current-version or live-environment guarantee. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- The request body requires `accountHolderCode`, identified as the code supplied when the account holder was created. Optional `returnUrl` redirects the account holder after completing the questionnaire **or** session timeout and has a 500-character maximum. The example values are illustrative.
- The HTTP 200 section says the request succeeded and lists `redirectUrl`, `pspReference`, `resultCode`, and `invalidFields` as optional response-body fields. `redirectUrl` is the questionnaire URL and is explicitly **one-time** and to be used within **30 seconds**. `pspReference` can uniquely identify the request; the response example has `resultCode: Success`, an empty `invalidFields` array and a test HOP URL. The table's optional fields mean the example does not establish every 200 response shape.
- The separately retained Classic partner setup guide, captured the same day, says to redirect within **15 seconds** and describes a 30-minute questionnaire session after redirect. Its 15-second link window conflicts with this API Explorer page's 30-second statement. Keep the limits source-qualified; this page alone does not resolve the operational window or establish questionnaire completion, PCI verification, or compliance.
- The page lists 400 malformed/unreadable request, 401 authentication required, 403 insufficient permissions, 422 validation error and 500 server processing error sections. Their error-body fields are table-optional. The page gives no authentication header scheme; the linked partner guide has a separate API-key example. Neither a successful link request nor the returned reference is a verification decision, payment result, settlement, or bank receipt.

## Detail locators

- Purpose, partner-only prerequisite and test Hop v6 server base: raw lines 5–12. Request body and example: raw lines 14–30.
- HTTP 200 response fields, one-time/30-second `redirectUrl` rule and example: raw lines 31–49 and 115–127. Error sections and response schemas: raw lines 51–113.
- Timing counterpart: [[source-adyen-docs-classic-platforms-platforms-for-partners]], its pinned raw lines 98–121, states a 15-second redirect window, 30-minute session after redirect, and 401 on late redirect or reload.

## Related

- [[adyen]] — provider context.
- [[adyen-classic-platforms]] — older account-holder and partner-platform model.
- [[source-adyen-docs-classic-platforms-platforms-for-partners]] — partner setup, SAQ A and verification flow; its redirect timing conflicts with this API page.

## Raw Sources

- [[raw/adyen/api-explorer/Hop/latest/post/getPciQuestionnaireUrl/2026-09-15|Adyen Hop latest POST /getPciQuestionnaireUrl, captured 2026-09-15]]
