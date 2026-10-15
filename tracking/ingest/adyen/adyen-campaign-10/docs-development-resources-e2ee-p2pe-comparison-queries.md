# Fixed retrieval checks: Adyen E2EE versus P2PE

## Q1 — Purpose and scope

**Query:** What does Adyen's E2EE/P2PE comparison cover, and does it certify a merchant's PCI compliance?

**Expected answer:** It compares default E2EE and opt-in P2PE for Adyen-provided payment terminals in a POS integration: encryption coverage, supported devices, validation and operational work. It is Adyen's dated guidance, not proof that a specific merchant or device is currently eligible or PCI compliant. Merchant responsibilities and the applicable SAQ need integration/acquirer/QSA-specific assessment; the page's statements do not certify a merchant deployment.

**Raw locators:** `# Adyen's E2EE and P2PE PCI security`, lines 15–21; `## Adyen's E2EE solution`, lines 23–41; `## Adyen's P2PE solution`, lines 43–55. **Canonical retrieval route:** [[source-adyen-docs-development-resources-e2ee-p2pe-comparison]] → [[raw/adyen/docs/development-resources/e2ee-p2pe-comparison/2026-09-15|pinned raw]].

## Q2 — Encryption, devices and PCI validation boundaries

**Query:** How do the solutions differ in encrypted material, device scope and validation effort, and which device claim needs caution?

**Expected answer:** Adyen says E2EE encrypts the whole terminal payment message, decrypting at its platform before issuer authorization; it is the default for Adyen-provided terminals but lacks a PCI P2PE validation stamp. Opt-in P2PE adds separate PAN/track-data encryption inside that message and has independent PCI P2PE validation, while requiring SAQ P2PE plus the P2PE Instruction Manual and operational measures such as terminal inspections/audit trails. The page says its E2EE route uses SAQ B-IP; treat these as Adyen's guide-specific validation statements, not automatic merchant compliance. P2PE covers a listed device subset; the table says V240m while the later detailed list says V240m Plus, so exact-model support is unresolved.

**Raw locators:** `## Comparing Adyen P2PE and E2EE`, lines 57–68; `### Supported terminals`, lines 70–73; `### Compliance`, lines 75–80; `### Security`, lines 82–88; `### Quality`, lines 90–95. **Canonical retrieval route:** [[source-adyen-docs-development-resources-e2ee-p2pe-comparison]] → [[raw/adyen/docs/development-resources/e2ee-p2pe-comparison/2026-09-15|pinned raw]].
