---
title: "Adyen Surcharge Compliance Guide"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/surcharge-compliance"
raw_files:
  - "adyen/docs/development-resources/surcharge-compliance/2026-09-15.md"
tags: [adyen, surcharging, compliance, cards, ecommerce, in-person]
---

## Overview

This Adyen development-resources snapshot gives general and regional surcharge-compliance guidance for merchants and platforms. It covers scheme notification, reporting, customer disclosure, cancellation choice, receipts, potential fines, and country or region examples across ecommerce and in-person payments. The page expressly says it is not legal advice and that the Adyen surcharge feature does not enforce card-network or local-law compliance. See [[adyen]] and [[adyen-surcharging]].

## Key takeaways

- Responsibility for applicable surcharge rules remains with the merchant or platform, including rules applying to platform users. Adyen directs readers to current network rules and legal advisers; local regulations may override network requirements. This 2026-09-15 snapshot does not establish today's legal permission, caps, notification status, or account enablement.
- Scheme notification is conditional: the captured page says Discover requires notice to Adyen at least 30 days before first surcharging, and Visa requires the same for Canada and the United States. It says Mastercard was updating its rules later in 2026 and, at capture time, its surcharge disclosure form was not required for credit-card intent registration. Treat that Mastercard status as dated, not current.
- The reporting path differs by integration. For ecommerce, the page limits the surcharge feature to API-only integration: `/payments` carries the surcharge in `surcharge`, while `amount.value` is original transaction amount plus surcharge. For in-person payments, the terminal or Mobile SDK calculates the surcharge from configuration, and the Terminal API payment request contains the original transaction amount. Do not transfer the ecommerce request arithmetic to Terminal API.
- Before applying a surcharge, the page calls for customer disclosure of its amount or rate, appropriate signage, and a choice to cancel or use an alternative payment method. Receipts need a separate surcharge line item. Adyen provides no signage template through the surcharge feature. The page says network non-compliance fines are passed through to the merchant or platform; platforms are liable for fines incurred by their users.
- Regional restrictions and caps are network-, card-type-, location-, and date-dependent. The snapshot says Canada and the United States prohibit debit/prepaid surcharging and that Adyen does not automatically reject such attempts or over-cap surcharges. It describes EEA-issued consumer cards in the EEA and SEPA transactions as non-surchargeable, with country-specific treatment for commercial cards. The Australia section says listed card-network debit, credit, and prepaid surcharging would cease from 1 October 2026; this future-at-capture date now requires current source verification before operational use.

## Detail locators

- Scope, legal-advice caveat, merchant/platform ownership, and local-rule priority: lines 15–23.
- Scheme notification and dated Mastercard status: `## Notification requirements`, lines 25–62; Discover lines 29–31 and Visa Canada/US lines 37–62.
- Ecommerce API-only versus in-person terminal/Mobile SDK surcharge reporting: `## Reporting the surcharge amount`, lines 64–70.
- Customer disclosure, signage, cancellation choice, and receipt line: lines 72–110. Fines, examples, and platform-user liability: lines 112–127.
- Region-specific snapshot sections: Australia lines 129–133; Canada lines 135–164; Europe lines 166–177; New Zealand lines 179–199; United States lines 201–231. Check exact card types, caps, and jurisdictional qualifications at these locators before use.

## Related

- [[adyen]] — provider context.
- [[adyen-surcharging]] — online surcharge feature and reciprocal compliance-guide route.
- [[source-adyen-docs-online-payments-surcharge]] — API-only online feature flow and payment lifecycle.

## Raw Sources

- [[raw/adyen/docs/development-resources/surcharge-compliance/2026-09-15|Adyen surcharge compliance guide (2026-09-15)]]
