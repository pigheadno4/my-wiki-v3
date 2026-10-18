# Query checks — Adyen Business Accounts industry codes list

## Q1 — purpose and approval boundary
**Question:** What does the captured industry-code child page require when selecting an IC for a user's Business Account, and when should a platform contact Adyen?
**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-verification-requirements-reference-additional-products-industry-codes]] → [[raw/adyen/docs/business-accounts/verification-requirements/reference-additional-products/industry-codes/2026-09-15]].
**Expected answer:** Choose the IC that best represents the user's business activity; Adyen maps ICs to MCCs under its internal rules, and some MCCs map to multiple ICs (raw lines 17–19). The page directs contacting Adyen or Support when a code needs pre-onboarding approval or when offering Business Accounts in new industries outside prior approval (lines 21–24). This is selection/approval guidance, not proof that a particular code or user was approved. The parent additional-products source provides separate business-line submission context.

## Q2 — missing list and orphaned footnotes
**Question:** Can this captured page identify the accepted IC values or connect its ATV/CBD/Amex footnotes to specific codes?
**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-verification-requirements-reference-additional-products-industry-codes]] → [[raw/adyen/docs/business-accounts/verification-requirements/reference-additional-products/industry-codes/2026-09-15]].
**Expected answer:** No. It says accepted values follow (raw line 26), but the raw moves directly to a separator and three unlabeled footnotes (lines 28–32), then a brand-specific list link (lines 34–36). The footnotes mention EUR 2,000 ATV, CBD/kava/baby-food, and American Express, but the code rows they would qualify are absent. No exact accepted code or footnote applicability can be inferred.
