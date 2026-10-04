# Braintree C38 fixed query audit — Group D

- Campaign: `braintree-campaign-38`
- Fixed allocation: D; four pages, two questions each
- Mode: repository read-only query audit; only this `/tmp` report was written
- Analysis ended (UTC): `2026-10-04T09:09:18Z`
- Artifact handoff (UTC): `2026-10-04T09:09:59Z`
- Result: **PASS — 8/8 fixed questions**

## 1. `articles-moneris-transactions-accepted-payment-methods`

**Route:** `wiki/index.md:11` → `wiki/braintree-index.md:574` → `wiki/concepts/braintree-payment-methods.md:24` → `wiki/sources/braintree/source-braintree-articles-moneris-transactions-accepted-payment-methods.md:1-60` → `raw/braintree/articles/moneris/transactions/accepted-payment-methods-2026-09-16.md`. Direct source catalog: `wiki/braintree-index.md:37`.

1. **Q1 — PASS.** This is the collected Braintree-hosted **Moneris-path account** article (page update 2025-04-01; snapshot 2026-09-16), not independent Moneris or card-network authority. It documents default Visa/Mastercard acceptance, separately arranged American Express processing, conditionally available PayPal/wallet methods, and USD/CAD merchant-account currency handling. It gives no merchant-specific approval, actual rate, or universal/current support guarantee. Scope and values: raw lines 17-44, 49-74.
2. **Q2 — PASS.** Its central purpose is payment-method and currency setup retrieval. Amex requires a direct Amex account, currency-matched Service Establishment Numbers, confirmation that Amex pricing was in the original agreement or a signed additional form, and both Braintree's per-transaction fee and Amex's separately assessed fees (raw 26-44). PayPal requires Business Account credentials; Google Pay and Apple Pay retain “most merchants,” eligible-customer, and device/app conditions; SRC is limited-release language; USD/CAD presentment and settlement must match (49-74). The retained SRC warning is real: the fully read dedicated source/raw says support ended 2026-01-20 while also retaining current-tense limited-release wording (`wiki/sources/braintree/source-braintree-payment-methods-secure-remote-commerce.md:14-35`; its raw 14-15, 21-48, 88-90). The snapshots do not resolve that conflict.

## 2. `articles-moneris-transactions-settlement-funding-timeline`

**Route:** `wiki/index.md:11` → `wiki/braintree-index.md:573` → `wiki/concepts/braintree-payment-platform.md:28` → `wiki/sources/braintree/source-braintree-articles-moneris-transactions-settlement-funding-timeline.md:1-48` → `raw/braintree/articles/moneris/transactions/settlement-funding-timeline-2026-09-16.md`. Direct source catalog: `wiki/braintree-index.md:38`.

1. **Q1 — PASS.** This is the Braintree-hosted **Moneris account-route** article for credit-card settlement batching and funding after successful settlement. It is account-setup-, card-brand-, bank-, weekday/holiday-, and event-anchor-qualified; it states no pricing model or regional rule. Apple Pay follows the Amex handling stated here, while PayPal disbursement is separate (raw 19-55). The latest canonical source is byte-identical to approved attempt 2, not attempt 1.
2. **Q2 — PASS.** The corrected lifecycle distinction is explicit. The account-dependent, unchangeable 8pm cutoff controls **pre-settlement batch inclusion**; submissions after it enter the next day's batch (raw 22-24). Only after Moneris confirms successful settlement are funds ready for payout: Visa/Mastercard is stated as 1-3 business days and Amex as 2-8, with Amex owning its cutoff and direct disbursement (26-32). Separately, Moneris funding descriptors and a bank-dependent 2-5-business-day reflection statement follow the settlement date, while weekday/holiday cadence can add another business day (35-45). Those timing statements are not reconciled into one deadline and do not prove settlement, payout, or bank arrival. Apple Pay/Amex and separate PayPal ownership are at 48-55.

## 3. `articles-br-payment-capabilities`

**Route:** `wiki/index.md:11` → `wiki/braintree-index.md:573` → `wiki/concepts/braintree-payment-platform.md:35` → `wiki/sources/braintree/source-braintree-articles-br-payment-capabilities.md:1-58` → `raw/braintree/articles/br/payment-capabilities-2026-09-16.md`. Direct source catalog: `wiki/braintree-index.md:39`.

1. **Q1 — PASS.** This is a 2026-09-16 Braintree **Brazil-path installment-payment** snapshot: Braintree and PayPal allow a customer-selected sale to be divided across a 2-12-month plan (raw 14-18). The page states no currency, card brand, SDK/API version, environment, merchant-account eligibility rule, or pricing schedule, so none can be inferred; it is not another region's capability or proof of account enablement or execution.
2. **Q2 — PASS.** The documented action is a checkout-selected installment sale: the customer is debited and the merchant paid every 30 days until fulfillment (raw 16-18). Disbursements divide evenly, with any remainder in the final installment (31-33). Integration updates are required, while exact create/refund/search procedures remain in the linked installment article (36-43). Disputes stay transaction-level—a customer cannot dispute one installment—and related debits/credits apply evenly across all installments; the Disputes Financial Impact Report is the reconciliation route (46-50). Activity, Disbursement, and Transaction Level Fee reports are navigation targets for lifecycle detail (21-28), not imported schemas or proof of funds.

## 4. `articles-moneris-reconciliation`

**Route:** `wiki/index.md:11` → `wiki/braintree-index.md:591` → `wiki/concepts/payment-reconciliation-reporting.md:117` → `wiki/sources/braintree/source-braintree-articles-moneris-reconciliation.md:1-39` → `raw/braintree/articles/moneris/reconciliation-2026-09-16.md`. Direct source catalog: `wiki/braintree-index.md:40`.

1. **Q1 — PASS.** This is a Braintree-hosted **Moneris-account reconciliation** snapshot for comparing a daily Settlement Batch Summary Report with monthly Moneris statements and bank-account deposits (raw 14-26). It states no region, currency, fee rate, or pricing model and is not authority for sibling processor/account routes, independent current Moneris policy, or an individual deposit.
2. **Q2 — PASS.** Gross sales are matched from Settlement Batch Summary daily sales to statement Daily Activity Summary sales; daily net-sales Totals are compared with account deposits, optionally cross-checking Settlement Batch Summary Totals (raw 19-26). Refunds are removed from that day's settlement batch before funding, and any shortfall is debited from the bank account (29-31). Monthly void-related transaction fees return as one small deposit at the beginning of the next month, calculated from prior-month void, gateway-rejection, and zero-amount counts (33). Statement terms map Gross Sales→Sales, Returns→Credits, and Net Sales→Totals (36-43).

## Shared verification

- **Manifest/hash PASS:** all four job IDs, raw paths, source targets, and canonical URLs match `manifest.json`; recomputed SHA-256 values match the pins: accepted methods `f17d5b81b7616a223d0cf21d9f40a1e022fa0d64b002325494262cf68687c09e`, settlement/funding `0e4a8a66b34bc4d69f5c045cd3d47e080cac1459116b6a914d4bf096b60bdf9f`, Brazil capabilities `2f8a29d09da1de80c9ef69c1c732a217e5bd87730b16e86d9f86f0591c494e12`, and reconciliation `baf69e100207635c921cdcbee1e8797af1ead16e3db8b61627c5c5187808b498`.
- **Route/ownership PASS:** root→Braintree index→main concept→source→pinned raw resolves for each page; every source frontmatter/raw link and each raw Source URL match the manifest. Exact primary-raw reverse lookup found one canonical source owner per selected raw.
- **Gap sweep:** filename and focused-content sweeps found the selected raws, same-topic processor/account siblings, and declared navigation-only targets. The selected raws answer all eight questions. No unlinked raw was needed; sibling pages were not read or used. The only extra full source/raw read was the dedicated SRC guide required to verify the retained support-status conflict.
- **Material retrieval failures:** none.
