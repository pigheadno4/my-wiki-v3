# Oney Web Component retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-oney-web-component`
**Full pinned raw:** `raw/adyen/docs/payment-methods/oney/web-component/2026-09-15.md`
**Verified locators:** `# Oney Component`, lines 15–25; `## Requirements`, lines 27–43; `## Component configuration`, lines 1255–1323; `## Capture the payment`, lines 1325–1331.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-oney-web-component.md` → pinned raw.
**Answer boundary:** This is a Web Components add-on guide, fetched 2026-09-15 but marked modified 2020-07-10. The TEST examples do not establish account enablement, a completed authorization, capture or shipment permission.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** prerequisites lines 27–43; `/sessions` fields lines 49–70 and TEST example 72–130; `/payments` field table lines 763–785 and v72 TEST example starting line 786; Component types and visibility lines 1255–1323; capture/refund lines 1325–1345; test/live lines 1347–1425.
**Answer boundary:** Add Oney to an existing Sessions/Advanced Web Components integration, include required shopper details and line items whose total matches the payment amount, and create a Component for each offered installment type. Hidden form fields still require request data. Ship only after successful capture; authorization expires if capture occurs after more than six days. Cancel before capture and refund after capture within the stated EUR 1 minimum and 13-month window. Both endpoint tables require a French mobile prefix `+336` or `+337` followed by eight digits (raw lines 59–60, 773–774), while TEST curl examples use `+33 1 76 35 07 90` (lines 87, 804); that sample is not validated Oney input. The Advanced C# sample uses `CountryCode = "EUR"` despite FR/ES country table values, and the test minimum table lists Italy despite the Component type table listing FR/ES; these sample/table differences remain unresolved in the capture.
