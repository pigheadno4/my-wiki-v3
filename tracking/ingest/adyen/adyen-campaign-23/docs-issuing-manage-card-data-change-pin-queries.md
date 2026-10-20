# Retrieval checks — docs-issuing-manage-card-data-change-pin

Q1. What does this Issuing PIN-change guide require and what is the high-level request path?

A1. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-manage-card-data-change-pin]] → [[raw/adyen/docs/issuing/manage-card-data/change-pin/2026-09-15]]. The page requires Configuration API credentials with the Bank Issuing PIN Change Webservice role (raw lines 38–43). It obtains a public key with GET `/publicKey?purpose=pinChange`, whose response includes an expiry date (raw lines 45–51, 211–225); the guide then describes generating an AES key, RSA-encrypted session key, no-zero 16-digit token and ISO-4 encrypted PIN block (raw lines 227–279). POST `/pins/change` supplies `paymentInstrumentId`, `encryptedKey`, `token`, and `encryptedPinBlock` (raw lines 281–290).

Q2. What security wording and response limitations matter before treating a request as a changed PIN?

A2. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-manage-card-data-change-pin]] → [[raw/adyen/docs/issuing/manage-card-data/change-pin/2026-09-15]]. The sequence says to encrypt the 256-bit AES key with Adyen's public key to form an encrypted session key (raw lines 229–238); the request table abbreviates `encryptedKey` as “The symmetric session AES key” (raw lines 283–290), so it should not be read as permission to send plaintext key material. The response can be `completed`, `pending` or `unavailable` (raw line 511), so a sample POST or pending state does not prove completion. The visible curl/library snippets are test-environment examples and include generic `string` arguments for publicKey calls even though the prose specifies `purpose=pinChange` (raw lines 51–59, 65–209).
