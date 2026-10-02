# C27 fixed query audit — Group C

Verdict: **PASS, 4/4 fixed questions**. Read-only snapshot audit; no live-support or payment-execution claim.

## tokenization-key-android-v5

1. **Where is Android v5 tokenization-key authorization documented?**
   - Actual route/page: `wiki/index.md` → `wiki/braintree-index.md:322` → `wiki/concepts/braintree-android-sdk.md:43` → `wiki/sources/braintree/source-braintree-authorization-tokenization-key-android-v5.md` → `raw/braintree/docs/guides/authorization/tokenization-key/android/v5-2026-09-16.md`.
   - Object/action match: Android v5 client-SDK tokenization-key authorization, not merchant OAuth.
   - Direct answer: the promoted **Braintree Tokenization Keys (Android v5)** guide, canonical URL `https://developer.paypal.com/braintree/docs/guides/authorization/tokenization-key/android/v5`.
   - Exact locator: raw lines 1, 7, 14, 24-28; source `Overview`, frontmatter and `Raw Sources`. **PASS**.

2. **What is the key's stated role, scope and consequential limitations?**
   - Same actual route/page; object/action is client authorization to tokenize payment information, not transaction authorization or completed vaulting.
   - Direct answer: static reduced-privilege, publishable credential, reusable across apps; multiple labeled keys and revocation deauthorizing clients. Lists credit cards, PayPal, Venmo, Apple Pay and Google Pay. Only tokenization: no customer ID, merchant account ID or other configuration; no direct client Vault save, Drop-in saved-method retrieval, or 3DS transaction. Save via nonce handoff to server or customer-scoped client token. Possible Account Admin permission for insufficient-privilege errors. Bound to one environment; production key reaches live Braintree regardless of debug/environment variables. Initialize before payment UI for configuration fetch. Preserve the broad “any Android/iOS SDK version” statement alongside the historical March 30, 2026 certificate warning, Android 4.45.0+/5.0.0+ upgrade targets and conditional total-traffic failure unless old app versions are decommissioned/force-upgraded; not current support evidence.
   - Exact locators: raw `Tokenization Keys` 24-28; `Static` 31-37; `Reduced privilege` 40-49; `Adding a tokenization key to your app` 65-77; `Initializing the SDK` 82-86; `IMPORTANT` 17-20. Source `Key takeaways`, warning and `Detail locators` preserve these boundaries. **PASS**.

## tokenization-key-ios-v7

3. **Where is iOS v7 tokenization-key authorization documented?**
   - Actual route/page: `wiki/index.md` → `wiki/braintree-index.md:323` → `wiki/concepts/braintree-ios-sdk.md:60` → `wiki/sources/braintree/source-braintree-authorization-tokenization-key-ios-v7.md` → `raw/braintree/docs/guides/authorization/tokenization-key/ios/v7-2026-09-16.md`.
   - Object/action match: iOS v7 client-SDK tokenization-key authorization, not merchant OAuth.
   - Direct answer: the promoted **Braintree Tokenization Keys (iOS v7)** guide, canonical URL `https://developer.paypal.com/braintree/docs/guides/authorization/tokenization-key/ios/v7`.
   - Exact locator: raw lines 1, 7, 14, 20-24; source `Overview`, frontmatter and `Raw Sources`. **PASS**.

4. **What is the key's stated role, scope and consequential limitations?**
   - Same actual route/page; object/action is client authorization to tokenize payment information, not transaction authorization or completed vaulting.
   - Direct answer: this variant independently states static reduced privilege, indefinite reuse, multiple labeled keys, revocation, publishability and possible Account Admin permission. Lists the same five methods. Restricts clients to tokenization, with no customer ID, specific merchant account ID, other configuration, direct client Vault save, Drop-in saved-method retrieval, or 3DS transaction; server nonce handoff/customer-scoped client token are the stated alternatives. Each key fixes its environment; production remains live despite debug/environment variables. Initialize before UI for configuration fetch. Its “any Android/iOS SDK version” statement is in tension with its historical March 30, 2026 certificate notice and iOS 6.17.0+ target, including conditional total-traffic failure for retained old app versions. Do not infer current iOS v7 support or GitHub parity from this snapshot.
   - Exact locators: raw `Tokenization Keys` 20-24; `Static` 27-33; `Reduced privilege` 36-45; `Adding a tokenization key to your app` 61-71; `Initializing the SDK` 74-84; `IMPORTANT` 17-18. Source `Key takeaways` and `Detail locators` retain the version/certificate tension. **PASS**.

## Shared evidence and navigation notes

- Full pinned raw reads: Android lines 1-87 and iOS lines 1-84. SHA-256 matches manifest: Android `ac3ab39ca6e15cf76b30ccab94c1f6b9a0590a77b2f79a0e732601094bd9a355`; iOS `09e0ea24bc483079095e00be87edbfdc7093f198200e2f2e8552997b38b5fd83`.
- Scoped filename gap sweep found the authorization overview, JavaScript tokenization-key variant, and Android/iOS setup/migration raws. Neither promoted source has a `Related raw API references` section. No extra raw full reads were needed: the two selected pages directly answer all four fixed questions. Other variants/historical evidence were not borrowed to infer parity.
- Reciprocal concept/source links exist for both selected pages; each source's `raw_files` and `Raw Sources` resolve to the exact selected raw. Direct source catalog entries were absent at observation time while coordinator aggregation was ongoing; the required index → concept → source route already worked. No query gap or correction required.
- Analysis-end UTC: 2026-10-02 12:30:37 UTC.
