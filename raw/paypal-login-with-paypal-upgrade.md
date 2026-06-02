<!-- Source URL: https://developer.paypal.com/docs/log-in-with-paypal/upgrade/ -->

## <!-- Fetched: 2026-04-16 -->

title: Upgrade options
slug: /docs/log-in-with-paypal/upgrade/
createTime: '2024-08-15T07:47:50.619Z'
updateTime: '2024-08-15T07:47:50.907Z'

---

# Upgrade options

PayPal recommends that new apps integrate with OpenID Connect. Apps integrated with OpenID will continue to work, but won't receive new features.

## Log in with PayPal legacy integrations

For Log in with PayPal legacy integrations (prior to January 2018), replace the /connect with /signin/authorize in your links, for example, instead of

https://www.sandbox.paypal.com/connect?flowEntry=static&amp;client_id=[client id]&amp;scope=[list of scopes]&amp;redirect_uri=[return URL]Log in with PayPal legacy integrations (prior to January 2018) use:

https://www.sandbox.paypal.com/signin/authorize?flowEntry=static&amp;client_id=[client id]&amp;scope=[list of scopes]&amp;redirect_uri=[return URL]
