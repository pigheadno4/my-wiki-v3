# Braintree C34 fixed-query audit — group C

- Scope: `articles-adyen-pricing-fees`, `articles-adyen-change-your-bank-account`, `articles-chase-pricing-fees`, `articles-risk-and-security-allowlisting`
- Result: **PASS — 8/8 approved questions answered from the exact selected sources and pinned raw files**
- Material retrieval failures: **none**
- Repository changes by auditor: **none**

## Shared evidence and route checks

- Root route is present at `wiki/index.md:5-11`; the Braintree index contains the four exact source routes at `wiki/braintree-index.md:23-31,40-46` and the relevant concept routes at `wiki/braintree-index.md:488-495`.
- Reciprocal concept/source links pass. `wiki/concepts/braintree-payment-platform.md:32-34` links all three processor/account sources, and each links back as its main concept (`source-braintree-articles-adyen-pricing-fees.md:34-39`, `source-braintree-articles-adyen-change-your-bank-account.md:42-47`, `source-braintree-articles-chase-pricing-fees.md:38-41`). `wiki/concepts/braintree-control-panel.md:23` links the allowlisting source, which links back at `source-braintree-articles-risk-and-security-allowlisting.md:37-41`.
- Each source's `raw_files` entry and `Raw Sources` link resolve to its manifest-pinned raw. SHA-256 verification passed exactly:

| Exact job ID | Pinned raw | Verified SHA-256 |
| --- | --- | --- |
| `articles-adyen-pricing-fees` | `raw/braintree/articles/adyen/pricing-fees-2026-09-16.md` | `33c26fc49d02df6b414cb2589d8e31dcf81aac59b061fbce95ceb6d57063d71b` |
| `articles-adyen-change-your-bank-account` | `raw/braintree/articles/adyen/change-your-bank-account-2026-09-16.md` | `dbd533ae2ecd5c17319fad07b2277dd9585a088da9004c446459a9b8a806a62d` |
| `articles-chase-pricing-fees` | `raw/braintree/articles/chase/pricing-fees-2026-09-16.md` | `037dd1c09078ffe9fa76627aabc7b9dbc3855ba25f7807af9a45e3b61f9ff61c` |
| `articles-risk-and-security-allowlisting` | `raw/braintree/articles/risk-and-security/allowlisting-2026-09-16.md` | `ff45c19e66ba209a8de40b5d86fede1895ef05fa1e7f2fce371e2812862a1035` |

- Shared authority boundary: all four are Braintree-hosted documentation snapshots fetched 2026-09-16. The Adyen and Chase pages are Braintree processor/account documentation, not independent present-day Adyen or Chase authority. No present-day rate or universal availability inference is made.

## 1. `articles-adyen-pricing-fees`

**Route:** `wiki/index.md:5-11` → `wiki/braintree-index.md:488` → `wiki/concepts/braintree-payment-platform.md:32` → `wiki/sources/braintree/source-braintree-articles-adyen-pricing-fees.md:1-48` → `raw/braintree/articles/adyen/pricing-fees-2026-09-16.md:1-78`.

**Q1 — PASS.** The object is the fee model and fee reporting for Braintree merchants in the page's Adyen-processor context. The raw calls IC++ the standard model for these Adyen merchants, comprising markup or applicable commission, per-transaction, interchange, and scheme fees; actual assessment varies primarily by card type and also by merchant type, sale cost, processing technology, region, and other factors (`raw/.../adyen/pricing-fees-2026-09-16.md:41-43`). It gives fee categories and treatment, not numeric rates, a merchant-specific contract, independent Adyen policy, or universal/current rates. Aggregated-versus-direct Amex account scope is at lines 34-38.

**Q2 — PASS.** The central commercial action is to calculate and deduct the documented fees with payout, using the converted settlement amount when presentment and settlement currencies differ (`raw/.../adyen/pricing-fees-2026-09-16.md:17-31`), and expose assessed fees through the payout-generated Settlement Details Report (`:49-56`). Material qualifications: successful transactions receive markup/per-transaction/interchange/scheme treatment, while refunds, verifications, voids, and gateway rejections receive only the per-transaction fee (`:22-31`); the monthly invoice covers settled-month transactions, does not match paid-account report coverage, and must not be used for reconciliation (`:59-65`); refunds do not return original transaction fees (`:70-72`); chargebacks/pre-arbitrations incur an outcome-independent non-refundable fee while retrievals do not in this snapshot (`:75-77`).

## 2. `articles-adyen-change-your-bank-account`

**Route:** `wiki/index.md:5-11` → `wiki/braintree-index.md:488` → `wiki/concepts/braintree-payment-platform.md:33` → `wiki/sources/braintree/source-braintree-articles-adyen-change-your-bank-account.md:1-56` → `raw/braintree/articles/adyen/change-your-bank-account-2026-09-16.md:1-60`.

**Q1 — PASS.** The object is the business checking account used for settled-transaction payouts on the documented Braintree account in its Adyen-processor context; it is not an independent Adyen-account procedure and not proof of an individual payout or deposit. The raw states no general regional availability or fee rate. Its geographic qualification is same-country domicile for the business and new checking account (`raw/.../adyen/change-your-bank-account-2026-09-16.md:38-39`); its multi-currency qualification is one checking account per configured settlement currency, settlement-currency deposits, and Adyen fee debits in the original application's GBP-or-EUR base currency (`:57-59`).

**Q2 — PASS.** The merchant action is to upload a recent statement for the new account through the Control Panel Business Uploads Tool; Braintree Support reviews it and follows up with the Braintree account's authorized signer (`raw/.../adyen/change-your-bank-account-2026-09-16.md:16-18,26-35`). The statement must show the matching DBA/legal account-holder name, currency, bank insignia, IBAN, and BIC/SWIFT (`:26-35`); online-banking screenshots are rejected (`:21-22`); savings, deposit-only, prepaid debit, and non-same-country accounts are rejected (`:38-39`). Only the authorized signer may request or change sensitive account information; that signer is not the Account Admin, cannot be managed in the Control Panel, and must answer security questions on a support call (`:44-52`).

## 3. `articles-chase-pricing-fees`

**Route:** `wiki/index.md:5-11` → `wiki/braintree-index.md:488` → `wiki/concepts/braintree-payment-platform.md:34` → `wiki/sources/braintree/source-braintree-articles-chase-pricing-fees.md:1-45` → `raw/braintree/articles/chase/pricing-fees-2026-09-16.md:1-60`.

**Q1 — PASS.** The object is fee treatment in this Braintree-owned Chase/Paymentech processing context. The merchant's account-selected model is either blended or IC+: blended is Braintree processing fees with possible account-dependent debit/credit differences; IC+ combines Braintree processing and variable interchange, with assessment depending mainly on card type plus merchant type, sale cost, technology, region, and other factors (`raw/.../chase/pricing-fees-2026-09-16.md:37-49`). This is not independent Chase authority and does not establish universal/current rates or current merchant eligibility.

**Q2 — PASS.** The central commercial action is deduction of the listed transaction fees from daily disbursements for successful sale transactions; the raw excludes refunds, verifications, declines, gateway rejections, and voids, and routes processing-fee reporting to Paymentech Online (`raw/.../chase/pricing-fees-2026-09-16.md:17-28`). A merchant using its own Amex account avoids Braintree's discount rate on that transaction but still owes Braintree's per-transaction fee plus interchange and direct Amex fees (`:31-32`). The model was fixed at signup and support is the account-specific route (`:37-39`); Chase owns reporting (`:52-54`). The collected page states a $15 non-refundable chargeback/pre-arbitration fee regardless of outcome and no retrieval fee "at this time" (`:57-59`); this is reported only as a snapshot value, not a present-day or universal rate.

## 4. `articles-risk-and-security-allowlisting`

**Route:** `wiki/index.md:5-11` → `wiki/braintree-index.md:495` → `wiki/concepts/braintree-control-panel.md:23` → `wiki/sources/braintree/source-braintree-articles-risk-and-security-allowlisting.md:1-49` → `raw/braintree/articles/risk-and-security/allowlisting-2026-09-16.md:1-60`.

**Q1 — PASS.** The object is merchant-configured IP-address/hostname restrictions on access to the Braintree Gateway Control Panel and server-to-server API calls (`raw/.../risk-and-security/allowlisting-2026-09-16.md:17-22,30`). It is explicitly not the separate task of allowing Braintree-owned IP addresses/domains through merchant infrastructure (`:17-18`). The page states no region or pricing model; it establishes a gateway access-control scope only. Browser-originated encrypted client-SDK calls, including nonce requests, remain outside the allowlist (`:30`).

**Q2 — PASS.** A user with the **Edit IP Restrictions** permission enters an IP address or hostname in Control Panel → API → Security → IP and Hostname Restrictions, chooses Control Panel access, API access, or both, adds entries, and enables restrictions (`raw/.../risk-and-security/allowlisting-2026-09-16.md:33-48`). Once enabled, unlisted sources are denied and denylisting is unsupported (`:22-26`). Granting only one access type blocks the other; sandbox testing is recommended before production (`:51-52`). Wildcard hostname/subnet matching and CIDR are supported (`:57-59`). These instructions do not prove present configuration or successful enforcement.

## Gap sweep and extra reads

- Filename sweep covered `pricing-fees`, `fee`, `change-your-bank-account`, `account-information`, `allowlisting`, `ip-address`, `role-permissions`, `settlement-funding-timeline`, `reporting-reconciliation`, and `chargebacks-retrievals` under `raw/braintree/`.
- The sweep found analogous regional/processor pages, but they are different account/processor scopes and were not imported into these answers. No conflict in the four selected source/raw pairs required cross-processor evidence.
- Related navigation inspected: Adyen settlement/funding and dispute overview; account-information and Adyen settlement/funding; Braintree IP-address/domain reference; role-permission route; Chase reporting/reconciliation. No extra raw was needed to answer the approved questions: the exact selected raws already contain the asserted fee treatment, bank-document/signer requirements, access scope, permission, procedure, and warnings. Per the query rule, navigation-only references remain non-evidence unless fully read.

## Close assessment

**PASS.** All eight questions restate the correct object and action, preserve processor/account/snapshot scope, supply detailed raw locators, and avoid present-day-rate or universal-availability inference. No material retrieval failure or conflict blocks group C.

Analysis ended UTC: `2026-10-04T05:16:02Z`
Artifact completed UTC (`completionUTC`): `2026-10-04T05:17:26Z`
