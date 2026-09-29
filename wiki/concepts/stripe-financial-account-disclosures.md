---
title: "Stripe Financial Account Disclosures"
type: concept
category: technology
tags: [stripe, financial-accounts, treasury, react, disclosures]
---

## Scope

Financial Accounts disclosure rendering is distinct from checkout or payment confirmation. The retained `@stripe/react-stripe-js@6.12.0` evidence adds `TreasuryDisclosure` alongside the existing `FinancialAccountDisclosure`; it does not establish that one replaces the other or that an account is eligible.

## React Wrapper

Import `TreasuryDisclosure` from the root `@stripe/react-stripe-js` entrypoint. It accepts its own Stripe object/promise (or null for initial server rendering), optional `businessName` and `learnMoreLink`, and `onLoad`/`onError` callbacks. The wrapper calls the hosted runtime's `createTreasuryDisclosure` through an `any` cast and inserts the returned HTML element. No Elements provider is required by this implementation. See [[source-github-react-stripe-js]].

## Version 6.12.0 Limits

- `onError` receives returned error objects, not uncaught promise rejections or thrown failures.
- Disclosure creation has no post-await unmount guard or stale-request cancellation. Late completion can access a null container or overwrite newer content.
- Changing callback identities can rerun creation because callbacks are effect dependencies.
- The export does not verify hosted method availability, eligibility, disclosure wording, or compliance. These are static-code observations; upstream tests and live rendering were not executed.

## Sources

- [[source-github-react-stripe-js]] - exact implementation and version-qualified caveats.
- [[changelog-github-react-stripe-js]] - release history.
- [[stripe]] - company context.
