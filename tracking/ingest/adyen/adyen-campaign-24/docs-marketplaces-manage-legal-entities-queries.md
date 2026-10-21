# C24 query checks — docs-marketplaces-manage-legal-entities

## Q1 — Purpose and prerequisites
Q: How does a Marketplace platform create and manage a user's legal entity, and what access/data conditions apply?
A: This pinned Marketplaces guide uses Legal Entity Management API v3 for an individual or organization Balance Platform legal entity, as part of onboarding and verification. It requires a Legal Entity Management web-service user with Manage LegalEntities via API and Balance Platform BCL Legal Entity role; creation data varies by location and entity type. POST /legalEntities creates the resource, and the returned ID is used for later account-holder and hosted-onboarding steps. See raw/adyen/docs/marketplaces/manage-legal-entities/2026-09-15.md:19-43, :373-400.
Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-manage-legal-entities]] → [[raw/adyen/docs/marketplaces/manage-legal-entities/2026-09-15]].

## Q2 — Material boundaries
Q: Does updating details or changing a legal-entity type establish verification approval, and can an associated legal entity's type be changed?
A: No. PATCH changes only supplied fields; hosted-onboarding updates and legal-entity-type changes rerun verification checks. Only the main legal entity's type can change; an incorrect associated entity requires a new legal entity. API-only direct changes are individual↔organization, with a further association step for organization→sole proprietorship. Customer Area access to listed unredacted PII is separately role-gated. See raw/adyen/docs/marketplaces/manage-legal-entities/2026-09-15.md:421-430, :649-651, :974-992, :1029-1036, :1244-1247.
Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-manage-legal-entities]] → [[raw/adyen/docs/marketplaces/manage-legal-entities/2026-09-15]].
