# C23 Classic Platforms HMAC notification retrieval checks

## Q1 — How does this Classic guide enable and verify HMAC-signed notifications?

It covers Notifications v5+, with basic authentication as the stated default and optional HMAC (raw lines 19–25). Supply a shared HMAC key in `/createNotificationConfiguration` for the endpoint, then read `HmacSignature` and `Protocol` from incoming HTTP headers. Compute SHA256 HMAC over the whole original HTTP body with that key and compare before deserializing; reordered JSON may fail a valid signature (raw lines 33–35, 84–90). Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-configure-notifications-signing-notifications-with-hmac]] → [[raw/adyen/docs/classic-platforms/configure-notifications/signing-notifications-with-hmac/2026-09-15]].

## Q2 — What rotation and example conflicts must an implementer retain?

Previous notifications stay signed with the previous HMAC key after a new key is generated (raw lines 29–31). The key is described as `32bit hexadecimal` but the example is 64 hex characters (raw lines 29, 54, 114–115). The prose says the configuration activates `ACCOUNT_HOLDER_VERIFICATION`, while both sample `eventConfigs` list `ACCOUNT_CREATED` (raw lines 35, 48–53, 71–76). Confirm the applicable key requirement and desired event configuration before deployment; the sample does not establish delivery of the verification event. Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-configure-notifications-signing-notifications-with-hmac]] → [[raw/adyen/docs/classic-platforms/configure-notifications/signing-notifications-with-hmac/2026-09-15]].
