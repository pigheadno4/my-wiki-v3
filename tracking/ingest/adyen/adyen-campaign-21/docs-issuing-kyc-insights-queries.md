# Retrieval checks — KYC verification analytics

## Q1: Who can view the dashboard, where is it, and what do its core metrics measure?

The guide requires one of Manage account holders and legal entities, Generate Balance Platform reports, or Download Balance Platform reports roles (raw lines 27–33). Customer Area's Analytics > KYC verification analytics route exposes Overview and Errors tabs, updates daily at 3:00 AM CET, and supports location, entity-type, integration-type and date filters (raw lines 35–47). Overview uses creation-date onboarding cohorts; attempts count each KYC submission, first-attempt success is first-try verified account holders over everyone who started onboarding, and median time runs from creation/first capability request through all valid checks (raw lines 59–62). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-kyc-insights]] → [[raw/adyen/docs/issuing/kyc-insights/2026-09-15]].

## Q2: Why might counts and status change, and what cannot the dashboard prove?

An account holder can have several error categories, so summed categories can exceed unique affected account holders; the Errors tab retains resolved errors and cohorts by account-holder creation date (raw lines 68–76). A verified account holder can later move to another status if more verification is required, while Classic Platforms upgrades start unsuccessful until they meet KYC/capability requirements (raw line 59). The guide's intervention and comparison examples suggest analyses, not causal proof or present-day transaction eligibility (raw lines 88–134). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-kyc-insights]] → [[raw/adyen/docs/issuing/kyc-insights/2026-09-15]].
