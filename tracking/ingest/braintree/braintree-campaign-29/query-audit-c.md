# C29 fixed query audit — group C

Result: **4/4 PASS**. Snapshot answers only; no live eligibility, SDK support, execution, or payment-completion claim. Repository remained read-only.

## Android v5 navigation — PASS

`[[index]] → [[braintree-index]] → [[braintree-3d-secure]] → [[source-braintree-3d-secure-rules-manager-android-v5]] → raw/braintree/docs/guides/3d-secure/rules-manager/android/v5-2026-09-16.md`.

The promoted concept's Sources entry reaches the guide. The provider catalog reaches that concept; a direct new source catalog row is coordinator-owned. Canonical URL and pinned raw identify the Android v5 route, not an installed SDK version. The guide's operational UI route is Control Panel → gear → Fraud Management → 3D Secure Rules → Options (raw lines 64–70).

## Android v5 detail — PASS

Merchant policy creation, modification, priority, criteria and merchant-account assignment belong in the Control Panel. No-developer-work setup is conditional on already integrating Braintree 3DS 2 (17–29). The collected automatic Sandbox/Production enablement statement concerns Rules Manager, not proof of account enrollment or compatibility (57–61).

Multiple rules per ruleset and multiple merchant accounts per ruleset are allowed, but an account has only one ruleset; evaluation occurs during `verifyCard()` (61). Only the higher-priority matching rule applies; request parameters `challenge_requested` or `requested_exemption_type` override a match (111–113). Criteria cover amount, method, issuing country, BIN and iOS/Android/Web platform (128–160), not native-version parity.

Actions apply 3DS, request a challenge, request low-value/TRA exemptions, skip where applicable, or use Data Only. Issuers control whether a requested challenge occurs; low-value exemption is described for below 30 EUR/GBP; granted exemptions lack liability shift and TRA requires qualification. Skip has no effect in PSD2-regulated markets; elsewhere it forfeits 3DS benefits and yields `skipped_due_to_rule` before separate transaction sale. Data Only lacks liability shift (142–150). None establishes authorization, capture or settlement.

Custom fields are defined/selected in Control Panel and matched against values supplied through `verifyCard()`; Java uses `ThreeDSecureRequest.setCustomFields`, Kotlin a request `customFields` map (163–230). Android's retry example uses `retry_transaction` but its prose names `retryTransaction` (239, 247, 255): unresolved snapshot spelling discrepancy, not a verified working contract. Geographic grouping and continued monitoring are recommendations, and business-objective expected outcomes are examples rather than guarantees (75, 296–343). Citation: [[source-braintree-3d-secure-rules-manager-android-v5]].

## JavaScript v3 navigation — PASS

`[[index]] → [[braintree-index]] → [[braintree-3d-secure]] → [[source-braintree-3d-secure-rules-manager-javascript-v3]] → raw/braintree/docs/guides/3d-secure/rules-manager/javascript/v3-2026-09-16.md`.

The promoted concept reaches the distinct JavaScript guide. Its canonical URL/raw identity is JavaScript v3-routed documentation, not native SDK support or parity. Operational UI route: Control Panel → gear → Fraud Management → 3D Secure Rules → Options (64–70).

## JavaScript v3 detail — PASS

Control Panel owns rule administration; the no-extra-developer-work statement assumes an existing Braintree 3DS 2 integration (17–29). The snapshot says Rules Manager is enabled in Sandbox/Production; it does not demonstrate a specific merchant's live configuration (57–61). Multiple prioritized rules may belong to one ruleset, multiple accounts may share it, and each account has only one ruleset evaluated on `verifyCard()` (61). Higher priority wins; `challenge_requested` or `requested_exemption_type` overrides a matched rule (109–111).

Criteria cover amount, method, country, BIN and iOS/Android/Web platform without proving native-version parity (126–158). Apply/challenge/exemption/skip/Data Only actions retain the issuer-controlled challenge, below-30-EUR/GBP low-value condition, TRA qualification, no liability shift for granted exemptions/Data Only, PSD2 skip ineffectiveness, and skipped-rule status before transaction sale (140–148). Rule matching and 3DS authentication are not authorization, gateway acceptance, capture, settlement or funding.

Control Panel custom fields must match values sent under JavaScript `verifyCardParams.customFields` (161–216). Retry code says `retry_transaction`, prose `retryTransaction`; do not infer an assured spelling (222–225). Geographic grouping, monitoring and maintenance are recommendations; business examples are not guaranteed conversion/compliance/liability outcomes (75, 253–318). Citation: [[source-braintree-3d-secure-rules-manager-javascript-v3]].

## Evidence, hashes and bounded gap sweep

Both promoted sources and both pinned raws were read completely. SHA-256 values match the C29 manifest:

- Android: `bfeba437865be45da72e8065c673eb4ce5d8622724f9449d4736944c331128f4`.
- JavaScript: `b69abb682f53e143db064f252fe5900ab0635096024bfb45ff25a0691333efd9`.

Bounded filename sweep selected only the Rules Manager topic and related overview/custom-field candidates. The two pinned raws answered the fixed questions; overview and custom-field article were not needed and remain unread navigation, not evidence. No new promotion, collection, catalog/count mutation or full concept semantic re-audit was performed. Android retry-name mismatch is visible in fully read raw and explicitly qualified above; its purpose-fit source does not summarize that routine example discrepancy, but retains the relevant raw locator. No blocking query gap.

analysis_end_utc: 2026-10-02 15:31:25 UTC
