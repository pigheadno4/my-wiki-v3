# Fixed retrieval answers: Onboarding on invite webhooks v1 overview

## Q1

The 2026-09-15 captured [Adyen Onboarding on invite webhooks overview](https://docs.adyen.com/api-explorer/onboarding-on-invite-webhooks/latest/overview) identifies the family as **v1** and says Adyen sends webhooks when a new account holder is onboarded in a balance platform using the onboarding on invite flow (pinned raw `raw/adyen/api-explorer/onboarding-on-invite-webhooks/latest/overview/2026-09-15.md:5-7`). Its sole listed endpoint is `POST balancePlatform.accountHolder.onboarded`, summarized “Account holder onboarded” (`:9-14`). This overview provides no event payload, identifiers, required or conditional fields, response, trigger timing or state-transition detail beyond that description. Source stem: `source-adyen-api-explorer-onboarding-on-invite-webhooks-latest-overview`.

## Q2

The catalog establishes that Adyen documents a notification for an on-invite account-holder onboarding event; it does not define webhook acceptance, response decisions, verified capabilities, payment authorization, payout eligibility, or final financial state (`raw/adyen/api-explorer/onboarding-on-invite-webhooks/latest/overview/2026-09-15.md:5-14`). Delivery order, retry, deduplication, signature and failure handling are not specified in this overview. The endpoint-specific reference must be read for its own contract. `latest` is the route label while the captured overview says v1; this 2026-09-15 snapshot is not evidence of current availability. Canonical route: [Adyen Onboarding on invite webhooks overview](https://docs.adyen.com/api-explorer/onboarding-on-invite-webhooks/latest/overview); source stem `source-adyen-api-explorer-onboarding-on-invite-webhooks-latest-overview`.
