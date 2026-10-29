# Fixed retrieval queries — Online Banking India

## Q1 — Purpose, scope, and evidence boundary

**Query:** What is Adyen's Online Banking India overview, where does it apply, and what should this captured page not be taken to prove?

**Expected:** The 2026-09-15-captured page at `https://docs.adyen.com/payment-methods/online-banking-india` describes an online-banking redirect method with a captured table for IN/INR. It is a method overview and route chooser, not proof of current merchant eligibility, live enablement, completed payment, or a full implementation recipe. The page explicitly requires compliance with India regulations, a local entity, and a local integration in India (raw line 25). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-india.md` → `raw/adyen/docs/payment-methods/online-banking-india/2026-09-15.md`. Evidence: raw lines 15–17, 25, 29–31.

## Q2 — Flow, capability boundaries, and integration routes

**Query:** How does Online Banking India send a shopper to pay, what feature boundaries does the captured table show, and where are the implementation choices?

**Expected:** The shopper selects an issuing bank from a list, then is redirected to that bank's website or mobile app to complete payment (raw line 27). The captured matrix marks refunds, partial refunds, and multiple partial refunds available, while recurring, separate captures, partial captures, multiple partial captures, and chargebacks are marked unavailable (raw lines 29–31). The overview routes to Web prebuilt UI, API-only custom UI for website/iOS/Android, and Pay by Link (raw lines 33–51); read the chosen child guide for implementation detail. The India compliance/local-presence prerequisite at raw line 25 remains in scope. Route: root index → provider index → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-india.md` → pinned raw above.
