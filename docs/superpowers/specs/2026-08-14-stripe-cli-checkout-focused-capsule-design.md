# Stripe CLI Checkout-Focused Capsule Design

**Date:** 2026-08-14
**Status:** Approved
**Repository:** `stripe/stripe-cli`
**Package:** `stripe-cli`

## Purpose

Collect the official Stripe CLI as immutable, package-qualified GitHub evidence for checkout development, local webhook handling, event simulation, and version queries. The first ingest must explain how developers authenticate the CLI, issue API requests, listen for and forward webhook events, and trigger checkout-relevant event fixtures.

The CLI spans many Stripe product domains. This capsule deliberately preserves deep evidence for Checkout, PaymentIntents, SetupIntents, invoices, customer subscriptions, and subscription schedules while leaving unrelated API resources and triggers outside the baseline. A later query may use an approved supplement when the retained evidence is insufficient.

## Approved Evidence Boundary

Design discovery found `stripe-cli@1.50.0` as the highest stable semantic tag and exact tag commit `a6f40658b99e4142fd63b2e4b560aa9c7ae337b1`. The default branch had moved to `4181fb7009b4c9095841534addced542e8b22363` on 2026-08-13. Collection must resolve and verify the selected stable tag again at run time; default-branch code is discovery context, not accepted release evidence.

### Included

- `README.md`, `ARCHITECTURE.md`, `LICENSE`, and `go.mod` for product scope, architecture, provenance, and dependency context.
- `cmd/stripe/main.go` and bounded `pkg/cmd/` files for root command wiring, authentication, configuration, direct API requests, `listen`, `trigger`, and fixture execution.
- Runtime source under `pkg/config/`, `pkg/login/`, `pkg/proxy/`, `pkg/requests/`, `pkg/stripe/`, and `pkg/websocket/`, excluding tests.
- `pkg/fixtures/fixtures.go` and `pkg/fixtures/triggers.go` for fixture parsing and dispatch behavior.
- Exact trigger JSON files for `checkout.session`, `payment_intent`, `setup_intent`, `invoice`, `customer.subscription`, and `subscription_schedule` events.
- Bounded RPC service implementations and `.proto` definitions used by listen, trigger, fixture, event-resend, and webhook-endpoint behavior.

The selected `pkg/fixtures/triggers/*.json` files are executable CLI product behavior, not ordinary repository test fixtures. They remain eligible even though tests and unrelated fixtures are excluded.

### Excluded

- Unit, integration, and canary tests;
- generated protobuf Go files and generated API resource-command trees;
- triggers outside the approved checkout and recurring-payment families;
- Terminal reader implementation, plugins, agent tooling, samples, sandbox tooling, and distribution packages;
- CI, release automation, editor files, binary assets, lockfiles, and local environment files.

## Registry Design

Enable the existing tier-2 monthly registry entry and add one stable major-version track:

```toml
[[repos.version_tracks]]
selector = "package:stripe-cli@1"
backfill = "latest-stable"
future = "all-stable"
include_prerelease = false
pinned_versions = ["1.50.0"]
```

Use one tagged-source capsule:

```toml
[[repos.capsules]]
id = "stripe-cli-checkout-source"
adapter = "tagged-tree-v1"
focus_packages = ["stripe-cli"]
dependency_scope = "configured-repository-paths"
changed_path_policy = "policy-bounded"
default_required_roots = [
  "pkg/config",
  "pkg/login",
  "pkg/proxy",
  "pkg/requests",
  "pkg/stripe",
  "pkg/websocket",
]
default_generated_target_paths = []
include_paths = [
  "README.md",
  "ARCHITECTURE.md",
  "LICENSE",
  "go.mod",
  "cmd/stripe/main.go",
  "pkg/cmd/root.go",
  "pkg/cmd/config.go",
  "pkg/cmd/login.go",
  "pkg/cmd/logout.go",
  "pkg/cmd/switch.go",
  "pkg/cmd/whoami.go",
  "pkg/cmd/get.go",
  "pkg/cmd/post.go",
  "pkg/cmd/delete.go",
  "pkg/cmd/http.go",
  "pkg/cmd/listen.go",
  "pkg/cmd/trigger.go",
  "pkg/cmd/fixtures.go",
  "pkg/cmd/resources.go",
  "pkg/fixtures/fixtures.go",
  "pkg/fixtures/triggers.go",
  "pkg/rpcservice/events_resend.go",
  "pkg/rpcservice/fixtures.go",
  "pkg/rpcservice/listen.go",
  "pkg/rpcservice/trigger.go",
  "pkg/rpcservice/triggers_list.go",
  "pkg/rpcservice/webhook_endpoint_create.go",
  "pkg/rpcservice/webhook_endpoints_list.go",
  "rpc/common.proto",
  "rpc/events_resend.proto",
  "rpc/fixtures.proto",
  "rpc/listen.proto",
  "rpc/trigger.proto",
  "rpc/triggers_list.proto",
  "rpc/webhook_endpoint_create.proto",
  "rpc/webhook_endpoints_list.proto",
  "pkg/fixtures/triggers/checkout.session.async_payment_failed.json",
  "pkg/fixtures/triggers/checkout.session.async_payment_succeeded.json",
  "pkg/fixtures/triggers/checkout.session.completed.json",
  "pkg/fixtures/triggers/checkout.session.expired.json",
  "pkg/fixtures/triggers/customer.subscription.created.json",
  "pkg/fixtures/triggers/customer.subscription.deleted.json",
  "pkg/fixtures/triggers/customer.subscription.paused.json",
  "pkg/fixtures/triggers/customer.subscription.trial_will_end.json",
  "pkg/fixtures/triggers/customer.subscription.updated.json",
  "pkg/fixtures/triggers/invoice.created.json",
  "pkg/fixtures/triggers/invoice.deleted.json",
  "pkg/fixtures/triggers/invoice.finalized.json",
  "pkg/fixtures/triggers/invoice.marked_uncollectible.json",
  "pkg/fixtures/triggers/invoice.paid.json",
  "pkg/fixtures/triggers/invoice.payment_action_required.json",
  "pkg/fixtures/triggers/invoice.payment_failed.json",
  "pkg/fixtures/triggers/invoice.sent.json",
  "pkg/fixtures/triggers/invoice.updated.json",
  "pkg/fixtures/triggers/invoice.voided.json",
  "pkg/fixtures/triggers/payment_intent.amount_capturable_updated.json",
  "pkg/fixtures/triggers/payment_intent.canceled.json",
  "pkg/fixtures/triggers/payment_intent.created.json",
  "pkg/fixtures/triggers/payment_intent.partially_funded.json",
  "pkg/fixtures/triggers/payment_intent.payment_failed.json",
  "pkg/fixtures/triggers/payment_intent.processing.json",
  "pkg/fixtures/triggers/payment_intent.requires_action.json",
  "pkg/fixtures/triggers/payment_intent.succeeded.json",
  "pkg/fixtures/triggers/setup_intent.canceled.json",
  "pkg/fixtures/triggers/setup_intent.created.json",
  "pkg/fixtures/triggers/setup_intent.requires_action.json",
  "pkg/fixtures/triggers/setup_intent.setup_failed.json",
  "pkg/fixtures/triggers/setup_intent.succeeded.json",
  "pkg/fixtures/triggers/subscription_schedule.aborted.json",
  "pkg/fixtures/triggers/subscription_schedule.canceled.json",
  "pkg/fixtures/triggers/subscription_schedule.completed.json",
  "pkg/fixtures/triggers/subscription_schedule.created.json",
  "pkg/fixtures/triggers/subscription_schedule.expiring.json",
  "pkg/fixtures/triggers/subscription_schedule.released.json",
  "pkg/fixtures/triggers/subscription_schedule.updated.json",
]
excluded_categories = ["tests", "fixtures"]
secret_detector = "text-secrets-v1"
max_file_bytes = 1000000
max_capsule_files = 180
max_capsule_utf8_bytes = 2500000
max_packet_files = 220
max_packet_utf8_bytes = 3200000
```

No glob or broad trigger directory may be substituted for the explicit list. If temporary exact-tag resolution exceeds a budget, collection stops for policy review rather than silently dropping required evidence or increasing limits.

## Collection and Comparison Flow

1. Add the reviewed registry track and exact capsule paths, then run focused registry tests and the offline GitHub validator.
2. Run a dry collection for `stripe/stripe-cli`; it must discover and verify the configured stable release without publishing raw evidence or a work item.
3. Resolve the exact release capsule in temporary storage to verify selected paths, hashes, UTF-8 validity, budgets, and secret scanning before publication.
4. Run real baseline collection only after the policy checks pass. Publish one exact-SHA snapshot, one package release record, comparisons where applicable, and one review packet.
5. Stop at `awaiting_approval`. Collection must not approve, claim ingest, or edit wiki knowledge.
6. Future checks collect every newer stable `1.x` release and compare it with the highest retained release. An unchanged check creates no ingest item.

The initial baseline is recommended as `full`. Later contained releases may be recommended as `delta` only when every retained change is classified and no major behavior, security, public-command, or capsule-policy boundary requires full review.

## Ingest Contract

After separate user approval, ingest exactly one work item and read every required path in full. Create one cumulative Stripe CLI source page and one package-qualified changelog under `wiki/sources/stripe/github/`.

Deep synthesis covers:

- CLI login, credentials, profiles, environments, and request authentication;
- root command and direct API request behavior;
- webhook listening, event filtering, forwarding, endpoint responses, reconnect behavior, and relevant API-version handling;
- checkout and recurring-payment event triggering, fixture request sequences, overrides, and limitations;
- version-qualified changes and migration impact.

The source page must state that simulated CLI events are development evidence, not proof of merchant enablement, production delivery, payment completion, or subscription execution.

## Validation and Success Criteria

- Registry tests and `scripts/validate_github_collection.py` pass.
- Dry run identifies and verifies the configured `stripe-cli@1` release without publishing raw evidence.
- Temporary exact-tag resolution stays within the reviewed budgets and reports no unsafe path, secret, missing required file, or unclassified evidence issue.
- Real collection stops at `awaiting_approval` with no wiki edits.
- The review packet recommends full ingest for the initial baseline and has no unresolved evidence gaps.
- Existing accepted evidence and unrelated workspace files remain untouched.
