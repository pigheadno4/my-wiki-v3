<!-- Source URL: https://developer.paypal.com/braintree/articles/risk-and-security/control-panel-security/two-factor-authentication -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Two-Factor Authentication
slug: /articles/risk-and-security/control-panel-security/two-factor-authentication/
createTime: '2025-04-02T00:29:23.113Z'
updateTime: '2025-04-02T00:29:23.142Z'
---



# Two-Factor Authentication

Two-factor authentication (2FA) is an extra layer of security that can be added to a user in the Control Panel, making it more difficult for unauthorized users to access your gateway. **Starting in September 2023, 2FA is required for all Braintree users, and each user must enable 2FA to access Control Panel.**

When 2FA is enabled on a Control Panel user's account, the user will be required to enter both their normal password and a different code each time they sign in. Users can choose to receive this code via an application on their smartphone or a text message (SMS) to their mobile device.


## How to enable 2FA

Starting in September 2023, 2FA is required for all Braintree users, and each user must enable 2FA to access Control Panel. For any user who does not have 2FA enabled, a 2FA set-up assistant will automatically appear after the user logs in. Please follow the instructions in the set-up assistant.

To manually enable 2FA, users can follow these steps:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Select your user icon in the top right corner
- Select**My User**from the drop-down menu
- Scroll to the**Two-Factor Authentication**section
- Select the**Enable**button
- Enter your password when prompted
- Scan the QR code using one of the[supported apps](#compatibility)on your mobile device, or select the**Use SMS As Primary**link
- Enter the code you receive on your mobile device to complete the process*

*If you opt to use an app, you will find the initial code within that application. If you choose SMS as your preference, this code will be texted to you.


## Setting up a Hardware Security Key

When 2FA is enabled on a user's account, they can then register a WebAuthn U2F compatible security key with their account:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Select the gear icon in the top right corner
- Select**Team**from the drop-down menu
- Locate the user you would like to make changes to
- Select the link in theUsername,Name, orEmailcolumn
- Scroll to the**Two Factor Authentication**section
- Select the**+ Add Key**button


**NOTE**
 The user will need a browser that is compatible with the [WebAuthn API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API#Browser_compatibility).

 


## Signing in with 2FA

Once 2FA is enabled on a user account, every time they sign into the Control Panel they'll be prompted for their second factor in the following order:


- Hardware Security Key (if registered)
- [Authenticator App](#compatibility)(if registered)
- SMS Code

If a user that selected the app as their preferred method is unable to access the app at the time of login, they can have a code sent to their mobile device via SMS by selecting **Text a code instead**.

If a user that selected the Hardware Security Key as their preferred method is unable to access the app at the time of login, they can fall back to the Authenticator App or have a code sent to their mobile device via SMS by selecting **Text a code instead**.

If none of the above options work, please ask the account admin to [disable 2FA for the user](https://developer.paypal.com/braintree/articles/risk-and-security/control-panel-security/two-factor-authentication#how-to-disable-2fa), so that the user can set up 2FA once again upon log in. If an account admin is unavailable to assist or if the user in question is the only admin account within the organization, [please get help from our support team](https://developer.paypal.com/braintree/help/PasswordResetHelp).


**NOTE**
 The user will automatically fall back to the Authenticator App or SMS if their browser does not support the [WebAuthn API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API#Browser_compatibility).

 


## Managing a Web Authentication (WebAuthn) Security Key


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Select the gear icon in the top right corner
- Select**Team**from the drop-down menu
- Locate the user you would like to make changes to
- Select on the link in theUsername,Name, orEmailcolumn
- Scroll to the**Two Factor Authentication**section
- Select the**Options**link


## How to Temporarily Disable 2FA for a user

If one of your users is locked out of the Control Panel, or is unable to access their mobile device at the time of login, your Braintree Account Admin will need to disable 2FA for that user's account. The user will be prompted to set up 2FA the next time they log in:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Select the gear icon in the top right corner
- Select**Team**from the drop-down menu
- Locate the user you would like to make changes to
- Select on the link in theUsername,Name, orEmailcolumn
- Scroll to the**Two Factor Authentication**section
- Select the**Disable**button


**NOTE**
 Only users with the Account Admin role will be able to disable 2FA for other users in the Control Panel.

 

[Contact us](/braintree/help?issue=UsersRolesQuestion) with questions.


## How to reset 2FA

Starting in September 2023, the users won't be able to disable 2FA for themselves. Instead, there will be the option to reset 2FA within **My User** from the drop-down menu. Users should only perform a 2FA reset if they plan to change their phone number or their authenticator app.

To reset 2FA, users can follow these steps:


- Log into the Control Panel
- Select your user icon in the top right corner
- Select**My User**from the drop-down menu
- Scroll to the**Two-Factor Authentication**section
- Select**Reset 2FA**(If you see**Enable**button instead, you have not enabled 2FA yet. Please see****[How to enable 2FA](https://developer.paypal.com/braintree/articles/risk-and-security/control-panel-security/two-factor-authentication#how-to-enable-2fa)for information on enabling 2FA)
- Enter your password when prompted to confirm reset
- Follow the steps to set up your new 2FA configuration*

*If you confirm 2FA reset but do not successfully complete the steps, you will need to enable 2FA from **My User** or set up 2FA once again the next time you log in.


## Compatibility


### Authenticator Apps

Braintree’s 2FA implementation is compatible with most Time-based One-Time Password (TOTP) applications. TOTP apps automatically generate an authentication code that changes after a certain period of time. Because they do not rely on incoming text messages, they are more reliable than SMS—especially for locations outside the US.

Popular TOTP apps include:


- [Google Authenticator](https://support.google.com/accounts/answer/1066447?hl=en)
- [Authy](https://www.authy.com/)
- [Duo Mobile](https://www.duosecurity.com/product/methods/duo-mobile)
- [Authenticator](http://www.windowsphone.com/en-us/store/app/authenticator/e7994dbc-2336-4950-91ba-ca22d653759b)


### Hardware Security Keys

Braintree’s hardware 2FA implementation is compatible with the newest versions of Chrome, Firefox, Safari and Edge browser:


- Chrome 67+
- Firefox 60+
- Safari 13+
- Edge 18+

In addition, we support all FIDO U2F hardware security keys. Some popular Hardware Security keys include:


- [Yubikey by Yubico](https://www.yubico.com)
- [Google Titan Security Key](https://cloud.google.com/titan-security-key)

