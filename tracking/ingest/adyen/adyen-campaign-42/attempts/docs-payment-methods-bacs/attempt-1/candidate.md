---
title: "Adyen BACS Direct Debit overview"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs"
raw_files:
  - "adyen/docs/payment-methods/bacs/2026-09-15.md"
tags: [adyen, bacs, direct-debit, gb, gbp, mandate, chargebacks]
---

## Overview

This 2026-09-15 Adyen overview describes **BACS Direct Debit** in the United Kingdom, including shopper bank details and Direct Debit Instruction (DDI/mandate), the clearing cycle, advance notice, chargeback rights, a feature table and platform routes. It is a direct-debit collection, not a one-time bank transfer. The captured page does not prove current merchant eligibility, valid mandate, a cleared payment or settled funds. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Collection and mandate:** the page says BACS supports one-off and recurring payments but advises against one-off use or physical-goods sales because of chargeback risk. The shopper enters name, bank account number, sort code and email, confirms account ownership and agreement, then can download the DDI after the payment is received; Adyen submits the DDI and payment for BACS processing. The page says clearing and settlement can take **four to six days**. Shopper confirmation and submission are distinct from cleared funds. The source says a statement may show Adyen with Service User Number **182827** rather than the merchant's company name. (raw lines 23–29)
- **Capability snapshot:** the table labels BACS **Direct Debit**, **Direct** flow, **GB/GBP**. It marks recurring, refunds, partial/multiple partial refunds, separate captures and chargebacks with checkmarks, but marks partial and multiple partial captures with x. These historical feature marks are not account-specific eligibility or detailed refund/capture instructions. (raw lines 31–33)
- **Advance notice:** Adyen **strongly recommends** notifying shoppers before processing. It attributes a **10-day-before-charge** notice consequence to scheme rules: shoppers may file a chargeback if they do not receive notification. Separately, its sample email is recommended **8 working days before capture**, with the charge expected to appear **2–3 working days later**. Preserve the distinction between source-stated scheme risk and Adyen's template timing; the template is not a blanket compliance guarantee. (raw lines 35–58)
- **Chargeback rights and event:** under the Direct Debit Guarantee, the source lists immediate money back for payment errors and the shopper's right to cancel the DDI at any time. Unpaid debits are booked as chargebacks, including changed/cancelled DDI, disputed due date/amount/frequency, nonpayment or insufficient funds. The page says BACS chargebacks **cannot be defended** and always refund the shopper. Its chargeback webhook fields include `pspReference`, `eventCode: CHARGEBACK`, reason and `success: true`; `success` here describes the chargeback event, not a successful payment. The example's `directdebit_GB.serviceUserNumber` is **298288**, differing from the prose's 182827, and its currency/payment method are blank. Do not use the sample as the merchant's configuration. (raw lines 60–118)
- **Implementation routes:** the overview links Web, iOS, Android, React Native, Flutter, API-only and Pay by Link child routes. Their guides define platform-specific mandate, request and outcome handling. (raw lines 125–167)

## Detail locators

- UK method, one-off/recurring caution, DDI and four-to-six-day clearing: pinned raw lines 15–29.
- GB/GBP capability table: pinned raw lines 31–33.
- Ten-day scheme-risk statement and eight-working-day template: pinned raw lines 35–58.
- Guarantee, undefendable chargebacks, event fields and conflicting Service User Numbers: pinned raw lines 60–118.
- Web/native/API-only/Pay by Link routes: pinned raw lines 125–167.

## Related

- [[adyen-online-payments]] — main provider payment/settlement context
- [[adyen-tokenization]] — provider recurring-payment context; BACS details require child evidence

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/2026-09-15|BACS Direct Debit overview, 2026-09-15]]
