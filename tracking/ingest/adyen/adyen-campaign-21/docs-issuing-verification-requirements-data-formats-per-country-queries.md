# C21 worker queries — data formats per country/region

Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-verification-requirements-data-formats-per-country]] → [[raw/adyen/docs/issuing/verification-requirements/data-formats-per-country/2026-09-15]].

## Q1. What does this page provide, and what preparation does it require?

It lists country/region-specific accepted formats and examples for legal-entity information, including addresses, bank accounts, individual IDs, and registration/tax numbers where shown (raw lines 15–19 and country tables at 29–452). For an Adyen for Platforms or Adyen Issuing integration, the page states there are no additional requirements, limitations, or preparations (raw lines 25–27). This is a dated format reference, not account eligibility evidence (raw lines 2, 11).

## Q2. What material boundary or failure matters when using these formats?

Adyen says automatic verification can fail for unverifiable or incorrect data, prompting additional documents (raw line 21). Canada requires a registration document without a Business Incorporation Number (raw line 86); Italy can verify CCIAA/REA only with a CCIAA document (raw line 240). The generic optional-separator statement (raw line 23) must be read with field-specific constraints: Singapore bank account numbers exclude separators/whitespace (raw line 373), and Swedish individual-number rows mandate a dash (raw lines 422–423). Cyprus requires English equivalents for registry prefixes (raw lines 108–114).
