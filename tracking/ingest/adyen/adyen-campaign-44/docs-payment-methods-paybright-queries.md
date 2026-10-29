# PayBright retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-paybright`
**Full pinned raw:** `raw/adyen/docs/payment-methods/paybright/2026-09-15.md`
**Verified locators:** `# PayBright`, lines 15–23 (CA purpose, Affirm acquisition, no new Adyen integrations, conditional risk and payout wording); feature matrix lines 31–33.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paybright.md` → pinned raw.
**Answer boundary:** historical page evidence does not establish present merchant availability, shopper approval, successful execution, capture or settlement.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** `# PayBright`, lines 23–29 (four installments, conditional PayBright risk checks and redirect/return); feature matrix lines 31–33 (CA/CAD, recurring and refund/capture marks, unresolved chargeback note); `## How do you want to integrate?`, lines 35–65 (child routes).
**Answer boundary:** PayBright is a CA/CAD redirect BNPL method in this capture, with four installments and conditional PayBright risk acceptance. The page says Adyen does not accept new PayBright integrations. Follow the relevant child guide for implementation fields and result handling; the overview gives no SDK/version or detailed prerequisites.
