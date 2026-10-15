# Fixed retrieval checks: Adyen account settings webhooks

## Q1 — Scope and setup

**Query:** Which account-setting changes does this webhook type report, and what must a receiver configure before relying on it in test and live?

**Expected answer:** The dated guide describes changes to company-account, merchant-account and store settings. It lists `accountStatus`, `blockPayout`, `merchantName`, `settlementCurrency` and `merchantCategoryCode` as trigger fields. A receiver exposes a server endpoint, accepts and verifies HMAC-signed notifications, and acknowledges every notification with a successful HTTP status within 10 seconds. Customer Area setup selects Account settings details and JSON. Live requires a separate live Customer Area configuration and, for HMAC-signed webhooks, a newly generated and verified live HMAC key. A settings notification does not prove a payment or payout outcome.

**Raw locators:** purpose and examples, lines 15–27; setup and live key, lines 29–41; trigger fields and status meanings, lines 55–73. **Canonical retrieval route:** [[adyen-webhooks]] → [[source-adyen-docs-development-resources-webhooks-webhook-types-account-settings-webhooks]] → [[raw/adyen/docs/development-resources/webhooks/webhook-types/account-settings-webhooks/2026-09-15|pinned raw]].

## Q2 — Payload identity and SOAP exclusion

**Query:** What does `pspReference` identify in an account-settings webhook, what payload qualifications matter, and what happens when a SOAP field is excluded?

**Expected answer:** `pspReference` is a change-specific `NO_PSP_REF`-prefixed reference; the page explicitly says it is not a payment PSP reference. The payload describes the changed entity, execution time and actor, field name and new value; `oldValue` is not included by default. `entityKey` documentation also lists a user-level format, although the trigger description covers company, merchant and store account fields, so that format alone does not establish a separate user-change trigger. In SOAP, excluding an account field stops new webhooks for that field, but pending unsent events are processed normally and retain the field. The example timestamps are illustrative, not current events.

**Raw locators:** SOAP exclusion and pending-event rule, lines 43–53; trigger scope, lines 55–57; payload table and non-payment reference, lines 75–98; examples, lines 100–156. **Canonical retrieval route:** [[adyen-webhooks]] → [[source-adyen-docs-development-resources-webhooks-webhook-types-account-settings-webhooks]] → [[raw/adyen/docs/development-resources/webhooks/webhook-types/account-settings-webhooks/2026-09-15|pinned raw]].
