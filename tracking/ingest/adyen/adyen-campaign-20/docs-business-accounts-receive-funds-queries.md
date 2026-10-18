# Query checks — Adyen Business Accounts receive funds

## Q1 — incoming credit and capability
**Question:** What is credited when an external third party sends funds to a Business Account, and what gate must the user satisfy?
**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-receive-funds]] → [[raw/adyen/docs/business-accounts/receive-funds/2026-09-15]].
**Expected answer:** The guide says third-party business payments are credited to the user's Business Account and available in its balance account (raw lines 19–21). `receiveFromThirdParty` must be both allowed and enabled (lines 24–26, 111–113); the sender uses the business account number returned at creation (line 111). Adyen says incoming bank-transfer webhooks notify the server (line 115). This is an external-sender credit, not an internal balance-account transfer or proof of actual receipt.

## Q2 — direct-debit boundary and dated-table conflict
**Question:** Does “receive funds” also mean incoming SEPA direct debits credit the account, and can the tables be used as current bank instructions or availability proof?
**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-receive-funds]] → [[raw/adyen/docs/business-accounts/receive-funds/2026-09-15]].
**Expected answer:** No. Third-party direct-debit collection **debits** the user's business account (raw lines 21–22). The captured guide limits its external direct-debit support statement to SEPA and calls for informing the user of its stated eight-week and thirteen-month dispute periods plus asking an Adyen contact to enable SEPA direct debits (lines 117–128). Treat those as historical documentation, not current legal advice. The currency/location priority matrices are dated and uneven (lines 48–79); the NL BIC row is labeled “Adyen US BIC” and UK sort code repeats the US routing-number sample (lines 89–107). Sample identifiers and availability marks cannot establish live instructions, eligibility, speed or fees.
