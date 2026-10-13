# Fixed retrieval checks — Adyen POS solutions

## 1. Purpose and scope

**Query:** What is the Solutions page for, and what should it not be used to infer?

**Answer:** It is a dated overview of Adyen's in-person payment paths: POS-to-terminal Terminal API integration, standalone terminals, mobile solutions, and partner-platform plugins (raw lines 17–53). It points to separate implementation guides. The page has no current terminal/SDK version, country, account-eligibility, payment-method, or plugin-configuration matrix, and it does not establish ecommerce checkout support or live operation.

**Route:** [[index]] → [[adyen-index]] → [[adyen-terminal-api]] → [[source-adyen-docs-point-of-sale-what-we-support-solutions]] → [[raw/adyen/docs/point-of-sale/what-we-support/solutions/2026-09-15]] (catalog promotion pending).

## 2. Central paths and prerequisites

**Query:** How do the integrated, standalone, mobile, and plugin paths differ?

**Answer:** Integrated POS uses Terminal API messages with Adyen-supplied PCI-certified terminals (lines 21–27). Standalone means a shopper transaction is initiated directly at an Adyen terminal without POS development, with a proposed internet-problem fallback that needs its own operational conditions checked (lines 29–35). The mobile POS app path first integrates Terminal API, then uses Mobile SDK for payment routing under the Terminal API specification; the page also names a distinct POS app-to-Adyen Payments app option (lines 37–45). A partner plugin uses Adyen terminals that communicate directly with the partner platform (lines 47–53). These descriptions do not certify a particular market, device, firmware, SDK release, payment type, or partner configuration.

**Route:** [[index]] → [[adyen-index]] → [[adyen-terminal-api]] → [[source-adyen-docs-point-of-sale-what-we-support-solutions]] → [[raw/adyen/docs/point-of-sale/what-we-support/solutions/2026-09-15]] (catalog promotion pending).
