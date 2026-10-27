# Fixed retrieval checks — ACH Android Drop-in

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ach-direct-debit-android-drop-in.md`.

## Q1. What is this source's purpose and scope, and what cannot be inferred?

This 2026-09-15 page gives **ACH-specific additions** to existing Android Drop-in Sessions and Advanced flows (primary raw `raw/adyen/docs/payment-methods/ach-direct-debit/android-drop-in/2026-09-15.md:15-25,102-112`; canonical source stem `source-adyen-docs-payment-methods-ach-direct-debit-android-drop-in`). It is not a complete Drop-in build guide, merchant eligibility decision, proof of Nacha-compliant mandate or bank validation, or final payment evidence. Adyen says bank authorization can take up to five business days after it receives a request, with successful bank authorization appearing in Settlement details report and failure producing `CHARGEBACK` (`:78-80,153-155`). Approved ACH overview `source-adyen-docs-payment-methods-ach-direct-debit` and giact source cover distinct mandate/SEC/account-validation obligations.

## Q2. What are the central capability, prerequisites and warnings?

Sessions requires existing Android Drop-in Sessions, Checkout API **v68+**, ACH addition in Customer Area and notice-of-change webhook; **Merchant allow bank-refund** roles apply to API and Customer Area refunds specifically (`:29-37`). No ACH-specific extra `/sessions` parameters are stated (`:39-43`). Advanced requires an existing Android Drop-in Advanced flow, ACH addition and webhook; it gives no API-version minimum of its own and says no ACH-specific extra `/payments` parameters (`:102-112,143-147`). Optional UI parameters control visible submit button (default true), full-address form and future-details checkbox (default true); US/PR are an address-config example, not proof of account eligibility (`:45-72,114-141`). The TEST formatted account/routing examples and `chargeback:R01` owner-name trigger simulate returns only (`:82-100,157-173`). The bank outcome is delayed, so request receipt or UI completion cannot be read as settled funds (`:80,155`).
