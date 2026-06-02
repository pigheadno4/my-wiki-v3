<!-- Repo: https://github.com/paypal/PayPal-PHP-Server-SDK -->
<!-- Commit SHA: f9aa3096ce4d278e34bbb231c9d89575d2e7467f -->
<!-- Date reviewed: 2026-04-16 -->
<!-- Detail directory: raw/github-paypal-php-server-sdk/ -->
<!-- Files saved (read directly from these paths):
  raw/github-paypal-php-server-sdk/README.md
  raw/github-paypal-php-server-sdk/composer.json
  raw/github-paypal-php-server-sdk/doc/client.md
  raw/github-paypal-php-server-sdk/doc/auth/oauth-2-client-credentials-grant.md
  raw/github-paypal-php-server-sdk/doc/controllers/orders.md
  raw/github-paypal-php-server-sdk/doc/controllers/payments.md
  raw/github-paypal-php-server-sdk/doc/controllers/vault.md
  raw/github-paypal-php-server-sdk/doc/controllers/subscriptions.md
  raw/github-paypal-php-server-sdk/doc/controllers/transaction-search.md
  raw/github-paypal-php-server-sdk/src/PaypalServerSdkClientBuilder.php
  raw/github-paypal-php-server-sdk/src/Environment.php
  raw/github-paypal-php-server-sdk/src/Controllers/OrdersController.php
  raw/github-paypal-php-server-sdk/src/Controllers/PaymentsController.php
  raw/github-paypal-php-server-sdk/src/Controllers/VaultController.php
  raw/github-paypal-php-server-sdk/src/Controllers/SubscriptionsController.php
  raw/github-paypal-php-server-sdk/src/Controllers/TransactionSearchController.php
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from the repo URL at the commit SHA above, then save any newly discovered files into raw/github-paypal-php-server-sdk/ preserving their repo-relative paths -->

# PayPal PHP Server SDK

GitHub: https://github.com/paypal/PayPal-PHP-Server-SDK
Packagist: `paypal/paypal-server-sdk:2.2.0`
Note: Currently covers 5 controllers only — same surface as TypeScript SDK

## What each file covers

| File | What to find there |
| --- | --- |
| `raw/github-paypal-php-server-sdk/README.md` | Setup, client init with builder pattern, retry config, environments, full usage examples |
| `raw/github-paypal-php-server-sdk/composer.json` | Package dependencies |
| `raw/github-paypal-php-server-sdk/doc/client.md` | All client config parameters: retry, backoff, logging, proxy |
| `raw/github-paypal-php-server-sdk/doc/auth/oauth-2-client-credentials-grant.md` | OAuth2 client credentials setup |
| `raw/github-paypal-php-server-sdk/doc/controllers/orders.md` | Orders: 8 methods with PHP signatures and examples |
| `raw/github-paypal-php-server-sdk/doc/controllers/payments.md` | Payments: authorize/reauthorize/void/capture/refund |
| `raw/github-paypal-php-server-sdk/doc/controllers/vault.md` | Vault/Payment Tokens: setup tokens, payment tokens, customer management |
| `raw/github-paypal-php-server-sdk/doc/controllers/subscriptions.md` | Subscriptions: products, plans, full lifecycle |
| `raw/github-paypal-php-server-sdk/doc/controllers/transaction-search.md` | Transaction search |
| `raw/github-paypal-php-server-sdk/src/PaypalServerSdkClientBuilder.php` | Builder pattern client initialization |
| `raw/github-paypal-php-server-sdk/src/Environment.php` | Environment constants (PRODUCTION, SANDBOX) |
| `raw/github-paypal-php-server-sdk/src/Controllers/OrdersController.php` | Orders controller PHP implementation |
| `raw/github-paypal-php-server-sdk/src/Controllers/PaymentsController.php` | Payments controller PHP implementation |
| `raw/github-paypal-php-server-sdk/src/Controllers/VaultController.php` | Vault controller PHP implementation |
| `raw/github-paypal-php-server-sdk/src/Controllers/SubscriptionsController.php` | Subscriptions controller PHP implementation |
| `raw/github-paypal-php-server-sdk/src/Controllers/TransactionSearchController.php` | Transaction search controller PHP implementation |
