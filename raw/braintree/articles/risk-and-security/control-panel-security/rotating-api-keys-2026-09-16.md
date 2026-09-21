<!-- Source URL: https://developer.paypal.com/braintree/articles/risk-and-security/control-panel-security/rotating-api-keys -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Rotating API Keys
slug: /articles/risk-and-security/control-panel-security/rotating-api-keys/
createTime: '2025-04-02T01:03:08.407Z'
updateTime: '2025-04-02T01:03:08.426Z'
---



# Rotating API Keys

Your [API keys](/braintree/articles/control-panel/important-gateway-credentials#api-credentials) are like a username and password. You should generate new ones if there’s any chance they’ve been exposed or compromised (e.g. if one of your developers leaves the company or if you send the keys in an email). Developers often refer to this as **rotating your API keys**.

If you generate new API keys, your old API keys will continue to work until you delete them. This allows you to rotate your keys without customers experiencing any downtime.


**IMPORTANT**
 **Do not** delete your old API keys until you have confirmed the new keys work as expected.

 

To generate a new set of API keys for your user:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**API**from the drop-down menu
- Scroll to the**API Keys**section
- Click the**Generate New API Key**button

After you've generated your new keys, you'll need to [update your code with the new values](/braintree/docs/start/go-live#update-live-server-configuration). Once you've updated your code and confirmed that your new keys are working, you can delete the old ones.

