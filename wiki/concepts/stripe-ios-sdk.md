---
title: "Stripe iOS SDK"
type: concept
category: framework
tags: [stripe, ios, swift, mobile, sdk, payments, apple-pay, payment-sheet, embedded-payments]
---

## Overview

`stripe-ios` is Stripe's official modular Swift SDK for native iOS payments and adjacent products. The retained history covers the legacy `25.14.0` capsule, the approved `stripe-ios@26.4.1` baseline at commit `d9252fd0a4a6d369fa45bb06f74c4e818c914f91`, and the `26.5.0` delta at `a1ea788163dee511239e2cfefe27cad576f045d3`.

Version `26.4.1` requires iOS 15 or later. Apps that still target iOS 13 or 14 must remain on `25.17.0`. The SDK supports Swift Package Manager and CocoaPods; Carthage binaries continue to be published but are no longer officially tested.

The approved `26.6.0` additive baseline at `3410ff0853b66e5ade3e8763e99f3ddb5dd77bc3` expands retained Checkout implementation while preserving those earlier versions. It does not make the Checkout SPI production-ready.

## Security and fulfillment boundary

Sensitive payment details are sent directly to Stripe instead of passing through the merchant server. The merchant backend still owns secret-key operations, including creating Intents and issuing customer or session credentials.

`PaymentSheetResult.completed` means that the customer completed the SDK payment or setup interaction. The payment may still be processing, so order fulfillment must wait for a successful Stripe payment event. This boundary is especially important when `allowsDelayedPaymentMethods` enables bank debits, vouchers, or methods that require later customer action.

## Module architecture

| Module | Purpose |
| --- | --- |
| `StripePaymentSheet` | PaymentSheet, FlowController, Embedded Payment Element, CustomerSheet, Link, appearance, and payment-method configuration |
| `StripePayments` | Low-level PaymentIntent, SetupIntent, PaymentMethod, token, source, Radar, and next-action APIs |
| `StripePaymentsUI` | Card fields, card forms, and lower-level payment UI |
| `StripeApplePay` | Lightweight Apple Pay integration, including App Clip support |
| `StripeConnect` | Embedded connected-account onboarding, management, payments, payouts, and check scanning |
| `StripeFinancialConnections` | Financial-account collection and token/session results |
| `StripeIdentity` | Native identity-document and selfie verification |
| `StripeIssuing` | Issuing PIN and Apple Wallet provisioning APIs |
| `StripeCryptoOnramp` | Alpha Link, KYC, wallet, payment-method, and crypto-checkout coordination |
| `Stripe` | Umbrella product containing the payment modules and Issuing |

The package manifest also contains internal dependencies such as `StripeCore`, `StripeUICore`, `Stripe3DS2`, and `StripeCameraCore`. Their presence does not make every internal API a supported merchant integration surface.

## Payment UI choices

### PaymentSheet

PaymentSheet provides a prebuilt collect-and-confirm flow. It can load an existing PaymentIntent or SetupIntent client secret or use an intent configuration that asks the merchant backend to create or confirm an Intent after collection. The retained `26.4.1` baseline also exposes Checkout Session initialization; do not treat that as a generally available, complete confirmation contract. In `26.6.0`, the shared confirmation function rejects Checkout intents and directs them to the unfinished `Checkout.confirm` SPI described below.

`PaymentSheet.Configuration` controls merchant display, customer credentials, Apple Pay, Link, appearance, billing and shipping collection, delayed methods, payment-method order, card-brand acceptance, custom methods, and external methods.

### FlowController

FlowController separates payment-option selection from confirmation so the merchant can own the surrounding checkout UI. It exposes sync, callback, and async APIs for creation, option presentation, confirmation, and updates.

### Embedded Payment Element

`EmbeddedPaymentElement` places payment-method selection directly in a UIKit or SwiftUI hierarchy. It supports creation, configuration updates, payment-option display data, clearing selection, and async confirmation. The merchant owns the confirm button and presenting view controller.

### CustomerSheet

CustomerSheet manages saved payment methods. Current configuration covers Customer Session credentials, billing collection, card-brand acceptance, Apple Pay, preferred networks, and card scanning. Customer Sessions replaced the older ephemeral-key-only configuration in the v25 migration.

### Version-qualified `26.5.0` changes

- Standalone Link's top-level `StripePaymentSheet.LinkConfiguration` gains optional billing-details collection overrides; nil preserves the controller's base configuration. It is distinct from `PaymentSheet.LinkConfiguration`. `LinkAppearance` customization becomes accessible through `LinkControllerPreview`, still private preview rather than general availability.
- `PaymentSheet.BillingDetailsCollectionConfiguration` gains a public initializer for collection modes, attaching defaults, and allowed countries.
- Embedded form cancellation reconstructs the last accepted form state. For Checkout-backed saved methods, the retained caller waits for billing-address sync before publishing selection; failure restores the prior selection and displays an error. The sync implementation itself is outside the capsule.
- The SwiftUI Embedded presenter resolves from its own view's window. FlowController cancellation invokes selection-snapshot restoration before publishing the payment option; the excluded restoration helpers prevent a complete claim about all restoration cases.
- Internal Checkout confirmation suppresses `save_payment_method` when `noPaymentRequired` is true and handles a returned SetupIntent before a PaymentIntent. These internal branches alone do not establish public subscription or free-order support.

The newer changelog retrospectively labels multi-scene presentation and Link selection fixes under `26.4.1`. Keep those upstream annotations separate from code differences observed between the retained `26.4.1` and `26.5.0` SHAs. See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]] for exact evidence and exclusions. No Apple Pay integration change is established by the version-only podspec bump.

### Version-qualified `26.6.0` changes

- PaymentSheet adds MB WAY and Bizum. Their retained authorization handlers require a PaymentSheet authentication context and a PaymentIntent, not a SetupIntent or standalone low-level context. Availability and polling UI details remain outside the retained evidence.
- Private-preview `LinkController.present` propagates selection errors, including the release-note-reported no-funding-sources case. Internal collection and FlowController callbacks discard the new error parameter; this is not a universal Link error contract.
- Alpha Crypto Onramp adds `deleteWalletAddress(walletId:)`, using a wallet ID and authenticated Link account information. The actual API request implementation is excluded.
- Checkout confirmation moves into dedicated Checkout helpers. At this exact SHA, the outer `Checkout.confirm` discards the internal result and returns canceled after committing a returned session response. Its Apple Pay branch, Express Checkout button actions, and Shipping Address completion also remain unfinished. Do not use this SPI as a production integration recipe or infer no payment from its canceled result.
- Newly retained session code defines `noPaymentRequired` from payment status and gates billing tax-region updates on automatic tax using billing. These close evidence gaps at `26.6.0`, not retroactively at `26.5.0`.

See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]] for release changes versus collection-scope additions. Older-version findings remain intact; no runtime payment testing was performed.

### Version-qualified `26.7.0` update

The approved delta at `62c2070c57f20b4d632b25fc62780841f8883cc8` adds a PaymentSheet dependency on `StripeFinancialConnectionsLite`. Manual/Carthage users must embed its xcframework; the migration notes require no additional action for CocoaPods/SPM.

`PaymentSheet.LinkConfiguration.Display.walletButtonHidden` keeps Link enabled but hides its button/row, unlike `.never`. Embedded row construction and selection preservation now consult a button-visibility helper. CustomerSheet autocomplete takes the Elements Session endpoint flag directly; the merchant-side STP SPI configuration switch is removed.

Vipps gains typed PaymentMethod models, parameters and serialization. Its handler does not treat `processing` alone as a completed payment flow. Types do not establish merchant eligibility or complete PaymentSheet support. The newly observed beta-header note under 26.6.0 and AddressElement dismissal notes under 26.5.0 are retrospective changelog annotations, not newly introduced 26.7.0 behavior.

Current outer Checkout implementation, Link visibility helper, autocomplete service, and Lite implementation are not retained. The unfinished Checkout finding above remains specific to 26.6.0; this delta neither confirms nor resolves it for 26.7.0. See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]].

### Version-qualified `26.8.0` additive baseline

The approved full additive ingest at `844404116961cb66eb8d67253386b4d564c66e87` preserves older baselines. Checkout confirmation now uses typed Apple Pay, Link and conventional payment-method flows under `CheckoutController`, checks pending/concurrent operations and maps returned session results. The retained supplemental controller reaches that engine; the always-canceled outer result is a historical 26.6.0 finding, not the observed 26.8.0 implementation. The exact first fixed release remains unknown because the 26.7.0 outer controller was excluded.

This remains STP/ReactNativeSDK SPI. Standard `PaymentSheet.confirm` rejects Checkout sessions. The Apple Pay wrapper delegates to excluded `CheckoutApplePayContext`; it does not prove end-to-end wallet behavior or general availability. A succeeded SDK result with a payment status is not settlement proof.

Other retained changes add FPX Agrobank, Bank of China and MBSB mappings; prioritize supplied decline text after 3DS; and pass optional Financial Connections permissions through top-level private-preview `LinkConfiguration`. Low-level Alipay options gain currency/future usage, while Klarna private-preview options distinguish interoperability tokens (PaymentIntent/SetupIntent) from partner confirmation tokens (PaymentIntent only). These additions do not prove automatic PaymentSheet forwarding or merchant eligibility.

The newer changelog retrospectively adds Alipay and horizontal-layout Link notes under 26.7.0 and Klarna notes under 26.5.0. Keep those historical labels separate from code differences observed at the retained 26.7.0 -> 26.8.0 boundary. See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]] for evidence and approved focused-reading limits.

### Version-qualified `26.9.0` additive baseline

The approved full additive ingest at `841b697a9c45a97a36ade02d9184c7d11b927e82` adds API bindings for Kakao Pay, Korean cards, Naver Pay, PAYCO and SeQura. Models and parameters do not establish PaymentSheet availability or merchant eligibility. The low-level handler does not treat `processing` alone as success for these five methods.

Checkout SPI confirmation now handles PaymentIntent before SetupIntent, polls open sessions, and returns `completed(paymentStatus:)` instead of `succeeded(paymentStatus:)`. Polling timeout can continue to client-side response reconstruction after Intent handling; neither timeout nor client completion proves settlement. Manual-approval and orchestration responses fail explicitly. Checkout-specific Embedded/FlowController creation overloads become internal; ordinary Intent-based public creation remains.

> [!info] Version-qualified behavior, not overwritten history
> The SetupIntent-first dispatch and `succeeded` result recorded for 26.8.0 remain historical facts. The 26.9.0 request serializer is excluded, so earlier no-payment-required save suppression is not verified for this release. Changed Apple Pay wrappers/context and other delegated internals also remain evidence gaps; no general-availability or runtime-payment claim follows from this SPI.

Financial Connections adds requested-permission plumbing, not proof of consent or data access. New internal helpers map billing collection settings into Apple Pay contact-field sets, but excluded callers prevent confirming actual wallet-request behavior. See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]] for the approved focused-reading scope, exact evidence, polling limits and compatibility details.

### Version-qualified `26.10.0` delta

Release notes announce PaymentSheet support for Naver Pay, Korean cards, PAYCO and SeQura, distinct from the API bindings recorded for 26.9.0. Availability/form-factory implementation is excluded, so this is release-announcement evidence, not a verified eligibility or end-to-end integration claim.

PaymentIntent automatic mandate inference removes Korean cards and Naver Pay, while retaining Kakao Pay and honoring explicitly supplied mandate data. SetupIntent code is unchanged; do not generalize this change across both Intent types. Financial Connections gains a narrow Onelink branding-override helper, Identity adds SPI branding-header configuration, and Embedded initial row restoration suppresses animation.

The retained Checkout Apple Pay caller passes `shippingAddressRequired: false` into a session-aware helper. Excluded current wallet internals prevent a broader shipping or Express Checkout claim. Arabic (Saudi Arabia) and alpha CryptoOnramp identifier additions are documented announcements. See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]] for the approved focused-reading scope and exact evidence; all earlier versions remain queryable.

### Version-qualified `26.11.0` additive baseline

Checkout SPI adds a confirmation path when the session has no selected payment method, before requiring a PaymentElement. The exact-SHA supplemental controller confirms that its optional element reaches this flow builder. This is not proof of general free-order/subscription support: the branch itself has no zero-amount guard, and backend/request serialization remains outside the evidence.

> [!warning] Version-qualified confirmation change
> Unlike the retained 26.9.0 missing-Intent failure, 26.11.0 allows a response with neither PaymentIntent nor SetupIntent. Completed polling sets session status to complete in this branch, but timeout can still return a completed SDK result while leaving the session open and preserving payment status. This is a source-code finding, not a runtime reproduction or settlement guarantee. Keep server-side payment verification.

Scalapay gains typed API bindings and announced PaymentSheet support; its processing state alone is not success. PaymentIntent inferred-mandate handling removes Kakao Pay while explicit mandate data still takes precedence; do not extend that finding to SetupIntent. The newer cumulative changelog retrospectively adds Kakao Pay PaymentSheet support under 26.10.0, absent from the earlier retained notes.

Link `walletButtonHidden` documentation now permits its button/row for recognized existing Link users, unlike the older unconditional-hiding documentation. Downstream visibility implementation is excluded. Identity adds SPI primary-button styling; Welsh localization is announced. Removing a billing-configuration argument from the Checkout Apple Pay wrapper does not establish that wallet billing collection stops.

See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]] for exact evidence, full-additive focused-reading scope and unresolved delegated implementation. All earlier version knowledge remains intact.

### Version-qualified `26.12.0` additive baseline

Alpha CryptoOnramp adds separate terms-and-conditions and terms-of-service methods. The coordinator retrieves current requirements using Link account information, skips presentation for notRequired, and otherwise presents HTML through Link. Acceptance awaits confirmation using the declaration ID before dismissal; cancellation is distinct, and callback errors propagate. Link's STP result has accepted/canceled, while the coordinator also handles notRequired. Excluded API and HTML-rendering internals prevent backend persistence, idempotency or compliance-completeness claims.

Embedded and FlowController remove their Checkout-specific pending-operation/queue wrappers around shared confirmation. Ordinary update guards remain, and shared PaymentSheet.confirm still rejects Checkout intents. This is not proof of unguarded Checkout payment execution; current outer Checkout/session implementation is excluded, so older supplemental evidence is not current caller proof.

Identity adds SPI secondary-button styling, and SPM adds CryptoOnramp localization resources. Release notes announce public CryptoOnramp Image exposure removal, StripeCore additionalHeaders SPI and a card-scan funding-warning fix; their implementation is excluded. The new card-program-name note under 26.11.0 is a retrospective annotation, not verified first-introduction evidence. See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]] for the approved focused-reading scope, exact evidence and preserved history.

### Version-qualified `26.12.1` additive baseline

Pix gains API bindings and announced PaymentSheet support. The retained handler requires a PaymentSheet authentication context, opens hosted instructions with a Safari fallback and requests polling. The approved exact-SHA supplement shows no countdown, a configured two-second polling interval and API expiry (24-hour fallback); actual requests start after a five-second scheduled delay. Failed/non-success deadline handling completes as canceled, not failed. Neither cancellation nor SDK completion proves the bank-payment outcome.

> [!warning] Pix redirect-return caveat
> The retained redirect-retrieval path exempts only PayNow and PromptPay from cancellation while an Intent still requires action; Pix has no method-specific PollingBudget. A still-pending Pix Intent can therefore reach canceled after returning or dismissing the redirect. This is a code-path risk, not a device reproduction or a claim that every Pix payment fails. Preserve server-side payment verification.

The STP polling protocol changes from PaymentIntent-specific to shared action parameters; custom SPI conformers must adjust. Explicit mandate data wins; automatic Pix inference applies to offSession PaymentIntents and the SetupIntent list. These bindings do not prove every setup, recurring or eligibility scenario; see [[stripe-pix]].

Financial Connections callback/async presentation gains optional preCollectedConsent: a Stripe-issued consent ID and the actual Unix-seconds acceptance timestamp for the complete issued text. Preserve that timestamp across retries. Server evaluation controls whether its consent pane is skipped. On a reused sheet, old overloads do not clear stored evidence; pass nil explicitly through a new overload to reset it. SDK input validation and backend enforcement are different boundaries.

Checkout SPI removes its new-method billing-email fallback from session.email; its no-method customerData email branch remains. Earlier confirmation/timeout cautions still apply, and this does not establish general public Checkout support. CryptoOnramp error-detail preservation and file-upload SPI are later annotations under 26.12.0, not proof of first implementation at that older SHA.

See [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]] for the approved full-additive focused-reading scope, three-file supplement and remaining delegated implementation gaps. All older versions remain intact; no SDK/device/payment testing was performed.

## Apple Pay

`STPApplePayContext` creates a Stripe PaymentMethod from a `PKPayment`, asks the delegate for confirmation details, and reports completion. It supports UIKit, SwiftUI-compatible presentation, async delegate methods, request customization, shipping and coupon changes, and explicit dismissal.

The lightweight `StripeApplePay` module is intended for integrations that do not need the larger payment UI, including App Clips. Apple Pay UI completion remains subject to the same server-side fulfillment boundary as other payment methods.

## Low-level payments and authentication

`STPAPIClient` exposes callback and async operations for:

- creating PaymentMethods, tokens, and legacy Sources;
- retrieving and confirming PaymentIntents and SetupIntents;
- updating PaymentMethods;
- verifying Intents with microdeposits; and
- creating Radar Sessions.

`STPPaymentHandler` confirms Intents and handles redirects, app-to-app flows, and native 3DS2 authentication through an `STPAuthenticationContext`. Its modern method names use `confirmPaymentIntent`, `confirmSetupIntent`, and `handleNextAction`; older generic names remain deprecated aliases.

The retained source models many payment-method bindings, but a public enum or model does not prove that a method is enabled for a particular merchant, country, currency, Intent mode, or connected account.

## Specialized products

### Connect

`EmbeddedComponentManager` creates account onboarding, account management, payment details, notifications, payouts, payments, and check-scanning components. Payments and Payouts became public API in `26.3.0`; merchant availability and server-created access credentials must be verified separately.

### Financial Connections and Identity

`FinancialConnectionsSheet` returns session or token-oriented results from a server-created Financial Connections Session client secret. `IdentityVerificationSheet` presents native verification from a server-created Verification Session client secret. Neither client surface replaces backend creation or result verification.

### Crypto Onramp

The alpha `CryptoOnrampCoordinator` supports Link account discovery and authentication, KYC, compliance identifiers, user attestation, wallet registration and ownership verification, payment-method collection, crypto payment-token creation, and checkout. Alpha and preview APIs must not be represented as generally available.

### Issuing

`STPPushProvisioningContext` supports adding Issuing cards to Apple Wallet. `STPPinManagementService` remains available but is deprecated in favor of Issuing Elements.

## Platform and migration history

| Version | Important boundary |
| --- | --- |
| `26.12.0` | Alpha partner-terms flows and announced Image API removal; scoped confirmation-wrapper cleanup, Identity styling and retrospective card-program-name note |
| `26.11.0` | Checkout SPI no-method/missing-Intent confirmation changes and timeout warning; Scalapay bindings/support announcement; revised Link visibility documentation |
| `26.10.0` | Announced PaymentSheet Naver Pay/Korean cards/PAYCO/SeQura; PaymentIntent-only mandate inference change; scoped branding, Identity and rendering updates |
| `26.9.0` | Five new payment-method API bindings; Checkout SPI polling, completion and creation-visibility changes; client completion is not settlement |
| `26.8.0` | CheckoutController SPI confirmation baseline with Apple Pay evidence gap; FPX additions, decline text fix, preview Link permissions and low-level Alipay/Klarna options |
| `26.7.0` | Financial Connections Lite migration; hide Link button without disabling Link; autocomplete flag changes; typed Vipps support with explicit evidence limits |
| `26.6.0` | MB WAY/Bizum PaymentSheet support; preview Link error propagation; alpha wallet deletion; expanded but unfinished Checkout SPI evidence |
| `26.5.0` | Private-preview Link billing/appearance configuration; retained selection and Checkout confirmation changes; release-note-only alpha Tempo wallet-address registration |
| `26.4.1` | Fixes some successful Alipay payments being incorrectly reported as failures |
| `26.4.0` | Makes `STPAPIClient.betas` public for preview API-version flags |
| `26.3.0` | Adds alpha wallet-ownership verification, private-preview standalone Link APIs, and public Connect Payments/Payouts components |
| `26.0.0` | Raises the minimum deployment target from iOS 13 to iOS 15 |
| `25.17.0` | Last documented release for iOS 13 and 14 |
| `25.0.0` | Adds async APIs broadly, makes Customer Sessions and Confirmation Tokens generally available, and removes several deprecated payment APIs |
| `25.14.0` | Legacy wiki baseline retained for historical queries |

The exact `26.4.1` patch is narrow. Broader architecture and migration findings come from the complete retained `26.4.1` capsule and cumulative changelog, not from that patch note alone.

## App Store boundary

The SDK README states that digital products or services consumed inside the app, including subscriptions, game currency, premium content, and feature unlocks, must use Apple's in-app purchase APIs. Stripe can process other eligible payment scenarios. Current Apple policy and regional exceptions still require separate verification.

## Sources

- [[source-github-stripe-ios]] - cumulative GitHub source for `stripe/stripe-ios`
- [[changelog-github-stripe-ios]] - package-qualified release history
- [[source-stripe-billing-ios-sdk]] - separate private-preview BillingSDK with buy buttons, entitlements, and customer portal APIs
- [[stripe-android-sdk]] - native Android counterpart
