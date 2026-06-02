<!-- Source URL: https://docs.paypal.ai/growth/disputes/set-up-accounts-environment -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up accounts and environment

Use these procedures to configure your PayPal business and sandbox accounts to manage disputes in the Resolution Center or to integrate with the Disputes API.

You can use the procedures in this section to ensure that your accounts and environment are set up to manage disputes.

## Set up sandbox account

<Tabs>
  <Tab title="Resolution Center">
    Use this path if you only need to test and manage disputes manually through the PayPal Resolution Center without integrating the Disputes API.

    1. <a href="https://www.paypal.com/signin?returnUri=https%3A%2F%2Fdeveloper.paypal.com%2Fdashboard%2F&intent=developer&ctxId=ul14c2e612301b4f5c99383ae8f762a937" target="_blank" rel="noopener noreferrer">Sign up for a developer account</a>. On successful signup, PayPal automatically creates your sandbox environment. The sandbox environment is a test environment that helps you mimic real-world transactions.
    2. Retrieve sandbox account credentials to log in to your PayPal sandbox account and access the Resolution Center. To do this:
       1. Select **Sandbox Accounts**. By default, the environment includes a business and personal account. To create more sandbox accounts, you can select **Create account**.
       2. Locate the account for which you want to get credentials, and select `⋮`.
       3. Select **View/Edit Account** to view the account email address and the system-generated password.
    3. Sign in to your <a href="https://www.sandbox.paypal.com/signin" target="_blank" rel="noopener noreferrer">PayPal sandbox account</a> using the personal sandbox credentials. In a separate browser session, sign in with the business sandbox credentials. When you test dispute workflows, use the personal account to create disputes and the business account to handle them. Verify the dispute status in both accounts.

  </Tab>

  <Tab title="Disputes API">
    Use this path if you plan to integrate the Disputes API and test automated dispute handling end to end.

    1. <a href="https://www.paypal.com/signin?returnUri=https%3A%2F%2Fdeveloper.paypal.com%2Fdashboard%2F&intent=developer&ctxId=ul14c2e612301b4f5c99383ae8f762a937" target="_blank" rel="noopener noreferrer">Sign up for a developer account</a>. On successful signup, PayPal automatically creates your sandbox environment. The sandbox environment is a test environment that helps you mimic real-world transactions. By default, the environment includes a business and personal account. When testing your app, you can use the personal account to create disputes and the business account to handle them. You can create additional business and personal accounts.

    2. Set up the sandbox environment:
       1. Go to your <a href="https://developer.paypal.com/dashboard/" target="_blank" rel="noopener noreferrer">PayPal developer account</a> and toggle to **Sandbox**.
       2. Go to **Apps & Credentials** and select **Create App**.
       3. Enter your app name, select **Type** as **Merchant**, select the sandbox business account to test your app, and select **Create App**. The app details page is displayed.
       4. Go to **Features** > **Add-on services**. By default, the **Customer disputes** checkbox is selected. If not, select it.
       5. Optional: Configure a webhook listener for the app and subscribe to events:
          1. In the app details page, go to **Sandbox Webhooks**.
          2. Select **Add Webhook**.
          3. Enter a **Webhook URL** (the server endpoint where notifications from PayPal are sent), select the events the app wants to subscribe to, and select **Save**.
          4. The webhook listener is successfully configured, and a **Webhook ID** is displayed. You can store the ID and use it in your app code to verify the source sending messages to your listener.
             For more information on webhooks, see <a href="https://developer.paypal.com/api/rest/webhooks/" target="_blank" rel="noopener noreferrer">Webhooks guide</a>. For the list of disputes events that the app can subscribe to, see <a href="/reference/webhook-events/disputes-v1" target="_blank" rel="noopener noreferrer">Webhook reference</a>.

    3. **Retrieve sandbox app credentials**: To integrate and test the Disputes API, you need the sandbox credentials (**Client ID** and **Client secret**) for your app. To retrieve them, see <a href="/developer/how-to/api/get-started#1-get-your-client-id-and-client-secret" target="_blank">Get your client ID and client secret</a>.

    4. **Get an access token**: To authenticate your API calls, get an access token using your client ID and client secret. For more information, see [Get started with PayPal REST APIs](https://docs.paypal.ai/developer/how-to/api/get-started#2-get-an-access-token)

    5. **Retrieve sandbox account credentials:** When you test your disputes integration end-to-end, you log in to your PayPal personal account, create a dispute, handle it through your PayPal business account, and check the dispute status in both accounts. You need sandbox login credentials for both accounts. For information on how to get these from your developer account, see <a href="/developer/how-to/api/get-started#3-get-sandbox-account-credentials" target="_blank" rel="noopener noreferrer"> Get sandbox account credentials</a>.

    6. Set up the development environment. This involves building your server, installing dependencies, verifying configuration files that the package managers use, and setting up the environment variables.

    ### Set up buyer-side credentials

    <Note>The procedures in this section apply only to the test simulations of the Disputes API.</Note>

    To create disputes or change dispute reasons as a buyer using the Disputes API, you need to set up buyer-side credentials. To do this:

    1. [Configure your REST app](#configure-your-rest-app).
    2. [Get buyer consent](#get-buyer-consent) for your sandbox personal account.
    3. [Use PayPal-Auth-Assertion request header](#use-paypal-auth-assertion-request-header) when you make API calls to create disputes or change dispute reasons as a buyer.

    #### Configure your REST app

    Contact your PayPal account manager to add the following scopes to your REST app:

    | Scope name       | Scope                                                   | Description                         |
    | ---------------- | ------------------------------------------------------- | ----------------------------------- |
    | `DISPUTE_CREATE` | `https://uri.paypal.com/services/disputes/create`       | Scope to create a dispute.          |
    | `UPDATE_BUYER`   | `https://uri.paypal.com/services/disputes/update-buyer` | Scope to change the dispute reason. |

    #### Get buyer consent

    You need to obtain buyer consent to create disputes or change dispute reasons on behalf of your sandbox personal account (buyer) using the Disputes API. To do this:

    1. Create a **Log in with PayPal** button:
       1. Complete the steps to <a href="https://developer.paypal.com/docs/log-in-with-paypal/integrate/#enable-log-in-with-paypal" target="_blank" rel="noopener noreferrer">Enable Log in with PayPal</a> in your PayPal developer account.
       2. Complete the steps to <a href="https://developer.paypal.com/docs/log-in-with-paypal/integrate/generate-button" target="_blank" rel="noopener noreferrer">Generate button</a>. When you do this, you can configure the following options:
          * `application ID (client ID)` as your app's client ID.
          * `container ID` as `lippButton`.
          * `auth end point` as `sandbox`. Confirm this is set to sandbox, as the field may default to production.
          * `scope` as either `https://uri.paypal.com/services/disputes/create` or `https://uri.paypal.com/services/disputes/update-buyer`.
          * `return URL` should match the one configured for your REST app in the previous step.
    2. Run your application.
    3. Under **Features** > **Add-on Services**, select the **Log in with PayPal** on your application.
    4. Log in with your sandbox personal account credentials as a buyer and approve the consent.

    #### Use PayPal-Auth-Assertion request header

    During the API test simulation, include the `PayPal-Auth-Assertion` request header in API calls to create disputes or change dispute reasons as a buyer.

    [Generate the JSON Web Token (JWT)](#generate-jwt-for-paypal-auth-assertion) and pass it in this request header to identify the buyer.

    ##### **Generate JWT for PayPal-Auth-Assertion** <a id="generate-jwt-for-paypal-auth-assertion" />

    Replace the following in the HTML code provided:

    * `CLIENT_ID` with your app's client ID.
    * `BUYER_EMAIL` with the buyer's email address.

    Run this code in any HTML sandbox environment or save it as an HTML file and open it in a browser. This generates a JWT that you can use in the `PayPal-Auth-Assertion` request header.

    ```html lines theme={null}
    <span id='cwppButton'></span>
    <html>
      <script>
        function base64url(source) {
          var encodedSource = btoa(source);
          encodedSource = encodedSource.replace(/=+$/, '');
          encodedSource = encodedSource.replace(/\+/g, '-');
          encodedSource = encodedSource.replace(/\//g, '-');
          return encodedSource;
        }
        function generateJWT() {
          var header = {"alg": "none", "typ": "JWT"};
          var data = {"iss":"CLIENT_ID", "email" : "BUYER_EMAIL" };
          document.write(base64url(JSON.stringify(header)) + "." +
          base64url(JSON.stringify(data)) + ".");
        }
      </script>
      <body onload="generateJWT()"/>
    </html>
    ```

    ### Common issues

    **Issue:** `PayPal-Auth-Assertion` header is ignored or rejected.\
    **Fix:** Verify that the JWT contains the correct `CLIENT_ID` and `BUYER_EMAIL`, and that you are using the sandbox personal account email for the buyer.

  </Tab>
</Tabs>

## Set up live account

<Tabs>
  <Tab title="Resolution Center">
    Use this path to manage disputes manually in production without building an API integration.

    Log in to your PayPal business account at the <a href="https://www.paypal.com/disputes/dashboard/" target="_blank" rel="noopener noreferrer">PayPal Business Dashboard</a>. No additional setup or configuration is required to use the Resolution Center in the live environment.

  </Tab>

  <Tab title="Disputes API">
    Use this path when you are ready to move your Disputes API integration from sandbox to production.

    <Note>**Partners**: To set up a partner account with connected integration, complete <a href="https://developer.paypal.com/docs/multiparty/#multi-party-form-wrapper" target="_blank" rel="noopener noreferrer">this form</a>. A PayPal representative will reach out to you. You can work with them to configure your Live account. Use the following procedure after your Live account is configured.</Note>

    1. Log in to your PayPal business account at the <a href="https://developer.paypal.com/" target="_blank" rel="noopener noreferrer">PayPal Developer Dashboard</a>.

    2. Switch to the **Live** environment.

    3. Go to **Apps & Credentials** and create a new app or select an existing app.

    4. Go to **Features** > **Other features**. By default, the **Customer disputes** checkbox is selected. If not, select it.

    5. Optional: Configure a webhook listener for the app and subscribe to events:

       1. On the app details page, go to **Live Webhooks**.
       2. Select **Add Webhook**.
       3. Enter a **Webhook URL** (the server endpoint where notifications from PayPal are sent), select the events the app wants to subscribe to, and select **Save**.
       4. The webhook listener is successfully configured, and a **Webhook ID** is displayed. You can store the ID and use it in your app code to verify the source sending messages to your listener.

       For more information on webhooks, see <a href="https://developer.paypal.com/api/rest/webhooks/" target="_blank" rel="noopener noreferrer">Webhooks guide</a>. For the list of dispute events that the app can subscribe to, see <a href="/reference/webhook-events/disputes-v1" target="_blank" rel="noopener noreferrer">Webhook reference</a>.

    6. Copy your **Client ID** and **Secret** for the live app.

    7. Optional: To download the files submitted as evidence, contact your PayPal account manager to add the following scopes to your REST app:
       1. In scopes - `DOCUMENTS_DISPUTES_DOWNLOAD`
       2. In claims - `dms_data_access_rule:all_of` and `dms_data_access_fields:account_number`

  </Tab>
</Tabs>
