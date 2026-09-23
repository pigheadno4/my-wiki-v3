# Braintree C15 Query Audit — Group B

- Scope: Authorization Responses + Merchant Advice Codes
- Started: `2026-09-23T11:33:35Z`
- Analysis ended: `2026-09-23T11:34:14Z`
- Handoff: `2026-09-23T11:34:22Z`
- Evidence: both selected raw pages read completely

## Authorization Responses

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-authorization-responses]]` → `[[raw/braintree/docs/reference/general/processor-responses/authorization-responses-2026-09-16]]`.

1. **Query:** Where is Braintree Authorization Responses documented?
   - **Object/action match:** Braintree processor authorization response classes and their handling; locate the reference.
   - **Direct answer:** The retrieval entry is `[[source-braintree-authorization-responses]]`; its factual evidence is the complete raw Authorization Response Codes page at the route above.
   - **Exact raw locator:** `# Authorization`, line 14; `## Approvals`, line 21; `## Declines`, line 35.
   - **Verdict:** PASS. The concept route is live. The direct provider-index source catalog entry is pending the campaign's approved aggregate close, not a source defect.

2. **Query:** How are approvals, decline categories and retry restrictions distinguished, including the stated merchant-fee qualification?
   - **Object/action match:** Processor authorization outcome classification and retry handling; distinguish—not collapse—approval, gateway acceptance, decline type, network failure, and recurring restrictions.
   - **Direct answer:** A 1000-class code means processor authorization and `success=true`, but processing settings can still gateway-reject it. A 2000-class code is a processor decline with `success=false`; a 3000-class code signals a back-end processing-network problem. Hard declines are non-temporary and the same payment method is unlikely to succeed; soft declines are temporary and may succeed later, but this does not grant unrestricted retries. Mastercard prohibits retries for codes 2009, 2012, 2019, 2022, 2047 and 2053. For transactions originally carrying a recurring ECI flag, soft declines are capped at 15 retries in 30 days; 2004 and 2015 must not be retried, and 2005 must not be retried with the same payment information. Authorization and capture can incur merchant fees only in some markets; the page points to the Braintree User Agreement. Processor authorization is not itself capture or final settlement.
   - **Exact raw locator:** fee qualification lines 17–18; processor approval versus possible gateway rejection line 23; 2000/3000 classes line 37; hard/soft definitions lines 40–44; general later-retry handling lines 50–52; Mastercard prohibited-retry codes lines 54–63; recurring-ECI limits lines 64–74.
   - **Verdict:** PASS.

## Merchant Advice Codes

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-merchant-advice-codes]]` → `[[raw/braintree/docs/reference/general/merchant-responses/merchant-advice-codes-2026-09-16]]`.

3. **Query:** Where is Braintree Merchant Advice Codes documented?
   - **Object/action match:** Mastercard Merchant Advice Codes returned with Braintree transaction responses; locate the reference.
   - **Direct answer:** The retrieval entry is `[[source-braintree-merchant-advice-codes]]`; its factual evidence is the complete Merchant Advice Codes raw page at the route above.
   - **Exact raw locator:** `# Merchant Advice Codes`, lines 14–20; code table, lines 22–38.
   - **Verdict:** PASS. The concept route is live. The direct provider-index source catalog entry is pending the campaign's approved aggregate close, not a source defect.

4. **Query:** What do optional Mastercard advice codes communicate about declines and possible retries, without overriding other retry restrictions?
   - **Object/action match:** Optional Mastercard decline advice and possible retry timing; interpret it without replacing processor-response or recurring-ECI rules.
   - **Direct answer:** When present, a Mastercard MAC can explain why a payment failed, whether it may be retried and sometimes how long to wait. The response fields are rendered in the collected prose as `merchant_advice_code` and `merchant_advice_code_text`. Code 03 says do not try again; 21 says stop recurring payment; 02 says try again later but gives no duration. Codes 24–30 prescribe waits of 1 hour, 24 hours, 2 days, 4 days, 6 days, 8 days and 10 days respectively. The MAC page does not say these instructions override separate authorization-response restrictions, so recurring-ECI and code-specific no-retry rules still need the Authorization Responses authority above.
   - **Exact raw locator:** MAC purpose and optional presence line 16; response-field rendering line 18; codes 02, 03 and 21 lines 25–28; timed codes 24–30 lines 29–35; separate authorization retry restrictions at Authorization Responses lines 54–74.
   - **Verdict:** PASS.

## Bounded gap sweep and completeness

- Searched Braintree raw and current wiki routes for authorization responses, decline retries, recurring ECI, Merchant Advice Codes and MAC. Adjacent recurring-billing, Control Panel decline, network-update and orchestration pages exist, but the four fixed questions are fully answered by the two selected complete raws; none was needed as additional factual evidence.
- Both source pages have path-qualified raw backlinks, and `[[braintree-server-sdk]]` has one reciprocal route to each. `[[recurring-payments]]` also routes to Authorization Responses for the recurring-ECI boundary.
- No wrong-object route, missing material qualification, contradictory answer, broken source/raw route or retrieval-source defect was found. Group B result: **4/4 PASS**. The only pending navigation work is the already planned campaign-close addition of the two direct source entries to `[[braintree-index]]`.
