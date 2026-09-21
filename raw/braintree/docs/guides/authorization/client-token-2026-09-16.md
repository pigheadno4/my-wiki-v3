<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/authorization/client-token -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Client Token
slug: /docs/guides/authorization/client-token/
createTime: '2025-04-01T22:23:50.384Z'
updateTime: '2025-04-01T22:23:50.403Z'
---



# Client Token

![Client,token,sequence,diagram](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/auth--client-token.png)A client token is a signed JWT that includes configuration and authorization information required by the [Braintree client SDK](/braintree/docs/start/hello-client/javascript/v3/).

Your server is responsible for [generating the client token](/braintree/docs/start/hello-server/ruby/#generate-a-client-token), which contains all of the necessary configuration information to set up the client SDKs. When your server provides a client token to your client, it authenticates the application to communicate directly to Braintree.

Your client is responsible for obtaining the client token from your server and initializing the client SDK.

Client tokens are valid for up to 24 hours. If the client token includes a customer ID and creates an excessive number of payment methods, it will be invalidated.

