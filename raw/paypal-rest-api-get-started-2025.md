<!-- Source URL: https://docs.paypal.ai/developer/how-to/api/get-started -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started with PayPal REST APIs

Current PayPal APIs use REST, authenticate with OAuth 2.0 access tokens, and return HTTP response codes and JSON responses. You can test US integrations with a <a href="https://developer.paypal.com/home/" target="_blank">PayPal Developer</a> account.

To try these REST APIs without a PayPal Developer account, you can use Postman. Learn more about this in our <a href="https://developer.paypal.com/api/rest/postman" target="_blank">Postman guide</a>.

To explore PayPal's REST API descriptions, generate code for your API clients, and import OpenAPI documents into compatible third-party tools, see the <a href="https://github.com/paypal/paypal-rest-api-specifications" target="_blank">PayPal REST API specifications on GitHub</a>.

<br />

> **Important:** You need a <a href="https://www.paypal.com/business/open-business-account" target="_blank">PayPal Business account</a> to:<br />
>
> - Go live with integrations.<br />
> - Test integrations outside of the US.

<br />

## 1. Get your client ID and client secret

PayPal integrations use a client ID and client secret to authenticate API calls:

- A client ID identifies an app. You need a client ID to get a PayPal payment button and standard credit and debit card fields.

- A client secret authenticates a client ID. To call PayPal APIs, you exchange your client ID and client secret for an access token. Keep your client secret safe.

Here's how to get your client ID and client secret:

1. Select <a href="https://developer.paypal.com/dashboard/" target="_blank">Log in to Dashboard</a> and log in to your account or sign up for a new account.
2. Select **Apps & Credentials**.
3. New accounts come with a default application in the **REST API apps** section. To create a new project, select **Create App**.
4. Copy the client ID and client secret for your app.

<br />

## 2. Get an access token

You exchange your client ID and client secret for an access token, which you use for authentication when calling PayPal REST APIs.

You can call the PayPal OAuth API in any language. The following examples show you how to get your access token using cURL or Postman.

<Tabs>
  <Tab title="cURL">
    ```bash theme={null}
    curl -v -X POST "https://api-m.sandbox.paypal.com/v1/oauth2/token" \
    -u "CLIENT_ID:CLIENT_SECRET" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "grant_type=client_credentials" 
    ```
  </Tab>

  <Tab title="Postman">
    In the Postman app:

    1. Set the verb to **POST**.
    2. Enter [https://api-m.sandbox.paypal.com/v1/oauth2/token](https://api-m.sandbox.paypal.com/v1/oauth2/token) as the request URL.
    3. On the **Authorization** tab, set up authorization:
       1. For **TYPE**, select **Basic Auth**.
       2. In **Username**, enter your client ID.
       3. In **Password**, enter your client secret.
    4. On the **Body** tab, complete these settings:
       1. Select the **x-www-form-urlencoded** option.
       2. In the **KEY** field, enter grant\_type.
       3. In the **VALUE** field, enter. **client\_credentials**.
    5. Select **Send**.

  </Tab>
</Tabs>

### Sample response

PayPal returns an access token and the number of seconds for which the access token is valid, as shown in the following example.

```bash theme={null}
{
  "scope": "https://uri.paypal.com/services/invoicing https://uri.paypal.com/services/disputes/read-buyer https://uri.paypal.com/services/payments/realtimepayment https://uri.paypal.com/services/disputes/update-seller https://uri.paypal.com/services/payments/payment/authcapture openid https://uri.paypal.com/services/disputes/read-seller https://uri.paypal.com/services/payments/refund https://api-m.paypal.com/v1/vault/credit-card https://api-m.paypal.com/v1/payments/.* https://uri.paypal.com/payments/payouts https://api-m.paypal.com/v1/vault/credit-card/.* https://uri.paypal.com/services/subscriptions https://uri.paypal.com/services/applications/webhooks",
  "access_token": "A21AAFEpH4PsADK7qSS7pSRsgzfENtu-Q1ysgEDVDESseMHBYXVJYE8ovjj68elIDy8nF26AwPhfXTIeWAZHSLIsQkSYz9ifg",
  "token_type": "Bearer",
  "app_id": "APP-80W284485P519543T",
  "expires_in": 31668,
  "nonce": "2020-04-03T15:35:36ZaYZlGvEkV4yVSz8g6bAKFoGSEzuy3CQcz3ljhibkOHg"
}
```

### Make API calls

When you make API calls, replace `ACCESS-TOKEN` with your access token in the authorization header: `-H Authorization: Bearer ACCESS-TOKEN`. When your access token expires, call `/v1/oauth2/token` again to request a new access token.

## 3. Get sandbox account credentials

The PayPal sandbox is a test environment that mirrors real-world transactions. By default, PayPal developer accounts have 2 sandbox accounts: a personal account for buying and a business account for selling. You'll get the login information for both accounts. Watch sandbox money move between accounts to test API calls.

Take the following steps to get sandbox login information for business and personal accounts:

1. Log into the <a href="https://developer.paypal.com/dashboard/" target="_blank">Developer Dashboard</a>.
2. Select **Testing Tools** > **Sandbox Accounts**. To create more sandbox accounts, you can select **Create account**.
3. Locate the account for which you want to get credentials, and select `⋮`.
4. To see mock information, such as the account email address and a system-generated password, select **View/Edit Account**.
5. Go to `sandbox.paypal.com/signin/`, and sign in with the personal sandbox credentials. In a separate browser, sign in with the business sandbox credentials.
6. Make API calls with your app's access token to see sandbox money move between the personal and business accounts.

## See also

- <a href="https://developer.paypal.com/tools/sandbox/" target="_blank">Sandbox testing guide</a>
- <a href="https://developer.paypal.com/docs/multiparty/" target="_blank">Multiparty payment solutions</a>
- <a href="https://developer.paypal.com/api/rest/webhooks/" target="_blank">Webhooks</a>
