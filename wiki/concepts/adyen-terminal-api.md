---
title: "Adyen Terminal API"
type: concept
category: technology
tags: [adyen, terminal-api, in-person-payments, point-of-sale, nexo]
---

## Adyen Terminal API

Adyen Terminal API is a Nexo-based message interface between a point-of-sale system and an Adyen payment terminal. A request wraps a message header containing protocol, class, category, type, sale ID, service ID, and terminal `POIID`, followed by category-specific payment, reversal, input, display, print, reconciliation, or stored-value data.

## Integration boundary

The retained Postman collection demonstrates Terminal API operations for terminal-present payments, refunds, shopper input, display and printing, reconciliation, card acquisition, tipping, instalments, and gift cards. It explicitly routes capture, recurring token charges, and authorization adjustments to Checkout API, and store or terminal-fleet administration to Management API.

Cloud transport requires an API key and a terminal ID. Merchant implementations must keep credentials private, generate unique request identities, correlate asynchronous or in-process operations, handle result and error fields, and avoid treating Postman test scripts as a production POS state machine.

## Payment and interaction patterns

- Payment messages can carry amounts, cashback, platform splits, tokenization data, MOTO/manual-entry conditions, tipping, or card-acquisition references.
- Reversal supports referenced full or partial refund examples; an unreferenced refund is represented as a refund payment.
- Abort and transaction-status messages control or inspect an in-process request.
- Input, display, print, barcode/QR, and admin messages let a POS coordinate shopper-terminal interactions outside the payment payload itself.
- Stored-value examples cover gift-card activation, payment, balance inquiry, loading, reversing a load, and refund.

These are exact-commit examples. Supported hardware, merchant enablement, regional rules, and current schema behavior must be confirmed from current Adyen documentation and live/test responses.

## Cloud Device distinction

Terminal API defines terminal messages. Adyen's Cloud Device API, represented separately by the Node.js library baseline, is a newer cloud transport and device-management surface using generated `tapi` models. Local Terminal API communication and legacy cloud Terminal clients remain distinct architectures; do not merge their version histories.

## Related

- [[source-github-adyen-postman]] - Postman request examples at exact commit
- [[changelog-github-adyen-postman]] - commit-qualified collection history
- [[adyen-node-api-library]] - Checkout v72 and Cloud Device API v1
- [[adyen]] - company and knowledge-status page
