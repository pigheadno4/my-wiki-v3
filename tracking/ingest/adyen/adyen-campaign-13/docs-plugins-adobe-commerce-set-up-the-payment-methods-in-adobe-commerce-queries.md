# Fixed retrieval checks — Adobe Commerce payment-method setup

Q1. What does this configuration guide cover, and what must not be inferred?
- Expected: Add methods to Adyen Customer Area first, then enable them in Adobe Commerce admin to render them in checkout. Card, alternative, online, headless, express and admin-order settings have distinct conditions. The page does not pin a plugin version or prove current account/method eligibility, live checkout, authorization, capture, refund, settlement or a token-consent contract; stored methods are a linked next step.
- Raw locators: `raw/adyen/docs/plugins/adobe-commerce/set-up-the-payment-methods-in-adobe-commerce/2026-09-15.md:15-37`, `:197-213`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-adobe-commerce-set-up-the-payment-methods-in-adobe-commerce.md` → `[[adyen-magento2]]`.

Q2. Which method-specific prerequisites, roles and outcome warnings matter?
- Expected: Visa requires visible and required holder name; card installments have regional limits and per-card setup. Headless origin/return fields differ from standard checkout return path. PayPal Express phone requirements must align; PayPal HUF transaction and line-item rounding must match. Mixed gift-card refunds have a configured strategy and headless gift cards need separate steps. Pay by Link needs Customer Area permission and remains unfinished until shopper payment, with cron closing unfinished orders; MOTO needs a MOTO merchant account and keys/mode. Giving is enabled by default but uses active campaigns and separate testing; setup does not prove a donation charge.
- Raw locators: `raw/adyen/docs/plugins/adobe-commerce/set-up-the-payment-methods-in-adobe-commerce/2026-09-15.md:39-76`, `:78-121`, `:136-195`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-plugins-adobe-commerce-set-up-the-payment-methods-in-adobe-commerce.md` → `[[adyen-magento2]]`.
