---
title: "Pre-Authorized Debit Canada | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pad"
raw_files:
  - "adyen/docs/payment-methods/pad/2026-09-15.md"
tags: [adyen, pad, canada, direct-debit, mandate, chargebacks]
---

## Overview

This Adyen overview describes Canadian Pre-Authorized Debit (PAD): a shopper permits a business to withdraw funds from a bank account, with transactions processed through Payments Canada's ACSS network. It says PAD can be recurring or one-off, but recommends against one-off use because of chargeback risk. Acceptance requires the merchant to have a Canadian account at a Canadian financial institution. The snapshot's capability table labels the method Direct Debit, Direct flow, CA/CAD; it marks recurring, refunds including partial and multiple partial refunds, and chargebacks available, while separate, partial and multiple partial captures are unavailable (raw lines 15–31).

## Key takeaways

- Before **any** PAD, one-off or recurring, the merchant must obtain and retain a shopper PAD agreement; this is explicitly the merchant's responsibility. The source's minimum contents are business contact and acceptance date, personal/business type, a shopper-accepted or signed authorization to debit the specified bank account, bank details, payment schedule or triggers, conditional waivers for immediate debit or omitted pre-notification, prescribed unauthorized-debit refund-right text, cancellation information, and a statement that Adyen processes the PAD. The page points to Payments Canada Rule H1 for details; this captured summary is not a current legal determination (raw lines 33–51).
- PAD has no real-time authorization. Debits may be reversed, including for insufficient funds. The source gives shopper chargeback windows up to **90 days** from the initial debit for personal accounts and **10 days** for business accounts (raw lines 53–57).
- Outdated or incorrect banking details can also cause reversals. If Adyen receives a bank/credit-union Notification of Change and the merchant has subscribed to `DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION`, Adyen says it sends an `eft.notificationOfChange` webhook with details. The page advises listening and updating customer bank details to avoid future chargebacks; a subscription is a condition of that webhook route (raw line 58).
- PAD chargebacks cannot be defended. A retry may be allowed depending on the reason code; the overview links the API-only guide for those codes (raw line 60).
- This page routes to Web pre-built UI and API-only merchant-built UI for website, iOS or Android. Those are integration navigation, not proof that any debit was submitted, settled, refunded or currently enabled (raw lines 62–74).

## Detail locators

- PAD identity, ACSS processing, merchant Canadian-account prerequisite and capability table: raw lines 23–31.
- Merchant-held PAD agreement and required contents/conditional waivers: raw lines 33–51.
- Reversal risk, account-type chargeback windows and change-notification route: raw lines 53–58.
- Nondefensible chargebacks and reason-code-dependent retry: raw line 60.
- Web and API-only integration routes: raw lines 62–74.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pad/2026-09-15|Pre-Authorized Debit Canada overview, fetched 2026-09-15]]
