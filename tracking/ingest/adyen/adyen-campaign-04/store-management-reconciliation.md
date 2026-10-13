# Bounded POS store-management reconciliation

Replace Definition paragraph:

For an Adyen point-of-sale integration, store administration uses the Management API to retrieve, create, and update merchant-associated stores and to configure their payment methods. This is distinct from Terminal API payment messaging.

With:

Adyen POS store administration is distinct from Terminal API payment messaging. Merchants can create stores in the Customer Area, or automate store retrieval, creation, updates, status changes and payment-method settings through Management API. The two setup routes have their own credential and configuration requirements; see the respective source guides.

In Operational boundary replace "New stores start active without payment methods" with "In the Management API automation guide, new stores start active without payment methods". The Customer Area creation guide instead presents default country/region methods and selection when creating a store. Both are route-scoped, not a same-scope contradiction. Do not add the previously rejected optional hierarchy paragraph.
