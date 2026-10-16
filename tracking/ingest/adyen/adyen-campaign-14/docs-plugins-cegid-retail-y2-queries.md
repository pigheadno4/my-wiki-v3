# Fixed retrieval checks — Adyen Cegid Retail Y2 overview

## Q1 — What is this page for, what is its scope, and what should not be inferred?

The captured page is the landing overview for Adyen's Cegid Retail Y2 CPOS plugin, an in-person POS-to-Adyen-terminal integration using Terminal API (raw/adyen/docs/plugins/cegid-retail-y2/2026-09-15.md:15–22). It lists host version and features and routes to setup, but does not establish the exact plugin build, merchant/terminal enablement, a completed payment or bank settlement. Proposed canonical route after coordinator promotes the new Cegid concept: `[[index]]` → `[[adyen-index]]` → `[[adyen-cegid-retail-y2]]` → `[[source-adyen-docs-plugins-cegid-retail-y2]]` → `[[raw/adyen/docs/plugins/cegid-retail-y2/2026-09-15]]`; canonical URL: https://docs.adyen.com/plugins/cegid-retail-y2.

## Q2 — Which capabilities and prerequisites are central, and what qualifications apply?

The overview names gift cards, DCC, QR wallets, partial authorizations, manual entry, tax-free shopping, delayed capture, card-only Giving donations, MOTO, Brazil/Japan/Mexico installments and mobile Pay by Link/Tap to Pay routes (raw lines 24–38). It states Retail Y2 v11.05+, recommends local POS-to-terminal communication, and permits cloud communication after Support contact; broad terminal/method links need exact eligibility checks (lines 40–57). Start with Adyen onboarding and a test account, set up plugin in Customer Area and Cegid back office, then follow gift-card/optional mobile and test/go-live guides while live credentials are pending (lines 69–89). A feature list or test setup is not proof of authorization, capture or settlement. Use the proposed concept→source→raw route and `[[adyen-terminal-api]]` only for underlying API context.
