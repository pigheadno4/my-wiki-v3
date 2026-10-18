# Worker retrieval checks

Q1. What UK direct-debit capability does this page describe, and what gates it?

A1. This 2019-modified guide describes a UK-only limited-availability pilot: an authorized counterparty can request a single or recurring Bacs collection from the user's Business Account (raw lines 15–24, 37–49). The platform needs Adyen for Platforms with Business Accounts, the user's `sendFundsToThirdParty` capability and Adyen enablement (raw lines 26–35). For a collection, Adyen checks active account, capability, approved linked mandate and available balance; unmet conditions result in rejection (raw lines 47–59). Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-accept-direct-debits-uk]] → [[raw/adyen/docs/business-accounts/accept-direct-debits-uk/2026-09-15]].

Q2. Does a mandate submission or amendment prove collection or an effective cancellation?

A2. No. For creation, the user's mandate information travels via the counterparty, its provider and Bacs to Adyen; Adyen validates account activity and capability before mandate approval and notification (raw lines 67–91). A later amendment or cancellation starts with the user/platform, then passes through Adyen and Bacs to the counterparty's provider, which validates and applies it; confirmation returns before Adyen notifies the platform (raw lines 93–113). The guide's collection path is distinct (raw lines 45–65), and the pilot warning limits current-availability claims (raw lines 19–20). Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-accept-direct-debits-uk]] → [[raw/adyen/docs/business-accounts/accept-direct-debits-uk/2026-09-15]].
