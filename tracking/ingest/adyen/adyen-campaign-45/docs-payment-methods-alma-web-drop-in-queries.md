# C45 Alma Web Drop-in retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-alma-web-drop-in`

Full pinned raw path: `raw/adyen/docs/payment-methods/alma/web-drop-in/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-alma-web-drop-in]]` → `[[raw/adyen/docs/payment-methods/alma/web-drop-in/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What does the Alma Web Drop-in guide add, and what does its FR/EUR example establish?

**Answer path:** Opening lines 15–23 scope the page to Alma additions for existing Web Drop-in Sessions and Advanced flows. The linked Alma overview `raw/adyen/docs/payment-methods/alma/2026-09-15.md` lines 23–29 lists France/EUR and three/four instalments. The child FR/EUR TEST examples do not prove a merchant's current method eligibility, financing approval, capture or settlement; live acceptance requires a separate live Customer Area request (lines 100–104, 202–206).

## Q2 — central capability, prerequisites and warnings

**Query:** Which fields and instalment choice does Alma Web Drop-in add, and how does redirect work?

**Answer path:** Sessions requirements lines 29–35 specify existing Web Drop-in, Checkout API v68+ and Customer Area addition. Sessions table lines 39–48 lists phone/email/billing/delivery data with blank Required cells; Advanced table lines 132–142 likewise lists these fields and makes `additionalData.alma.installments_count` optional, set to 3 or 4 or omitted for shopper choice. Optional `Redirect` import appears at lines 86–96 and 118–128. Advanced redirect prerequisites lines 110–116 and response lines 184–198 show an initial redirect action, not final payment. The Sessions Web sample has an app-style return URL at line 64; both curl examples omit continuation before `-d` (53–58, 147–152), and the Advanced base-link at line 114 contains an unresolved encoded platform template. Test/live sections 98–104 and 200–206 supply status and live-request routes, not outcome proof.
