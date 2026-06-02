<!-- Source URL: https://developer.paypal.com/docs/log-in-with-paypal/integrate/generate-button/ -->
<!-- Fetched: 2026-04-16 -->

# Generate button

Follow these steps to generate the JavaScript for the Log in with PayPal button:

## Configure button

Modify the following fields to personalize the Log in with PayPal button. When you're finished, use the following dynamically generated Javascript.

- application ID (client ID): REPLACE_WITH_YOUR_APPLICATION_ID (create or find an application; requires login)
- auth end point: production / sandbox (must match the environment of the application client id being used)
- scope: openid (available scopes)
- container ID: lippButton
- responseType
- Code
- locale: English (US)
- theme: PayPal blue / neutral
- labelType: Log in with PayPal
- buttonSize: small
- FullPage: True
- return URL: REPLACE_WITH_YOUR_RETURN_URL (if the application specifies a return URL, this field must match)

Generate JavaScript

Test the generated button. Once it works to your satisfaction, add the following generated HTML code into your site.

Required fields are missing or malformed.

For recommendations on where to place this button on your site, see Button placement.

## Modify JavaScript

You can optionally modify the generated JavaScript button code with the following parameters:

| Parameter | Required | Description |
| --- | --- | --- |
| appid |  | The application ID (the client ID from PayPal app creation). Note: The application ID and client ID terms are used interchangeably. |
| authend | Optional | The authorization server URL: Pass sandbox for the test environment. Otherwise, for live, omit this value. |
| scope |  | The profile information requested (available scopes). |
| locale |  | Language and country specifier. |
| buttonSize |  | The button size specifier: sm. Small. md. Medium. lg. Large. |
| theme | Optional | The button styling: PayPal blue or neutral. |
| returnurl |  | The page to return to after successful login. |
| responseType |  | The response type specifier: code / id_token / code & id_token |
| fullpage |  | The full page specifier: true / false. Default is mini browser. |
| nonce | Optional | The nonce specifier can be a random number, for example 11111111. If you don't provide this parameter, the return url redirection behavior is mini browser. If you provide the parameter with a random number, it will redirect to parent browser. |
