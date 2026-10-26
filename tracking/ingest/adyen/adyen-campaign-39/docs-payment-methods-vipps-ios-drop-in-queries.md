# Vipps iOS Drop-in retrieval checks

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-vipps-ios-drop-in]]`.

## Q1. What is its purpose and scope, and what cannot be inferred?

The canonical stem `source-adyen-docs-payment-methods-vipps-ios-drop-in` is a 2026-09-15 Vipps-specific add-on for existing iOS Drop-in Sessions and Advanced server-side flows (`raw/adyen/docs/payment-methods/vipps/ios-drop-in/2026-09-15.md:15-25,104-114`). It is not evidence of present merchant enablement, a completed payment, capture or settlement; test-app approval is only a shopper step, and live status is checked through a webhook and Customer Area after separate live setup (`:80-102,160-174,180-204`). NOK/NO and return URLs in TEST examples are illustrative, not general eligibility or return-URL rules (`:49-65,137-157`).

## Q2. What are the central capability, prerequisites, and warnings?

Sessions needs an existing iOS Drop-in Sessions integration, Checkout API v68+ and Vipps added in Customer Area (`raw/adyen/docs/payment-methods/vipps/ios-drop-in/2026-09-15.md:29-34`). Its `/sessions` table gives `shopperStatement` with a `reference` fallback and a 100-minor-unit/1.00-NOK minimum, while Required cells remain blank (`:38-45`). Advanced needs an existing iOS Drop-in Advanced integration, redirect handling and Customer Area setup (`:108-114`); its `/payments` table describes optional-looking phone prefill, statement fallback, channel and the same amount minimum, again with blank Required cells (`:124-133`). Neither flow adds Vipps-specific Drop-in configuration (`:68-72,116-120`). The Advanced example returns `RedirectShopper` and `action.type: redirect`, an intermediate redirect rather than final authorization (`:135-174`). The Advanced `channel` and `amount.value` links point at `/paymentMethods` anchors even though the section is about `/payments` (`:132-133`). TEST needs the Vipps developer test app and test-merchant addition (`:78-92,180-194`); LIVE needs a separate live Customer Area request followed by low-amount payment, `AUTHORISATION` webhook and live payment-list checks (`:94-102,196-204`).
