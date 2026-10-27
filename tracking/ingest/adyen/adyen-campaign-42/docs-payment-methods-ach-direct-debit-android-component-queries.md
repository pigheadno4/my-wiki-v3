# Fixed retrieval checks — ACH Android Component

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ach-direct-debit-android-component.md`.

## Q1. What is this source's purpose and scope, and what cannot be inferred?

The 2026-09-15 page gives ACH-specific Android Component additions for an **existing** Sessions or Advanced integration (primary raw `raw/adyen/docs/payment-methods/ach-direct-debit/android-component/2026-09-15.md:15-25,179-185`; canonical source stem `source-adyen-docs-payment-methods-ach-direct-debit-android-component`). It is not a full Android flow, a bank-validation procedure, a signed-mandate guide, evidence of current account availability or final ACH payment proof. Request receipt can precede bank authorization by up to five business days and failed bank authorization yields `CHARGEBACK` (`:155-159,308-312`). Follow approved ACH overview `source-adyen-docs-payment-methods-ach-direct-debit` for SEC/mandate/return boundaries and giact child source for consumer bank validation.

## Q2. What are the central capability, prerequisites and warnings?

Sessions requires an existing Android Components Sessions flow, Checkout API **v68+**, ACH Customer Area addition and notice-of-change webhook; its bank-refund roles are specifically for API/Customer Area **refunds**, while no ACH-specific extra `/sessions` fields are called for (`:29-44`). Both flows import the ACH Android module and optionally Compose module; UI defaults are visible submit/store checkbox and full-address form, with examples setting US/PR address countries (`:46-95,197-241`). Sessions obtains ACH from the checkout session; Advanced obtains it from `/paymentMethods`, and Compose examples require a unique key per different screen/session (`:104-150,249-298`). Advanced says no ACH-specific additional `/payments` fields (`:300-304`), which does not waive standard request, mandate or verification requirements. TEST routing/account examples and `chargeback:R01` simulate payment/return flows only (`:161-177,314-330`). The bank result remains asynchronous (`:159,312`).
