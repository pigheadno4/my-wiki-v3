# C10 fixed queries — docs-development-resources-security-integration-security

## Q1 — Purpose, scope, and inference boundary

**Query:** Does the integration-security page certify an Adyen merchant integration as secure or PCI compliant, and does it provide API, TLS, or webhook HMAC implementation rules?

**Expected answer:** It is general guidance for online and in-person Adyen integrations and explicitly says it is incomplete and not definitive. It assigns merchant responsibility for merchant-controlled pages/apps and gives terminal-safety advice. It neither assesses a merchant nor proves compliance or payment safety. API authentication, TLS transport and webhook HMAC details belong to separate documentation; links on this page are navigation, not implementation evidence.

**Evidence:** `raw/adyen/docs/development-resources/security/integration-security/2026-09-15.md:15-35`, `raw/adyen/docs/development-resources/security/integration-security/2026-09-15.md:69-73`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-pci-dss-compliance]]` → `[[source-adyen-docs-development-resources-security-integration-security]]` → pinned raw.

## Q2 — Central capability, prerequisites, and warnings

**Query:** Which online and POS security responsibilities does this snapshot name, and when do extra P2PE manual requirements apply?

**Expected answer:** Online, the merchant is responsible for its own checkout pages and apps; vulnerable third-party scripts can expose data, and the page routes to PCI/IAM/script-security guidance. POS, it calls for terminal inventory and updates, monitored placement, inspection on receipt and regularly afterward, verified maintenance access, and shielding PIN entry. If using Adyen P2PE, implement the P2PE Instruction Manual requirements as well. These are guidance and a conditional obligation, not proof that controls were deployed or a merchant uses P2PE.

**Evidence:** `raw/adyen/docs/development-resources/security/integration-security/2026-09-15.md:31-67`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-pci-dss-compliance]]` → `[[source-adyen-docs-development-resources-security-integration-security]]` → pinned raw.
