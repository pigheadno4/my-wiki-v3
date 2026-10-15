# Fixed retrieval checks — Customer Area email login

## Q1 — What is this page for, what is its scope, and what should not be inferred?

It is a 2026-09-15 guide for a Merchant admin to migrate existing Adyen Customer Area users to email-address login, separately in test and live. It does not establish that any merchant has performed migration, assign roles or account permissions, configure MFA/SSO, change API credentials, or specify password recovery. Retrieve through `[[adyen-customer-area-iam]]` → `[[source-adyen-docs-account-email-log-in]]` → `[[raw/adyen/docs/account/email-log-in/2026-09-15]]`; raw lines 15–31 and 71–100. Canonical page: https://docs.adyen.com/account/email-log-in.

## Q2 — What is the central migration flow, prerequisites, and warning?

The documented role is Merchant admin (raw lines 23–27); test/live migrations are separate (line 31). Review status reports first: a duplicate email across Customer Area accounts or same-organization SSO/email-login collision needs resolution (lines 43–69). The administrator may start one or multiple users (lines 71–96); individual start sends an email, while bulk start does not notify users at that point. Pending users cannot access Customer Area until completing migration with prior credentials; after completion, prior credentials stop working (lines 96–100). Cancellation is permitted only before completion and can later be restarted (lines 102–126). Use the same concept→source→raw route; this is user-login lifecycle guidance, not proof of an actual account change.
