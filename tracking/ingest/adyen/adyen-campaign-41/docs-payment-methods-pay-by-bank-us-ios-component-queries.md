# docs-payment-methods-pay-by-bank-us-ios-component retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-pay-by-bank-us-ios-component]].

## Q1 — What is this source for, and what cannot be inferred?

The 2026-09-15 guide adds Pay by Bank (US) Redirect Component to existing iOS Components, with Sessions and Advanced prerequisites, regular/stored Component examples, capture/recurring scope and Plaid live registration (pinned raw lines 15–37, 59–150, 203–207). It does not prove account/bank eligibility, completed Plaid registration, captured funds or payment success. Authorization-time checks do not hold funds, and ACH capture can still fail for insufficient funds (lines 132–138). Canonical source stem: `source-adyen-docs-payment-methods-pay-by-bank-us-ios-component`.

## Q2 — What are central prerequisites, flow and warnings?

Both flows require iOS Components **5.70.0+** and Customer Area addition; the broader Sessions v5.0.0-default statement is distinct (pinned raw lines 25–45). Sessions marks `countryCode` required but says US is the default if omitted; the `/payments` row is optional/recommended, with only US currently supported in both descriptions (lines 47–57). The Swift examples choose regular `PayByBankUSComponent` or stored `StoredPaymentMethodComponent`, delegating to session or self by flow; base Components handles redirect/outcome (lines 59–130). Immediate capture is strongly recommended but cannot eliminate asynchronous ACH insufficient-funds risk; recurring tokenization and explicit shopper permission are recommended (lines 132–150). TEST can simulate an Authorised payment followed by post-capture/settlement CHARGEBACK (lines 182–201). LIVE requires Plaid registration after Customer Area addition; the `paymentMethod.created` webhook signals acceptance can start (lines 203–207). Canonical source stem: `source-adyen-docs-payment-methods-pay-by-bank-us-ios-component`.
