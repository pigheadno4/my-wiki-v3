# Fixed retrieval checks — Capital static financing offers

Q1. What does this source establish about static offers, and what must not be inferred?
- Expected: A 2026-09-15 Capital API guide for account-holder static-offer listing/detail and creation notifications. Variable 90/180/360-day term options are marked limited-availability pilot. Up to nine offers may be shown based on processing history, not guaranteed. A returned/listed/announced offer is not acceptance, grant approval, disbursement, repayment, bank receipt or current user/country eligibility. Terms of Service and grant request are separate next steps.
- Raw locators: `raw/adyen/docs/capital/get-grant-offers/static-offers/2026-09-15.md:15-24`, `:39-45`, `:408-423`, `:470-482`.
- Canonical URL: `https://docs.adyen.com/capital/get-grant-offers/static-offers`.
- Forward route: `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-capital]]` → `wiki/sources/adyen/source-adyen-docs-capital-get-grant-offers-static-offers.md` → `[[raw/adyen/docs/capital/get-grant-offers/static-offers/2026-09-15]]`.

Q2. Which access gates, expiry rules, amount/term fields and example inconsistencies limit implementation?
- Expected: Requires Capital-supporting Platforms integration, Balance Platform API key with Configuration and Grant Initiation roles, user's getGrantOffers capability and Capital compliance setup. Offers last seven days; renewal occurs only if account holder still qualifies and amount can change. List GET by accountHolderId also returns static offers made through dynamic flow; specific GET by offer ID. Per-offer minor-unit amount/fee, start/end, loan contractType, basis-points daily net-volume deduction, 30-day minimum threshold and estimated versus maximum term are distinct. Example estimated terms 90/180/360 contrast with maximum 120/270/450. Specific GET requests ID 000...001 but response shows 000...003, so don't infer matched lookup. Webhook announces offer creation and says accept before expiration; none proves a funded grant.
- Raw locators: `raw/adyen/docs/capital/get-grant-offers/static-offers/2026-09-15.md:26-73`, `:79-109`, `:171-186`, `:260-276`, `:354-405`, `:408-468`.
- Canonical URL: `https://docs.adyen.com/capital/get-grant-offers/static-offers`.
- Forward route: `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-capital]]` → `wiki/sources/adyen/source-adyen-docs-capital-get-grant-offers-static-offers.md` → `[[raw/adyen/docs/capital/get-grant-offers/static-offers/2026-09-15]]`.
