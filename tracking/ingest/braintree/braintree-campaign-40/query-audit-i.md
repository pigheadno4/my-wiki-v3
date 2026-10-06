# Braintree Campaign 40 Fixed Query Audit — Group I (33–36)

Audit time: 2026-10-05T01:38:19Z

Scope: exactly four manifest jobs, two fixed questions per source page. Catalog edits are deferred. Answers are bounded to the 2026-09-16 captured pages; linked downloads and navigation targets are not treated as evidence unless explicitly read.

## Result

**8/8 PASS.** Each fixed query is answerable from the source summary with an exact raw route, while preserving page-specific scope, prerequisites, material warnings, and non-inference boundaries.

## Shared evidence and routing checks

- **Manifest/raw integrity — PASS:** all four manifest paths exist and their SHA-256 values match exactly:
  - financing options: `31bb88953352b4dd28f4ac62b5bcd7696f1299a6a0629e06e682e5a4fcb1b2c3`
  - PayPal Intake dictionary: `844778078e7bc653ebe56d1865c1f4889c092a12a81b14bd11c65d876acf6020`
  - Mastercard Spring 2023: `6e230ba120650d8c5518b044d666abc84dea6bd9aab3e36274afed0321048b4d`
  - Account Onboarding/UOB dictionary: `c73a9b6c142f1c8ad1ed6abe5a9df6dbffa1733aa3fc2c242632de221d4c6af5`
- **Root → provider — PASS:** `wiki/index.md:5-11` routes Braintree queries to `[[braintree-index]]`.
- **Provider → source — FAIL, catalog deferred:** exact-slug search finds none of the four source links in `wiki/braintree-index.md`. No catalog edit is made in this audit.
- **Concept ↔ source reverse routing — PASS:** financing is linked from `wiki/concepts/braintree-payment-methods.md:24`; the other three are linked from `wiki/concepts/braintree-payment-platform.md:27,30-31`. Each source links back to its concept and company (`financing source:44-45`; Intake `:39-40`; Mastercard `:38-39`; UOB `:41-42`).
- **Source → raw and canonical provenance — PASS:** each source's `raw_files` entry and `## Raw Sources` link resolve to the manifest raw path, and each raw line 1 URL matches the source/manifest canonical URL.
- **Bounded gap sweep — PASS:** distinctive-term/path search under `raw/braintree/` found (a) the duplicated Mastercard sections in the all-Spring-2023 aggregate, fully checked and consistent with the child page; (b) adjacent Application Uploader overview/sample material, which reinforces v1/v2 and submission-versus-approval boundaries but is not field-level dictionary authority; (c) an Account Onboarding integration guide that routes to the UOB dictionary; and (d) separate Pay Later/Credit and validation-error materials that are outside this Brazil Billing Agreement guide's fixed questions. No contradiction or missing authority changes an answer. The Mastercard aggregate adds its own “accurate as of March 31, 2023 / subject to change / may not apply” qualification (`raw/.../s-2023-all-2026-09-16.md:17-27`); the audited child source already preserves the historical/non-current boundary.

## 33. `graphql-integration-guides-financing-options`

### Q1. What exact product/merchant scope and two-step action does the page document, and what inputs does each step require?

**PASS.** It documents PayPal Billing Agreement with Installments only for merchants domiciled in Brazil, through Braintree GraphQL; server SDK support is described as future work. The merchant first calls `paypalFinancingOptions` with a payment-method ID, transaction information, currency code, and country code. It then calls `chargePayPalAccount` with the payment-method ID, transaction information, and a selected financing option. Do not generalize this to another domicile, payment method, installment product, SDK, or environment.

Locators: source `:14,18-20,22,26-30,34-40`; raw `:14-18,21-27,35-37,93-105,163-165,199-217`.

### Q2. Which states does the guide call a successful charge, and what do those states and examples not prove?

**PASS.** The documented alternatives are `SETTLING`, `SUBMITTED_FOR_SETTLEMENT`, or `SETTLED`; the displayed response happens to show `SETTLING`. They are distinct lifecycle states, not evidence that the example actually ran or that any real charge settled or funded. The snippets also do not establish an exhaustive/current schema, nullability, validation behavior, buyer or merchant eligibility, guaranteed offers, or Sandbox/Production availability.

Locators: source `:20-21,24-30,38-40,47-49`; raw `:220-251`.

## 34. `articles-guides-application-uploader-paypal-intake-data-dictionary`

### Q3. What intake routes and downloadable schema families does this landing page identify, and what availability limit can be stated exactly?

**PASS.** The page routes bulk application data through the Intake API or the Application Uploader and identifies PayPal Intake v1 and v2 dictionaries plus v1/v2 samples, along with a separate branded-solution dictionary and sample. Only the **Application Uploader** is explicitly said here to be available to select merchants; the page does not say the Intake API has that same availability restriction. The CSVs are linked but their rows were not collected/read, so the landing page cannot establish exact field keys, requiredness, enums, formats, or current download contents.

Locators: source `:14,18,26-28`; raw `:17-24,26-48`.

### Q4. What does the page actually say about discount-program registration, and which section/purpose facts are safe to retain?

**PASS.** The seven prose sections are Identifier, Business, Owner, Funding, ACH, Discount program registration, and American Express. ACH, Discount Program, and American Express are not required for branded solutions. Discount-program data is included only when the biller **should be registered**; this does not mean the biller is already registered. For API use, the page says `discountProgramRegistration.registered` need not be supplied because a value in `discountProgramRegistration.registrationIdentifier` implies `yes`. This field rule belongs to the Intake page and must not be transferred to UOB. Business/owner data supports underwriting and feature setup, but application preparation/submission is not approval or enablement.

Locators: source `:19-22,29-34`; raw `:50-64,67-78,81-101,106-110`.

## 35. `articles-risk-and-security-compliance-network-updates-2023-mastercard-s23`

### Q5. What Canada fee and APAC program does this historical page report, including every APAC qualification?

**PASS.** For Canada, it reports a March 13, 2023 Mastercard Digital Enablement Fee of 0.02% on card-not-present authorizations, with a USD $0.02 minimum and $0.20 maximum per transaction, while retiring certain existing CNP fees. For APAC, it reports B9 at 0.325% + USD $0.00, with cumulative—not alternative—criteria: amount greater than USD $10,000; CNP; invoiced in USD and settled with Mastercard in USD (BIN may be any currency); non-travel-and-entertainment spend; cross-border and intraregional Asia/Pacific; issuer country not Korea; and acceptance by a B2B acceptance enabler registered in Mastercard's BPAP. The page describes that BPA as merchant of record accepting card transactions for an end supplier.

Locators: source `:18-19,31-32`; raw `:17-29,32-52`.

### Q6. What did the page say about service-location fields and Europe final-authorization clearing, and what historical/applicability qualifications control the answer?

**PASS.** It planned service-location fields for clearing messages in April 2023 and authorization messages in June 2023, while saying merchants were not expected to be ready yet and presenting the item as future information. The captured phrase “merchants that move” is unclear, so no affected merchant class may be reconstructed. For Europe, beginning May 22, 2023, a merchant processing there had to submit a clearing record for a final authorization within three calendar days of approval, down from seven; estimated and incremental authorizations were excluded. These are historical Braintree-hosted statements, not current Mastercard policy, merchant-specific applicability/pricing, compliance proof, or fee-assessment evidence.

Locators: source `:14,20-27,33-34`; raw `:57-72`; overlapping aggregate qualification raw `s-2023-all-2026-09-16.md:17-27`.

## 36. `articles-guides-application-uploader-paypal-uob-api-data-dictionary`

### Q7. What distinguishes this UOB route from the PayPal Intake route, what downloads are exposed, and what field detail is actually evidenced?

**PASS.** This is the select-merchant **Account Onboarding API** dictionary route for preparing many applications through the onboarding API, not the separate PayPal Intake/API-or-Application-Uploader route. It links a general Account Onboarding dictionary CSV and a separate Account Onboarding Branded Solution dictionary CSV. Those downloads were not collected/read. The landing-page prose safely establishes two Create Account Input settings—external ID and Country Code—and that other properties are nested under that input, but it does not establish exact CSV column keys, the complete row list, enums, formats, requiredness, validation rules, or a current API schema.

Locators: source `:14,18,27-28,32-36,45-48`; raw `:17-34,54-56`.

### Q8. Which UOB application-section qualifications and onboarding prerequisites/boundaries must an answer retain?

**PASS.** The seven sections are Create Account Input, Business, Stakeholder, Funding, ACH, Discount Program registration, and American Express. Branded Solution omits ACH, Discount Program, and American Express. Business/stakeholder information supports underwriting and PayPal/Venmo/Hyperwallet setup; if additional people beyond beneficial owners or authorized signers should join vetting/review, at least one Point of Contact is required, and stakeholder information is required for any beneficial owner with more than 25% ownership. Discount-program information is included only if the biller **should be registered**—not proof of existing registration. Preparing or submitting this data does not prove approval, activation, feature enablement, payment processing, or payout execution.

Locators: source `:19-28,34-37`; raw `:36-49,59-74,79-96`.

## Analysis end / handoff

Completed at 2026-10-05T01:38:19Z. Query content is ready for coordinator review: **8 PASS, 0 FAIL**. One shared discovery defect remains intentionally deferred: add the four source links to `wiki/braintree-index.md` only under the coordinator's catalog-update workflow. No repository files were modified by this audit.
