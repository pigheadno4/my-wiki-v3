# Fixed queries — docs-platforms-manage-access

## Q1 — purpose, scope, and non-inference

**Query:** What does this Adyen Platforms “Manage access for your team” page cover, and does initial admin access prove API or financial-product permissions?

**Answer:** It is a Customer Area orientation: Adyen creates an initial platform admin user on signup, activates it after email verification, and lets that admin create team users and assign roles (raw lines 15–19, 34–38). It navigates resource, payment, transfer, webhook, report and financial-product administration but does not prove any specific credential, API role, product enablement, payment or payout. Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-manage-access]] → pinned raw.

## Q2 — central capability, prerequisites, and warnings

**Query:** How are Customer Area users and API credentials related in this guide, and what test/live or role detail is specified?

**Answer:** The admin's email verification activates the initial Customer Area user. Team users get assigned Customer Area roles for their actions, while API credentials are a separate management area covering payments, balance platform and financial products; the page links the Balance Platform credential guide for API requests (raw lines 19, 25–38, 40–52). It does not enumerate exact roles, API key scopes, permissions or test/live migration, and its Customer Area link is a test-domain URL. Consult the operation-specific child guides and the actual account configuration before inferring access. Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-manage-access]] → pinned raw.
