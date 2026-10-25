# FPX Online Banking Malaysia Flutter Drop-in retrieval checks

## Q1 — Purpose, scope and inference limit

The canonical source [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-flutter-drop-in]] is a 2026-09-15-captured FPX-specific add-on to an existing Flutter Drop-in integration, with separate Sessions and Advanced sections (raw lines 15–25, 58–62). It does not establish present merchant eligibility, a completed redirect, an authorized payment or settlement; the live-request step remains separate from setup and test guidance (raw lines 50–56, 82–88).

Full retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-flutter-drop-in]] → [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/flutter-drop-in/2026-09-15]].

## Q2 — Capability, prerequisites and warnings

Sessions names Flutter Drop-in, Checkout API v68+, redirect handling, and contacting Support to add FPX in Customer Area; it says no extra `/sessions` fields or configuration (raw lines 29–48). The Sessions integration row links to an Advanced-flow target despite its label; other Sessions links point to Sessions flow (raw lines 33–35, 42). Advanced names Flutter Drop-in and redirect handling, directs Customer Area addition, and says no extra configuration or `/payments` fields; this section gives no API version floor (raw lines 62–80). Both test sections refer to available issuer IDs for a “Component” despite the Drop-in title, and require a separate live Customer Area request before live acceptance (raw lines 50–56, 82–88). These steps and wording do not prove successful payment processing.

Full retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-flutter-drop-in]] → [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/flutter-drop-in/2026-09-15]].
