# C32 retrieval checks: express checkout

Q1. What is express checkout in this overview, and which method/version prerequisites does it list?

It places supported express-method options on product, cart or basket pages so a shopper need not visit a separate checkout page, while saying additional integration steps are required (raw lines 19–37). Its **Component** matrix says Apple Pay Web Advanced 5.0.0/Sessions 6.31.0, iOS Advanced 5.0.0/Sessions not supported; Google Pay Web Advanced 5.0.0/Sessions 6.31.0; PayPal Web Advanced and Sessions 5.59.0 (raw lines 39–48). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-express-checkout]] → [[raw/adyen/docs/payment-methods/express-checkout/2026-09-15]].

Q2. What boundary stops a reader from treating the overview as proof of available wallets or completed payment?

The matrix is conditional on method, platform, flow and Component version; notably iOS Apple Pay Sessions is marked not supported (raw lines 39–48). Checkout-page instant wallets, tokenization and Web-only Click to Pay are listed as alternatives, not equivalent express integrations (raw lines 66–84). Get-started child links give route selection, not merchant enablement, consent, authorization, capture, settlement or actual fulfillment data (raw lines 86–98). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-express-checkout]] → [[raw/adyen/docs/payment-methods/express-checkout/2026-09-15]].
