# C44 worker query check: Scalapay Web Component

## Q1 — purpose, scope, non-inference

**Query:** What is this Scalapay page and what does it prove?

**Answer:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-scalapay-web-component]] routes to the 2026-09-15 captured Web Components Sessions/Advanced add-on. It is not live method approval or a payment result. Product limits route to [[source-adyen-docs-payment-methods-scalapay]]. Pinned full raw: `raw/adyen/docs/payment-methods/scalapay/web-component/2026-09-15.md`; verified locators raw 15–39 and 462–468.

## Q2 — central capability, prerequisites, warnings

**Query:** How do merchants add Scalapay and which conditions remain?

**Answer:** Existing Components integration and Customer Area setup precede `scalapay_3x` redirect mounting. Request tables mark IT/FR/PT/ES country and shopper first/last name; /payments can send either optional flight date or lodging check-in date. v6 uses Redirect constructor, v5 and earlier use checkout.create; the v6 snippet omits import and base links retain an encoded platform template. Activation defaults standard pricing and account-manager consultation is stated for Enterprise eligibility. The related overview matrix gives EUR and no recurring (overview raw 19–23), despite this child's tokenization See also link. Live acceptance needs a separate request; no capture/refund flow is shown in this child. Verified raw locators 21–71, 430–475.
