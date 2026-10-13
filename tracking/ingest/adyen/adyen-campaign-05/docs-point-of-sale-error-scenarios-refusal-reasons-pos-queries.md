# Fixed retrieval checks — Terminal API refusal reasons

## Purpose, scope, and limits

**Query:** Which fields identify a declined Terminal API payment, and which should POS logic use?

**Answer:** For a declined POS payment response, `ErrorCondition` is the error category in `PaymentResponse.Response`; `refusalReason` and `message` add explanation in `Response.AdditionalResponse`. Adyen says POS code can use `ErrorCondition` but should not code against `refusalReason` or `message`; underlying acquirer/issuer raw responses are separate and not universal rule keys (raw lines 15–39). This 2026-09-15 page capture has a 2022-01-28 `last_modified` value and a `latest` API Explorer link, so it does not pin a Terminal API version or prove current merchant eligibility or a live outcome. Route after catalog update: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-terminal-api.md` → `wiki/sources/adyen/source-adyen-docs-point-of-sale-error-scenarios-refusal-reasons-pos.md` → `raw/adyen/docs/point-of-sale/error-scenarios/refusal-reasons-pos/2026-09-15.md`.

## Condition-specific actions and missing-result boundary

**Query:** Does a decline or retry checkmark mean the POS should always resend a payment?

**Answer:** No. The tables give row-specific retry flags for Aborted, Busy, Cancel, DeviceOut, InvalidCard, NotAllowed, Refusal, UnreachableHost, and WrongPIN (raw lines 25–153). Busy is no-retry; a payment-in-progress row identifies another `serviceId` that can be used to abort that in-progress request (lines 49–55). Cancel/Approved is no-retry despite initial issuer approval, while other Cancel rows vary (lines 57–86). Refusal mixes retry-marked acquirer, balance, generic and wallet/PIN cases with no-retry blocked-card, AID-banned, suspected-fraud and restricted-card cases (lines 111–140). UnreachableHost and WrongPIN examples have retry checks (lines 142–153). These rows address a **received decline**; a missing response/uncertain outcome belongs to the separately linked response-handling/status guide, which is navigation here, not a basis to blindly retry (lines 155–158). Route after catalog update: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-terminal-api.md` → `wiki/sources/adyen/source-adyen-docs-point-of-sale-error-scenarios-refusal-reasons-pos.md` → `raw/adyen/docs/point-of-sale/error-scenarios/refusal-reasons-pos/2026-09-15.md`.
