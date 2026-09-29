# Braintree C21 fixed-query audit — Group C

Scope: the four predetermined questions for Apple Pay and Google Pay. Evidence is limited to the two C21-pinned payment-method articles; no current-support or sibling-guide inference is made.

## Apple Pay

Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-apple-pay.md` → `wiki/sources/braintree/source-braintree-payment-methods-apple-pay.md` → `raw/braintree/articles/guides/payment-methods/apple-pay-2026-09-16.md` (canonical URL `https://developer.paypal.com/braintree/articles/guides/payment-methods/apple-pay`; pinned SHA-256 `c7761ef9c0f22613c16fa7516c273291028775d1e6c86f960606cfeb98820ba3`, verified).

1. **Navigation question — Where is Braintree's Apple Pay guide?**
   - **Object/action match:** Yes — the route selects the Braintree Apple Pay payment-method guide and the requested action is to locate that guide, not infer a current capability.
   - **Direct answer:** It is the canonical source page `wiki/sources/braintree/source-braintree-payment-methods-apple-pay.md`, backed by the pinned raw article at `raw/braintree/articles/guides/payment-methods/apple-pay-2026-09-16.md` and the canonical URL above.
   - **Exact raw locator:** `# Apple Pay`, lines 14–18; source URL metadata, line 1.
   - **Verdict:** **PASS**

2. **Detail question — What setup, platform and use boundaries does this page itself state?**
   - **Object/action match:** Yes — the answer concerns Apple Pay setup, platform scope and uses stated by this pinned page itself.
   - **Direct answer:** Setup requires working with Braintree and Apple to configure Apple Pay certificates and Merchant IDs, then completing an iOS and/or JavaScript v3 client integration plus a server integration; when using Braintree's iOS client SDK, the certificate expires after 25 months and must be kept current. Platform eligibility is conditional on merchant location and processing settings. The page covers in-app (`iOS 8+` plus Touch ID or Face ID), mobile web (`iOS 10+` plus Touch ID or Face ID), and desktop web; desktop requires an iPhone, iPad, Apple Watch, or Mac able to authorize, macOS Sierra 10.12+, and Safari, while the latest Apple Pay SDK is stated to allow non-Safari browsers. Eligible merchants may accept customers in Apple Pay-supported regions, but the merchant must also be domiciled where Braintree onboarding and Apple Pay compatibility apply. Apple Pay cards may be vaulted for recurring billing and split shipments; separately, the page says vaulting should only be used when the customer consents at checkout for future merchant-initiated transactions. Using a vaulted card for a later customer-present transaction is stated to cause declines and is not recommended. These are statements from the 2026-09-16 snapshot, not proof of current merchant, buyer, browser, device, card or transaction eligibility.
   - **Exact raw locator:** `## Availability`, lines 23–35; `### Customer availability > #### Device requirements`, lines 41–62; `#### Location requirements`, lines 74–80; `## Processing > ### Recurring billing and vaulting`, lines 118–122; `## Setup`, lines 125–132.
   - **Verdict:** **PASS**

## Google Pay

Route: `wiki/index.md` → `wiki/braintree-index.md` → `wiki/concepts/braintree-payment-methods.md` → `wiki/sources/braintree/source-braintree-payment-methods-google-pay.md` → `raw/braintree/articles/guides/payment-methods/google-pay-2026-09-16.md` (canonical URL `https://developer.paypal.com/braintree/articles/guides/payment-methods/google-pay`; pinned SHA-256 `86081a92cfec0f5943b7d75c3e61a91c69f5fca2404eccdd210f74a8161e4403`, verified).

3. **Navigation question — Where is Braintree's Google Pay guide?**
   - **Object/action match:** Yes — the route selects the Braintree Google Pay payment-method guide and the requested action is to locate that guide, not infer a current capability.
   - **Direct answer:** It is the canonical source page `wiki/sources/braintree/source-braintree-payment-methods-google-pay.md`, backed by the pinned raw article at `raw/braintree/articles/guides/payment-methods/google-pay-2026-09-16.md` and the canonical URL above.
   - **Exact raw locator:** `# Google Pay`, lines 14–18; source URL metadata, line 1.
   - **Verdict:** **PASS**

4. **Detail question — What setup, platform and use boundaries does this page itself state?**
   - **Object/action match:** Yes — the answer concerns Google Pay setup, platform scope and uses stated by this pinned page itself, with Google-account cards kept distinct from cards stored directly on an Android device.
   - **Direct answer:** The page covers Android-app and web checkout. Setup requires application-code changes, Google Pay enablement in the Braintree Control Panel, and Google approval before production. Merchant acceptance is conditional on region and processing settings and remains subject to Google's terms and payment-content policies. For customers, cards or PayPal accounts saved to a Google account are stated to be available worldwide, while methods saved directly to an Android device follow Google Pay-supported countries/regions; in both cases, the merchant must separately be in a Braintree-onboarding country compatible with Google Pay. Google-account cards support risk-threshold rules and Premium Fraud Management Tools and may be vaulted for future transactions, recurring billing and split shipments. Cards stored directly on an Android device do not support Basic Fraud Tools but do support Premium Fraud Management Tools; they may be vaulted only for recurring billing and split shipments, require checkout consent for each unique transaction, and are decline-prone/not recommended when vaulted for future transactions. The page separately says “Google Pay accounts” cannot be vaulted or used for recurring billing or split shipments, without reconciling that label with its opening reference to PayPal accounts; the raw's underqualified generic fraud statement likewise must not override the preceding card-specific rules. These are page-scoped snapshot statements, not proof of current merchant, customer, device, browser, card or PayPal eligibility.
   - **Exact raw locator:** `# Google Pay`, lines 14–18; `## Availability`, lines 23–39; `### Customer availability`, lines 44–60; `### Supported browsers`, lines 65–67; `## Processing > ### Fraud tools`, lines 87–99; `### Recurring billing and vaulting`, lines 104–111; `## Setup`, lines 114–116.
   - **Verdict:** **PASS**

## Shared gap sweep, extra reads and reciprocal links

- **Bounded filename/content sweep:** Searched wallet-specific filenames under `raw/braintree/` and content matches within the C21 payment-method article directory plus the Apple Pay and Google Pay developer-guide folders. The sweep found the two pinned articles and sibling implementation/configuration/testing/reference raws. Those sibling raws are separate navigation authorities and were not needed to answer the two questions that explicitly ask what each payment-method page itself states.
- **Extra full reads:** None. Both pinned raws were read completely; no discovered conflict or missing answer required a sibling or historical full read.
- **Reciprocal links:** **PASS.** `braintree-apple-pay.md` links to the Apple Pay source, which links back to `[[braintree-apple-pay]]` (and also to `[[braintree-payment-methods]]`). `braintree-payment-methods.md` links to the Google Pay source, which links back to `[[braintree-payment-methods]]`. The provider index catalogs both sources and both routes begin at the root/provider indexes.
- **Group verdict:** **PASS — 4/4 questions.**
