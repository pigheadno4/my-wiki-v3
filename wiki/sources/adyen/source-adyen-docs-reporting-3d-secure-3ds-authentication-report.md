---
title: "Adyen 3DS Authentication report"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/3d-secure/3ds-authentication-report"
raw_files:
  - "adyen/docs/reporting/3d-secure/3ds-authentication-report/2026-09-15.md"
tags: [adyen, reporting, 3d-secure, authentication]
---

## Overview

This Adyen webpage snapshot describes the **3DS Authentication report** for analysing authentication performance where Adyen attempted 3D Secure authentication or applied an exemption. It excludes transactions with no applicable 3DS and transactions authenticated by a different provider. The report is authentication evidence, not proof that a payment was authorised, captured, settled, or paid out. See [[adyen]], [[adyen-reporting]], and [[adyen-3d-secure]].

## Key takeaways

- The report is available for company and merchant accounts, can be obtained manually or automatically, uses a **CET report time zone**, and lets the user select a Customer Area date range (raw lines 25–31). Availability by account type does not establish a particular user's report permission.
- Each CSV line after the header is a separate transaction entry (raw lines 39–49). The `Creation Date` column is explicitly CET **or CEST** according to the transaction date, with format `YYYY-MM-DD HH:MM:SS` (line 77); preserve this column qualification alongside the page-level CET report statement.
- This report is intended to replace the older **3D Secure Authentication report**, but updated filtering means the two reports' numbers cannot be fully reconciled. Adyen warns automatic or manual report-ingestion logic may need updates (raw lines 21–23). The **3D Secure Conversion report** has different coverage: it starts from all offered card transactions and may include drop-offs, while this authentication report focuses on Adyen's 3DS attempts and exemptions (lines 33–37).
- Read `Authentication Flow` together with `Authentication Success`; the latter records whether **Adyen considers** authentication successful. Requested and applied flows can differ. `Authentication Only` requires additional configuration and the `authenticationOnly` payment-request parameter (raw lines 65–67, 97, 111–127). Authentication success is separate from the `Acquirer Response` authorization column (line 56) and is not payment success.
- The column table includes cardholder name, BIN, shopper email, shopper IP, merchant/shopper references, request metadata, and 3DS transaction identifiers (raw lines 59–60, 71–72, 82, 88–90, 94, 104–109). Handle exports as potentially sensitive transaction/shopper data; the page supplies no specific role or retention policy.

## Detail locators

- `How to use this report`, raw lines 33–37: purpose and comparison with old authentication and conversion reports.
- `Structure / Entries`, raw lines 39–49, and `Columns`, lines 51–109: transaction grain, CSV types, currency/amount, timestamps, authentication/acquirer fields, identifiers, and shopper data. Amount is described in the `Currency Code` column's currency; a separate `Amount (EUR)` column is listed (lines 61–62, 78).
- `Authentication flows and success`, raw lines 111–127: per-flow values, including `No 3DS (exemption)` with no success value and `Rejected` with no authorization attempt.

## Related

- [[adyen-reporting]] — report retrieval and evidence boundaries.
- [[adyen-3d-secure]] — merchant 3DS integration context, separate from report-row evidence.

## Raw Sources

- [[raw/adyen/docs/reporting/3d-secure/3ds-authentication-report/2026-09-15|3DS Authentication report, fetched 2026-09-15]]
