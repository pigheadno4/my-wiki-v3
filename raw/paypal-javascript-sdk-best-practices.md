---
title: Best Practices
slug: /sdk/js/best-practices/
createTime: "2024-03-14T23:48:42.121Z"
updateTime: "2026-02-04T13:28:50.196Z"
---

# Best Practices

**warning**
**Important:** This documentation covers the JavaScript SDK v5 with the CardFields component. For the legacy HostedFields component, see the [archived reference](/sdk/js/v1/reference/) .

[Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) (CSP) is a security measure that helps prevent a range of attacks on a website, including Cross Site Scripting (XSS), clickjacking, and other code injection attacks. CSP adds a special HTTP header to web pages that tells the browser to load only approved content sources for each type of resource, such as scripts, stylesheets, and images. By enforcing these restrictions, CSP limits the potential attack vectors for malicious actors.

To integrate PayPal's JavaScript SDK, you need to add PayPal's script sources to your CSP's approved list so the browser trusts the scripts to handle transactions. You reduce the risk of XSS and similar attacks by ensuring that only scripts from trusted PayPal sources can run.

### Our CSP recommendation: use 'unsafe-inline'

**info**
**Note:** If you prefer to not use 'unsafe-inline' see the following **Using a nonce instead of 'unsafe-inline'** section for more details.

| Value       | Description                                                   |
| ----------- | ------------------------------------------------------------- |
| child-src   | _.paypal.com _.paypalobjects.com \*.venmo.com                 |
| connect-src | _.paypal.com _.paypalobjects.com \*.venmo.com                 |
| frame-src   | _.paypal.com _.paypalobjects.com \*.venmo.com                 |
| img-src     | _.paypal.com _.paypalobjects.com \*.venmo.com data:           |
| script-src  | _.paypal.com _.paypalobjects.com \*.venmo.com 'unsafe-inline' |
| style-src   | _.paypal.com _.paypalobjects.com \*.venmo.com 'unsafe-inline' |

#### Example CSP

#### **`Example CSP`**

```javascript
default-src 'self'; script-src 'self' *.paypal.com *.paypalobjects.com *.venmo.com 'unsafe-inline'; connect-src 'self' *.paypal.com *.paypalobjects.com *.venmo.com; child-src 'self' *.paypal.com *.paypalobjects.com *.venmo.com; frame-src 'self' *.paypal.com *.paypalobjects.com *.venmo.com; img-src 'self' *.paypal.com *.paypalobjects.com *.venmo.com data:; style-src 'self' *.paypal.com *.paypalobjects.com *.venmo.com 'unsafe-inline';
```

### Using a nonce instead of 'unsafe-inline'

Using a nonce with your CSP is safer than 'unsafe-inline' . A nonce is a random string added to a script or style tag and in the CSP header, permitting specific inline scripts or styles while blocking others. This method is more secure than 'unsafe-inline' , which can create potential security risks.

### Our CSP recommendation: use a nonce

**info**
**Note:** When using a nonce, be sure to pass the nonce into your JS SDK script. See the following **Adding nonce to your JS SDK integration** section for more details.

| Value       | Description                                                    |
| ----------- | -------------------------------------------------------------- |
| child-src   | _.paypal.com _.paypalobjects.com \*.venmo.com                  |
| connect-src | _.paypal.com _.paypalobjects.com \*.venmo.com                  |
| frame-src   | _.paypal.com _.paypalobjects.com \*.venmo.com                  |
| img-src     | _.paypal.com _.paypalobjects.com \*.venmo.com data:            |
| script-src  | _.paypal.com _.paypalobjects.com \*.venmo.com nonce-YOUR_NONCE |
| style-src   | _.paypal.com _.paypalobjects.com \*.venmo.com nonce-YOUR_NONCE |

#### Example CSP

#### **`Example CSP with nonce`**

```javascript
default-src 'self'; script-src 'self' *.paypal.com *.paypalobjects.com *.venmo.com nonce-aus44zz6eg; connect-src 'self' *.paypal.com *.paypalobjects.com *.venmo.com; child-src 'self' *.paypal.com *.paypalobjects.com *.venmo.com; frame-src 'self' *.paypal.com *.paypalobjects.com *.venmo.com; img-src 'self' *.paypal.com *.paypalobjects.com *.venmo.com data:; style-src 'self' *.paypal.com *.paypalobjects.com *.venmo.com nonce-aus44zz6eg;
```

### Adding nonce to your JS SDK integration

#### **`Vanilla JS`**

```javascript
<script nonce="YOUR_NONCE" data-csp-nonce="YOUR_NONCE" src="https://www.paypal.com/sdk/js?client-id=test" />
<script nonce="YOUR_NONCE">
          paypal.Buttons().render('#paypal-button');
</script>
```

#### **`React (JS)`**

```javascript
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";
export default function App() {
  const initialOptions = {
    clientId: "YOUR_CLIENT_ID",
    dataCspNonce: "YOUR_NONCE",
    // Add other options as needed
  };
  return (
    <div className="App">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons />
      </PayPalScriptProvider>
    </div>
  );
}
```

#### **`ES Module`**

```javascript
import { loadScript } from "@paypal/paypal-js";
let paypal;
try {
  paypal = await loadScript({
    clientId: "YOUR_CLIENT_ID",
    dataCspNonce: "YOUR_NONCE",
  });
} catch (error) {
  console.error("failed to load the PayPal JS SDK script", error);
}
if (paypal) {
  try {
    await paypal.Buttons().render("#paypal-button-container");
  } catch (error) {
    console.error("failed to render the PayPal Buttons", error);
  }
}
```

## Cross-Origin-Opener-Policy

Cross-Origin-Opener-Policy (COOP) is a security feature that helps prevent cross-origin attacks, such as cross-site scripting (XSS) and data leaks. It allows a web application to control how it interacts with other browsing contexts, like iframes and popups, from different origins.

By setting a COOP header, a website can ensure that its documents can only be opened by documents from the same origin. This can help isolate the web application from potentially malicious content loaded from different origins, enhancing security and user privacy.

If you are using the PayPal Web SDK on your webpage, we recommend that you set the header to Cross-Origin-Opener-Policy: same-origin-allow-popups .

For more details, you can refer to the [Cross-Origin-Opener-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy) documentation
