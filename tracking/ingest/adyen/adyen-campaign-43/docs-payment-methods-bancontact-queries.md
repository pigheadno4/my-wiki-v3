# Fixed retrieval checks — Bancontact overview

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-bancontact.md`.

## Q1. What is this source's purpose and scope, and what cannot be inferred?

This is Adyen's Bancontact **method overview and card/mobile chooser**, captured 2026-09-15 though its page metadata says last modified 2019-12-17 (primary raw `raw/adyen/docs/payment-methods/bancontact/2026-09-15.md:5-15,23-49`; canonical source stem `source-adyen-docs-payment-methods-bancontact`). It distinguishes Bancontact card, Bancontact mobile and a separate in-person route. Its BE/EUR and capability table is a historical method-level snapshot, not proof of current merchant/account/app eligibility, enabled WIP, payment success or settlement (`:30-35`). This overview does not provide exact channel request schema, app/QR payload or return handling; use the linked children (`:37-49`).

## Q2. What are the central capabilities, prerequisites and warnings?

Bancontact **card** is described as card-like with no security code, mandatory 3D Secure and automatic capture; the table calls it Debit Card/Redirect in BE/EUR (`:25-27,30-32`). Bancontact **mobile** hands off to Payconiq by Bancontact or an integrated banking app, directly on mobile or via desktop QR; its table calls it Wallet/Redirect or Additional action in BE/EUR (`:28,30-33`). Both rows mark refunds and partial refunds available while separate/partial captures and chargebacks are unavailable in this snapshot (`:30-33`). The recurring checkmarks are footnoted to **Bancontact Wallet Initiated Program (WIP)**; do not infer ordinary recurring support without that qualification (`:30-35`). The card, mobile and in-person children are distinct (`:37-49`).
