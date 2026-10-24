# Retrieval checks — docs-payment-methods-wallets-india-web-component

Q1. What does this Wallets India Web Component guide require for Sessions and Advanced?

A1. Sessions requires an existing Web Components Sessions flow, Checkout API v68+ and adding Wallets India in Customer Area; it imports WalletINElement and states no extra method-specific /sessions or configuration parameters (raw lines 23–75). Advanced separately requires an existing Advanced Web Components integration and Customer Area setup, imports the same element, and states no extra method-specific /payments or configuration parameters (raw lines 83–132). The page does not name issuers, currencies or redirect behavior. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-wallets-india-web-component]] → [[raw/adyen/docs/payment-methods/wallets-india/web-component/2026-09-15]].

Q2. Which sample and environment limits prevent treating this as a ready payment flow?

A2. Both snippets import WalletINElement but call undefined newWalletINElement, and comments refer to a configuration object despite prose saying no method-specific configuration (raw lines 45–75, 94–125). The page states there is no Wallets India test platform and requires a request in live Customer Area before accepting live payments (raw lines 77–81, 134–138); a request is not approval, and the page offers no authorization/capture/settlement result evidence. Checkout API v68+ appears in Sessions requirements only (raw lines 27–33, 85–90). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-wallets-india-web-component]] → [[raw/adyen/docs/payment-methods/wallets-india/web-component/2026-09-15]].
