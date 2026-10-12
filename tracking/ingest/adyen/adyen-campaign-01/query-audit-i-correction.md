# Adyen C01 audit I — JWE correction review

Job: `docs-online-payments-card-encryption-with-jwe` (manifest position 42)

## Targeted checks

- **Pinned evidence unchanged:** `raw/adyen/docs/online-payments/card-encryption-with-jwe/2026-09-15.md` hashes to `0fe7d8b472ed2cf23b069289c37487b0b2bf0b9f64735a8f9fce6eb02661f064`, exactly matching the manifest.
- **Correction is evidence-bounded:** source lines 28–29 now state that the retained sample certificate is EC P-256 while the import/encryption examples use `RSA-OAEP-256`, mark the sample as non-working guidance, and require a compatible merchant certificate/algorithm to be verified. This matches raw lines 77–95 and 119–127 and does not infer a replacement algorithm or current upstream behavior.
- **Both detail routes are corrected:** source lines 36–37 annotate `## Compute your JWK` and `## Encrypt card details` with the same certificate/algorithm conflict, so readers retrieving either half of the procedure receive the warning.
- **Concept context is corrected:** `wiki/concepts/adyen-card-encryption.md:18-21` carries the same warning and routes back to the source; its purpose, prerequisites, PCI boundary, and outcome non-inference at lines 10–14 remain intact.
- **Retrieval route remains complete:** `wiki/index.md:10` → `wiki/adyen-index.md:56,103` → `wiki/concepts/adyen-card-encryption.md:10,18-21` → `wiki/sources/adyen/source-adyen-docs-online-payments-card-encryption-with-jwe.md:12-48` → pinned raw.

## Fixed-query residual verdict

- **Q1 scope / must-not-infer:** **PASS, unchanged.** The source still correctly limits the page to the custom Web API-only JWE flow and preserves PCI, eligibility, certificate, library, decryption, payment, settlement, and fulfillment boundaries.
- **Q2 purpose / material warnings / detail retrieval:** **PASS after correction.** The material sample-key/algorithm conflict is now explicit at source and concept layers and attached to both exact procedural locators. Detailed fields and request shape remain retrievable from the unchanged pinned raw.

**Residual verdict: PASS — no material fixed-query issue remains for position 42.**
