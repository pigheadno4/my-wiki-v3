# Fixed retrieval checks: Classic API integration

## Q1 — Purpose and scope

**Query:** What does Adyen's Classic API integration page describe, and can a merchant use it for a new online integration?

**Expected answer:** It describes a legacy website/mobile card-payment flow in which the merchant handles raw shopper card data and sends it to the Adyen Payment API. The endpoint is inactive and unsupported for new integrations; Adyen directs new builds to Checkout API and existing users to contact Adyen about migration. Do not infer current merchant eligibility, active endpoint availability, PCI compliance certification, or successful payment execution from this snapshot.

**Raw locators:** `# Classic API integration`, lines 16–29. **Canonical retrieval route:** [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/2026-09-15|pinned raw]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** In the documented Classic flow, what does the merchant send, what does the response signify, and what qualifications matter?

**Expected answer:** After test-account setup and obtaining API-key or basic-authentication credentials, the merchant server posts an `/authorise` request with merchant account, reference, minor-unit amount and card data. The page conditions the raw-card integration on PCI compliance at Level 1 or 2. A validated message undergoes risk analysis, and an authorization attempt depends on the outcome; the sample `Authorised` response is not a guaranteed payment or capture. Capture and webhook confirmation are linked as next steps. Where co-badged-card guidance applies, offer supported brand selection and pass the shopper's selected brand. Preserve the inactive/new-integration warning.

**Raw locators:** `## Requirements`, lines 31–38; `## Authorise request`, lines 48–78; `## Authorise response`, lines 80–92; `## Requirements for co-badged cards`, lines 94–104; `## Next steps`, lines 106–118. **Canonical retrieval route:** [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/2026-09-15|pinned raw]].
