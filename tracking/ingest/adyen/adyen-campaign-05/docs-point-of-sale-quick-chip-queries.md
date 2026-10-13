# Fixed retrieval checks — Adyen Quick Chip

## 1. Purpose, scope, and exclusions

**Query:** What does Quick Chip do, and what does early card removal prove?

**Answer:** The 2026-09-15 guide describes a US-only Terminal API pattern allowing a shopper to insert and remove an EMV chip card before the final sale amount or authorization response is available (raw lines 17–29). The POS first acquires card details and later sends a separate payment request. Early removal or `CARD_ACQ_COMPLETED` is not authorization, capture, or settlement; the payment response gives the later result. The guide requires terminal software 1.95+ and Support enablement and does not prove any particular merchant, terminal, card scheme, or present SDK/version eligibility.

**Route:** [[index]] → [[adyen-index]] → [[adyen-terminal-api]] → [[source-adyen-docs-point-of-sale-quick-chip]] → [[raw/adyen/docs/point-of-sale/quick-chip/2026-09-15]] (catalog promotion pending).

## 2. Sequence, identifiers, and money flow

**Query:** How does the POS link a preinserted card to the final-amount payment, and which sample caveats matter?

**Answer:** Send Service/`CardAcquisition` with a required `CardAcquisitionTransaction` object, empty or with placeholder `TotalAmount` while checkout totals the goods (raw lines 31–62). Check the acquisition response for `CARD_ACQ_COMPLETED`, retain its `POIData.POITransactionID.TimeStamp` and `TransactionID`, and place both in `PaymentData.CardAcquisitionReference` of a later Service/`Payment` request with the final `RequestedAmount` (lines 94–171). A successful payment is determined from the payment response (lines 214–264). `ServiceID` must be unique for 48 hours per terminal `POIID` (lines 45–53, 151–159). The guide's examples reuse a ServiceID and mismatch acquisition IDs, request/response amounts, and chip-versus-Contactless mode, so they should not be treated as one executable transaction.

**Route:** [[index]] → [[adyen-index]] → [[adyen-terminal-api]] → [[source-adyen-docs-point-of-sale-quick-chip]] → [[raw/adyen/docs/point-of-sale/quick-chip/2026-09-15]] (catalog promotion pending).
