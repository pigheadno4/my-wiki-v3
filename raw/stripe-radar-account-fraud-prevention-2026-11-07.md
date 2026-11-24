<!-- Source URL: https://docs.stripe.com/radar/account-fraud-prevention -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Account fraud prevention

Use Stripe tools to reduce buyer and connected account risk.

Stripe provides risk tools for Connect platforms to help you prevent, detect, and mitigate both buyer risk and financially risky connected accounts.

Radar can help your platform manage risk end-to-end:

- [Identify potential financial risk](https://docs.stripe.com/radar/account-fraud-prevention.md#identify-potential-financial-risk) using risk scores and customized rules engines
- [Investigate connected accounts](https://docs.stripe.com/radar/account-fraud-prevention.md#investigate-connected-account) using risk metrics and agentic insights
- [Gather additional information](https://docs.stripe.com/radar/account-fraud-prevention.md#request-account-identity) using document verification or a selfie confirmation with [Stripe Identity](https://docs.stripe.com/identity.md)
- [Take action](https://docs.stripe.com/radar/account-fraud-prevention.md#take-action) on transactions and connected accounts (including setting reserves)

See the tool in action here:
[Watch on YouTube](https://www.youtube.com/watch?v=atKApQzu564)
## Identify potential financial risk

Using its AI models, Radar generates risk scores for individual transactions and connected accounts as a whole. Each score receives one of the following risk levels: `normal`, `elevated`, `highest`, or `not assessed`.

### Risk scores and levels

Stripe enables its connected account risk levels by default as connected account-level rules in your Radar rules page. Stripe identifies connected accounts scored as `highest` or `elevated` for review. We base this on their probability of financial loss because of fraud or insolvency risk. The score correlates to the probability that an account would cause losses to your platform.

- `highest` risk, or a score of 90 or higher, indicates a probability of over 90% .
- `elevated` risk, or a score of 50-89, indicates a probability of 50% to 89%.

Account risk scores and levels update each time a new event occurs, such as a transaction or a change in business information. Stripe also provides agentic risk insights to explain the assigned risk level, such as transaction patterns, connected account behavior, or connected account information that matches previous fraudulent activity. [Transaction risk scores and levels](https://docs.stripe.com/radar/transaction-risk-prevention.md#risk-outcomes) behave the same for platforms as for direct Stripe accounts.

> We recommend using Radar’s risk factors together with other risk factors to make holistic decisions about what additional information to request and what actions to take.

### Custom rule creation

You can customize the criteria for both connected account and transaction rules to suit the unique risks of your business. You can take one of the following actions when [creating your rules](https://docs.stripe.com/radar/rules.md):

#### Connected accounts

- Raise a review
- Pause payouts and raise a review

#### Treasury transactions (Private preview)

- Block
- Review

For a complete list of supported attributes in rule creation, see our [transaction rule attributes](https://docs.stripe.com/radar/rules/supported-attributes.md) and [connected account rule attributes](https://docs.stripe.com/radar/rules/supported-attributes.md?payment-method=card&radar-rules=account#attributes-for-platforms).

### Connected account reviews

After you write your Radar rules, we alert you when any of your connected accounts match a rule by highlighting these accounts in your Dashboard. Go to the **Radar rule match** queue of your [accounts list view](https://docs.stripe.com/connect/dashboard/viewing-all-accounts.md) or the **Reviews** tab in Radar to view accounts that match any of your rules. You can filter this list by the matched rule and risk level assigned.

### Treasury transaction reviews (Private preview)

After you create your Treasury review rules, you can view all matching Treasury transactions by going to the **Reviews** tab in Radar and selecting **Treasury reviews**. Matching a review rule doesn’t automatically block a transaction. Treasury transactions flagged for review might still be processed as usual.

## Investigate a connected account

Select an account from the connected account review list to see its [details page](https://docs.stripe.com/connect/dashboard/managing-individual-accounts.md). This page shows:

- Account status
- Current enablement status of payments and payouts
- Required actions for the account
- Account balances

From here you can view the **Risk tab** for that connected account. Your team can use this page to assist with investigating financial risks. This page has the following features to help with your review:

- Agent-generated risk indicators
- Risk metrics charts
- Recommended next steps
- Risk history log with note taking capabilities

### Risk metrics

The **Risk metrics** section highlights risky trends or anomalies using the following visualizations:

- A time-series graph of the count and volume of payments, disputes, declines, or refunds
- Time-series graphs for dispute rates, refund rates, and failure rates
- A filter to adjust the time period shown in the graphs
- A filter to show metrics by either count or volume

Dispute and refund data reflect the occurrence date of the dispute or refund, not the underlying transaction date. For example, hovering over the January 5 date on the disputes graph shows you the number of disputes opened on January 5, not the number of transactions on January 5 that were subsequently disputed. Also, the disputes graph shows the count of disputes, not the number of transactions disputed. A customer can file multiple disputes on a single transaction.

Failed payments typically include issuer declines, Radar declines, and failed API calls. Declined payments in the **Risk metrics** charts include only issuer declines and Radar blocks. We don’t consider failed API calls risky, so they’re excluded.

### Agentic account risk insights 

If Stripe detects a risk level of `elevated` or `highest` on the connected account, we provide agentic-generated explanations of the risks we see with risk insights to help you investigate. You can then make an informed decision to dismiss the review or reject the account. These insights can take up to 48 hours to display the first time you enable the tool.

Examples of indicators include:

- Related suspicious accounts in the Stripe network, such as those with a matching bank account that Stripe previously rejected for fraud.
- Suspicious business information and account or transaction activity, such as “This business shows strong card testing indicators: all charges are $1-$2 and 3 charges occurred within 12 seconds showing rapid retry behavior after declines. A single card was used for all charges with billing address changes between attempts, and one charge was blocked by fraud detection.”
- Mismatches between business location and login location.

### Risk history

The **Risk history** section shows previous reviews raised on the account and the actions your platform took to address them, such as pausing payouts and charges, setting reserves, and rejecting accounts. Your team can also take notes in this section for future reference.

## Request connected account identity

To research risk further, request that connected accounts verify their government-issued identity document and selfie. [Stripe Identity](https://docs.stripe.com/identity.md) is available as an add-on and can help reduce fraud risk.

1. On the [connected account details](https://docs.stripe.com/connect/dashboard/managing-individual-accounts.md) page, click the overflow menu (⋯), and choose **Request information**.
2. Select **Identity document** from the **Information** dropdown.
3. Set the consequence of not completing the verification before the deadline by selecting **Pause payouts** or **Pause payouts and payments** from the **Enforcement** dropdown.
4. Set the deadline for completing the verification using the **Condition** dropdowns. You can define the deadline as a time limit or as a total lifetime volume. To enforce the consequence immediately, select **Time limit** and **Immediately**.
5. Click **Send request** to immediately add the requirement to the connected account and display a remediation link that the account can use to fulfill the requirement.
6. Click **Copy** to provide the link to the connected account in your communication, if needed. Depending on your Stripe integration, Stripe might automatically notify the connected account of the requirement. If your platform automatically sends account links based on [account.updated](https://docs.stripe.com/connect/webhooks.md) webhooks, it might automatically notify the connected account.

## Take action on connected accounts

To take the following actions on a connected account, select the overflow menu (⋯) on the connected account details page.

When a connected account matches a Radar rule, you can reject the account or dismiss the review.

| Action | Description |
| --- | --- |
| **Raise a review** | Flag the account for manual investigation by your risk team. |
| **Pause payouts** | Hold funds while you investigate to reduce potential losses. |
| **Pause payments** | Stop the account from processing new transactions. |
| **Reject the account** | Permanently disable the account if you confirm it’s fraudulent. |
| **Set reserves** | Require a percentage of each transaction to be held as a reserve against future losses. |
| **Request identity verification** | Ask the connected account to verify their identity with a government-issued document and selfie, if you use [Stripe Identity](https://docs.stripe.com/identity.md). |

### Reject a connected account

Rejecting the account disables payments (and optionally, payouts). Stripe uses this risk factor to continue to improve our detection of financially risky accounts. Choose one of the following reasons as your primary determination of risk:

| Reason | Description |
| --- | --- |
| **fraud\_card\_casher** | The business’s behavior suggests they’re processing several stolen credit cards in a short amount of time with the intent of cashing out. For example, the business is both the buyer and the seller and uses stolen credit cards to quickly buy a large volume of goods. |
| **fraud\_card\_tester** | The business processes small (often in 0 USD - 5 USD range), repeated transactions (which often fail) from stolen credit cards in a short amount of time. |
| **fraud\_no\_intent\_to\_fulfill** | The business scams legitimate cardholders by tricking them into making purchases the business has no intention to fulfill or intends to fulfill with low quality or fake goods. |
| **fraud\_other** | You don’t know which fraud bucket qualifies. For example, the business’s KYC data looks fake. |
| **credit** | The business is legitimate, but at risk of delinquency. |
| **terms\_of\_service** | The business is prohibited or has other terms-of-service violations. |
| **other** | You reject the business for a reason unrelated to fraud, credit, or terms-of-service risk. |

> If you reject a connected account, you must contact Stripe Support to reverse the rejection.

Click **Reject**. Refresh the page to confirm the updated connected account status. If the account has a positive balance, your team can decide how to proceed. For example, you can transfer the balance to your platform to refund customers or to payout the balance to the business.

### Dismiss risk review

If you determine that the connected account isn’t risky enough to reject, you can dismiss the review for that particular rule for a period of time. This makes sure your team doesn’t review the same accounts repeatedly, but also lets you reevaluate later if the account continues to trigger the rule.

### Set reserves

To continue supporting connected accounts with elevated financial risks (such as long fulfillment timelines or elevated dispute and refund rates), you can set reserves to retain funds as a buffer against potential losses for your platform. Learn more about [reserves](https://docs.stripe.com/connect/connected-account-reserves.md).

To manage reserves, open the connected account in the Dashboard and select **Reserve funds**. You can review existing holds and reserve plans from the account’s **Manage reserves** page, including individual holds, releases, and planned release dates.

To set a reserve, you can create:

- A **One-time hold** to set aside an existing balance until a specified release date.
- A **Fixed reserve plan** to hold a percentage of future payments and release the funds on a specified date.
- A **Rolling reserve plan** to hold a percentage of future payments and release each held amount after a set number of days.

### Permissions

You must have the Connect Risk Analyst, Administrator, or Super Administrator [user role](https://docs.stripe.com/get-started/account/teams/roles.md) to view and take action on risk reviews.

- Stripe sends email notifications to Connect Risk Analyst team members of connected accounts we flag as `elevated` or `highest`.
- Admin team members can opt in to these notifications in their [communication preferences](https://dashboard.stripe.com/settings/communication-preferences#account) under the **highest risk accounts** option.

### Identity verification request notifications

If you request identity verification from a connected account, Stripe communications depend on your integration.

| Connected account access | Stripe communication |
| --- | --- |
| Stripe-hosted Dashboard | Stripe posts an alert in the Dashboard. Stripe also emails the connected account directing them to their Dashboard, where the connected account can satisfy the requirements. |
| Embedded Notifications Banner | Stripe posts an alert in the banner, where the connected account can satisfy the requirements. |
| None | If the connected account can’t access a Stripe-hosted Dashboard or the Embedded Notifications Banner, Stripe doesn’t notify the connected account of the requirement. In this case, you might need to send the connected account a [remediation link](https://docs.stripe.com/connect/dashboard/remediation-links.md) they can use to complete the requirements. |

### Identity verification request results

You can view the status of an identity verification request in the **Actions required** section of the connected account details page in your Dashboard.

When the connected account completes the requirement, Stripe sends an [account.updated](https://docs.stripe.com/connect/webhooks.md) webhook event and updates the **Verification attempts** section of the connected account details page in your Dashboard with the results of the check.

If a connected account fails the check, the consequences of the enforcement that you set, such as pausing payouts, begin after the time limit or volume limit elapses.
