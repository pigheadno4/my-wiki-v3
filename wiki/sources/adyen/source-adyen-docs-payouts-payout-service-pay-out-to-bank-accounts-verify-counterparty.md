---
title: "Adyen Payout Service counterparty name verification"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts/verify-counterparty"
raw_files:
  - "adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/verify-counterparty/2026-09-15.md"
tags: [adyen, payouts, payout-service, enterprise-accounts, bank-accounts, verification]
---

## Overview

This 2026-09-15 [[adyen]] **enterprise-payouts** guide describes a counterparty **name lookup** before a proposed transfer to a **domestic EU or UK bank account**. The enterprise bank-account holder enters recipient details through a platform interface; the platform calls `POST /verifyCounterpartyName`, presents the result and asks the user whether to continue or cancel. Only after confirmation does the guide route to a separate `POST /transfers` request. A name-check response is not a payout authorization, account capability determination, transfer execution, or bank receipt. [[adyen-payouts]]

## Key takeaways

- The Balance Platform API key needs **CounterpartyNameVerification Webservice Initiate**, with Adyen Support asked to enable the role. The integration type is enterprise payouts. This page does not say the lookup role grants transfer-initiation permission. See raw lines 28–36.
- For a domestic **EU** account the request uses account-holder full name and an IBAN identification; for a domestic **UK** account it uses full name, eight-digit account number, six-digit sort code, `ukLocal` identification and personal/business account type. `reference` and `balanceAccountId` are optional in both tables; Adyen expressly says it **does not verify** the supplied balance-account ID. The examples use the TEST BCL v2 URL, not proof of LIVE enablement. See raw lines 48–60, 81–129.
- Response codes include match, no match, partial match and unsupported cases, with additional UK-only account/type outcomes. Only partial-name-match variants return the registered name; other outcomes withhold it to reduce name guessing. The human-readable `responseDescription` is **not** to drive client logic; branch on `response` and show a relevant warning/choice. See raw lines 62–75 and 191–280.
- The UI guidance includes a **continue with payment** option even for some no-match/unsupported responses, after presenting a warning. A match does not automatically submit a payment, and a non-match is not stated as an API-level transfer prohibition. The enterprise bank-account holder chooses whether to proceed; the later transfer request is separate. See raw lines 72–75 and 221–280.
- **TEST responses are synthetic**: the supplied `reference` selects a named test response, while an unrecognized reference defaults to HTTP 200/`nameMatch`. A test `nameMatch` therefore does not establish a real recipient-name match or a production payout capability. See raw lines 282–294 and 396–410.

## Detail locators

- **Enterprise/EU-UK domestic scope, required role and sequence:** raw lines 19–75.
- **EU and UK request fields and TEST examples:** raw lines 81–189.
- **Response fields, EU/UK variants, name privacy and client logic:** raw lines 191–280.
- **TEST reference-driven fixtures and examples:** raw lines 282–543.
- **Separate bank-payout and webhook next steps:** raw lines 545–553.

## Related

- [[adyen-payouts]]
- [[source-adyen-docs-payouts-payout-service-enterprise-accounts]]
- [Bank payout request](https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts/bank-payout-request)

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/verify-counterparty/2026-09-15|Adyen counterparty name verification — collected 2026-09-15]]
