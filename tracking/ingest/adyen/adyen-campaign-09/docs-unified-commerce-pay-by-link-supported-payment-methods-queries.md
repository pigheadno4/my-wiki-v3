# Fixed retrieval checks: Pay by Link supported methods

## Q1 — Purpose and scope

**Query:** What does Adyen's Pay by Link supported-methods page establish about method availability?

**Expected answer:** It is a dated matrix comparing listed methods for Customer Area versus API-created links, and says a method must first be added to the merchant account. A listed row or method-guide link does not prove an account has the method enabled, that a shopper meets country/currency/device conditions, that it will render, or that payment will succeed. The snapshot's metadata says last modified 2024-06-11. The page contains limited row labels such as Afterpay AU/NZ/US/CA and Clearpay GB, not a complete eligibility specification.

**Raw locators:** `# Supported payment methods`, lines 15–19; `## Add payment methods to your account`, lines 21–30; `## Available payment methods`, lines 32–102. **Canonical retrieval route:** [[source-adyen-docs-unified-commerce-pay-by-link-supported-payment-methods]] → [[raw/adyen/docs/unified-commerce/pay-by-link/supported-payment-methods/2026-09-15|pinned raw]].

## Q2 — Channel distinctions and consequential limits

**Query:** Which Customer Area/API distinctions and material prerequisites or conflicts must be retained when using the Pay by Link matrix?

**Expected answer:** Read each channel column: for example, Afterpay, Clearpay, Billie via Klarna, Klarna, Oney 3x4x, and stored card details are marked API-side with blank Customer Area cells. Apple Pay requires Adyen's Apple Pay certificate and Google Pay requires `eu.adyen.link` as a supported Google Developer Console domain. This table nevertheless marks Affirm, Alma and Atome for Customer Area, conflicting with the separate Customer Area creation guide's blanket BNPL exclusion; preserve that unresolved difference. ACH check marks are qualified by the page's warning that Pay by Link does not automatically validate accounts or provide the mandated debit-authorization text; it calls B2C ACH links non-compliant and limits the advised B2B case to separately collected/stored authorization. Do not infer a method's current country, currency, device or merchant eligibility merely from navigation links.

**Raw locators:** `## Available payment methods`, lines 32–105; `## Compliance of ACH Direct Debit payment links`, lines 107–111; conflict context: [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links-customer-area]], opening paragraph. **Canonical retrieval route:** [[source-adyen-docs-unified-commerce-pay-by-link-supported-payment-methods]] → [[raw/adyen/docs/unified-commerce/pay-by-link/supported-payment-methods/2026-09-15|pinned raw]].
