<!-- Source URL: https://docs.paypal.ai/growth/payouts/setup -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up accounts and environment for payouts

You can use the procedures in this section to ensure that your accounts and environment are set up to send payouts.

## Set up business account for Web UI file upload

Work with your account manager, call 1-888-221-1161, or <a href="https://www.paypal.com/payoutsweb/landing?_ga=2.176099874.1452783257.1750650615-149702003.1736315018" target="_blank" rel="noopener noreferrer">contact PayPal</a> to request Payouts access. After successful activation, you can go to your account and send payouts through file upload.

## Set up SFTP account for large-batch file transfer

1. <a href="https://www.paypal-support.com/" target="_blank">Contact PayPal</a> or your PayPal account manager to onboard you to PayPal’s DropZone SFTP server and to enable Payouts. As part of onboarding, PayPal asks you for your server authentication preference – password or SSH.
2. If your authentication preference is SSH, generate a public and private SSH key-pair and share the public SSH key with PayPal.
3. PayPal onboards you to the DropZone SFTP server. DropZone is PayPal’s SFTP platform. The account setup might take up to 48 hours. After this, PayPal sends an encrypted email to your primary email address with the DropZone SFTP server access credentials.
4. Log in to your <a href="https://www.paypal.com/mep/dashboard/" target="_blank">PayPal business account</a> and add users who can access the SFTP server:
   1. Click on your profile logo and from the dropdown menu, select **Account settings**.
   2. On the Account access page, click **Update** next to Secure FTP.
   3. Follow the on-page instructions to add users. When finished, the final page displays the list of SFTP server users and their information.
5. Use any SFTP client of your choice (FileZilla, WinSCP, or Cyberduck) and access `dropzone.paypal.com` (production) or `dropzone.es-ext.paypalcorp.com` (sandbox).
6. Log in with the following credentials:
   - **Username**: SFTP account name sent in the email from PayPal
   - **Password**: Password sent in the email from PayPal

   OR
   - **Username**: SFTP account name sent in the email from PayPal
   - **SSH key**: Private key generated in step 2

### Sandbox DropZone SFTP server credentials

- **Sandbox endpoint/URL**: `dropzone.es-ext.paypalcorp.com`
- **Destination host port**: `22`
- **Username**: Sent in the encrypted mail from PayPal after SFTP server onboarding
- **Your private SSH key**

### Production DropZone SFTP server credentials

- **Production endpoint/URL**: `dropzone.paypal.com`
- **Destination host port**: `22`
- **Username**: Sent in the encrypted mail from PayPal after SFTP server onboarding
- **Your private SSH key**

## Set up sandbox account for Payouts API integration

1. <a href="https://www.paypal.com/signin?returnUri=https%3A%2F%2Fdeveloper.paypal.com%2Fdashboard%2F&intent=developer&ctxId=ul14c2e612301b4f5c99383ae8f762a937" target="_blank">Sign up for a developer account</a>. On successful signup, PayPal automatically creates your sandbox environment. The sandbox environment is a test environment that helps you mimic real-world transactions. By default, the environment includes a business and personal account. When testing your app, you can use the business account to send payouts and the personal account to receive. You can create multiple additional business and personal accounts.

2. Set up the sandbox environment:
   1. Go to your [PayPal developer account](https://developer.paypal.com/dashboard/) and toggle to **Sandbox**.
   2. Go to **Apps & Credentials** and select **Create App**.
   3. Enter your app name, select **Type** as **Merchant**, select the sandbox business account to test your app, and select **Create App**. The app details page is displayed.
   4. Configure a webhook listener for the app and subscribe to events:
      - Go to **Features** > **Sandbox Webhooks**.
      - Select **Add Webhook**.
      - Enter a **Webhook URL** (the server endpoint where notifications from PayPal are sent), select the events the app wants to subscribe to, and select **Save**.
        The webhook listener is successfully configured and a **Webhook ID** is displayed. You can store the ID and use it in your app code to verify the source sending a message to your listener. For more information on webhooks, see [Webhooks guide](https://developer.paypal.com/api/rest/webhooks/). For the list of payouts events that the app can subscribe to, see <a href="/reference/webhook-events/payouts-v1" target="_blank">Webhook reference</a>.

3. **Retrieve sandbox app credentials**: To integrate and test the Payouts API successfully, you need the sandbox credentials (**Client ID** and **Client secret**) for your app. To retrieve them, see <a href="/developer/how-to/api/get-started#1-get-your-client-id-and-client-secret" target="_blank">Get your client ID and client secret</a>.

4. **Retrieve sandbox account credentials**: When you test your payout integration end-to-end, you run your app, start a payout, log in to your business and personal PayPal accounts, and check that money moves from your business to your personal account. If you send a payout to a Venmo account, you check that the money moves from your business account. You require sandbox login credentials for both accounts. For information on how to get these from your developer account, see <a href="/developer/how-to/api/get-started#3-get-sandbox-account-credentials" target="_blank">Get sandbox account credentials</a>.

5. Set up the development environment. This involves building your server, installing dependencies, verifying configuration files that the package managers use, and setting up the environment variables.

## Set up live account

To use PayPal Payouts, you need a verified PayPal business account. After creating your production business account:

1. **Verify your account**:
   1. Complete [identity verification](https://www.paypal.com/policy/flow/verifyCip).
   2. Complete [email verification](https://www.paypal.com/in/cshelp/article/how-do-i-confirm-my-email-address-help138).
   3. [Link a bank account or credit card](https://www.paypal.com/businessexp/money/addbank) to your PayPal account.

2. **Request payouts activation**: [Contact PayPal support](https://www.paypal.com/payoutsweb/landing) to enable Payouts on your account.

## Fund your account

To successfully send payouts, ensure your PayPal account has sufficient funds.

1. **Link a funding source**: Log in to your PayPal account and link a bank account or credit card.
2. **Add funds to your PayPal account**:
   1. Navigate to the **Wallet** section of your PayPal account.
   2. Transfer money from your linked bank account or card to your PayPal balance.
3. **Set up auto-funding**: Enable auto-funding in your PayPal account settings to ensure your account always has sufficient funds for payouts.
4. **Monitor transactions**: Regularly review your account balance and transaction history to ensure smooth payouts.
