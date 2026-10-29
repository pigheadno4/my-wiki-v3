# PayBright API-only retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-paybright-api-only`
**Full pinned raw:** `raw/adyen/docs/payment-methods/paybright/api-only/2026-09-15.md`
**Verified locators:** `# PayBright for API only`, lines 15–27; `## Requirements`, lines 29–34; `## Build your payment form for PayBright`, lines 36–53; `## Test and go live`, lines 1011–1017.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paybright-api-only.md` → pinned raw.
**Answer boundary:** Existing Web API-only integration, CA/CAD and test Customer Area setup. The page says no new PayBright integrations are accepted despite a later live-request instruction; it does not establish present merchant eligibility or actual payment execution.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** Merchant form/risk fields lines 36–53; `/payments` fields and TEST v68 example lines 55–141; redirect/return lines 828–883; result and webhook paths lines 885–902; capture and partial-capture rules lines 904–963; refund/cancel lines 965–1009.
**Answer boundary:** Collect shopper and item data, send server `/payments`, follow returned redirect action, then send `redirectResult` to `/payments/details` or use AUTHORISATION webhook if no return. Outcome is distinct from capture. Capture is automatic by default. For post-shipment timing the page suggests capture delay or manual capture; it also mentions those for partial capture, but separately states that partial capture is unavailable when Customer Area automatic capture is enabled (raw lines 908, 914). A delay alone does not establish partial-capture eligibility; the page does not reconcile the statements. When eligible, a partial capture has a Support and unclaimed-balance gate. Cancel before capture, refund afterward. Partial-refund prose and example use different endpoint shapes; the partial-capture sample amount does not reconcile with its invoice lines. Do not infer current onboarding from the live-request line.
