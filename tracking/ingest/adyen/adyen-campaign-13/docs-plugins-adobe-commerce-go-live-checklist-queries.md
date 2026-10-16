# Fixed retrieval checks — docs-plugins-adobe-commerce-go-live-checklist

## Q1 — Purpose, scope, and what not to infer

**Query:** What is this Adobe Commerce go-live checklist for, and what does it not prove?

**Answer:** It is a pre-live configuration and end-to-end test checklist for an Adyen Adobe Commerce plugin integration. Test setup does not carry into live; the page enumerates live account, finance, risk/compliance, API communication, webhooks, and real-payment tests. It does not prove merchant activation, PCI/accessibility compliance, payment or capture success, settlement, or token migration. Its metadata is last modified 2023-05-03 and the raw snapshot was captured 2026-09-15; use [[adyen-magento2]] for separately version-qualified repository facts. Evidence: raw lines 11, 15–27, 90–102, 141–165. Canonical route: [[adyen-index]] → [[adyen-magento2]] → ## Related → [[source-adyen-docs-plugins-adobe-commerce-go-live-checklist]] → [[raw/adyen/docs/plugins/adobe-commerce/go-live-checklist/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** What must be prepared and tested before live Adobe Commerce payments according to this page, and which conditions matter?

**Answer:** Configure live Customer Area/account users and payment methods, finance/reconciliation and risk settings; generate live API and client keys, grant the four named API permissions and set live endpoints in Adobe Commerce. Configure live webhook credentials/HMAC, required event types including non-default OFFER_CLOSED, acceptance and the plugin cronjob; the example HTTP 200 response is an endpoint test, not proof of order processing. Review the page's dated SAQ A/default card component, CSP/v9.17.0+, custom/headless and accessibility responsibilities. Test with real payment details; these incur fees. The scenario list includes method-by-method success, refusal/fraud and 3DS cases, while manual capture, pre-capture cancel and multiple partial captures are conditional on those capture settings. The page provides no token-migration process and a completed checklist statement is not independent outcome evidence. Evidence: raw lines 31–50, 52–102, 104–139, 141–161. Canonical route: [[adyen-index]] → [[adyen-magento2]] → ## Related → [[source-adyen-docs-plugins-adobe-commerce-go-live-checklist]] → [[raw/adyen/docs/plugins/adobe-commerce/go-live-checklist/2026-09-15]].
