# Capital user capabilities retrieval checks

Q1. Which Capital capabilities must an account holder have before offer and grant steps, and what prerequisites and roles govern their management?
Expected forward route: [[adyen-index]] → [[adyen-capital]] → ## Sources → [[source-adyen-docs-capital-manage-user-capabilities]] → [[raw/adyen/docs/capital/manage-user-capabilities/2026-09-15]]. Inspect raw lines 19–35 for account holder, Capital enablement, roles, region and setup; lines 37–44 for getGrantOffers, receiveGrants, eligibility, Terms of Service and separate disbursement step.

Q2. Does requesting or enabling a Capital capability prove it is allowed, an offer exists, or funds were disbursed?
Expected forward route: [[adyen-index]] → [[adyen-capital]] → ## Sources → [[source-adyen-docs-capital-manage-user-capabilities]] → [[raw/adyen/docs/capital/manage-user-capabilities/2026-09-15]]. Inspect raw lines 46–118 for request/approval and requested=true, allowed=false, pending example; lines 120–148 for allowed, enabled, verificationStatus and problems; lines 150–224 for enable/disable and allowed-but-disabled example. These fields do not report offer acceptance or completed funding.
