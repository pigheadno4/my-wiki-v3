# Fixed queries — Adyen for Platforms support

## Q1 — purpose, scope, and what must not be inferred

**Query:** Who supports a platform's users, and does Adyen directly serve them or guarantee resolution?

**Answer:** The platform business owns its user relationship, inquiries and communications; Adyen Support serves the platform business rather than its users directly. The page offers an illustrative tiered team and escalation routes, not a required staffing model, support SLA or guarantee that an issue, KYC review, payment or payout resolves. Raw: `raw/adyen/docs/platforms/quickstart-guide/support/2026-09-15.md:17-27,38-50,113-121`. Canonical route: `[[source-adyen-docs-platforms-quickstart-guide-support]]` → `[[adyen-platforms]]`.

## Q2 — central support routes, prerequisites, and warnings

**Query:** How should a platform triage KYC/payout questions and contact or escalate to Adyen?

**Answer:** Use account-holder status/capability webhooks, reports, status reasons, verification errors and KYC documents to investigate and communicate with users. Customer Area **? > Submit a ticket** asks for subject and description, with product/environment/account context; the template requests relevant IDs in text. Urgent widespread payout/processing failures or inaccessible hosted onboarding route through the Adyen Account manager. `Pending` KYC review has a typical 24–48-hour timeframe, with Support clarification after 48 hours, not a deadline. Suspended/closed account holders are expected to have payout capabilities blocked; changing a non-Adyen-suspended status is not proof of verification or payout success. Booked payments may differ from value-date-funded payout amounts; use the linked accounting report and failure reasons to investigate, not to assert bank receipt. The page states no ticket-access role or response SLA. Raw: `raw/adyen/docs/platforms/quickstart-guide/support/2026-09-15.md:29-36,48-91,93-121,127-167`. Canonical route: `[[source-adyen-docs-platforms-quickstart-guide-support]]` → `[[adyen-platforms]]`.
