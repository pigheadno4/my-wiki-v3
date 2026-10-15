# Adyen TLS retrieval checks

## Q1 — Purpose, scope, and non-inference

**Query:** What does Adyen's TLS page require for existing versus new integrations, and can this snapshot establish a currently successful or compliant connection?

**Expected route:** `[[adyen-index]]` → `[[adyen-api-access]]` → `[[source-adyen-docs-development-resources-security-sensitive-data-tls]]`; pinned raw `# Transport Layer Security (TLS)` lines 15–26, `## Requirements` lines 28–34, and `## Supported TLS versions and ciphers` lines 36–49.

**Expected answer:** The 2026-09-15 snapshot applies to all Adyen integration types. It says TLS 1.2 is only supported for existing merchants using its listed strong ciphers; new integrations must use TLS 1.3 with either `TLS_AES_256_GCM_SHA384` or `TLS_CHACHA20_POLY1305_SHA256`, and TLS connections must use SNI. Unsupported settings may prevent Adyen from receiving requests. The page is configuration guidance, not evidence of current supported inventory, negotiated TLS, PCI compliance, API authorization, or a successful payment.

## Q2 — Central capability, prerequisites, warnings

**Query:** What certificate-pinning policy and rotation handling does the page set out, including the exception for an organization that must pin?

**Expected route:** Same source; raw `## Certificate pinning` lines 56–65 and `### Certificate changes` lines 67–86; exact root names at lines 73–79.

**Expected answer:** Adyen strongly recommends against any certificate pinning because server certificate changes can break client connections even when the replacement chains to a trusted CA. If organizational policy mandates pinning, the guide says to pin all listed roots, not leaf certificates or the entire chain, and keep track of future roots. Routine changes have a stated 30-day system-message notice; emergencies may have less notice. The integration owner is responsible for handling changes. The listed roots and notification timing are snapshot statements and need current verification before implementation.
