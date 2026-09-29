# Braintree C21 fixed-query audit — Group A

Pinned pages were read completely: ACH Direct Debit (273 lines) and SEPA Direct Debit (51 lines).

## ACH Direct Debit

**Actual route:** `wiki/index.md` line 11 `[[braintree-index]]` → `wiki/braintree-index.md` line 239 `[[braintree-payment-methods]]` → `wiki/concepts/braintree-payment-methods.md` line 41 `[[source-braintree-payment-methods-ach]]` → source frontmatter/raw route at `wiki/sources/braintree/source-braintree-payment-methods-ach.md` lines 6–8 and 48–50 → `raw/braintree/articles/guides/payment-methods/ach-2026-09-16.md`.

### Q1 — Where is the Braintree ACH payment-method guide?

- **Object/action match:** MATCH — the requested object is the Braintree ACH payment-method guide and the route terminates at the pinned ACH Direct Debit article, not an SDK or GraphQL page.
- **Direct answer:** The canonical guide recorded by the pinned page is `https://developer.paypal.com/braintree/articles/guides/payment-methods/ach`; the wiki route above reaches its canonical source and pinned raw snapshot.
- **Exact raw locator:** raw line 1 (source URL); line 14 (`# ACH Direct Debit`).
- **Verdict:** PASS.

### Q2 — What availability, setup and payment-lifecycle boundaries does this page itself state?

- **Object/action match:** MATCH — the answer reports the ACH article's own availability, setup and lifecycle statements.
- **Direct answer:** In the 2026-09-16 snapshot, eligibility is limited to US merchants transacting in the US in USD through Braintree Direct, in good standing, able to implement a custom client-side JavaScript v3 integration; ACH is unavailable in Drop-in, and qualifying merchants are told to contact Braintree to enable it in sandbox. A bank account must be verified before collection; the page names instant verification, network check, micro-transfers and independent check and recommends a backup method. Setup also requires application-code changes and Control Panel enablement. Processing is batch based, with no card-style authorization/capture: Braintree waits three business days for returns, then disburses, with two more business days stated for bank receipt. Later returns can be deducted from the next disbursement, and `Settled` remains displayed after a late return. Refunds are limited to `Settled` transactions. The page is internally inconsistent on voids: it first says ACH transactions cannot be voided at any lifecycle point, then says support can enable voiding with transaction-dependent timing. Bank accounts can be vaulted, but Braintree recurring billing is stated not to support repeat bank-account payments. Unauthorized-dispute and extended warranty-claim windows also mean neither settlement nor disbursement is stated as irreversible.
- **Exact raw locator:** availability lines 19–33; verification lines 36–76; batch/status/timeline lines 95–153; void/refund conflict lines 161–169; late returns lines 172–216; dispute windows and extended claims lines 223–263; vaulting/recurring boundary and setup lines 267–272.
- **Verdict:** PASS.

## SEPA Direct Debit

**Actual route:** `wiki/index.md` line 11 `[[braintree-index]]` → `wiki/braintree-index.md` line 239 `[[braintree-payment-methods]]` → `wiki/concepts/braintree-payment-methods.md` line 23 `[[source-braintree-payment-methods-sepa-direct-debit]]` → source frontmatter/raw route at `wiki/sources/braintree/source-braintree-payment-methods-sepa-direct-debit.md` lines 6–8 and 48–50 → `raw/braintree/articles/guides/payment-methods/sepa-direct-debit-2026-09-16.md`.

### Q3 — Where is SEPA Direct Debit documented in Braintree?

- **Object/action match:** MATCH — the requested object is Braintree's SEPA Direct Debit payment-method guide and the route terminates at that pinned article, not an ACH or card page.
- **Direct answer:** The canonical guide recorded by the pinned page is `https://developer.paypal.com/braintree/articles/guides/payment-methods/sepa-direct-debit`; the wiki route above reaches its canonical source and pinned raw snapshot.
- **Exact raw locator:** raw line 1 (source URL); line 14 (`# SEPA Direct Debit`).
- **Verdict:** PASS.

### Q4 — What availability, timing and lifecycle boundaries does this page itself state?

- **Object/action match:** MATCH — the answer reports the SEPA article's own availability, timing and lifecycle statements, without importing ACH timing.
- **Direct answer:** In the 2026-09-16 snapshot, SEPA Direct Debit is in limited release and only available to pilot merchants, who are directed to contact Braintree. The bank-account holder must accept a debit mandate. Integration requires a valid PayPal business account created, verified and linked in the Braintree Control Panel, account-manager configuration of that PayPal account, then client and server integration. The page says most returns arrive within three business days, but returns may arrive after disbursement; Braintree then deducts the amount from the next business day's disbursement and displays a SEPA Direct Debit Return Code followed by `Failed After Settlement`. It also says funds settle into the merchant's PayPal account once the customer confirms payment. Read together, confirmation, settlement and disbursement are not stated as irreversible. The page states that vaulting and recurring transactions are supported. Its pilot language is snapshot evidence, not proof of present availability or merchant enablement.
- **Exact raw locator:** limited-release availability lines 17–18; mandate line 22; setup lines 25–27; returns and post-disbursement handling lines 38–40; funding lines 43–45; vaulting/recurring support lines 48–50.
- **Verdict:** PASS.

## Shared gap sweep, extra reads and reciprocal links

- **Bounded filename/content sweep:** Filename matching found the two pinned payment-method articles plus an ACH GraphQL guide. Content matching also found the provider-wide payment-method overview, ACH/SEPA integration guides, webhook/status/testing references and two accepted-payment-method pages. No matched page was needed to answer these questions because each detail question explicitly asks what its selected article itself states and both pinned articles fully answer it.
- **Extra full raw reads:** None.
- **Reciprocal links:** PASS — root index links the Braintree index; the Braintree index links `[[braintree-payment-methods]]` and both source pages; the concept links both sources (lines 23 and 41); each source links the concept (line 45) and its exact pinned raw (line 50). Both pinned SHA-256 values also match the C21 manifest.
- **Group result:** PASS; no retrieval failure found.
