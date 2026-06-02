<!-- Source URL: https://developer.paypal.com/docs/payouts/standard/reference/fees/ -->

## <!-- Fetched: 2026-04-16 -->

title: Payouts fees
slug: /docs/payouts/standard/reference/fees/
createTime: '2024-08-15T08:01:10.990Z'
updateTime: '2025-05-13T11:08:50.088Z'

---

# Payouts fees

The sender pays Payout fees at transaction time. Fees vary by sending country, are calculated as a percentage of each transaction, and are capped. Typically, the variable component is 2% and the domestic payments cap differs from the international payments cap. For detailed information about payout fees, see the [PayPal Merchant Fees](https://www.paypal.com/us/webapps/mpp/merchant-fees#paypal-payouts) page.

The funding PayPal account for a payout request must hold the total payout amount plus any fees in the currency being sent. A payout item has these limits but the maximum total payout amount is unlimited:

| Country         | Individual payout maximum                             | Total payout maximum |
| --------------- | ----------------------------------------------------- | -------------------- |
| U.S.            | $20,000.00 USD                                        | Unlimited            |
| Other countries | Up to $20,000.00 USD in your country's local currency | Unlimited            |
