---
title: "Adyen Classic Platforms: Document upload requirements"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/verification-process/document-requirements"
raw_files:
  - "adyen/docs/classic-platforms/verification-process/document-requirements/2026-09-15.md"
tags: [adyen, classic-platforms, verification, documents, account-holders]
---

## Overview

This 2026-09-15 capture of a 2021-modified Adyen page gives document-upload requirements for **Classic Adyen for Platforms** account-holder verification. It directs new implementations to a separate new integration guide. If automatic entity verification fails because information is wrong or cannot be verified, Adyen may request identity, registration, or bank evidence. Account holders can upload through the Classic Hosted Onboarding Page, or the platform can collect documents in its own flow and submit them to Adyen through the API. See [[adyen-classic-platforms]] and [[adyen]]; this is dated source guidance, not a finding that a particular account holder passed verification.

## Key takeaways

- **Individuals:** In the EU the page requires account-holder photo ID; elsewhere Adyen asks for photo ID if identity cannot be validated automatically (raw lines 28–30). Accepted ID types include passport data page, both sides of an ID card, or both sides of a driving licence, with front/back as separate files where relevant (raw lines 32–38, 51–55). The ID name must match onboarding data; if it does not, the check fails and matching first/last names must be supplied. Single-name individuals use the same name in both fields (raw lines 40–42). The ID must be physical, unexpired, appropriately signed where a signature field exists, and legible; digital IDs, secondary screenshots/copies, AI or image-editor modifications, and low-quality images are rejected (raw lines 44–64).
- **Organizations:** After automatic verification fails for the listed business or organization types, Adyen asks for a registration document, with asynchronous verification averaging about two days; that duration is guidance, not a completion guarantee (raw lines 81–88). The document must come from a reliable independent source and meet the page's one-year issuance or signed/status-date condition (raw lines 85–88).
- **Bank accounts:** If bank verification fails, Adyen asks for bank-account evidence. The page lists statements, deposit documents, **screenshots of the online banking environment**, official bank letters, and cheques, with location-specific forms (raw lines 99–115). This acceptance of online-banking screenshots is scoped to bank evidence; it does not override the photo-ID rejection of screenshots. Bank-issued card photos are explicitly disallowed because they contain sensitive information (raw lines 117, 133–140). The account-holder name, account number/IBAN, country, and bank issuer indicator must be visible, with issuance-date rules and exceptions for specified document types (raw lines 119–131).
- **File limits and regional conditions:** Individual photo-ID uploads have a general 15-page statement, but the same section restricts PDF files to two pages and limits files to 1 KB–4 MB (raw lines 64, 74–77); read these together rather than treating 15 pages as a PDF allowance. Organization files are generally 1 KB–4 MB with two-page PDFs, except legal-arrangement PDFs can reach 25 MB (raw lines 90–97). Bank evidence allows PDFs without a page maximum but retains the 1 KB–4 MB size range (raw lines 162–166). France, Poland and Ukraine notes are dated snapshot-specific, including an anomalous Polish date string `2013/19/01`; do not infer current legal validity from them (raw lines 66–72).
- The bank-evidence text gives a less-than-12-month issuance rule with exceptions for RIBs, cheques, online banking and TAMIEYTHPIO; if a RIB or online-bank view shows an issue date, that date must also be under 12 months (raw lines 125–127). Its later generic rejection of documents older than 12 months (raw line 137) does not restate those exceptions, so apply the type-specific wording rather than flattening the rules.

## Detail locators

- Classic-only scope, failed-verification trigger, HOP/API upload routes: raw lines 15–26.
- Individual ID conditions, exclusions, countries and format limits: raw lines 28–79.
- Organization registration document, asynchronous check and size exceptions: raw lines 81–97.
- Bank evidence types, disallowed card photos, mandatory fields, age exceptions, document-specific rules and file limits: raw lines 99–166.

## Related

- [[adyen]] — provider context.
- [[adyen-classic-platforms]] — Classic account-holder verification route.
- [[source-adyen-docs-classic-platforms-verification-process-accepted-data-format]] — separate accepted data-format reference.
- [[adyen-platforms]] — newer platform model, with separate verification rules.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/verification-process/document-requirements/2026-09-15|Classic Platforms document upload requirements, captured 2026-09-15]]
