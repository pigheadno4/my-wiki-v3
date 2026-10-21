# Retrieval checks — docs-marketplaces-internal-fund-transfers-approve-cancel-transfers

Q1. What is this review gate for, and what must be in place? Answer: A Marketplace transfer can include a `review` object at POST `/transfers` so a designated team member approves or cancels the pending request before Adyen processes it; the API key needs TransferService Approval role and Transfer Webhooks subscription. One or more IDs, at most 500, go to POST `/transfers/approve` or `/transfers/cancel`. Raw lines 19–30, 38–58, 261–267.

Q2. What outcomes and evidence boundaries matter? Answer: Approval authorizes continued processing, cancellation fails and stops the request, and no decision within 30 days fails it. HTTP 200 or `authorised` / `approved` webhook does not prove booking. Pending review shows `received` / `pending`; cancellation shows `cancelled` / `unknown`. The three webhook JSON examples are TEST outgoing bank transfers (`category: bank`, `type: bankTransfer`), not an internal two-leg booking or bank-receipt proof. Raw lines 40–48, 259, 468, 470–495, 501–562, 565–571, 577–650, 653–660, 666–736.

Forward route: [[index]] → [[adyen-index]] → [[adyen-platform-internal-transfers]] → [[source-adyen-docs-marketplaces-internal-fund-transfers-approve-cancel-transfers]] → [[raw/adyen/docs/marketplaces/internal-fund-transfers/approve-cancel-transfers/2026-09-15]].
