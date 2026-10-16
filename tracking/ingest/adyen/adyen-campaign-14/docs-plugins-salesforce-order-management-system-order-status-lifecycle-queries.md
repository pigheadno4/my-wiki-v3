# Fixed queries — SFCC/OMS order-status lifecycle

## Q1 — purpose, scope, and what must not be inferred

**Query:** What does this page say about SFCC–OMS order statuses, and can its retained text establish a particular transition or financial result?

**Answer:** The page points to an SVG diagram for learning statuses and testing/troubleshooting synchronization, but the pinned Markdown does not transcribe the status labels or transitions. Its text defines payment-flow types only. No particular order status, webhook transition, successful authorization/capture, refund, reversal, settlement or bank receipt can be inferred from the retained text alone. Raw: `raw/adyen/docs/plugins/salesforce-order-management-system/order-status-lifecycle/2026-09-15.md:17-30`. Canonical route: `[[source-adyen-docs-plugins-salesforce-order-management-system-order-status-lifecycle]]` → `[[adyen-salesforce-order-management-system]]`.

## Q2 — central capability, prerequisites, and warnings

**Query:** How do SALE and AUTH differ, and which methods can choose a flow?

**Answer:** SALE captures directly after authorization; AUTH separates authorization and capture into two steps. The page says alternative methods such as local methods may use either and can be configured in Adyen Customer Area, while cards use AUTH by default. It does not give method-specific eligibility, current merchant settings, configuration roles or execution proof. The diagram is needed for detailed SFCC/OMS status mapping, and it must be read separately. Raw: `raw/adyen/docs/plugins/salesforce-order-management-system/order-status-lifecycle/2026-09-15.md:19-28`. Canonical route: `[[source-adyen-docs-plugins-salesforce-order-management-system-order-status-lifecycle]]` → `[[adyen-salesforce-order-management-system]]`.
