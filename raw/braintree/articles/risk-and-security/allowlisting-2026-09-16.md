<!-- Source URL: https://developer.paypal.com/braintree/articles/risk-and-security/allowlisting -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Allowlisting
slug: /articles/risk-and-security/allowlisting/
createTime: '2025-04-01T21:57:24.357Z'
updateTime: '2025-04-01T21:57:24.377Z'
---



# Allowlisting


**NOTE**
 This article covers how to use IP and hostname restrictions to better control what users have access to your Braintree Gateway. For information on allowlisting Braintree IP addresses and domains, [see our developer docs](/braintree/docs/reference/general/braintree-ip-addresses).

 

If you want to add an extra layer of security to your gateway, you can define which specific IP addresses or hostnames can access your Control Panel or take certain actions via the API. This is called allowlisting. Once enabled, access will be denied unless the user's IP address or hostname is added to the allowlist.


**NOTE**
 Braintree does not currently offer the option to denylist – or block – specific IP addresses or hostnames.

 

The allowlist only applies to Control Panel access and server-to-server calls via the API. Any encrypted calls that come straight from the customer’s browser (e.g. requests for [payment method nonces](/braintree/docs/guides/payment-method-nonces) using our client SDKs) will not be subject to the allowlist and will be passed to Braintree, regardless of the user’s IP address.


## Enabling IP and hostname restrictions

Users with the Edit IP Restrictions [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-edit-ip-restrictions) can follow these steps to allowlist certain IP addresses or hostnames:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**API**from the drop-down menu
- Click on the**Security**tab
- Scroll to the**IP and Hostname Restrictions**section
- Click the**Edit**button
- Fill in theIP Address or Hostnamefield
- Check the boxes to select whether to allow Control Panel access and/or API access
- Click the**Add Allowed Host**button
- Repeat steps 7-9 to add any other desired IP addresses or hostnames
- Click the**Enable Restrictions**button


**IMPORTANT**
 If you give an IP address or hostname access to only the Control Panel or only the API, it will block access to the other. We always recommend testing in the sandbox before implementing allowlisted IP addresses or hostnames in production.

 


## Wildcards and CIDR notation

You can use wildcard logic to allowlist a range of hostnames under a specific domain, or all IPs within a certain subnet range. For example, adding 127.54.63.* will allow all IP address within the 127.54.63 subnet range. Classless Inter-Domain Routing (CIDR) notation is also supported.

