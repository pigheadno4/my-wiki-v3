---
title: "Verify counterparty name | Adyen Business Accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/send-funds/verify-counterparty"
raw_files:
  - "adyen/docs/business-accounts/send-funds/verify-counterparty/2026-09-15.md"
tags: [adyen, business-accounts, counterparty-verification, bank-transfers, eu, uk]
---

## Overview

This 2026-09-15 [[adyen]] Business Accounts guide describes checking the name supplied for an intended recipient's domestic EU or UK third-party bank account before an outgoing transfer. The platform calls `POST /verifyCounterpartyName`, presents the result to the business account holder, and, only if the user confirms continuation, separately requests a transfer through `POST /transfers`. The lookup is neither a transfer nor proof of funds received by the destination bank. See [[adyen-business-accounts]].

## Key takeaways

- The guide requires a Balance Platform API key with **CounterpartyNameVerification Webservice Initiate**; it directs the platform to contact Adyen Support to enable the role. The described integration is Business Accounts. These setup statements do not establish a particular platform's current access or a successful request.
- For the EU domestic check, the request supplies the proposed full account-holder name and an `iban` account identification. For the UK domestic check, it supplies the name, eight-digit account number, six-digit sort code and `personal` or `business` account type with `ukLocal` identification. The documented `balanceAccountId` and `reference` are optional in these tables; Adyen says it does not verify `balanceAccountId`. See the raw field tables for formatting and examples.
- The response classifies the check, including a match, no match, partial match or unavailable check. The UK has additional account-not-found, switched, opted-out and account-type mismatch cases. The actual registered name is returned only for a partial-name-match result, including the UK business/personal partial variants. A `nameMatch` does not return the account name. Use `counterpartyVerification.response` for client decisions; Adyen warns not to use the human-readable `responseDescription` for logic.
- The interface guidance presents user choices after the response, including warnings and cancel/edit/continue options for mismatch or unavailable-check cases. Confirmation precedes any separate transfer request. A name-check result is not an instruction to transfer, a guarantee that the destination accepts funds, or settlement evidence.
- In Adyen's **test environment**, the `reference` value selects a simulated `response`; an unrecognized reference defaults to HTTP 200 and `nameMatch`. Partial-match test responses append `y` to the name. These fixtures can test client messaging but cannot demonstrate a real bank's name check.

## Detail locators

- Service scope, requirements and two-step user/transfer flow: pinned raw lines 15–76.
- EU and UK request fields and test endpoint examples: raw lines 77–158.
- Response examples, response fields and regional result values: raw lines 160–219. The prose at line 70 names a generic partial match; the response table at line 202 also lists UK-only partial business/personal variants.
- Suggested user messaging and options, including mismatch, unsupported and account-type cases: raw lines 221–280.
- Simulated test response selection and example payloads: raw lines 282–543. The examples have inconsistencies between supplied names and forced outcomes, and the final `nameMatchPersonal` example's response `reference` differs from its request; treat them as test illustrations, not measured bank results.

## Related

- [[adyen-business-accounts]] — product and account context.
- [[source-adyen-docs-business-accounts-verify-account-holder]] — separate Open Banking/AISP route for an unregistered external individual's account ownership, with a different actor and flow.

## Raw Sources

- [[raw/adyen/docs/business-accounts/send-funds/verify-counterparty/2026-09-15|Adyen Docs: Verify counterparty name (2026-09-15 snapshot)]]
