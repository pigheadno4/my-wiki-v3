# Versioning retrieval checks

## Q1 — Purpose and scope

**Query:** What does Adyen's versioning guide cover, and what should it not be used to infer?

**Answer:** It describes versioning policy for Adyen APIs and server-side API libraries. The 2026-09-15 snapshot has 2022-01-18 last-modified metadata. It does not prove current availability of a named API version, merchant eligibility, or behavior of a specific SDK release. For direct calls, find an individual API version in the URL; a server-side library has its own package version and release notes for included API versions. **Raw locators:** `raw/adyen/docs/development-resources/versioning/2026-09-15.md:5-17`, `:25-42`, `:124-130`. **Canonical route:** [[source-adyen-docs-development-resources-versioning]] → [[raw/adyen/docs/development-resources/versioning/2026-09-15]]; [[adyen-sdk-automation]] for generation and release provenance.

## Q2 — Central capability and qualifications

**Query:** How does Adyen classify version changes, and what must an upgrader check?

**Answer:** Breaking API changes receive a new API version; non-breaking changes can reach existing versions. Classification differs for new and classic APIs: adding a response-body field is non-breaking in new APIs and breaking in classic APIs. Documentation deprecation of a field is non-breaking, while removal is separately listed as breaking. An API version may appear without visible consumer changes and numbers may be skipped. Server-side libraries use MAJOR.MINOR.PATCH semantics; check the specific API's Explorer/release notes and the library release before upgrading. The guide recommends upgrading but describes continuing on an existing version until ready; its dated snapshot does not guarantee current availability. **Raw locators:** `raw/adyen/docs/development-resources/versioning/2026-09-15.md:27-33`, `:54-69`, `:73-110`, `:112-138`. **Canonical route:** [[source-adyen-docs-development-resources-versioning]] → [[raw/adyen/docs/development-resources/versioning/2026-09-15]]; [[adyen-sdk-automation]] for SDK release provenance.
