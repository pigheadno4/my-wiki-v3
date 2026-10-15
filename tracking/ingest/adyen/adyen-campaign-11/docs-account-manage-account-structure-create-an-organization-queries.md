# Create an organization retrieval checks

## Q1 — Purpose and scope

**Query:** What does an Adyen organization group, and does it merge merchant accounts, contracts, or funds?

**Answer:** The guide defines an organization as a group of **legally related company accounts** for one Customer Area login, subject to Adyen-side configuration. It is distinct from the company-to-merchant-account processing hierarchy. The guide does not establish a new merchant of record, contract holder, consolidated balance, payout recipient, or funds flow, nor prove any setup was completed. **Raw locators:** `raw/adyen/docs/account/manage-account-structure/create-an-organization/2026-09-15.md:15-29`, `:31-37`. **Canonical route:** [[source-adyen-docs-account-manage-account-structure-create-an-organization]] → [[raw/adyen/docs/account/manage-account-structure/create-an-organization/2026-09-15]]; [[adyen-account-structure]].

## Q2 — Access and setup qualifications

**Query:** If two company accounts join one organization, does every user gain both accounts with the same roles and SSO automatically?

**Answer:** No. **Merchant admin** manages organizations; each legally related company is added individually after Adyen-side configuration. A user does not get access to every company account by default; create a company user where access is absent. Existing roles stay different per company. SSO inheritance follows which added company has SSO, while copying SSO configuration and migrating users are separate steps. Some profile/security changes for a user with multiple company accesses propagate across those accounts. The page describes UI confirmation messages, not evidence of a completed account change. **Raw locators:** `raw/adyen/docs/account/manage-account-structure/create-an-organization/2026-09-15.md:19-37`, `:39-61`, `:63-105`. **Canonical route:** [[source-adyen-docs-account-manage-account-structure-create-an-organization]] → [[raw/adyen/docs/account/manage-account-structure/create-an-organization/2026-09-15]]; [[adyen-account-structure]].
