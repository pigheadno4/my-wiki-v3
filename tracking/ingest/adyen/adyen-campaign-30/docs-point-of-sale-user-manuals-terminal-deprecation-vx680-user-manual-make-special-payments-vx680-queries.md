# C30 VX680 Special Payments retrieval checks

## Q1 — Main purpose and prerequisites

**Question:** What does the VX680 Special Payments page describe, and what controls access to its options?

**Answer:** It describes the historical VX680 custom or ad hoc Special Payments menu, whose contents may vary by merchant configuration (pinned raw lines 14–16). The entry steps use an illustrated key plus 8 and require a PIN to unlock the device (lines 20–24); the raw provides no textual name for the image-only key. The listed normal and manual-entry choices are expressly configuration-dependent (lines 26–30). Route: [[index]] → [[adyen-index]] → [[adyen-payment-terminals]] → [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-make-special-payments-vx680]] → [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/make-special-payments-vx680/2026-09-15]].

## Q2 — Material boundary or failure

**Question:** Does selecting manual entry or seeing the refund option prove a transaction or refund succeeded, or that VX680 remains supported?

**Answer:** No. The manual-entry example prompts for amount, PAN and expiry, then only says the transaction follows the normal flow; it reports no result (pinned raw lines 30–35). The refund is a pointer to a separate procedure (line 37), and the menu's options depend on merchant configuration (line 16). The separate eVo deprecation table lists VX680 with a historical **29 March 2024** “No more transactions” date (deprecation raw lines 32–35). Route: [[index]] → [[adyen-index]] → [[adyen-payment-terminals]] → [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-make-special-payments-vx680]] → [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/make-special-payments-vx680/2026-09-15]].
