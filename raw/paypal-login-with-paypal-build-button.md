<!-- Source URL: https://developer.paypal.com/docs/log-in-with-paypal/integrate/build-button/ -->

## <!-- Fetched: 2026-04-16 -->

title: Build button
slug: /docs/log-in-with-paypal/integrate/build-button/
createTime: '2024-08-15T05:52:53.173Z'
updateTime: '2025-10-21T02:30:08.458Z'

---

# Build button

Follow these steps to manually build the **Log in with PayPal** button:

## 1. Select button type

Choose if you want to use the branded **Log in with PayPal** button or to create your own.

- To create your own **Log in with PayPal** button, reference our [Button design guide](/docs/log-in-with-paypal/customize/button-design-guide/) .

- To use the branded **Log in with PayPal** button, use https://www.paypalobjects.com/devdoc/log-in-with-paypal-button.png for the button image location.

  **Note:** To ensure the button image stays in sync with PayPal branding, don't download the button image and host it on your own server.

## 2. Construct authorization endpoint

The authorization URL is called each time your users select the **Log in with PayPal** button. Construct the authorization endpoint according to the following template:

| https://www.sandbox.paypal.com/signin/authorize?flowEntry=static&client_id=CLIENT-ID&scope=LIST-OF-SCOPES&redirect_uri=RETURN-URL | Variable                                                                                                                                                                                                                                                                                                              | Description |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| client ID                                                                                                                         | ReplaceCLIENT-IDwith your app’s sandbox or live client ID. Example: ARfDleH_j-C17kxbdUzYivR70xP5Uy5N_DrFZVOvyZvNGBaPB_QNbwWkgF7lMsemGJycLRFVwaM                                                                                                                                                                       |
| list of scopes                                                                                                                    | ReplaceLIST-OF-SCOPESwith a space-separated list of scopes. You'll need to to includeopenid. See[Scope attributes](/docs/log-in-with-paypal/integrate/reference/#scope-attributes)for details on how attributes map to scopes. Example: openid profile email address https://uri.paypal.com/services/paypalattributes |
| return URL                                                                                                                        | ReplaceRETURN-URLwith the URL to return to after successful login. This URL must be encoded and match the Return URL set in**Apps & Credentials**in the Developer Dashboard. Example: https%3A%2F%2Fwww.myreturnurl.com&state=123456                                                                                  |

### Sample URL

https://www.sandbox.paypal.com/connect/?flowEntry=static&client_id= ARfDleH_j-C17kxbdUzYivR70xP5Uy5N_DvNGBaPB_QNbwWkgF7lMsemGJycLRFVwaM&response_type=code&scope=openid profile email address&redirect_uri=https%3A%2F%2Fwww.myreturnurl.com&state=123456## 3. Customize functionality
You can optionally use the following advanced parameters to customize your button:

| Parameter     | Description                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| response_type | code– to receive authentication code in the response. id_token– used only by direct instruction of your integration team.                     |
| fullPage      | To open the flow in a mini browser, do not pass this parameter. To open the Log in with PayPal flow as a full page in the same tab, passtrue. |

## 4. Get authorization code

When your users successfully log in to PayPal and consent to sharing their basic information, PayPal passes an authorization code to the return URL you specify.

| Parameter          | Description                                                                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| authorization code | The authorization code is appended as a parameter to the return URL after the user logs in and consents to share information with your website. |

### Sample URL

https://myreturnurl.com/?code={authorization_code}&scope=address%20openid%20profile%20email## Next steps

- [Get access token](/docs/log-in-with-paypal/integrate/#link-getaccesstoken)
