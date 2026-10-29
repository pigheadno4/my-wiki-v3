**Contents**

- [What's Changed](#whats-changed)
- [New Features](#new-features-)
- [Contributor Notes](#contributor-notes-)
- [Other Changes](#other-changes-️)
- [PRs](#prs-️)
- [Contributors](#contributors)

## What's Changed

- Add support for the Foreign Exchange API, so you can calculate converted amounts and exchange rates.
- Add `Client::setRegion()` so you can route Terminal API cloud requests to a regional live endpoint.
- Remove the `adviceAuthorised` and `adviceRefused` status values from Transfer Webhooks models as they are no longer used.
- Add transfer tracing data, network reason details, and card network variants to Transfer Webhooks and Transaction Webhooks. Add `transactionLinkId` to the Payment API and sub-merchant data to the Payments App API.

## New Features 💎

### Foreign Exchange API

- Add support for [Foreign Exchange API](https://docs.adyen.com/api-explorer/foreignexchange/1/overview) for calculating the amounts and exchange rates required to convert a transaction's currency, using `Adyen\Service\ForeignExchange\RatesApi::calculate()`. ([#943](https://github.com/Adyen/adyen-php-api-library/pull/943))

### Payment API

- Add `transactionLinkId` to `AdditionalDataCommon` and `ResponseAdditionalDataCommon`. ([#931](https://github.com/Adyen/adyen-php-api-library/pull/931))

### Payments App API

- Add `subMerchantData` to `BoardingTokenRequest`, using the new `SubMerchantData` model. ([#938](https://github.com/Adyen/adyen-php-api-library/pull/938))

### Terminal API

- Add `Client::setRegion()` to configure the Terminal API cloud region. In the live environment, `PosPayment` writes the matching regional endpoint to `endpointTerminalCloud` and throws `AdyenException` for a region that has no Terminal API endpoint. ([#936](https://github.com/Adyen/adyen-php-api-library/pull/936))
- Deprecate `Client::retrieveCloudEndpoint()`. ([#936](https://github.com/Adyen/adyen-php-api-library/pull/936))

### Transaction Webhooks

- Add `networkVariant` to `IssuedCard` (values `maestro_us`, `mastercard`, and `visa`) and to `TransferViewCategoryData`. ([#941](https://github.com/Adyen/adyen-php-api-library/pull/941))

### Transfer Webhooks

- Add network reason details and transfer tracing data. ([#914](https://github.com/Adyen/adyen-php-api-library/pull/914), [#942](https://github.com/Adyen/adyen-php-api-library/pull/942))
  - Add `networkReason` (new `NetworkReason` model) and `tracing` (new `TransferDataTracing` model) to `TransferData`.
  - Add `tracingData` (new `TransferEventTracingData` model) to `TransferEvent`.
  - Add the `UKFpsTracingData` model for UK Faster Payments tracing and the `USAchTracingData` model for US ACH tracing.
- Add the `reversalReceived` status to `Modification`, `TransferData`, and `TransferEvent`. Add the `fxSell` and `fxBuy` types to `TransferData`. Add `networkVariant` to `IssuedCard` (values `maestro_us`, `mastercard`, and `visa`) and to `TransferDataCategoryData`. ([#942](https://github.com/Adyen/adyen-php-api-library/pull/942))

## Contributor Notes 🔧

- Update the development dependency `squizlabs/php_codesniffer` from `4.0.1` to `4.0.2` to fix a security vulnerability (CVE-2026-67434). ([#929](https://github.com/Adyen/adyen-php-api-library/pull/929))

## Other Changes 🖇️

- Update the `MidServiceNotificationData::setType()` documentation in Management Webhooks to describe the `cartesBancaires` details returned for the `cartebancaire` payment method variant. ([#940](https://github.com/Adyen/adyen-php-api-library/pull/940))

## PRs 📋️

- [transferwebhooks] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#914](https://github.com/Adyen/adyen-php-api-library/pull/914)
- Update dependency squizlabs/php_codesniffer to v4.0.2 [SECURITY] by [@renovate[bot]](https://github.com/apps/renovate) in [#929](https://github.com/Adyen/adyen-php-api-library/pull/929)
- Release v30.1.0 by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#930](https://github.com/Adyen/adyen-php-api-library/pull/930)
- [payment] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#931](https://github.com/Adyen/adyen-php-api-library/pull/931)
- Feature Terminal API regional endpoint configuration by [@ashwaniarya-adyen](https://github.com/ashwaniarya-adyen) in [#936](https://github.com/Adyen/adyen-php-api-library/pull/936)
- [paymentsapp] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#938](https://github.com/Adyen/adyen-php-api-library/pull/938)
- [managementwebhooks] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#940](https://github.com/Adyen/adyen-php-api-library/pull/940)
- [transactionwebhooks] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#941](https://github.com/Adyen/adyen-php-api-library/pull/941)
- [transferwebhooks] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#942](https://github.com/Adyen/adyen-php-api-library/pull/942)
- [foreignexchange] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#943](https://github.com/Adyen/adyen-php-api-library/pull/943)

## Contributors

- [@AdyenAutomationBot](https://github.com/AdyenAutomationBot)
- [@ashwaniarya-adyen](https://github.com/ashwaniarya-adyen)
- [@renovate[bot]](https://github.com/apps/renovate)

**Full Changelog**: https://github.com/Adyen/adyen-php-api-library/compare/v30.0.2...v30.1.0
