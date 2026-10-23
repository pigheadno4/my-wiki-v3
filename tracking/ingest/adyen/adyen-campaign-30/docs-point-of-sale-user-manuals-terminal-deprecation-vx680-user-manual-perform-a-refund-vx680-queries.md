# C30 VX680 standalone refund retrieval checks

## Q1 — Main purpose and prerequisites

**Question:** What does this historical VX680 refund page cover, and what must be enabled or entered before amount entry?

**Answer:** It describes a refund when the VX680 is in standalone mode (pinned raw lines 15–17). The page says Adyen enables refunds per device and that a password must be entered (line 22). Its steps show an **image-only key plus 8** for Special Payments, a PIN to unlock the device, and then the amount (lines 28–30). It does not say whether the password and PIN labels identify the same credential. Route: [[index]] → [[adyen-index]] → [[adyen-payment-terminals]] → [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-perform-a-refund-vx680]] → [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/perform-a-refund-vx680/2026-09-15]].

## Q2 — Material boundary or failure

**Question:** What does the top-bar exclamation mean, and does following the steps prove a completed refund or present-day VX680 transaction support?

**Answer:** The exclamation means the terminal holds data it could not synchronize with Adyen because it lacked outgoing Internet access (pinned raw line 19). The last step only says to enter the amount and proceed like a normal transaction (line 30); no refund response, settlement or shopper credit is recorded. The separate eVo deprecation table lists VX680 with a historical **29 March 2024** “No more transactions” date (deprecation raw lines 32–35). Route: [[index]] → [[adyen-index]] → [[adyen-payment-terminals]] → [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-vx680-user-manual-perform-a-refund-vx680]] → [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/perform-a-refund-vx680/2026-09-15]].
