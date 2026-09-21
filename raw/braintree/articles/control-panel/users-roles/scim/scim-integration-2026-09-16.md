<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/users-roles/scim/scim-integration -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: SCIM Integration Guide
slug: /articles/control-panel/users-roles/scim/scim-integration/
createTime: '2025-04-01T22:47:06.407Z'
updateTime: '2026-03-30T14:16:30.814Z'
---



# Overview

This guide provides step-by-step instructions on how to integrate either Okta or Microsoft Entra with Braintree as SCIM providers. Thisenables automated user provisioning, de-provisioning, and user role and merchant account access management through these Identity providers.

If you are looking to integrate through SCIM with Braintree using OneLogin or another IdP solution, we are currently working on guides for these options. For now, refer to the IdP's own guide on creating a custom SCIM app or integration.




##### Supported Features

Braintree's SCIM integration supports User Create, Get, Update, and Delete. We also support Group Update. We do not support creating or deleting groups for roles and merchant accountsthrough SCIM. Roles and merchant accounts themselves must continue to be managed through the BT website.




## Pre-requisites for Onboarding to SCIM


**IMPORTANT**
Onboarding to SCIM is only possible if you fulfill these essential requirements.

Before starting, ensure that:


- You have administrative access to your Okta organization.
- You are a managed merchant (ie, you have a dedicated CSM or TAM). We are not currently onboarding unmanaged merchants to SCIM.
- You have both a production and a sandbox merchant with us. If you do not have a sandbox merchant, create one at[https://apply.braintreegateway.com/signup/sandbox](https://apply.braintreegateway.com/signup/sandbox),and send us the merchant's public ID. A sandbox merchant is requiredfor us to onboard you to SCIM, as we do not allow onboarding to SCIM in production without said sandbox merchant being onboarded first.
- Your sandbox and production merchants are onboarded to SSO and use a BraintreeOIN app instance for each merchant to establish the SSO connection. Even if you are already using Okta for SSO for Braintree, you must be using an instance of the Braintree OIN app for us to onboard you to SCIM. If you need to onboard to SSO or switch to an OIN app instance for the SSO connection, please use[our SSO guide](https://developer.paypal.com/braintree/articles/guides/single-sign-on-sso).
- All users you want managed with SCIM who use SSO to log in are converted to SSO users, or are already SSO users.**You cannotconvert existing non-SSO users to SSO onceonboarded to SCIM.** Refer to our[SCIM FAQ](https://developer.paypal.com/braintree/articles/control-panel/users-roles/scim/scim-faq), specifically the "**Now that I'm on SCIM, I'm not able to create new SSO users or edit existing ones. What gives?**" section for further details.
- For your sandbox and production merchant, there are nopendingSSO users.**Pending SSO users are not allowed during SCIM onboarding**and must be resolved to another status before we can onboard you to SCIM (**active**,**suspended**, or**deleted**). Please refer to the FAQ guide linked above, specifically the "**When I import my users, it won't let me import my pending users from Braintree**" section for more information.

If you do not meet all of these prerequisites, please work with your CSM/TAM to ensure you do. We will not be able to onboard you to SCIM until you meet all of these requirements.


## Setup and configuration steps


##### Reach out to Braintree support (Okta or Entra)




- To begin with, reach out to your CSM/TAMand ask to be onboarded to SCIM on Braintree. If you do not have a dedicated CSM/TAM, you cannot be onboarded to SCIM at this time.
- The Braintree Identity team will need to run some internal tasks to get your merchant account ready for the SCIM integration process.
- When we do this, we will disable your ability to edit SSO users on the control panel to ensure data consistency.
- We will also provide you with a SCIM access token. This is what is used by Okta/Entra to access your Braintree merchant account and take actions upon it on your behalf.






## Okta Setup



Accessing the Okta Admin Console




- Log in to your Okta Admin Console




##### Adding the SCIM app

**Note** : If you are already using the Braintree OIN app for SSO, then you will not need to create a new instance of said application in order to onboard to SCIM. You can use this existing application for your SCIM integration. Please ensure the application information mentioned in step 5 below is accurate for your existing OIN application instance. After confirming this, you can skip this section and continue at "Configuring the SCIM Integration".




- Navigate to the "Applications" Section:
- In the left-hand menu, select "Applications", then select "Applications"again.


- Open the Okta Integration Network (OIN):
- Select B"rowseApp Catalog".


- Search for the SCIM app:
- Use the search bar to find the Braintree app.
- You can also add our integration by directly navigating to its OIN marketplace page:[https://www.okta.com/integrations/braintree/](https://www.okta.com/integrations/braintree/)


- Select and add the app:
- Select the "Braintree" app from the search results.
- Select the "Add"button to start the integration process.


- Configure general settings:
- Follow the prompts to configure the basic settings for the app. This is when you'll input your SSO callback URL to the application so it knows how to connect.
- For "BT SSO Partial Callback URL", this comes from your SSO configuration. This is the UUID at the end of your SSO Callback URL already provided to you by Braintree support during your SSO onboarding. For example, if your full SSO Callback URL is "https://id.sandbox.braintreegateway.com/sso/callback/14dcc51e-7aa5-474a-a746-12bcf7db52d1", then the partial SSO Callback URL used by the OIN app would be "14dcc51e-7aa5-474a-a746-12bcf7db52d1"
- "SCIM Endpoint" is the endpoint Okta will use to send SCIM requests to. This variable is environment specific. So, if your merchant is in Braintree sandbox,use "id.sandbox.braintreegateway.com". For a production merchant,use "id.braintreegateway.com". You can tell which environment your merchant is in by looking at the URL of the merchant's home page. If you see "sandbox" in the URL, then this is a sandbox merchant.
- Select Done after you have completed the configuration.









**Note** : If you are already using Okta for SSO with an existing custom app, you'll have to do a cutover of the SSO target from the old app to this new OIN app instance. Send us the new OIN app's cert,SSO target url, and the timeframe by which you want us to do the cutover and then we can change, on our side, which app we expect users to use to login. You will need to assign all of your existing users to the new OIN app before we do the cutover, or else they won't be able to login.




##### Configuring the SCIM Integration


- Open the SCIM App Settings:
- After adding the app, go back toApplications &gt; Applications.


- Select the SCIM app you just added to open its settings.


- Go to the"Sign On" Tab, then click "More Details".


- Copy the Sign-on URL and Certificate. Send those to your Braintree contact. They will need to update the SSO configuration on our side to point to this new application, or else your users will not be able to login via this new app. Please refer to [https://developer.paypal.com/braintree/articles/guides/single-sign-on-sso#how-to-perform-an-sso-provider-or-application-migration](https://developer.paypal.com/braintree/articles/guides/single-sign-on-sso#how-to-perform-an-sso-provider-or-application-migration) for more information on how to complete this process.


- **Note** : This step is not necessary if you are already using this OIN app instance for SSO with us, as we already have the SSO configuration on our side matching this app's SSO information, or else the SSO login this app is already providing wouldn't be functioning.




- Now, navigate to the "Provisioning" Tab:
- Select theProvisioningtab.


- Configure API Integration:
- Select "Configure API Integration".
- Check the box labeled "Enable API Integration".
- Enter the required SCIM API credentials:

- "OAuth Bearer Token": This is the token used to authenticate SCIM API requests. At this point in the setup, you should've received this from Braintree. If you have not, reach out to us.



- 

"Import Groups": Ensure this is checked as enabled. Otherwise, you will not be able to setup role/merchant_account access management.


- Test API Credentials:
- Select "Test API Credentials"to verify the connection to your application.
- If the test is successful, select "Save".
- If it fails, read the error message. It is likely you have misentered the access token.






##### Defining Provisioning Settings




- Enable Provisioning Features:
- In the "Provisioning"tab, then the "To App"tab, enable the necessary provisioning features by checking the relevant boxes:

- "Create Users": Automatically creates users in Braintree.
- "Update User Attributes": Automatically updates user information in Braintree.
- "Deactivate Users": Automatically deactivates users in Braintree.
- Sync Password: You do not need to sync passwords, as SSO users at Braintree have no password. Feel free to leave this unchecked.



- Map Attributes:
- Select "To Okta"to configure attribute mappings between Okta and your application.
- Ensure the mappings match the sample. You can also leave it as the defaults:![Attribute,Mapping,Sample](https://www.paypalobjects.com/devdoc/okta-scim.png)
- Navigate to the "General" section on this same page.
- Ensure "Okta username format" is "Email Address".
- Navigate to the "User Creation and Matching" section on this same page.
- Ensure "Imported user is an exact match to Okta user if" is set to "Email matches"
- We also recommend (but it is not strictly required) that you set "Allow partial matches" to "Enabled" by clicking the radio button for "Partial match on first and last name"




##### Running the User Import




- Manual User Import:
- After setting up the application and the SCIM connection, you must run the user import to automatically set up the Braintree users and their roles in Okta.
- Open theImporttab.
- SelectImport Now.


- Review Import Results:
- After the import is completed, review the results.
- You likely will have users you need to confirm before Okta will create them automatically from the Braintree data it just imported. These users will show up on the import page as unconfirmed users. Review the data and confirm the users. You can refer to the following**Matching and Confirming Users**section on how to do this.
- SelectView Logsto check for errors or issues during the import process.
- Go to thePeoplesection to see the newly imported users and their profiles.

**Note**: Pending users (i.e, SSO users that have been created in Braintree but have not logged in yet) do not have a name. As such, when you try to import them to Okta, it will fail due to the users having a lack of a name. The workaround is to manually create these users on Okta (or use the existing user on Okta), then assign those users manually to the new OIN app we created. This will cause Okta to send us a call to update the name on our side.




##### Matching and Confirming Users




- Matching Users:
- Okta will attempt to match imported users with existing Okta users based on attributes such as email address or username.
- Review the matched users to ensure they are correctly identified.


- Confirming Users:
- Confirm the new users to finalize the import.
- For unmatched users, decide whether to create new Okta user accounts or ignore them.






##### Assigning push groups to the app groups




- After the import, the app groups in Okta will be automatically created, and users will be assigned to them automatically. In order to see the groups the import created, navigate to "Directory" in the sidebar, then "Groups".
- Once you are on the groups page, change "Group source type" to "App groups". You should see the four sets of groups created by the import below, and they should be populated with the users associated with the roles/merchant_accounts/GAMA/API Access associated with that group. See below for an explanation of the four sets of groups.
- When you first do the import, it will create four sets of groups. These groups will have the type "app group" in Okta. These four sets of groups are:
- **Role Groups**: Every role on your merchant will have its own group. In order to add or remove a user from a role in Braintree, you will add or remove the user from the associated role group in Okta. The name of a given role's group in Okta when imported will be in the format "BT [SANDBOX/PRODUCTION] Role [ROLE_NAME]". For example, for my role "Accountants" on my production merchant, the corresponding role group in Okta will be named "BT PRODUCTION Role Accountants".
- **Merchant Account Groups**: Every one of your merchant accounts will also have a group associated with it. In order to add or remove a user's access to a given merchant account, you must add or remove that user from the associated Okta group. The name of these groups will be in the format "BT [SANDBOX/PRODUCTION] Merch Acct [Merchant_Account_Unique_Id]". For example, if I have a merchant account in production with the unique ID "kwdnwhs", the name of the group associated with said merchant account will be "BT PRODUCTION Merch Acctkwdnwhs".
- **Grant All Merchant Accounts Group**: This is a unique group every merchant has. If a user is a part of this group, they will have the grant_all_merchant_accounts flag enabled on their user. This flag allows this user to access ALL merchant accounts on your merchant gateway, regardless of their membership in the individual merchant account groups. This group will be named "BT [PRODUCTION/SANDBOX]Grant All Merch Accts [merchant public_id]". For example, if your sandbox merchant's homepage is[https://sandbox.braintreegateway.com/merchants/hsbcfkndts9pp5d4/home](https://sandbox.braintreegateway.com/merchants/hsbcfkndts9pp5d4/home), then your merchant's public_id is hsbcfkndts9pp5d4, so your grant all merchant account group's name would be "BT SANDBOX Grant All Merch Accts hsbcfkndts9pp5d4". There will only ever be one of this group per merchant.
- **API Access Group**: The second unique group you will have is the API Access Group.If your user is in this group, they will be able to create and use API keys and tokenization keys associated with their user. Learn more about API keys and tokenization keys here:[https://developer.paypal.com/braintree/articles/control-panel/important-gateway-credentials#api-credentials](https://developer.paypal.com/braintree/articles/control-panel/important-gateway-credentials#api-credentials)and[https://developer.paypal.com/braintree/docs/guides/authorization/tokenization-key/javascript/v3](https://developer.paypal.com/braintree/docs/guides/authorization/tokenization-key/javascript/v3)). Likewise, if the user is not in this group, they will not be able to create or use API keys or tokenization keys associated with that user. This group's name will be "BT [SANDBOX/PRODUCTION] API Access Enabled [merchant public_id]". For example, if your merchant homepage ishttps://sandbox.braintreegateway.com/merchants/hsbcfkndts9pp5d4/home, then your merchant's public_id is hsbcfkndts9pp5d4, therefore your API Access group's name will be "BT SANDBOX API Access Enabled hsbcfkndts9pp5d4".


- Before setting up the push groups for the above four sets of groups, you should setup a master Okta group to manage which users are assigned to Braintree.
- Go to the "Groups" tab under "Directory" and then click "Add Group".
- Name this group something meaningful, like "All Braintree Users".
- Then, open this group's individual page by clicking the name of the group in the groups page.
- Once on the group's individual page, click "Applications", then "Assign applications", then select the OIN app we setup as part of this onboarding guide. This will assign this group to your BT OIN app. This is so, when you add a user to this group, it will automatically provision that user on the Braintree portal. Likewise, if you remove a user from this group, it will suspend the user on the Braintree portal (assuming you do not directly assign the user to the Braintree OIN app or assign it to the OIN app via a different group).
- Once the group is assigned to the Braintree OIN app, assign all of the users you want to have access to Braintree to this group by going to the "People" tab in the group's individual page, and clicking "Add People".
- As an aside, you cannot use push groups as a way to manage users' overall access to Braintree. This can lead to bad edge cases. Refer to the below linked troubleshooting guide for more information on this edge case.


- Once you setup the master Braintree assignment group in the previous step, you need to setup the imported groups as push groups. This is so you can automate role/merchant_account access.You can do this by following the below steps:
- On the "Groups" page (Located by clicking "Directory" on the left sidebar), click "Add Group".
- For the Name of the new group, it MUST EXACTLY MATCH the App group name. So if you're setting up the push group for your API Access Group named"BT SANDBOX API Access Enabled hsbcfkndts9pp5d4", then you MUST name this new group to match this EXACTLY.
- For the description, it doesn't affect the integration what you put, but we suggest some description that says this is a push group, for example, just putting "push group".
- Click "Save" and copy the group's name. You will need it later.
- At this stage, there should now be two groups with that name, one with the type "app group" and populated with users, and one with the type "Okta group" and empty. You MUST populate the Okta group's membership with the same membership of the App group. If you do not, when you merge the two groups into a push group in the later steps, Okta will empty the membership of the new group to match the empty Okta group, and might push this empty membership to us, removing all user's access to the associated role/merchant_account on our side.
- Once you do this, navigate to your OIN app's page by clicking "Applications" on the left sidebar, then "Applications" underneath that, then selecting the OIN app we've been manipulating.
- Once on the application's page, click the "Push Groups" tab, then the blue "+ Push Groups"button, then "Find groups by name".
- Paste or type the group's name you just created into the search bar. Underneath the "Match Result and push action" title, it should show "Match found".
- Click "Save". If you enabled "push group membership immediately/automatically" earlier in the setup, then it will immediately push the group's membership to us. If you followed the above group setup instructions correctly, and pre-populated the Okta group's membership BEFORE merging the groups, then it should affect no change on our side. Please go to the Braintree control panel and verify no change has occurred.
- If you did not setup this automatic membership push, then you must go to the "push groups" tab, then click the "Active" section under "Push Status" next to this group, then "Push now".
- Repeat this cycle for every other app group you see in the groups tab. By the end, there should be no BT app groups left, as they will all be converted to push groups, which have the group type "Okta group".
- To save time, you can create all the Okta groups for all of your app groups right after the import, then use "save and add another" on the push group search page in the previous step. Please ensure you update the membership of each Okta group BEFORE you make it a push group, or you will remove all your users from the associated role / merchant account on Braintree.
- As a note, we recommend against assigning the push groups themselves' to the Braintree OIN application. If assignment is handled incorrectly, it can lead to some bad edge cases.




**IMPORTANT**
Ensure users are assigned to the Okta groups before linking them to the app groups as a push group, otherwise their roles will be removed. Refer to the troubleshooting guide below for more details.




##### Assigning Users to the App post-import




- Create the user in Okta.
- Navigate to the Groups Tab:
- Select the master Braintree user group we created in the previous step.


- Assign Users or Groups:
- SelectAssign&gt;Assignto People.
- Select the user you want to provision to the application.
- SelectAssignand thenDoneto complete the assignment.
- Braintree users require at least one role to log in to Braintree, so you'll want to assign this user to a push group as well.
- Follow the above steps for adding to the master group, but for one of the push groups we set up above.
- If your push groups are set up to push synchronously, it will push this change automatically to Braintree.
- If your push groups are async, you'll need to manually push the group changes by going to thePush Groupstab on theApplicationpage.






##### Testing Provisioning




- Verify User Creation:
- Assign a test user to the application and check if the user is created in Braintree.


- Verify Attribute Updates:
- Update the test user's group membership in Okta and ensure the changes are reflected in Braintree.


- Verify User Deactivation:
- Deactivate the test user in Okta and confirm that the user is suspended in Braintree.






##### Monitoring and Troubleshooting




- Check Provisioning Logs:
- In the SCIM app settings, go to theProvisioningtab.
- SelectView Logsto see the provisioning logs and check for errors or issues.


- Review SCIM Events:
- Go toReports&gt;System Logto review SCIM-related events.


- Resolve Issues:
- If any errors occur, consult the logs and verify that SCIM endpoint details and attribute mappings are correctly configured and that you are getting a successful response from Braintree. The Okta user's username MUST match the email.
- If you cannot resolve the issue, contact Okta support.








## Microsoft Entra Setup


##### 

Log in to [https://portal.azure.com/](https://portal.azure.com/)


- Navigate to Enterprise Applications
- Select on "New Application."
- Select "Create your own application."
- Give it a name
- Select "Integrate any other application...(non-gallery application)"
- Select Create
- The new application is created with default settings
- Follow the steps in the "Get Started" section
- Navigate to "Assign Users and Groups"
- Click on "Add user/group" and search for the Groups/Users, and "Assign" to the application
- Navigate to "Setup Single-Sign on"
- Select "SAML" Authentication strategy
- In the "Basic SAML Configuration" section: Update Identifier, Reply URL, Sign On URL to the BT callback URL provided by your CSM.
- Download the Base64 Certificate and Login URL from this application and share them with your CSM. We will need these to set up SSO on our end.
- Select the "Test" button to confirm that the Single Sign-On configurations are updated correctly. Confirm you can redirect to the Braintree SSO Login page
- After your CSM has confirmed the SSO configuration has been set up on our side, assign an SSO user that already exists on the Braintree side to this Entra app.
- Have the user attempt an SSO login to the Braintree platform. If it does not work, stop here and work with your CSM to get the SSO login working. The SSO config may not match on one side or the other.
- Navigate to "Get Started with application provisioning."

**Note:** Before you continue the setup, ask the Braintree Engineering team to provide you with an SCIM access token to complete it.


- Select the "Connect your application" button for creating the configuration
- Select the "Bearer Authentication" authentication method
- Enter the following Tenant URL:
- Production:[https://id.braintreegateway.com/scim](https://id.braintreegateway.com/scim)
- Sandbox:[https://id.sandbox.braintreegateway.com/scim](https://id.sandbox.braintreegateway.com/scim)


- In the "Secret Token" field, input the access token provided by your CSM.
- Confirm the authentication method by clicking on "Test Connection". If the configurations are valid, you will notice a "Connection Successful" growl notification.
- Navigate to Configure Users & Groups -&gt; Map attributes
- For Users: Confirm userName, givenName, familyName, and nameFormatted attributes are mapped. Remove all other attributes, as these will break the user provisioning. The userName must be mapped to your Entra user's email address.
- For Groups: Confirm that displayName, externalId, and members attributes are mapped. (Default settings work)
- Navigate to "Test "On-demand provisioning" flow":
- Select a user to provision into Braintree, and click on the "Provision" button.
- If you are seeing an error regarding "the source system", it means something is wrong with the Entra user. It is likely not active in Entra, or is not assigned to the application. The user must be assigned to the application before you attempt to provision them.
- If On-demand Provisioning is successful, you will see a confirmation page of the provisioned user.
- Finally, enable "Start provisioning" by clicking the "Start Provisioning" button, and confirm you see a "Start Successful" Growl notification.
- Confirm that Provisioning has been started and wait for the upcoming sync to finish. This may take a while for initial Provisioning.
- After Entra states the automatic Provisioning is complete, confirm its success by logging into Braintree as a user admin, navigating to your users page, and seeing the users created on said page as pending users.

**Setting up push groups:**

The above guide for Entra only covers setting up automatic user provisioning and management. We are still working on a guide for setting up automatic role/merchant account access management for Entra. For now, refer to Microsoft's guides on the matter.



**For more information, check out our** [FAQ](/braintree/articles/control-panel/users-roles/scim/scim-faq#troubleshooting-and-faqs).




## Post-Configuration Testing Steps



At this point in the guide, you should have your user management automated, as well as your role and merchant account access management automated. We highly recommend you walk through a few different actions on your IdP to ensure all features of SCIM are functioning. Please refer to the below list of basic actions to walk through:


- Adding and removing a user to the application
- Adding and removing a user from a role group
- Adding and removing a user from a merchant account group
- Adding and removing a user from the API Access group
- Adding and removing a user from the Grant All Merchant Accounts group
- Creating a new user and adding them to your IdP and the Braintree application
- Having an SSO user login via both our SSO login page ([https://id.braintreegateway.com/sso/sessions/new](https://id.braintreegateway.com/sso/sessions/new)) and through your IdP.

Please remember that we do not support:


- Creating a new role or merchant account through SCIM / your IdP
- Deleting a role or merchant account through SCIM / your IdP
- Changing the name of a role or merchant account through SCIM / your IdP
- (Okta only) Deleting an SSOBraintree user through SCIM / your IdP
- Any management of non-SSO users through SCIM / your IdP

All of these actions MUST be undertaken on the Braintree control panel directly (and in the case of deleting SSO users, cannot be done at all due to how Okta has chosen to implement their SCIM integration). For more information on our SCIM integration, or help with any edge cases or gotcha's you run into, please refer to our SCIM FAQ page here: [https://developer.paypal.com/braintree/articles/control-panel/users-roles/scim/scim-faq](https://developer.paypal.com/braintree/articles/control-panel/users-roles/scim/scim-faq)


##### 



