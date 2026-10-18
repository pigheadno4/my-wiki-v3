# Query checks — Business Accounts transaction rules

## Q1 — Purpose and prerequisites

**Query:** What are Business Accounts transaction rules for, and what must a reader establish before relying on them?

**Answer:** The 2022-modified, 2026-09-15-captured overview describes rules that evaluate outgoing third-party bank-transfer requests and decline matches to configured conditions. It explicitly calls the feature a limited-availability pilot and refers interested platforms to an Adyen contact. The overview defines criteria, conditions and hardBlock outcome, but leaves operational credential, webhook and creation prerequisites to its linked create-and-manage guide. Neither the pilot description nor a configured rule proves current entitlement or any completed transfer.

**Evidence:** Pinned raw lines 15–26 contain the scope and pilot warning; lines 28–54 define decision parts; lines 141–159 define hardBlock and combined rules; lines 168–178 point to the child guide. Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-transaction-rules]] → [[raw/adyen/docs/business-accounts/transaction-rules/2026-09-15]].

## Q2 — Material hardBlock, score, state and conflict boundaries

**Query:** Do the rules score, approve or settle transfers, and how should a velocity-rule limit and decline be interpreted?

**Answer:** In this overview the only selectable outcome is hardBlock, declining a transfer if all conditions within one applicable rule match; one matching hardBlock among multiple rules suffices. The page defines no scoring outcome or active/inactive rule-status procedure. Velocity considers previous transfers within its interval and aggregates at balance-account level, including when a rule targets an account holder or platform. The interval table distinguishes per-transaction, fixed, rolling and sliding evaluation. Its limit paragraph says authorizations consume count/amount and canceled or expired authorizations restore them, but its capture terminology conflicts with the surrounding outgoing-bank-transfer framing; it should not be read as bank settlement or a card capture flow. A webhook's declinedByTransactionRule reason reports a rule decline, not a successful payout.

**Evidence:** Pinned raw lines 57–96 cover types, intervals and aggregation; lines 130–139 use authorization/capture language; lines 141–159 define hardBlock and multi-rule behavior; lines 161–166 identify decline reporting. Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-transaction-rules]] → [[raw/adyen/docs/business-accounts/transaction-rules/2026-09-15]].
