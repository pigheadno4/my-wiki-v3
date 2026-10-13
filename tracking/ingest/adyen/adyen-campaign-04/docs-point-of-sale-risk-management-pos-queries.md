# Fixed retrieval checks — Adyen POS risk management

## 1. Purpose, scope, and limits

**Query:** What is this POS risk page for, and what should a reader avoid inferring from it?

**Answer:** This dated Adyen guide describes enabling Customer Area risk checks for riskier MOTO and Manual Key Entry payments, using the RevenueProtect name in a page last modified 2022-12-26 and fetched 2026-09-15. It says most ordinary POS payments do not need those ecommerce-oriented rules. It does not establish current merchant enablement, a universal terminal fraud rule, mobile SDK behavior, cardholder-verification policy for other entry modes, or a live outcome. See raw lines 24–28 and the source's scope note.

**Route:** [[index]] → [[adyen-index]] → [[adyen-risk-management]] → [[source-adyen-docs-point-of-sale-risk-management-pos]] → [[raw/adyen/docs/point-of-sale/risk-management-pos/2026-09-15]] (catalog promotion pending).

## 2. Central flow, prerequisites, and warnings

**Query:** How does the guide configure and test POS risk checks for MOTO/MKE, and what warnings matter?

**Answer:** Enable risk and POS checks in Customer Area at company scope, or at merchant scope after overriding the company setting (raw lines 30–47). The company default profile then applies; for a merchant processing only POS, Adyen recommends a dedicated assigned profile and directs disabling three shared-IP/shopper-reference rules that may wrongly decline terminal traffic (lines 49–87). Optional Consistency, Velocity, AVS with address data, CVC mismatch, and custom rules are described at lines 89–103. Under the described settings a score of 100 declines with Card blocked; the test example produces Terminal API Failure/Refusal with reason 199 and says not to retry (lines 26, 105–143). The guide says MOTO/MKE have no liability shift and the accepting merchant is liable for fraud chargebacks (line 28).

**Route:** [[index]] → [[adyen-index]] → [[adyen-risk-management]] → [[source-adyen-docs-point-of-sale-risk-management-pos]] → [[raw/adyen/docs/point-of-sale/risk-management-pos/2026-09-15]] (catalog promotion pending). [[adyen-terminal-api]] provides the parallel Terminal API response route.
