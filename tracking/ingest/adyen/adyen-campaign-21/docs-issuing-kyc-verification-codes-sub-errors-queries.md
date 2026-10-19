# Q1 — main purpose and prerequisites

**Query:** For an Adyen Issuing integration, what is the suberror catalog for, and what preparation does this page require?

**Answer:** The catalog maps granular KYC verification causes to messages and, when applicable, remediating-action codes (raw line 16). The page says there are no additional requirements, limitations or preparations **if an Adyen for Platforms or Adyen Issuing integration already exists** (raw lines 18–20). That statement does not establish an entity's onboarding or current capability. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-kyc-verification-codes-sub-errors]] → [[raw/adyen/docs/issuing/kyc-verification-codes/sub-errors/2026-09-15]].

# Q2 — material boundary, failure and conflict

**Query:** Can every suberror be treated as an ordinary retry, and where does the general error code sit in the example?

**Answer:** No. Organization suberror `1_5052` says the payout entity is not 100% affiliated and setup cannot be continued, although its row links action `1_100` (raw line 188); individual `1_3082` states a minimum-age failure (raw line 124). The opening says general codes and messages are in `subErrors` (raw line 16), while the example places general `1_30` under `verificationErrors` and granular `1_3001`/`1_3000` under `subErrors` (raw lines 340–382). This dated, illustrative page does not settle a current runtime schema or guarantee remediation. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-kyc-verification-codes-sub-errors]] → [[raw/adyen/docs/issuing/kyc-verification-codes/sub-errors/2026-09-15]].
