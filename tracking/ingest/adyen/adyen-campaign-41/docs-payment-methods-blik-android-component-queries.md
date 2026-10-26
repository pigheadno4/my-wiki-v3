# docs-payment-methods-blik-android-component — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-blik-android-component]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-blik-android-component]] is the BLIK Android Components v5.0.0 add-on, with separate Sessions and Advanced base-guide routes and an explicit earlier-versions link (raw lines 15–39, 61–67). It says nothing about the detailed code form, `await` action, result-code, webhook, One Click, tokenization or payment outcome (full raw, lines 1–85). The dated v5.0.0 scope and 2026-09-15 capture do not establish later SDK behavior or current merchant activation (raw lines 2, 11, 21, 31, 38).

## Q2 — What central capability, prerequisites, and warnings are stated?

[[source-adyen-docs-payment-methods-blik-android-component]] requires an existing Sessions or Advanced Android Components integration at v5.0.0 minimum and BLIK added in Customer Area (raw lines 23–39). It states no additional BLIK-specific fields for Sessions `/sessions` or Advanced `/payments`, and no additional method-specific Component configuration for either flow (raw lines 41–59). It then points to the base guide's create-session or launch/show step (raw lines 61–67). For TEST code payments, it gives `999000`, BLIK guidelines and end-to-end testing; live acceptance requires BLIK in live Customer Area (raw lines 69–79). The linked base guides, not this short add-on, must supply the rest of the flow.
