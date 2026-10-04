# C38 fixed query audit — Group E

Scope: jobs 17–20 and exactly eight fixed questions from `tracking/ingest/braintree/braintree-campaign-38/selection-review.md`. Overall verdict: **8/8 PASS**.

## `articles-br-transactions-accepted-payment-methods`

Route: `wiki/index.md:11` → `wiki/braintree-index.md:553` → `wiki/concepts/braintree-payment-methods.md:25` → `wiki/sources/braintree/source-braintree-articles-br-transactions-accepted-payment-methods.md:1-47` → `raw/braintree/articles/br/transactions/accepted-payment-methods-2026-09-16.md:1-44`.

1. **PASS — Scope.** This is the Braintree-hosted BR-path Accepted Payment Methods article, updated 2025-04-01 and fetched 2026-09-16 (`raw:1-10`). Its account-scoped wording says the account is set up by default for Visa, Mastercard, Amex, Elo and Hipercard (`raw:17-26`); Brazil combo-card, local-acquirer Amex and BRL qualifications make it neither a provider-wide nor sibling-route capability claim (`raw:29-43`).

2. **PASS — Purpose, action and consequential conditions.** The page identifies the default card bundle; for Brazilian combo cards it directs the integration to send `account_type` in 3DS and/or the transaction sale call and requires a customer account-type choice because no combo-card indicator exists (`raw:29-31`). It says locally acquired Amex is default with no separate Amex merchant-account application and assigns Amex funding, descriptors, chargebacks, support and statement inclusion to Braintree (`raw:34-38`). Transactions use the merchant account's BRL; customer-bank conversion may add fees, and refund difficulty may increase chargebacks (`raw:41-43`).

## `articles-br-transactions-descriptors`

Route: `wiki/index.md:11` → `wiki/braintree-index.md:559` → `wiki/concepts/braintree-control-panel.md:20` → `wiki/sources/braintree/source-braintree-articles-br-transactions-descriptors.md:1-43` → `raw/braintree/articles/br/transactions/descriptors-2026-09-16.md:1-40`.

1. **PASS — Scope.** This is a Braintree Brazil-path descriptor snapshot, updated 2025-04-01 and fetched 2026-09-16 (`raw:1-10`), for statement identification after mobile-app or website purchases (`raw:14-20`). It documents an account-level format and does not name a processor, environment, card brand, payment method or pricing model; the customer's bank controls final rendering (`raw:16-20`).

2. **PASS — Purpose, action and consequential conditions.** The descriptor identifies the charge after authorization and settlement and becomes permanent when the bank finalizes status (`raw:16-20`). The account permits 22 characters: an eight-character hardcoded common prefix, `*`, then at most 13 merchant-account-level characters, with only letters and numbers stated as allowed after the prefix (`raw:23-30`). The examples conflict with those stated restrictions (short prefix and a space), so the snapshot supplies no resolved validator rule (`raw:32-37`). Braintree configures the value from application information; requested changes go through Contact us with the restrictions supplied (`raw:39`).

## `articles-moneris-overview`

Route: `wiki/index.md:11` → `wiki/braintree-index.md:552` → `wiki/concepts/braintree-payment-platform.md:28` → `wiki/sources/braintree/source-braintree-articles-moneris-overview.md:1-45` → `raw/braintree/articles/moneris/overview-2026-09-16.md:1-23`.

1. **PASS — Scope.** This is a Braintree-hosted Moneris navigation portal, updated 2025-04-01 and fetched 2026-09-16 (`raw:1-10`). Receipt of its link means **at least one** of the recipient's merchant accounts is provisioned and funded by Moneris (`raw:22`); it does not identify a region, pricing model or every account, nor provide independent Moneris authority.

2. **PASS — Purpose, action and consequential conditions.** The page routes the recipient to account-tailored articles that are available only by direct link and recommends bookmarking the portal because support-site search will not find them (`raw:14-18`). Banking-partner differences can change accepted payment types, generic public articles may omit important details, partner assignment depends mostly on signup timing and business domicile, and multiple merchant accounts may use multiple partners (`raw:20`). The portal itself therefore does not establish a linked article's instructions or outcomes.

## `articles-br-transactions-three-d-secure-processing-requirements`

Route: `wiki/index.md:11` → `wiki/braintree-index.md:545` → `wiki/concepts/braintree-3d-secure.md:22` → `wiki/sources/braintree/source-braintree-articles-br-transactions-three-d-secure-processing-requirements.md:1-42` → `raw/braintree/articles/br/transactions/three-d-secure-processing-requirements-2026-09-16.md:1-36`.

1. **PASS — Scope.** This is the Brazil-path 3D Secure Processing Requirements article, updated 2025-04-02 and fetched 2026-09-16 (`raw:1-10`). The named applicable card types are Visa and Mastercard (`raw:17-23`), while the operative statements distinguish Visa debit cards from Mastercard debit cards; the page does not state a rule for other brands, credit cards, pricing, another region or every Braintree transaction.

2. **PASS — Purpose, action and consequential conditions.** For Brazilian Visa debit, issuers only **tend** to approve at higher rates when 3DS-authenticated (`raw:26-28`). For Mastercard debit, the page reports a Mastercard requirement to use either standard or data-only 3DS (`raw:31-33`). Braintree consequently recommends 3DS authentication for debit cards to seek the highest approval rates (`raw:35`); this is not an approval guarantee, general Visa mandate, liability-shift statement or payment-success proof.

## Shared checks

All four selected source pages and pinned raws were read completely. Recomputed SHA-256 values match manifest lines 161–194: accepted methods `7c04114340228cd9db2593c32b0039f6881cf914393155b6324954f69cff7611`; descriptors `fc48e9707b05aef352152647433da57a183fe4d1f633c44633be1316b503b144`; Moneris overview `6d88f6a697c8f449eb81d41c8541f6aadc2b00c5a96d1b322d24f9c5d004bb70`; 3DS requirements `193637695ba0ce7dc9458f3d40ac068c8229f78ea70bc6afb937ebcd94b5fe21`. Embedded raw URLs match source canonical URLs. Each source links to its selected main concept and pinned raw, and each main concept links back to the source. The provider index exposes each selected concept; the deferred direct source catalog was not treated as a missing route.

The bounded filename/object/action sweep found only the four selected BR/Moneris pages plus the distinct Moneris accepted-methods and descriptors siblings. Those siblings have different requested objects/account scope and are unnecessary to these answers. No selected source has navigation-only related raw references. No additional full raw read was needed; the only material conflict used is internal to the fully read BR descriptors raw.

Analysis end UTC: `2026-10-04T09:07:28Z`.
Handoff UTC: `2026-10-04T09:08:13Z`.
