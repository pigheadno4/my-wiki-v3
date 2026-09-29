# Braintree C21 Fixed Query Audit — Group D

## Routes

### Local Payment Methods

`wiki/index.md` (`## PSP Indexes`, `[[braintree-index]]`, line 11) → `wiki/braintree-index.md` (`## Concepts`, `[[braintree-payment-methods]]`, line 239) → `wiki/concepts/braintree-payment-methods.md` (`## Sources`, `[[source-braintree-payment-methods-local-payment-methods]]`, line 35) → `wiki/sources/braintree/source-braintree-payment-methods-local-payment-methods.md` (`raw_files` and `## Raw Sources`, lines 7-8 and 50-52) → `raw/braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16.md` (pinned SHA-256 `2653330a1f1972eae675ec4b9bb02be6656d8d4d874a0ff812c2ff402d4c5bb1`).

### UnionPay

`wiki/index.md` (`## PSP Indexes`, `[[braintree-index]]`, line 11) → `wiki/braintree-index.md` (`## Concepts`, `[[braintree-payment-methods]]`, line 239) → `wiki/concepts/braintree-payment-methods.md` (`## Sources`, `[[source-braintree-payment-methods-unionpay]]`, line 27) → `wiki/sources/braintree/source-braintree-payment-methods-unionpay.md` (`raw_files` and `## Raw Sources`, lines 7-8 and 49-51) → `raw/braintree/articles/guides/payment-methods/unionpay-2026-09-16.md` (pinned SHA-256 `e4a19a82e56c2718ef620c75e65dbd80f0d078eb2b5722646c09bc5f0b930f9a`).

## Questions

### D1. Where is the local payment methods guide?

- **Object/action match:** The requested object is Braintree's Local Payment Methods guide and the action is to locate it. The route resolves to the source page whose canonical URL and pinned raw identify `/braintree/articles/guides/payment-methods/local-payment-methods`; it does not substitute a method-specific implementation page.
- **Direct answer:** Follow the Local Payment Methods route above to `source-braintree-payment-methods-local-payment-methods`, then its pinned raw `raw/braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16.md`.
- **Exact locator:** Pinned raw lines 1 and 6-7 identify the source URL, title and slug; line 14 is the guide heading.
- **Verdict:** **PASS**.

### D2. What scope, availability and flow qualifications does this page itself state?

- **Object/action match:** The requested object is the Local Payment Methods article itself and the action is to extract its stated scope, availability and flow qualifications. The reached raw is that exact article, not the linked method catalog or client/server integration documentation.
- **Direct answer:** The page defines Local Payment Methods as banks, wallets or other means limited to particular regions, using iDEAL in the Netherlands and Bancontact in Belgium as examples. It says they are available to eligible merchants in Braintree-supported countries only after PayPal is added to the Braintree integration; checkout is presented in euros, settlement goes to the merchant's PayPal business account in its primary currency, and applicable conversion is added to the customer's payment amount. Customer methods depend on locality, while Custom UI lets the merchant choose what to display based on customer country. Setup requires a created, verified and linked valid PayPal business account in the Braintree Control Panel before the separate client/server integrations. Most methods redirect the customer; Payment Contexts provide pre-transaction visibility into initiation, method type and customer progress, not settlement proof. The page also says Local Payment Method disputes, vaulting and recurring transactions are currently unsupported.
- **Exact locator:** Scope and regional examples: line 16; eligible-merchant, PayPal, euro-presentment and settlement qualifications: line 21; locality and display control: line 26; PayPal account/setup prerequisite: line 31; funding: line 44; disputes: line 49; vaulting/recurring limits: line 54; redirect-qualified Payment Context purpose and pre-transaction scope: lines 59-63; statuses and examples: lines 74-91.
- **Verdict:** **PASS**.

### D3. Where is UnionPay documented in Braintree?

- **Object/action match:** The requested object is Braintree's UnionPay payment-method guide and the action is to locate it. The route resolves to the source and raw page titled `UnionPay`, without substituting generic credit-card or SDK documentation.
- **Direct answer:** Follow the UnionPay route above to `source-braintree-payment-methods-unionpay`, then its pinned raw `raw/braintree/articles/guides/payment-methods/unionpay-2026-09-16.md`.
- **Exact locator:** Pinned raw lines 1 and 6-7 identify the source URL, title and slug; line 14 is the guide heading.
- **Verdict:** **PASS**.

### D4. What setup, flow and limitations does this page itself state?

- **Object/action match:** The requested object is the UnionPay article itself and the action is to extract its setup, checkout flow and limitations. The reached raw is that exact article; statements are kept UnionPay-specific and snapshot-qualified.
- **Direct answer:** The page first says the dedicated UnionPay integration is deprecated because UnionPay can now be processed as a credit card through Discover, yet it also says UnionPay transactions are not enabled by default, require additional setup, and later calls UnionPay a limited release. It describes most European merchants using Android v4, iOS v4+, or JavaScript v3, excludes the JavaScript v3 Drop-in UI, requires settlement in USD, GBP, EUR or CHF, and directs merchants to contact Braintree for setup/access. Its described checkout asks for a mobile number and an SMS code before processing; verification repeats for each purchase unless the card is vaulted. After verification, processing resembles regular cards and typically settles within three business days. Limits include a UnionPay-specific processing rate, a non-refundable USD 25 (or settlement-currency equivalent) chargeback fee regardless of outcome including pre-arbitrations, and CVV/AVS-rule bypass for certain transactions because some cards lack CVV and postal codes are rarely collected. The page's deprecation notice and limited-release setup statement are unresolved tension in the collected snapshot and do **not** establish current support or merchant enablement.
- **Exact locator:** Deprecation/Discover path and default-disabled setup: lines 17-20; merchant, SDK, Drop-in and currency qualifications: lines 23-27; SMS and vaulted-card flow plus settlement timing: lines 30-34; processing fee: lines 37-39; chargeback limitation: lines 42-44; fraud-tool and CVV/AVS qualifications: lines 47-53; vaulted-card SMS behavior and limited-release setup statement: lines 56-63.
- **Verdict:** **PASS**.

## Group checks

- **Complete pinned-raw reads:** Read both selected raw files end-to-end (92 and 66 file lines respectively); both hashes match `tracking/ingest/braintree/braintree-campaign-21/manifest.json`.
- **Bounded filename/content gap sweep:** One sweep across `raw/braintree` for `local-payment-methods`/`unionpay` filenames and exact `Local Payment Methods|UnionPay` content found the two pinned articles plus related method-specific implementation, configuration, testing, webhook and overview pages. No extra raw was selected: the fixed questions expressly ask what each article itself states, the pinned articles answer them completely, the Local Payment Methods article routes method-by-method/client-server details outward, and the UnionPay deprecation-versus-limited-release tension is already explicit within the pinned article. No current-support inference was made.
- **Reciprocal links:** `wiki/braintree-index.md` links `[[braintree-payment-methods]]`; the concept links both source pages; each source links back to `[[braintree-payment-methods]]` and links its exact pinned raw under `## Raw Sources`. All referenced route files exist. **PASS**.
- **Extra full raw reads:** None.
