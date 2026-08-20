---
title: "Stripe Link CLI"
type: concept
category: technology
tags: [stripe, link, link-cli, agentic-commerce, virtual-card, shared-payment-token, machine-payments, mcp]
---

## Definition

Stripe Link CLI is an agent-facing command-line and MCP tool that obtains user-approved, one-time payment credentials from a consumer's Link wallet. At the retained `@stripe/link-cli@0.13.0` baseline, it is available only to US Link accounts and is distinct from [[stripe-cli]], Stripe's merchant developer and operations tool.

## Payment Paths

- **Virtual card:** the default spend-request credential is a one-time PAN for standard web checkout forms. The repository states that the card is not restricted to Link-enabled or Stripe sellers.
- **Shared Payment Token (SPT):** for a seller returning an HTTP `402` Stripe MPP challenge, `mpp pay` extracts the network ID, creates an approval-gated spend request, retrieves the one-time SPT, signs the challenge, and retries the request. A failed payment requires a new SPT and spend request.
- **Link Pay Token (LPT):** LPT is a merchant-bound execution mode for the card flow, not a third credential type. An agent must inspect a Stripe checkout frame, enable its AI-agent steering control, and confirm both the `link_pay_token` input and DOM-provided Stripe account ID before creating the request. LPT does not support test mode and is valid for up to 30 minutes or until the spend request expires.

## Spend-Request Lifecycle

A regular request records the payment method, amount, currency, merchant identity, purchase context, line items, totals, metadata, and optional delegated approval details. The lifecycle supports create, update, request approval, retrieve, and cancel operations.

The retained CLI enforces a 100-character minimum purchase context and a maximum request amount of 500,000 cents. Approval is required before credentials are exposed. `requires_action` with `auto_resume` continues polling through 3D Secure; other resolutions require user action followed by a new spend request. Polling limits return a non-zero `POLLING_TIMEOUT` instead of treating a pending request as complete.

## Authentication and Data Access

Device authorization connects an identifiable agent or application to a Link account. `auth upgrade` requests a superset of current scopes and authorization details while keeping the existing session usable until the replacement is approved.

Version `0.13.0` exposes beta `balances`, `sources`, and `transactions` commands and ships a financial-insights agent skill. These read-only commands require narrowly requested source actions such as `read_balances`, `read_source_details`, `read_link_transactions`, and `read_external_transactions`.

## Agent and Security Boundaries

- The CLI supports standalone structured output, local stdio MCP, and an HTTP MCP endpoint. HTTP mode binds to `127.0.0.1` by default; anyone who can reach a non-loopback binding can use the CLI's authenticated Link session.
- Stored OAuth credentials and pending device codes use owner-only `0600` permissions. Full card output can be written to a `0600` file with exclusive creation and final-path symlink rejection.
- Server-controlled strings are sanitized before terminal or agent output. MPP response bodies and headers remain untrusted merchant input.
- The repository contains a private `@stripe/link-sdk` implementation used by the CLI. Its source is evidence for CLI behavior, not a promise that merchants can install a supported public SDK.
- The retained web-bot-auth implementation is not registered in the CLI command tree at this baseline, so it is not treated as an exposed `0.13.0` command.

## Version Boundary

This concept is grounded in package-qualified release `@stripe/link-cli@0.13.0` at exact SHA `d540389e030d0f475a6b85cd64ccaf978ff498ac`. The release specifically exposes financial-insight commands and improves duplicate spend-request messaging; the broader behavior is the initial repository baseline, not functionality introduced entirely in `0.13.0`.

## Related

- Company: [[stripe]]
- Concepts: [[stripe-shared-payment-tokens]], [[stripe-machine-payments]], [[stripe-agentic-commerce]], [[agentic-commerce]]
- Source: [[source-github-link-cli]]
- History: [[changelog-github-link-cli]]
