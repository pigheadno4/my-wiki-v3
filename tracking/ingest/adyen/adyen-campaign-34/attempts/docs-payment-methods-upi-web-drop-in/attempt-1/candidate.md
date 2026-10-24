---
title: "Adyen UPI Web Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/upi/web-drop-in/2026-09-15.md"
tags: [adyen, upi, web, drop-in, online-payments]
---

## Overview

This 2026-09-15 Adyen guide describes adding **UPI** to an existing **Web Drop-in** integration, with separate Sessions and Advanced server-side paths. It covers UPI Intent/QR simulator testing, and an Advanced Intent `appId` payment field. It does **not** describe UPI Collect or a Collect migration date; use the separate [[source-adyen-docs-payment-methods-upi-api-only]] for that history rather than applying it to this Drop-in page. The snapshot does not establish current method eligibility or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The page requires existing Sessions Web Drop-in, **Checkout API v68 or later**, and UPI added in Customer Area. It says no UPI-specific extra `/sessions` fields or configuration. Optional individual-method tree-shaking prose says include `UPI`, while its JavaScript import spells the symbol **`Upi`**; do not assume those spellings are interchangeable code. (raw lines 23–57)
- **Advanced:** It requires existing Advanced Web Drop-in, handling an additional action labelled **`action.type: await`**, and UPI in Customer Area. It says no extra UPI configuration, but the `/payments` table conditionally requires **`paymentMethod.appId` for UPI Intent** (`paymentMethod.type: upi_intent`) to identify the shopper's third-party app. The TEST v72 INR/IN `gpay` request is an example, not a blanket API-version or app eligibility rule. No separate Advanced Checkout API minimum appears. (raw lines 83–143)
- **Advanced guide link defect:** The Advanced Integration type link embeds an unresolved encoded `getParameter('platform')` template in the platform query value; neighboring action-handling and import links use `platform=Web`. Retain the Advanced Web Drop-in prose requirement but do not silently treat that templated URL as resolved. (raw lines 91–99)
- **TEST simulator and outcome:** In both sections, Adyen says UPI can be tested in its Payment Simulator. The stated TEST path redirects UPI Intent to the hosted simulator page; **UPI QR on web** is scanned to reach that page. The page asks testers to choose an outcome, verify integration handling, accept a webhook with the source-spelled `eventCode: AUTHORISED`, and inspect Customer Area. These are test instructions, not observed results, current LIVE availability, or a final production payment. The Advanced action table says `await` while the simulator paragraph says Intent redirects; preserve those contexts instead of turning either into a universal action claim. The sibling API-only guide's AUTHORISATION webhook table differs from this checklist's AUTHORISED spelling; verify webhook semantics with the actual integration authority. (raw lines 59–81, 87–93, 145–167)
- **Scope limit:** Method-specific 'no extra configuration' and Sessions 'no extra parameters' statements do not waive the underlying Web Drop-in integration. This page does not give a live go-live prerequisite, Collect migration/eligibility rule, or authorization/capture/settlement/refund result. Its modification-test link is a recommendation. (raw lines 19–167)

## Detail locators

- Sessions version/setup, request fields, optional import and no-extra-configuration wording: raw lines 23–57.
- Sessions Intent/QR simulator route, outcome/webhook/Customer Area checks: raw lines 59–81.
- Advanced prerequisites, templated integration URL, `await` action and `appId` condition: raw lines 83–121.
- Advanced TEST v72 sample and repeated simulator checklist: raw lines 123–167.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-upi-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/web-drop-in/2026-09-15|Adyen UPI Web Drop-in guide, 2026-09-15 snapshot]]
