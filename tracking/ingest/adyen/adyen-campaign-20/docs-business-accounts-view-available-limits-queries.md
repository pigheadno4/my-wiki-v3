# Query checks — View available limits

## Q1 — Purpose and prerequisites

**Query:** What can a Business Accounts platform read from the available-limits endpoint, and what access and setup does this page require?

**Answer:** This 2025-modified, 2026-09-15-captured page describes GET /balanceAccounts/{id}/limits for calculated amount and count limits regulating outgoing transfers from a user's balance account. It requires an Adyen for Platforms Business Accounts integration and Configuration API access with Bank Manage TransactionRules role. Its setup row calls for a transaction rule using totalAmount or matchingTransactions. The result includes calculatedAt, limit/spent/remaining, source and interval. The introduction also names transfer limits, but the page's prerequisites primarily describe transaction rules; the readout is no proof of a specific transfer's approval or settlement.

**Evidence:** Raw lines 15–30 identify purpose and figures; 40–49 specify access, supported restrictions and setup; 60–100 give the route, selector and response. Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-view-available-limits]] → [[raw/adyen/docs/business-accounts/view-available-limits/2026-09-15]].

## Q2 — Resource level, limits and current-availability boundary

**Query:** If GET /balanceAccounts/{id}/limits returns no limit or a remaining amount, does that show every applicable control or guarantee a transfer can proceed?

**Answer:** No. The page limits this readout to totalAmount or matchingTransactions with balance-account-level aggregation, excludes matchingValues combined with matchingTransactions, omits limits aggregated above balance-account level, and says blockList has no limits to show. A transactionRuleId may select one rule; if omitted, the page says it returns an applicable limit using a hierarchy but links to Issuing rather than a Business Accounts hierarchy. Its amount/count and remaining figures are calculated at calculatedAt, not a future authorization or settlement guarantee. The guide uses authorization/capture wording in an outgoing-transfer context and describes CET fixed resets alongside a default UTC timezone field; these need the explicit response interval and additional authority before operational inference.

**Evidence:** Raw lines 40–58 cover exclusions and calculation; lines 64–100 show resource/selector/response fields; lines 102–123 specify interval and timezone. Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-view-available-limits]] → [[raw/adyen/docs/business-accounts/view-available-limits/2026-09-15]].
