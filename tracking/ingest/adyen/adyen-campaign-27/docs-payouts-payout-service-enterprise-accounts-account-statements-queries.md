# C27 enterprise-account statement retrieval checks

## Q1 — Purpose, product and access

**Query:** What account statements does Payout Service generate for enterprise accounts, and what setup is required?

**Answer:** The guide describes CAMT.053 ISO 20022 statements of enterprise-account financial activity, potentially including Adyen-issued-card transactions when linked to the same balance account (raw lines 15–21). It requires a Payouts integration and enterprise account, Adyen-enabled/configured statement feature, Report user API key with Merchant Report Download, and a subscribed/receivable `balancePlatform.report.created` webhook (raw lines 23–45). Statements are automatically generated; the webhook provides a URL for a separate GET download (raw lines 47–91). Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-payouts-payout-service-enterprise-accounts-account-statements]] → [[raw/adyen/docs/payouts/payout-service/enterprise-accounts/account-statements/2026-09-15]].

## Q2 — Grain and reconciliation boundary

**Query:** Can a summarized file support transaction-level matching, and does a booked statement entry prove bank receipt?

**Answer:** Each `<Stmt>` represents one account and currency, and a file can contain multiple statements (raw line 142). The standard statement has one `<Ntry>` per transaction, while the optional daily summarized file has one per BAI-code group, totaling transactions and using date-only fields (raw lines 473–537); use the detailed file for transaction-level matching. Configured balances may be booked or available, which are distinct measures (raw lines 174–181). A booked entry records account activity and does not establish an external beneficiary-bank credit (raw lines 199–219). Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-payouts-payout-service-enterprise-accounts-account-statements]] → [[raw/adyen/docs/payouts/payout-service/enterprise-accounts/account-statements/2026-09-15]].
