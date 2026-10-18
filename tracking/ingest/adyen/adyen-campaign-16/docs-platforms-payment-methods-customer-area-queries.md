# Fixed retrieval checks: docs-platforms-payment-methods-customer-area

## Q1 — Scope, prerequisites and usable status

**Query:** How does a platform request payment methods for a user's store in Customer Area, and when can the user actually use a method?

**Expected answer:** The 2026-09-15-captured Platforms guide requires an Adyen online or point-of-sale integration, the Customer Area **Change payment methods** role, payment-method webhook subscription, and an existing business line and user store. Only methods supported for the currency and integration are configurable there; some methods may require the Management API. The operator works under a merchant account, requests a method, applies it to the user's store and submits. Addition is asynchronous; `paymentMethod.created` follows when a method is added, while availability typically appears within a day rather than at a guaranteed time. A requested method is enabled for the user by default, but usable acceptance requires the account holder's `receivePayments` capability to have `verificationStatus: valid`, `enabled: true` and `allowed: true`. Updating verified legal-entity or account-holder information may disable methods until reverification. A submitted request, test webhook or enabled configuration does not prove live acceptance or payment.

**Evidence locators:** `raw/adyen/docs/platforms/payment-methods/customer-area/2026-09-15.md:19-43`, `:45-83`, `:91-103`, `:157-201`. **Canonical route:** `[[adyen]]` → `[[adyen-platforms]]` → `[[source-adyen-docs-platforms-payment-methods-customer-area]]` → pinned raw.

## Q2 — Error handling, settings and deletion

**Query:** What Customer Area management actions, failure timing and removal conditions does this page document?

**Expected answer:** From the merchant-account Payment methods table, the operator can filter/list methods, open details, select methods and Activate or Deactivate them. An immediate **Submit request** error should be corrected before resubmission. In the rare case a submitted request fails later and no webhook subscription provides an automated alert, the page says to wait 24 hours before retrying. A method marked **Inactive** and unused for 90 days is automatically deleted; a method linked to a closed store becomes Inactive and is deleted after 90 days. The detailed Customer Area edit flow changes Country/Region and offers **ANY** to avoid a country restriction. Although the introduction mentions currency updates, the requirements direct nondefault currency changes to Support; the documented steps do not establish a currency-edit control. Country selection does not override payment-method, currency, integration or account-holder eligibility.

**Evidence locators:** `raw/adyen/docs/platforms/payment-methods/customer-area/2026-09-15.md:21-27`, `:38-43`, `:85-89`, `:203-233`. **Canonical route:** `[[adyen]]` → `[[adyen-platforms]]` → `[[source-adyen-docs-platforms-payment-methods-customer-area]]` → pinned raw.
