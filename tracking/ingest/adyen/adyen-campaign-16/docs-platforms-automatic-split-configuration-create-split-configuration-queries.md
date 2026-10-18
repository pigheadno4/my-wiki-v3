# Fixed queries — docs-platforms-automatic-split-configuration-create-split-configuration

## Q1 — purpose, scope, and non-inference

**Query:** What does this split-configuration guide create, and does a profile prove payment splitting or ownership of funds?

**Answer:** It describes creating a conditional split-configuration profile for transactions through a platform user's store, then linking the profile and selected user balance account to that store. When neither the profile nor Checkout/Terminal payment request includes split instructions, the guide says funds/fees book to the platform liable balance account (raw lines 15–24, 39–49). After successful store association, the highest-priority matching rule is evaluated, with full hierarchy in a separate guide (lines 2375–2389). A profile, test response or rule does not prove a live payment, booked split, payout, legal seller or MOR. Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-automatic-split-configuration-create-split-configuration]] → pinned raw.

## Q2 — central capability, prerequisites, and warnings

**Query:** Which roles, conditions and booking limits matter when creating and linking a profile?

**Answer:** Requires a platform-model integration and Support enablement; Management API creation needs `Management API—SplitConfiguration read and write`, while Customer Area creation needs the Support-enabled admin role (raw lines 26–37). Create the first rule with conditions such as shopper interaction, method, funding source and currency; card-region condition is pilot/API-only. Store association names both profile ID and user balance-account ID via Management API create/update; introduction allows an Onboarding-on-invite Customer Area exception that later text does not repeat (lines 21–24, 41–49, 65–79, 113–145, 2375–2387). Fee levels are mutually constrained; multi-partial-capture stores must not use refund `deductAccordingToSplitRatio`; online conversion remainder, pilot in-person DCC, and region-limited surcharge have distinct scopes (lines 161–180, 570–581, 997–1003, 1380–1397, 1457–1468). Amounts are minor units and percentage inputs basis points in the composite example; example snippets are test/versioned and contain discrepancies, so consult the current API schema and actual response before use (lines 1855–1920, 2326–2373). Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-automatic-split-configuration-create-split-configuration]] → pinned raw.
