# Fixed queries — docs-platforms-manage-account-holder-risk

## Q1 — purpose, scope, and non-inference

**Query:** What does the Platforms “Manage account holder risk” guide let operators do, and does a Score flag prove fraud or payout state?

**Answer:** It describes Customer Area Score case review and risk-rule automation after potential fraud or unusual activity is signaled (raw lines 15–19, 31–99). A signal, score, case label or example webhook is not confirmation of fraud, verified KYC, allowed capabilities, actual payout execution or bank receipt. The page's 2020 last-modified metadata predates its later roadmap wording; its post-October-2024 default and planned October-31-2026 enablement are not account-specific availability proof (lines 11, 25–29). Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-manage-account-holder-risk]] → pinned raw.

## Q2 — central capability, prerequisites, and warnings

**Query:** Which roles and risk controls are documented, and what actions or webhook conditions are consequential?

**Answer:** The guide lists `Merchant Marketplace Risk` for cases/direct actions and `Merchant Marketplace Risk Admin` for rules/automatic actions (raw line 27). A rule can change score impact or choose None, Bump KYC tier or Disable payouts, with an automated-actions log for review (lines 31–62). Direct case actions include queue labels, payout block/re-enable, account suspension, trusting linked accounts and high-risk KYC values only from confirmed fraudulent users (lines 64–99). False-positive signals can be muted for a chosen duration; excluding a KYC identifier from linked accounts is permanent and cannot be undone (lines 100–126). Risk-signal webhook delivery needs receiving server, Configuration-webhook subscription and Adyen enablement; sample `data.id` is a per-calculation ID separate from account-holder identity, not proof of a live action (lines 159–204). Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-manage-account-holder-risk]] → pinned raw.
