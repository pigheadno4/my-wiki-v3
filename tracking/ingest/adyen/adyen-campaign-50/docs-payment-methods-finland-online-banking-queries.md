# Retrieval checks: Online banking Finland

## Q1 — Purpose and scope
Query: What does Adyen's Online banking Finland overview describe, and what does it not prove?
Expected: It is a 2026-09-15-captured Paytrail-backed Finnish bank-redirect method overview with shopper journey, FI/EUR capability matrix and integration routes. It does not prove current bank coverage, account eligibility, a completed payment, or a child-guide request recipe. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-finland-online-banking]] → [[raw/adyen/docs/payment-methods/finland-online-banking/2026-09-15|pinned raw]]. Verify canonical stem `/payment-methods/finland-online-banking`, raw lines 15–23 and **How do you want to integrate?** lines 38–80.

## Q2 — Bank journey and capabilities
Query: Where does the shopper choose a bank, and what does the captured capability table establish?
Expected: Intro says bank choice in checkout dropdown then bank website/app redirect (raw line 23); numbered journey says first Adyen-hosted payment page for bank choice, then bank authentication/account/one-time code and merchant return (lines 25–32). The page does not reconcile these locations. Matrix labels Online Banking/redirect/FI/EUR, crosses recurring, listed capture variants and chargebacks, checks refunds and partial/multiple partial refunds. Refunds cell says “See note” but no note appears, so do not infer its missing condition. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-finland-online-banking]] → [[raw/adyen/docs/payment-methods/finland-online-banking/2026-09-15|pinned raw]]. Verify canonical stem and raw lines 23–36.
