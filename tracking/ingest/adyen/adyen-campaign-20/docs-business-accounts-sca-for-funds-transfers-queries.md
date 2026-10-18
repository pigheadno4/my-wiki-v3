# Query checks — Adyen Business Accounts SCA for funds transfers

## Q1 — purpose and prerequisites
**Question:** How does the captured Business Accounts guide authenticate an EEA user's funds transfer, and what must exist first?
**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-sca-for-funds-transfers]] → [[raw/adyen/docs/business-accounts/sca-for-funds-transfers/2026-09-15]].
**Expected answer:** It describes SDK SCA with availability check, challenge, client authentication and finalizing request, either on transfer initiation or reviewer approval. The guide requires installed SDK, registered device, and API credential TransferService Webservice Initiate role. Raw lines 19–31, 33–37, 129–136, 575–626, 1321–1349, 1426–1445 and 1906–1917. The reviewer can cover multiple pending transfers (line 136).

## Q2 — failure, boundary and conflict
**Question:** Does an authorised SCA response prove funds reached the payee, and what captured-guide ambiguities affect implementation?
**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-sca-for-funds-transfers]] → [[raw/adyen/docs/business-accounts/sca-for-funds-transfers/2026-09-15]].
**Expected answer:** No. The page describes SCA and transfer-request/approval success, not settlement or bank receipt. Authentication must complete within 10 minutes (raw line 1353), the web availability check can throw `SCA_UNAVAILABLE` (line 123), and challenge examples use 401 before successful authentication (lines 575–626, 1321–1349). The prose says authorised response header, but the illustrative final response body says `received`/`pending` (lines 1872–1903). Initial bank-account counterparty and `bank` category conflict with finalization table's balance-account counterparty and several `internal` code samples (lines 151–152, 1447–1452, 1740–1741, 1885–1895). Approval route separately asks for an authorised transfer-updated webhook (lines 2117–2119). These captured 2022-modified examples are not current availability proof.
