# Fixed retrieval checks — docs-plugins-netsuite-payment-processing-in-netsuite

## Q1 — Purpose, scope, and what not to infer

**Query:** What does this NetSuite payment-processing page describe, and what does it not prove?

**Answer:** It describes Adyen SuitePayment workflow in NetSuite for Sales Order authorisations, shipment-linked captures, direct Cash Sales, Customer/Cash refunds, plug-in logs and Adyen-to-NetSuite result labels. It does not establish that a particular authorization, capture, refund, settlement or bank receipt occurred; a NetSuite checkbox, saved request, Cash Sale record or mapped status is not independent financial proof. The raw webpage is 2023-modified and captured 2026-09-15, with no package version. Evidence: raw lines 10, 16–18, 33–46, 56–88. Canonical route: [[adyen-index]] → [[adyen-netsuite]] → ## Sources → [[source-adyen-docs-plugins-netsuite-payment-processing-in-netsuite]] → [[raw/adyen/docs/plugins/netsuite/payment-processing-in-netsuite/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** How do Sales Order authorisation, capture, Cash Sale, refunds and result labels differ in this guide?

**Answer:** A Sales Order can request authorisation before shipment via an available active processing profile and **Get Authorisation**. If the card was approved outside automated communication, **Credit Card Approved** signals that path and the Adyen PSP reference must be entered in **P/N Ref.** before shipment capture; the optional auth code is separate. Shipment confirmation uses the original authorisation reference and capture prompts secondary confirmation. Direct Cash Sale, unless manually pre-approved, initiates an authorise-and-capture request; partial captures or imported authorisations may need manual PSP-reference entry. Customer Refund and Cash Refund both require a P/N Reference to the original Auth/Sale; unreferenced refunds and SuitePayment credits are unsupported. The result table maps Adyen outcomes into NetSuite labels (for example Authorised→ACCEPT, Received/Pending→CONFIRMATION_PENDING), and unknown entries to GENERAL_REJECT or FATAL_ERROR. These are request/record/status descriptions, not proof of capture completion or payout. No payment-hold or deposit lifecycle is defined on this page. Evidence: raw lines 18–31, 33–71, 86–125. Canonical route: [[adyen-index]] → [[adyen-netsuite]] → ## Sources → [[source-adyen-docs-plugins-netsuite-payment-processing-in-netsuite]] → [[raw/adyen/docs/plugins/netsuite/payment-processing-in-netsuite/2026-09-15]].
