# Fixed retrieval answers — api-explorer-onboarding-on-invite-webhooks-latest-post-balanceplatform-accountholder-onboarded

Canonical source: [[source-adyen-api-explorer-onboarding-on-invite-webhooks-latest-post-balanceplatform-accountholder-onboarded]]; URL: https://docs.adyen.com/api-explorer/onboarding-on-invite-webhooks/latest/post/balancePlatform.accountHolder.onboarded. Pinned raw: `raw/adyen/api-explorer/onboarding-on-invite-webhooks/latest/post/balancePlatform.accountHolder.onboarded/2026-09-15.md`.

## Q1

Adyen sends this incoming event when a new account holder has been onboarded to a balance platform; it supplies created-resource references and IDs useful in later payment/payout processing (raw lines 5–9). The body table requires top-level `data`, `environment`, and `type`; optional `timestamp` is queue time (lines 13–16, 48–50). Inside `data`, the listed account-holder, primary balance-account, balance-platform, capability map, creation date, legal-entity, merchant, store and transfer-instrument fields are optional (lines 17–47). Their IDs denote distinct resources; `creationDate` is event trigger time (line 33). Optional capability settings include `allowed`, `enabled`, `requested`, and `verificationStatus` (lines 28–32). The TEST example's `data.id` has no corresponding displayed schema row, and its store balance-account ID differs in string length from the primary balance-account ID (lines 62, 70–71, 91). The page gives no precise trigger timing beyond the onboarding statement and event/queue timestamps.

## Q2

A `2xx` status accepts the webhook; `notificationResponse: "[accepted]"` is only an optional example body (raw lines 115–134). The onboarding event indicates a new holder onboarded, but optional capability fields and the TEST example's `receivePayments` true/valid values do not prove another holder's verification or ability to receive payments (lines 28–32, 76–82). Receipt does not establish a payment, payout, settlement or bank receipt. This page states no delivery/order/retry/deduplication/signature rule or deprecation policy. `latest` is the captured route label, not later-version evidence.
