# Adyen Issuing get-started retrieval checks

## Q1 — What is the page for, and what precedes live setup?

**Answer:** It outlines a contact-led card-program journey: discuss fit; design account structure, card type, authorisation, and funding; receive test credentials; create API credentials and Customer Area users; build and test the Issuing integration; contact Adyen about live; then configure the separate live account. The account structure affects onboarding, verification, and funds flow. This is setup guidance, not proof that an account is open or live transactions have occurred.

**Evidence:** `raw/adyen/docs/issuing/get-started/2026-09-15.md:17-47,49-86`, especially lines 27, 36, 51, 78-86. **Forward route:** `[[index]]` → `[[adyen-index]]` → `[[adyen-issuing]]` → `[[source-adyen-docs-issuing-get-started]]` → `[[raw/adyen/docs/issuing/get-started/2026-09-15]]`.

## Q2 — Does a test account's setup carry into live, and does this page prove live operation?

**Answer:** No. The page explicitly says test setup and configuration are not replicated to live and directs the integrator to repeat setup there. It says to contact Adyen to take the account live after building and testing, and to follow the go-live checklist. Receipt of test credentials, Customer Area access, or a completed test integration does not itself establish live account activation, successful funding, card issuance, or payment execution.

**Evidence:** `raw/adyen/docs/issuing/get-started/2026-09-15.md:49-66,72-86`, especially lines 78-86. **Forward route:** `[[index]]` → `[[adyen-index]]` → `[[adyen-issuing]]` → `[[source-adyen-docs-issuing-get-started]]` → `[[raw/adyen/docs/issuing/get-started/2026-09-15]]`.
