<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/api-authentication -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: API Authentication
slug: /in-person/guides/api-authentication/
createTime: '2024-11-20T19:04:43.013Z'
updateTime: '2024-11-20T19:04:43.265Z'
---



# API Authentication


## Choosing an Authentication Option for your POS Solution

GraphQL requests (Braintree In-Person mutations) can be authenticated in one of two ways.


### 1st Party API Caller (API Keys) - Basic Authentication

This is the ideal method if you're developing a custom application for a single merchant or offering a solution in which the merchant is fully responsible for the code calling the API and infrastructure surrounding it. In this model, a merchant logs in to the Braintree Control Panel to [generate API Keys](/braintree/articles/control-panel/important-gateway-credentials#api-keys) (public and private keys), copies and securely stores them, and makes API calls with them as a base64-encoded string, [as outlined here for GraphQL](/braintree/graphql/guides/making_api_calls/#request-requirements).


### 3rd Party Application (OAuth) - Bearer Authentication

This is the ideal method if you're developing a single application or codebase leveraged by multiple merchants. This method removes the need for merchants to copy and paste credentials by replacing them with a web-based permission-granting flow within your application.

You will need to [create an OAuth Application](/braintree/docs/guides/extend/oauth/configuration), [implement the merchant-facing web-based OAuth Flow](/braintree/docs/guides/braintree-auth/overview), and [store theAccessTokenandRefreshToken](/braintree/docs/guides/extend/oauth/access-tokens) on behalf of each of your merchants. Your application will also need to monitor token expiry and refresh them behind the scenes prior to expiry as needed.

**NOTE**
You cannot grant 3rd Party permissions to your own account. For testing and development, you will need to [create two Braintree sandbox accounts](https://www.braintreepayments.com/sandbox?locale=us). One account will act as the application owner, and the other account to simulate a test merchant.

[Account Structure](/braintree/in-person/get-started-1/account-structure/)[Setup Reader](/braintree/in-person/guides/setup-reader/)