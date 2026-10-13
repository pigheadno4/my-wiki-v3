---
title: "Adyen Docs: Payout to a bank account"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/online-payouts/payouts-to-a-bank-account"
raw_files:
  - "adyen/docs/online-payments/online-payouts/payouts-to-a-bank-account/2026-09-15.md"
tags: [adyen, payouts, bank-accounts, payout-api, transfers-api]
---

## Overview

This [[adyen]] page is a bank-account payout reference for the **legacy Payout API**. Although it shows `/storeDetailAndSubmitThirdParty` request fields and test examples, the 2026-09-15 snapshot says Adyen no longer accepts new Payout API integrations. It directs new builds to the Transfers API bank-payout guide and existing Payout API integrators to their Adyen contact for migration. This is outbound disbursement guidance, not an online shopper-payment acceptance flow or evidence of payout execution. See [[adyen-payouts]].

## Key takeaways

- The page says Transfers API can serve multiple payout use cases, offer features such as instant payouts, and provide webhooks with more detail and defined transfer states. These are Adyen's migration reasons in the snapshot, not proof that a specific merchant account or destination is enabled.
- The legacy bank-payout route shown here submits a `/storeDetailAndSubmitThirdParty` request. The required request fields depend on the **country or region of the recipient's bank account**. The page sends readers to its parent [[source-adyen-docs-online-payments-online-payouts|Online payouts]] page for supported recipient regions; those are snapshot listings, not current eligibility proof.
- For a **SEPA** recipient bank account, the page lists bank country code, owner name, and IBAN, together with nationality and entity type. Its shopper-name and birth-date qualifiers differ by recipient actor: first name, gender, and date of birth are listed for **natural persons only**, while last name is listed for **companies and natural persons**. Consult raw **Payouts to SEPA locations** for the exact field spellings and test `v65` request example.
- For a **United States** recipient bank account, the page instead lists bank country code and owner name, account number, ABA-number `bankLocationId`, bank name/city, and billing-address fields. Consult raw **Payouts to the United States** for the full list and test `v65` request example. Example values, including `merchantAccount` and `recurring.contract`, illustrate the legacy request; they do not show a successful payout or define Transfers API requirements.

## Detail locators

- Raw opening migration notice — no new Payout API integrations, Transfers API capabilities, new-build route, and Adyen-contact migration route.
- Raw **Payouts to SEPA locations** — legacy endpoint field list with natural-person/company distinctions and a test request.
- Raw **Payouts to the United States** — legacy US bank and billing-address fields and a test request.

## Related

- [[source-adyen-docs-online-payments-online-payouts-payouts-to-bank-accounts-and-wallets]] — separate staged-payout lifecycle, approval, and review context for legacy bank and wallet payouts.
- [[source-adyen-docs-online-payments-online-payouts]] — parent payout overview and recipient-region matrix.

## Raw Sources

- [[raw/adyen/docs/online-payments/online-payouts/payouts-to-a-bank-account/2026-09-15|Payout to a bank account (2026-09-15 snapshot)]]
