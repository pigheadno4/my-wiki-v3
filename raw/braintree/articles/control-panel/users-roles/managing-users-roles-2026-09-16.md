<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/users-roles/managing-users-roles -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Managing Users and Roles
slug: /articles/control-panel/users-roles/managing-users-roles/
createTime: '2025-04-02T01:14:35.697Z'
updateTime: '2025-04-02T01:14:35.722Z'
---



# Managing Users and Roles

Creating users allows you to manage who can access your Control Panel. You can also create different roles that restrict or grant user access to certain information and gateway functionalities. For example, you might have a member of your team that only needs to look at customer information in the Control Panel but should never be able to create a transaction. The role assigned to a user will also determine what information we can provide should that individual contact us via phone or email.

The [PCI security standards council](https://www.pcisecuritystandards.org/) requires that you create a separate user for every person who needs access to the Control Panel. Since each user will have unique login credentials, you can track which user interacted with certain transactions.


**NOTE**
 For security, we recommend that all users of your Control Panel enable [two-factor authentication (2FA)](/braintree/articles/risk-and-security/control-panel-security/two-factor-authentication).

 


## Creating and editing roles

You must assign at least one role to each user, with specific [role permissions](/braintree/articles/control-panel/users-roles/role-permissions) granted to each role. If a user has multiple roles, the role with the greatest permissions trumps any others assigned. To create or edit a role:


- Log into the[Control Panel](https://www.braintreegateway.com/login).
- Select the gear icon in the top right corner.
- Select**Team**from the drop-down menu.
- Select the**Roles**tab ​to see a list of your existing roles.
- Select the**New Role**button to create a new role.
- Select the**Edit**link to the right of an existing role you'd like to change.



The **Account Admin** role has the maximum permissions possible and can't be edited or renamed.


## Creating users

To create a new user:


- Log into the[Control Panel](https://www.braintreegateway.com/login).
- Select the gear icon in the top right corner.
- Select**Team**from the drop-down menu.
- Select the**New User**button at the top of the page.
- Specify the user's details, including:
- Their email address.
- Whether they should have API access.
- Their Control Panel role.
- Which[merchant account(s)](/braintree/articles/control-panel/important-gateway-credentials#merchant-account-id)they should have access to.


- Select the**Create User**button.

Once you’ve finished these steps, we will send an email prompting the new user to activate their account by completing the user information form. Here they will fill in their full name, create a username and password, and log into the Control Panel. After logging in, their status in the Control Panel will officially change from Pending to Active, and the Username and Name fields will be populated.


## Editing users

After you’ve created a user, you can change most of their information and permissions. While you can't edit the username associated with a user, you can change the Name and Email fields, as long as the user still has access to the original email account in order to confirm the update. If they no longer have access to the original email account, you’ll need to create a new user.

To edit a user:


- Log into the[Control Panel](https://www.braintreegateway.com/login).
- Select the gear icon in the top right corner.
- Select**Team**from the drop-down menu.
- Locate the user you'd like to make changes to.
- Select the**Edit**link to the right of the user.
- Make any desired changes.
- Select the**Save**button.


**NOTE**
 When a user first sets up their account, it is possible for them to enter an email address as their username; this is separate from the Email field, which defines the email address associated with that user. If they later wish to change their email address, they will do so by adjusting the Email field. This will not impact the Username field, as usernames cannot be edited.

 


## Password safety

In general, you’ll only need to reset your password if you’ve forgotten it, but there are some cases where resetting your password can help protect the security of your account. We recommend [resetting your password](#resetting-user-passwords) in these cases:


- You notice something suspicious in your Control Panel account
- You suspect that someone you don't trust may have your password
- You notice something suspicious in your email or other online accounts
- You have recently removed malware from your system
- We ask you to change your password

If you have not requested to reset your password and you receive an email asking you to change it, it could be a case of phishing. Instead of selecting on a suspect link in an email, log into your account to reset your password there.


### Resetting user passwords


**NOTE**
 The Control Panel allows 6 failed login attempts before requiring a password reset.

 

Anyone can reset their password by selecting the **Forgot** link on the [sign-in page](https://www.braintreegateway.com/login). Alternatively, users with the Manage Users [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-manage-users-addeditdeletereset-password) can change passwords in the Control Panel. To reset a user's password:


- Log into the[Control Panel](https://www.braintreegateway.com/login).
- Select the gear icon in the top right corner.
- Select**Team**from the drop-down menu.
- Locate the user you'd like to make changes to.
- Select the link in theUsername,Name, orEmailcolumn.
- Scroll to the**Authentication**section.
- Select the**Change Login**button.
- Select**Yes**to confirm the change.

The user will then receive an email to either reset their password or [log in using their PayPal credentials](#log-in-with-paypal).


**IMPORTANT**
 If there is a phone number associated with the user (listed in the **Details** section), they will also be required to authenticate the password reset with a code sent via text to their mobile device.

 


### Password requirements

New passwords must meet the following criteria:


- Must be at least 14 characters
- Must include at least 1 letter and 1 number
- Can't be one of the last 4 previously used passwords

