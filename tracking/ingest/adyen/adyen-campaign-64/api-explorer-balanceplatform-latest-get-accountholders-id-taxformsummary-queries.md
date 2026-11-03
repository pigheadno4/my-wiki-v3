# Original fixed-query answers: api-explorer-balanceplatform-latest-get-accountholders-id-taxformsummary

## Q1

The 2026-11-02-captured Balance Platform API v2 TEST reference for `GET /accountHolders/{id}/taxFormSummary` returns a summary of tax forms for an account holder. The displayed base is `https://balanceplatform-api-test.adyen.com/bcl/v2`. The required path `id` is the account-holder identifier; required query `formType` accepts `US1099k` or `US1099nec`. A documented `200` body has required `data`, an array of objects with required `legalEntityId` and required integer `taxYears` array. The pinned page states no caller role, defaults or limits. [[source-adyen-api-explorer-balanceplatform-latest-get-accountholders-id-taxformsummary]] [API Explorer](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/accountHolders/(id)/taxFormSummary); raw lines 5–35.

## Q2

A documented `200` succeeds as a summary read, and each listed legal entity/year indicates a tax form for the selected type. The response is not the form or proof of filing, delivery, tax calculation, payment, payout, or bank receipt. The pinned page gives no authentication role, idempotency, lifecycle/deletion/propagation, asynchronous outcome, failure/reversal, or version-conflict rule; its only displayed server is TEST, and the 2026-11-02 snapshot does not establish LIVE availability or account-specific eligibility. The example IDs and years are illustrative. [[source-adyen-api-explorer-balanceplatform-latest-get-accountholders-id-taxformsummary]] [API Explorer](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/accountHolders/(id)/taxFormSummary); raw lines 9–10, 25–60.
