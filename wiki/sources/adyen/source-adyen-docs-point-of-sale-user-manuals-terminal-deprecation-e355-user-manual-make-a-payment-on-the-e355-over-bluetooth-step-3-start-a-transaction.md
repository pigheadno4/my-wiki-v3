---
title: "Adyen e355 Bluetooth transaction-start step"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/step-3-start-a-transaction"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/step-3-start-a-transaction/2026-09-15.md"
tags: [adyen, point-of-sale, e355, bluetooth, terminal-deprecation]
---

## Overview

This 2026-09-15-captured [[adyen]] e355 manual step describes **starting** a POS-app card transaction after the terminal is boarded and connected over Bluetooth. A Bluetooth icon in the terminal status bar signals a connected device in this historical [[adyen-payment-terminals]] guide (raw lines 14–16). The page is under terminal deprecation and does not establish current e355 transaction support.

## Key takeaways

- **Precondition:** The e355 must be boarded and connected to the app before a cashier or shopper starts this flow; the icon is the page's visible connection cue, not payment authorization evidence (raw line 16).
- **Input sequence:** Enter an amount in the POS app and press **Card**. The manual then says to “Enter a card” when the terminal prompts and hand the terminal to the customer for PIN entry (raw lines 18–22). It does not specify a card-interface mode, firmware or protocol version here.
- **Approval wording limit:** The page states that a correct PIN results in approval (raw line 22). Treat that as the manual's simplified conditional flow description, not a guarantee that PIN correctness alone determines authorization or that any actual transaction was approved. It gives no response code, webhook, receipt, capture or settlement evidence.

## Detail locators

- Boarded/connected precondition and Bluetooth status icon: raw lines 14–16.
- Amount, Card selection, card prompt and customer PIN step: raw lines 18–22.

## Evidence boundary

This is a short historical user-manual procedure. It gives no live device eligibility, Bluetooth timing, firmware matrix or outcome record. Connection and PIN entry are setup/input states; the final sentence cannot verify a payment authorization, capture or merchant settlement for a particular transaction.

## Related

- [[adyen-payment-terminals]] — physical-terminal route.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-make-a-payment-on-the-e355-over-bluetooth-step-2-pair-the-e355-with-a-mobile-device]] — preceding pairing and boarding step.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-make-a-payment-on-the-e355-over-bluetooth-troubleshoot-the-bluetooth-connection]] — separate connection troubleshooting.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/step-3-start-a-transaction/2026-09-15|Pinned e355 transaction-start manual step, captured 2026-09-15]]
