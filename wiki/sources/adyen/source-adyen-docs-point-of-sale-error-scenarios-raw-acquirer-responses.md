---
title: "Raw responses | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/error-scenarios/raw-acquirer-responses"
raw_files:
  - "adyen/docs/point-of-sale/error-scenarios/raw-acquirer-responses/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, raw-acquirer-response, refusals]
---

## Overview

This Adyen Docs page explains the optional **raw acquirer response** returned with a declined point-of-sale payment and provides a table of common raw-response examples, Customer Area statuses, and shopper-facing instructions. Card schemes or issuers send raw decline explanations to Adyen; because their strings vary and can change, Adyen maps them to a combination of Terminal API `ErrorCondition`, `refusalReason`, and `message`. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- A merchant can opt in from the **merchant account** in Customer Area under Developers → Additional data → **Raw acquirer result**. After a declined payment, the optional raw value appears as `refusalReasonRaw` in `Response.AdditionalResponse` of `PaymentResponse`. The page explicitly warns **not to base integration code on the raw value** because acquirers and issuers may change it without notice; use the mapped Terminal API response and the linked response-handling guide for behavior.
- The long table is a **most-common-examples lookup**, with Customer Area `Status`, raw response, and a described shopper action. Its raw code is not a universal outcome rule: for example, `00: Approved or completed successfully` appears under **Cancelled** after an initial issuer approval, and `85` appears under **Authorised** for zero-value verification. `91` has distinct **Refused** and **Error** rows. Interpret the full row and transaction context, not a bare code.
- Shopper actions vary by row. Some issuer/account or limit cases say to contact a bank or use another payment method; chip/communication or timeout examples say to retry or use another method. The `94: Duplicate transmission detected` row says to **check that duplicate-decline condition before processing again if needed**. `Offline - Y1 / Y3 / Z1 / Z3` says to inspect transaction logs rather than treating the text as a generic retry order.
- Scheme and context qualifiers are embedded in rows: Bancontact/BCMC PIN or EMV examples, eftpos entry-mode restrictions, suspected fraud, restricted-country card examples, a missing-store-ID merchant setup case, and terminal/card communication failures. These do not establish cross-scheme equivalence, a region-wide merchant eligibility rule, or a universal retry policy. The page contains no merchant-liability rule for raw response codes.
- This 2026-09-15 website capture does not prove that an issuer will return a listed string today, that a merchant has enabled the optional field, or that a payment was authorized, captured, reversed, or settled. The linked refusal-reasons and handling pages are navigation until separately read.

## Detail locators

- `Raw responses`, lines 15–21: issuer/scheme origin, mapped Terminal API `ErrorCondition`/`refusalReason`/`message`, optional raw receipt.
- `Receive raw responses`, lines 23–35: merchant-account Customer Area opt-in, `refusalReasonRaw` placement, warning against code dependence.
- `Most common raw responses`, lines 37–43: table structure and `00` Cancelled example; lines 44–55: issuer referral, `05` variants, `10` partial approval cancelled example.
- Table lines 56–100: transaction/card/limit/refusal rows, **Authorised** `85` zero-value examples at 88–89, **Refused/Error** `91` distinction at 94–95, test-card-on-live `92` example at 96, duplicate `94` check at 98.
- Table lines 101–136: generic/invalid-card/amount rows and Bancontact-specific `182–186` rows at 115–118; card removal and offline-card response examples.
- Table lines 137–175: communication and chip failures, eftpos-specific rows at 143 and 163, missing-store-ID case at 152, terminal/acquirer errors, cancelled and offline-processing examples.
- Table lines 176–198: unsupported method, recurring shopper-reference, cancellations, timeouts and validation rows. Check the exact status, scheme, and row-specific instruction before acting.
- `See also`, lines 200–203: refusal-reason and response-handling links are navigation, not additional evidence in this entry.

## Related

- [[adyen]] — provider page.
- [[adyen-terminal-api]] — Terminal API response and in-person error concept.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/error-scenarios/raw-acquirer-responses/2026-09-15|Raw responses (2026-09-15 snapshot)]]
