# Q1 — purpose and prerequisites

**Query:** What does the Marketplace-path suberror catalog provide, and which integrations does its requirements sentence actually name?

**Answer:** It maps granular causes of KYC verification errors to messages and, where applicable, remediating-action codes (raw line 16). Although the URL says Marketplace, its requirement statement names an **existing Adyen for Platforms or Adyen Issuing integration** and says there are no additional preparations for those integrations (raw lines 18–20). That is not proof of a particular entity's verification or a Classic Account API rule. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-kyc-verification-codes-sub-errors]] → [[raw/adyen/docs/marketplaces/kyc-verification-codes/sub-errors/2026-09-15]].

# Q2 — material failure and example conflict

**Query:** Can every listed suberror be fixed by retrying a linked action, and where does the example place general versus specific codes?

**Answer:** No. Organization `1_5052` says the payout entity is not 100% affiliated and setup cannot continue despite its linked action `1_100` (raw line 194); individual `1_3082` states minimum-age failure (raw line 130). The opening says general codes and messages are in `subErrors` (raw line 16), but the example places general `1_30` in `verificationErrors` and granular `1_3001`/`1_3000` inside `subErrors` (raw lines 366–408). Confirm any runtime shape and next action against the actual response/current schema. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-kyc-verification-codes-sub-errors]] → [[raw/adyen/docs/marketplaces/kyc-verification-codes/sub-errors/2026-09-15]].
