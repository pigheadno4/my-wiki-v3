# Fixed queries — docs-plugins-netsuite-supported-payment-methods

## Q1 — purpose, scope, and what not to infer

**Question:** What does the NetSuite bundle payment-method table show, and does a listed check mark establish live account eligibility?

**Expected answer:** The dated page lists bundle-supported and unavailable methods by named country/region across cards, cash/ATM, direct debit, online banking, BNPL, prepaid/gift cards and wallets. It says “latest version” without naming a version. A check mark identifies table availability, not that the merchant account has requested or been approved for a method, that the method supports a particular currency, or that a shopper payment succeeded. Method requests are submitted separately for a selected test or live merchant account. Route: [[index]] → [[adyen-index]] → [[adyen-netsuite]] → [[source-adyen-docs-plugins-netsuite-supported-payment-methods]] → [[raw/adyen/docs/plugins/netsuite/supported-payment-methods/2026-09-15]]. Raw locators: opening lines 15–21; request path lines 23–36; method tables lines 38–165.

## Q2 — central capability, prerequisites, and warnings

**Question:** Which method-specific exceptions and scope boundaries matter before selecting a NetSuite payment method?

**Expected answer:** Check the exact method row and country/region. The bundles exclude product-page express Pay buttons, while Apple Pay and Google Pay are separately marked available in the wallet table; the table does not define their checkout placement. Generic Gift cards are marked unavailable while Nordic gift card via NETS is marked available. PayPal is listed but partial captures are unsupported. Trustly has a separate note that additional European country/region coverage requires Support information. Request a method through the merchant account in test or live Customer Area and await actual account-specific enablement. This page does not specify currency, tokenization, refunds, POS-terminal behavior or NetSuite ERP processing profiles. Route: [[index]] → [[adyen-index]] → [[adyen-netsuite]] → [[source-adyen-docs-plugins-netsuite-supported-payment-methods]] → [[raw/adyen/docs/plugins/netsuite/supported-payment-methods/2026-09-15]]. Raw locators: express limit line 21; request path lines 23–36; online banking/Trustly lines 87–109; gift-card rows lines 125–131; wallets and PayPal footnote lines 133–165.
