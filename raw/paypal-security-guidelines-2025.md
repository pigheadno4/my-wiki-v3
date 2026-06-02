<!-- Source URL: https://docs.paypal.ai/developer/how-to/security-guidelines -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# PayPal security guidelines for developers

Creating strong, secure payment systems keeps both your app and your customers' private information safe. Learn about and use PayPal's security guidelines, tools, and best practices when you integrate PayPal as a payment option to keep your customers and your app secure.

## Overview

PayPal provides a robust set of APIs and SDKs for integrating payments into your applications. Security is a top priority, and PayPal enforces strict guidelines and provides tools to help developers protect sensitive data, authenticate securely, and prevent fraud.

When integrating with PayPal, keep the following principles in mind:

- Implement IP restrictions for API access.
- Never store full credit card details.
- Encrypt any stored customer or transaction data.
- Comply with PCI DSS requirements.
- Implement HTTP Strict Transport Security (HSTS).
- Prevent brute force attacks by limiting API requests and adding timeouts.
- Conduct regular security reviews and stay updated with PayPal's advisories.

## General security requirements and guidelines

The following security requirements and guidelines apply to all PayPal integrations and help protect both your application and your customers' sensitive payment information from unauthorized access and potential security threats.

### Use Open Authorization (OAuth) 2.0 for all API authentication

PayPal uses OAuth 2.0 as the standard authentication mechanism for all REST API integrations. OAuth 2.0 provides secure, token-based authentication, allowing applications to access PayPal APIs without exposing user credentials. The process involves obtaining an access token using your client ID and secret, which is then used to authorize API requests.

For a detailed overview of how OAuth 2.0 works with PayPal, see the [PayPal Authentication Guide](https://developer.paypal.com/api/rest/authentication/).

To get an access token, your server sends a `POST` request to the PayPal OAuth endpoint with your client credentials. PayPal responds with a short-lived access token, which you use in the `Authorization` header for subsequent API calls.

For step-by-step instructions and code samples, see [Get an Access Token](https://developer.paypal.com/reference/get-an-access-token/).

### Always use HTTPS for all API and SDK requests

All communication with PayPal APIs and SDKs must use HTTPS to ensure data is encrypted in transit and protected from interception or tampering. HTTPS is required for PCI DSS compliance and is enforced by PayPal for all endpoints. Using HTTPS also ensures that sensitive information, such as credentials and payment data, is never sent in plain text.

Learn more about HTTPS requirements in the [PayPal Security Guidelines](https://developer.paypal.com/api/rest/reference/info-security-guidelines/) and [Secure Communications](https://developer.paypal.com/api/rest/reference/info-security-guidelines/#link-securecommunications).

### Never expose your client secret or API credentials in client-side code

Your client secret and API credentials must always be kept confidential and used only on the server side. Exposing these credentials in client-side cod, such as JavaScript running in the browser, can lead to credential theft and unauthorized access to your PayPal account.

For best practices on protecting your credentials, see [Secure Your API Credentials](https://developer.paypal.com/community/blog/secure-your-api-credentials/).

PayPal provides tools for managing and rotating API credentials, including the ability to generate, revoke, and monitor credentials in the developer dashboard. For more information, see [Get started with PayPal REST APIs](https://developer.paypal.com/api/rest/).

### Store credentials securely using environment variables or secure vaults

Sensitive credentials should be stored in environment variables or secure vaults, not in source code or configuration files. This reduces the risk of accidental exposure through version control or code sharing. Use secrets management tools or environment variable configuration supported by your deployment platform.

For more on secure storage, see [Secure Your API Credentials](https://developer.paypal.com/community/blog/secure-your-api-credentials/) and [Authentication Requirements](https://developer.paypal.com/api/rest/reference/info-security-guidelines/#link-authenticationrequirements).

### Rotate API credentials regularly and remove unused credentials

Regularly rotating your API credentials and removing any that are no longer in use minimizes the risk if credentials are ever compromised. PayPal allows you to manage and rotate credentials in the developer dashboard, and you should establish a schedule for credential rotation as part of your security policy.

### Validate all webhook signatures to ensure authenticity

Always verify webhook signatures using PayPal's verification API before processing events. This ensures the event is genuine and untampered, protecting your application from spoofed or malicious notifications.

For implementation details, see [Webhooks](https://developer.paypal.com/api/rest/webhooks/).

### Keep all dependencies, SDKs, and libraries up to date

Regularly update all dependencies, SDKs, and libraries to patch security vulnerabilities and benefit from the latest security improvements. Outdated software can expose your application to known exploits.

See [JavaScript SDK Best Practices](https://developer.paypal.com/sdk/js/best-practices/) for more information.

### Use Transport Layer Security (TLS) 1.2 or higher

Ensure your servers and clients support TLS 1.2 or higher for all communications with PayPal. TLS provides strong encryption and is required for PCI DSS compliance. PayPal endpoints do not support older, less secure protocols.

Read more about TLS requirements in [Secure communications](https://developer.paypal.com/reference/guidelines/info-security-guidelines/#secure-communications).

### Enable two-factor authentication (2FA) on your PayPal account

Enable 2FA to add an extra layer of security to your PayPal account and developer dashboard. 2FA helps prevent unauthorized access, even if your password is compromised.

For more information, see [Enable and Configure Two-Factor Authentication](https://developer.paypal.com/community/blog/2-factor-authentication/).

### Monitor and log all payment and API activity for suspicious behavior

Implement logging and monitoring for all payment and API activity to detect and respond to suspicious or unauthorized actions. Monitoring helps you identify fraud, abuse, or operational issues quickly.

### Follow the principle of least privilege for API credentials

Grant only the minimum permissions necessary for each API credential to reduce risk if credentials are compromised. Use separate credentials for different environments and roles.

### Do not log sensitive information such as access tokens or payment details

Never log sensitive data such as access tokens, client secrets, or full payment details to prevent accidental exposure. Logging sensitive data can lead to data breaches and non-compliance with PCI DSS.

## Integration-specific security guidelines

PayPal offers several integration paths, each with unique security considerations beyond the general guidelines. The following sections outline specific security requirements, best practices, and code examples for API, SDK, and webhook integrations.

### API integration path

The API integration path is for developers who interact directly with PayPal's REST APIs from their server-side applications. Custom payment flows, order management, and other advanced integrations in which you need to securely obtain access tokens, create and capture orders, and handle webhooks, typically use API integration.

#### Security requirements

- Use OAuth 2.0 for all API authentication.
- Always use HTTPS for all API requests.
- Never expose your client secret or API credentials in client-side code.
- Store credentials securely (environment variables or secure vaults).
- Rotate API credentials regularly and remove unused credentials.
- Validate all webhook signatures.
- Use TLS 1.2 or higher.
- Enable two-factor authentication (2FA) on your PayPal account.
- Monitor and log all payment and API activity.
- Do not log sensitive information such as access tokens or payment details.

#### Security best practices

- Never hardcode credentials in your application.
- Use environment variables or a secrets manager.
- Validate all incoming webhook events.
- Keep all dependencies and SDKs up to date.
- Enforce least privilege for API credentials.
- Regularly review and rotate credentials.
- Encrypt sensitive data at rest and in transit.

#### Back-end server code samples

The following code samples demonstrate how to obtain an OAuth 2.0 access token from PayPal in various programming languages. This is the first step required for any secure API integration and should be implemented on your back-end server, never in client-side code.

<Tabs>
  <Tab title="cURL" default>
    ```bash theme={null}
    curl -v https://api-m.sandbox.paypal.com/v1/oauth2/token \
      -u "CLIENT_ID:CLIENT_SECRET" \
      -H "Accept: application/json" \
      -H "Accept-Language: en_US" \
      -d "grant_type=client_credentials"
    ```
  </Tab>

  <Tab title="Java">
    ```java theme={null}
    import java.net.*;
    import java.io.*;
    import java.util.Base64;

    public class PayPalToken {
        public static void main(String[] args) throws Exception {
            String clientId = "CLIENT_ID";
            String clientSecret = "CLIENT_SECRET";
            String auth = Base64.getEncoder().encodeToString((clientId + ":" + clientSecret).getBytes());

            URL url = new URL("https://api-m.sandbox.paypal.com/v1/oauth2/token");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Authorization", "Basic " + auth);
            conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            conn.setDoOutput(true);

            OutputStream os = conn.getOutputStream();
            os.write("grant_type=client_credentials".getBytes());
            os.flush();

            BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String inputLine;
            StringBuffer content = new StringBuffer();
            while ((inputLine = in.readLine()) != null) {
                content.append(inputLine);
            }
            in.close();
            System.out.println(content.toString());
        }
    }
    ```

  </Tab>

  <Tab title="JavaScript (Node.js)">
    ```nodejs theme={null}
    const fetch = require('node-fetch');
    const clientId = 'CLIENT_ID';
    const clientSecret = 'CLIENT_SECRET';

    fetch('https://api-m.sandbox.paypal.com/v1/oauth2/token', {
      method: 'POST',
      headers: {
        'Authorization': 'Basic ' + Buffer.from(`${clientId}:${clientSecret}`).toString('base64'),
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: 'grant_type=client_credentials'
    })
      .then(res => res.json())
      .then(data => console.log(data));
    ```

  </Tab>

  <Tab title=".NET (C#)">
    ```csharp theme={null}
    using System;
    using System.Net.Http;
    using System.Net.Http.Headers;
    using System.Text;
    using System.Threading.Tasks;

    class Program {
        static async Task Main() {
            var client = new HttpClient();
            var byteArray = Encoding.ASCII.GetBytes("CLIENT_ID:CLIENT_SECRET");
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Basic", Convert.ToBase64String(byteArray));
            var content = new StringContent("grant_type=client_credentials", Encoding.UTF8, "application/x-www-form-urlencoded");
            var response = await client.PostAsync("https://api-m.sandbox.paypal.com/v1/oauth2/token", content);
            string result = await response.Content.ReadAsStringAsync();
            Console.WriteLine(result);
        }
    }
    ```

  </Tab>

  <Tab title="PHP">
    ```php theme={null}
    <?php
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, "https://api-m.sandbox.paypal.com/v1/oauth2/token");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, "grant_type=client_credentials");
    curl_setopt($ch, CURLOPT_USERPWD, "CLIENT_ID:CLIENT_SECRET");
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        "Accept: application/json",
        "Accept-Language: en_US"
    ]);
    $result = curl_exec($ch);
    curl_close($ch);
    echo $result;
    ?>
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={null}
    import requests
    from requests.auth import HTTPBasicAuth

    url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
    auth = HTTPBasicAuth('CLIENT_ID', 'CLIENT_SECRET')
    headers = {"Accept": "application/json", "Accept-Language": "en_US"}
    data = {"grant_type": "client_credentials"}

    response = requests.post(url, headers=headers, data=data, auth=auth)
    print(response.json())
    ```

  </Tab>

  <Tab title="Ruby">
    ```ruby theme={null}
    require 'net/http'
    require 'uri'
    require 'base64'

    uri = URI('https://api-m.sandbox.paypal.com/v1/oauth2/token')
    req = Net::HTTP::Post.new(uri)
    req['Authorization'] = 'Basic ' + Base64.strict_encode64('CLIENT_ID:CLIENT_SECRET')
    req['Content-Type'] = 'application/x-www-form-urlencoded'
    req.body = 'grant_type=client_credentials'

    res = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) { |http| http.request(req) }
    puts res.body
    ```

  </Tab>

  <Tab title="TypeScript">
    ```typescript theme={null}
    import fetch from 'node-fetch';

    const clientId = 'CLIENT_ID';
    const clientSecret = 'CLIENT_SECRET';

    async function getAccessToken() {
      const response = await fetch('https://api-m.sandbox.paypal.com/v1/oauth2/token', {
        method: 'POST',
        headers: {
          'Authorization': 'Basic ' + Buffer.from(`${clientId}:${clientSecret}`).toString('base64'),
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'grant_type=client_credentials'
      });
      const data = await response.json();
      console.log(data);
    }

    getAccessToken();
    ```

  </Tab>
</Tabs>

### SDK integration path

The SDK integration path is for developers who use PayPal's JavaScript SDK to embed payment buttons and checkout flows directly into their web applications. Developers typically choose the SDK path for web-based integrations because it abstracts much of the complexity and provides built-in security features.

#### Security requirements

- Always load the PayPal JavaScript SDK from the official PayPal CDN.
- Never expose sensitive credentials (client secret) in client-side code.
- Use HTTPS for all SDK requests.
- Validate all payment events on the server.
- Use CSP and SRI for script integrity.
- Keep SDK and dependencies up to date.

#### Security best practices

- Only use the official PayPal CDN for SDK scripts.
- Use Subresource Integrity (SRI) and Content Security Policy (CSP) headers.
- Validate all payment events on the server before fulfilling orders.
- Never include secrets or sensitive data in client-side code.
- Regularly review and update SDK versions.

#### Front-end formatting code samples

The following code samples demonstrate how to securely implement PayPal payment buttons in various frontend frameworks and approaches. Each example shows the proper way to load the PayPal JavaScript SDK and render payment buttons while adhering to the security best practices mentioned in previous sections.

<Tabs>
  <Tab title="ECMAScript (ES Modules)">
    ```javascript theme={null}
    // index.html
    <script type="module" src="paypal.js"></script>
    <div id="paypal-button-container"></div>

    // paypal.js
    const script = document.createElement('script');
    script.src = "https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID";
    script.onload = () => {
      window.paypal.Buttons().render('#paypal-button-container');
    };
    document.body.appendChild(script);
    ```

  </Tab>

  <Tab title="JavaScript (React)">
    ```javascript theme={null}
    import React, { useEffect } from 'react';

    function PayPalButton() {
      useEffect(() => {
        const script = document.createElement('script');
        script.src = "https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID";
        script.addEventListener('load', () => {
          window.paypal.Buttons().render('#paypal-button-container');
        });
        document.body.appendChild(script);
      }, []);

      return <div id="paypal-button-container"></div>;
    }

    export default PayPalButton;
    ```

  </Tab>

  <Tab title="JavaScript (Vanilla)" default>
    ```javascript theme={null}
    <script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID"></script>
    <div id="paypal-button-container"></div>
    <script>
      paypal.Buttons().render('#paypal-button-container');
    </script>
    ```
  </Tab>

  <Tab title="TypeScript (React)">
    ```typescript theme={null}
    import React, { useEffect } from 'react';

    const PayPalButton: React.FC = () => {
      useEffect(() => {
        const script = document.createElement('script');
        script.src = "https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID";
        script.addEventListener('load', () => {
          (window as any).paypal.Buttons().render('#paypal-button-container');
        });
        document.body.appendChild(script);
      }, []);

      return <div id="paypal-button-container"></div>;
    };

    export default PayPalButton;
    ```

  </Tab>
</Tabs>

### Webhook and notification integration

Webhook and notification integration is essential for handling asynchronous events from PayPal, such as payment completions, disputes, or subscription updates. This path ensures your server can securely receive and process notifications and that your system trusts only genuine PayPal events.

#### Security requirements

- Always validate webhook signatures on your server.
- Never trust webhook data without verification.
- Use HTTPS for all webhook endpoints.

#### Security best practices

- Validate every webhook event before processing.
- Log all webhook activity for auditing.
- Rotate webhook IDs and secrets as needed.

#### Server-side webhook verification example

This example uses Python, but you can use any of the supported languages: .NET (C#), cURL, Java, JavaScript (Node.js), PHP, Python, Ruby, and TypeScript.

```python theme={null}
import hashlib
import base64
from OpenSSL import crypto
import requests
import os
from flask import Flask, request, jsonify

def verify_webhook_signature(request_body, headers):
    webhook_id = os.environ.get('PAYPAL_WEBHOOK_ID')
    transmission_id = headers.get('paypal-transmission-id')
    timestamp = headers.get('paypal-transmission-time')
    webhook_event = request_body
    webhook_signature = headers.get('paypal-transmission-sig')
    cert_url = headers.get('paypal-cert-url')
    response = requests.get(cert_url)
    cert = crypto.load_certificate(crypto.FILETYPE_PEM, response.content)
    data_string = transmission_id + '|' + timestamp + '|' + webhook_id + '|' + hashlib.sha256(str(webhook_event).encode('utf-8')).hexdigest()
    try:
        crypto.verify(cert, base64.b64decode(webhook_signature), data_string.encode('utf-8'), 'sha256')
        return True
    except:
        return False

app = Flask(__name__)
@app.route('/webhooks/paypal', methods=['POST'])
def paypal_webhook():
    if verify_webhook_signature(request.json, request.headers):
        event = request.json
        # Process event
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'error': 'Invalid signature'}), 400
```

## Security testing guidelines

Testing your security implementation is critical to ensure your integration is robust against various threats and edge cases. While comprehensive response handling testing is covered in [Handling API responses](/developer/how-to/api/handling-api-responses), consider these additional security-specific tests:

### Authentication and authorization testing

- Test with expired access tokens to verify your token refresh logic works correctly.
- Attempt operations with insufficient permissions to ensure proper access control.
- Verify webhook signature verification correctly rejects unsigned or improperly signed events.

### Data protection testing

- Confirm sensitive data is not logged in your application logs during testing.
- Verify that error messages displayed to end-users don't expose sensitive information.
- Test that your client-side code never receives or processes sensitive credentials.

### Integration security testing

- Use [PayPal's negative testing tools](https://developer.paypal.com/tools/sandbox/negative-testing/request-headers/) to simulate various security-related errors.
- Test your implementation with different network conditions (timeouts, dropped connections).
- Verify that your TLS configuration meets PayPal's security requirements.

For comprehensive testing of API responses, including error handling and recovery flows, see the [Testing your response handling](/developer/how-to/api/handling-api-responses#testing-your-response-handling) section in the API responses guide.

## PayPal security tools

PayPal offers a suite of security tools and features to help secure your integration.

| Tool/Feature                                                                                                                        | Purpose/Use Case                       | Integration Location                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------- |
| [Open Authorization (OAuth) 2.0](https://developer.paypal.com/api/rest/authentication/)                                             | Secure API authentication              | Back-end                                                                    |
| [Webhook signature verification](https://developer.paypal.com/api/rest/webhooks/#verify-webhook-signature)                          | Validate event authenticity            | Back-end                                                                    |
| [Transport Layer Security (TLS)](https://developer.paypal.com/reference/guidelines/info-security-guidelines/#secure-communications) | Secure data in transit                 | Everywhere                                                                  |
| API credential management                                                                                                           | Securely manage API keys and secrets   | [Developer Dashboard](https://developer.paypal.com/developer/applications/) |
| [JavaScript SDK](https://developer.paypal.com/sdk/js/best-practices/)                                                               | Secure client-side payment integration | Front-end                                                                   |
| [Fraud detection tools](https://developer.paypal.com/docs/checkout/advanced/customize/fraud-protection/)                            | Prevent and detect fraudulent activity | Back-end/PayPal Portal                                                      |
