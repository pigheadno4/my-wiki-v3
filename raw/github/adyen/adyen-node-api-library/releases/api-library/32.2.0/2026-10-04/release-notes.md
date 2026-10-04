## What's Changed

This range adds sub-merchant details to Payments App boarding-token requests and makes the Node HTTPS client reuse its agent across requests, with optional keep-alive configuration.

## New Features 💎

### Payments App API

- Add `SubMerchantData` to `BoardingTokenRequest.subMerchantData`, allowing boarding-token requests to carry sub-merchant identity, contact, and address details. ([#1783](https://github.com/Adyen/adyen-node-api-library/pull/1783))

## Fixes ⛑️

### Other

- Reuse the HTTPS agent in `HttpURLConnectionClient` across requests, accept optional `AgentOptions` such as `keepAlive`, preserve the agent on HTTPS 308 redirects, and rebuild it when certificate settings change. ([#1784](https://github.com/Adyen/adyen-node-api-library/pull/1784))

## PRs 📋️

- [paymentsapp] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1783](https://github.com/Adyen/adyen-node-api-library/pull/1783)
- fix: reuse HTTPS agent across requests by [@naseemkullah](https://github.com/naseemkullah) in [#1784](https://github.com/Adyen/adyen-node-api-library/pull/1784)

## Contributors

- [@AdyenAutomationBot](https://github.com/AdyenAutomationBot)
- [@naseemkullah](https://github.com/naseemkullah)

**Full Changelog**: https://github.com/Adyen/adyen-node-api-library/compare/v32.1.0...HEAD
