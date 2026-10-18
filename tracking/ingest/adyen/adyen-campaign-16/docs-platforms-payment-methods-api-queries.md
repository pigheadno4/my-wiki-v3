# Fixed retrieval checks — docs-platforms-payment-methods-api

Q1. What is this source for, what scope does it cover, and what must not be inferred?
- Route: [[source-adyen-docs-platforms-payment-methods-api]] → [[adyen-platforms]].
- Answer: This 2026-09-15 Platforms Management API guide covers requesting, listing, inspecting and updating payment-method settings for a user's store under a merchant account. It does not prove that a method is live and usable, that card variants are approved for a particular account, or that a payment, split booking or payout occurred. It gives no merchant-of-record or fund-ownership determination.
- Evidence: raw lines 15–27 (scope and variant example); 42–58 (POST and fields); 476–485 (list); 648–652 (detail); 796–808 (PATCH/deletion).

Q2. What are the central capabilities, prerequisites, and warnings?
- Route: [[source-adyen-docs-platforms-payment-methods-api]] → [[adyen-platforms]]; use pinned raw for field and example detail.
- Answer: The platform needs an online or in-person integration, configured user store and business line, Management API Payment methods read and write credential role, supported method/currency/integration and payment-method webhook. POST under merchant ID specifies method type, store ID and business line; countries/currencies are optional filters. The request is asynchronous: a method ID or `enabled` setting alone does not make it usable. Account-holder `receivePayments` must be enabled, allowed and valid; check via Configuration API or account-holder update webhook. A pending request is removed after 60 days if the capability does not reach the stated states. Updates to verified legal-entity/account-holder data can disable methods; disabled methods and methods linked to a closed store are deleted after 90 days. GET routes inspect methods and PATCH changes country/currency/enabled settings. Test-environment examples are not live operational proof.
- Evidence: raw lines 29–40 (requirements and availability timing); 42–58 (request fields); 289–343 (added/pending/webhooks); 364–475 (capability and legal-entity changes); 476–795 (GET routes); 796–808 (PATCH and deletion).
