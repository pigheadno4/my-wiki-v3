---
title: "Payment notifications in NetSuite | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/netsuite/payment-notifications-in-netsuite"
raw_files:
  - "adyen/docs/plugins/netsuite/payment-notifications-in-netsuite/2026-09-15.md"
tags: [adyen, netsuite, webhooks, notifications, chargebacks]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot explains where NetSuite Customer Center users view asynchronous Adyen payment notifications and chargeback notifications. A notification can confirm a transaction or communicate a later status change; the page explicitly warns that an earlier sales-order `approved='true'` authorization status may later be revoked. Log visibility is not financial finality. [[adyen-netsuite]]

## Key takeaways

- Adyen webhooks are called notifications in NetSuite. The **View Gateway Asynchronous Notifications** route opens a Notifications Log; a transaction can have one or more entries, and multiple Payment Processing Profiles can produce multiple entries for a single transaction. Treat the log grain as notification entries, not one final row per payment or one order record per webhook.
- The page says received notifications appear in the NetSuite log immediately upon receipt, with no lag between NetSuite receipt and display. This is a receipt-to-display claim only; it does not guarantee when Adyen sends a callback, network delivery, webhook processing, or a final payment result. The page gives no access-role matrix or signature-validation procedure for the viewer.
- For shopper-initiated chargebacks or reversals of chargebacks, Adyen sends corresponding notifications and the Adyen Payment Processing plugin creates NetSuite chargeback records visible under **View chargeback notifications**. Those records document the cited events, not a guaranteed final dispute result, refund, payout or bank credit.

## Detail locators

- **Transaction confirmation/status change, revocable authorization and gateway log:** raw lines 16–26.
- **Asynchronous bundle view and multiple-profile entry qualification:** raw lines 28–35.
- **Chargeback notifications and generated record view:** raw lines 37–45.

## Related

- [[adyen]]
- [[adyen-netsuite]]
- [[adyen-webhooks]] — separate webhook delivery and verification context

## Raw Sources

- [[raw/adyen/docs/plugins/netsuite/payment-notifications-in-netsuite/2026-09-15|Adyen NetSuite payment notifications — collected 2026-09-15]]
