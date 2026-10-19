# Retrieval checks — docs-issuing-onboard-users-terms-of-service

## Q1 — Purpose and prerequisites

How does a platform using its own onboarding UI collect Adyen Terms of Service acceptance? The 2026-09-15 guide requires generating and presenting the document, then recording acceptance by an individual legal entity; an organization uses an authorized signatory (raw lines 19-23). Its requirements table calls for an Adyen for Platforms integration, Legal Entity Management API credentials, webhooks and the relevant legal entities (raw lines 30-42). Follow the account-holder webhook, GET required types, POST documents, present every required document, then PATCH acceptance and optionally GET acceptance information (raw lines 44-53, 109-115, 129-137, 359-396, 620-622). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-onboard-users-terms-of-service]] → [[raw/adyen/docs/issuing/onboard-users/terms-of-service/2026-09-15]].

## Q2 — Boundary or conflict

Does the Issuing-path guide prove an Issuing-only account can use this exact API flow, or that its test response has the three illustrated types? No. Its requirements table explicitly says Adyen for Platforms despite the Issuing path (raw lines 8, 36). The prose says the test environment returns only `adyenForPlatformsAdvanced`, while the response example lists that type plus `adyenCapital` and `adyenAccount` (raw lines 115, 119-127). Hosted onboarding completes the acceptance step in its own flow (raw line 21); the self-built UI steps should not be imposed on it. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-onboard-users-terms-of-service]] → [[raw/adyen/docs/issuing/onboard-users/terms-of-service/2026-09-15]].
