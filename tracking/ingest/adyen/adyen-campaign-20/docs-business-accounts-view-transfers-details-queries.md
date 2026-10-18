# Query checks — Adyen Business Accounts view transfer details

## Q1 — retrieval purpose and prerequisites
**Question:** How can a platform inspect third-party Business Accounts transfers and what access is required?
**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-view-transfers-details]] → [[raw/adyen/docs/business-accounts/view-transfers-details/2026-09-15]].
**Expected answer:** The captured guide routes list and single-transfer detail views through Customer Area or Transfers API. Platform integration is required; API retrieval uses TransferService Webservice Retrieve role, Customer Area transfer viewing uses Balance platform base role. Customer Area filters one balance platform at a time. `GET /transfers` uses createdSince/createdUntil and an identifier per page text; `GET /transfers/{id}` selects a transfer by ID. Raw lines 23–45, 47–72, 253–258, 465–486, 632–640.

## Q2 — status, conflict and confirmation boundary
**Question:** Does a booked transfer or downloaded confirmation letter prove that the beneficiary bank received the funds, and are the sample list parameters reliable?
**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-view-transfers-details]] → [[raw/adyen/docs/business-accounts/view-transfers-details/2026-09-15]].
**Expected answer:** No. The guide separates initiated, Adyen-authorized and booked stages (raw lines 25–31). The PDF confirms Adyen sent the transfer instruction (raw line 756); it does not attest to beneficiary receipt. Download needs its own role, and unmasked PII needs an additional role (raw lines 770–778). The listed date window is less than six months and an identifier is required (raw lines 66–72), yet the narrative example spans May 2025–May 2026 and the curl example omits identifiers (raw lines 74–84). A list example has `reason: counterpartyAccountNotFound` alongside `status: booked` (raw lines 304–312), so do not equate booked with beneficiary credit.
