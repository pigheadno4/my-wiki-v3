---
title: "Braintree SCIM Integration Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/users-roles/scim/scim-integration"
raw_files:
  - "braintree/articles/control-panel/users-roles/scim/scim-integration-2026-09-16.md"
tags: [braintree, control-panel, scim, sso, identity-provisioning, access-control, okta, microsoft-entra]
---

## Overview

This collected [[braintree]] guide documents onboarding and configuration routes for using Okta or Microsoft Entra as SCIM identity providers for Braintree users. Its purpose is automated user provisioning and de-provisioning plus provider-qualified role and merchant-account access management; it is a captured setup guide for [[braintree-control-panel]], not proof that a request was approved, an account was enabled, a synchronization completed or a particular permission change took effect.

## Key takeaways

- The integration supports user create, get, update and delete operations plus group updates. It does not create or delete the roles or merchant accounts represented by those groups; those resources remain managed through the Braintree website. The later limitations section further says Okta cannot delete an SSO Braintree user through SCIM and that SCIM does not manage non-SSO users.
- The collected prerequisites say onboarding is limited to managed merchants with a dedicated CSM or TAM and requires both Sandbox and Production merchants, with Sandbox onboarded before Production. They also require both merchants to be on SSO, use a Braintree OIN application instance for each merchant, have intended SCIM-managed users already converted to SSO users and have no pending SSO users. The prerequisite wording is Okta-specific even though the guide also covers Entra, so do not infer an undocumented Entra equivalent from it.
- The merchant asks its CSM or TAM to begin onboarding, after which the Braintree Identity team has internal preparation work. The guide says that preparation disables Control Panel editing of SSO users for data consistency and supplies the SCIM access token used by Okta or Entra. A request, token receipt or connection test does not by itself establish that internal preparation, onboarding or synchronization completed.
- For an Okta merchant moving from an existing custom SSO app to the Braintree OIN app, the guide says to send Braintree the new OIN app certificate, SSO target URL and requested cutover timeframe so Braintree can change its expected SSO target. All existing users must be assigned to the new OIN app before the cutover or they will be unable to log in. Supplying the app data or requesting a timeframe is not evidence that Braintree completed the target change.
- In the Okta route, assigning a master group to the Braintree OIN application provisions users and removing a user from that group suspends the Braintree user unless another direct or group assignment remains. Imported role, merchant-account, Grant All Merchant Accounts and API Access groups have distinct permission effects. Push groups are not the mechanism for overall Braintree application access, and a Braintree user needs at least one role to log in.
- Okta push-group names must exactly match the imported app-group names. The Okta group must be populated to match the app group before the two are linked: otherwise Okta can replace membership with the empty group and remove users' associated Braintree role or merchant-account access. The page directs the administrator to verify the Braintree Control Panel after a push; the setup action itself is not completion evidence.
- The Entra section configures a non-gallery enterprise application, SAML SSO and bearer-token SCIM provisioning. It requires the user mapping to contain only `userName`, `givenName`, `familyName` and `nameFormatted`, with `userName` mapped to email, and describes group mappings separately. Its captured procedure covers automatic user provisioning and management only; it explicitly leaves automatic role and merchant-account access management to external Microsoft guidance.
- Post-configuration, the guide recommends testing application assignment, user lifecycle, role and merchant-account groups, API Access, Grant All Merchant Accounts and both SSO login paths. It does not support creating, deleting or renaming roles or merchant accounts through SCIM, and it says these resource-management actions remain Control Panel tasks.

## Detail locators

- Guide identity, provider scope and purpose: `# Overview`, lines 14-18.
- Supported user and group operations and Braintree-managed role/merchant-account resources: `##### Supported Features`, lines 23-25.
- Managed-merchant, Sandbox-before-Production, SSO/OIN, existing-SSO-user and no-pending-user prerequisites: `## Pre-requisites for Onboarding to SCIM`, lines 30-46.
- CSM/TAM request, Braintree internal work, SSO-user edit disablement and access-token handoff: `##### Reach out to Braintree support (Okta or Entra)`, lines 52-60.
- Existing-custom-Okta-app to OIN-app cutover inputs, Braintree-side target change, required pre-cutover user assignment and login-loss warning: `**Note**` and `##### Configuring the SCIM Integration`, lines 120-141.
- Okta provisioning features, attribute matching and user import: `##### Defining Provisioning Settings` through `##### Matching and Confirming Users`, lines 173-235.
- Okta role, merchant-account, Grant All Merchant Accounts and API Access group meanings: `##### Assigning push groups to the app groups`, lines 242-253.
- Master assignment-group lifecycle, push-group scope, exact-name requirement and destructive empty-membership warning: `##### Assigning push groups to the app groups`, lines 256-284.
- At-least-one-role login condition and synchronous versus asynchronous push behavior: `##### Assigning Users to the App post-import`, lines 289-306.
- Okta creation, update and deactivation verification plus logs: `##### Testing Provisioning` and `##### Monitoring and Troubleshooting`, lines 309-350.
- Entra SSO prerequisite, environment-specific tenant URLs, user/group mappings, on-demand test and later sync confirmation: `## Microsoft Entra Setup`, lines 359-407.
- Entra role/merchant-account guide gap: `**Setting up push groups:**`, lines 409-411.
- Recommended lifecycle/access tests and unsupported role, merchant-account, Okta-delete and non-SSO operations: `## Post-Configuration Testing Steps`, lines 420-444.

## Evidence boundary

> [!warning] Provider and snapshot scope
> The generic prerequisites use Okta-specific administrative and OIN-app wording, while the Entra procedure creates a non-gallery application. Keep the two provider routes distinct and do not invent a shared prerequisite, current entitlement or completed onboarding state. The Entra section does not document role or merchant-account automation, and its external Microsoft link is navigation rather than evidence here.

> [!warning] Identity and permission transitions
> A connection test, import, provisioning command, group link or UI success notification is not by itself evidence of the resulting Braintree user state or permission set. Use the guide's explicit verification steps, and preserve its warning that linking an empty Okta group can remove role or merchant-account access. Keep general User Delete support distinct from the later Okta-specific prohibition on deleting SSO Braintree users.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/control-panel/users-roles/scim/scim-faq-2026-09-16|Braintree SCIM FAQ]] - unread navigation-only troubleshooting and edge-case route
- [[raw/braintree/articles/guides/single-sign-on-sso-2026-09-16|Braintree SSO guide]] - unread navigation-only SSO onboarding and migration route
- [[raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16|Braintree gateway credentials]] - unread navigation-only API and tokenization-key route

## Raw Sources

- [[raw/braintree/articles/control-panel/users-roles/scim/scim-integration-2026-09-16|Braintree SCIM Integration Guide]] - complete collected guide for Okta and Microsoft Entra onboarding, user lifecycle, provider-qualified permission groups and consequential setup limits
