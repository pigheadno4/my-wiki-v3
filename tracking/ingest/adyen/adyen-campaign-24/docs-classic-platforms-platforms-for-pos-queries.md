# C24 Classic Platforms POS retrieval checks

## Q1 — What must be ready before a Classic account holder processes POS payments?

Have a Terminal API integration and give Adyen Support the intended countries, currencies, MCCs and payment methods so store creation can be enabled (raw lines 28–43, 109–113). Subscribe to store status changes, create the holder store via Classic Account API details, and wait for its `Active` store-status notification; a `Pending` response is insufficient (raw lines 45–55, 115–133, 218–253). Assign/configure and board a terminal for that store (raw lines 275–294). Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-platforms-for-pos]] → [[raw/adyen/docs/classic-platforms/platforms-for-pos/2026-09-15]].

## Q2 — How do split overrides and capture outcomes limit the example flow?

Store-level automatic split rules can be overridden by per-payment or capture API split instructions; `MarketPlace`/`VAT` target a specified account and `Commission`/`PaymentFee` the platform liable account (raw lines 296–303, 335–353). If the final split is unknown at payment time, enable manual POS capture—which applies to all POS account holders—and submit a capture split; `status: received` is only request receipt, with the CAPTURE webhook giving the outcome (raw lines 407–417, 872–880). The prose labels a Terminal API subscription endpoint while the example calls Notification API v6, and the USD capture story has a NodeJS EUR request; verify these before copying code (raw lines 49–62, 432–445, 640–660). Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-platforms-for-pos]] → [[raw/adyen/docs/classic-platforms/platforms-for-pos/2026-09-15]].
