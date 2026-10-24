# WeChat Pay overview retrieval questions

## Q1 — What is this page for, and what must be true to use a route?

It is Adyen's historical WeChat Pay overview and chooser for website, mobile-app and in-person acceptance, with distinct desktop QR/H5, native in-app, Pay by Link, POS and Mini Program links (raw lines 27–33, 41–71). The explicit mobile-website condition is initiation from the WeChat app (line 33). The overview's `International`/`Multiple` table labels do not establish a specific merchant, country or currency's eligibility (lines 37–39). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-wechat-pay]] → [[raw/adyen/docs/payment-methods/wechat-pay/2026-09-15]].

## Q2 — What are the material capability and outcome boundaries?

The table describes an additional-action wallet, marks refunds including partial and multiple partial refunds, and marks recurring, separate/partial/multiple partial capture and chargebacks unavailable in this snapshot (raw lines 37–39). Most outcomes receive immediate confirmation, but a small number require webhook confirmation, so handoff or an initial response cannot universally prove success (line 35). The “Desktop QR and H5” mobile-browser link is broader than the explicit mobile-web WeChat-app initiation condition; child flow details are separate (lines 33, 45–47). This snapshot does not prove current enablement, authorization, capture, settlement or refund. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-wechat-pay]] → [[raw/adyen/docs/payment-methods/wechat-pay/2026-09-15]].
