# Fixed retrieval checks — Online Banking India API-only

## Q1 — Purpose, scope and limits

**Query:** What does the captured Online Banking India API-only guide cover, and what can it not establish about a merchant or payment?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-india-api-only.md` → `raw/adyen/docs/payment-methods/online-banking-india/api-only/2026-09-15.md`.

**Expected answer:** The guide at canonical stem `https://docs.adyen.com/payment-methods/online-banking-india/api-only` adds the method to an existing API-only integration with issuer discovery, required payment additions, and redirect action handling (full pinned raw, lines 15–29, 31–62, 486–500). It is not a complete base integration, current merchant eligibility, live account enablement, final authorization, or settlement proof. The related method overview at `raw/adyen/docs/payment-methods/online-banking-india/2026-09-15.md` lines 25–31 states India compliance, local entity and local integration prerequisites and its IN/INR redirect scope.

## Q2 — Issuer selection, fields, redirect and warning

**Query:** How does this page discover issuers, construct an Online Banking India payment, and handle the redirect; what type-name mismatch must remain visible?

**Expected route:** Same root → Adyen index → online-payments concept → API-only source → full pinned raw `raw/adyen/docs/payment-methods/online-banking-india/api-only/2026-09-15.md`.

**Expected answer:** For /paymentMethods, set countryCode IN, amount.currency INR and channel Web, iOS or Android (raw 31–39). Show issuers from the returned method and pass the shopper-selected issuer to the server; dynamic list construction and top-ten-plus-more presentation are recommendations because issuers change (41–53). The /payments additions table marks issuer and browserInfo required; the sample uses onlinebanking_IN, issuer CBI, INR and a test endpoint (55–95). Handle action.type redirect via the base API-only flow; the child page does not itself show a final result (486–500). The discovery prose calls the response type **onlineBanking_IN** while all /payments examples use **onlinebanking_IN** (47 versus 80 and later). Preserve the capitalization mismatch and verify the API contract before implementing. Live acceptance requires a live Customer Area request (496). Canonical stem: `https://docs.adyen.com/payment-methods/online-banking-india/api-only`.
