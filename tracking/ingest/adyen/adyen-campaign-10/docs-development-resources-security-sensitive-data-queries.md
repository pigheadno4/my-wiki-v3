# Adyen sensitive-data landing-page retrieval checks

## Q1 — Purpose, scope, and non-inference

**Query:** Does this page itself prove a merchant's encryption or PCI compliance, or provide enough detail to configure TLS and PGP?

**Expected route:** `[[adyen-index]]` → `[[adyen-api-access]]` → `[[source-adyen-docs-development-resources-security-sensitive-data]]`; pinned raw `# Protecting sensitive data` lines 15–25.

**Expected answer:** It is a short security navigation page. It says Adyen applies security practices and the integrator should protect sensitive information; it names TLS for data in transit and PGP for sensitive-card-data exchange. It does not provide configurations, prove an integration's encryption state or key registration, establish merchant eligibility, or determine PCI DSS compliance.

## Q2 — Central capability, prerequisites, warnings

**Query:** Which two distinct next-step routes does the page name, and what can be learned from this landing page alone?

**Expected route:** Same source; raw bullet signposts at lines 23–25 and `## Next steps` at lines 27–35. TLS detail belongs to `[[source-adyen-docs-development-resources-security-sensitive-data-tls]]`; the PGP raw link in the source entry is marked unread navigation.

**Expected answer:** The page routes to Transport Layer Security (TLS) for protecting data during transmission and to PGP encryption for learning how to generate/upload a key for sensitive card-data exchange with Adyen. It does not state exact TLS versions/ciphers, PGP steps, whether both are needed for a given integration, or any compliance outcome. Follow each dedicated guide before making implementation claims.
