# Fixed retrieval checks — Adyen 3DS Authentication report

## Q1 — Purpose, scope, and non-inference

**Question:** Which transactions does the 3DS Authentication report cover, how does it differ from the conversion report, and what does a successful authentication entry not prove?

**Expected answer:** It covers transactions for which **Adyen** attempted 3DS authentication or applied a 3DS exemption; it excludes cases where 3DS did not apply or a different provider attempted authentication. The conversion report starts from all card transactions offered and may contain drop-offs, so its population differs. A report row and `Authentication Success` describe authentication context, not proof of payment authorization, capture, settlement, or payout; authorization has a separate `Acquirer Response` field.

**Raw locators:** Introduction lines 17–21; `How to use this report` lines 33–37; `Entries` line 43; `Columns` lines 56 and 65–67.

**Canonical wiki route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-3d-secure-3ds-authentication-report]] (provider-index link to reporting awaits coordinator placement).

## Q2 — Central capability, prerequisites, and warnings

**Question:** What are the report's grain, access/time qualifications, migration warning, and sensitive-field caveat?

**Expected answer:** Each CSV line after the header represents a transaction. The page says the report is available for company and merchant accounts and obtainable manually or automatically, with Customer Area date selection and a CET report time zone. The `Creation Date` field is CET or CEST depending on transaction date. `Authentication Only` requires additional configuration and `authenticationOnly` in the request. The report replaces an older 3D Secure Authentication report, but changed filtering prevents full numeric reconciliation and may require ingestion changes. The CSV includes shopper email and IP, cardholder name/BIN, references, metadata and 3DS IDs, so exports contain potentially sensitive data; the page does not define user-role or retention rules.

**Raw locators:** Introduction lines 21–31; `Entries` line 43; `Columns` lines 66, 71–72, 77, 82, 88–90, 94, 104–109; `Authentication flows and success` lines 111–127.

**Canonical wiki route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-3d-secure-3ds-authentication-report]] → [[raw/adyen/docs/reporting/3d-secure/3ds-authentication-report/2026-09-15|pinned raw snapshot]].
