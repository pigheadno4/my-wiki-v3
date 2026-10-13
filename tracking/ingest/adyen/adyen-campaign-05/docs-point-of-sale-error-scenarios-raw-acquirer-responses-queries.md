# Fixed retrieval checks — POS raw acquirer responses

## Purpose, scope, and limits

**Query:** What does this page explain, and what should a merchant integration avoid inferring?

**Answer:** It explains the optional issuer/scheme raw decline string for Adyen POS Terminal API payments and a table of common raw-response examples. Adyen maps variable raw strings into `ErrorCondition`, `refusalReason`, and `message`; after merchant-account Customer Area opt-in, `refusalReasonRaw` appears in `Response.AdditionalResponse` of a declined `PaymentResponse`. The page expressly warns against coding on raw strings because they can change without notice (raw lines 15–35). The 2026-09-15 capture does not prove current raw-string behavior, enablement for a merchant, payment completion, or a merchant-liability rule. Route after catalog update: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-terminal-api.md` → `wiki/sources/adyen/source-adyen-docs-point-of-sale-error-scenarios-raw-acquirer-responses.md` → `raw/adyen/docs/point-of-sale/error-scenarios/raw-acquirer-responses/2026-09-15.md`.

## Central lookup and warning

**Query:** Can one raw code determine payment status or a universal retry action?

**Answer:** No. The table combines Customer Area status, complete raw text, context, and a row-specific instruction. For example, `00: Approved or completed successfully` appears with **Cancelled** after initial issuer approval; `85` appears with **Authorised** for zero-value verification; `91` has both Refused and Error variants (raw lines 39–43, 88–95). The duplicate-transmission `94` row says to check the condition before processing again if needed, whereas `Offline - Y1 / Y3 / Z1 / Z3` directs checking transaction logs (raw lines 98, 175). Bancontact/BCMC and eftpos rows, a missing-store-ID case, and country-restriction examples have their own contexts (raw lines 81, 115–118, 143, 152, 163). Do not infer a scheme-wide, region-wide, or blanket retry rule. The refusal-reasons and response-handling links are navigation until read (raw lines 200–203). Route after catalog update: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-terminal-api.md` → `wiki/sources/adyen/source-adyen-docs-point-of-sale-error-scenarios-raw-acquirer-responses.md` → `raw/adyen/docs/point-of-sale/error-scenarios/raw-acquirer-responses/2026-09-15.md`.
