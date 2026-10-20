# Retrieval checks — docs-issuing-manage-card-data-reveal-pin

## Q1 — What is this guide for, and what does the platform need before requesting PIN data?

The 2026-09-15 snapshot describes revealing an Adyen-issued card's PIN to its cardholder in the platform app/site (raw lines 15–23). It requires Configuration API credentials and the Bank Issuing PIN Reveal Webservice role (lines 37–42). The flow gets `GET /publicKey?purpose=pinReveal` (lines 44–50), generates a 256-bit AES key (line 228), encrypts it using the Adyen RSA public key and PKCS 1 (lines 230–237), then posts `paymentInstrumentId` and `encryptedKey` to `/pins/reveal` (lines 239–249). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-manage-card-data-reveal-pin]] → [[raw/adyen/docs/issuing/manage-card-data/reveal-pin/2026-09-15]].

## Q2 — What sensitive-data boundary or contradiction limits use of the decryption instructions?

The response contains an ISO Format 4 encrypted PIN block and a token, passed to the client for decryption and cardholder display (raw lines 449–467). Yet line 486 says to decrypt an intermediate result using RSA in ECB mode with the previously generated key, while line 228 defines that key as AES; this is internally inconsistent and needs source clarification before treating the final step as reliable code guidance. Line 232 also labels the reveal session-key step a PIN-change request. Sample calls use a test host/environment (lines 57, 75, 255) and do not establish live eligibility or successful PIN disclosure. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-manage-card-data-reveal-pin]] → [[raw/adyen/docs/issuing/manage-card-data/reveal-pin/2026-09-15]].
