---
title: Integrate FraudNet into your web app
slug: /limited-release/fraudnet/integrate/
createTime: "2024-08-15T08:05:56.413Z"
updateTime: "2024-09-18T01:14:58.569Z"
---

# Integrate FraudNet into your web app

This page guides you through the steps to integrate FraudNet into your web application. The basic steps are:

- Embed a FraudNet JavaScript or noscript snippet into your web page.
- Pass a Client MetaData ID (CMID, also known as the correlationId ) to the FraudNet Session Identifier f variable used by the JavaScript and noscript tags. This enables the FraudNet JavaScript to post data asynchronously by using the Session Identifier f .
- Pass the above CMID to PayPal Risk (via the PAYPAL-CLIENT-METADATA-ID header) in the backend. This enables PayPal Risk to pull data that the FraudNet JavaScript stores.

The bulk of the integration code is based on the non-blocking script loader pattern described below. There are three parts to the integration:

- script/ element used as a parameter block for passing input parameters to FraudNet
- script/ element with code for asynchronously loading the FraudNet JavaScript
- noscript/ element if JavaScript is not enabled for the application

## Content Security Policy integration

### CSP tags

If you are using Content Security Policy (CSP), you must allowlist the following URLs in CSP:

| Tag        | Attribute (Live)                                |
| ---------- | ----------------------------------------------- |
| img-src    | https://c.paypal.com,https://b.stats.paypal.com |
| frame-src  | https://c.paypal.com                            |
| script-src | https://c.paypal.com                            |

### CSP scripts

If your Content Security Policy (CSP) does not allow inline-scripts, you may use one of the following options:

- Add unsafe-inline as a directive in your script-src policy , such as Content-Security-Policy: script-src 'unsafe-inline' . This allows access to all inline-resources throughout your app.
- Implement a nonce value to allowlist the script.

#### Allowlist inline scripts

You can allowlist specific inline scripts without using the unsafe-inline directive, by using either a cryptographic nonce (a number used once) or an SHA hash.

To use a nonce, add a nonce attribute in the script tag. You must generate a nonce at random with each page load and insert it into the CSP and the FraudNet script. PayPal recommends encoding a nonce value in Base64 using a cryptographically secure random number generator with at least 128 bits of data.

**Note** : PayPal recommends not using a static nonce because it is actually less secure than using the unsafe-inline directive. If attackers utilize the nonce value, they can bypass all other restrictions in the CSP and execute any script they want.

Nonce example:

&lt;script nonce=abcRANDOM_NONCE_VALUExyz&gt;
alert('Hello, world.');
&lt;/script&gt;

Content-Security-Policy: script-src 'nonce-abcRANDOM_NONCE_VALUExyz'Alternately, you can create an SHA hash of the script itself (without its tags), and place that value in the CSP script-src .

Script hash example:

&lt;script&gt;
alert('Hello, world.');
&lt;/script&gt;

Content-Security-Policy: script-src 'sha256-abc_hash-of-MixEd1-CaSE2&numS_xyz='See [Configuration parameters](/limited-release/fraudnet/integrate/add-parameter-block/) for more details.

## Add a JavaScript code block

The block below should work on any modern browser that has JavaScript enabled.

This JavaScript passes parameters to FraudNet. All FraudNet parameters except parameter s and parameter f are optional. For more information about optional parameters, see [Add Parameter Block](/limited-release/fraudnet/integrate/add-parameter-block/) .

The fncls attribute is mandatory, and its value must be fnparams-dede7cc5-15fd-4c75-a9f4-36c430ee3a99 . In order to find and process parameters, FraudNet JavaScript searches for a script of type application/json with an attribute fncls , and its value match that string.

Copy and update the following code snippet into the page where you are integrating FraudNet.

&lt;script type="application/json" fncls="fnparams-dede7cc5-15fd-4c75-a9f4-36c430ee3a99"&gt;
{
"f":"change_this_to_32char_guid",
"s":"unique_flowid_per_web_page" // unique ID for each web page
}
&lt;/script&gt;There are two options for passing the data:

// Option 1: Insert this after the "fnparams" Configuration JSON
&lt;script type="text/javascript" src="https://c.paypal.com/da/r/fb.js"&gt;&lt;/script&gt;// Option 2: Or, run FraudNet after your logic by appending it
// pass your configuration as options: { fnUrl: "https://c.paypal.com/da/r/fb.js" }
function \_loadFraudnetConfig(options) {
var script = document.createElement('script');
script.src = options.fnUrl;
document.body.appendChild(script);
}## Add a noscript code block
The following block is rendered only by Web browsers that do not have JavaScript enabled. It collects data from a visitor, even when JavaScript is not available.

&lt;noscript&gt;
&lt;img src="https://c.paypal.com/v1/r/d/b/ns?f=change_this_to_32char_guid&s=unique_flowid_per_web_page&js=0&r=1" /&gt;
&lt;/noscript&gt;
