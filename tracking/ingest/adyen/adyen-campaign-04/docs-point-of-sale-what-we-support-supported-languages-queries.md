# Fixed retrieval checks — Adyen in-person locations and terminal languages

## Purpose, scope, and limits

**Query:** Which support question does this page answer, and what should a reader not infer from it?

**Answer:** It is a 2026-09-15 capture of Adyen's country/region and payment-terminal **UI-language** support tables for **all Adyen in-person integration types**, with a 2025-02-10 `last_modified` value. It does not prove current merchant/account, terminal, payment-method, or Mobile eligibility. It also does not document shopper language-selection mechanics, terminal system language, receipt language, BCP-47/ISO codes, default-selection behavior, or a Terminal API language control field (raw lines 5–27, 29–94). Route after catalog update: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-terminal-api.md` (related in-person route; broader source) → `wiki/sources/adyen/source-adyen-docs-point-of-sale-what-we-support-supported-languages.md` → `raw/adyen/docs/point-of-sale/what-we-support/supported-languages/2026-09-15.md`.

## Central support tables and warnings

**Query:** How should the region and terminal-language tables be read?

**Answer:** Use the country/region tables for the captured Americas/APAC/Europe/Middle East list, including the UK note that includes Guernsey and Isle of Man but excludes Jersey and other overseas territories/crown dependencies, and the UAE note that Verifone terminals lack 5 GHz network coverage there (raw lines 29–57). Mobile solutions do not yet cover every listed geography; their separate status link is navigation until read (raw lines 59–62). The primary language table says what UI languages terminals can show **on latest software**, not what a shopper necessarily sees or what a receipt prints. Preserve table labels exactly, including the literal `Russia` entry (raw lines 64–75). Deprecated legacy models have a separate latest-software UI-language table (raw lines 77–90). Route after catalog update: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-terminal-api.md` (related in-person route; broader source) → `wiki/sources/adyen/source-adyen-docs-point-of-sale-what-we-support-supported-languages.md` → `raw/adyen/docs/point-of-sale/what-we-support/supported-languages/2026-09-15.md`.
