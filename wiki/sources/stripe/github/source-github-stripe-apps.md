---
title: "GitHub: stripe/stripe-apps"
type: source
date_ingested: 2026-08-28
date_updated: 2026-08-28
original_format: github-repo
raw_files:
  - "github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/manifest.json"
tags: [stripe, stripe-apps, dashboard, ui-extensions, app-manifest, app-marketplace, github-repository]
---

## Overview

`stripe/stripe-apps` provides Stripe App manifest schemas, developer resources, and examples for embedding custom experiences in the Stripe Dashboard. This initial full ingest records exact `main` commit `9b14b71be496ca299401b3303b572856fd19baf4`, committed on 2026-08-21 and collected on 2026-08-28.

Repository: <https://github.com/stripe/stripe-apps>

## Evidence Boundary

- This is a commit-tracked developer-platform repository. It has no retained release tags, while `schema/package.json` declares placeholder version `0.0.0`; neither provides a semantic repository release identity.
- The root changelog delegates UI SDK history to the independently versioned `@stripe/ui-extension-sdk` npm package. SDK release behavior must be collected under its own package-qualified evidence before attribution.
- The retained 72-file capsule contains root guidance, three manifest schemas, and the complete current `examples/full-page` implementation. Tests, fixtures, lockfiles, generated/decorative assets, and workflows are outside this baseline.
- Payment-related permission names are schema vocabulary. Their presence does not prove a Checkout integration, merchant entitlement, regional availability, or API approval.
- The Pizzazz Loyalty example is fully mocked. It contains no live Stripe API request, payment confirmation, webhook, Checkout Session, or PaymentIntent lifecycle.

## Stripe App Model

The root README defines Stripe Apps as a way to embed custom user experiences directly in the Stripe Dashboard and orchestrate the Stripe API. A standard app manifest can describe:

| Area | Retained schema behavior |
| --- | --- |
| Identity | app ID, developer-defined version, display name, and PNG icon |
| Permissions | purpose-qualified Stripe API permissions, including payment, billing, customer, Connect, and other resource families |
| Dashboard UI | component names mapped to supported Dashboard viewports |
| Network policy | `connect-src`, `image-src`, and an installation-facing purpose statement |
| Installation | post-install action and allowed redirect URIs |
| Distribution | `public` or `private` |
| API access | `restricted_api_key`, `oauth`, or `platform` |
| Environment | boolean sandbox-install compatibility |
| Constants | custom values passed to UI views through context props |

The local-development schema can extend a base `stripe-app.json` and override the same identity, permission, distribution, API-access, sandbox, UI, CSP, redirect, and constants fields.

## Extension Manifest Schema

The retained file named `stripe-app.schema.yaml` contains JSON syntax and defines a distinct "Stripe App Manifest Extension" model. It requires top-level app identity plus an `extensions` array. Each extension declares its own ID, name, interface ID, semantic version, purpose-qualified permissions, and implemented methods.

At this commit, the retained method schema exposes `custom_workflow_action_run`, with `remote_function` or `script` implementation types, managed-resource identifiers, and optional custom input/UI schema paths. This extension model should not be collapsed into the ordinary `stripe-app.json` model.

## Full-Page Example Architecture

The `examples/full-page` application is a React and TypeScript Stripe Dashboard UI extension named Pizzazz Loyalty. It requires Node.js 18+, pnpm, Stripe CLI with the Apps plugin, `@stripe/ui-extension-sdk` `9.2.0`, React Query, and React Router support from the Stripe navigation package. The package also lists `stripe` `^17.7.0`, but retained source does not import or call it.

Its three registered views are:

- `FullPage` at `stripe.dashboard.fullpage`;
- `AppSettings` at `settings`;
- `DrawerDefaultView` at `stripe.dashboard.home.overview`.

`FullPage` wraps `AppRouter`; route definitions cover overview/member/reward/activity pages and retain a legacy `/customers/:id` redirect to `/members/:id`. The settings view edits loyalty-program name, points-per-dollar, currency, and engagement windows. The drawer links into the full-page application.

## UI and State Patterns

The example demonstrates:

- full-page tabs, overview modules, charts, detail pages, data tables, filters, row actions, drawers, settings, and queued toasts;
- typed in-app navigation with route parameters and a legacy-route redirect;
- role-gated destructive reward actions using the Dashboard user's `admin` role;
- React Query providers, query keys, composite cache synchronization, loading/error states, and mutation callbacks;
- content rendered through Stripe UI-extension components rather than arbitrary browser DOM components.

These are implementation examples, not guarantees that every component, viewport, or role behavior applies to every installed app or SDK release.

## Mock-Only Data Boundary

All members, rewards, transactions, trends, program settings, order IDs, and dates come from checked-in mock data. Fetch functions return copied arrays after a fixed simulated delay, and mutations update the React Query cache in memory. "Grant points", member edits, reward changes, settings saves, and archive actions do not call a merchant backend or Stripe.

The example's transaction and order labels are presentation data. They do not establish Stripe Order objects, payment settlement, refund behavior, webhook fulfillment, or loyalty-account persistence.

## Manifest and Example Drift

> [!warning] Contradiction
> The checked-in `examples/full-page/stripe-app.json` does not satisfy the retained standard JSON schema literally. The schema requires `permissions`, but the example omits it. The example uses `stripe.dashboard.fullpage`, which is absent from the retained viewport enum, and declares a `modal` post-install action while the retained schema permits onboarding, settings, or external actions. This likely reflects repository evolution across different tooling surfaces, but the capsule does not prove which definition is authoritative for every environment.

The example additionally sets private distribution, platform API access, and sandbox compatibility. Those declarations describe example configuration only; they do not establish marketplace approval or access for another app.

## Development, Publishing, and Security

The documented local workflow is `pnpm install`, followed by `pnpm start` to run `stripe apps start`, with `pnpm build` for production output. The root README links a temporary workaround for Dashboard preview-mode issues, so local preview should not be assumed problem-free at this commit.

Public marketplace publication is described as requiring separate review requirements, listing guidelines, and design best practices. The repository does not prove that a particular app passed those gates.

Security vulnerabilities should be reported through Stripe's vulnerability disclosure and reward program rather than public GitHub issues or pull requests.

## Query Guidance

Use this source for commit-qualified questions about Stripe App manifests, Dashboard UI-extension structure, the retained full-page example, local development commands, and repository-level drift. Search [[changelog-github-stripe-apps]] for later commit transitions. For actual Checkout or payment behavior, use the relevant Stripe payment source instead of inferring behavior from permission enums or mock transaction labels.

## Related

- Company: [[stripe]]
- Concept: [[stripe-apps]]
- History: [[changelog-github-stripe-apps]]

## Raw Sources

- [Snapshot manifest](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/manifest.json) — exact-SHA capsule inventory and hashes
- [Root README](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/README.md) — platform purpose, resources, preview warning, and publishing boundary
- [Repository changelog](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/CHANGELOG.md) — delegated UI-extension SDK changelog link
- [Standard manifest schema](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/schema/stripe-app.schema.json) — ordinary app-manifest fields and enums
- [Local manifest schema](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/schema/stripe-app-local.schema.json) — local extension and override model
- [Extension manifest schema](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/schema/stripe-app.schema.yaml) — distinct extension interface and method model
- [Full-page example README](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/examples/full-page/README.md) — prerequisites and commands
- [Full-page package manifest](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/examples/full-page/package.json) — dependency and script versions
- [Example app manifest](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/examples/full-page/stripe-app.json) — current example views and installation configuration
- [Mock API](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/examples/full-page/src/data/api.ts) — local fetch boundary
- [Mock network](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/examples/full-page/src/data/network.ts) — simulated delay
- [Cache mutations](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/examples/full-page/src/data/cache-mutations.ts) — in-memory update behavior
- [Application routes](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/examples/full-page/src/routes.tsx) — typed page navigation and legacy redirect
- [Application providers](../../../../raw/github/stripe/stripe-apps/snapshots/2026-08-28-9b14b71/files/examples/full-page/src/providers/AppProviders.tsx) — navigation and React Query wiring
