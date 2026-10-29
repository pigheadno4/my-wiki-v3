# Pay by Bank (Europe) Web router retrieval checks

## Q1 — What does this captured Web page directly provide?
Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-pay-by-bank-europe-web.md` → `raw/adyen/docs/payment-methods/pay-by-bank-europe/web/2026-09-15.md`.
Expected answer: a short Web integration router, captured 2026-09-15 with metadata last modified 2022-11-21, linking Pay by Bank (Europe) Drop-in and Components method pages. The link text calls them an all-in-one UI solution and a prebuilt Component respectively. Raw locators: lines 1–13 and 15–27. No child implementation fact follows from the link descriptions.

## Q2 — What further routes and limits should an answer retain?
Expected route: same root/provider/concept/source/raw chain.
Expected answer: the page also links general Web Drop-in and Components integration guides at line 29. It does not specify server-side flow, request fields, version requirements, redirect handling, onboarding, geography, settlement or live-payment outcome. Route method-level claims to approved `wiki/sources/adyen/source-adyen-docs-payment-methods-pay-by-bank-europe.md`, which separately preserves the captured Finland list conflict and authorization-versus-funds warning. Route implementation claims to fully read child guides. Raw locators: lines 19–29.
