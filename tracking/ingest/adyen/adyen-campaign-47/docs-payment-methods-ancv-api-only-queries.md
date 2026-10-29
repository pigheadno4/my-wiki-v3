# ANCV API-only worker retrieval queries

## Q1 — Purpose and integration scope

**Query:** What does the ANCV API-only guide add to an existing integration, and how is ANCV discovered?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ancv-api-only.md` → `raw/adyen/docs/payment-methods/ancv/api-only/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/ancv/api-only`; full pinned raw `raw/adyen/docs/payment-methods/ancv/api-only/2026-09-15.md`, `# ANCV for API only` lines 15–21, `## Requirements` lines 23–29, `## Build your payment form` lines 38–49, and `## Get ANCV as an available payment method` lines 51–58. This is a Web Advanced-flow API-only add-on using FR/EUR discovery, not evidence of merchant enablement or successful payment.

## Q2 — Await, partial authorization and example warnings

**Query:** Which ANCV ID is required, how does await/Pending become a payment outcome, and where does continuation orderData and correct authorized amount come from?

**Expected route:** Same root → Adyen index → online-payments concept → ANCV API-only source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: `## Add additional parameters to your /payments request` lines 349–356, response fields lines 728–756, `## Show the waiting screen` lines 758–761, `## Get outcome` lines 763–839, partial authorized amount warning line 871, and `## Test and go live` lines 905–909. The beneficiary ID is email or 11 digits. Pass `action.paymentData` to details, ignore `/payments` orderData and use details orderData for partial-payment continuation. Details and webhook provide correct `authorisedAmountValue` even if Customer Area shows requested amount. `Pending` is not final authorization. The curl examples omit continuation after `-X POST` (lines 62–70, 363–368); the details curl is fenced as JSON and lacks a closing quote (lines 767–778), while partial details and webhook examples omit commas (lines 799–800, 893–894).
