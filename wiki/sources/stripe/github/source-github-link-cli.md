---
title: "GitHub: stripe/link-cli"
type: source
date_ingested: 2026-08-15
date_updated: 2026-08-15
original_format: github-repo
raw_files:
  - "github/stripe/link-cli/snapshots/2026-08-15-d540389/manifest.json"
tags: [stripe, link, link-cli, agentic-commerce, virtual-card, shared-payment-token, machine-payments, mcp, github-repository]
---

## Overview

`stripe/link-cli` is Stripe's agent-facing command-line and MCP tool for obtaining user-approved, one-time payment credentials from a consumer's Link wallet. This initial full ingest records package-qualified release `@stripe/link-cli@0.13.0`, exact SHA `d540389e030d0f475a6b85cd64ccaf978ff498ac`, released on 2026-08-13 and collected on 2026-08-15.

Repository: <https://github.com/stripe/link-cli>

## Evidence Boundary

- Findings apply to retained package release `@stripe/link-cli@0.13.0`, not an unqualified latest Link product.
- The capsule retains 107 checkout-relevant files from the CLI, its private internal SDK, and two agent skill definitions. It excludes tests and fixtures and is not the complete upstream repository.
- Link CLI acts for a Link consumer and their agent. It is not a merchant-side checkout SDK and does not replace Stripe's canonical seller API documentation.
- `@stripe/link-sdk` is marked private in this repository. Its retained source explains the CLI's implementation but does not establish a supported public SDK contract.
- Web Bot Auth source exists, but its CLI registration is commented out at this SHA. It must not be presented as an exposed `0.13.0` command.
- The README says the product is currently limited to US Link accounts. Future geographic availability requires newer evidence.

## Grounding Excerpts

> "Link CLI lets agents get secure, one-time-use payment credentials from a Link wallet to complete purchases on your behalf — without storing your real card details."
>
> `raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/README.md:3`

> "The issued card works anywhere, and is not restricted to Link-enabled sellers or sellers that use Stripe."
>
> `raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/README.md:7`

> "Anyone who can reach the port can use this CLI's authenticated Link session"
>
> `raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/README.md:71`

> "Polling exits successfully only after the request reaches a terminal status such as `approved`, `denied`, `expired`, or `canceled`."
>
> `raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/README.md:228`

> "The SPT is one-time-use — if payment fails, create a new spend request."
>
> `raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/README.md:324`

## Package and Architecture

The public package is `@stripe/link-cli@0.13.0`. The repository workspace declares Node.js 22 or newer and uses pnpm; the published CLI manifest itself has no `engines` field. The CLI package is published, while workspace package `@stripe/link-sdk@1.0.0` is private and consumed internally during the build.

The command tree uses `incur` for CLI and MCP command definitions and Ink/React for interactive terminal flows. `ResourceFactory` supplies authentication and SDK resources for spend requests, payment methods, shipping addresses, user information, reports, balances, sources, and transactions. Agent-mode commands use structured output and `_next` instructions for approval and polling handoffs.

The CLI supports:

- standalone interactive and structured command output;
- local stdio MCP through `--mcp`;
- HTTP MCP through `serve`;
- guided `onboard` and `demo` flows for virtual cards and SPT-based MPP payments;
- optional outcome reports for success, blocked, and abandoned purchase attempts.

## Authentication and Authorization

Authentication uses an OAuth device-code flow against `login.link.com`. The default scopes are `userinfo:read` and `payment_methods.agentic`; callers can request additional scopes and structured authorization details.

`auth login` refuses to replace a usable session implicitly. `auth upgrade` instead merges requested scopes and action-based authorization details with the current grant. The current session remains usable during the pending upgrade, and the old refresh token is revoked only after replacement credentials are stored. An abandoned upgrade therefore does not destroy the prior working session.

Access tokens are refreshed with a 60-second expiry buffer. SDK resources retry once after a `401` by forcing token refresh. This authentication retry is not a business-operation retry guarantee and must not be generalized to payment success.

Credentials can come from owner-only local storage or `LINK_ACCESS_TOKEN` and `LINK_REFRESH_TOKEN`. `LINK_NO_REFRESH` makes expiry fail rather than refresh. Base URLs, auth file, and HTTP proxy are configurable through documented environment variables.

## Payment Path Selection

Link CLI exposes two credential types plus one merchant-bound execution mode.

### Virtual Card

The default `card` credential creates a one-time virtual PAN for a normal checkout form. A regular request requires merchant name, merchant URL, amount, currency, and at least 100 characters of purchase context; payment method ID is optional and falls back to the default or first eligible method.

After approval, `spend-request retrieve --include card` can return number, CVC, expiry, billing address, and validity. The README says the card can work beyond Stripe or Link-enabled sellers. That statement establishes intended credential reach, not a guarantee that every merchant, card network rule, fraud system, or checkout will accept it.

### Shared Payment Token and MPP

For an HTTP `402` challenge with Stripe `charge` or `session` intent, `mpp decode` validates the challenge and extracts its network ID. `mpp pay` can:

1. probe the target URL;
2. parse the Stripe challenge and amount;
3. choose a Link payment method;
4. create an approval-gated spend request with `credential_type=shared_payment_token`;
5. poll for approval;
6. retrieve the SPT; and
7. retry the request with an MPP authorization credential.

An already approved SPT spend request can be supplied by ID. The implementation requires that request to be approved, typed as `shared_payment_token`, and contain the token. An SPT is one-time use; failure requires a new spend request rather than replaying the credential. Merchant-controlled response headers and bodies are sanitized for terminal output but remain untrusted data.

### Link Pay Token

Link Pay Token is an execution mode of the card flow, not a third credential type. Before creating an LPT-bound request, a browser agent must locate and enable the checkout's AI-agent steering block and confirm that `input[name="link_pay_token"]` and `data-stripe-merchant-account` appear in the same Stripe frame.

The request uses `execution_method=link_pay_token` and the DOM-derived Stripe account ID. Merchant name and URL, SPT network ID, delegated `approve`, and test mode are rejected for this path. Link resolves canonical merchant identity for approval. After approval, the agent retrieves the LPT immediately and injects it into the same checkout surface. The documented validity is up to 30 minutes or until spend-request expiry; missing DOM markers require fallback to a normal virtual card request.

## Spend-Request Lifecycle and Limits

The resource supports list, create, update, request approval, retrieve, and cancel operations. Creation can carry line items, totals, metadata, test mode, and structured delegated approval details. The delegated create path uses `/spend_requests/create_delegated` when `approve` is selected.

Statuses include `created`, `pending_approval`, `approved`, `denied`, `expired`, `succeeded`, `failed`, `canceled`, and `requires_action`. `requires_action` includes a typed next action and resolution:

- `auto_resume`, currently used for 3D Secure, keeps polling the same request after user verification;
- other resolutions stop polling and direct the caller to complete the action and create a new request.

Agent-mode polling yields only changed results. Exhausting timeout or attempts before terminal state returns non-zero `POLLING_TIMEOUT`, preventing a pending request from being mistaken for success.

Documented baseline limits include:

| Constraint | `@stripe/link-cli@0.13.0` |
| --- | --- |
| Maximum request amount | 500,000 cents / $5,000 USD equivalent as documented |
| Approval window | 10 minutes |
| Card or SPT validity | 12 hours from request creation |
| Daily spend | $5,000 |
| Rolling 30-day spend | $20,000 |
| Concurrent active / approved requests | 30 / 10 |
| Creation rate | 50 per hour; 200 per 60 days |

These are repository-documented Link CLI limits, not general Stripe account or merchant processing limits.

## Financial Insights in `0.13.0`

Release `0.13.0` exposes beta `balances`, `sources`, and `transactions` commands and ships a financial-insights skill. The commands are read-only and use narrowly scoped source actions:

- `read_balances` for account balances;
- `read_source_details` for connected source metadata;
- `read_link_transactions` for Link-originated activity;
- `read_external_transactions` for connected-account activity.

Balances, sources, and transactions support cursor pagination. Transactions can filter by date, category, origin, and source. The skill requires currency-aware minor-unit formatting, preserves separate currencies, and limits retrieval to the data needed for the user's question.

> [!warning] Contradiction
> The package manifest, release tag, and release record identify `@stripe/link-cli@0.13.0`, and the `0.13.0` notes say the financial-insights skill ships in this release. However, both retained skill frontmatter blocks still declare `version: 0.11.0`. Treat their workflow text as content retained at the `0.13.0` repository SHA, but do not present the embedded skill version as synchronized package metadata.

## Credential and Server Security

Local auth storage contains access tokens, refresh tokens, and pending device codes and uses mode `0600`. Full card output can be written to a `0600` file; the writer uses exclusive creation, rejects a final-path symbolic link, and requires `--force` before replacing a regular file.

The resource factory recursively strips ANSI escape sequences and control characters from SDK responses before CLI rendering or agent formatting. MPP output applies the same treatment to attacker-controlled HTTP response headers and body.

The HTTP MCP server binds to `127.0.0.1` by default, permits only `/mcp` and GET skill-discovery routes, and limits browser origins to loopback. Binding another interface prints a warning because any reachable caller can act through the authenticated Link session. This is a network trust boundary, not multi-tenant authentication.

## Release-Specific Change

The exact `0.13.0` release notes contain two changes:

- expose `balances`, `sources`, and `transactions` in the CLI and ship the financial-insights skill;
- surface duplicate spend-request error messaging in interactive mode.

The wider authentication, payment, lifecycle, MCP, and security behavior above is an initial baseline and must not be attributed as newly introduced by `0.13.0`.

## Related

- Company: [[stripe]]
- Concepts: [[stripe-link-cli]], [[stripe-shared-payment-tokens]], [[stripe-machine-payments]], [[stripe-agentic-commerce]], [[agentic-commerce]]
- History: [[changelog-github-link-cli]]

## Raw Sources

- [Snapshot manifest](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/manifest.json) — exact-SHA capsule inventory and hashes
- [Release record](../../../../raw/github/stripe/link-cli/releases/link-cli/0.13.0/2026-08-15/manifest.json) — package-qualified tag, SHA, and release date
- [Release notes](../../../../raw/github/stripe/link-cli/releases/link-cli/0.13.0/2026-08-15/release-notes.md) — exact `0.13.0` changes
- [README](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/README.md) — product scope, commands, payment paths, limits, and security warnings
- [CLI entrypoint](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/packages/cli/src/cli.tsx) — exposed command tree and disabled Web Bot Auth registration
- [Authentication command](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/packages/cli/src/commands/auth/index.tsx) — login, upgrade, polling, token replacement, and logout
- [Spend-request command](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/packages/cli/src/commands/spend-request/index.tsx) — validation, lifecycle, polling, output, and action handling
- [MPP payment implementation](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/packages/cli/src/commands/mpp/pay.tsx) — challenge, SPT, approval, and payment retry flow
- [HTTP MCP server](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/packages/cli/src/commands/serve/index.ts) — binding, route, and origin controls
- [Resource factory](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/packages/cli/src/utils/resource-factory.ts) — SDK resource construction and output sanitization boundary
- [Credential writer](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/packages/cli/src/utils/credential-output.ts) — card-file permissions and path handling
- [SDK spend-request resource](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/packages/sdk/src/resources/spend-request.ts) — endpoint operations, normalization, and authentication retry
- [SDK storage](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/packages/sdk/src/utils/storage.ts) — token persistence, expiry, and permissions
- [Payment credential skill](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/skills/create-payment-credential/SKILL.md) — agent workflow and payment safety boundaries
- [Financial insights skill](../../../../raw/github/stripe/link-cli/snapshots/2026-08-15-d540389/files/skills/financial-insights/SKILL.md) — source actions, read-only commands, pagination, and interpretation rules
