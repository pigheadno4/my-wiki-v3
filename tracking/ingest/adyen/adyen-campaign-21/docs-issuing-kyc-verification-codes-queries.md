# Retrieval checks — docs-issuing-kyc-verification-codes

## Q1 — Main purpose and access

Where does an Issuing/Platforms integration find verification codes, and what access does it need? The guide separates general errors, granular linked suberrors and possible remediating actions (raw lines 19-25). API access to the codes requires a Configuration API web-service credential; Customer Area access needs Manage account holder capabilities (raw lines 27-35). Inspect the Customer Area account-holder Capabilities tab, GET `/accountHolders/{id}`, or follow account-holder created/updated webhooks; codes are in capability `problems` (raw lines 37-61). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-kyc-verification-codes]] → [[raw/adyen/docs/issuing/kyc-verification-codes/2026-09-15]].

## Q2 — Material boundary and nested failure detail

Does every general error guarantee one remediating action, or does the overview enumerate every code? No: Adyen says it sends a possible action whenever possible (raw line 21). A `problems` item identifies the legal entity; nested `verificationErrors` carry general code/type/message, optional common actions and `subErrors` with their own details/actions (raw lines 69-81). The example uses ellipses and is not parse-ready JSON (raw lines 83-144). The guide links separate general, suberror and action catalogues (raw lines 146-164). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-kyc-verification-codes]] → [[raw/adyen/docs/issuing/kyc-verification-codes/2026-09-15]].
