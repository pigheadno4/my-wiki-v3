---
title: "Adyen POS unreferenced refund"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/unreferenced"
raw_files:
  - "adyen/docs/point-of-sale/basic-tapi-integration/refund-payment/unreferenced/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, unreferenced-refund, fraud, refund-webhook]
---

## Overview

This unversioned Adyen website guide, captured on 2026-09-15, describes a POS **unreferenced refund** to a card presented at the terminal without linking the request to the original payment. Unlike the referenced POS `ReversalRequest`, this is a Terminal API `PaymentRequest` with `PaymentData.PaymentType: Refund`. It applies to Terminal API integrations with payment terminals or an eligible Mobile solution; it is separate from an online Checkout API refund. The merchant must reconcile the refund to its original purchase.

## Key takeaways

- An unreferenced refund can return an amount to **any card presented**, so it carries duplicate-refund, wrong-card, wrong-amount and return-fraud risk. Adyen says the merchant is **fully liable** for fraudulent or duplicate losses. Adyen strongly recommends POS reconciliation to the original purchase. A same-card check is an optional mitigation that requires card acquisition and saved card aliases; this page does not state the PCI scope of that optional step.
- Enablement is gated. The page excludes certain MCCs and lists Brazil, Mexico, Australia, Malaysia, Singapore, Hong Kong and India as countries where the feature cannot be enabled. QR-code wallets such as Alipay and WeChat Pay cannot receive an unreferenced refund; use a referenced refund. Gift-card refunds need additional parameters described in a separate guide. None of these examples proves account permission or supported card acceptance.
- Customer Area enablement for a **store or individual terminal/mobile device** requires the **Merchant POS Terminal Management** role. API enablement at store/terminal scope uses a Management API credential/key with **Terminal settings read and write** role and a PATCH to `/terminalSettings` setting `refunds.unreferenced.enableUnreferencedRefunds: true`; a cloud Terminal API integration may reuse its existing API key. Company or merchant-account enablement requires Adyen Support. The page supplies no different refund request for local versus cloud communications.
- The Management API setting only **enables** unreferenced refunds. A store/terminal limit is set in Customer Area, where the UI calls it **Offline limit for unreferenced refunds**; the guide says Adyen Support can set limits at company/merchant/store/terminal level. A refund above the configured per-refund maximum fails. A refund delay, set through Support at company/merchant-account level, leaves a review window to cancel before completion. Do not infer an API field for either limit or delay from the enablement PATCH.
- The POS sends `MessageCategory: Payment`, `PaymentType: Refund`, a terminal `POIID`, merchant refund reference/timestamp, and refund currency/amount. The shopper presents the card to the terminal. If the original payment was offline, its tender reference may be included in the merchant refund reference to aid reconciliation; this does not establish how to execute a refund while disconnected.
- `PaymentResponse.Response.Result: Success` says Adyen received the request. Processing is **usually asynchronous**, dependent on scheme and card-use country/region. If the response includes `acquirerResponseCode: Approved`, the guide says that request was processed synchronously and approved. It still directs the merchant to the **REFUND_WITH_DATA** webhook for outcome; a terminal approval screen or generic `Success` must not be read as universal finality.

## Detail locators

- Unreferenced identity, reconciliation/fraud controls and optional card acquisition: raw lines 15-23.
- Integration, Customer Area/API roles, REFUND_WITH_DATA webhook, country/MCC and QR-wallet exclusions, limits and Support boundary: raw `## Requirements`, lines 25-48.
- Liability, per-refund limit and review delay: raw `## Risk with unreferenced refunds`, lines 50-59.
- Store/terminal versus company/merchant enablement, Customer Area controls, API PATCH and permission-error example: raw `## Enable unreferenced refunds`, lines 61-140.
- Payment request, `PaymentType: Refund`, card presentation, response fields and conditional synchronous code: raw `## Make an unreferenced refund`, lines 142-328.
- Linked cancellation, refund-outcome, offline, standalone and FAQ routes: raw `## See also`, lines 330-336. These are navigation; this page does not establish the linked flow details.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-terminal-api]]
- Separate online Checkout refund concept: [[adyen-refunds]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/basic-tapi-integration/refund-payment/unreferenced/2026-09-15|Adyen POS unreferenced refund]] — full captured enablement and request guide
