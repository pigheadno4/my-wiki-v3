# Fixed retrieval checks — Adyen white POS test card v1

## 1. Purpose, scope, and limits

**Query:** What does the white v1 card page cover, and what should a reader avoid inferring?

**Answer:** It documents the white Adyen physical POS test card's Mastercard/Maestro application, currency, CVM, and decline fixtures for a test terminal. The page does not say v1 is retired, but explicitly says it cannot test contactless or mobile Tap to Pay; those tests are directed to green-blue v2.4+ (raw lines 15–33). It does not prove current hardware/software acceptance, other brands, offline-payment support, or live issuer/payment results.

**Route:** [[index]] → [[adyen-index]] → [[adyen-payment-testing]] → [[source-adyen-docs-point-of-sale-testing-pos-payments-test-card-v1]] → [[raw/adyen/docs/point-of-sale/testing-pos-payments/test-card-v1/2026-09-15]] (catalog promotion pending).

## 2. Simulation and warnings

**Query:** How do amount and currency select CVM or decline tests, and which conditions matter?

**Answer:** A payment-request currency or an inserted-card choice selects a programmed application (raw lines 35–47). Amount and currency select its CVM row; repeated wrong PIN attempts block the card, while card-inserted online PIN tests accept any PIN and invalid offline PIN declines (lines 49–69). For decline simulation, the final three digits of `RequestedAmount` select a table row (lines 71–133). Do not code against `refusalReason`, `message`, or raw acquirer responses (lines 87, 135–139). Suffix 139 with `AllowPartialAuthorisation` produces a partial payment; some rows need terminal cancellation, several tap/mobile rows are inapplicable to white v1, and 156/160/161 are internal only. These fixtures do not establish live outcomes.

**Route:** [[index]] → [[adyen-index]] → [[adyen-payment-testing]] → [[source-adyen-docs-point-of-sale-testing-pos-payments-test-card-v1]] → [[raw/adyen/docs/point-of-sale/testing-pos-payments/test-card-v1/2026-09-15]] (catalog promotion pending).
