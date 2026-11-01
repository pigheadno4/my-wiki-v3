---
title: "Adyen ACS webhook: Cardholder authentication finalized"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.created"
raw_files:
  - "adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.created/2026-09-15.md"
tags: [adyen, issuing, acs, 3d-secure, webhooks]
---

## Overview

This 2026-09-15-captured ACS webhook `latest` reference describes Adyen's incoming `balancePlatform.authentication.created` notification after cardholder authentication is finalized, whether successful, failed, or expired. Its `data.id` identifies the authentication and `paymentInstrumentId` identifies the card instrument. This is an Issuing-side 3D Secure authentication outcome, separate from payment authorisation, capture, or settlement. The pinned operation does not state a numeric ACS webhook API version. [[adyen-issuing]] [[adyen]]

## Key takeaways

- The required envelope is `data`, `environment` (`test` or `live`), and notification `type`; `timestamp` for queue time is optional. Required `data` fields are `authentication`, authentication `id`, `paymentInstrumentId`, `purchase`, and outcome `status`; `balancePlatform` is optional. Required purchase fields are `date`, `merchantName`, and `originalAmount` object. See [[raw/adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.created/2026-09-15|raw lines 11–41]].
- `authentication` requires distinct ACS, Directory Server, and 3DS Server transaction IDs (`acsTransId`, `dsTransID`, `threeDSServerTransID`), plus `challengeIndicator`, `createdAt`, `deviceChannel`, `inPSD2Scope`, `messageCategory`, `messageVersion`, `transStatus`, and authentication `type` (`frictionless` or `challenge`). `challenge` is optional and returned when authentication `type` is `challenge`; its sample `flow`, `lastInteraction`, phone, resend, and retry fields are not specified in this table. Optional `exemptionIndicator`, `riskScore`, and `transStatusReason` have separate meanings. See [[raw/adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.created/2026-09-15|raw lines 15–30 and 45–168]].
- The `data.status` outcome allows `authenticated`, `rejected`, or `error`; `authentication.transStatus` separately uses 3D Secure values `Y`, `N`, `U`, `I`, or `R` with distinct descriptions. The introduction mentions expiration, but the status table does not list an `expired` literal or map expiration to one of these outcomes. The examples show authenticated challenge, authenticated frictionless, and rejected challenge; they do not define every possible outcome. See [[raw/adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.created/2026-09-15|raw lines 5–7, 28–38 and 43–168]].
- The response section labels HTTP 200 success and says any 2xx HTTP status accepts the webhook, with optional `notificationResponse`. Acceptance acknowledges the notification; it is not an ACS decision response or a later payment result. The separate Issuing OOB Authentication SDK guide describes a relayed authentication request, a two-second response deadline, challenge finalization and this later outcome event; those timing/decision duties are not specified by this outcome-event page. See [[raw/adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.created/2026-09-15|raw lines 169–177]] and [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-authenticate-cardholders|OOB authentication guide]].

## Cross-source warning

The separate [[source-adyen-docs-issuing-3d-secure-troubleshooting|Issuing troubleshooting guide]] broadly says a failed 3D Secure authentication has no webhook, while this event reference explicitly covers failure and gives a rejected example; the OOB guide also says this authentication outcome event is sent regardless of outcome. Keep the troubleshooting statement scoped to its authorisation/Payments-list discussion rather than using it to rule out this authentication-specific event. These snapshots do not establish a later authorisation or transfer event for every attempt.

## Detail locators

- Full field table, including nested requiredness and 3DS status meanings: [[raw/adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.created/2026-09-15|raw lines 9–41]].
- Authenticated challenge and frictionless examples: [[raw/adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.created/2026-09-15|raw lines 43–123]].
- Rejected challenge example with `transStatus: N`: [[raw/adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.created/2026-09-15|raw lines 125–168]].
- Receiver response: [[raw/adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.created/2026-09-15|raw lines 169–177]].

## Related

- [[adyen-issuing]] — Issuing payment-instrument and 3D Secure context.
- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-authenticate-cardholders]] — separately sourced challenge and outcome flow.
- [[source-adyen-docs-issuing-3d-secure-troubleshooting]] — broad no-webhook statement qualified above.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.created/2026-09-15|ACS authentication-created API Explorer reference (captured 2026-09-15)]]
