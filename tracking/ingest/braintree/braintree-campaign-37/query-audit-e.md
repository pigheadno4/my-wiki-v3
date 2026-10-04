# C37 fixed query audit E — jobs 17–20

Result: **PASS — 8/8 fixed questions.** Analysis ended: `2026-10-04T07:42:09Z`.

## 17. `articles-apac-change-your-bank-account`

Route: `wiki/index.md:11` → `wiki/braintree-index.md:552` → `wiki/concepts/braintree-payment-platform.md:28` → `wiki/sources/braintree/source-braintree-articles-apac-change-your-bank-account.md` → `raw/braintree/articles/apac/change-your-bank-account-2026-09-16.md` (`sha256:7db6eab4504cd5f6400c9f78d011c0c4e737b18b97ddb6bc4c24e010365192cb`).

1. **Q1 — PASS.** This is the captured Braintree APAC route for the checking account supplied with the original business application and used for settled-transaction payouts. It names no banking partner or processor, does not enumerate APAC eligibility, and says nothing about pricing. Its document scope is a preferred voided check or, alternatively, a direct-deposit form or bank statement issued within three months; the replacement must be a business checking account domiciled in the same country as the business. Account/payout scope: raw `16`; document and recency scope: `18`; same-country/account-type scope: `39-40`.
2. **Q2 — PASS.** The documented action is to update business bank-account information by uploading the new-account evidence through the Business Uploads Tool in the Control Panel. Online-banking-profile screenshots are rejected; the document must include bank name/address, issue date, legal business name as account holder, account number, BIC/SWIFT and applicable sort code. Hong Kong, Malaysia and Singapore have distinct listed sort-code fields; savings, deposit-only and prepaid debit accounts are rejected. The UI procedure proves neither API presence/absence nor permission, approval, completion or payout arrival. Action/alternatives: raw `18`; screenshot warning: `21-22`; required fields: `26-34`; country-specific sort codes: `36`; account exclusions: `39-40`.

## 18. `articles-apac-overview`

Route: `wiki/index.md:11` → `wiki/braintree-index.md:552` → `wiki/concepts/braintree-payment-platform.md:38` → `wiki/sources/braintree/source-braintree-articles-apac-overview.md` → `raw/braintree/articles/apac/overview-2026-09-16.md` (`sha256:bfaea7650819a486f482e7211bd350e9c53d904280a2a4bd9009ed347ce1698a`).

1. **Q1 — PASS.** The audience is a recipient with at least one merchant account provisioned by an unnamed banking partner in the Asia-Pacific region. The page does not say every account is so provisioned, identify the partner or a processor, establish who funds the account, or document bank-change evidence or pricing. Exact account/region condition: raw `17-18`; partner variability and multiple-account qualification: `26`.
2. **Q2 — PASS.** This page is a direct-link-only portal to account-tailored articles. It warns that public support content can omit important details because accepted payment types and other processing behavior vary by banking partner; partner assignment was determined during application, mostly by signup timing and business domicile, and multiple merchant accounts can use multiple partner banks. It recommends bookmarking the portal. Portal/search limitation: raw `22`; bookmark action: `24`; variability, application factors and multi-bank qualification: `26`.

## 19. `articles-au-overview`

Route: `wiki/index.md:11` → `wiki/braintree-index.md:552` → `wiki/concepts/braintree-payment-platform.md:29` → `wiki/sources/braintree/source-braintree-articles-au-overview.md` → `raw/braintree/articles/au/overview-2026-09-16.md` (`sha256:8b29cc5312d42b7d36602cf84ebdff0fec67c6ec2f1b21cf0fdc20d14460e732`).

1. **Q1 — PASS.** The audience condition is Braintree Direct plus at least one merchant account located in Australia and funded by Braintree. It does not say every account meets that condition, name another processor or bank, or specify documents, pricing, accepted methods, account-change rules or reconciliation resources. Exact product/location/funding condition: raw `17-18`; topics named only as examples of setup-dependent nuance: `22`.
2. **Q2 — PASS.** The page routes the recipient from generic public support material to location- and setup-sensitive account articles. Those articles are accessible only by direct link, are not public-search discoverable, and should be bookmarked. The portal itself does not establish any destination article's instructions, values, current eligibility or outcomes. Portal purpose and example nuance categories: raw `22`; direct-link/search/bookmark limitation: `24`.

## 20. `articles-br-overview`

Route: `wiki/index.md:11` → `wiki/braintree-index.md:552` → `wiki/concepts/braintree-payment-platform.md:30` → `wiki/sources/braintree/source-braintree-articles-br-overview.md` → `raw/braintree/articles/br/overview-2026-09-16.md` (`sha256:f2beac23c91b77a4e9569e8286cc4e7076e4da3db041160d9672a443303833ab`).

1. **Q1 — PASS.** The audience condition is Braintree Direct plus at least one merchant account located in Brazil and funded by Braintree. It does not say every account meets that condition, define additional meaning for the `br` path, name another processor or bank, or specify documents, pricing, accepted methods, account-change rules or reconciliation resources. Exact product/location/funding condition: raw `17-18`; topics named only as examples of setup-dependent nuance: `22`.
2. **Q2 — PASS.** The page is the portal from generic public support material to location- and setup-sensitive account articles. Those articles are direct-link-only, absent from public-support search, and the page recommends bookmarking the portal. The overview supplies no destination article's instructions, values, present eligibility or outcome evidence. Portal purpose and example nuance categories: raw `22`; direct-link/search/bookmark limitation: `24`.

## Shared checks and extra reads

- All four manifest paths, canonical URLs and SHA-256 values match the live source frontmatter and pinned raw bytes. The provider index also lists all four sources at `wiki/braintree-index.md:41-44`; each source reciprocally identifies `[[braintree-payment-platform]]` and its exact raw file.
- Fully read the four source pages, four pinned raw files, `wiki/concepts/braintree-payment-platform.md`, and the relevant administration concept `wiki/concepts/braintree-control-panel.md`. The latter's general statement that most Control Panel functions can also be automated does not establish a bank-account-change API and creates no retained-claim conflict.
- Exact-topic filename sweep found no alternate APAC change/overview, AU overview or BR overview raw version. The AU bank-change sibling and the APAC source's two navigation-only related raws were not read because neither is needed to answer these fixed page queries and sibling behavior must not be transferred.
- Scope separation held: APAC overview means banking-partner provisioning and does **not** establish Braintree funding; AU and Brazil overview mean the explicit Braintree Direct, at-least-one-account, location and Braintree-funded conditions and do **not** import APAC partner-provisioning semantics.

Handoff recorded: `2026-10-04T07:43:13Z`.
