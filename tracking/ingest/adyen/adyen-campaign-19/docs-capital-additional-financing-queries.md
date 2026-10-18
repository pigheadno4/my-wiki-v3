# Retrieval probes — Capital additional financing

Q1. How does the captured guide distinguish new financing after full repayment from pilot renewal of a partially repaid grant?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-additional-financing]] → [[raw/adyen/docs/capital/additional-financing/2026-09-15]].

Expected answer: A fully repaid prior grant follows the first-time new-grant path. Pilot renewal of a partially repaid prior grant needs a risk-assessed repayment threshold that varies by balance platform, no missed repayments, at least 90 days of age, same currency and a renewal offer at least 150% of outstanding balance. Underwriting can change fee, repayment percentage and maximum; offers recalculated weekly expire after seven days. The user must accept new ToS after selecting an offer. Raw locators: lines 19–29, 31–54; `## Eligibility`, `## Renewal conditions`. The page does not itself state API role or country lists, and eligibility is not actual funding.

Q2. What amount is effectively available in a renewal, and can one formula or UI state prove the prior grant settled and new funds arrived?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-additional-financing]] → [[raw/adyen/docs/capital/additional-financing/2026-09-15]].

Expected answer: The guide says full subsequent principal is disbursed and prior outstanding principal reserved for repayment atomically, unpaid prior fee waived, new fee charged on full subsequent principal, and effectively available funds equal new principal minus prior outstanding principal. The UI route speaks of minimum outstanding balance plus EUR 500/equivalent, whereas the general eligibility table says offer at least 150% outstanding; no reconciliation is given, so do not substitute one universal formula. API-only uses eligibility webhook/GET, qualifying offer, new ToS and `renewsGrantId`. These are described flow mechanics, not actual transaction/debt/bank-receipt proof. Raw locators: lines 37–41, 45–54, 56–77; `## Renewal conditions`, `## How renewal works`.
