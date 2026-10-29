# docs-payment-methods-bancontact-bancontact-card-web-component — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-bancontact-bancontact-card-web-component]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-bancontact-bancontact-card-web-component]] is the Bancontact **card** Web Component guide for an existing Sessions or Advanced Web Components integration, with v6 and earlier mounting variants (raw/adyen/docs/payment-methods/bancontact/bancontact-card/web-component/2026-09-15.md:15–53, 72–92). It is separate from Bancontact Mobile app-switch/QR instructions. Its 2021-10-27 `last_modified` metadata and 2026-09-15 capture do not prove current SDK behavior, merchant/WIP eligibility, or payment success (raw lines 5–11, 170–198, 566–599).

## Q2 — What central capability, prerequisites, and warnings are stated?

The Component collects card information and redirects for mandatory 3DS; the card path normally has no CVC, though co-badged cards may display one, and separate captures are unsupported (raw/adyen/docs/payment-methods/bancontact/bancontact-card/web-component/2026-09-15.md:19–27). It requires an existing Sessions or Advanced Web Components integration and Bancontact card setup in Customer Area; v6 uses the imported `Bancontact` constructor, v5.x.x or earlier `checkout.create('bcmc')` (raw lines 29–53, 72–92). Holder-name and storage-checkbox settings are optional (raw lines 94–130). WIP recurring requires signup/eligibility/Support and transaction limits; after consent/SCA and settlement, the token webhook supplies `storedPaymentMethodId` for later `ContAuth` requests (raw lines 170–225). The test-card section includes a co-badged Visa example that may route to Bancontact or Visa, a decline fixture, and separate live Customer Area setup; none proves live payment execution (raw lines 566–599).
