# C29 fixed query audit B

Verdicts: **4/4 PASS**. Repository read-only; no filing, promotion, catalog or count edits.

## Android v5 navigation — PASS

`[[index]]` → `[[braintree-index]]` → `[[braintree-3d-secure]]` (Sources) → `[[source-braintree-3d-secure-advanced-options-android-v5]]` → its `raw_files` / Raw Sources → `raw/braintree/docs/guides/3d-secure/advanced-options/android/v5-2026-09-16.md`. The source records canonical URL `https://developer.paypal.com/braintree/docs/guides/3d-secure/advanced-options/android/v5`. Root/provider indexes expose the concept route; direct new-source catalog aggregation remains coordinator-owned.

## Android v5 details — PASS

`[[source-braintree-3d-secure-advanced-options-android-v5]]` supplies central meaning, material warnings and located detail routes, all verified against the complete 426-line pinned raw:

- Liability flags guide UI flow, not trusted server risk decisions; accepting advanced-risk outcomes can retain fraud liability. Failed authentication permits nonce use only with suitable server risk policy and server `required=false`; another method is a card-brand recommendation. Both flags false permits a transaction without shift; SafeKey shift can later be revoked. Server nonce/transaction 3DS information is a separate reporting route (Liability shift, lines 17–247).
- Vaulted-card verification starts with a server-created nonce from the stored token (249–296). Brazilian domestic combo-card selection propagates `accountType` into `verifyCard()` and the corresponding transaction/payment-method/customer call (301–316). The challenge heading at 298 has no captured explanatory body: do not infer an Android challenge parameter from it.
- Google Pay 3DS applies to accessible-PAN non-network-tokenized cards, not DPAN cards. Custom UI supplies `GooglePaymentCardNonce` and checks network tokenization; requested Drop-in 3DS automatically processes eligible cards. The captured Drop-in notice gives deprecated July 14, 2025 / unsupported July 14, 2026, potential suspension and migration to Braintree SDK; this is not present modular Android package support proof (318–363).
- SCA exemptions are issuer-discretionary, never guaranteed, and retain merchant liability. Captured low-value conditions are <30 EUR, at most five consecutive exemptions, and SCA after >100 EUR cumulative since last SCA. TRA is <250 EUR, based on acquirer fraud rate over 90 days and not enabled by default. Distinguish `Transaction.sale().scaExemption` from `verifyCard().requestedExemptionType`; sale-time requests do not override normal 3DS rejection logic; unmet authentication-time conditions fall back to standard authentication (365–397).
- Data-only seeks improved authorization rates without liability shift; captured scope is Mastercard/Maestro and Visa on select processors, not PSD2 countries, with Control Panel merchant/card-brand support check. `dataOnlyRequested` or Rules Manager flags it; unsupported combinations fall back and `verifyCard()` remains necessary. US DCAP route asks for device ID, IP, billing address and email (400–416).
- Visa DAF establishes a credential through issuer step-up, lasting up to two years; same-instrument/same-merchant follow-ups **should**, not must, be frictionless with full shift. PSD2 requires acquirer TRA; captured regional restrictions and acquiring-bank eligibility confirmation apply; request via `requestVisaDAF` (419–425).

All statements are Android v5-routed **2026-09-16 snapshot** statements; authentication/nonce information does not establish authorization, capture, settlement, payment completion or current merchant eligibility.

## iOS v7 navigation — PASS

`[[index]]` → `[[braintree-index]]` → `[[braintree-3d-secure]]` (Sources) → `[[source-braintree-3d-secure-advanced-options-ios-v7]]` → its `raw_files` / Raw Sources → `raw/braintree/docs/guides/3d-secure/advanced-options/ios/v7-2026-09-16.md`. Canonical URL: `https://developer.paypal.com/braintree/docs/guides/3d-secure/advanced-options/ios/v7`. The relevant platform concept is linked separately, not used as exact API authority.

## iOS v7 details — PASS

`[[source-braintree-3d-secure-advanced-options-ios-v7]]` exposes central qualifications and complete detail locators, verified against the full 334-line pinned raw:

- Liability/UI-only/server-risk boundary, failure alternative with server `required=false`, ineligible-card no-shift path and SafeKey revocation are stated here independently (17–229); authentication is not payment authorization or completion.
- Server-generated nonce from vaulted token is passed to client `startPaymentFlow:completion:` (231–276). `challengeRequested=true` on `BTThreeDSecureRequest` requests an issuer challenge, not guarantees one (277–279). Domestic Brazilian combo-card account choice must flow into `accountType` and corresponding server operation (280–290).
- Issuer-discretionary SCA exemptions retain merchant liability. Same captured low-value (<30 EUR, five consecutive, >100 EUR cumulative) and TRA (<250 EUR, 90-day fraud basis, opt-in support) qualifications apply. Sale-time `scaExemption` versus authentication-time `requestedExemptionType` are distinct, normal 3DS logic is not overridden, and unmet conditions fall back (292–312).
- Data-only is frictionless/no shift, seeks better authorization rates, and has Mastercard/Maestro/Visa, selected-processor, non-PSD2 and merchant-account support qualifications. Unsupported combinations fall back; Rules Manager flagging still requires `verifyCard()`; DCAP has eligible-US data routes (313–329).
- Visa DAF has issuer-step-up, up-to-two-year credential, qualified **should be frictionless** wording, same-merchant/instrument condition, PSD2/acquirer-TRA prerequisite, regional exclusions and acquiring-bank eligibility check, requested via `requestVisaDAF` (332–334).

These are iOS v7-routed **2026-09-16 snapshot** statements, not current package compatibility/support, merchant eligibility or execution proof. Android Google Pay/Drop-in content is not transferred to this iOS answer.

## Hash / gap report

Both selected source pages and raws read completely. Computed SHA-256 matches C29 manifest pins:

- Android: `523b5dcbba910bf51cc9b7367786d4c74a9c51fdd6021b92b52978f7f26968e3`.
- iOS: `746fa3d198848248261a89e39bbcb213c83888118ff25e927d384dab76560d28`.

Bounded filename sweep inspected 3DS advanced-options / Rules Manager and Android/iOS Google Pay configuration paths; Android source Related raw API references also inspected. No additional raw is needed for these snapshot-purpose questions. Related configuration, Rules Manager and lifecycle pages remain unread navigation, not factual evidence. No reusable missing-source promotion needed. Android challenge-body absence is a captured-evidence limit, not proof the platform lacks challenge support. No blocking route or retained-claim conflict found. Routine inventories stay in raw locators.

analysis_end_utc: 2026-10-02 15:31:16 UTC
