# Fixed queries — docs-industries-peak-season-in-person-payments

## Q1 — purpose, scope, and what not to infer

**Query:** What is Adyen's “In-person payments” peak-season page for, and what does it establish?

**Answer:** It is a preparation checklist for in-person payment methods, terminal and Mobile hardware, software, offline/cellular outage planning, and live cloud Terminal API regional endpoints. The terminal-software timings and recommendations are explicitly for the 2025 Christmas/end-of-year season; raw lines 76–94 include an internally reversed no-rollout date range. It is not proof that an account has enabled a method or offline mode, a terminal is boarded/on a given version, a route is reachable, or any payment was authorized or settled. See [[source-adyen-docs-industries-peak-season-in-person-payments]] via [[adyen-terminal-management]] → [[adyen-index]]; raw lines 19–23, 67–94, 104–133.

## Q2 — central capability, prerequisites, and warnings

**Query:** What preparation and outage options does the guide describe, and what conditions matter?

**Answer:** Review and test regional methods/currencies/refund fit early; allow lead time to order, assign, board and test terminals/backup devices (raw lines 25–65). Check solution-specific terminal and Mobile SDK versions, with 2025-season version advice and Mobile SDK six-month expiry in this snapshot; do not rely on the inconsistent freeze dates without verification (lines 67–102). Temporary network loss calls for separately enabled offline payments: terminal Offline EMV depends on card/issuer behavior, while Store and forward approves locally without verification and has higher issuer-decline risk; Mobile Store and forward requires prior device attestation and does not support offline PIN completion (lines 104–119). Cellular failover and geographically correct regional endpoints apply to their distinct terminal-network and live cloud Terminal API contexts (lines 121–133). Canonical route: [[adyen-index]] → [[adyen-terminal-management]] → [[source-adyen-docs-industries-peak-season-in-person-payments]] → pinned raw.
