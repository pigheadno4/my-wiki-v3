# Retrieval probes — Adyen IRIS API-only (captured 2026-09-15)

## Q1 — Scope and limits

**Question:** What does the captured Adyen IRIS API-only guide cover, and what does it not prove about a merchant's current account or live payment?

**Expected route:** [[wiki/index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-iris-api-only]] → [[raw/adyen/docs/payment-methods/iris/api-only/2026-09-15]].

**Expected answer:** The guide is for adding IRIS to an existing API-only online payments integration in Greece and EUR. It documents issuer redirect and QR-code branches, action handling, issuer discovery, result/webhook handling, testing, and Greek-bank plus Adyen onboarding. It is captured documentation, not evidence that a particular merchant is eligible, enabled on live, has processed a payment, or received funds. The related IRIS overview says Adyen acts as gateway and refunds/cancellations are handled through the Greek bank; this child guide supplies no Adyen operation for them.

**Evidence:** `raw/adyen/docs/payment-methods/iris/api-only/2026-09-15.md` lines 15–42, 63–70, 1340–1372; related `raw/adyen/docs/payment-methods/iris/2026-09-15.md` lines 23–41.

## Q2 — Flow choice, prerequisites, and outcome

**Question:** In Adyen's captured IRIS API-only guide, what selects issuer redirect versus QR, which setup and result steps matter, and what example mismatch could mislead an implementer?

**Expected route:** [[wiki/index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-iris-api-only]] → [[raw/adyen/docs/payment-methods/iris/api-only/2026-09-15]].

**Expected answer:** Both flows require an existing API-only integration that handles redirect and qrCode actions, IRIS addition in Customer Area, and Greek-bank/Adyen onboarding with DIAS code, merchant account, and stores before live. A selected issuer ID plus returnUrl chooses issuer redirect; omission of issuer yields QR data, and returnUrl is not required for QR. For redirect, use the returned URL and submit the returned redirectResult to /payments/details; QR renders qrCodeData and has a 10-minute completion window. QR is intended for desktop and requires a webhook for final outcome; redirect needs a webhook if the shopper does not return. Pending/Received is not final, and Authorised means sent to bank processing rather than guaranteed settlement. Several issuer-redirect code examples omit issuer although the field table says omission selects QR, so do not treat those examples as proof of redirect behavior.

**Evidence:** `raw/adyen/docs/payment-methods/iris/api-only/2026-09-15.md` lines 25–40, 380–388, 439–447, 478–488, 522–534, 597–607, 695–705, 712–740, 1312–1361, 1372.
