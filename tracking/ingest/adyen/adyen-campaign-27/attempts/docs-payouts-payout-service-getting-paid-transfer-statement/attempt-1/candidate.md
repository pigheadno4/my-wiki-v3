---
title: "Adyen Payout Service transfer statement descriptions"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/getting-paid/transfer-statement"
raw_files:
  - "adyen/docs/payouts/payout-service/getting-paid/transfer-statement/2026-09-15.md"
tags: [adyen, payout-service, payouts, bank-statements, transfer-descriptions]
---

## Overview

This 2026-09-15-captured [[adyen]] **Payout Service** guide explains how a transfer `description` and `referenceForBeneficiary` may appear on a recipient's bank statement within [[adyen-payouts]]. Adyen passes the supplied description to the recipient bank, and says **most** banks show it; visibility, allowed characters and displayed length depend on country, currency and payout priority. This is a statement-text reference, not proof that a particular payout was accepted or credited.

## Key takeaways

- A statement description helps the recipient identify a payout. In some regions, banks combine `description` and `referenceForBeneficiary` in one statement field, so the visible-character limit applies to their combined text. Overlong text is truncated. The illustrative combination of “Payment for service - June 30” and “PaymentFromYourCompanyName” shows possible display, not universal bank formatting. See raw lines 19–30.
- Adyen Support can configure default descriptions, and a transfer request can override the default. The page does not prescribe a universal default value or prove that a requested override was displayed by a specific bank. See raw line 32.
- The tables are organized by Europe, North America and Asia Pacific, then country, currency and payout priority. They list `description` and `referenceForBeneficiary` separately with allowed character sets, **maximum characters accepted** and **characters visible on statements**. Do not substitute the accepted request limit for the bank-visible limit or apply one route's number globally. See raw lines 34–207.
- Material route examples: PLN regular accepts both fields but lists **0** characters visible; PLN wire lists 140. EUR instant lists 0 visible for `referenceForBeneficiary` despite 80 accepted. SGD wire lists 0 visible for both fields. AUD fast lists 280 potentially visible but says Adyen accepts a maximum of 140 for `description` (80 for reference); the displayed capacity is not permission to submit 280 characters. Check the exact currency/priority rows before designing a beneficiary-facing reference. See raw lines 85–90, 105–110, 169–176 and 202–207.
- Allowed character sets vary by route; the matrix is a dated provider snapshot and does not establish that every displayed country/currency/priority combination is enabled for an account. It also does not establish actual bank-statement appearance or beneficiary-bank receipt for a specific payout. See raw lines 34–207.

## Detail locators

- Purpose, combined field and truncation behavior: raw lines 19–30.
- Support default description and per-transfer override: raw line 32.
- Europe currency/priority/character matrix: raw lines 38–138.
- North America matrix: raw lines 139–163.
- Asia Pacific matrix: raw lines 164–207.

## Related

- [[adyen]] — provider profile.
- [[adyen-payouts]] — payout concept; keep Payout Service distinct from legacy Payout API and Marketplace user payouts.
- [[source-adyen-docs-payouts-payout-service-get-started]] — contact-led Payout Service onboarding route.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/getting-paid/transfer-statement/2026-09-15|Payout Service transfer statement descriptions — pinned 2026-09-15 raw snapshot]]
