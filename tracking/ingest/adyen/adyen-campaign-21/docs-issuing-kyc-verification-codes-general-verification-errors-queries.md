# Retrieval checks — general verification errors

## Q1: What does this error catalog do, and is extra setup required to use it?

The 2021-modified page, captured 2026-09-15, says general codes broadly identify a verification problem and appear with messages in `verificationErrors`, which usually also includes suberrors (raw line 16). It says Adyen for Platforms or Issuing integrations need no additional preparation for this reference (raw line 20). Sections map general, individual, organization, legal-arrangement, bank, signatory, business-line, missing-data, missing-contract and review codes (raw lines 22–130, 133–304). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-kyc-verification-codes-general-verification-errors]] → [[raw/adyen/docs/issuing/kyc-verification-codes/general-verification-errors/2026-09-15]].

## Q2: What do capability, missing-data and contract errors mean, and what should not be inferred?

`1_12` states legal entity declined, and `1_14`–`1_16` identify capabilities disallowed for individual/entity type or country (raw lines 39–45); no workaround or current eligibility follows from these labels. Missing-data rows map a returned missing item to a remediating-action code, not a universal field requirement for all integrations (raw lines 133–290). `2_901`, `2_902`, `2_904` concern PCI forms, Terms of Service and incomplete integration; `3_10` requires data review (raw lines 292–304). The sample `problems` array is illustrative (raw lines 306–335). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-kyc-verification-codes-general-verification-errors]] → [[raw/adyen/docs/issuing/kyc-verification-codes/general-verification-errors/2026-09-15]].
