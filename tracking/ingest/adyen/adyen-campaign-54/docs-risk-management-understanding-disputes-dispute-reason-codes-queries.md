# C54 dispute reason codes retrieval checks

Source stem: `source-adyen-docs-risk-management-understanding-disputes-dispute-reason-codes`
Canonical URL: https://docs.adyen.com/risk-management/understanding-disputes/dispute-reason-codes
Pinned raw: `raw/adyen/docs/risk-management/understanding-disputes/dispute-reason-codes/2026-09-15.md`

## Q1

**Question:** For a Visa 10.4 card-absent fraud chargeback, when does this snapshot say the merchant can respond, and when does the shorter window apply?

**Answer:** Visa 10.4 is marked defendable. The row says 9 or 18 days from receiving the NoC. Note 1 limits 9 days to disputes opened from 21 July 2025 on payments processed locally in the United States or Canada; earlier disputes in those countries and disputes in other countries or regions have 18 days in this snapshot. Check the specific case's event and processing region rather than treating 9 days as universal.

**Raw locator:** `## Visa → ### Fraud`, lines 856–870, especially code 10.4 at 865 and note 1 at 868–869.

## Q2

**Question:** Is a Notification of Fraud itself defendable, and how does that differ from a Klarna high-risk-order RFI?

**Answer:** The NoF tab explicitly says its reason codes cannot be defended. Separately, the Klarna RFI `high_risk_order` row is marked defendable with a 96-hour window from receiving the RFI and links to the `High risk order` evidence heading. These are different dispute events; the NoF statement does not cancel the RFI row.

**Raw locator:** `### Tab: Request for Information → ## Klarna`, lines 1018–1029 (especially 1029); `### Tab: Notification of Fraud`, lines 1085–1092; `### High risk order`, lines 1910–1945.
