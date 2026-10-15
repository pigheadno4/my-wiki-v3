# Fixed retrieval queries — docs-online-payments-classic-integrations-classic-api-integration-client-side-encryption-hosting-the-cse-library

## Q1 — purpose, scope, and non-inference

**Query:** What does the dated Adyen Classic CSE hosting page cover, and what should a reader avoid inferring from it?

**Expected answer:** It describes how an existing merchant Web CSE integration can self-host or embed Adyen's legacy JavaScript encryption library to encrypt card data client-side before sending encrypted data to the merchant server. Adyen recommends its own hosting from a unique URL. The page says CSE Web is being phased out, no longer developed, and closed to new CSE integrations, while expressly saying mobile integrations are unaffected. It does not establish a current supported Web integration, CSE library version, PCI DSS compliance, or successful payment authorization. Its raw metadata says last modified in 2019; the snapshot was captured 2026-09-15. The newer JWE route has separate requirements.

**Raw locators:** lines 15–29; **Requirements** (line 31); **Merchant hosted** (lines 35–40); **JavaScript only** (line 135). Canonical route: https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/client-side-encryption/hosting-the-cse-library

## Q2 — central capability, prerequisites, and warnings

**Query:** What must the merchant supply when self-hosting Classic CSE, which library variant fits which integration, and what form/security qualifications apply?

**Expected answer:** The merchant obtains the CSE public key from Customer Area. `adyen.encrypt.min.js` supports HTML form binding and JavaScript-only integration; `adyen.encrypt.nodom.min.js` supports JavaScript-only use. In the form variant, card inputs carry `data-encrypted-name` and omit `name`, the merchant supplies a server handler and JS binding, and the library adds encrypted card data at submit. A server-created `generationtime` is required because the page says payment requests more than 24 hours after it are refused and browser clocks may be wrong. Plain JavaScript and AMD/Require.js loading are illustrated. In the no-DOM variant, encrypt the card-data object before sending it to the merchant server. The PCI discussion is rationale for keeping raw card fields out of ordinary form posts, not proof of compliance or reduced scope.

**Raw locators:** **Requirements** (lines 31–33); **Merchant hosted** (lines 35–40); **Form template** (lines 42–71); **Plain JavaScript** (lines 77–99); **Require.js** (lines 101–131); **JavaScript only** (lines 135–170). Canonical route: https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/client-side-encryption/hosting-the-cse-library
