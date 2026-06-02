<!-- Source URL: https://docs.stripe.com/radar/radar-for-platforms -->
<!-- Fetched: 2026-05-10 -->

# Radar for Platforms

Use Stripe tools to reduce buyer and connected account risk.

Stripe has developed risk tooling for Connect platforms to help you more effectively prevent, detect, and mitigate both buyer risk and financially risky connected accounts (for example, fraud risk).

Radar for Platforms helps your platform manage risk end-to-end:

- Identify potential financial risk using machine learning generated risk scores and customized rules engines
- Investigate connected accounts using risk metrics and indicators
- Gather additional information using document verification or a selfie confirmation
- Take action on transactions and connected accounts (including setting reserves)

### Risk signals through the API (Private preview)

In addition to Dashboard-based risk assessment, Radar for Platforms provides programmatic access to risk signals through the API. These signals enable you to build automated workflows and integrate risk data directly into your platform’s operations. The following signal categories are available in private preview. To request access to the private preview, contact your Stripe account team.

- **Account fraud signal**: Detect connected accounts engaging in fraudulent activity, such as misrepresenting goods or services, processing unauthorized transactions, or committing first-party fraud.
- **Account insolvency signal**: Identify connected accounts showing financial distress indicators that might lead to unfulfilled orders, increased disputes, or inability to cover refunds. Early detection helps you take proactive steps such as setting reserves before losses materialize.
- **Fraudulent website signal**: Flag connected accounts operating deceptive websites, including sites with misleading product claims, fake storefronts, or content that doesn’t match the stated business model.

## Request early access

## Identify potential financial risk

Radar for Platforms uses machine learning from millions of processed payments to generate risk scores for individual transactions and connected accounts as a whole. Each score receives one of the following risk levels: `normal`, `elevated`, `highest`, or `not assessed`.

### Risk scores and levels

Stripe enables its connected account risk levels by default as connected account-level rules in your Radar rules page. Stripe identifies connected accounts scored as `highest` or `elevated` for review. We base this on their probability of financial loss because of fraud or insolvency risk. The score correlates to the probability that an account would cause losses to your platform.

- `highest` risk, or a score of 90 or higher, indicates a probability of over 90% .
- `elevated` risk, or a score of 50-89, indicates a probability of 50% to 89%.

Account risk scores and levels update each time a new event occurs, such as a transaction or a change in business information. Stripe also provides risk indicators to explain the assigned risk level, such as transaction patterns, connected account behavior, or connected account information that matches previous fraudulent activity. [Transaction risk scores and levels](https://docs.stripe.com/radar/risk-evaluation.md#risk-outcomes) behave the same for platforms as for direct Stripe accounts.

> We recommend using machine learning-generated risk factors together with other risk factors to make holistic decisions about what additional information to request and what actions to take.

### Custom rule creation

You can customize the criteria for both connected account and transaction rules to suit the unique risks of your business. You can take one of the following actions when [creating your rules](https://docs.stripe.com/radar/rules.md):

#### Transactions

- Request 3DS
- Allow
- Block
- Review

#### Connected accounts

- Raise a review
- Pause payouts and raise a review

For a complete list of supported attributes in rule creation, see our [transaction rule attributes](https://docs.stripe.com/radar/rules/supported-attributes.md) and [connected account rule attributes](https://docs.stripe.com/radar/rules/supported-attributes.md?payment-method=card&connect-loss-liability-owner=platform#attributes-for-platforms).

### Connected account reviews

After you write your Radar rules, we alert you when any of your connected accounts match a rule by highlighting these accounts on your Home page. Go to either the **Radar rule match** queue of your [accounts list view](https://docs.stripe.com/connect/dashboard/viewing-all-accounts.md) or the **Reviews** tab in Radar to view accounts that match any of your rules. You can filter this list by the matched rule and risk level assigned.

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

### Risk indicators

If Stripe detects a risk level of `elevated` or `highest` on the connected account, our agent explains the risks we see with risk indicators to help you investigate. Then you can make an informed decision to confirm or deny the account risk. Examples of indicators include:

- Related suspicious accounts in the Stripe network
- Suspicious business information and account or transaction activity
- Mismatches between business location and login location

### Risk history

The **Risk history** section shows previous reviews raised on the account and the actions your platform took to address them, such as pausing payouts and charges, setting reserves, and rejecting accounts. Your team can also take notes in this section for future reference.

## Request connected account identity

One way to further research risk is to ask to verify the connected account’s government-issued identity document and selfie.

1. On the [connected account details page](https://docs.stripe.com/connect/dashboard/managing-individual-accounts.md), click the overflow menu ⋯ and choose **Request information**.
1. In the dialog, select **Identity document** from the **Information** drop-down.
1. Set the consequence of not completing the verification before the deadline by selecting **Pause payouts** or **Pause payouts and payments** from the **Enforcement** drop-down.
1. Set the deadline for completing the verification using the **Condition** drop-downs. You can define the deadline as a time limit or as a total lifetime volume. To enforce the consequence immediately, select **Time limit** and **Immediately**.
1. Click **Send request** to immediately add the requirement to the connected account and display a remediation link that the account can use to fulfill the requirement.
1. Click **Copy** to provide the link to the connected account in your communication, if needed. Depending on your Stripe integration, Stripe might automatically notify the connected account of the requirement. If your platform automatically sends account links based on [account.updated](https://docs.stripe.com/connect/webhooks.md) webhooks, it might automatically notify the connected account.

## Take action on connected accounts

You can take the following actions against a connected account by clicking the overflow menu ⋯ on the connected account details page:

- Pause payments
- Pause payouts
- Reject the account (which also pauses payments and, optionally, payouts)
- Set reserves

When a connected account has a Radar rule match, to close the review, you must either reject the account or dismiss the review.

### Reject a connected account

Rejecting the account disables payments (and optionally, payouts). Stripe uses this risk factor to continue to improve our detection of financially risky accounts. Choose one of the following reasons as your primary determination of risk:

- **fraud_card_casher**: The business’s behavior suggests they’re processing several stolen credit cards in a short amount of time with the intent of cashing out. For example, the business is both the buyer and the seller and uses stolen credit cards to quickly buy a large volume of goods.
- **fraud_card_tester**: The business processes small (often in 0 USD - 5 USD range), repeated transactions (which often fail) from stolen credit cards in a short amount of time.
- **fraud_no_intent_to_fulfill**: The business scams legitimate cardholders by tricking them into making purchases the business has no intention to fulfill or intends to fulfill with low quality or fake goods.
- **fraud_other**: You aren’t sure which fraud bucket qualifies. For example the business’s KYC data looks fake.
- **credit**: The business is legitimate but at risk of delinquency.
- **terms_of_service**: The business is prohibited, or has other terms-of-service violations.
- **other**: You’re rejecting the business for any reason unrelated to fraud, credit, or terms-of-service risk.

> After you reject a connected account, reversal is difficult. You must contact Stripe Support to un-reject it.

Click **Reject**. Refresh the page to confirm the updated connected account status. If the account has a positive balance, your team can decide how to proceed. For example, you can transfer the balance to your platform to refund customers or to payout the balance to the business.

### Dismiss risk review

If you determine that the connected account isn’t risky enough to reject, you can dismiss the review for that particular rule for a period of time. This makes sure your team doesn’t review the same accounts repeatedly, but also let you reevaluate later if the account continues to trigger the rule.

### Set reserves

If you determine a connected account isn’t fraudulent but you’re concerned about their exposure (such as businesses that have long delivery windows or high dispute and refund trends) you can use a reserve plan to set aside funds from each transaction to reduce potential losses. Reserves automatically adjust your exposure and allow your platform to support businesses that might otherwise be too risky. See [reserves](https://docs.stripe.com/connect/connected-account-reserves.md) to learn more.

### Permissions

You must have the Connect Risk Analyst, Administrator, or Super Administrator [user role](https://docs.stripe.com/get-started/account/teams/roles.md) to view and take action on risk reviews.

- Stripe sends email notifications to Connect Risk Analyst team members of connected accounts we flag as `elevated` or `highest`.
- Admin team members can opt in to these notifications in their communication preferences under the **highest risk accounts** option.

### Identity verification request notifications

If you request identify verification from a connected account, Stripe communications depend on your integration:

- If the connected account has access to a Stripe-hosted Dashboard, Stripe posts an alert there. Stripe also emails the connected account directing them to their Dashboard, where the connected account can satisfy the requirements.
- If the connected account has access to the Embedded Notifications Banner, Stripe posts an alert there, where the connected account can satisfy the requirements.
- If the connected account can’t access a Stripe-hosted Dashboard or the Embedded Notifications Banner, Stripe doesn’t directly notify the connected account of the requirement. In this case, you might need to send the connected account a [remediation link](https://docs.stripe.com/connect/dashboard/remediation-links.md) they can use to complete the requirements.

### Identity verification request results

You can view the status of an identity verification request in the **Actions required** section of the connected account details page inyour Dashboard.

When the connected account completes the requirement, Stripe sends an [account.updated](https://docs.stripe.com/connect/webhooks.md) webhook event and updates the **Verification attempts** section of the connected account details page in your Dashboard with the results of the check.

If a connected account fails the check, the consequences of the enforcement that you set, such as pausing payouts, begin after the time limit or volume limit elapses.

## Apply Radar rules to direct charges

Radar for Fraud Teams runs your Radar rules on payments made to your platform, including transactions where your platform is the [merchant of record](https://docs.stripe.com/connect/merchant-of-record.md).

To apply your Radar rules on transactions where your connected account is the merchant of record, like [direct charges](https://docs.stripe.com/connect/charges.md#direct) you must enable Radar for Platforms.

1. In the Dashboard, go to **Radar** > **Risk controls**.
1. Click **Platform payment controls**.
1. Choose who manages fraud prevention:
   - **Only my platform controls fraud prevention rules and settings**
     - Your platform’s Radar rules and settings apply to all payments, including direct charges on connected accounts.
     - Your connected accounts can’t manage Radar, write their own rules, or change Radar settings.
     - Connected accounts can’t see your platform’s rules, but can see when a platform rule blocked their payments.
     - This setting overrides a connected account’s own Radar rules, if they exist.
   - **Both my platform and connected accounts control fraud prevention**
     - Your platform’s Radar rules and settings apply to all payments, including direct charges on connected accounts.
     - Connected accounts can also configure their own Radar rules.
     - Evaluation order: your platform’s rules run first, followed by the connected account’s rules. For example, if your platform allows a payment, a connected account rule can still block or review it. If a payment matches rules set by both your platform and the connected account, the platform’s rule has priority.

> These settings apply only to connected accounts that are controlled solely by your platform.

### Hide Radar from connected accounts

If you set **Only my platform controls fraud prevention rules and settings**, you can also choose whether connected accounts can see Radar in their Dashboard.

- **Show Radar to connected accounts**: Connected accounts can view outcomes but can’t change Radar rules or settings.
- **Hide Radar from connected accounts**: Radar doesn’t appear in their Dashboard.
