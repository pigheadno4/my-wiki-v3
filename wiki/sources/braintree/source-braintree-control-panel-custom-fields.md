---
title: "Braintree Control Panel Custom Fields"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/custom-fields"
raw_files:
  - "braintree/articles/control-panel/custom-fields-2026-09-16.md"
tags: [braintree, control-panel, custom-fields, api, fraud-protection]
---

## Overview

This collected Braintree article documents how custom fields are configured and surfaced across the Control Panel and API. It distinguishes Pass Thru from Store and Pass Back fields, identifies who can create, edit or delete the configuration, and records separate visibility behavior for Fraud Protection Advanced fields.

## Key takeaways

- Braintree describes two custom-field types. Pass Thru fields carry checkout values through the API for a merchant's server to handle; although their definitions are configured in the Control Panel, the fields can only be used to pass data through the API.
- Store and Pass Back values are stored in the Control Panel, returned on the transaction response object, and downloadable through Transaction or Vault Search. Search applies to the passed value, not the custom-field name.
- New custom-field definitions can be configured only in the Control Panel, not through the API, and the configuring user's role must have **Add/Edit Processing Options** permission. The creation flow assigns an API name used in code and a display name shown in transaction history and Vault records; exact naming constraints and steps remain at the raw locator.
- A permitted user can edit a field's display name or switch its type between Store and Pass Back and Pass Thru. Deletion has an additional eligibility boundary: the field must never have been used to collect customer or transaction data.
- Fraud Protection Advanced custom fields follow a separate setup route: they must be added through the Fraud Protection Advanced Dashboard. The final Control Panel view is described as showing all **ACTIVE** custom fields added through that Dashboard.
- The page also routes custom-field use to transaction creation, Vault customer creation or update, and 3D Secure authentication. Those linked API and guide authorities own the operation-specific request and response behavior; this article documents configuration and visibility rather than an API operation.

## Detail locators

- Custom-field purpose and linked use cases: introductory text and list, lines 16-24.
- Pass Thru versus Store and Pass Back identity and Control Panel/API placement: `## Custom field types`, lines 27-41.
- Store-and-pass-back response, download and value-versus-name search behavior: `### Store and Pass Back fields`, line 41.
- Control-Panel-only creation and required role permission: `## Creating a custom field`, line 46.
- API-name and display-name setup, naming limits, and transaction-history/Vault visibility: `## Creating a custom field`, lines 48-66.
- Editable properties and required role permission: `## Editing a custom field`, lines 69-85.
- Never-used deletion eligibility, permission and removal path: `## Deleting a custom field`, lines 88-105.
- Fraud Protection Advanced setup owner and ACTIVE-field Control Panel visibility: `## Viewing the custom fields created through Fraud Protection Advanced`, lines 108-122.

## Evidence boundary

> [!warning] Control Panel configuration is not an API setup operation
> This page says custom-field definitions cannot be created through the API even though configured fields can carry or return data through API operations. Preserve the role-permission requirement, the never-used deletion condition, and the separate Fraud Protection Advanced Dashboard/ACTIVE-field visibility wording. The 2026-09-16 snapshot is collected evidence, not proof of current support or account eligibility.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- API/SDK context: [[braintree-server-sdk]]
- Parent overview: [[source-braintree-control-panel-overview]]

## Related raw API references

- [[raw/braintree/articles/control-panel/users-roles/role-permissions-2026-09-16|Braintree Control Panel role permissions]] - navigation-only route for the linked Add/Edit Processing Options permission detail
- [[raw/braintree/articles/control-panel/search-2026-09-16|Braintree Control Panel search]] - navigation-only route for the linked Transaction and Vault Search behavior
- [[raw/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced-2026-09-16|Braintree Fraud Protection Advanced]] - navigation-only route for the linked fraud-tool behavior and Dashboard context
- [[raw/braintree/docs/reference/request/transaction/sale/node-2026-09-16|Braintree Node.js transaction sale request]] - navigation-only route for transaction custom-field use
- [[raw/braintree/docs/reference/request/customer/create/node-2026-09-16|Braintree Node.js customer create request]] - navigation-only route for Vault customer custom-field use
- [[raw/braintree/docs/reference/request/customer/update/node-2026-09-16|Braintree Node.js customer update request]] - navigation-only route for Vault customer custom-field updates

## Raw Sources

- [[raw/braintree/articles/control-panel/custom-fields-2026-09-16|Braintree Control Panel Custom Fields]] - complete collected article covering custom-field types, Control Panel configuration permissions, deletion eligibility, API visibility, and Fraud Protection Advanced field visibility
