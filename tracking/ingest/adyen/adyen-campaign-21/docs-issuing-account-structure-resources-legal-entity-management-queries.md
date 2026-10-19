# C21 worker queries — Issuing legal entity management resources

Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-account-structure-resources-legal-entity-management]] → [[raw/adyen/docs/issuing/account-structure-resources/legal-entity-management/2026-09-15]].

## Q1. What resources does the platform create for Issuing user verification?

Adyen says the platform must create legal entities and associated resources to submit required user verification information (raw lines 19–25). The legal entity holds user identity details; the transfer instrument is the user's verified payout bank account; supporting documents verify legal-entity or transfer-instrument information; and the business line describes industry and source of funds (raw lines 27–30). The page names the Legal Entity Management API for managing these resources (raw line 32).

## Q2. What boundary should a reader keep between these resources and actual outcomes?

The page presents the transfer instrument as a payout bank account, not a card or balance account (raw line 28). It says Adyen must verify users before payments, payouts, and financial products (raw line 19), but supplies no evidence that any particular user has passed verification or has a live account, card, or payout. The detailed requirements are linked out rather than enumerated here (raw line 21); the diagram is an image link at line 34.
