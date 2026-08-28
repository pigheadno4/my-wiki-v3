---
title: "Stripe Apps"
type: concept
category: technology
tags: [stripe, stripe-apps, dashboard, ui-extensions, app-marketplace, developer-platform]
---

## Definition

Stripe Apps is Stripe's developer platform for embedding custom user experiences in the Stripe Dashboard and connecting those experiences to Stripe API capabilities. Apps declare their identity, requested permissions, Dashboard placement, network policy, distribution model, API-access model, and sandbox compatibility through manifests.

## Application Model

- A standard `stripe-app.json` manifest describes the app name, version, icon, permissions, UI views, post-install behavior, allowed redirects, content security policy, distribution type, API-access type, and sandbox compatibility.
- UI extensions are React components rendered in supported Stripe Dashboard viewports. The retained full-page example uses an app router for overview, member, reward, activity, settings, and detail views.
- Distribution can be `public` or `private`. Public marketplace publication also has review and listing requirements outside the retained repository capsule.
- The retained schema recognizes `restricted_api_key`, `oauth`, and `platform` API-access types. Their presence in a schema does not prove that a particular app is approved, configured, or entitled to use every Stripe API permission.
- Local development manifests can extend a base manifest and override development-oriented configuration.

## Evidence Boundaries

- Permission names such as `checkout_session_write` and `payment_intent_write` describe manifest vocabulary; they do not establish a payment flow, merchant eligibility, or product availability.
- The retained Pizzazz Loyalty example uses local mock records, simulated network delays, and in-memory React Query mutations. It demonstrates Dashboard UI-extension patterns, not live Stripe API or Checkout behavior.
- The example manifest and retained standard JSON schema do not validate against each other literally: the example omits the schema-required `permissions`, uses `stripe.dashboard.fullpage` outside the retained viewport enum, and specifies a modal post-install action outside the retained standard schema alternatives. Treat the example as exact-commit repository evidence rather than a universal manifest template.
- The retained `.schema.yaml` file contains a distinct extension-manifest schema with `extensions`, interface IDs, permissions, and methods. It is not merely a YAML serialization of the standard app manifest.
- The repository-level changelog redirects to the independently versioned `@stripe/ui-extension-sdk` npm changelog. The repository commit is therefore tracked independently from SDK package releases.

## Related

- Company: [[stripe]]
- Source: [[source-github-stripe-apps]]
- History: [[changelog-github-stripe-apps]]
