# Retrieval checks — Issuing payment authorisation

## Q1: In what order is an issued-card payment initially checked, and what controls can the platform configure?

Adyen performs required issuer validation and internal regulatory checks first, including card legitimacy, available balance and missing capabilities (raw lines 19–37). Once these pass, optional platform transaction rules can accept or refuse on configured conditions; optional relayed authorisation sends an attempt to the platform server, which has up to 2000 ms to respond or Adyen applies the configured default fallback (raw lines 39–55). The numbered initial flow places validations before configured rules and relayed authorisation, and ends in approval or refusal (raw lines 63–71). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-authorisation]] → [[raw/adyen/docs/issuing/authorisation/2026-09-15]].

## Q2: Is the initial approval/refusal final, and does it prove capture or settlement?

The guide distinguishes its initial authorization endpoint from later scheme advice: in some cases a scheme evaluates the payment after Adyen's first flow. If its decision differs, Adyen defers to the scheme; that result sets final payment status and reserved-balance change and triggers an updated transfer webhook with a new booking event (raw lines 73–79). The page does not establish capture or settlement. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-authorisation]] → [[raw/adyen/docs/issuing/authorisation/2026-09-15]].
