---
title: "Stripe Decline Codes"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/declines/codes"
raw_files:
  - "stripe-declines-codes-2026-11-07.md"
  - "stripe-decline-codes-2026.md"
tags: [stripe, declines, decline-codes, card-declines, lpm, radar, authentication-required, fraud]
---

## Overview

This is Stripe's decline-code reference for card and local payment method (LPM) failures, captured on May 9 and November 7, 2026. A Stripe decline code gives a more specific reason than an issuer decline code; an error may separately include an `advice_code` with suggested next steps. The API error `code` field is a separate error reference. Do not equate a Stripe decline code, an issuer or network code, a charge outcome reason, and optional advice.

The November card table has **50 rows**. Its LPM table has **29 rows but 27 distinct decline-code names**: three Klarna outcomes share `klarna_payment_declined`. The May LPM table had **19 rows and 19 distinct names**. Table presence does not establish that a given provider or account will emit a listed code.

## Card decline codes

- **Authentication:** `authentication_required` means authentication such as 3DS is needed. With Stripe front ends, an issuer soft decline usually triggers the authentication flow; an off-session payment may need the customer to retry on-session. If this code still comes from the issuer after successful authentication, the customer must contact the issuer. For `authentication_not_handled`, run 3DS/SCA; prepare off-session authentication on-session and fall back to on-session when needed. These are two different conditions.
- **Customer-correctable data:** `incorrect_cvc`/`invalid_cvc`, `incorrect_number`/`invalid_number`, `incorrect_zip`, `incorrect_address`, `incorrect_pin`/`invalid_pin`, and invalid expiry month/year call for corrected details. `expired_card` needs another card. `incorrect_pin` applies only to card-reader payments. For `offline_pin_required`, insert the card and enter a PIN; `online_or_offline_pin_required` permits prompting for Online PIN without a new transaction only if the reader supports it, otherwise insert and retry. `pin_try_exceeded` calls for another card or payment method, while `mobile_device_authentication_required` calls for another mobile-device tap.
- **Issuer or eligibility response:** `call_issuer`, `do_not_honor`, `no_action_taken`, `not_permitted`, and `transaction_not_allowed` direct the customer to the issuer. `card_not_supported` and `currency_not_supported` have card-type or currency-specific issuer checks. `insufficient_funds` and `withdrawal_count_limit_exceeded` call for an alternative payment method. `invalid_amount` calls for an issuer check **if** the amount appears correct.
- **Check before retrying:** `duplicate_transaction` calls for checking whether a recent payment already exists. `issuer_not_available`, `approve_with_id`, and `reenter_transaction` call for another attempt, then issuer contact if still unprocessed. In the **November** card table, `processing_error` likewise says retry and then contact the issuer if still unprocessed; the **May** card row instead said to try again later after a failed retry. Use the dated November guidance for that changed row, not an undated blanket retry rule.
- **Mask the specific reason:** For card `fraudulent`, `lost_card`, `stolen_card`, and `merchant_blacklist`, present the decline to the customer in the same manner as `generic_decline`. This is card-table guidance; the LPM `lost_or_stolen_card` row instead uses `partner_generic_decline`.
- **Other labels:** `testmode_decline` says a Stripe test card number was used and a genuine card is needed; neither capture says it necessarily occurred in live mode. Both tables mark card decline-code names `do_not_try_again` and `try_again_later` as deprecated. This page does not say those exact names migrated to `advice_code`.

The full 50-row card table and each code's exact next step are at November raw lines 19–70; the May comparison is at old raw lines 18–69. Codes appearing in both card and LPM tables can have different descriptions, outcome reasons, and recommended actions.

## Local payment method decline codes

The LPM table has four distinct columns: **decline code**, **charge outcome reason**, **seller message**, and **API error message** (November lines 76–106). Do not read a value in one column as a value in another.

- **Klarna:** All three rows use decline code `klarna_payment_declined`; the outcome reasons distinguish `klarna_payment_declined` (payment declined), `klarna_payment_canceled` (customer canceled checkout), and `klarna_session_expired` (checkout expired). Each row has its own seller and API wording.
- **Customer and BLIK:** `customer_declined` has outcome `generic_decline` for a customer-declined payment. BLIK `code_invalid` and `code_expired` also have `generic_decline` outcomes, but different seller/API messages. The `code_expired` API message says BLIK codes expire after two minutes and asks for another code; the row also covers an already-used code or exceeded lifetime.
- **New partner/card-data rows:** `partner_action_not_supported` and `card_already_activated` explicitly say retries will not succeed. The LPM `lost_or_stolen_card` row says not to disclose the specific reason to the customer and to present `partner_generic_decline`. `invalid_track_data` directs the customer to the card issuer. These instructions apply to their named LPM rows only.
- **Existing conditional outcomes:** `invalid_customer_account` and `payment_limit_exceeded` may succeed after the customer resolves the account issue; `expired_card` and `insufficient_funds` likewise depend on customer action. `invalid_business_account` may be retried **if** the business account is reactivated; `payment_disputed` may be retried **if** the dispute resolves for the business; `expired_payment_information` may be retried after the customer updates the information. `recurring_not_supported_by_bank` directs selection of a bank that supports recurring payments.
- **Explicit non-retry rows:** The LPM API messages for `invalid_billing_agreement`, `currency_not_supported`, `invalid_amount`, `compliance_violation`, `invalid_authorization`, and `invalid_payment_information` say retries will not succeed. The LPM `processing_error`, `partner_high_risk_customer`, `partner_payment_not_found`, and `duplicate_transaction` rows give their own descriptions without the card `processing_error` retry/issuer instruction. Consult the exact row before deciding on a retry.

The eight decline-code names added to the November LPM table are `klarna_payment_declined`, `customer_declined`, `code_invalid`, `code_expired`, `partner_action_not_supported`, `lost_or_stolen_card`, `card_already_activated`, and `invalid_track_data`. No May LPM decline-code name was removed.

## Detail locators

- Card authentication, masking, processing, and deprecated rows: November raw lines 21–22, 32, 48–49, 57, 64, 68; May raw lines 20–21, 28, 31, 47–48, 56, 63, 67.
- Full LPM table with all four field columns and row-specific messages: November raw lines 76–106; May raw lines 75–95.
- Klarna outcome mapping: November raw lines 78–80. BLIK messages: lines 83–84. New partner/card-data handling: lines 103–106.
- For broader card retry policy, see [[source-stripe-card-declines]]. For issuer and network mappings, see [[source-stripe-network-decline-codes]].

## Related

- [[stripe-declines]] — decline types, outcome fields, retry context, and source routes.
- [[source-stripe-declines-overview]] — issuer declines, Stripe blocks, and invalid calls.

## Raw Sources

- [[raw/stripe-declines-codes-2026-11-07|November 7, 2026 decline-code reference]]
- [[raw/stripe-decline-codes-2026|May 9, 2026 decline-code reference]]
