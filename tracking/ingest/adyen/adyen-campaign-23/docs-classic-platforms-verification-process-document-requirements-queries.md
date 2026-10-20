# C23 worker queries — Classic Platforms document uploads

Route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-verification-process-document-requirements]] → [[raw/adyen/docs/classic-platforms/verification-process/document-requirements/2026-09-15]].

## Q1. When are documents requested, and how can a Classic account holder provide them?

This page is for Classic Platforms, with new implementers directed to another guide (raw line 19). If Adyen cannot automatically verify an account holder's entity because data is incorrect or unverifiable, it asks for additional documents (raw line 21). The account holder can upload through the Hosted Onboarding Page, or the platform can collect documents in its own flow and submit an API request (raw lines 23–26). Individuals in the EU require photo ID; elsewhere ID is requested if automatic identity validation fails (raw lines 28–30). Organizations and bank accounts have their own failed-verification document paths (raw lines 81–83, 99–101).

## Q2. What material exclusions and conditional limits prevent a misleading upload answer?

Photo IDs must be physical, unexpired and legible, with matching name data; digital IDs, screenshots/secondary copies, AI edits and low-quality images are rejected (raw lines 40–64). By contrast, screenshots of an online banking environment are listed as bank-account evidence, but photos of bank-issued cards are barred (raw lines 103–117). Bank documents need visible identifying data and normally a date under 12 months, with named type-specific exceptions and a later broad older-than-12-month rejection that does not repeat them (raw lines 119–140). Individual ID text states a 15-page maximum while its PDF format row limits PDFs to two pages; organization legal-arrangement PDFs have a 25 MB exception, and bank PDFs have no page maximum (raw lines 64, 74–77, 90–97, 162–166). These are dated document criteria, not proof of approval or current law.
