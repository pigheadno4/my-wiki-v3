<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/fastlane/setup-integration -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Setup and Integration
slug: /docs/guides/fastlane/setup-integration/
createTime: '2025-04-02T01:48:35.939Z'
updateTime: '2025-04-02T01:48:35.952Z'
---



# Setup and Integration


- Added PHP and Ruby for server-side code for Fastlane.

- We added the two remaining SDKs to BT server-side code for Fastlane

- Updated CSP Policy

- The CSP Policy has been updated based on recent SDK changes. Encourage merchants to update their CSP policy for the integration.



#### Setup

To use Fastlane through Braintree:


- Create a Braintree sandbox account: Ensure you have a Braintree sandbox account. If not, you can create one using the instructions[here](https://www.braintreepayments.com/sandbox).
- Enable Fastlane in sandbox: Under the Account Settings section, select Customer Checkout, and then click "Turn On".

![](https://www.paypalobjects.com/devdoc/fastlane-customer-checkout.png)


#### Configure your Content Security Policy

Content Security Policy (CSP) is a web browser feature that helps prevent cross-site scripting and other attacks by restricting the sources from which resources can be loaded on your page. This allows you to maintain better control over potentially malicious code. Refer to [advanced options](/braintree/docs/guides/fastlane/advanced-option#configure-your-content-security-policy) for more information.


#### Integration Flow

The following diagram depicts the integration required to enable the Fastlane experience.![](https://www.paypalobjects.com/devdoc/fastlane_integration_flow.jpeg)

Next step: [Client-side Integration](/braintree/docs/guides/fastlane/client-side)

