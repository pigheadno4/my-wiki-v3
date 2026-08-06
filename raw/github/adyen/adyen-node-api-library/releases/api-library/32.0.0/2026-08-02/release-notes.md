<!-- Release notes generated using configuration in .github/release.yml at main -->

# What's Changed

✨  This release introduces the support of [Checkout API v72](https://docs.adyen.com/api-explorer/Checkout/72/overview) and [Cloud device API](https://docs.adyen.com/api-explorer/cloud-device-api/1/overview), a first-class replacement for the legacy `TerminalCloudAPI` that brings built-in Nexo message encryption, device management, and a cleaner service design.

## Breaking Changes 🛠

### Checkout API 

There are several breaking changes during the Checkout `v72` upgrade, check #1727 for the full details

- in`DirectDebitAuDetails` class `holderName` is now **required** (was optional). Consumers must always provide this field.
- `donationType` is now **optional** and deprecated. Use `type` instead.
- in `DonationPaymentRequest` several fields are removed : `additionalData`, `conversionId` `deliverAt`, `threeDSAuthenticationOnly` (this was deprecated since Checkout API v69, use `authenticationData.authenticationOnly`.
- in `PaymentAmountUpdateRequest` has been removed  `enhancedSchemeData`. Use the new `mpiData` field instead.
- in `PaymentRequest` `conversionId` was removed (deprecated since Checkout API v68, use `checkoutAttemptId`).
- in `StandalonePaymentCancelRequest` attribute `enhancedSchemeData` was removed.

### Transfers API

- `Counterparty` model removed and replaced by `GrantCounterparty` (used in `CapitalGrant`) and `GrantInfoCounterparty` (used in `CapitalGrantInfo`), with different field sets for each context. See #1634

## New Features 💎

### Checkout API 

- In `PaymentAmountUpdateRequest` add  `adjustAuthType` field (`PaymentAmountUpdateRequest.AdjustAuthTypeEnum`). Possible values: `cardholderInitiatedTransaction`, `merchantInitiatedTransaction`.
- New `adjustAuthorisationData` field (string) for [synchronous authorization adjustments](https://docs.adyen.com/online-payments/adjust-authorisation).
- New `mpiData` field (`ThreeDSecureData`) replacing `enhancedSchemeData`.

### Cloud Device API 

Two new services replace the deprecated `TerminalCloudAPI`:

- `cloudDeviceApi` — Send synchronous and asynchronous Terminal API messages, query connected devices and device status.
- `encryptedCloudDeviceApi` — Variant of `cloudDeviceApi` with built-in Nexo message encryption/decryption. Requires `EncryptionCredentialDetails` information.
New supporting security classes: `nexoSecurityManager`, `nexoCryptoPrimitives`, `nexoDerivedKeyGenerator`, `nexoSecurityException`, `encryptionCredentialDetails`.

It includes documentation:
- [Cloud device API docs](doc/CloudDeviceApi.md)
- [Migrating from Terminal (Cloud) API to Cloud device API](doc/MigratingToCloudDeviceApi.md)

### Transfers API
  - Add `CashOutApi` for initiating cashouts.
  - Add transfer tracing models and fields for UK FPS and US ACH.
  - Add `NetworkReason`, `InterchangeData`, and `UltimatePartyIdentification`.

## Fixes
- Fix ESM-compatible NexoCrypto exports and safely handle differing HMAC lengths. #1701 (https://github.com/Adyen/adyen-node-api-library/pull/1701)
- Correct webhook HMAC validation and discriminator mappings for webhook bank-account models.
- Update ESLint, Nock, and CI actions for Node.js 24 compatibility.

### PRs.
* [checkout] Code generation: update services and models by @AdyenAutomationBot in https://github.com/Adyen/adyen-node-api-library/pull/1727
* [transfers] Code generation: update services and models by @AdyenAutomationBot in https://github.com/Adyen/adyen-node-api-library/pull/1634
* [tapi] Code generation: update services and models by @AdyenAutomationBot in https://github.com/Adyen/adyen-node-api-library/pull/1708
* Add CloudDevice service class by @gcatanese in https://github.com/Adyen/adyen-node-api-library/pull/1709
* Add cloud device live URL support with region-based routing by @gcatanese in https://github.com/Adyen/adyen-node-api-library/pull/1713
* CloudDevice API Integration Testing by @gcatanese in https://github.com/Adyen/adyen-node-api-library/pull/1714
* [transferwebhooks] Code generation: update services and models by @AdyenAutomationBot in https://github.com/Adyen/adyen-node-api-library/pull/1716
* [tapi] Code generation: update services and models by @AdyenAutomationBot in https://github.com/Adyen/adyen-node-api-library/pull/1717
* Add support of encrypted payload for Cloud Device API by @gcatanese in https://github.com/Adyen/adyen-node-api-library/pull/1715
* Cloud device API documentation by @gcatanese in https://github.com/Adyen/adyen-node-api-library/pull/1721
* Add PredefinedContentHelper for Cloud device API (tapi) by @gcatanese in https://github.com/Adyen/adyen-node-api-library/pull/1726
* README: Update API/Webhook versions  by @gcatanese in https://github.com/Adyen/adyen-node-api-library/pull/1728
* fix: remove environment from publish-npm job to fix OIDC trusted publishing by @gcatanese in https://github.com/Adyen/adyen-node-api-library/pull/1705
* revert: restore environment: release in publish-npm job by @gcatanese in https://github.com/Adyen/adyen-node-api-library/pull/1707
* fix: guard against mismatched HMAC length in NexoCrypto.validateHmac (#1703) by @CedricConday in https://github.com/Adyen/adyen-node-api-library/pull/1712
* chore(ci): upgrade GitHub Actions to Node.js 24 compatible versions by @gcatanese in https://github.com/Adyen/adyen-node-api-library/pull/1704
* fix: guard HMAC comparison on decoded length in HmacValidator by @CedricConday in https://github.com/Adyen/adyen-node-api-library/pull/1725
* Move tapi PredefinedContentHelper to src/utils/tapi by @gcatanese in https://github.com/Adyen/adyen-node-api-library/pull/1731
* Add SaleToAcquirerData parser and SaleDataHelper for Cloud device API (tapi) by @gcatanese in https://github.com/Adyen/adyen-node-api-library/pull/1732
* Release v32.0.0 by @AdyenAutomationBot in https://github.com/Adyen/adyen-node-api-library/pull/1706

## New Contributors
* @CedricConday made their first contribution in https://github.com/Adyen/adyen-node-api-library/pull/1712

**Full Changelog**: https://github.com/Adyen/adyen-node-api-library/compare/v31.0.0...v32.0.0