# Fixed retrieval queries — Adyen Giving seasonal page

## Q1 — Purpose, scope, and what it does not infer

**Question:** What does the peak-season Adyen Giving page cover, and what must not be inferred?

**Answer:** It introduces shopper donations tied to a purchase, nonprofit selection and campaign management, and points to in-person, online and platform Giving routes. Its final-two-months framing is seasonal advice, not an eligibility period. The fee/full-donation/direct-nonprofit-settlement statements describe Adyen’s product claims; the snapshot does not prove a merchant’s campaign, raised amount, donation outcome, nonprofit bank receipt, permissions, or current channel eligibility. Canonical route: [[index]] → [[adyen-index]] → [[adyen-giving]] → [[source-adyen-docs-industries-peak-season-giving]]; seasonal context [[adyen-peak-season-readiness]]. Raw: `raw/adyen/docs/industries/peak-season/giving/2026-09-15.md`, lines 15–31 and 52–56.

## Q2 — Central capability, prerequisites, and warnings

**Question:** How do the page’s in-person and online Giving paths differ, and what checks does it defer?

**Answer:** In both cases the merchant manages a Customer Area Campaigns donation campaign and selects a nonprofit. For in-person payments, the configured campaign can show a terminal donation prompt automatically without integration work, with an optional Terminal API trigger. For online payments, the merchant integration displays a donation form and sends a separate `/donations` request if the shopper opts in, in addition to the payment request. Before a campaign, the page points to channel-specific supported geographies/currencies, methods, terminal models and donation options; this raw page does not contain those matrices or grant campaign permissions. It links platform donations without describing their flow. Raw lines 25–56. Route: [[index]] → [[adyen-index]] → [[adyen-giving]] → [[source-adyen-docs-industries-peak-season-giving]].
