# Braintree C36 fixed query audit C

- Audit group: C
- Analysis UTC: `2026-10-04T07:07:05Z`
- Handoff UTC: `2026-10-04T07:08:50Z`
- Coverage: 4/4 exact pages; 8/8 fixed questions; 4/4 pinned raw hashes; all selected source and raw files read in full
- Overall verdict: **PASS**
- Material failures: none

## Shared route, integrity, and gap checks

`wiki/index.md:11` exposes `[[braintree-index]]`. The provider index exposes all three main concepts used here: `[[braintree-payment-methods]]` at `wiki/braintree-index.md:510`, `[[braintree-control-panel]]` at `wiki/braintree-index.md:516`, and `[[payment-reconciliation-reporting]]` at `wiki/braintree-index.md:527`. Each concept links the selected source, each selected source links back to its main concept, and each source's `raw_files` plus `## Raw Sources` route resolves to the same pinned raw. The direct provider source catalog is not required for these already-complete concept routes.

| Page | Manifest SHA-256 | Actual SHA-256 | Result |
| --- | --- | --- | --- |
| `articles-aib-af-transactions-descriptors` | `0d2e3e76a9a377688289b145e757b85e930675c381e9ba077e9aa6d3a19c52d7` | same | PASS |
| `articles-aib-af-transactions-accepted-payment-methods` | `7a9d3ab65a9972a99194d040cf3382cdd913b6ff8346206fee2177533eb35f5c` | same | PASS |
| `articles-aib-af-reconciliation` | `efb6a511703339ecffcfcffbfea7d808d3323760a33606f1b244d10ec64f34dc` | same | PASS |
| `articles-aib-af-statements` | `628958a7a9a32fd78f27a711341f8fe57f92de57399af44a9201a6afb2308975` | same | PASS |

The shared filename/topic sweep covered AIB AF near-neighbors plus the directly related Control Panel, payment-method, currency, pricing, role-permission, statement, and reconciliation raws. Relevant nearby raws have source owners; no reusable unlinked raw gap was found. Processor/account variants (AIB BF, Wells, Chase, Adyen, APAC, AU, BR, Moneris, NAB) were not imported into these AIB AF answers, and no automatic historical full read was performed.

One extra source/raw pair was fully read because the main payment-method concept exposes a relevant conflict: `wiki/sources/braintree/source-braintree-get-started-payment-methods.md` and `raw/braintree/articles/get-started/payment-methods-2026-09-16.md`. The provider-wide raw says Visa Click to Pay/Secure Remote Commerce will no longer be supported after 2026-01-20 (`raw/.../get-started/payment-methods-2026-09-16.md:14-15`) but later calls SRC a current limited release (`:87-89`). The selected AIB AF raw repeats limited-release wording (`raw/.../aib-af/transactions/accepted-payment-methods-2026-09-16.md:89-91`), so current SRC support remains unresolved; this qualification is preserved below. The selected reconciliation and statements raws were both fully read, resolving their direct Funding Totals cross-reference without another read.

## `articles-aib-af-transactions-descriptors` — PASS

**Route:** `wiki/index.md:11` → `wiki/braintree-index.md:516` → `wiki/concepts/braintree-control-panel.md:22` → `wiki/sources/braintree/source-braintree-articles-aib-af-transactions-descriptors.md:40,43-45` → `raw/braintree/articles/aib-af/transactions/descriptors-2026-09-16.md:1`.

1. **Scope — PASS.** This is the Braintree-hosted AIB AF descriptor document for purchases through a merchant's app or website. It covers application-derived hard/soft descriptors and per-transaction dynamic descriptors. It does not define AF, establish AIB BF equivalence, or state a general region, account-eligibility, or pricing rule. The customer's bank controls final statement rendering. Evidence: source `:14,23-24`; raw `:14-25,27-37`.
2. **Purpose/action/conditions/warnings — PASS.** It defines soft, hard, and dynamic descriptors; requires merchant name plus clearing city or phone; routes hard/soft changes through Braintree, PayPal changes through the PayPal console, and Amex changes directly through Amex. Hard/soft constraints are at raw `:42-57`; refund reuse and dynamic composition are at `:60-68`; exact dynamic name/phone/URL limits are at `:71-99`. The refund default is descriptor reuse, not proof of refund, settlement, or funding, and the API link at `:101` is navigation only. Source locator summary: `:26-35`.

## `articles-aib-af-transactions-accepted-payment-methods` — PASS

**Route:** `wiki/index.md:11` → `wiki/braintree-index.md:510` → `wiki/concepts/braintree-payment-methods.md:25` → `wiki/sources/braintree/source-braintree-articles-aib-af-transactions-accepted-payment-methods.md:51,65-67` → `raw/braintree/articles/aib-af/transactions/accepted-payment-methods-2026-09-16.md:1`.

1. **Scope — PASS.** This is the exact AIB AF account article. It says Visa, Mastercard, and Maestro are default (`raw:17-24`); Amex requires a separate Amex account and a pricing-agreement check (`:27-45`); transactions use the merchant-account currency, with another merchant account and merchant-account-ID selection needed for another currency (`:94-100`). It supplies no fixed fee values and must not be transferred to AIB BF, another processor, region, or merchant account. Source: `:14,18-26`.
2. **Purpose/action/conditions/warnings — PASS.** The page identifies separately enabled methods and setup constraints: Maestro same-country/3DS/recurring behavior and the eventual rejection of Control Panel card-number entry (`raw:50-58`); JCB and Discover/Diners conditions (`:61-68`); PayPal, Apple Pay, Google Pay, and qualified SRC routes (`:71-91`); and conversion-fee/refund/chargeback friction plus added-currency setup (`:94-100`). Exact locator index: source `:34-46`. The material unresolved conflict is SRC availability: the same-date provider-wide raw contains the opposing end-of-support and limited-release statements cited in the shared check, so neither current-support claim is treated as conclusive.

## `articles-aib-af-reconciliation` — PASS

**Route:** `wiki/index.md:11` → `wiki/braintree-index.md:527` → `wiki/concepts/payment-reconciliation-reporting.md:113` → `wiki/sources/braintree/source-braintree-articles-aib-af-reconciliation.md:46,48-50` → `raw/braintree/articles/aib-af/reconciliation-2026-09-16.md:1`.

1. **Scope — PASS.** This is ordinary AIB AF reconciliation using the AIB Merchant Statement and AIB Transaction Fee Report, distinct from AIB AF `Reconciliation (LR)` and AIB BF. It states no region or applicable pricing model; it says to use Total Fee Amount regardless of pricing model and supplies no fee schedule. Evidence: source `:14-16,24,29-30`; raw `:17-24,82-93`.
2. **Purpose/action/conditions/warnings — PASS.** General reconciliation compares Funding Totals with deposits (`raw:17-19`); transaction-level work requires the Create, Run, and Download Reports permission, merchant-account/date selection, and wider settlement-date coverage (`:27-43`), then a Processing Date PivotTable and net-settlement calculation (`:46-58`), statement download (`:61-70`), and date matching with rounding/adjacent-date techniques (`:73-79`). Settlement Amount and Total Fee Amount meanings are at `:82-93`. The typical one-business-day timing and statement/report records are matching guidance, not deposit-arrival proof. Source locator index: `:32-41`.

## `articles-aib-af-statements` — PASS

**Route:** `wiki/index.md:11` → `wiki/braintree-index.md:516` → `wiki/concepts/braintree-control-panel.md:20` → `wiki/sources/braintree/source-braintree-articles-aib-af-statements.md:43,46-48` → `raw/braintree/articles/aib-af/statements-2026-09-16.md:1`.

1. **Scope — PASS.** This is the Braintree-hosted AIB AF monthly statement document. It covers Control Panel access, batch processing detail, pricing-sensitive statement fields, other applicable fees, and Funding Totals. It does not define AF, establish AIB BF equivalence, or provide current region/account eligibility or pricing authority. IC+ interchange display is conditional, and fee columns depend on the merchant's pricing model. Evidence: source `:14-16,20-27`; raw `:49-75`.
2. **Purpose/action/conditions/warnings — PASS.** Statements are available by the ninth business day and require the View Statements permission (`raw:14-25`). Processing Details field meanings are at `:30-46`; Merchant Service Charges and IC+-qualified interchange/scheme fields at `:49-70`; optional non-processing fees and blank VAT fields at `:73-87`; Funding Totals and bank-statement text at `:90-94`. Funding Totals describes completed transfers in the billing period but does not independently prove receipt, availability, or a specific transaction's success. Source locator index: `:32-38`.

## Final disposition

All four canonical concept routes are query-ready. All eight fixed answers are directly supported by the selected source/raw evidence, all four raw hashes match the approved manifest, reciprocal concept/source/raw routes resolve, and no material unlinked evidence gap was found. Preserve the one SRC conflict qualification when answering availability questions. **Group C verdict: PASS; failures: none.**
