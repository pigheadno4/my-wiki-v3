<!-- Source URL: https://docs.paypal.ai/growth/payouts/send-money/customize-web-ui -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Customize Web UI payouts

You can use the procedures in this section to improve payout governance and global payout capabilities using the Web UI.

## Pay recipients in their local currency

You can pay recipients in any supported currency, even if your PayPal account does not hold a balance in that currency. To do this:

1. <a href="/growth/payouts/send-money/use-web-ui#1-create-input-file" target="_blank" rel="noopener noreferrer">Create one input file</a> for each payout currency.
   <Note>An input file can payout only in one currency type. For local currency payouts, group recipients based on currency type and create multiple files.</Note>
2. <a href="/growth/payouts/send-money/use-web-ui#2-upload-input-file" target="_blank" rel="noopener noreferrer">Upload the input files one by one</a>. PayPal reviews the file and if valid, displays the Review your payment details page. The page contains the currency conversion fees and other currency exchange details, that PayPal calculates automatically.
3. Review and select **Send Payout**.

<Note>For more information about currency conversion, country exclusions, and restrictions, see <a href="/growth/payouts/reference/countries-supported-features#currency-conversion" target="_blank" rel="noopener noreferrer">Currency conversion</a>.</Note>

## Set up payout approval flow

You can add an approval flow to your payouts for proper governance over fund disbursement. To do this:

1. Log in to your PayPal business account.
2. Go to **Account Settings** > **Account Access** > **Manage Users** and select **Update**.
3. In the Users page, select **Manage Approvals**.
4. In the Approvals page, select **Get Started** for **Send payouts**.
5. In the pop-up window, choose the users who can approve payout requests and select **Done**.
6. Select **Yes, Turn On Approvals**.
7. Select **Close**. The Send Payout approvers page displays the users who can approve payout requests.

<Note>The user who creates a payout cannot approve the same payout.</Note>
