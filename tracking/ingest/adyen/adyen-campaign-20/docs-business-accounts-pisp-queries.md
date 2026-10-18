# Query checks — Adyen Business Accounts PISP

## Q1 — initiation actor and response
**Question:** Who may use the captured PISP guide to start a payment and what does the creation response prove?
**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-pisp]] → [[raw/adyen/docs/business-accounts/pisp/2026-09-15]].
**Expected answer:** The actor is a third-party PISP acting for a consenting holder, after Adyen open-banking onboarding and with an access token (raw lines 19–33). The documented single-payment POST names amount, creditor and debtor account identities, creditor name/address (lines 35–48). The response supplies a paymentId and current transactionStatus; the example is PDNG and includes payment and SCA-status links (lines 81–119). It establishes an initiated resource in the example, not settlement or creditor receipt.

## Q2 — consent, SCA and payment-status boundary
**Question:** If the authorization lookup says `scaStatus: finalised`, has the creditor received the payment?
**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-pisp]] → [[raw/adyen/docs/business-accounts/pisp/2026-09-15]].
**Expected answer:** No. The payment lookup by paymentId returns `transactionStatus` and is recommended to be polled about every five seconds (raw lines 121–148). A separate authorization lookup uses paymentId plus authorizationId and returns `scaStatus`; `finalised` only means the SCA authorization resource completed successfully (lines 150–179). The status catalog separately defines ACCC as creditor-account settlement completed and other stages, but no actual payment result is shown (lines 83–99). The examples are inconsistent: initiation has amount 0.50 and PDNG, status lookup has -0.50 and RCVD (lines 49–79, 101–148); authorization curl uses Basic with an access token although payment calls use Bearer (lines 53–58, 129–132, 158–162). Check current endpoint details before operational use.
