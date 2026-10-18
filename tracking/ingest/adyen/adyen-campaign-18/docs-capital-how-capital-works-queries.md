# How Capital works — retrieval probes

## Q1 — Eligibility and offer boundary

**Query:** If a platform user has processed Adyen payments for 90 days at 1,000 per month, is a Capital grant guaranteed?

**Expected answer:** No. The captured minimum screen also requires a supported location and legal-entity type and excludes businesses in a high-risk industry. It lists at least three consecutive months of processing and volume of at least 1,000 in EUR, GBP, USD or AUD over that period, but explicitly says meeting minimums does not guarantee a financing offer. Adyen's risk assessment and capability process determines available offers. The country/entity table is dated and has regional exceptions. It omits Netherlands and Spain even though the linked Capital overview lists them as supported locations (pinned raw/adyen/docs/capital/2026-09-15.md lines 36–40); do not infer entity-type eligibility or country exclusion from that mismatch. Verify current Adyen guidance; these pages do not establish eligibility or approved terms for a specific user.

**Raw locators:** lines 21-34 (minimum requirements and no-guarantee statement); 36-48 (country/entity matrix); 50-82 (underwriting and offer variants). **Canonical discovery route:** [[adyen-index]] → [[adyen-capital]] → [[source-adyen-docs-capital-how-capital-works]] → [[raw/adyen/docs/capital/how-capital-works/2026-09-15]]. Provider-index adyen-capital route is pending coordinator repair.

## Q2 — Funding, fee and repayment

**Query:** After a user selects a Capital offer, where does the grant go, when could money reach the bank, and how are fee and repayments described?

**Expected answer:** The user must accept Capital Terms of Service for each new grant. The grant is initially disbursed to the user's linked balance account; after that initial disbursement settles, the guide permits instruction in the same API request to transfer to the user's verified bank-account transfer instrument. These are distinct steps, with no bank-receipt proof in this page. The offer has principal plus a fixed fee, a daily repayment rate applied to daily net captured volume, a 30-day minimum threshold and a maximum repayment period. Scheduled repayment is default; the page limits unscheduled early/missed-payment action to users in certain regions without naming those regions. It requires additional platform action and is described for both UI-components and API-only integrations. Additional financing is described as a pilot, with partial renewal reserving outstanding principal and requiring new underwriting and Terms acceptance. No displayed offer, configuration request or example proves the user's debt balance or final repayment.

**Raw locators:** lines 71-110 (offer, acceptance and funding); 112-135 (repayment/renewal); 137-147 (offer elements). **Canonical discovery route:** [[adyen-index]] → [[adyen-capital]] → [[source-adyen-docs-capital-how-capital-works]] → [[raw/adyen/docs/capital/how-capital-works/2026-09-15]]. Provider-index adyen-capital route is pending coordinator repair.
