---
title: "Braintree Amex Express Checkout Configuration"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/amex-express-checkout/configuration"
raw_files:
  - "braintree/docs/guides/amex-express-checkout/configuration-2026-09-16.md"
tags: [braintree, amex-express-checkout, configuration, control-panel, legacy]
---

## Overview

This 2026-09-16 Braintree website snapshot is an unversioned configuration page for legacy Amex Express Checkout. It routes a merchant through Control Panel enablement and signup, then identifies the returned client credentials needed to configure the Amex Express Checkout tag on a checkout page. The page also directs merchants to repeat the configuration in their sandbox account. See [[braintree]] and [[braintree-payment-methods]].

## Key takeaways

- The configuration route begins in the Braintree Control Panel under **Processing** and **Payment Methods**, where the merchant selects **Enable** for Amex Express Checkout, completes the signup form and submits it.
- After submission, the page says the merchant is redirected to a configuration page containing `client_id` and `client_key` values for the Amex Express Checkout tag. Credential values are account-specific configuration material and are not reproduced here.
- Sandbox testing requires following the same enablement steps in the merchant's sandbox account; completing either set of steps is not established by this documentation snapshot.

> [!warning] Replacement and current-configuration tension
> The same page says Amex Express Checkout has been replaced by Visa Secure Remote Commerce (SRC) and directs prior users to integrate with SRC, while still using current-tense language for enabling and configuring Amex Express Checkout. Its SRC direction is itself qualified as a limited release for eligible merchants, subject to API change and access request. The page names Android v2, iOS v4 and JavaScript v3 only as the Client SDK generations in which SRC was introduced; it does not provide an SDK integration or prove that this Control Panel path remains available. [[braintree-payment-methods]] separately preserves the unresolved SRC current-availability versus dated end-of-support conflict.

## Scope and evidence boundary

This stored configuration page establishes the documented merchant-Control-Panel action, credential purpose and separate sandbox-account step as of its capture date. It does not establish present Amex or SRC availability, merchant eligibility or enablement, usable credentials, exact SDK/runtime behavior, successful migration, or payment execution.

## Detail locators

- Replacement by SRC, limited-release eligible-merchant scope, API-change warning, introducing Client SDK generations and access-request route: `# Configuration > AVAILABILITY`, raw lines 17-18.
- Control Panel prerequisite and navigation through **Processing** and **Payment Methods** to the Amex Express Checkout **Enable** action: `## Enabling Amex Express Checkout`, raw lines 20-29.
- Signup-form completion and submission: `## Enabling Amex Express Checkout`, raw lines 30-31.
- Redirected configuration page, `client_id` and `client_key` purpose, checkout-page tag scope and separate sandbox-account instruction: raw lines 33-35.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Product overview and replaced-versus-currently-available tension: [[source-braintree-docs-guides-amex-express-checkout-overview]]

## Raw Sources

- [[raw/braintree/docs/guides/amex-express-checkout/configuration-2026-09-16|Braintree Amex Express Checkout configuration]] - complete collected snapshot for the replacement notice, Control Panel enablement, returned client-credential purpose and sandbox-account step
