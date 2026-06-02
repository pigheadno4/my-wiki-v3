<!-- Source URL: https://docs.paypal.ai/growth/payouts/test-and-go-live/test-values -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Payouts API - test values

You can use predefined test values to simulate a variety of positive and negative API responses.

<Note>Test values are case-sensitive.</Note>

## Create payout batch

Use the test values in the request payload to simulate both positive and negative responses.

**Endpoint**: `POST v1/payments/payouts/`

**Positive response test values**

| Trigger        | Test value | Simulated response                         |
| -------------- | ---------- | ------------------------------------------ |
| items\[0]/note | POSPYO001  | PAYLOAD WITH `201` RESPONSE CODE           |
| items\[0]/note | POSPYO003  | PAYLOAD WITH `201` RESPONSE CODE FOR VENMO |

**Negative response test values**

| Trigger                   | Test value | Simulated error response                  |
| ------------------------- | ---------- | ----------------------------------------- |
| items\[0]/note            | ERRPYO001  | `SENDER_RESTRICTED`                       |
| items\[0]/note            | ERRPYO002  | `SENDER_EMAIL_UNCONFIRMED`                |
| items\[0]/note            | ERRPYO003  | `AUTHORIZATION_ERROR`                     |
| items\[0]/note            | ERRPYO005  | `INSUFFICIENT_FUNDS`                      |
| items\[0]/note            | ERRPYO006  | `INTERNAL_ERROR`                          |
| items\[0]/note            | ERRPYO010  | `VALIDATION_ERROR`                        |
| items\[0]/note            | ERRPYO011  | `REQUIRED_SCOPE_MISSING`                  |
| items\[0]/note            | ERRPYO012  | `SENDER_LOCKED`                           |
| items\[0]/sender_batch_id | ERRPYO013  | `VALIDATION_ERROR FOR VENMO NOTE MISSING` |
| items\[0]/note            | ERRPYO014  | `USER_BUSINESS_ERROR`                     |
| items\[0]/note            | ERRPYO035  | `RATE_LIMIT_VALIDATION`                   |
| items\[0]/note            | ERRPYO036  | `REQUEST_TIMEOUT_EXCEEDED`                |
| items\[0]/note            | ERRPYO037  | `SYNC_MODE_NOT_APPLICABLE`                |
| items\[0]/note            | ERRPYO038  | `NON_HOLDING_CURRENCY`                    |
| items\[0]/note            | ERRPYO039  | `PREVIOUS_REQUEST_IN_PROGRESS`            |
| items\[0]/note            | ERRPYO040  | `CIP_NOT_VERIFIED`                        |

## Track status

Use the test values as path parameters in the request URL to simulate both positive and negative responses.

**Endpoint**: `GET v1/payments/payouts/{id}`

**Positive response test values**

| Path parameter                  | Simulated response |
| ------------------------------- | ------------------ |
| /v1/payments/payouts/ERRPYOB001 | `SUCCESS`          |
| /v1/payments/payouts/ERRPYOB002 | `PENDING`          |
| /v1/payments/payouts/ERRPYOB003 | `PROCESSING`       |

**Negative response test values**

| Path parameter                  | Simulated response |
| ------------------------------- | ------------------ |
| /v1/payments/payouts/ERRPYOB004 | `DENIED`           |

## Show payout details

Use the test values as path parameters in the request URL to simulate both positive and negative responses.

**Endpoint**: `GET v1/payments/payouts/{id}`

**Positive response test values**

| Path parameter                 | Simulated response               |
| ------------------------------ | -------------------------------- |
| /v1/payments/payouts/POSPYO002 | PAYLOAD WITH `200` RESPONSE CODE |

**Negative response test values**

| Path parameter                  | Simulated error response                                    |
| ------------------------------- | ----------------------------------------------------------- |
| /v1/payments/payouts/ERRPYOB005 | `ACCOUNT_RESTRICTED`                                        |
| /v1/payments/payouts/ERRPYOB006 | `ACCOUNT_UNCONFIRMED_EMAIL`                                 |
| /v1/payments/payouts/ERRPYOB007 | `APPROVER_DENIED`                                           |
| /v1/payments/payouts/ERRPYOB008 | `GAMER_FAILED_COUNTRY_OF_RESIDENCE_CHECK`                   |
| /v1/payments/payouts/ERRPYOB009 | `GAMER_FAILED_FUNDING_SOURCE_CHECK`                         |
| /v1/payments/payouts/ERRPYOB010 | `GAMING_INVALID_PAYMENT_FLOW`                               |
| /v1/payments/payouts/ERRPYOB011 | `NON_HOLDING_CURRENCY`                                      |
| /v1/payments/payouts/ERRPYOB012 | `PENDING_RECIPIENT_NON_HOLDING_CURRENCY_PAYMENT_PREFERENCE` |
| /v1/payments/payouts/ERRPYOB013 | `SENDER_STATE_RESTRICTED`                                   |
| /v1/payments/payouts/ERRPYOB014 | `SPENDING_LIMIT_EXCEEDED`                                   |
| /v1/payments/payouts/ERRPYOB015 | `TRANSACTION_DECLINED_BY_TRAVEL_RULE`                       |
| /v1/payments/payouts/ERRPYO015  | `CLOSED_MARKET`                                             |
| /v1/payments/payouts/ERRPYO016  | `CURRENCY_COMPLIANCE`                                       |
| /v1/payments/payouts/ERRPYO017  | `CURRENCY_NOT_SUPPORTED_FOR_RECEIVER`                       |
| /v1/payments/payouts/ERRPYO018  | `DUPLICATE_ITEM`                                            |
| /v1/payments/payouts/ERRPYO019  | `RECEIVER_ACCOUNT_LOCKED`                                   |
| /v1/payments/payouts/ERRPYO020  | `RECEIVER_COUNTRY_NOT_ALLOWED`                              |
| /v1/payments/payouts/ERRPYO021  | `RECEIVER_UNCONFIRMED`                                      |
| /v1/payments/payouts/ERRPYO022  | `RECEIVER_UNREGISTERED`                                     |
| /v1/payments/payouts/ERRPYO023  | `RECEIVER_YOUTH_ACCOUNT`                                    |
| /v1/payments/payouts/ERRPYO024  | `RECEIVING_LIMIT_EXCEEDED`                                  |
| /v1/payments/payouts/ERRPYO025  | `REGULATORY_BLOCKED`                                        |
| /v1/payments/payouts/ERRPYO026  | `REGULATORY_PENDING`                                        |
| /v1/payments/payouts/ERRPYO027  | `RISK_DECLINE`                                              |
| /v1/payments/payouts/ERRPYO028  | `SELF_PAY_NOT_ALLOWED`                                      |
| /v1/payments/payouts/ERRPYO029  | `TRANSACTION_LIMIT_EXCEEDED`                                |
| /v1/payments/payouts/ERRPYO030  | `UNDEFINED`                                                 |
| /v1/payments/payouts/ERRPYO031  | `ZERO_AMOUNT`                                               |
| /v1/payments/payouts/ERRPYO032  | `INVALID_RESOURCE_ID`                                       |
| /v1/payments/payouts/ERRPYO033  | `INTERNAL_ERROR`                                            |
| /v1/payments/payouts/ERRPYO034  | `INVALID_EMAIL`                                             |
| /v1/payments/payouts/ERRPYO060  | `RECEIVER_ACCOUNT_LIMITATION`                               |

## Cancel payout item

Use the test values as path parameters in the request URL to simulate both positive and negative responses.

**Endpoint**: `POST v1/payments/payouts-item/payouts_item_id/cancel`

**Positive response test values**

| Path parameter                             | Simulated response               |
| ------------------------------------------ | -------------------------------- |
| /v1/payments/payouts-item/POSPOI002/cancel | PAYLOAD WITH `200` RESPONSE CODE |

**Negative response test values**

| Path parameter                             | Simulated error response   |
| ------------------------------------------ | -------------------------- |
| /v1/payments/payouts-item/ERRPOI001/cancel | `INVALID_RESOURCE_ID`      |
| /v1/payments/payouts-item/ERRPYO004/cancel | `BATCH_NOT_COMPLETED`      |
| /v1/payments/payouts-item/ERRPYO007/cancel | `ITEM_ALREADY_CANCELLED`   |
| /v1/payments/payouts-item/ERRPYO008/cancel | `ITEM_CANCELLATION_FAILED` |
| /v1/payments/payouts-item/ERRPYO009/cancel | `ITEM_INCORRECT_STATUS`    |

## Show payout item details

Use the test values as path parameters in the request URL to simulate both positive and negative responses.

**Endpoint**: `GET v1/payments/payouts-item/{item-id}`

**Positive response test values**

| Path parameter                      | Simulated response          |
| ----------------------------------- | --------------------------- |
| /v1/payments/payouts-item/POSPOI001 | PAYLOAD WITH `200` RESPONSE |

**Negative response test values**

| Path parameter                        | Simulated error response                                    |
| ------------------------------------- | ----------------------------------------------------------- |
| /v1/payments/payouts-item/ERRPYO041   | `CLOSED_MARKET`                                             |
| /v1/payments/payouts-item/ERRPYO042   | `CURRENCY_COMPLIANCE`                                       |
| /v1/payments/payouts-item/ERRPYO043   | `CURRENCY_NOT_SUPPORTED_FOR_RECEIVER`                       |
| /v1/payments/payouts-item/ERRPYO044   | `RECEIVER_ACCOUNT_LOCKED`                                   |
| /v1/payments/payouts-item/ERRPYO045   | `RECEIVER_COUNTRY_NOT_ALLOWED`                              |
| /v1/payments/payouts-item/ERRPYO046   | `RECEIVER_UNCONFIRMED`                                      |
| /v1/payments/payouts-item/ERRPYO047   | `RECEIVER_UNREGISTERED`                                     |
| /v1/payments/payouts-item/ERRPYO048   | `RECEIVER_YOUTH_ACCOUNT`                                    |
| /v1/payments/payouts-item/ERRPYO049   | `RECEIVING_LIMIT_EXCEEDED`                                  |
| /v1/payments/payouts-item/ERRPYO050   | `REGULATORY_BLOCKED`                                        |
| /v1/payments/payouts-item/ERRPYO051   | `REGULATORY_PENDING`                                        |
| /v1/payments/payouts-item/ERRPYO052   | `RISK_DECLINE`                                              |
| /v1/payments/payouts-item/ERRPYO053   | `SELF_PAY_NOT_ALLOWED`                                      |
| /v1/payments/payouts-item/ERRPYO054   | `TRANSACTION_LIMIT_EXCEEDED`                                |
| /v1/payments/payouts-item/ERRPYO055   | `UNDEFINED`                                                 |
| /v1/payments/payouts-item/ERRPYO056   | `ZERO_AMOUNT`                                               |
| /v1/payments/payouts-item/ERRPYO057   | `INVALID_RESOURCE_ID`                                       |
| /v1/payments/payouts-item/ERRPYO058   | `INTERNAL_ERROR`                                            |
| /v1/payments/payouts-item/ERRPYO059   | `INVALID_EMAIL`                                             |
| /v1/payments/payouts-item/ERRPYO061   | `RECEIVER_ACCOUNT_LIMITATION`                               |
| /v1/payments/payouts-items/ERRPYOB016 | `ACCOUNT_RESTRICTED`                                        |
| /v1/payments/payouts-items/ERRPYOB017 | `ACCOUNT_UNCONFIRMED_EMAIL`                                 |
| /v1/payments/payouts-items/ERRPYOB018 | `APPROVER_DENIED`                                           |
| /v1/payments/payouts-items/ERRPYOB019 | `GAMER_FAILED_COUNTRY_OF_RESIDENCE_CHECK`                   |
| /v1/payments/payouts-items/ERRPYOB020 | `GAMER_FAILED_FUNDING_SOURCE_CHECK`                         |
| /v1/payments/payouts-items/ERRPYOB021 | `GAMING_INVALID_PAYMENT_FLOW`                               |
| /v1/payments/payouts-items/ERRPYOB022 | `NON_HOLDING_CURRENCY`                                      |
| /v1/payments/payouts-items/ERRPYOB023 | `PENDING_RECIPIENT_NON_HOLDING_CURRENCY_PAYMENT_PREFERENCE` |
| /v1/payments/payouts-items/ERRPYOB024 | `SENDER_STATE_RESTRICTED`                                   |
| /v1/payments/payouts-items/ERRPYOB025 | `SPENDING_LIMIT_EXCEEDED`                                   |
| /v1/payments/payouts-items/ERRPYOB026 | `TRANSACTION_DECLINED_BY_TRAVEL_RULE`                       |
