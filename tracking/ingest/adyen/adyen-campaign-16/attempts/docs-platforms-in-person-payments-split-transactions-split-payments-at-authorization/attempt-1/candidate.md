---
title: "Adyen Platforms in-person split at authorization"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/split-transactions/split-payments-at-authorization"
raw_files:
  - "adyen/docs/platforms/in-person-payments/split-transactions/split-payments-at-authorization/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, authorization, split-transactions]
---

## Overview

This Adyen for Platforms guide (last modified 2023-03-27; captured 2026-09-15) describes per-transaction split instructions in an in-person Terminal API payment request at authorization, including formatting, account targets and later booking visibility. It is not a standalone-terminal instruction, capture-result guarantee, current role/eligibility determination, or proof of money movement. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Scope and prerequisites:** It assumes the general Platforms in-person requirements and a Terminal API integration with payment terminals or a mobile solution. Standalone mode does not support splits in individual authorization requests; the page mentions automatic split profiles as a separate route. It specifies Split API version 1 inside instructions and Terminal API ProtocolVersion 3.0 in the dated payment example. It does not specify a page-specific user role or partial-capture behavior.
- **Request format and units:** Gather transaction currency, total in minor units and split count, then numbered split items. Send one SaleData.SaleToAcquirerData string, either ampersand-separated key-value pairs or Base64-encoded JSON; AdditionalResponse follows that request format. The split total must equal the sum of specified split amounts and split count must match items. Terminal PaymentTransaction.AmountsReq.RequestedAmount instead uses decimal major units (USD 80.00 rather than 8000), so those numeric fields must not be interchanged.
- **Allocation and fees:** BalanceAccount books sale amount to a named user balanceAccountID; Commission books to the liable balance account without an account field. Tip and Surcharge can be directed at authorization. Split-item amount is omitted for fees, tips and surcharges because unknown then; a BalanceAccount split requires a reference, while a reference for every item is strongly recommended for reconciliation. Including a fee type such as PaymentFee is a recommendation; unspecified transaction fees book to the liable balance account. The USD 80 example allocates USD 75 sale, USD 5 commission and fees to a user account; it is illustrative, not a fee quote.
- **Outcome and fallback:** PaymentResponse.Result Success and the tender/PSP reference identify the payment response, not proof that every split reached its intended account. Terminal API validates split format but not target balance-account existence/status. If an account is nonexistent or linked to a closed holder, the full transaction and fees book to the liable balance account; the page routes balance correction to internal transfers. Track each split through Transfer and Transaction webhooks, distinguishing received, authorised, captured and booked states; test JSON is not a real payout or bank receipt.
- **Later changes and example caution:** The guide says capture-time splits override authorization splits if amounts are decided later, but recommends sending authorization splits because some methods do not support delayed capture. It does not give a general partial-capture rule or explicitly state per-request priority over automatic profiles here. Its fee webhook example names a second user balance account although the authorization request names the first, and commission example IDs/signs vary; do not use those illustrative IDs as authoritative allocation behavior.

## Detail locators

- Per-payment scope, standalone exclusion and four-step process: pinned raw lines 19-51.
- Split API 1 fields, minor-unit totals, conditional item amount/account/reference and fee fallback: pinned raw lines 53-84.
- SaleToAcquirerData encodings and example data: pinned raw lines 85-195.
- Terminal ProtocolVersion 3.0, RequestedAmount decimal units, payment response and AdditionalResponse: pinned raw lines 196-296.
- Split-target validation, liable fallback and per-item webhook tracking: pinned raw lines 298-320; illustrative payment/fee/commission stages: lines 322-1285.
- Other split-type navigation, reference recommendation and capture override/delayed-capture caveat: pinned raw lines 1286-1323.

## Related

- [[adyen-platforms]] — platform split-processing concept and reciprocal source route.
- [[source-adyen-docs-platforms-in-person-payments-split-transactions-split-payments-at-capture]] — separate capture-time split limits and outcome tracking.
- [[source-adyen-docs-platforms-process-payments]] — broader channel and split overview.

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/split-transactions/split-payments-at-authorization/2026-09-15|Adyen Split payments at authorization, captured 2026-09-15]]
