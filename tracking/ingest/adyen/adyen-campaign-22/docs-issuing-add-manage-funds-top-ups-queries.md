# docs-issuing-add-manage-funds-top-ups retrieval checks

Q1. What is the top-up flow and what determines the amount and trigger?

Answer: A recurring top-up initiates an outgoing direct-debit request to a bank-account source and an incoming transfer to the linked balance account (raw lines 19, 60-66). The amount is fixed or target available balance (raw lines 26-31). The guide describes a threshold and weekday/weekly/monthly checks in the balance account's time zone or a null/omitted schedule with continuous checking; it says the trigger is available balance below threshold (raw lines 33-44). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-add-manage-funds-top-ups]] → [[raw/adyen/docs/issuing/add-manage-funds/top-ups/2026-09-15]].

Q2. Which limits or source conflicts matter before treating this as an executed top-up?

Answer: The funding source is referenced by `counterparty.transferInstrumentId`; if none is listed, the guide says to contact Adyen (raw lines 46-58). It calls schedule and threshold both criteria yet also defaults an omitted schedule to null (raw lines 35, 42). This overview says below threshold, while the companion create guide has a Customer Area less-than-or-equal statement (its raw lines 99, 242); equality is unresolved. A configured rule or direct-debit request does not prove a completed bank debit or balance-account transfer (raw lines 60-66). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-add-manage-funds-top-ups]] → [[raw/adyen/docs/issuing/add-manage-funds/top-ups/2026-09-15]].
