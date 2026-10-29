# Fixed retrieval checks — docs-payment-methods-paypo-web-component

## Q1 — Purpose and outcome limit

**Query:** What does the PayPo Web Component guide add, and does its redirect response prove payment completion?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paypo-web-component.md` → `raw/adyen/docs/payment-methods/paypo/web-component/2026-09-15.md`.

**Answer:** It is a PayPo add-on for existing Web Components Sessions and Advanced integrations (raw 15–35, 467–475). The Advanced sample returns RedirectShopper/action.type redirect, a next action rather than settled payment (885–899). The historical TEST guide does not prove present merchant eligibility. Canonical stem: `https://docs.adyen.com/payment-methods/paypo/web-component`.

## Q2 — Authorization clock, capture, fields and warnings

**Query:** What are PayPo's offer and repayment clocks, capture rule and Web Component prerequisites?

**Expected route:** same root → provider → concept → source → pinned raw.

**Answer:** Sessions requires Web Components Sessions, Checkout API v68+, Customer Area PayPo, and name/email; billing/delivery addresses are optional (29–48). Advanced requires Web Components Advanced, redirect handling and PayPo enabled; /payments adds type paypo with name/email required and addresses optional (469–475, 501–513). TEST examples are PL/PLN (55–74, 519–542). The pre-authorization offer link lasts up to 72 hours; when shopper accepts, status becomes Authorised and the 30-day payment term starts at authorization. Merchant capture follows authorization and is full-only; automatic capture can be configured at live setup, while manual capture uses original PSP reference (391–420, 901–931). Warn about Sessions app-scheme returnUrl versus Advanced HTTPS (66, 534), missing curl continuation before -d (59–60, 524–525), unquoted paypo in Redirect Component snippets (450, 498), and separate live Customer Area request (465, 945). Canonical stem: `https://docs.adyen.com/payment-methods/paypo/web-component`; pinned raw: `raw/adyen/docs/payment-methods/paypo/web-component/2026-09-15.md`.
