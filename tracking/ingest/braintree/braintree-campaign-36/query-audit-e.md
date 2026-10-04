# Braintree C36 fixed query audit E

- Analysis completed UTC: `2026-10-04T07:10:57Z`
- Coverage: `4/4` exact pages, `8/8` predetermined questions, `4/4` pinned raw SHA-256 values.
- Verdict: **PASS** (`8/8` question cells).
- Material failures: **none**.

## `articles-aib-af-change-your-bank-account` — PASS

**Route:** `wiki/index.md:11` `[[braintree-index]]` → `wiki/braintree-index.md:531` `[[braintree-payment-platform]]` → `wiki/concepts/braintree-payment-platform.md:34` `[[source-braintree-articles-aib-af-change-your-bank-account]]` → `wiki/sources/braintree/source-braintree-articles-aib-af-change-your-bank-account.md:54` → `raw/braintree/articles/aib-af/change-your-bank-account-2026-09-16.md`. Direct source catalog: `wiki/braintree-index.md:41`. Pinned and actual SHA-256: `9b017bb4a606fdefcd2b885cbde12fe7fa380aa00c2d175017828c656b4b7913`.

- **Q1 PASS — exact scope:** Captured Braintree-hosted **AIB AF** article for the business checking account supplied with the original application and used for settled-transaction payouts. It defines no region, pricing model, AF expansion, current eligibility, or BF/other-processor applicability (`raw:14-18`; source `:12-16`). Its document scope is exactly a bank statement or signed bank letter for the replacement account.
- **Q2 PASS — purpose/action/conditions/warnings/locators:** Request the change through the Control Panel Business Uploads Tool (`raw:18`). Online-banking-profile screenshots are rejected (`raw:21-22`). Statement requirements—legal business name, IBAN, BIC/SWIFT, currency, English-alphabet characters, issue date within three months—are at `raw:29-36`; signed bank-letter requirements, including official letterhead, bank-representative signature and six-month recency, are at `raw:39-48`. The replacement must be a business checking account; savings, deposit-only and prepaid debit accounts are rejected (`raw:51-52`). Upload is not acceptance/completion proof, and the UI procedure establishes neither API presence nor absence (source `:20-30`).

## `articles-aib-af-transactions-settlement-funding-timeline` — PASS

**Route:** `wiki/index.md:11` `[[braintree-index]]` → `wiki/braintree-index.md:531` `[[braintree-payment-platform]]` → `wiki/concepts/braintree-payment-platform.md:28` `[[source-braintree-articles-aib-af-transactions-settlement-funding-timeline]]` → `wiki/sources/braintree/source-braintree-articles-aib-af-transactions-settlement-funding-timeline.md:54` → `raw/braintree/articles/aib-af/transactions/settlement-funding-timeline-2026-09-16.md`. Direct source catalog: `wiki/braintree-index.md:42`. Pinned and actual SHA-256: `ed030747b0b4165b2be21fb2ccce9062c7421590e6873447a69a6649a268fd70`.

- **Q1 PASS — exact scope:** Captured Braintree-hosted **AIB AF** post-settlement schedule for the merchant account-to-bank-account path. The raw gives a 6 p.m. Central Time (US) account cutoff, but does not identify a merchant region or pricing model, define AF, or establish BF/other-account applicability (`raw:16,27`; source `:14-16,29-30`). AIB disburses card funds only after successful settlement; PayPal funding is separate from the Braintree-managed account (`raw:29,47-49`).
- **Q2 PASS — purpose/action/conditions/warnings/locators:** First deposit has an additional 10-business-day delay (`raw:22-23`). Transactions are batched and sent to the processing bank to confirm settlement; submissions after the fixed cutoff enter the next batch (`raw:27`). After successful settlement, stated deposit schedules are 2–3 business days for Visa/Mastercard/Discover/Maestro and 2–8 for Amex; Amex owns its cutoff and direct disbursement (`raw:29-35`). Default weekday disbursement, weekend/bank-holiday rollover, another typical visibility day, and optional weekly/monthly cadence are at `raw:37-39`; Apple Pay/Google Pay alignment is at `raw:42-44`. Schedules do not prove settlement, sending or arrival (source `:26-30`). The current source chronology is correct: batching confirms settlement, then AIB disburses after successful settlement (source `:14,21-22`; raw `:27-29`).

## `articles-aib-af-overview` — PASS

**Route:** `wiki/index.md:11` `[[braintree-index]]` → `wiki/braintree-index.md:531` `[[braintree-payment-platform]]` → `wiki/concepts/braintree-payment-platform.md:32` `[[source-braintree-articles-aib-af-overview]]` → `wiki/sources/braintree/source-braintree-articles-aib-af-overview.md:41` → `raw/braintree/articles/aib-af/overview-2026-09-16.md`. Direct source catalog: `wiki/braintree-index.md:43`. Pinned and actual SHA-256: `1ce4b837f69f7aa2d9fe0f3e5dab048439b71f5ae0f54ff5668475b255b83358`.

- **Q1 PASS — exact scope:** Captured Braintree-hosted **AIB AF path** portal. Receipt of the link means **at least one** merchant account is both provisioned and funded by AIB (`raw:22`), not every account. It does not define AF, identify a region or pricing model, enumerate accepted methods, or establish any destination article's behavior (`source:14-25`).
- **Q2 PASS — purpose/action/conditions/warnings/locators:** Use and bookmark the direct-link-only account-tailored portal; its articles cannot be found through support-site search (`raw:16-18`). Banking-partner-dependent details can make generic public articles incomplete; partner assignment was determined during application, mostly by signup time and business domicile, and multiple merchant accounts can use multiple partner banks (`raw:20`). The page is navigation/account-scope evidence only, not payment, settlement or funding execution evidence (`source:16,24-25`).

## `articles-aib-bf-overview` — PASS

**Route:** `wiki/index.md:11` `[[braintree-index]]` → `wiki/braintree-index.md:531` `[[braintree-payment-platform]]` → `wiki/concepts/braintree-payment-platform.md:30` `[[source-braintree-articles-aib-bf-overview]]` → `wiki/sources/braintree/source-braintree-articles-aib-bf-overview.md:40` → `raw/braintree/articles/aib-bf/overview-2026-09-16.md`. Direct source catalog: `wiki/braintree-index.md:44`. Pinned and actual SHA-256: `81057bab06ce30f248376aa6c4ee0cafaf832500527483a75cacd2604ed62251`.

- **Q1 PASS — exact scope:** Captured Braintree-hosted **AIB BF path** portal. Receipt of the link means **at least one** merchant account is provisioned by AIB and **funded by Braintree** (`raw:22`), not every account. It does not define BF, identify a region or pricing model, state accepted methods, or establish destination-article behavior (`source:14,19-24`). This preserves the material contrast with AF's AIB-provisioned-and-AIB-funded account.
- **Q2 PASS — purpose/action/conditions/warnings/locators:** Use and bookmark the direct-link-only account-tailored portal (`raw:16-18`). Banking-partner variability, possible omissions in generic public articles, application-time partner selection, signup/domicile factors and possible multiple partner banks are at `raw:20`. The overview provides no detailed payment, settlement, funding, eligibility or pricing instructions; those require a separately read destination (`source:18-24`).

## Shared gap sweep / extra reads

- Read in full: root index, Braintree index, `braintree-payment-platform`, all four selected source pages and all four selected raws. All source `canonical_url`, `raw_files` and `## Raw Sources` routes agree with the manifest/raw identity. Root → provider index → concept → source → raw routing is reciprocal for every page; no ordered edge is missing.
- Focused filename/content sweep found the sibling AIB BF bank-change/timeline pages, other processor/account variants, and the two authorization raws explicitly outside C36. None is needed to answer these page-local fixed questions or resolve a selected-evidence conflict. The selected AF timeline was the only linked destination also in this group and was already read fully. No historical-version full read or other extra raw full read was performed.
- The linked account-information, accepted-payment-method and PayPal-funding destinations remain navigation only: no retained answer depends on their unverified contents. No material unlinked evidence gap or selected-evidence contradiction was found.
- Campaign event evidence records the AF timeline's initial chronology failure and bounded correction (`events.jsonl:103,108`). The present approved source matches raw chronology at `raw:27-29`; the defect is not present in the audited page.

- Handoff UTC: `2026-10-04T07:11:25Z`
