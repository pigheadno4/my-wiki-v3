---
title: "Adyen Disputes API v30 POST /acceptDispute"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Disputes/latest/post/acceptDispute"
raw_files:
  - "adyen/api-explorer/Disputes/latest/post/acceptDispute/2026-09-15.md"
tags: [adyen, disputes, api, chargebacks]
---

## Overview

Captured **Disputes API v30** `POST /acceptDispute` reference on the `ca-test` server. It accepts a specified dispute identified by its **dispute** PSP reference, scoped to a merchant account. In the related [[source-adyen-docs-risk-management-disputes-api]] workflow, accepting is the choice made when the merchant does not defend the dispute. See [[adyen]] and [[adyen-risk-management]].

## Key takeaways

- The request table marks `disputePspReference` and `merchantAccountCode` required properties. `disputePspReference` is the PSP reference **assigned to the dispute**, not the payment PSP reference that may appear in generic error schemas. The page does not separately label the request body as required.
- This is a consequential acceptance action, not defense submission. The related [[source-adyen-docs-risk-management-manage-disputes]] guide says that after acceptance **and expiry of the defense period**, a chargeback's final status becomes `Lost` and its dispute cycle ends. That timing/status detail comes from the separate guide, not this endpoint's response schema.
- A 200 HTTP response contains required `disputeServiceResult`; its nested required `success` boolean reports whether the **request** succeeded, and optional `errorMessage` may explain a general error. The example shows `success: true`. Do not treat HTTP 200 alone as `success: true`, a defense win, an immediate final dispute status, or a payment/settlement result.
- The captured test server is `https://ca-test.adyen.com/ca/services/DisputeService/v30`. `latest` in the canonical URL does not prove the current latest version or live-account eligibility. Error classes shown are 400, 401, 403, 422 and 500; this raw contains no error response examples or detailed propagation timing.

## Detail locators

- Raw lines 5–18: endpoint purpose, v30 test server and two required request properties.
- Raw lines 20–28: acceptance request example.
- Raw lines 29–39 and 106–117: 200 response schema and `success: true` example.
- Raw lines 42–104: error classes and generic error response fields.
- Related guide raw: `risk-management/disputes-api` lines 143–145 describes accepting in place of defending; `risk-management/manage-disputes` lines 52–64 supplies the later Lost-status qualification.

## Related

- [[adyen-risk-management]] — provider risk and disputes concept.
- [[source-adyen-docs-risk-management-disputes-api]] — dispute API workflow and accept/defend choice.
- [[source-adyen-docs-risk-management-manage-disputes]] — related acceptance and final-status guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Disputes/latest/post/acceptDispute/2026-09-15|Captured Disputes API v30 POST /acceptDispute reference]]