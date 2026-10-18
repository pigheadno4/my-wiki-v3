# Fixed retrieval queries: docs-capital-download-offers

## Q1 — CSV purpose, scope and offer boundary

**Question.** What does the captured Capital offer-download page provide in its CSV, how fresh and personalized is that data described to be, and what cannot be inferred from downloading or viewing it?

**Forward route.** `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-capital]]` → `[[source-adyen-docs-capital-download-offers]]` → `[[raw/adyen/docs/capital/download-offers/2026-09-15]]`.

**Expected answer.** It provides a Customer Area CSV for eligible account holders across the selected balance platform. Each offer is personalized from processing history; the export contains minimum and maximum eligible grant amounts, not an exact committed grant amount. Data is described as generated daily at midnight CET; offers have account-holder-specific expiry, may appear despite an active grant, and absent holders have no active offer according to the guide. The CSV identifies balance platform and account holder, min/max in major units, currency and validity timestamps. The sample rows are illustrative. Exporting is not offer selection, ToS acceptance, grant request, funding, debt or repayment proof.

**Raw locators.** Lines 19–25 (purpose, range and cadence); 39–44 (download); 46–70 (sample and schema); 72–74 (separate API route).

## Q2 — access, validity and live-offer qualification

**Question.** Which integration, Customer Area role, jurisdiction and validity conditions does the captured guide place around this export, and does an expired or absent row prove permanent ineligibility?

**Forward route.** `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-capital]]` → `[[source-adyen-docs-capital-download-offers]]` → `[[raw/adyen/docs/capital/download-offers/2026-09-15]]`.

**Expected answer.** It names an Adyen for Platforms integration, Customer Area Capital base role, user operation in a linked supported country/region, and compliance with linked Capital UI/marketing guidelines. The offer remains valid for seven days; after expiry a new offer is generated only if the account holder still meets qualification criteria, and its amount may change. An absent row means no active offer in that list, not permanent ineligibility. The linked region and compliance pages must be checked for their dated specifics; this export page does not establish current eligibility, approved marketing, live user authorization or a funded grant.

**Raw locators.** Lines 27–37 (requirements and validity); 21–23 (personalization and absence/subsequent-offer nuance); 39–44 (selected-platform Customer Area path).
