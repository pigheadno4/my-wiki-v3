# Fixed queries — docs-partners-uplift-enablement

## Q1 — Purpose, scope, and what must not be inferred

**Answer:** This Adyen guide is for partners enabling merchant customers to use Uplift across Protect, Tokenize, Authenticate, Optimize and Personalize. It divides feature implementation, merchant decisions, and Adyen-managed capabilities. It is a configuration and integration guide, not evidence of a merchant's entitlement, measured conversion lift or cost reduction, authentication success, successful payment, or settlement. The guide recommends Web Drop-in/Components v6 and Checkout API v71+; API-only v71+ routes have additional requirements rather than identical support.

**Raw locators:** lines 15–21 (identity, audience, five modules); 23–39 (integration/version, webhook, application and shopper-data requirements); 41–51 (module map).

**Canonical route:** [[adyen-index]] → [[adyen-uplift]] → [[source-adyen-docs-partners-uplift-enablement]] → [[raw/adyen/docs/partners/uplift-enablement/2026-09-15]]. Broader partner context: [[adyen-partners]].

## Q2 — Central capability, prerequisites, and warnings

**Answer:** General partner requirements include webhook processing, application information in every payment request, and shopperEmail at minimum; the linked requirements page owns the full field list. Protect adds configurable/static risk-profile and dispute/data choices, with premium case review conditional. Tokenize requires four named token fields; Network Tokenization needs Adyen-side configuration and RTAU is optional paid with updates in payment responses rather than webhooks. Authenticate needs native or redirect 3DS2, threeDS2 action handling, and browserInfo in Advanced flow. Optimize has qualifying US enhanced-data/webhook work, co-badged Web v6.16.0 minimum, at-least-two-route routing off by default, Auto Rescue outcome webhooks, and an ERPS maintenance/authorization-rate warning. Personalize works automatically with Sessions per the guide; Advanced requires shopperConversionId in both payment and methods requests and preservation of returned order. These conditions are module- and flow-specific; none guarantees a business or payment result.

**Raw locators:** lines 23–39 (general requirements); 53–75 (Protect); 77–92 (Tokenize); 94–111 (Authenticate); 113–134 (Optimize, version floor and ERPS); 136–152 (Personalize).

**Canonical route:** [[adyen-index]] → [[adyen-uplift]] → [[source-adyen-docs-partners-uplift-enablement]]; complete module matrix at [[raw/adyen/docs/partners/uplift-enablement/2026-09-15]].
