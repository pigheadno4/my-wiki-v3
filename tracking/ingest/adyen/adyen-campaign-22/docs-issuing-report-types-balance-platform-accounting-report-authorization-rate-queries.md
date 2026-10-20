# C22 Issuing authorization-rate report retrieval checks

## Q1 — What report information does this page suggest for investigating refusals?

Given access to the Balance Platform Accounting Report, the page suggests inspecting acquirer-sent payment context: payment-instrument type/ID, point-of-sale `Entrymode`, `Shopper interaction` such as POS or Ecommerce, MCC and counterparty name/address/city/country (raw lines 17–27). It points to Customer Area for additional payment-instrument information but states no role, API or separate report-access prerequisite (raw line 23). Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-report-types-balance-platform-accounting-report-authorization-rate]] → [[raw/adyen/docs/issuing/report-types/balance-platform-accounting-report/authorization-rate/2026-09-15]].

## Q2 — What does this page not establish about authorization rates or outcomes?

It says the report can help investigate refusals and increase authorization rate, but provides only the context-field list; no rate numerator/denominator, cohort, time window, specific refusal diagnosis, remedial action or observed improvement is supplied (raw lines 19–27). A report field or investigated refusal is not proof that a later authorization, capture or settlement succeeded. Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-report-types-balance-platform-accounting-report-authorization-rate]] → [[raw/adyen/docs/issuing/report-types/balance-platform-accounting-report/authorization-rate/2026-09-15]].
