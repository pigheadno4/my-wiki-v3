---
title: "Adyen POS shopper engagement"
type: concept
category: technology
tags: [adyen, point-of-sale, shopper-engagement, terminal-api]
---

## Definition

Adyen's shopper-engagement documentation describes use of a payment terminal to interact with customers, with examples of displaying Terms and Conditions, asking for an opinion or contact details, and printing a ticket. The 2026-09-15 captured overview says these operations often appear in advanced flows such as loyalty and routes readers to Display, Input, Print and multi-request Session guides. [[source-adyen-docs-point-of-sale-shopper-engagement]]

## Evidence boundary

The overview is navigation, not an implementation contract. It does not specify Terminal API fields, session identity or lifetime, timeouts, asynchronous outcomes, consent or handling of contact details, or merchant/device support. Payment and refund message behavior belongs to [[adyen-terminal-api]] and its operation-specific sources; a displayed or collected shopper message by itself is not evidence of a financial transaction.

## Sources

- [[source-adyen-docs-point-of-sale-shopper-engagement-display-data]] — 2026-09-15 captured Display overview for out-of-payment terminal QR, virtual-receipt, image and idle-screen child-guide routes; request/response detail remains in child sources.


- [[source-adyen-docs-unified-commerce-shopper-engagement]] — Unified Commerce overview (2026-09-15 snapshot) naming POS-app Terminal API Input/Display as a shopper-interaction route; operation details remain in POS-specific sources.


- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input]] — shopper-input overview captured 2026-09-15: POS-app/terminal communication and merchant processing boundary, nine input-type child routes, and cancel/session navigation without child-guide behavior.


- [[source-adyen-docs-point-of-sale-shopper-engagement-display-data-display-image]] — 2026-09-15 Adyen Docs Device/Display image guide for Base64 file payloads, `MessageRef`/`Image` fields, replacement time and single-item `OutputResult` array.


- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-cancel-input]] — 2026-09-15 guide to POS Service/Abort targeting an active Device/Input request versus terminal Cancel, with distinct response checks and type-specific flags.


- [[source-adyen-docs-point-of-sale-shopper-engagement-display-data-idle-display]] — 2026-09-15 Terminal API standby-display guide for recommended MessageRef/Idle request, model-limited XHTML alternative and display-result check.


- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-text]] — historical Terminal API `GetText` InputRequest guide (2021-09-29 modified; 2026-09-15 capture) for shopper/staff text entry, placeholder/masking field discrepancy, merchant validation and timeout/Cancel/Busy branches; no identity, consent or payment outcome proof.


- [[source-adyen-docs-unified-commerce-terminal-interaction]] — 2026-09-15 Input/Display overview for terminal confirmation, text, menu and rating prompts plus image, QR and pre-payment purchase-overview display routes.


- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-signature]] — 2026-09-15 Device/Input signature guide for `GetSignature`/`GetConfirmation`, two-text/model conditions, raw signature and confirmation flag, and timeout/Busy branches.


- [[source-adyen-docs-point-of-sale-shopper-engagement-create-session]] — Adyen 2026-09-15 snapshot of Terminal API Admin Begin/End shopper-flow session and per-operation waiting screen for Input, Display and Payment requests; Admin success is separate from payment outcome.


- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-digit]] — 2026-09-15 Terminal API Device/Input GetDigit guide for unvalidated DigitString capture, masking-field discrepancy, merchant validation and timeout/Cancel/Busy outcomes.


- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-phone-number]] — Terminal API GetPhoneNumber input guide (2025 last-modified; 2026-09-15 capture) for prompt/default/mask fields, returned DigitInput and timeout/cancel/override outcomes.


- [[source-adyen-docs-point-of-sale-shopper-engagement-display-data-display-qr-code]] — 2026-09-15 Adyen Docs Device/Display QR guide for URL-encoded or plain-URL values, optional header/footer, duration, response flag and index-matched `OutputResult` array.


- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-confirmation]] — 2026-09-15 Terminal API Device/Input GetConfirmation guide for ordered prompt/button labels, ConfirmedFlag mapping, timeout and payment-override outcomes; input success is separate from payment or legal-consent proof.


- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-rating]] — 2026-09-15 Adyen Docs GetRating terminal InputRequest for Device/Input fields, prompt UI, unvalidated `DigitInput`, timeout, override and Cancel response branches.


- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-rating-rating-single-press]] — 2026-09-15 Terminal API `GetOneKeyRating` guide for immediate one-press rating, merchant-side validation, terminal limits, and timeout/Cancel/Busy outcomes.


- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-amount]] — 2026-09-15 Terminal API Device/Input GetAmount guide for terminal decimal entry, currency display, timeout/Cancel/Busy outcomes and merchant validation before further use.


- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-multi-menu]] — Terminal API multiple-answer MenuButtons input guide (2026-09-15 snapshot) for request fields, selection flags, bounds, timeout and cancellation/override outcomes.


- [[source-adyen-docs-point-of-sale-shopper-engagement-shopper-input-menu]] — Terminal API single-answer MenuButtons input guide (2025 last-modified; 2026-09-15 capture) for option display, selection indicators and timeout/cancel/override outcomes.


- [[source-adyen-docs-point-of-sale-shopper-engagement-display-data-display-receipt]] — 2026-09-15 Adyen Docs pre-payment virtual-receipt `DisplayRequest` guide for Base64 XML, template/model scope, persistence, response and conditional XSD validation.


- [[source-adyen-docs-unified-commerce-digital-receipts]] — 2026-09-15 example of terminal GetConfirmation input for an emailed-receipt choice before a separate POS payment and merchant delivery step.


- [[source-adyen-docs-point-of-sale-shopper-engagement-print-data]] — 2026-09-15 captured Device/Print Terminal API guide for out-of-payment text, QR and PNG printing, printer hardware/format limits, and `DeviceOut` result handling.


- [[source-adyen-docs-point-of-sale-shopper-engagement-third-party-interactions]] — historical third-party POS Input/Display guide (2022-12-27 modified; 2026-09-15 capture) for merchant-authorized non-payment terminal interactions, credentials, notifications/webhooks, privacy limits and cancellation conflict; dated model/WebSocket/OPI scope needs current verification.


- [[source-adyen-docs-point-of-sale-shopper-engagement]] — Adyen website overview (2022 last-modified; 2026-09-15 capture) for shopper-interaction examples and Display, Input, Print and Session guide routes.
