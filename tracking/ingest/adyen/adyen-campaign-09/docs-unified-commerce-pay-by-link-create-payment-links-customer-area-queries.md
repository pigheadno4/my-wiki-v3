# Fixed retrieval checks: Customer Area payment links

## Q1 — Purpose and scope

**Query:** What does the Adyen Customer Area Pay by Link guide let a merchant user do, and what should a link or hosted page not prove?

**Expected answer:** With the Pay by Link Interface role and account setup, a user can create and send a payment link from Customer Area without development work. A shopper opening it reaches an Adyen-hosted payment form. This dated guide says the Customer Area route excludes buy now, pay later methods, but the separately reviewed supported-methods matrix marks Affirm, Alma and Atome under Customer Area. This unresolved snapshot conflict prevents a blanket BNPL availability claim; verify applicable method, account and product conditions. Link creation, sending and opening do not prove payment authorization, capture, final success or live-account readiness. Optional server webhooks require development work.

**Raw locators:** `# Payment links through the Customer Area`, lines 15–34; `## Requirements`, lines 36–49; `## 2. Send the payment link to your shopper`, lines 96–108; `## Test and go live`, lines 209–220. **Canonical retrieval route:** [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links-customer-area]] → [[raw/adyen/docs/unified-commerce/pay-by-link/create-payment-links/customer-area/2026-09-15|pinned raw]].

## Q2 — Workflow, roles, expiry and privacy

**Query:** How are Customer Area links configured and checked, and what status, role, expiry and shopper-data limits apply?

**Expected answer:** The user selects a merchant account, goes to Payments > Payment links, fills fields subject to creation settings, creates/copies/sends the link, and checks the result in Payment list or configured email/webhook updates. Single use is default; the validity setting defaults to 24 hours and can be at most 70 days. A `Completed` link is authorized and may still need manual capture; `Payment pending` has no final result. Reusable links stay Active or Expired. Link details are kept three months; the list shows links created within 90 days. Payment-method customization needs Change payment methods, and theme customization needs Merchant admin or Pay by Link Settings. Shopper reference must exclude PII, unmasking shopper details needs Merchant view PII, and saving payment details needs consent; Customer Area supports recurring-payment tokenization, with later one-off use routed to the Pay by Link API.

**Raw locators:** `## Requirements`, lines 36–49; `## 1. Create a payment link`, lines 51–94; `## 3. Get updates about the payment`, lines 110–150; `## Customize the payment page`, lines 165–207. **Canonical retrieval route:** [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links-customer-area]] → [[raw/adyen/docs/unified-commerce/pay-by-link/create-payment-links/customer-area/2026-09-15|pinned raw]].

**Cross-source conflict locator:** [[source-adyen-docs-unified-commerce-pay-by-link-supported-payment-methods]] → pinned matrix lines 39, 43, 45, compared with this guide line 23.
