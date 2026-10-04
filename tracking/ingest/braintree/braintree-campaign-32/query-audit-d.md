# C32 Query Audit D — 8/8 PASS

- Campaign: `braintree-campaign-32`
- Approved group: D
- Mode: query audit only; no ingest/review and no repository edits
- Prompt path: `/root/c32_audit_d`

## `extend-forward-api-transformations` — 2/2 PASS

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-forward-api]]` → `[[source-braintree-extend-forward-api-transformations]]` → `[[raw/braintree/docs/guides/extend/forward-api/transformations-2026-09-16]]`.

1. **Q1 — PASS.** The exact object is the collected Braintree Extend **Forward API Transformations** webpage, an unversioned guide at canonical URL `/braintree/docs/guides/extend/forward-api/transformations`, pinned to `raw/braintree/docs/guides/extend/forward-api/transformations-2026-09-16.md`. The source title, canonical URL and sole `raw_files` owner are at source lines 2–8; raw provenance, title and slug are at raw lines 1–10. Manifest SHA-256: `5327197255a952a641504e390ee54bfccf0c68c16898e177d76acf68da56f67d` (verified).
2. **Q2 — PASS.** Its central purpose is ordered request construction: config transformations insert payment-method/caller data into `/body`, `/header`, `/urlparam`, or temporary `/var`, with a strict DSL and content-type/path semantics. Production Forward API use is eligibility-gated; PAN/CVV and username/password examples contain sensitive data; the transformations do not establish destination authority, credential validity, request acceptance, payment authorization/capture, settlement, payout, or funding. Exact evidence: raw lines 16–19, 30–55, 94, 97–120; source answer/qualifications at lines 14, 18–32 and locators at 36–41.

## `extend-forward-api-cryptography` — 2/2 PASS

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-extend-forward-api-cryptography]]` → `[[raw/braintree/docs/guides/extend/forward-api/cryptography-2026-09-16]]`.

1. **Q1 — PASS.** The exact document is the collected unversioned Braintree **Forward API Cryptography** guide at canonical URL `/braintree/docs/guides/extend/forward-api/cryptography`, pinned to `raw/braintree/docs/guides/extend/forward-api/cryptography-2026-09-16.md`. The source title, canonical URL and sole `raw_files` owner are at source lines 2–8; raw provenance, title and slug are at raw lines 1–10. Manifest SHA-256: `7e07246bbea037ec19ed5af9bd1280f5b6c102315816aecf03fa62db588cbea4` (verified).
2. **Q2 — PASS.** Its central purpose is the Forward API toolkit for encrypting or signing parts of an outgoing request. The guide says card data emitted by Forward API is already TLS-protected, but some destination APIs **may require further security**; therefore destination-dependent encryption/signing is not characterized as universally optional. It documents AES-GCM, RSA public-key encryption and certificate-based mutual TLS. AES keys and mutual-TLS private keys are sensitive and are to be PGP-encrypted before submission for configs; sandbox can pass PEM client certificate/key per request, while production loads them with the config if necessary. Production use remains eligibility-gated, RSA output is non-deterministic, and examples do not prove delivery, destination acceptance, or payment execution. Exact evidence: raw lines 16–22, 25–39, 67–122 and 204–206; source answer/qualifications at lines 14, 18–28 and locators at 32–39.

## `extend-forward-api-pgp-key` — 2/2 PASS

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-forward-api]]` → `[[source-braintree-extend-forward-api-pgp-key]]` → `[[raw/braintree/docs/guides/extend/forward-api/pgp-key-2026-09-16]]`.

1. **Q1 — PASS.** The exact document is the collected unversioned **Braintree Forward API PGP Public Key** retrieval page at canonical URL `/braintree/docs/guides/extend/forward-api/pgp-key`, pinned to `raw/braintree/docs/guides/extend/forward-api/pgp-key-2026-09-16.md`. The source title, canonical URL and sole `raw_files` owner are at source lines 2–8; raw provenance, title and slug are at raw lines 1–10. Manifest SHA-256: `1c2aa87357276aa02a5f326c10ea431f3934bc5ca71378904ed4f69fd5e4acf1` (verified).
2. **Q2 — PASS.** Its actual purpose is to publish the public key used to encrypt secrets sent during communication with the Forward API team. The snapshot names **PayPal Braintree Forward API**, email `forward-api@getbraintree.com`, a 4096-bit RSA PGP key, key ID `D26C77FA`, and fingerprint `8BE6 69D2 D1ED 9DCA B4B5 E0E8 85D1 D4A4 D26C 77FA`; production Forward API use remains eligibility-gated. The page supplies no expiry, rotation, revocation, or present-trust validation, so the recorded name/fingerprint and immutable snapshot do **not** establish that the key is current or trusted. Exact evidence: raw lines 14–29 and armored block lines 31–84; source answer/qualification at lines 14, 18–26 and locators at 30–34.

## `extend-forward-api-tokenization-support` — 2/2 PASS

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-extend-forward-api-tokenization-support]]` → `[[raw/braintree/docs/guides/extend/forward-api/tokenization-support-2026-09-16]]`.

1. **Q1 — PASS.** The exact document is the collected unversioned Braintree **Forward API Tokenization Support** developer guide at canonical URL `/braintree/docs/guides/extend/forward-api/tokenization-support`, pinned to `raw/braintree/docs/guides/extend/forward-api/tokenization-support-2026-09-16.md`. The source title, canonical URL and sole `raw_files` owner are at source lines 2–8; raw provenance, title and slug are at raw lines 1–10. Manifest SHA-256: `53b7d399dceb6a856b40252526e7390a18c9eb36c846f85a2fd8282c0e3289c6` (verified).
2. **Q2 — PASS.** Its central purpose is conditional Braintree-side conversion of a referenced payment method to Discover or Mastercard TPAN information for forwarding, plus selection/restriction controls. In this snapshot, Discover is restricted to US-issued cards plus PayPal/Venmo accounts; Mastercard to EU/UK-issued cards plus PayPal accounts. Production tokenization separately requires Forward API eligibility, approval, and linked PayPal credentials. Neither network supports cryptogram-based authorizations; CVV and multiple-authorization behavior is conditional on `expire_at`; PayPal is limited to channel-initiated billing agreements and Venmo is listed only for Discover. Automatic tokenization is an attempt, and `tokenize_on_forward`/TSP options control forwarded data and restrictions—not destination acceptance, authorization, charging, settlement, or funding. Exact evidence: raw lines 16–19, 22–44 and sandbox examples 47–119; source answer/qualifications at lines 14–34 and locators at 38–44.

## Shared gap sweep, extra reads, and link checks

- Fully read primary evidence: all four selected source pages and all four pinned raw files. The selected PGP raw also supplied the cross-page identity/purpose context needed to assess the cryptography guide's PGP instruction; its name/fingerprint was not promoted into a current-trust claim.
- Related/unlinked sweep: inspected Braintree Forward API guide/reference filenames and raw content matches for `Forward API`, `NetworkTokenizedCard`, `tokenize_on_forward`, `D26C77FA`, and `aes-gcm-nonce`. The reference/config/function/variable/error pages and sibling destination/example guides were not needed to answer these eight questions and were not used as factual evidence. Provider-external tokenization/PGP filename matches were out of scope. No older duplicate of any exact selected page was found, so no history/conflict read was triggered.
- Link resolution: root `[[braintree-index]]` exists; the Braintree index links both actual concepts; the concepts reciprocally link the assigned sources (`braintree-forward-api` for transformations/PGP, `braintree-payment-platform` for cryptography/tokenization); every source links its concept, declares exactly one matching `raw_files` owner, and includes the exact dated Raw Sources target; all targets exist. Forward and reverse concept/source/raw lookups therefore pass.
- Hashes: all four current raw SHA-256 values equal the approved manifest. That verifies pinned-byte provenance and immutability only; it does not prove present truth, availability, eligibility, operational authority, current key trust, or execution.
- Coordinator boundary: aggregate company/source catalogs and final campaign close checks remain coordinator-owned and are not closed by this group audit.

Analysis ended / handoff: `2026-10-04T03:13:59Z` UTC.
