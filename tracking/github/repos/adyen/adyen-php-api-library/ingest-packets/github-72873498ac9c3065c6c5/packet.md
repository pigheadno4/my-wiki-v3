# GitHub ingest packet

- Repository: `adyen/adyen-php-api-library`
- Work item: `github-72873498ac9c3065c6c5`
- Snapshot: `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/manifest.json`
- Recommended mode: `full`
- Review priority: `high`

## `adyen-php-api-library`

- Version: `30.0.2` -> `30.1.0`
- Recommendation: `full` / `high`
- Unchanged retained files: `441`

### Required reading

- `raw/github/adyen/adyen-php-api-library/releases/adyen-php-api-library/30.1.0/2026-10-29/manifest.json`
- `raw/github/adyen/adyen-php-api-library/releases/adyen-php-api-library/30.1.0/2026-10-29/release-notes.md`
- `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/manifest.json`
- `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/files/README.md`
- `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/files/VERSION`
- `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/files/composer.json`
- `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/files/src/Adyen/Client.php`
- `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/files/src/Adyen/Model/Payments/AdditionalDataCommon.php`
- `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/files/src/Adyen/Model/Payments/ResponseAdditionalDataCommon.php`
- `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/manifest.json`
- `tracking/github/repos/adyen/adyen-php-api-library/comparisons/adyen-php-api-library/30.0.2--30.1.0/comparison.json`
- `tracking/github/repos/adyen/adyen-php-api-library/comparisons/adyen-php-api-library/30.0.2--30.1.0/comparison.md`
- `tracking/github/repos/adyen/adyen-php-api-library/comparisons/adyen-php-api-library/30.0.2--30.1.0/diff.patch`

### Upstream changes

- `modified` `README.md`: `retained-evidence` (snapshot-file)
- `modified` `VERSION`: `retained-evidence` (snapshot-file)
- `modified` `composer.json`: `retained-evidence` (snapshot-file)
- `added` `sdk-generation-log/foreignexchange.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `sdk-generation-log/managementwebhooks.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `sdk-generation-log/payment.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `sdk-generation-log/paymentsapp.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `sdk-generation-log/transactionwebhooks.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `sdk-generation-log/transferwebhooks.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/Adyen/Client.php`: `retained-evidence` (snapshot-file)
- `added` `src/Adyen/Model/ForeignExchange/Amount.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/ForeignExchange/CalculateRateRequest.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/ForeignExchange/CalculateRateRequestItem.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/ForeignExchange/CalculateRateResponse.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/ForeignExchange/CalculateRateResponseItem.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/ForeignExchange/DefaultErrorResponseEntity.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/ForeignExchange/ExchangeSide.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/ForeignExchange/InvalidField.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/ForeignExchange/ModelInterface.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/ForeignExchange/ObjectSerializer.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/ForeignExchange/RateType.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/Adyen/Model/ManagementWebhooks/MidServiceNotificationData.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/Adyen/Model/Payments/AdditionalDataCommon.php`: `retained-evidence` (snapshot-file)
- `modified` `src/Adyen/Model/Payments/ResponseAdditionalDataCommon.php`: `retained-evidence` (snapshot-file)
- `modified` `src/Adyen/Model/PaymentsApp/BoardingTokenRequest.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/Adyen/Model/PaymentsApp/InvalidField.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/PaymentsApp/SubMerchantData.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/Adyen/Model/TransactionWebhooks/IssuedCard.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/Adyen/Model/TransactionWebhooks/TransferViewCategoryData.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/Adyen/Model/TransferWebhooks/IssuedCard.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/Adyen/Model/TransferWebhooks/Modification.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/TransferWebhooks/NetworkReason.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/Adyen/Model/TransferWebhooks/TransferData.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/Adyen/Model/TransferWebhooks/TransferDataCategoryData.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/TransferWebhooks/TransferDataTracing.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/Adyen/Model/TransferWebhooks/TransferEvent.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/TransferWebhooks/TransferEventTracingData.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/TransferWebhooks/UKFpsTracingData.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Model/TransferWebhooks/USAchTracingData.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `src/Adyen/Service/ForeignExchange/RatesApi.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `src/Adyen/Service/PosPayment.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `tests/Resources/ForeignExchange/calculate-rate-error-422.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `tests/Resources/ForeignExchange/calculate-rate-success.json`: `intentional-policy-exclusion` (outside-capsule-policy)
- `added` `tests/Unit/ForeignExchangeTest.php`: `intentional-policy-exclusion` (outside-capsule-policy)
- `modified` `tests/Unit/RegionTest.php`: `intentional-policy-exclusion` (outside-capsule-policy)
