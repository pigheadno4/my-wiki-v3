<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/general/braintree-ip-addresses -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Braintree IP Addresses
slug: /docs/reference/general/braintree-ip-addresses/
createTime: '2025-04-01T22:35:07.212Z'
updateTime: '2025-04-01T22:35:07.238Z'
---



# Braintree IP Addresses

An allowlist provides access to specified domains and IP addresses when your security policy would otherwise prevent that access. On top of the guarantees that SSL makes, allowlisting Braintree IP addresses further ensures that requests from your server are indeed going to a trusted Braintree server.

Allowlisting can be useful, but it comes with additional overhead and complication.**If you do not properly allowlist the Braintree domain namesandIP addresses, you may be unable to process payments.**

You can download our list of Braintree IP addresses at[ips.json](https://assets.braintreegateway.com/json/ips.json).
**IMPORTANT**
Braintree IP addresses are subject to change. We recommend watching for changes in [ips.json](https://assets.braintreegateway.com/json/ips.json) .


## Braintree production domains

Braintree production fully qualified domain names are:
### text
```html
api.braintreegateway.com
www.braintreegateway.com
gstatic.braintreegateway.com
payments.braintree-api.com
```

## Braintree production IP addresses

Braintree production domain names may resolve to any of the[production IP ranges and addresses](https://assets.braintreegateway.com/json/ips.json). If you use a firewall, you must allowlist these to ensure secure and uninterrupted communication with Braintree.
## Braintree sandbox domains

Braintree sandbox fully qualified domain names are:
### text
```html
api.sandbox.braintreegateway.com
sandbox.braintreegateway.com
gstatic.sandbox.braintreegateway.com
payments.sandbox.braintree-api.com
```

## Braintree sandbox IP addresses

Braintree sandbox domain names may resolve to any of the[sandbox IP ranges and addresses](https://assets.braintreegateway.com/json/ips.json). If you use a firewall, you must allowlist these to ensure secure and uninterrupted communication with Braintree.