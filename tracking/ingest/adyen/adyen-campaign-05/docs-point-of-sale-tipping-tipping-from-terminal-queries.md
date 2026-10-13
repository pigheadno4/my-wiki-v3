# Fixed retrieval checks — Adyen tipping from the terminal

## 1. Purpose, scope, and exclusions

**Query:** What does this page cover, and what should a reader avoid inferring?

**Answer:** The 2026-09-15 Adyen guide covers shopper tip entry on Adyen-provided payment terminals in a Terminal API integration. It describes tip-amount and total-amount prompts, configuration, the `AskGratuity` payment request, response amounts, and optional staff/reporting/warning features (raw lines 17–36, 38–132, 401–571). It does not prove current merchant/device/region eligibility, a present API or SDK version, configuration inheritance, capture timing, settlement allocation, or behavior of unread linked overrides.

**Route:** [[index]] → [[adyen-index]] → [[adyen-terminal-api]] → [[source-adyen-docs-point-of-sale-tipping-tipping-from-terminal]] → [[raw/adyen/docs/point-of-sale/tipping/tipping-from-terminal/2026-09-15]] (catalog promotion pending).

## 2. Central request, conditions, and money flow

**Query:** How do preset/custom tips and total entry work, and which amount is authorized?

**Answer:** For tip-amount mode, the terminal can offer up to four preset options or three plus a custom option; it can also prompt for a custom tip without presets. Before-card prompting is default, while after-card prompting requires Support enablement and single tap is optional (raw lines 38–71, 79–132). Total entry asks for a total at least equal to the original purchase and requires Support enablement; the guide calls it customary in Nordic regions (lines 401–410). In either mode, the Terminal API payment sends `AskGratuity` in `SaleToAcquirerData` and puts the **original purchase** in `RequestedAmount` (lines 416–452). The terminal then sends purchase plus tip to Adyen; `PaymentResponse` reports the tip if added and the total `AuthorizedAmount` (lines 489–509). A high-tip warning, if Support-enabled, compares the tip to the original purchase amount (lines 560–571). Standard webhooks are listed as a prerequisite and staff display notifications as optional (lines 26–36, 548–552).

**Route:** [[index]] → [[adyen-index]] → [[adyen-terminal-api]] → [[source-adyen-docs-point-of-sale-tipping-tipping-from-terminal]] → [[raw/adyen/docs/point-of-sale/tipping/tipping-from-terminal/2026-09-15]] (catalog promotion pending).
