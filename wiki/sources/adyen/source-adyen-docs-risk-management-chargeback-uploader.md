---
title: "Adyen Docs: Chargeback Uploader"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/chargeback-uploader"
raw_files:
  - "adyen/docs/risk-management/chargeback-uploader/2026-09-15.md"
tags: [adyen, risk-management, protect, chargebacks, csv]
---

## Overview

This [[adyen]] guide describes uploading chargeback data from an external acquirer into the Adyen payments platform so Protect can use it. **The Chargeback Uploader does not manage disputes**; merchants must dispute those chargebacks with the external acquirer. The 2026-09-15 snapshot covers Customer Area CSV upload, company-level placement, and an irreversible transaction-status update, not defense submission, deletion, or reporting actions. See [[adyen-risk-management]].

## Key takeaways

- The guide requires an online payments integration and the **Upload Chargebacks** Customer Area role, which the merchant asks Adyen Support to enable. After selecting a merchant account, the merchant uses **Risk & disputes → Disputes → Upload**. Chargebacks within one company can be uploaded under one merchant account; separate uploads for each merchant are not necessary. A CSV can contain **at most 1,000 payments**.
- Adyen processes the uploaded CSV request and updates transaction status. **Once updated, that status cannot be reversed or amended.** The guide does not present the upload as submitting a chargeback defense or changing the external acquirer's dispute outcome.
- The CSV table marks `pspreference`, `amount`, and `reason` as required headers. `pspreference` identifies the transaction. The `amount` description says the full transaction value is used by default; a partial chargeback requires an amount in minor units without a decimal point. The `reason` description asks for a scheme-specific code; if left empty, the chargeback is considered non-fraudulent, while the value `fraud` is offered when the code is unknown but fraud should be flagged. These row descriptions do not establish that a required header may be omitted.

## Detail locators

- **Purpose and boundary, raw lines 15–21** — external-acquirer data for Protect and dispute-management exclusion.
- **Requirements, raw lines 23–31** — online integration, enabled uploader role, and 1,000-chargeback CSV limit.
- **Upload sequence, raw lines 33–50** — Support enablement, merchant-account and company scope, Customer Area route, processing, and irreversible status update.
- **Required fields, raw lines 52–60** — marked CSV headers, full versus partial amount in minor units, and reason-code/fraud classification behavior.

## Related

- [[adyen-risk-management]]
- [[source-adyen-docs-risk-management-manage-disputes]]

## Raw Sources

- [[raw/adyen/docs/risk-management/chargeback-uploader/2026-09-15|Adyen Chargeback Uploader guide (2026-09-15 snapshot)]]
