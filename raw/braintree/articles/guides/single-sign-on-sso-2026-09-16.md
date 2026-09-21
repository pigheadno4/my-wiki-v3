<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/single-sign-on-sso -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Single Sign-On (SSO) Onboarding Guide
slug: /articles/guides/single-sign-on-sso/
createTime: '2025-04-01T22:10:56.910Z'
updateTime: '2026-05-20T10:38:53.923Z'
---



# Braintree Single Sign-On (SSO) Integration Guide

**NOTE**
This guide assumes familiarity with SAML(Security Assertion Markup Language) and SSO. If you are unfamiliar, please read our explainer section below before continuing onwards.


## What is SSO? What is SAML? How does this all work?



Single Sign-On (SSO) is a technology that allows users to access multiple applications with a single login. Instead of entering credentials for each individual app, users authenticate once and gain seamless access to all their assigned SaaS applications.SSO is sort of like a bar. In a bar, customers only show ID once to order drinks, instead of re-verifying for each round. Similarly, with SSO, users verify their identity once and then gain access to multiple services without repeated logins.



The basic steps of a SSO/SAML Login flow are as such:


- **User attempts to access a service** (like Salesforce).


- The **service provider redirects** the user to the identity provider (like Okta, Entra, OneLogin etc.).


- The **identity provider authenticates** the user (usually with credentials or MFA).


- Upon successful login, the identity provider generates a **SAML assertion** (an XML-based document).


- The SAML assertion is passed back to the **service provider**, verifying that the user is authenticated.


- The **service provider grants access** to the user without requiring a separate login.






## What does SSO/SAML at Braintree look like?

Braintree supports SAML 2.0-based Single Sign-On (SSO), allowing users to log in through your organization's identity provider.


- Users are created, edited, suspended, andmanaged in the **Braintree Control Panel**


- Users **log in via your Identity Provider (IdP)** -&gt; No password on our site.


- Users suspended in the IdP will be denied access to Braintree but will still appear active in the Control Panel unless manually suspended or deleted


- We support SP-Initiated SSO, or when users begin login at Braintree's site through [https://id.braintreegateway.com/sso/sessions/new](https://id.braintreegateway.com/sso/sessions/new) in production or [https://id.sandbox.braintreegateway.com/sso/sessions/new](https://id.sandbox.braintreegateway.com/sso/sessions/new) in sandbox.


- 



We also support IdP-Initiated SSO, where users begin login from their IdP dashboard.








## Required Setup Values

| Field | Example | Notes |
| --- | --- | --- |
| **Merchant ID** | 1ab2cdefghij4kl5 | Found in the Control Panel URL after/merchants/ |
| **Email Domain(s)** | @yourcompany.com | List all domains used for user login. Any users with an email address NOT listed will NOT be able to login. |
| **SSO HTTP POST Binding URL** | https://idp.example.com/saml2/sso/post | The SAML callback/POST endpoint from your IdP |
| **X.509 Certificate** | &lt;?xml version="1.0" ... &gt; | For validating SAML responses |

💡 You'll receive the**Audience/Callback URL**from Braintree once the above details are shared with us and we can setup your SSO configuration on our side. You'll need this for setting up SSO on your IdP.
## Optional Values

| Field | Example | Notes |
| --- | --- | --- |
| **Logout Redirect URL** | https://idp.example.com/saml2/sso/logout | Defaults to your SSO POST Binding URL if not provided |

When reaching out to Braintree to enable SSO, please include all of the above values. We cannot onboard you without them.


## IdP-Side Configuration Details

These are values you'll need to configure in your IdP’s SAML settings:

| Field | Description |
| --- | --- |
| **Audience/Issuer Value (Entity ID)** | This should be the same as the callback URL in most cases. It technically matches our Issuer/Audience Value on our side, which in most cases is set to the callback URL, but may be a different value in some cases. |
| **Reply URL / ACS URL (Assertion Consumer Service URL)** | Same as Callback URL |
| **Recipient / Callback URL** | Provided by Braintree |
| **NameID Format** | Email/Email address |
| **NameID Value** | User's email address |


## Step-by-Step Setup (Any IdP)


- Submit a request to your CSM/TAM or via [Braintree support](https://developer.paypal.com/braintree/help) with:


- Merchant Public ID


- Email domains


- SSO Certificate(If using Okta, you won't have these until you start the below onboarding section)


- SSO HTTP Post-Binding URL(If using Okta, you won't have these until you start the below onboarding section)




- Braintree will respond with your SSO Callback URL (e.g., https://id.sandbox.braintreegateway.com/sso/callback/UUID). They may also include a separate Issuer/Audience value in some cases.






### Okta




- Add the Braintree Application:


- Go to "Applications", then "Browse Catalog"


- Search and select "Braintree". You can also add our OIN application directly via its application page:https://www.okta.com/integrations/braintree/


- Add the app and use the **UUID** from your Callback URL for the "BT SSO Partial Callback URI". The format of the callback URL is "https://id.braintreegateway.com/sso/callback/&lt;UUID&gt;", enter only the**UUID**portion into this field. For example, if your full callback URL ishttps://id.sandbox.braintreegateway.com/sso/callback/14dcc51e-7aa5-474a-a746-12bbf7db52d2, then your "BT SSO Partial Callback URL" would be "14dcc51e-7aa5-474a-a746-12bbf7db52d2"


- **Note**: During initial integration, you can use a placeholder value (e.g., placeholder) for the "BT SSO Partial Callback URI" since the correct value may not be immediately available. This can be updated with the actual value after you have received it from us.


- Set the SCIM endpoint:


- Sandbox: id.sandbox.braintreegateway.com


- Production: id.braintreegateway.com






- Configure SAML settings:


- Navigate to the "Sign-On" tab


- Click "Edit" in the top right


- Click "Credential Details"


- Set "Application username format" to "email"


- Set "Update application username on" to"create and update"


- Leave everything else default


- Save




- After saving:


- Navigate to the "Sign-On" tab


- In the "SAML 2.0"section, click "More Details"


- Copy the "Sign-On URL" and "Signing Certificate".Send them to your Braintree contact


- We will use these values to update your SSO config on our side. We will also enable SSO for your BT merchant.




- Test login via "Post-Configuration Steps"


- Due to regulatory requirements, we require MFA attribution for all SSO applications. As such, please follow our [MFA compliance guide](https://developer.paypal.com/braintree/articles/guides/single-sign-on-sso/mfa) in order to satisfy this requirement for your application.






### OneLogin


- In OneLogin:


- Log into the OneLogin Admin Portal.


- Navigate to Apps → Add App.


- Select the “SAML Test Connector (IdP)” app.


- Give the app a display name like “Braintree Dashboard”.




- Configure the App in OneLogin


- Open OneLogin's Configuration tab for the new app. Click `Edit` in the top right


- Retrieve the SSO Callback URL given to you by BT Support.


- &gt;Paste the BraintreeSSO Callback URLinto the ACS (Consumer) URL, Recipient, Audience, and ACS (Consumer) URL Validator fields in OneLogin.


- Save




- After saving:


- Go to **Sign-On**


- Copy the **Sign-On URL** and **Signing Certificate**


- Send them to your Braintree contact


- We will use these values to update your SSO config on our side. We will also enable SSO for your BT merchant.




- Test login via`Post-Configuration Steps`


- Due to regulatory requirements, we require MFA attribution for all SSO applications. As such, please follow our [MFA compliance guide](https://developer.paypal.com/braintree/articles/guides/single-sign-on-sso/mfa) in order to satisfy this requirement for your application.






### Microsoft Entra ID (Azure AD)






- Add Braintree as an Enterprise App:


- Sign into the Microsoft Entra admin center.Navigate to Apps → Add App.


- Go to Entra ID → Enterprise apps → All applications.


- Click New application → Create your own application.


- Name the app, for example “Braintree SSO”, select “Integrate any other application…” (Non‑gallery), and click Create




- Configure SAML‑SSO in Entra ID


- Navigate to the newly created Braintree app, then open Single sign-on and select SAML.


- Click the pencil icon in the Basic SAML configuration section and enter the BT SSO Callback URL you should've recieved from BT support, into theIdentifier (Entity ID),Reply URL (Assertion Consumer Service URL), andSign-on URLfields and save. If Braintree support gave you a separate Audience/Issuer value, then you must set the Identifier (Entity ID) field to this separate value. Likewise, when you test the SSO login, if you get an error similar to "Application with identifier 'Banana' was not found in the directory 'Paypal'.", then the issuer/audience value is set differently on our side. If this is the case, tell Braintree support and they should be able to retrive the distinct Issuer/Audience value for you. If this Issuer/Audience value has spaces in it, Entra does not allow this. Let Braintree support know, and we can fix the Audience value to the callback URL.


- Save the configuration once complete.




- Obtain Certificate & Metadata:


- From the same SAML pane, scroll to the SAML Certificates section.


- Download either the Raw or Base64 certificate file—this is needed by Braintree.


- Also copy the SSO Login URL. This is used for the SSO redirect.


- Send both values to BT support.


- We will use these values to update your SSO config on our side. We will also enable SSO for your BT merchant.




- Test login via`Post-Configuration Steps`


- 

Due to regulatory requirements, we require MFA attribution for all SSO applications. As such, please follow our [MFA compliance guide](https://developer.paypal.com/braintree/articles/guides/single-sign-on-sso/mfa) in order to satisfy this requirement for your application.














## Post-Configuration Steps



Once Braintree confirms setup:


- Please test your SSO configuration by adding a new user to the system or converting an existing non-SSO user to SSO and having said user attempt an SSO login, both from the IdP side and from our side. Please refer to the below sections on how to accomplish this


- If you are looking to onboard to SCIM, please ensure you convert all the non-SSO users you want to use SSO first, before attempting to onboard to SCIM. Once you are on SCIM, you will no longer be able to convert non-SSO users to SSO. Please refer to our [SCIM FAQ](https://developer.paypal.com/braintree/articles/control-panel/users-roles/scim/scim-faq) for further details, specifically the " **Now that I'm on SCIM, I'm not able to create new SSO users or edit existing ones. What gives?** " section.


- Once you do the above, please refer to the same[SCIM FAQ](https://developer.paypal.com/braintree/articles/control-panel/users-roles/scim/scim-faq)for further information about our SCIM integration. If you desire to onboard, please refer to our[onboarding guide](https://developer.paypal.com/braintree/articles/control-panel/users-roles/scim/scim-integration)






## How to Create a new SSO Enabled User

Once you are onboarded to SSO as a merchant, you will have the ability to create new SSO users, or convert old non-SSO users to SSO login. In order to do either, please follow the instructions below:

**Creating a New SSO User:**




- **Create a new user on your IdP**. The below steps will assume you are using Okta. The exact flow and naming of various sections may be different for different IdP's. For other IdP's, please refer to your IdP's guide on creating SSO users.The core requirement is that the email address of the user on the IdP and the user on Braintree MUST match EXACTLY.


- Log on to your Okta admin panel.


- Open "Directory", then "People".


- Create a user. Ensure their username and email are both the user's email address. This is essential, as we use the email address as the unique identifer for SSO users.


- Once the user is created, assign the user to the new SSO app. You can do this by:


- Navigate to the new user's user page. This can be done by going to "Directory", then "People", then searching for the user's email address, and then clicking on said user.


- Click "Assignments", then "Add Assignment".


- Select the new SSO app we just created.





Now that we have a user on the IdP side (the above button names are for Okta, they may be different for different IdP's), we need to create the user on the Braintree side.


- **Creating a new user on Braintree**


- On the Braintree control panel, navigate to your merchant's user page. This can be done by navigating to your merchant's home page, then changing the end directory to /users. For example, if your merchant home page is "https://sandbox.braintreegateway.com/merchants/cs7ssx6rwd3rgvh6/home", then your Users page will be located at "https://sandbox.braintreegateway.com/merchants/cs7ssx6rwd3rgvh6/users"


- Once on the users page, select "New User".


- Enter the user's details. Ensure the email matches the email address of the user we just created on the Idp side. If they do not match, the SSO login will not work.


- Click "Create User" to save the new user.


- Wait up to five minutes for the caches to update.





Once both steps are complete, have the user try to login both via the IdP (a new tile with the app name should now appear in their homepage) and via our SSO login pagehttps://id.sandbox.braintreegateway.com/sso/sessions/new. If they are able to login both times, then your SSO configuration is working.




## How to Convert an Existing Non-SSO User to SSO




- Create the user on your IdP if they do not already have an account on said IdP. Please refer to the previous section on creating SSO users on how to accomplish this.
- In Braintree, go to the user's show page. In order to do this:
- Login to the Braintree control panel.
- Go to your users page. You can accomplish thisby navigating to your merchant's users URL, which will be in the format of braintreegateway.com/merchants/[merchant public_id]/users. For example, if your merchant's home page is "https://sandbox.braintreegateway.com/merchants/cs7ssx6rwd3rgvh6/home", then your Users page will be at "https://sandbox.braintreegateway.com/merchants/cs7ssx6rwd3rgvh6/users"
- Search for your user. You can use our newly introduced search bar feature to do this.
- Select your user. The page should redirect to your user's show page, with the URL pattern of "https://sandbox.braintreegateway.com/merchants/[merchant public_id]/users/[user public_id]". For example, if your user's public_id isp3wgxdvyzhjqz7ym, then the URL for said user's show page would be "https://sandbox.braintreegateway.com/merchants/cs7ssx6rwd3rgvh6/users/p3wgxdvyzhjqz7ym"
- Once you are on your user's show page, it should show their details, 2FA status, and other information. There should be an "SSO Status" section that has a button that says "Enable". If the section does not appear, please reach out to support, as it means you either have not been onboarded to SSO fully on our side, or you are a SCIM merchant.
- Click the "Enable" button in the "SSO Status" section. This should convert the user to SSO. They will no longer be able to login via username and password on our site, and instead will need to login via SSO.
- Please wait up to five minutes for caches to invalidate. After this, you can test their SSO status by having the user go to our SSO login page ([https://id.braintreegateway.com/sso/sessions/new](https://id.braintreegateway.com/sso/sessions/new)) and enter their email address. It should then redirect them to your IdP in order to login to your IdP. If they have an SSO enabled user account on multiple Braintree merchants, it will first prompt them to select which merchant they want to login to.
- If the above login executes successfully (that is, they are redirected out to your IdP, login to said IdP, then are redirected back to our page, logged in, and sent to your merchant homepage), then your SSO configuration was successful.







**Note** : If one of your SSO users is redirected to a 403 page, this may be due to a known redirect bug that occasionally occurs. In this case, please have the user click the "Go Back" button presented on said page. It should redirect them back to the merchant homepage as a logged in user.


## How to Perform an SSO Provider or Application Migration

If you are changing SSO providers, say from Entra to Okta, you will need to coordinate with Braintree support in order to perform this change safely. These steps also apply if you are changing the SSO app instance within your existing IdP.The basic steps are:

1. Create a new SSO app in the new provider.

2. Assign your existing users to this new application.

3. Copy the SSO target URL (also known as the SSO signon URL) and the SSO certificate.

4. Open a Braintree support ticket or talk to your CSM to get a ticket opened.

5. Send them your SSO target URL and certificate and a timeframe for switching over our SSO configuration from the old app to this new app.

6. At the requested time, we will swap our configuration over to point to the new application. The Braintree SSO callback URL used by your application will not change.

7. Have one of your SSO users attempt to login through the new IdP and into the Braintree platform as a test. If they are able to login, then the migration was successful.

p.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px 'Atkinson Hyperlegible Next'; color: #000000} span.s1 {font-kerning: none} span.s2 {text-decoration: underline ; font-kerning: none; color: #000055}

