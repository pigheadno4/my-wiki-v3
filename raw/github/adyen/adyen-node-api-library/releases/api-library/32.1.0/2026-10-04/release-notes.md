## What's Changed

This release adds Checkout session updates and richer payment, travel, lodging, and enhanced-scheme models; introduces the Document Collector API with multipart file uploads; and exposes Session Authentication types. It also removes obsolete Checkout error models and two deprecated payment-method enum values.

## New Features 💎

### Checkout API

- Add `PaymentsApi.updateSession(sessionId, checkoutSessionPatchSessionRequest, requestOptions?)` with `CheckoutSessionPatchSessionRequest`, `CheckoutSessionPatchSessionResponse`, and `SessionAmountUpdate` to update a session's amount and payable state. ([#1735](https://github.com/Adyen/adyen-node-api-library/pull/1735))
- Add `AuPayDetails`, `DBaraiDetails`, and `SepaDirectDebitDonations`, including their `TypeEnum` values, and update discriminator mappings for payment methods and response actions. ([#1735](https://github.com/Adyen/adyen-node-api-library/pull/1735))
- Add enhanced-scheme models `CarRental`, `PickupInfo`, `RentalSurcharges`, `ReturnInfo`, `Healthcare`, `Lodging`, `Folio`, `Room`, and `TemporaryServices`; expose them through `EnhancedSchemeData.carRental`, `healthcare`, `lodging`, and `temporaryServices`. ([#1735](https://github.com/Adyen/adyen-node-api-library/pull/1735))
- Add `ThirdPartyTokenRedundancyInfo` with `requestParameters` and `requestTemplateCode`; expose it on `CreateCheckoutSessionRequest`, `CreateCheckoutSessionResponse`, and `PaymentRequest`, and add `CreateCheckoutSessionRequest.shopperConversionId`. ([#1735](https://github.com/Adyen/adyen-node-api-library/pull/1735))
- Add `LineItem.returnShippingCompany`, `returnTrackingNumber`, `returnTrackingUri`, `shippingCompany`, `shippingMethod`, `trackingNumber`, and `trackingUri`; add `PaypalUpdateOrderRequest.deliveryAddress`, `discountAmount`, and `shippingAmount`. ([#1735](https://github.com/Adyen/adyen-node-api-library/pull/1735))
- Add `AffirmDetails.financingProgram`, `CardBrandDetails.healthcare`, `DonationCampaignsRequest.label`, `KlarnaDetails.merchantData`, `RivertyDetails.merchantData`, and `StoredPaymentMethod.externalToken`. ([#1735](https://github.com/Adyen/adyen-node-api-library/pull/1735))
- Make `SepaDirectDebitDetails.iban` and `SepaDirectDebitDetails.ownerName` optional. ([#1380](https://github.com/Adyen/adyen-node-api-library/issues/1380)) ([#1735](https://github.com/Adyen/adyen-node-api-library/pull/1735))

### Document Collector API

- Add support for [DocumentCollectorAPI](https://docs.adyen.com/api-explorer/Document-Collector/1/overview) for multipart cross-border invoice uploads.

### Payment API

- Add `transactionLinkId` to `AdditionalDataCommon` and `ResponseAdditionalDataCommon`. ([#1738](https://github.com/Adyen/adyen-node-api-library/pull/1738))

## Fixes ⛑️

- Export the `Types.sessionAuthentication` namespace so request and response models used by `SessionAuthenticationAPI` are available from the public package entry point. ([#1751](https://github.com/Adyen/adyen-node-api-library/issues/1751)) ([#1760](https://github.com/Adyen/adyen-node-api-library/pull/1760))
- Update the Banking webhook HMAC README example to use `validateHMACSignature(hmacKey, hmacSignature, data)` instead of the deprecated, misleading call. ([#1744](https://github.com/Adyen/adyen-node-api-library/pull/1744))

## Notes

Few unused attributes have been removed: 
- Remove `Types.checkout.DefaultErrorResponseEntity`, its `constructor()`, and its serialized properties `detail`, `errorCode`, `instance`, `invalidFields`, `requestId`, `status`, `title`, and `type`. ([#1735](https://github.com/Adyen/adyen-node-api-library/pull/1735))
- Remove `Types.checkout.InvalidField`, its `constructor()`, and its serialized properties `message`, `name`, and `value`. ([#1735](https://github.com/Adyen/adyen-node-api-library/pull/1735))
- Remove `Types.checkout.PaymentDetails.TypeEnum.Paybright` and move the `gopay_wallet` value from `Types.checkout.PaymentDetails.TypeEnum.GopayWallet` to `Types.checkout.StoredPaymentMethodDetails.TypeEnum.GopayWallet`. ([#1735](https://github.com/Adyen/adyen-node-api-library/pull/1735))


## Contributor Notes 🔧

- Add `form-data` 4.0.6 as a runtime dependency and reusable multipart and URL-encoded request helpers; update the generated API template for file uploads. ([#1761](https://github.com/Adyen/adyen-node-api-library/pull/1761))
- Patch transitive security-sensitive dependencies: `fast-uri` 3.1.5, `brace-expansion` 1.1.18, `ajv` 6.15.0, `js-yaml` 3.15.1/4.3.1, and an override for `micromatch` 4.0.8. ([#1753](https://github.com/Adyen/adyen-node-api-library/pull/1753)) ([#1754](https://github.com/Adyen/adyen-node-api-library/pull/1754)) ([#1755](https://github.com/Adyen/adyen-node-api-library/pull/1755)) ([#1756](https://github.com/Adyen/adyen-node-api-library/pull/1756)) ([#1757](https://github.com/Adyen/adyen-node-api-library/pull/1757))
- Update contributor tooling: `eslint-plugin-unused-imports` 4.x, `ts-loader` 9.6.2, and `acorn` 8.17.0. ([#1402](https://github.com/Adyen/adyen-node-api-library/pull/1402)) ([#1646](https://github.com/Adyen/adyen-node-api-library/pull/1646)) ([#1724](https://github.com/Adyen/adyen-node-api-library/pull/1724))
- Update release, stale, and Node setup actions, and improve the SonarCloud scanner configuration. ([#1719](https://github.com/Adyen/adyen-node-api-library/pull/1719)) ([#1722](https://github.com/Adyen/adyen-node-api-library/pull/1722)) ([#1723](https://github.com/Adyen/adyen-node-api-library/pull/1723)) ([#1752](https://github.com/Adyen/adyen-node-api-library/pull/1752))
- Remove redundant generated `void` statements so SDK Automation can continue removing unused imports. ([#1779](https://github.com/Adyen/adyen-node-api-library/pull/1779))

## Other Changes 🖇️

- Add a `SaleToAcquirerData.additionalData` usage example, fix the classic Platforms API documentation link, and list Document Collector API v1 in the supported APIs table. ([#1741](https://github.com/Adyen/adyen-node-api-library/pull/1741)) ([#1743](https://github.com/Adyen/adyen-node-api-library/pull/1743)) ([#1782](https://github.com/Adyen/adyen-node-api-library/pull/1782))

## PRs 📋️
- Update dependency eslint-plugin-unused-imports to v4 by [@renovate[bot]](https://github.com/apps/renovate) in [#1402](https://github.com/Adyen/adyen-node-api-library/pull/1402)
- Update dependency ts-loader to v9.6.2 by [@renovate[bot]](https://github.com/apps/renovate) in [#1646](https://github.com/Adyen/adyen-node-api-library/pull/1646)
- Update actions/setup-node action to v4.4.0 by [@renovate[bot]](https://github.com/apps/renovate) in [#1719](https://github.com/Adyen/adyen-node-api-library/pull/1719)
- Update actions/stale action to v9.1.0 by [@renovate[bot]](https://github.com/apps/renovate) in [#1722](https://github.com/Adyen/adyen-node-api-library/pull/1722)
- Update Adyen/release-automation-action action to v1.4.0 by [@renovate[bot]](https://github.com/apps/renovate) in [#1723](https://github.com/Adyen/adyen-node-api-library/pull/1723)
- Update dependency acorn to v8.17.0 by [@renovate[bot]](https://github.com/apps/renovate) in [#1724](https://github.com/Adyen/adyen-node-api-library/pull/1724)
- [storedvalue] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1733](https://github.com/Adyen/adyen-node-api-library/pull/1733)
- [checkout] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1735](https://github.com/Adyen/adyen-node-api-library/pull/1735)
- [payment] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1738](https://github.com/Adyen/adyen-node-api-library/pull/1738)
- SaleToAcquirerData.additionalData: Add examples in test and code by [@gcatanese](https://github.com/gcatanese) in [#1741](https://github.com/Adyen/adyen-node-api-library/pull/1741)
- Fix Platforms APIs documentation link by [@gcatanese](https://github.com/gcatanese) in [#1743](https://github.com/Adyen/adyen-node-api-library/pull/1743)
- docs: fix Banking webhook HMAC example in README by [@mrSamDev](https://github.com/mrSamDev) in [#1744](https://github.com/Adyen/adyen-node-api-library/pull/1744)
- Improve SonarCloud workflow configuration by [@gcatanese](https://github.com/gcatanese) in [#1752](https://github.com/Adyen/adyen-node-api-library/pull/1752)
- Update fast-uri to 3.1.5 by [@gcatanese](https://github.com/gcatanese) in [#1753](https://github.com/Adyen/adyen-node-api-library/pull/1753)
- Update brace-expansion to 1.1.18 by [@gcatanese](https://github.com/gcatanese) in [#1754](https://github.com/Adyen/adyen-node-api-library/pull/1754)
- Update ajv to 6.15.0 by [@gcatanese](https://github.com/gcatanese) in [#1755](https://github.com/Adyen/adyen-node-api-library/pull/1755)
- Update js-yaml patched versions by [@gcatanese](https://github.com/gcatanese) in [#1756](https://github.com/Adyen/adyen-node-api-library/pull/1756)
- Override micromatch to 4.0.8 by [@gcatanese](https://github.com/gcatanese) in [#1757](https://github.com/Adyen/adyen-node-api-library/pull/1757)
- [documentcollector] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1758](https://github.com/Adyen/adyen-node-api-library/pull/1758)
- Export Session Authentication types by [@shin4141](https://github.com/shin4141) in [#1760](https://github.com/Adyen/adyen-node-api-library/pull/1760)
- Add multipart request support by [@gcatanese](https://github.com/gcatanese) in [#1761](https://github.com/Adyen/adyen-node-api-library/pull/1761)
- [balancecontrol] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1763](https://github.com/Adyen/adyen-node-api-library/pull/1763)
- [storedvalue] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1764](https://github.com/Adyen/adyen-node-api-library/pull/1764)
- [capital] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1765](https://github.com/Adyen/adyen-node-api-library/pull/1765)
- [disputes] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1766](https://github.com/Adyen/adyen-node-api-library/pull/1766)
- [checkout] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1767](https://github.com/Adyen/adyen-node-api-library/pull/1767)
- [documentcollector] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1768](https://github.com/Adyen/adyen-node-api-library/pull/1768)
- [posmobile] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1769](https://github.com/Adyen/adyen-node-api-library/pull/1769)
- [transfers] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1770](https://github.com/Adyen/adyen-node-api-library/pull/1770)
- [legalentitymanagement] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1771](https://github.com/Adyen/adyen-node-api-library/pull/1771)
- [payout] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1772](https://github.com/Adyen/adyen-node-api-library/pull/1772)
- [dataprotection] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1773](https://github.com/Adyen/adyen-node-api-library/pull/1773)
- [sessionauthentication] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1774](https://github.com/Adyen/adyen-node-api-library/pull/1774)
- [recurring] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1775](https://github.com/Adyen/adyen-node-api-library/pull/1775)
- [paymentsapp] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1776](https://github.com/Adyen/adyen-node-api-library/pull/1776)
- [binlookup] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1777](https://github.com/Adyen/adyen-node-api-library/pull/1777)
- [payment] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1778](https://github.com/Adyen/adyen-node-api-library/pull/1778)
- [Bug]: Remove redundant void statements from generated APIs by [@gcatanese](https://github.com/gcatanese) in [#1779](https://github.com/Adyen/adyen-node-api-library/pull/1779)
- [documentcollector] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1780](https://github.com/Adyen/adyen-node-api-library/pull/1780)
- [documentcollector] Code generation: update services and models by [@AdyenAutomationBot](https://github.com/AdyenAutomationBot) in [#1781](https://github.com/Adyen/adyen-node-api-library/pull/1781)
- Add Document Collector API to README by [@gcatanese](https://github.com/gcatanese) in [#1782](https://github.com/Adyen/adyen-node-api-library/pull/1782)

## Contributors

- [@AdyenAutomationBot](https://github.com/AdyenAutomationBot)
- [@gcatanese](https://github.com/gcatanese)
- [@mrSamDev](https://github.com/mrSamDev)
- [@renovate[bot]](https://github.com/apps/renovate)
- [@shin4141](https://github.com/shin4141)

**Full Changelog**: https://github.com/Adyen/adyen-node-api-library/compare/v32.0.0...HEAD
