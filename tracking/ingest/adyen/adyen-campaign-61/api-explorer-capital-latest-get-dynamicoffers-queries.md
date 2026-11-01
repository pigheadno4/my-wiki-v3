# Capital dynamic-offer retrieval checks

## Q1 — What does GET /dynamicOffers return and how is it scoped?

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-capital.md` → `[[source-adyen-api-explorer-capital-latest-get-dynamicoffers]]` ([canonical URL](https://docs.adyen.com/api-explorer/capital/latest/get/dynamicOffers)). The pinned raw says the Capital GET operation returns available dynamic offers for required `accountHolderId` (lines 5–7, 19–24). Optional `financingType` lists `businessFinancing` and omission requests all available types (line 22). Test and live bases are separate `/capital/v1` hosts (lines 9–15). This is an offer lookup, not grant acceptance or funding proof.

## Q2 — Which offer terms and validation-error details can the endpoint return?

Route: `[[source-adyen-api-explorer-capital-latest-get-dynamicoffers]]` ([canonical URL](https://docs.adyen.com/api-explorer/capital/latest/get/dynamicOffers)) → pinned raw lines 25–66. The 200 response requires a `dynamicOffers` array; each offer requires holder/offer IDs, loan-or-cash-advance contract type, `businessFinancing`, validity dates, minimum/maximum amounts in minor units and a repayment object with term object (lines 30–47). The schema does not further expand term fields. The 422 body documents optional validation-problem fields; `invalidFields` is optional, with required `message`, `name`, `value` inside each item if present (lines 50–66). Neither response establishes disbursement or repayment.
