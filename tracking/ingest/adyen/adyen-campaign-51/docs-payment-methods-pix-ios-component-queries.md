# Fixed retrieval checks — docs-payment-methods-pix-ios-component

## Q1 — Identify Pix iOS Component flow and request scope

- Query: What does the captured Pix iOS Component guide add to Sessions and Advanced flows, including the SDK/API minimum and QR action?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-pix-ios-component.md` → `raw/adyen/docs/payment-methods/pix/ios-component/2026-09-15.md`.
- Expected: Existing iOS Components Sessions integration, Checkout API v68+, Customer Area Pix setup; `/sessions` Pix table marks `amount` required and optional shopper/statement/items fields (raw lines 25–50). No additional Pix configuration; Swift initializes `InstantPaymentComponent` and delegates to the session (507–533). Advanced requires existing iOS Components integration, `action.type: qrCode` handling and Pix setup (554–564), initializes the same class with a different delegate (572–590), and its `/payments` table marks `paymentMethod` and `amount` required (593–610). The example response contains `resultCode: Pending` plus a `qrCode` action (1098–1118), not final paid status.
- Scope: The Advanced prerequisite labels Components but links a Drop-in base guide (raw line 562); its `state.data.paymentMethod`/`onSubmit` wording is unreconciled with the iOS Swift example (580–610). The source is an add-on, not the full base request, live eligibility or observed payment execution.

## Q2 — Recover versioned validity, statement limits and asynchronous test/live boundary

- Query: What differs between Sessions and Advanced Pix statement fields, what changes at Checkout API v72, and how is pending Pix tested?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-pix-ios-component.md` → pinned raw.
- Expected: Sessions table gives `shopperStatement` a 140-character maximum (raw line 48); Advanced says keep a supplied value under 60 characters and describes a default text (605). Advanced `sessionValidity` defaults to 1 hour through Checkout API v71 or 24 hours from v72 (606); this is distinct from the Sessions v68+ minimum (34). Pix is asynchronous; in test Customer Area **Payments > Offers**, select a pending offer's PSP reference and promote it to a sale, then see paid/promoted records in **Payments > Payment list** and test reconciliation (539–550, 1124–1135). Live acceptance requires a Pix request in live Customer Area (552, 1137). The page states refunds within 90 days by Customer Area or API (535–537, 1120–1122).
- Scope: This 2026-09-15 capture's sample sessionValidity timestamps are historical (71, 286, 388, 640 and repeats); examples and test promotion do not prove a live completed payment, eligibility or refund.
