# Fixed retrieval checks — 3D Secure 2 redirect authentication

## Q1 — What is this page for, what is its scope, and what should not be inferred?

This is the 2026-09-15 Adyen Docs landing/route page for redirect 3DS2 authentication. It says Adyen provides a URL where the shopper can complete authentication, and it points API-only integrations to Web, iOS, and Android Component guides. It does not specify a Checkout API call sequence, SDK version, merchant eligibility, or a successful authentication/payment outcome. Start at `[[adyen-3d-secure]]` → `[[source-adyen-docs-online-payments-3d-secure-redirect-3ds2]]` → `[[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/2026-09-15]]`; see raw lines 15-29 and 33-47. Canonical page: https://docs.adyen.com/online-payments/3d-secure/redirect-3ds2.

## Q2 — What is the central capability, prerequisite or choice, and warning?

The central route is an Adyen-provided redirect URL for the shopper's 3DS2 identity verification. The page describes passive, biometric, or two-factor verification; for an API-only integration it directs the reader to a Web, iOS, or Android Component guide and separately links native 3DS2 as a non-redirect option. These are route choices, not proof that a platform-specific integration has been configured or that a payment was authorized or captured. Use the same canonical source route; raw lines 19-29 identify the choice and raw lines 33-47 provide the platform navigation. Follow each linked Component source for its own implementation and version conditions.
