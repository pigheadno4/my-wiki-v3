<!-- Repo: https://github.com/paypal/Payouts-PHP-SDK -->
<!-- Commit SHA: 3c102e0cc1e85480f3466e49d01069919e6237bb -->
<!-- Date reviewed: 2026-04-16 -->
<!-- Detail directory: raw/github-paypal-payouts-php-sdk/ -->
<!-- Files saved (read directly from these paths):
  raw/github-paypal-payouts-php-sdk/README.md
  raw/github-paypal-payouts-php-sdk/composer.json
  raw/github-paypal-payouts-php-sdk/samples/PayPalClient.php
  raw/github-paypal-payouts-php-sdk/samples/CreatePayoutSample.php
  raw/github-paypal-payouts-php-sdk/samples/GetPayoutSample.php
  raw/github-paypal-payouts-php-sdk/samples/ItemGetSample.php
  raw/github-paypal-payouts-php-sdk/samples/ItemCancelSample.php
  raw/github-paypal-payouts-php-sdk/lib/PaypalPayoutsSDK/Payouts/PayoutsPostRequest.php
  raw/github-paypal-payouts-php-sdk/lib/PaypalPayoutsSDK/Payouts/PayoutsGetRequest.php
  raw/github-paypal-payouts-php-sdk/lib/PaypalPayoutsSDK/Payouts/PayoutsItemGetRequest.php
  raw/github-paypal-payouts-php-sdk/lib/PaypalPayoutsSDK/Payouts/PayoutsItemCancelRequest.php
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from the repo URL at the commit SHA above, then save any newly discovered files into raw/github-paypal-payouts-php-sdk/ preserving their repo-relative paths -->

# PayPal Payouts PHP SDK

GitHub: https://github.com/paypal/Payouts-PHP-SDK
Composer: `paypal/paypal-payouts-sdk ~1.0.0`
Requires: PHP 5.6+, TLS 1.2

## What each file covers

| File | What to find there |
| --- | --- |
| `raw/github-paypal-payouts-php-sdk/README.md` | Setup, credentials, usage examples, test instructions |
| `raw/github-paypal-payouts-php-sdk/composer.json` | Package dependencies and autoload config |
| `raw/github-paypal-payouts-php-sdk/samples/PayPalClient.php` | Client instantiation with SandboxEnvironment/ProductionEnvironment |
| `raw/github-paypal-payouts-php-sdk/samples/CreatePayoutSample.php` | End-to-end create payout (PayoutsPostRequest) with response parsing |
| `raw/github-paypal-payouts-php-sdk/samples/GetPayoutSample.php` | Retrieve payout batch by batch ID (PayoutsGetRequest) |
| `raw/github-paypal-payouts-php-sdk/samples/ItemGetSample.php` | Get individual payout item details (PayoutsItemGetRequest) |
| `raw/github-paypal-payouts-php-sdk/samples/ItemCancelSample.php` | Cancel an unclaimed payout item (PayoutsItemCancelRequest) |
| `raw/github-paypal-payouts-php-sdk/lib/PaypalPayoutsSDK/Payouts/PayoutsPostRequest.php` | POST /v1/payments/payouts — request class definition |
| `raw/github-paypal-payouts-php-sdk/lib/PaypalPayoutsSDK/Payouts/PayoutsGetRequest.php` | GET /v1/payments/payouts/{batch_id} — request class definition |
| `raw/github-paypal-payouts-php-sdk/lib/PaypalPayoutsSDK/Payouts/PayoutsItemGetRequest.php` | GET /v1/payments/payouts-item/{item_id} — request class definition |
| `raw/github-paypal-payouts-php-sdk/lib/PaypalPayoutsSDK/Payouts/PayoutsItemCancelRequest.php` | POST /v1/payments/payouts-item/{item_id}/cancel — request class definition |
