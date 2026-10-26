# docs-payment-methods-trustly-android-component retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-trustly-android-component]].

## Q1 — What is this source for, and what cannot be inferred?

The 2026-09-15 page is the Trustly Android Components v5 guide, with a separate earlier-version link and Sessions/Advanced setup routes (pinned raw lines 15–39). It provides no redirect response, return/details request or final webhook outcome sequence (lines 41–81). It does not prove a transaction succeeded or funds were received; the related Trustly overview explicitly warns that successful AUTHORISATION only initiates a bank transfer and can be followed by an unfunded chargeback (overview raw lines 38–53). Canonical source stem: `source-adyen-docs-payment-methods-trustly-android-component`.

## Q2 — What are central prerequisites and warnings?

Sessions and Advanced each require existing Android Components at minimum **v5.0.0** and Trustly added in Customer Area; earlier versions use their own guide (pinned raw lines 19–39). This page says no Trustly-specific `/sessions` or `/payments` fields and no extra Component configuration, while the base flow still creates a checkout session or launches the Component (lines 41–67). TEST includes a `YYMMDD-XXXX` Login ID/Personal number format and Customer Area status check; LIVE acceptance requires a separate live Customer Area request (lines 69–75). Base-flow authorization is not proof of funding under the overview's chargeback warning (overview raw lines 38–53). Canonical source stem: `source-adyen-docs-payment-methods-trustly-android-component`.
