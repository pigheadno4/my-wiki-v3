---
title: "Adyen Payment Method Variants"
type: concept
category: technology
tags: [adyen, payment-methods, variants]
---

## Overview

Adyen's `paymentMethodVariant` identifies the payment method type used in a transaction. The documented variant list is open to additional values depending on configuration. The related Management API table concerns variants when **adding** payment methods and carries separate ecommerce/POS indicators and method-specific conditions; a returned transaction variant does not establish a merchant's setup eligibility.

## Sources

- [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-paymentmethodsettings-paymentmethodid]] — 2026-11-05-captured Management API v3 TEST PATCH of merchant payment-method settings by merchant and payment-method IDs; returned enabled, allowed and verification fields are separate from payment execution.

> [!warning] Contradiction
> This PATCH introduction refers to request `type` and a possibly required method-specific object, while its request table has no top-level `type` row. The snapshot does not resolve whether that field is accepted or needed. [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-paymentmethodsettings-paymentmethodid]]


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-paymentmethodsettings]] — 2026-11-05-captured Management API v3 TEST merchant payment-method settings list, with pagination, variant and separate enabled, allowed and verification fields.


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-paymentmethodsettings]] — 2026-11-05-captured Management API v3 TEST reference for requesting a merchant payment method by variant, with method-specific inputs and separate screening, enablement and verification response states.


- [[source-adyen-docs-development-resources-paymentmethodvariant]] — Adyen transaction-variant code reference and separate Management API adding-method table (webpage snapshot, 2026-09-15).
