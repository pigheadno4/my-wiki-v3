# Fixed retrieval checks: custom cards

1. **Question:** Does Adyen process a custom-card payment after a merchant swipes its employee-benefit card on a terminal?
   **Expected answer:** The documented Adyen Terminal API flow reads a Support-enabled custom magnetic-stripe card by swipe and returns data to the merchant POS. The merchant processes any transaction through that card's issuer. The acquisition response is not proof of Adyen authorization or settlement, and this is separate from Adyen-managed gift-card stored-value payment. Source: pinned raw opening, `## Requirements`, `## How it works`, `## Make a card acquisition request` (2026-09-15 snapshot).

2. **Question:** What must happen after custom-card acquisition, and does `AbortTransaction` refund an issuer-side payment?
   **Expected answer:** The merchant sends a Terminal API `EnableService` request with `TransactionAction=AbortTransaction` to stop the continuing card-acquisition loading screen, free the terminal and have it discard the card data. This aborts the acquisition flow, not a separate issuer transaction. The acquisition response may contain sensitive PAN and raw track data; the page does not grant a PCI exemption or specify storage controls. Source: pinned raw `## Make a card acquisition request`, `## Complete the card acquisition` (2026-09-15 snapshot).
