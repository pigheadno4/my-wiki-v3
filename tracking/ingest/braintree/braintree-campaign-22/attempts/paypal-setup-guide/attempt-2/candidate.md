---
title: "Braintree PayPal Setup Guide"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/setup-guide"
raw_files:
  - "braintree/articles/guides/payment-methods/paypal/setup-guide-2026-09-16.md"
tags: [braintree, paypal, payment-methods, setup, control-panel, currencies]
---

## Overview

This collected Braintree article is the setup route for adding PayPal after confirming that the merchant account is eligible to accept PayPal transactions. It separates the required account-linking sequence and the conditional requirements for accepting multiple currencies from recommendations to enable PayPal disputes, enable Settlement Withdrawal, and block eChecks before authorization; it is not a general PayPal account-configuration guide or an SDK implementation specification.

## Key takeaways

- The article's required sequence is to obtain a verified PayPal Business Account, enter that account's credentials in the Braintree Control Panel, and then add PayPal through the linked Braintree developer guide. Eligibility confirmation comes before this sequence.
- Linking PayPal credentials in the Braintree Control Panel enables the payment method in production, and the article states that only one PayPal account can be linked to a Braintree gateway. Newly approved Braintree accounts may take a few business days to expose the credential option.
- A REST API app may be created in the PayPal Apps Control Panel after linking. The article says Braintree uses it to interact with the PayPal API, PayPal transactions cannot be processed through the Braintree account without it, and recommends never deleting it.
- The article says Braintree does not support eCheck transactions: an attempted eCheck authorization may succeed, but the associated transaction will be automatically voided. It recommends blocking eChecks before authorization in PayPal payment-receiving preferences.
- PayPal multi-currency acceptance requires a Braintree merchant account for each accepted currency, PayPal account configuration for foreign-currency payments, and selection of the applicable Braintree merchant account during processing. PayPal may assess conversion and cross-border fees depending on account setup.

## Evidence boundaries

> [!warning] Required versus recommended setup
> The verified PayPal Business Account, Braintree Control Panel credential link and integration step are the article's required sequence. PayPal-dispute enablement and Settlement Withdrawal are recommendations, not stated prerequisites. Use `## Required steps` and `## Recommended setup options` in the raw page to keep that distinction intact.

> [!warning] Account-link and REST app dependency
> The one-PayPal-account-per-gateway statement is scoped to the Braintree gateway described by this article. The article recommends not deleting the generated REST API app and says PayPal transactions through the Braintree account cannot be processed without it.

> [!warning] eCheck and foreign-currency tradeoffs
> A successful eCheck authorization does not mean Braintree supports the resulting transaction; the article says it will be automatically voided. Blocking all foreign-currency payments can avoid additional fees but also prevents sales to customers who do not use the account currency, and PayPal may still assess conversion and cross-border fees depending on account setup.

## Detail locators

- Eligibility-first setup sequence: `# Setup Guide`, lines 16-21.
- PayPal Business Account creation or upgrade and required personal-information verification: `### Sign up for a PayPal Business Account`, lines 27-38.
- Production credential link, one-account-per-gateway limit and Control Panel navigation: `### Enter your PayPal credentials in the Braintree Control Panel`, lines 43-59.
- Generated REST API app purpose and do-not-delete recommendation: `#### REST API app`, lines 64-66.
- Recommended dispute and Settlement Withdrawal options: `## Recommended setup options`, lines 69-79.
- Unsupported eCheck result and recommended pre-authorization blocking: `### eCheck payments`, lines 82-86.
- PayPal multi-currency prerequisites, merchant-account selection, blocking tradeoff and possible fees: `### Foreign currencies` through `#### Avoiding conversion and cross border fees`, lines 89-106.
- Account-change and support-contact routes: `## Contacting PayPal support`, lines 111-115.

## Related

- Company: [[braintree]]
- Main payment-method route: [[braintree-payment-methods]]
- Production account-linking context: [[paypal-braintree-integration]]
- Control Panel administration: [[braintree-control-panel]]
- Currency setup context: [[braintree-currencies]]

## Related raw API references

- [[raw/braintree/articles/guides/payment-methods/paypal/overview-2026-09-16|Braintree PayPal overview]] - unread navigation-only authority linked by this article for merchant-account eligibility; it was not used as factual evidence here, so no eligibility conditions are inferred from it

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/paypal/setup-guide-2026-09-16|Braintree PayPal Setup Guide]] - complete collected article covering the eligibility-first setup sequence, account linking, REST app dependency and optional settings
