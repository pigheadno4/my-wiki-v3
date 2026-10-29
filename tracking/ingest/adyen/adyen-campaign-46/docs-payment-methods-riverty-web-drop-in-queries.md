# Fixed retrieval checks — docs-payment-methods-riverty-web-drop-in

## Q1 — Purpose and scope

**Query:** What does Adyen's Riverty Web Drop-in page cover, and does it prove merchant eligibility or a successful payment?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-riverty-web-drop-in.md` → `raw/adyen/docs/payment-methods/riverty/web-drop-in/2026-09-15.md`.

**Answer:** It is a Riverty-specific add-on to existing Web Drop-in Sessions and Advanced integrations, not a complete base guide. The fetched 2026-09-15 snapshot cannot prove current account eligibility or successful execution. Verify at raw lines 14–25, Sessions requirements 29–39 and Advanced requirements 585–593. Canonical stem: `https://docs.adyen.com/payment-methods/riverty/web-drop-in`.

## Q2 — Central lifecycle, prerequisites and warnings

**Query:** What must a Web Drop-in merchant handle for Riverty authorization, capture, partial changes and checkout consent?

**Expected route:** same root → provider → concept → source → pinned raw.

**Answer:** Sessions requires existing Web Drop-in, Checkout API v68+, Customer Area enablement and its required shopper/address/line-item fields (raw 29–55). Advanced requires existing Advanced Drop-in and redirect handling (585–593), uses country AT/BE/DE/NL/CH and currency EUR/CHF discovery filters (627–655), and has flow-specific request fields (690–708); these do not promise each pairing or merchant availability. B2B is described as unsupported (47–48, 700–701). After shipment, Riverty needs manual capture even if other methods auto-capture; authorization expires after 30 days absent an extension (149–153, 803–809). Partial capture needs matching amount/line items, cancellation of unclaimed balance, and Support setup for multiple partial captures (155–166, 811–822). For partial refunds, use `capturePspReference` to avoid the default last-capture selection (263–267, 915–923). Checkout must present terms and data protection guidelines for shopper approval (577–579, 1231–1233). Preserve Sessions versus Advanced delivery-address difference and the first-time-shopper risk exception: if a different delivery address causes rejection, send only billingAddress and deliver there (45–55 vs 694–708, especially line 699), top-level versus nested deviceFingerprint inconsistency (603–623 vs 706/729), invoice-sender wording difference (151 vs 607), and non-copy-ready curl samples (64–65, 173, 643–644, 717–718). Example `status: received` is not evidence of final settlement/refund (213, 547, 869, 1201). Canonical stem: `https://docs.adyen.com/payment-methods/riverty/web-drop-in`; pinned raw: `raw/adyen/docs/payment-methods/riverty/web-drop-in/2026-09-15.md`.
