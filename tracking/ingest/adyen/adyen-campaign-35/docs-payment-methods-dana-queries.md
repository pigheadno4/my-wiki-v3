# DANA overview retrieval questions

## Q1 — What is this page's purpose and scope, and what cannot be inferred?

It is a DANA wallet overview for Indonesian **ID/IDR** redirect payments, with a shopper DANA-site login/PIN/confirmation journey and links to Web, native, API-only, Pay by Link and in-person guides (raw lines 23–33, 37–39, 43–91; [[source-adyen-docs-payment-methods-dana]]). The return redirect and displayed DANA result do not alone prove merchant-side final authorization or settlement, and the overview does not supply child API/SDK versions, token mechanics or webhook procedure. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-dana]] → [[raw/adyen/docs/payment-methods/dana/2026-09-15]].

## Q2 — What central conditions and limits does it give?

The redirect page lasts **five minutes by default**, then times out (raw line 35). A payment must be at least **300 IDR** for DANA to appear as available; meeting that floor is not an approval guarantee (line 41). The matrix marks recurring and refunds including partial/multiple partial available, but separate/partial/multiple partial captures and chargebacks unavailable in this historical snapshot (lines 37–39). These marks do not establish actual token consent, refund execution, current merchant eligibility or a successful payment ([[source-adyen-docs-payment-methods-dana]]). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-dana]] → [[raw/adyen/docs/payment-methods/dana/2026-09-15]].
