# C23 query checks — docs-issuing-manage-card-data

Q1. What is this page for, and what must a platform consider before implementing it?

The 2026-09-15 Issuing hub routes platform builders to cardholder functions for revealing card details (PAN/expiry), revealing PIN, and changing PIN; each has an iOS SDK route and a standard-encryption route (pinned raw lines 15–24, 32–57). These operations transfer sensitive card data between the platform's servers and Adyen, and the page says all transferred data must be encrypted, citing AES and ISO-4 as methods (26). Detailed prerequisites, roles, exact crypto flows and SDK versions belong to the child pages, not this hub. Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-manage-card-data]] → [[raw/adyen/docs/issuing/manage-card-data/2026-09-15]].

Q2. What capability and evidence boundaries matter?

At the pinned snapshot, the Adyen card-management SDK is stated to be iOS-only; an Android release is a forecast, not confirmation of current support (raw 28). The page offers implementing algorithms yourself or using the SDK, and labels linked iOS procedures “Adyen Card Reveal iOS” (28–30, 38–57). This hub proves neither PCI scope nor successful PIN change, card authentication, payment authorisation, capture or settlement. Follow the operation-specific guide and current product requirements for those claims. Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-manage-card-data]] → [[raw/adyen/docs/issuing/manage-card-data/2026-09-15]].
