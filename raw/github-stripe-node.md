<!-- Repo: https://github.com/stripe/stripe-node -->
<!-- Commit SHA: 1899375db06ae1e102a93637e193f8c9cb1de831 -->
<!-- Date reviewed: 2026-05-08 -->
<!-- Detail directory: raw/github-stripe-node/ -->
<!-- Files saved (read directly from these paths):
  raw/github-stripe-node/README.md
  raw/github-stripe-node/src/stripe.core.ts
  raw/github-stripe-node/src/Error.ts
  raw/github-stripe-node/src/Webhooks.ts
  raw/github-stripe-node/src/autoPagination.ts
  raw/github-stripe-node/src/StripeResource.ts
  raw/github-stripe-node/src/RequestSender.ts
  raw/github-stripe-node/src/ResourceNamespace.ts
  raw/github-stripe-node/src/Types.ts
  raw/github-stripe-node/src/shared.ts
  raw/github-stripe-node/src/resources/PaymentIntents.ts
  raw/github-stripe-node/src/resources/Checkout/Sessions.ts
  raw/github-stripe-node/examples/webhook-signing/README.md
  raw/github-stripe-node/examples/webhook-signing/express/main.ts
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from https://github.com/stripe/stripe-node at commit SHA 1899375db06ae1e102a93637e193f8c9cb1de831, then save any newly discovered files into raw/github-stripe-node/ preserving their repo-relative paths -->

# stripe-node — Official Stripe Node.js SDK

SDK version: 22.1.1
OpenAPI spec version: v2252

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-stripe-node/README.md` | Installation (npm/yarn/UMD), basic usage, async/await patterns, configuration, Node.js version requirements, TypeScript usage |
| `raw/github-stripe-node/src/stripe.core.ts` | Main Stripe client class, resource factory pattern, all resource registrations, SDK initialization options, event emission |
| `raw/github-stripe-node/src/Error.ts` | Full error taxonomy: StripeCardError, StripeRateLimitError, StripeAuthenticationError, StripeIdempotencyError, StripeInvalidRequestError, StripeAPIError, StripeConnectionError, OAuth errors |
| `raw/github-stripe-node/src/Webhooks.ts` | Webhook signature verification (sync/async), `constructEvent()`, `constructEventAsync()`, test header generation, clock skew tolerance |
| `raw/github-stripe-node/src/autoPagination.ts` | Pagination: V1Iterator with `autoPagingEach()` and `autoPagingToArray()`, handling `has_more` and `next_page` |
| `raw/github-stripe-node/src/StripeResource.ts` | Base resource class, request delegation, auto-pagination setup, V2 API coercion |
| `raw/github-stripe-node/src/RequestSender.ts` | HTTP request orchestration, retry logic with exponential backoff, idempotency key handling, telemetry headers, maxNetworkRetries, timeout |
| `raw/github-stripe-node/src/ResourceNamespace.ts` | Nested resource pattern (e.g., `stripe.issuing.cards`, `stripe.billing.invoicing`) |
| `raw/github-stripe-node/src/Types.ts` | RawErrorType enum, MethodSpec, BaseAddress, RequestAuthenticator, V2RuntimeSchema |
| `raw/github-stripe-node/src/shared.ts` | Metadata, Address, pagination parameter types (PaginationParams), recurring types |
| `raw/github-stripe-node/src/resources/PaymentIntents.ts` | Complete PaymentIntent resource: create, retrieve, update, list, confirm, capture, cancel, incrementAuthorization, applyCustomerBalance, verifyMicrodeposits, search |
| `raw/github-stripe-node/src/resources/Checkout/Sessions.ts` | Checkout Session resource: create, retrieve, update, list, expire, listLineItems; all session parameters and options |
| `raw/github-stripe-node/examples/webhook-signing/README.md` | Multi-framework webhook guide: Express, Koa, Next.js, NestJS; Stripe CLI setup, signature secret management |
| `raw/github-stripe-node/examples/webhook-signing/express/main.ts` | Complete Express webhook handler: raw body requirement, `stripe.webhooks.constructEvent()`, event type handling, error responses |
