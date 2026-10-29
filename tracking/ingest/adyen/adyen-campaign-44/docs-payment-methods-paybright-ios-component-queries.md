# PayBright iOS Component retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-paybright-ios-component`
**Full pinned raw:** `raw/adyen/docs/payment-methods/paybright/ios-component/2026-09-15.md`
**Verified locators:** `# PayBright Redirect Component`, lines 15–21; `## Requirements`, lines 23–39; `## Component configuration`, lines 1312–1367; `## Test and go live`, lines 1476–1482.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paybright-ios-component.md` → pinned raw.
**Answer boundary:** This is an iOS Components add-on for existing integrations. The page says Adyen accepts no new PayBright integrations, despite its later live-request instruction. It does not establish current eligibility or successful payment execution.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** `/sessions` and `/payments` tables lines 45–60, 789–804; code examples lines 62–1310; component versions lines 1312–1367; capture/partial rules lines 1369–1428; cancel/refund lines 1430–1474.
**Answer boundary:** Existing Sessions/Advanced iOS Components and Customer Area addition are prerequisites; v5+ uses `InstantPaymentComponent`, v4 uses `PayBrightComponent`. Capture is automatic by default. For post-shipment timing the page suggests capture delay or manual capture; it also mentions those for partial capture, but separately states that partial capture is unavailable when Customer Area automatic capture is enabled (raw lines 1373, 1379). A delay alone does not establish partial-capture eligibility; the page does not reconcile the statements. When eligible, a partial capture cancels the remainder unless multiple partial captures are enabled through Support. Cancel before capture, refund afterward. Request examples contain blanks for required fields/currency, and Advanced Java/PHP use USD for CA where the overview lists CAD. The partial refund prose/example use different endpoint shapes. Do not copy these examples as validated requests.
