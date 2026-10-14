# Fixed answers: Order terminals with Management API

## Query 1 — Can a merchant order a test terminal by posting the example terminal order to the Management API test endpoint?

**Answer:** No. This guide covers Management API ordering of live payment terminals, accessories, and enabled hardware kits for a company or merchant account. A request to the Management API test endpoint does not create an actual order for a test terminal. For test hardware, the guide routes the merchant to a sales order in the test Customer Area. The sample `management-test.adyen.com/v3` curl and SDK calls demonstrate request shape; they do not prove a physical test order, current inventory, pricing, account eligibility, or a successful live order.

**Prerequisites and warnings:** The POS integration needs an API key with the applicable Management API Terminal ordering read or read-and-write role. Live terminal-order endpoints have rate limits. For live ordering, first discover the account and country-filtered terminal products, then use product IDs plus a shipping location ID and normally a billing entity ID; Brazil is the billing-entity exception. Hardware kits require Adyen enablement and packaging onboarding, and cannot be mixed with non-kit items. Terminals are region-specific.

**Retrieval route:** [[source-adyen-docs-point-of-sale-automating-terminal-management-order-terminals-api]] → pinned [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15|Requirements; Create a terminal order]]. The source entry is pending coordinator catalog promotion.

## Query 2 — What can be changed after an Adyen terminal order is placed, and can cancelling that order refund a payment?

**Answer:** The guide lets the company or merchant account list or retrieve an order, then update its items, shipping location, or billing entity, or cancel the order, **only while its status is `Placed`**. An `items` update replaces the whole array, so it must include every item to retain. Order cancellation uses `POST .../terminalOrders/{orderId}/cancel` with no request body. This is cancellation of a hardware purchase order; the guide does not establish payment-refund behavior.

**Prerequisites and warnings:** Check the order ID and current `Placed` status before a change; once processing advances, the guide does not allow update or cancellation. Order-update platform webhooks are optional logistics notifications; email and Customer Area are also described. The guide does not promise that a cancellation reverses an external charge, and its example `Cancelled` response is not a live outcome.

**Retrieval route:** [[source-adyen-docs-point-of-sale-automating-terminal-management-order-terminals-api]] → pinned [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15|Manage orders; Update an order; Cancel an order]]. The source entry is pending coordinator catalog promotion.
