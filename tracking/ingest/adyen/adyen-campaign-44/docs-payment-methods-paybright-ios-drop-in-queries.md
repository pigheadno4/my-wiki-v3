# C44 worker query check: PayBright iOS Drop-in

## Q1 — purpose, scope, non-inference

**Query:** Can a new merchant integrate PayBright from this guide?

**Answer:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paybright-ios-drop-in]] routes to the 2026-09-15 iOS Drop-in Sessions/Advanced add-on for existing integrations. The page explicitly says Adyen will not accept new PayBright integrations; its later live-request sentence is legacy tension, not permission for new onboarding. Pinned full raw: `raw/adyen/docs/payment-methods/paybright/ios-drop-in/2026-09-15.md`; verified locators: raw lines 15–40 and 1429–1435.

## Q2 — capability, prerequisites, warnings

**Query:** What data and capture/refund behavior does the guide describe?

**Answer:** The API tables require shopper first/last name, birth date, email, phone, country, billing address and unique shopper reference; optional line items are recommended. No PayBright-specific Drop-in configuration is required. By default capture is automatic; partial capture requires delayed/manual setup, normally cancels the unclaimed remainder, and multiple partial capture needs Support enablement. Cancel applies before capture, refund after. The [[source-adyen-docs-payment-methods-paybright|PayBright overview]] matrix lists CA/CAD (overview raw lines 31–33), while this guide's CA /payments Java and PHP examples use USD (raw 883–888 and 970–976) and most other samples leave currency blank. The USD examples do not establish support; use the overview and account-specific provider configuration for the currency decision. Partial-refund prose mixes Checkout /refunds with legacy /refund fields. Verified locators: raw 45–60, 789–804, 886–887, 975–976, 1312–1427.
