---
title: "Adyen Classic Platforms: 2022 verification requirements update"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/verification-process/requirements-update"
raw_files:
  - "adyen/docs/classic-platforms/verification-process/requirements-update/2026-09-15.md"
tags: [adyen, classic-platforms, verification, onboarding]
---

## Overview

This 2022-modified Classic Adyen for Platforms guide, captured 2026-09-15, describes additional sub-merchant verification information enforced for new sub-merchants from **1 August 2022**. Existing sub-merchants may be asked for it during periodic risk review or when account-holder data or processing tier changes. The page directs new implementations to a separate, newer integration guide; its Classic Account API payloads and verification notifications must not be applied to current balance-platform Legal Entity Management resources. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The update distinguishes organization shareholders as **owners** (individuals with at least 25% direct or indirect shares, votes or equity) versus **controllers** (ultimate effective control, or senior management if none is identified). It calls for at least one owner or controller for EEA sub-merchants, at least one controller outside the EEA, and identification of all signatories. It separately says at least one signatory is required, with name, title, residence address, birth date, email and phone; ID details may depend on residence country.
- Other dated inputs include nationality for individual account holders, shareholders and signatories with an address in Hong Kong or Singapore; `principalBusinessAddress` when it differs from the registered address (same country, no PO Box); listed ultimate parent-company data for wholly owned subsidiaries of publicly listed/regulated-market companies; and company TIN for business sub-merchants that processed **more than USD 1,000**. The introduction calls the TIN requirement risk-classification-dependent, while its detailed section gives the monetary trigger; retain both formulations. Gender is no longer required for individuals or shareholders.
- Classic Account API **v5/v6** examples put shareholders and signatories directly under `businessDetails`; **v4 and earlier** wrap them in `ShareholderContact` or `SignatoryContact`. The signatory-nationality examples are labeled signatory but use a `shareholders` array, so those samples cannot settle the correct payload path. The supported stock exchanges spreadsheet and linked API pages remain separate references.
- Signatories undergo verification like shareholders, with `ACCOUNT_HOLDER_VERIFICATION` notification examples for identity and passport states including `AWAITING_DATA`, `DATA_PROVIDED`, and `INVALID_DATA`. Those samples are historical test payloads, not proof that a particular sub-merchant passed verification.
- The action depends on onboarding mode and cohort. For Hosted Onboarding Page (HOP), Adyen requests information from new sub-merchants, while existing ones start verification when Adyen requests it. A custom implementation can use Classic `/getAccountHolder` to inspect existing data, `/updateAccountHolder` when information is requested, or `/createAccountHolder` with complete data up front for new sub-merchants. Submission is distinct from verification approval or any payment/payout outcome.

## Dated creation-guide counterparts

The 2021-modified [[source-adyen-docs-classic-platforms-account-holders-and-accounts|account-holder creation guide]] lists minimum creation inputs, and the 2021-modified [[source-adyen-docs-classic-platforms-quick-start|quick start]] gives basic test payloads, including a sample `gender` field. Read those older examples with this update's cohort rule: its additional requirements apply to **new sub-merchants from 1 August 2022** and may be requested of existing sub-merchants during periodic risk review or when their data or processing tier changes (raw lines 21–27). This update also says `gender` is no longer required for individuals and shareholders (raw lines 434–436). The older minimum fields and samples alone do not establish completion of later verification; this does not make every older creation field or payload invalid.

## Detail locators

- Raw lines 19–27 establish Classic scope, 2022 enforcement, and new/existing cohort conditions; lines 29–45 list updated requirement topics and shareholder definitions.
- Raw lines 47–142 show Classic Account API v5/v6 versus v4-and-earlier shareholder payloads and title examples; lines 144–214 cover signatory identity fields and versioned payloads.
- Raw lines 216–309 cover Hong Kong/Singapore nationality and the signatory/shareholder example-path mismatch; lines 311–395 cover principal address and wholly owned listed-parent information.
- Raw lines 397–436 give the TIN threshold/country table and gender change; lines 438–537 show Classic verification notification examples.
- Raw lines 539–577 distinguish HOP and custom onboarding actions for existing versus new sub-merchants.

## Related

- [[adyen-classic-platforms]] — Classic Platforms concept.
- [[adyen]] — provider context.
- [[adyen-platforms]] — separate current Platforms integration.
- [[adyen-index]] — provider navigation.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/verification-process/requirements-update/2026-09-15|Adyen Classic Platforms verification requirements update, captured 2026-09-15]]
