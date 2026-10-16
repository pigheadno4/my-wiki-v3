---
title: "Adyen Disputed transactions report"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/disputed-transactions"
raw_files:
  - "adyen/docs/reporting/disputed-transactions/2026-09-15.md"
tags: [adyen, reporting, disputes, chargebacks]
---

## Overview

Adyen's Dispute transaction details report lists dispute details that can help a merchant manage disputes. Its filename date is the date the included disputes were recorded, and the report follows the account time-zone setting. This is a 2026-09-15 captured description of report data, not proof of a dispute's current outcome. See [[adyen]] and [[adyen-reporting]].

## Key takeaways

- Each line after the header is a separate **entry**. The original payment's **Psp Reference** and the separate **Dispute PSP Reference** identify different objects. **Record Type** denotes a dispute accounting event, with examples from request for information and chargeback to reversal and pre-arbitration outcomes; an entry should not be treated as one complete dispute or a final financial result.
- **Record Date** is when a dispute event was entered into Adyen's accounting system. **Payment Date** is the original authorisation date; **Dispute Date** is when the dispute was first entered; **Dispute End Date** is when the defense period ended. Each date has a separately listed account-time-zone field. The report filename date refers to recorded disputes, not the original payment date.
- **Dispute Currency/Amount** and **Payment Currency/Amount** have different meanings: a dispute may be in a cardholder currency or lower than the original payment, while Payment Amount is the original authorisation amount. Do not equate the amounts or infer a conversion.
- Standard fields include scheme-specific RFI, chargeback and fraud reason codes; the chargeback code can be blank where no formal coding exists, in which case the free-form **Dispute Reason** is the source field to consult. The optional **Status** is the most recent chargeback status. **Auto Defense Dispute Auto Defended** says whether Adyen auto-defended a chargeback, not whether a defense succeeded.
- Generated reports can have extra columns beyond the sample. Customer Area column configuration can affect automated consumers and requires one of the listed merchant roles.

## Detail locators

- Account time zone, report purpose and recorded-dispute filename date: pinned raw lines 19–29.
- Entry grain, payment/dispute references, record types, reason codes, amounts and date meanings: pinned raw lines 31–79.
- Other standard fields, including shopper, authentication and auto-defense indicators: pinned raw lines 80–100.
- Optional fields, including liability shift, RDR, second chargeback and latest chargeback status: pinned raw lines 102–118.
- Column configuration and required Customer Area roles: pinned raw lines 120–139.

## Related

- [[adyen-reporting]] — Adyen reporting concept route.
- [[payment-reconciliation-reporting]] — cross-provider context; its provider-specific examples do not define this dispute report.

## Raw Sources

- [[raw/adyen/docs/reporting/disputed-transactions/2026-09-15|Adyen Disputed transactions, captured 2026-09-15]]
