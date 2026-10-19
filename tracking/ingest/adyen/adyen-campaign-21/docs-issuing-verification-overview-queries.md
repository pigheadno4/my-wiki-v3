# Retrieval checks — docs-issuing-verification-overview

Q1. When does Adyen verify Issuing cardholders, and how are capabilities requested?

A1. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-verification-overview]] → [[raw/adyen/docs/issuing/verification-overview/2026-09-15]]. The page says Adyen verifies cardholders before payout and before allowing requested capabilities (raw lines 19–30). Integration-default capabilities are requested when each new cardholder's account holder is created; non-default capabilities require a separate request and sometimes more verification (raw lines 34–38). Data changes after capabilities are allowed trigger re-verification (raw lines 42–48). The checks are asynchronous; errors may appear while status remains pending, and rejection disallows the capability (raw lines 140–152).

Q2. What are the deadline and webhook boundaries if updated cardholder data fails verification?

A2. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-verification-overview]] → [[raw/adyen/docs/issuing/verification-overview/2026-09-15]]. The page qualifies verification deadlines to Legal Entity Management API v3/v4 (raw line 54). It lists standard 30-day and 60-day capability groups, but says monitoring/checks can shorten or remove a deadline (raw lines 60–75). Capabilities can remain usable during an active deadline; unresolved or failed checks can disallow them (raw lines 44–48, 56–58, 162–168). The `balancePlatform.accountHolder.updated` webhook is only for capability-related account-holder changes, not legal-entity data changes themselves (raw line 50). The sample response at raw lines 82–132 illustrates fields and dates, not a verified live account or guaranteed deadline.
