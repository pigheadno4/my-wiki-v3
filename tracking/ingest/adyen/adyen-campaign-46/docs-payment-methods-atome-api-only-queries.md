# Fixed retrieval checks — docs-payment-methods-atome-api-only

## Q1 — Purpose and scope

**Query:** What does Adyen's Atome API-only page cover, and does the example prove payment success or current availability?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-atome-api-only.md` → `raw/adyen/docs/payment-methods/atome/api-only/2026-09-15.md`.

**Answer:** It is an Atome add-on to an existing Web API-only Advanced-flow integration with merchant-built payment form and redirect handling (raw 15–38). The sample discovery and RedirectShopper responses do not prove live account availability, completed authorization or settlement (344–355, 1087–1101). Canonical stem: `https://docs.adyen.com/payment-methods/atome/api-only`.

## Q2 — Discovery, payment fields, redirect and test/live

**Query:** Which Atome API-only inputs, country pairs and test/live steps matter?

**Expected route:** same root → provider → concept → source → pinned raw.

**Answer:** Existing API-only integration must handle redirect actions and Atome must be enabled in Customer Area (23–29). The merchant-built form collects name, email, phone and billing/delivery details for risk checks (38–55). Discovery uses MY/MYR or SG/SGD (42–48, 59–66); /payments marks type atome, name, email, phone, billing address, lineItems and countryCode required, with deliveryAddress optional when same as billing (357–370). The TEST SG/SGD /payments response requires redirect handling (377–435, 1087–1101). Partial refund specifies amount (1103–1109). Sandbox testing needs a country-specific test shopper account, and live acceptance needs Support to enable Atome in live Customer Area (1111–1129). Warn that both curl examples omit continuation before -d (77–78, 381–382), the discovery shopperLocale sg-SG is only an example (85), and the separate overview carries portable-electronics and automatic-capture qualifications absent here. Canonical stem: `https://docs.adyen.com/payment-methods/atome/api-only`; pinned raw: `raw/adyen/docs/payment-methods/atome/api-only/2026-09-15.md`.
