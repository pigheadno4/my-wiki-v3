---
title: "Stripe Fiat-to-Crypto Onramp"
type: concept
category: technology
tags: [stripe, crypto, onramp, fiat-to-crypto, kyc, dapp]
---

## Overview

Stripe's fiat-to-crypto onramp enables customers to purchase and exchange cryptocurrencies directly within a merchant's platform or decentralized application (Dapp). Stripe acts as **merchant of record**, assuming full liability for fraud and disputes, handling KYC verifications, regulatory requirements, and sanctions screening.

Customer payment methods, KYC data, and wallet information are saved with Stripe, reducing friction for repeat onramp sessions.

## Integration Modes

| Mode | Dated availability evidence | Use case and guide coverage |
| --- | --- | --- |
| **Stripe-hosted** | May 11, 2026: public preview; application for access | No-code redirect to `crypto.link.com`; amount, currency and network customization |
| **Embedded** (iframe widget) | May 11, 2026: public preview; application for access | Onramp API in a website or mobile webview; branding and parameter customization |
| **Embedded components** (headless SDK) | May 11, 2026 overview and integration guide: private preview with separate signup; November status unverified | May full guide covers Web, React Native, Android and iOS with custom UI through SDK and API; May quickstart covers web/React Native and links native samples. November same-URL hub points to a distinct quickstart and platform guides, whose current bodies were not captured here. |

> [!warning] Contradiction
> The May overview assigns preview status separately to each mode. The November 7 overview collapses availability to a single `Public preview` cell and omits the separate mobile signup; the November Embedded Components hub gives navigation, not an access statement. That cell does not prove mobile public-preview access or any account's eligibility. See [[source-stripe-crypto-onramp]].

## Access

To access the onramp, the May and November 2026 overview and Stripe-hosted guides require a Stripe account, an application at `dashboard.stripe.com/crypto-onramp/get-started`, and approval before sandbox/test development. Stripe says it reviews **most** applications within 48 hours, then notifies applicants of approval or a request for more information; neither the timing nor access is established for a particular account. Constructing a frontend redirect URL without a Stripe account is a separate code-path statement and does not waive onramp approval or prove a transaction can complete.

## Stripe-Hosted Currency Snapshot (US + EU, May/November 2026)

ETH, ETH (Base), SOL, POL, MATIC, BTC, AVAX, XLM, USDC (Ethereum/Solana/Polygon/Avalanche/Base/Stellar)

**Geo restrictions in the May and November 2026 Stripe-hosted guides, with available currencies expressly subject to change**:

- XLM, USDC (Stellar/Avalanche/Polygon): not in New York
- ETH (Base), MATIC, AVAX, USDC (Solana/Polygon/Avalanche/Base): not in EU

These document snapshots do not establish current asset, country, or account eligibility.

## Stripe-Hosted: Two Customization Paths

| Path | Requirements | Capability |
| --- | --- | --- |
| Generate redirect URL (frontend) | May 11, 2026 hosted guide: no Stripe account needed to construct the URL; onramp use still requires an account, application and approval, including sandbox access | Light customization; no branding |
| Mint session with redirect URL (backend) | Stripe account + API | Full customization incl. wallet address; branding |

Frontend scripts must load from Stripe domains (`js.stripe.com`, `crypto-js.stripe.com`) — never bundle or self-host (PCI requirement).

Session API: `POST /v1/crypto/onramp_sessions` → `redirect_url`, `client_secret`, `transaction_details`.

## Embedded Integration (dated Node/React and November variants)

The May 11, 2026 quickstart shows Node/Express creating an `OnrampSession` with a custom `Stripe.StripeResource` extension and returning `clientSecret`. Its browser example uses `@stripe/crypto` and `@stripe/stripe-js`, calls `loadStripeOnramp` with the publishable key, then mounts an iframe using the client secret. The client sends sample `transaction_details` (`destination_currency`, `destination_exchange_amount`, `destination_network`); the server separately reads `customer_ip_address` from its request. These are passed sample fields, not a complete schema showing universal requiredness. The shown `usdc`, `13.37`, and `ethereum` values are sandbox examples.

The November 7 capture adds alternative Ruby, Python, PHP, Go, .NET and Java server snippets and a direct browser-script variant. For that script variant, Stripe instructs loading its Stripe.js and crypto-js scripts from Stripe domains, without bundling or self-hosting them. The React package path remains separately documented. `onramp_ui_loaded` means the UI loaded and `onramp_session_updated` reports a session status change; neither alone proves payment finality or crypto delivery. See [[source-stripe-crypto-onramp-embedded-quickstart]].

> [!warning] Contradiction
> Both dated quickstarts call the onramp API limited beta and say official libraries lack built-in endpoint support, while the November page also shows Java `client.v1().crypto().onrampSessions().create(params)` and a .NET `OnrampSessionService`. The May Node custom extension is a historical example; this page does not verify which SDK versions implement those other snippets or merchant access.

## Session Lifecycle States

The embedded-widget guide lists `initialized`, `rejected`, `requires_payment`, `fulfillment_processing` and `fulfillment_complete`. `fulfillment_processing` means payment completed **but crypto has not yet been delivered**; `fulfillment_complete` means delivery is confirmed. See [[source-stripe-crypto-onramp-embedded-setup]] for the dated state descriptions.

## Quotes API

`GET /v1/crypto/onramp/quotes` — `source_amount` OR `destination_amount`, filter by `destination_currencies[]`/`destination_networks[]`. Response: per currency-network pair with `network_fee_monetary` + `transaction_fee_monetary`.

## Sandbox Test Values

OTP: `000000` | SSN: `000000000` | Address line 1: `address_full_match` | Card: `4242424242424242`

## Payment Methods and Delivery

- Credit, debit, Apple Pay, ACH (US only)
- All eligible for **instant crypto delivery** after KYC completion
- Returning users: faster checkout via [[stripe-link]] consumer account

Every session status change generates a webhook.

## Embedded Components (Headless) Mode

The May 11, 2026 [[source-stripe-crypto-onramp|overview]] and [[source-stripe-crypto-onramp-embedded-components-integration|integration guide]] described Embedded Components as **private preview**; the integration guide scoped it to US users excluding New York, distinct from the embedded iframe's May US/EU scope excluding Hawaii. It describes a custom headless UI, while the May [[source-stripe-crypto-onramp-embedded-components|quickstart]] documents Link OAuth for the authenticated flow. The November 7 same-URL hub instead routes to a distinct quickstart, platform guides and an EU KYC guide; it states no current preview or regional eligibility. The November [[source-stripe-crypto-onramp-kyc-integration|KYC guide]] addresses EU customers' additional identifier and attestation requirements and allows mobile Apple Pay or Google Pay collection before Link authentication, while token creation still requires authentication and minimum identity submission.

> [!warning] Contradiction
> The May integration guide's US-only, excluding-New-York scope and the November KYC guide's EU-customer note leave present regional scope unresolved. The hub's EU KYC link is navigation, and the linked guide body was not captured here. Neither source proves EU merchant eligibility, current preview access or a particular account's authorization; check the current variant and account access before applying either dated regional statement.

| | Embedded (iframe) | Embedded Components (headless) |
| --- | --- | --- |
| Auth | Session `client_secret` | Link OAuth → `crypto_customer_id` |
| SDK | `loadStripeOnramp` | `loadCryptoOnrampAndInitialize` |
| API version | Standard | `Stripe-Version: 2026-03-25.dahlia;crypto_onramp_beta=v2` |

**Customer setup sequence**: The May 2026 guide depicted auth → KYC → identity verification → wallet → payment method → checkout. For the November 2026 iOS, Android, and React Native **Apple Pay or Google Pay** path, payment-method collection may occur before Link registration/authentication and KYC submission; it is not KYC approval or a purchase. Complete registration or authentication and submit minimum identity information before `createCryptoPaymentToken`. L0/L1 verification is asynchronous: check CryptoCustomer until no verification remains pending before creating an onramp session, which otherwise returns HTTP 400. This KYC guide does not generalize pre-auth collection to other payment methods.

**May Web SDK method examples**: `registerLinkUser()`, `authenticate()`, `submitKycInfo()`, `verifyDocuments()`, `registerWalletAddress()`, `collectPaymentMethod()`, `performCheckout()`. React Native, Android, and iOS use their own platform methods; see the platform locators in [[source-stripe-crypto-onramp-embedded-components-integration]].

**KYC tiers** (Embedded Components): L0 (name/phone/email/address as customer information) → L1 (+ DOB/SSN) → L2 (+ photo ID/selfie). The May 2026 guide required L0 submission before payment-method collection; the November guide permits Apple Pay or Google Pay collection before Link authentication/KYC on iOS, Android and React Native, while registration/authentication plus minimum identity submission are still required before `createCryptoPaymentToken`. Wallet phone/email go to Link registration, not `attachKYCInfo`; KYC name/address go to that API. L0/L1 verification is asynchronous — poll before session creation; L2 uses `verifyIdentity()`. A current tier can be pending/rejected and must not be read as verified; a failed L0 can be superseded by completed L1. Session creation returns 400 on pending verification. Minimum-identity, L1 and L2 error codes require their distinct step-up paths; L2 can also be required by risk rules below a tier's amount limit. See [[source-stripe-crypto-onramp-kyc-integration]].

> [!warning] Contradiction
> The May L0-before-payment-method rule conflicts with the November mobile Platform Pay sequencing. The November minimum-identity error means missing submission, not necessarily failed L0 verification. Payment-method collection is not token creation, KYC approval, session creation or purchase.

**Session**: `ui_mode: 'headless'` + `crypto_customer_id` + `payment_token`. In the May Web ACH checkout path, pass `mandate_data` and collect the user's IP address and user agent. In the May React Native, Android, and iOS ACH paths, the API may report missing `mandate_data`; collect acceptance and send it on a later checkout call if required. Refresh an expired quote before retrying when indicated.

**Access token TTL**: 1 hour; refresh token returned on each use — store the latest; use in `Stripe-OAuth-Token` header.

**May Web `CryptoNetwork` type (13 enum values)**: bitcoin, ethereum, solana, polygon, stellar, avalanche, base, aptos, optimism, worldchain, xrpl, sui, tempo. This list alone does not establish current account, region, mode, or currency-network eligibility; the May iOS livemode table is separate.

`@stripe/stripe-react-native@0.73.0` adds `tempo` to its `CryptoNetwork` enum, providing package-level evidence that the React Native wrapper exposes the network. This does not by itself prove account, country, currency, or production eligibility.

**`performCheckout` last_error codes**: `action_required` (3DS — retry), `missing_kyc`, `missing_document_verification`, `charged_with_expired_quote`, `missing_consumer_wallet` (all retriable); `transaction_limit_reached`, `location_not_supported`, `transaction_failed` (terminal — do not retry).

## React Native 0.82.0 Contact Prefill and Country Hint

`Onramp.Configuration.countryHint` accepts an optional merchant-provided ISO alpha-2 country to help merchant-of-record selection before a KYC region is established; the established region takes precedence. The retained iOS configuration mapper forwards it to coordinator creation; Android forwarding appears in comparison hunks, not a complete retained Onramp mapper. This does not establish backend selection rules or eligibility.

Wallet collection may return optional `kycInfo.email`, normalized E.164 `phone` and original `rawPhone`. Request Apple Pay email/phone via `requiredShippingAddressFields`, with name/address via billing contact fields; Google Pay uses `isEmailRequired` and billing-address phone requirements. Samsung contact collection is opt-in via `samsungPay.collectContactInformation` (documented default false). Use phone for registration only after E.164 validation, and rawPhone for display/correction. The iOS KYC input mapper does not submit these three contact fields with `attachKycInfo`. Android contact-return/configuration changes are hunk-level evidence. Collection, contact prefill and KYC submission are distinct operations.

The retained example now prefills name/address and address-update forms, retaining existing fields when a wallet field is absent and asking for review. A separate registration-screen change shows prefill before registration only in comparison hunks; it is not a fully retained/tested integration recipe. Native pins are Android 23.23.0/iOS 26.14.0: do not infer the newer native KYC API or funding-label changes have React Native bindings.

> [!warning] Contradiction
> The 0.82.0 raw changelog retrospectively places the Platform Pay contact-prefill/Samsung note under 0.81.0. The earlier retained 0.81.0 bridge/types lack these additions; the exact 0.81.0 -> 0.82.0 comparison observes them. Preserve both raw attributions, not an unsupported first-release claim. See [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]].

## React Native 0.75.0 Delta

### React Native 0.77.0 KYC Typing

`KycInfo.idType` accepts `social_security_number` (US SSN), `ca_sin` (Canada SIN), `co_nit` (Colombia NIT), and `ph_tin` (Philippines TIN), with SSN as the documented default. Retained iOS mapping also falls back to SSN for missing/unrecognized strings; Android mappings show the same fallback in comparison hunks. These identifiers do not prove regional merchant access or successful KYC validation. The demo clears the ID number when residence changes and keeps EU-only birthplace/nationality fields separate. Android presenter recreation is a release-note announcement backed by changed hunks, not a full-file or device-tested guarantee. See [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]].

### React Native 0.76.0 Wallet Deletion

`useOnramp().deleteWalletAddress(walletId)` deletes a registered wallet from the current Link account and requires an authenticated Link user. Await its `{error?}` result and handle failure before changing local state. The iOS bridge delegates to the native coordinator and maps failure; Android delegation/result handling is visible in comparison hunks, but the complete Android Onramp implementation remains outside the capsule. This is wallet-record deletion, not a crypto transfer or account deletion; propagation, idempotency and retry guarantees are not established.

The retained demo lists wallets through its backend, deletes by ID with its reauthentication wrapper, removes the successful result from local state, and clears selected wallet/challenge state when it matches. That demo retry behavior is not a general SDK retry guarantee. See [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]].

`@stripe/stripe-react-native@0.75.0` adds Android Samsung Pay collection through `useOnramp()`. Enable the Onramp module with `StripeSdk_includeOnramp=true`, include Samsung Pay SDK `2.22.00` in the app, and pass `samsungPay.serviceId` to `configure`. Optional fields are `merchantId`, `merchantName`, and `allowedCardBrands`; an omitted or empty brand list uses SDK defaults.

After configuration, call `isSamsungPaySupported()` before offering the option. The retained iOS bridge resolves `false`; Android readiness and setup changes are visible in comparison hunks, while complete Android Onramp implementation files are outside this capsule. This capability is specific to Crypto Onramp and does not establish Samsung Pay support in ordinary PaymentSheet.

```tsx
// Inside a component, after successful Onramp configuration/authentication.
const { isSamsungPaySupported, collectPaymentMethod } = useOnramp();
if (await isSamsungPaySupported()) {
  const result = await collectPaymentMethod('SamsungPay', {
    samsungPay: { currencyCode: 'USD', amount: 100, orderNumber: 'order-123' },
  });
  if (result.error) throw new Error(result.error.message);
  // Continue with token creation and the existing backend/session checkout flow.
}
```

`amount` uses the currency's smallest unit; `orderNumber` must identify the transaction uniquely. Collection alone does not complete checkout. The retained demo uses a fixed collection amount and separately hardcodes its session amount, so it is a flow example rather than a production pricing template.

The release also adds `onrampErrorType` variants `InvalidWalletOwnershipSignatureError`, `WalletOwnershipChallengeExpiredError`, `InvalidWalletOwnershipChallengeError`, `WalletNotFoundError`, and `UnsupportedNetworkError`. Keep generic-error fallback handling and review exhaustive switches. Wallet challenge APIs already existed in `0.70.0`; the new contribution is specific error classification. Native pins advance to Stripe Android `23.16.0` and Stripe iOS `26.7.0`. See [[source-github-stripe-react-native]] and [[changelog-github-stripe-react-native]].

### Android `23.15.0` Samsung Pay Contracts

Native compiled API adds OnrampConfiguration.SamsungPayConfig, samsungPayConfig, samsungPayIsReadyCallback, SamsungPay selection/display types and Available/Unavailable results carrying SamsungPayException. Errors expose a reason, optional native error code and developer/user messages. The release requires the merchant app to supply the Samsung Pay SDK; its version, parameter meanings/defaults and runtime mapping are not established by these declarations because implementation is excluded. This is Crypto Onramp, not ordinary PaymentSheet wallet support. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]]; the React Native integration above has its own evidence/version boundary.

### Android `23.16.0` Wallet Deletion

Experimental `OnrampCoordinator.deleteWalletAddress(walletId: String)` is documented to delete a crypto wallet from the current Link account and requires an authenticated Link user. The retained method delegates to `OnrampInteractor`; compiled signatures expose `OnrampDeleteWalletAddressResult.Completed` and `Failed`, with `Failed.error` as Throwable. Network authorization, deletion propagation, idempotency and retry behavior remain implementation gaps, not inferred guarantees. This concerns registered wallet information, not crypto transfer or account deletion. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

### Android `23.17.0` Module Requirements

The retained Crypto Onramp and Identity Gradle files declare `minSdkVersion 24`; Onramp depends on Identity, which adds MediaPipe Tasks Vision 0.10.35. Guided 3D selfie capture is a release announcement, not a verified flow in the bounded capsule. This does not raise the minimum for every Android payment module. The new changelog labels the API 24 requirement under 23.15.0 retrospectively, absent from the earlier retained builds; exact first implementation release remains unproven. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

### Android `23.18.0` KYC Type Evidence

Compiled API adds `IdType.CanadianSocialInsuranceNumber`, `ColombianTaxIdentificationNumber`, `PhilippinesTaxpayerIdentificationNumber` and `SocialSecurityNumber`, plus `KycInfo.getIdType()` and constructor overloads carrying IdType. Earlier constructors remain present. The inventory does not establish parameter names/defaults, identifier formats, serialization, country eligibility or backend validation; the changed model/request implementations are excluded.

The newer changelog labels these additions under 23.17.1 retrospectively, but the retained 23.17.1 API/notes lacked them. Keep that later label separate from the observed 23.17.1 -> 23.18.0 signature boundary; neither proves the exact first implementation release. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

### Android `23.21.0` Conditional Terms Contracts

Experimental OnrampCoordinator.Presenter adds presentTermsAndConditionsIfNeeded and presentTermsOfServiceIfNeeded. Both document an authenticated Link user; terms and conditions are called before checkout, terms of service during onboarding after authentication. Each delegates to the presenter coordinator and delivers its result through the corresponding OnrampCallbacks hook. Compiled API adds termsAndConditionsCallback/termsOfServiceCallback and OnrampPartnerTermsResult variants Accepted, Cancelled, Failed (Throwable) and NotRequired. These declarations do not establish persistence, version-of-terms matching, retries, enforcement or the complete UI/network flow because those implementations are excluded. Acceptance is not checkout or settlement.

> [!warning] Contradiction
> The 23.21.0 raw changelog moves the KYC addition previously labeled 23.17.1 to 23.18.0 and adds the terms-method note under 23.19.0 retrospectively. The earlier retained API/source lacked these terms methods through 23.20.0; this comparison directly observes their 23.20.0 -> 23.21.0 addition. Preserve both immutable history records and the observed boundary without claiming an exact first implementation release. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

### Android `23.22.0` Wallet Contacts and Pre-Authentication Collection

Release notes announce Google Pay/Samsung Pay collection before Link authentication, while crypto payment-token creation still requires a crypto customer. Wallet collection can return contact-only KycInfo for prefill: email, validated E.164 phone and original rawPhone; these fields are not submitted with KYC. This version-qualified native announcement differs from the older headless setup sequence; collection is not checkout, KYC completion or payment success. The retained coordinator is unchanged, and the changed wallet/interactor/model/request implementations are excluded.

Compiled API directly adds KycInfo contact getters/new constructor overloads (old overloads remain), OnrampConfiguration.countryHint, SamsungPayConfig.collectContactInformation and PlatformPayAccountChangedException with StripeCryptoOnrampError getters. Notes call the error recoverable by repeating wallet collection after an account change; exact detection, defaults, hint validation and error/request mapping are unverified. CryptoNetwork.Celo is newly declared without proving serialized value or eligibility. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]]; do not transfer these findings to a React Native version without bridge evidence.

### Android `23.23.0` Presenter Callback Restoration

OnrampCoordinator now receives OnrampCallbackStore. Builder.build updates it with built callbacks, and createPresenter(activity) calls restore() before building launchers that may synchronously deliver pending results. The prior builder wrote directly to global callback references and the prior createPresenter lacked restoration. The store, lifecycle cleanup and component implementations are excluded, so this is observed caller ordering, not proof of delivery after process death or isolation across coordinators.

The new cumulative changelog labels the reused-coordinator/missing-callback fix under 23.22.0, but the retained 23.22.0 coordinator lacked this code. Preserve the later attribution separately from the observed 23.22.0 -> 23.23.0 boundary. Generated AdditionalKycScreen Compose declarations are added without establishing a new supported merchant KYC API. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

### Android `23.24.0` Restricted KYC and Wallet Labels

Experimental OnrampCoordinator.Presenter adds `fulfillKycRequirements()`, explicitly annotated `@RestrictTo(RestrictTo.Scope.LIBRARY_GROUP)`. Its body delegates to the excluded presenter coordinator; its documentation describes collecting/submitting outstanding KYC requirements and delivery through OnrampCallbacks. This is not a supported general merchant entry point, proof of KYC completion, callback delivery, authentication enforcement or a complete document-upload integration. Generated AdditionalKycScreen Compose declarations are replaced by KycScreen declarations without proving feature removal or a new public UI API. [[source-github-stripe-android]]

Release notes announce Google Pay/Samsung Pay card sublabels including Credit, Debit or Prepaid, with Card fallback. That formatting implementation is excluded, and label text does not prove wallet eligibility, funding authorization or successful checkout. Retained build changes add the moved core ApiConfigurationPreview opt-in; Onramp's API 24 floor remains unchanged. The cumulative changelog moves the older Identity/Onramp floor note from 23.15.0 to 23.17.0; preserve previous attributions separately from the observed retained build boundary. All older native/React Native/iOS findings remain version-qualified in [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

### Android `23.25.0` Card Funding Display Declaration

The compiled `PaymentMethodDisplayData` surface adds `getCardFunding(): CardFunding` alongside its existing label, sublabel, icon and type getters. This is display-model API evidence, not proof of its nullability, default value, parsing/formatting behavior, availability on each wallet or a new funding authorization. The model implementation is excluded and retained OnrampCoordinator/build are unchanged. Keep the `23.24.0` wallet-label announcement separate; no new React Native binding or payment capability is inferred. [[source-github-stripe-android]] [[changelog-github-stripe-android]]

## iOS `26.13.0` Alpha Delta

This version-qualified native alpha flow is distinct from the older web/headless setup sequence above. `CryptoOnrampCoordinator.collectPaymentMethod(type:from:)` can present Apple Pay before Link authentication: its platform-client resolver now forwards an optional crypto customer ID instead of rejecting an absent one. Card/bank collection still checks verified Link state, and `createCryptoPaymentToken()` still requires a crypto customer ID. Collection creates a payment source; it does not perform checkout or prove payment success.

`create(..., countryHint: nil)` gains an optional merchant-provided ISO alpha-2 country hint. The coordinator forwards it into platform settings and token creation; documentation says it assists merchant-of-record selection before the customer has an established KYC region and is ignored afterward. Successful registration, token authentication and authorization store the customer ID and clear the cached platform API client; logout also clears that cache. The settings/token API implementations are excluded, so exact backend selection, validation and enforcement are not established.

MainActor `fulfillKYCRequirement(from:)` gets Link account information and delegates to an additional-KYC flow. The caller returns submitted, pendingVerification, canceled or notRequired and logs completion only for the first two. Submission/pending verification is not verified KYC or guaranteed transaction eligibility; result definitions, document/UI/network internals remain excluded.

Release-note-only findings describe optional Apple Pay-derived `KycInfo.email`, normalized E.164 `phone` and original `rawPhone`, all for prefill. Normalization uses the billing country when possible; names fall back to shipping values, and a usable name or billing address is still needed (email/phone alone is insufficient). The changed KycInfo model and announced missingLinkSessionKey error implementation are excluded. No general-availability, country eligibility or runtime guarantee follows. See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

## iOS `26.14.0` Apple Pay Region Revalidation

The alpha coordinator now retains the original Apple Pay context's publishable key and whether collection began without a crypto customer ID. Before creating a token for that pre-auth selection, it fetches current platform settings using the authenticated customer ID. A different publishable key raises `PaymentMethodKYCRegionChangedError` with code `payment_method_kyc_region_changed` before calling token creation. The same customer ID does not imply the same resolved key.

Recover by successfully calling `collectPaymentMethod(type: .applePay(paymentRequest:), from:)` again, then retry token creation. Do not merely loop token creation with the stale selection. The error guidance recommends a matching countryHint or authenticating before Apple Pay collection. This is a version-qualified native alpha flow, not a general Apple Pay payment failure or merchant-eligibility guarantee.

Attempt identity guards ignore late/mismatched completion callbacks; logout clears selection/cache/attempt metadata and resumes a pending Apple Pay continuation as canceled. Only successful wallet completion promotes the pending selection. The supplement closes the error/mapping/selection evidence gap; settings/token request implementation and backend region-selection rules remain excluded. See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

## iOS `26.15.0` Alpha Compatibility and Labels

The native alpha API renames `fulfillKYCRequirement(from:)` to `fulfillKYCRequirements(from:)` and `FulfillKYCRequirementResult` to `FulfillKYCRequirementsResult`. The retained coordinator no longer declares the old method. The supplemental result defines submitted (accepted for asynchronous verification), pendingVerification, canceled and notRequired. Update explicit method/type names, but do not interpret submission or a completed analytics event as completed verification or payment. The delegated document/KYC implementation remains excluded.

Apple Pay preview construction still requires a recognized brand display string and last4. It now forwards `card.funding` to LinkController.formattedCardDetails, which normalizes the value and delegates formatting. Release notes specify Credit/Debit/Prepaid with Card fallback; the final ConsumerPaymentDetails formatter is outside the retained scope. This is display metadata, not funding authorization or merchant eligibility. The 26.14.0 region-recollection contract remains version-qualified history; no new React Native support is inferred from this native update. See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

## Relationship to Other Crypto Products

### Android `23.14.0` Evidence

The retained native API signature adds CryptoNetwork.Tempo. Release notes also announce internal preview API-version pinning; the request/network implementation is excluded, so the enum does not prove its serialized value, enabled networks or merchant eligibility. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]] for version-qualified evidence; this is distinct from the React Native wrapper milestone above.

- [[stripe-stablecoin-payments]] — accepting stablecoin payments on Stripe (different from onramp: onramp helps customers *buy* crypto; stablecoin payments lets merchants *accept* crypto)

## Sources

- [[source-github-stripe-ios]] - native 26.13.0 alpha pre-auth Apple Pay, merchant-of-record hint/cache lifecycle and additional-KYC caller; explicit delegated implementation limits
- [[source-github-stripe-android]] - native 23.14.0 Tempo declaration and explicit request-implementation limits

- [[source-stripe-crypto-onramp]] — May and November 2026 overview of Stripe's merchant-of-record role, three onramp modes, dated preview labels, and application requirement
- [[source-stripe-crypto-onramp-stripe-hosted]] — May/November 2026 hosted-onramp guides: application gate, changeable currency/geography list, frontend URL versus backend session path, and dated Dahlia/Endive script examples
- [[source-stripe-crypto-onramp-embedded]] — Embedded overview: payment methods (credit/debit/ApplePay/ACH), instant delivery, Link, webhooks per status change
- [[source-stripe-crypto-onramp-embedded-quickstart]] — Embedded quickstart: Node.js server, React client, OnrampSession API, events, dark mode, sandbox test values
- [[source-stripe-crypto-onramp-embedded-setup]] — May and November 2026 public-preview widget setup: states, pre-population, estimated quotes and fee total, mobile flow, webhook/errors and session persistence

> [!warning] Contradiction
> Both dated embedded-widget guides show `client_secret` in a mobile URL path but also forbid putting it in URLs because it exposes wallet-address information. The source does not reconcile the example with its own handling rule; treat the URL pattern as an unresolved conflict, not implementation guidance. See [[source-stripe-crypto-onramp-embedded-setup]].

- [[source-stripe-crypto-onramp-embedded-components]] — May 11, 2026 headless quickstart with Link OAuth, setup and checkout flow; November 7 same-URL hub routes to a distinct quickstart and integration guides
- [[source-stripe-crypto-onramp-embedded-components-integration]] — May 2026 full Embedded Components guide for Web, React Native, Android, and iOS, with platform-specific KYC, checkout errors, and LinkAuthIntent APIs; November 7 base URL is a variant index.
- [[source-stripe-crypto-onramp-kyc-integration]] — May and November 2026 Embedded Components KYC guide: tier status/error interpretation and November's mobile Platform Pay pre-auth collection with later identity gates.
- [[source-github-stripe-react-native]] — React Native Tempo typing in `0.73.0`, plus Samsung Pay Onramp collection and wallet-verification error types in `0.75.0`
