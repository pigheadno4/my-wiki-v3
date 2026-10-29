---
title: "GitHub changelog: braintree/braintree_php"
type: source
date_ingested: 2026-08-19
date_updated: 2026-10-29
original_format: github-repo
raw_files:
  - "github/braintree/braintree_php/snapshots/2026-10-29-b116668/manifest.json"
  - "github/braintree/braintree_php/snapshots/2026-10-29-883a219/manifest.json"
  - "github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/manifest.json"
  - "github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/manifest.json"
tags: [braintree, php-sdk, server-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree_php`. Cumulative implementation knowledge belongs in [[source-github-braintree-php]] and the linked immutable snapshots.

## `braintree_php@6.40.0` (ingested 2026-10-29)

- From 6.39.0, exact SHA `b116668cb1c66b10aceb71e7753a49fbf4e44fd6`; approved focused-reading delta after terminal completion of 6.39.0. Manifest October 27 timestamp is tag/commit-derived; no GitHub Release-note body.
- Declares SignatureService's existing public key/digest properties and allows Error\Validation dynamic properties to avoid PHP 8.2+ deprecation notices. Signing/digest logic and validation extra-key conversion/getters remain unchanged. ACH mandate has only a future-major review comment; no removal or new payment API.
- Composer minimum stays PHP >=7.3.0. README tested branches become 7.4/8.2/8.3/8.4/8.5; it recommends latest-patch 8.4/8.5 and reports patched minimum versions 8.2.35/8.3.36/8.4.27/8.5.12 in a new runtime advisory. Advisory/CVE claims are attributed to upstream, not independently assessed. SDK installation is not an interpreter security patch.
- Migration: address runtime patching independently from SDK adoption, and distinguish declared compatibility from tested/recommended runtimes. No PHP compatibility/exploit/gateway/payment execution performed. All 6.37.0/6.38.0/6.39.0 history preserved.
- Six modified/220 unchanged retained files; 33 upstream dispositions (six retained/27 exclusions), no gaps/unclassified changes. All changed source/content and affected prior files read, 452 file identities checked; old changelog tail identical. Concept first, then cumulative source/company/catalog/logs; source_count unchanged.

Evidence:
- `raw/github/braintree/braintree_php/snapshots/2026-10-29-b116668/manifest.json`
- `raw/github/braintree/braintree_php/releases/braintree_php/6.40.0/2026-10-29/manifest.json`
- `tracking/github/repos/braintree/braintree_php/comparisons/braintree_php/6.39.0--6.40.0/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-braintree-php]] - exact source paths, five located quotes and runtime-advisory limits

## `braintree_php@6.39.0` (ingested 2026-10-29)

- From 6.38.0, exact SHA `883a2199aad6f3e1e4796d0f3bea6725c981fd85`; approved serial delta with focused reading. Manifest October 19 timestamp is tag/commit-derived, not verified GitHub Release publication; no release-note body.
- Adds static/gateway `reverse()` and `reverseNoValidate()`: one reverse POST, validated ID/options, optional `apiRequestKey`, gateway-selected void/full refund. No amount for partial refund or local fallback. `reverseNoValidate()` still validates through `reverse()` and unwraps success or throws `ValidationsFailed`, rather than returning a failed validation result as its docblock suggests.
- Adds `previousMastercardTransactionLinkId` to transaction and static card-verification signatures, plus five error constants. Static verification enforces its signature; the unchanged direct gateway create does not invoke that wrapper check. No new card/customer fields or general merchant enablement inferred.
- Migration: choose result versus exception-style handling deliberately; retain explicit refund for amount-specific operations and confirm gateway reversal/external-vault eligibility independently. Existing runtime, credentials, client-token, webhook and 6.37.0/6.38.0 history preserved. No PHP/gateway/payment execution.
- Six modified/220 unchanged retained files; 11 upstream dispositions, no gaps/unclassified changes. All changed implementation and affected prior context read; 452 snapshot identities and unchanged changelog tail verified mechanically. Updated existing concept first, then source/company/index/logs; source_count unchanged.

Evidence:
- `raw/github/braintree/braintree_php/snapshots/2026-10-29-883a219/manifest.json`
- `raw/github/braintree/braintree_php/releases/braintree_php/6.39.0/2026-10-29/manifest.json`
- `tracking/github/repos/braintree/braintree_php/comparisons/braintree_php/6.38.0--6.39.0/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-braintree-php]] - exact source paths, five located quotes and implementation limits

## `braintree_php@6.38.0` (2026-09-16)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree_php` | `6.37.0` | `6.38.0` | `2a97c3d516a1ee66e710db8140a835d79789627a` | Delta |

**Important findings:** Extended the existing path-segment helper across 14 gateway classes; added settlement `shipping`/`shippingAddressId` (also inherited by partial settlement), ACH-type search/constants, explicit refund `surchargeAmount` acceptance, and validation constant `TRANSACTION_SURCHARGE_NOT_ON_ORIGINAL_SALE` (`97605`). Nineteen retained files changed; 207 remained unchanged. Package metadata and the shared helper are unchanged.

**Developer or merchant impact:** Affected operations can reject invalid path IDs locally, before HTTP dispatch. The helper requires strings with ASCII letters/digits/underscore/hyphen; some validators also reject `"0"` via PHP `empty()`. Exception handling is method-specific: private ID validators use `InvalidArgumentException`, while new inline checks use `Braintree\Exception\NotFound`. TransactionLineItem's previous lowercase-only allowlist is broadened, not narrowed. Subscription `retryCharge()` and other body-ID use are not universally covered.

**Migration action:** Audit trusted ID types and exception handling; do not sanitize rejected IDs into a different identity. Supply settlement additions through the third argument and refund additions through an options array. ACH search uses `TransactionSearch::achType()->is(Transaction::ACH_TYPE_SAME_DAY)` or `.in()` with the supported constants. Optional request fields do not establish gateway acceptance, payment-method enablement, settlement speed or refund success.

**Updated source sections:** Additive `6.38.0` findings, evidence boundary and raw inventory; PHP version boundary in [[braintree-server-sdk]]; company status, provider index and logs. The complete `6.37.0` baseline and its release entry remain preserved.

**Evidence boundary:** Empty upstream release-note body; findings come from the exact repository changelog and retained implementation diff. User-approved focused reading fully covered changed implementation, affected prior code and helper/search dependencies, with 452 snapshot hash/size checks and unchanged changelog history verified mechanically. Tests/fixtures excluded by policy. Ingested 2026-10-11; no live gateway or application execution.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree_php/releases/braintree_php/6.38.0/2026-10-10/manifest.json`
- Empty release-notes record: `raw/github/braintree/braintree_php/releases/braintree_php/6.38.0/2026-10-10/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/manifest.json`
- Prior snapshot manifest: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/manifest.json`
- Comparison: `tracking/github/repos/braintree/braintree_php/comparisons/braintree_php/6.37.0--6.38.0/comparison.json`
- Comparison reading: `tracking/github/repos/braintree/braintree_php/comparisons/braintree_php/6.37.0--6.38.0/comparison.md`
- Patch: `tracking/github/repos/braintree/braintree_php/comparisons/braintree_php/6.37.0--6.38.0/diff.patch`
- Changelog: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/CHANGELOG.md`
- Unchanged helper: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/lib/Braintree/Util.php`
- Transaction signature and dispatch: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/lib/Braintree/TransactionGateway.php`
- Search: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/lib/Braintree/TransactionSearch.php`
- Constants: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/lib/Braintree/Transaction.php`
- Validation codes: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/lib/Braintree/Error/Codes.php`
- Subscription checks: `raw/github/braintree/braintree_php/snapshots/2026-10-10-2a97c3d/files/lib/Braintree/SubscriptionGateway.php`

## `braintree_php@6.37.0` (2026-08-05)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree_php` | Initial baseline | `6.37.0` | `0f53ece38397c9fed05b94620634a5a23ef8ee48` | Full |

**Important findings:** Fixed path traversal in Address and Dispute gateway paths by rejecting path separators and relative segments; added PayPal account email validation codes `92963` and `92964`; added `preferredPaymentMethodToken` to client-token generation.

**Developer or merchant impact:** Applications receive explicit codes for malformed or excessively long PayPal email addresses. Server integrations can generate client-token context for a preferred vaulted payment method. The path validation is a security hardening change for applications that pass external IDs into affected gateway methods.

**Migration action:** No mandatory migration is documented. Upgrade to an active release for security coverage, avoid transforming rejected IDs to bypass validation, and treat the new client-token field as optional until the corresponding client experience is confirmed.

**Updated source sections:** Evidence boundary; client tokens, nonces, and vaulting; webhooks, errors, and security; exact release findings; Braintree company and provider index.

**Evidence boundary:** This is the first retained Braintree PHP baseline, so no prior exact-SHA comparison exists. The upstream release-note record has no body; patch findings come from the retained repository changelog. Broader server behavior in the source page is cumulative `6.37.0` implementation knowledge, not a list of changes introduced by this release.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree_php/releases/braintree_php/6.37.0/2026-08-19/manifest.json`
- Empty release-notes record: `raw/github/braintree/braintree_php/releases/braintree_php/6.37.0/2026-08-19/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/manifest.json`
- Repository changelog: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/CHANGELOG.md`
- Client-token implementation: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/ClientTokenGateway.php`
- Address path validation: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/AddressGateway.php`
- Dispute path validation: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/DisputeGateway.php`
- Validation codes: `raw/github/braintree/braintree_php/snapshots/2026-08-19-0f53ece/files/lib/Braintree/Error/Codes.php`
