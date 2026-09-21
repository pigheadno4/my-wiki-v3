<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/custom-fields -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Custom Fields
slug: /articles/control-panel/custom-fields/
createTime: '2025-04-02T01:10:09.720Z'
updateTime: '2025-06-05T09:21:24.910Z'
---



# Custom Fields

Custom fields allow you to customize your checkout experience by collecting specific information about your customers and their purchases.

You can include custom fields when:


- [Creating a transaction](/braintree/docs/reference/request/transaction/sale/ruby#custom-fields)
- [Creating a customer in the Vault](/braintree/docs/reference/request/customer/create#use-custom-fields)
- [Updating a customer in the Vault](/braintree/docs/reference/request/customer/update#custom_fields)
- [Creating a 3D Secure authentication](/braintree/docs/guides/3d-secure/rules-manager#custom-fields)


## Custom field types

There are two types of custom fields: Pass Thru fields and Store and Pass Back fields.


### Pass Thru fields

Pass Thru fields are designed to pass a value from your checkout form to your servers, where you can either store or respond to the data. For example, if you have a checkbox for "Join Mailing List" on your checkout form and you pass this data through as a custom field, your servers can respond by adding the customer to your mailing list.

While Pass Thru custom fields are [configured in the Control Panel](#creating-a-custom-field), they can only be used to pass data via the API.


### Store and Pass Back fields

The data passed by Store and Pass Back fields is stored in the Control Panel and returned via the API [on the transaction response object](/braintree/docs/reference/response/transaction#custom_fields). It's also available for download via a [Transaction or Vault Search](/braintree/articles/control-panel/search#advanced-search-options). Keep in mind that you can only search for the data passed within a Store and Pass Back field; you won’t be able to search for the field name itself.


## Creating a custom field

Custom fields can only be configured directly in the Control Panel by users with the Add/Edit Processing Options [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-addedit-processing-options-including-avscvv). There isn’t a way to set up new custom fields via the API.

To create a custom field:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Account Settings**from the drop-down menu
- Scroll to the**Transactions**section
- Next to**Custom Fields**, click the**Options**link
- Click the**Add**link located on the right side of the page
- Enter a custom field API name to pass with your code
- This value must be less than or equal to 255 characters and can't contain any spaces or capital letters


- Enter a display name
- This is what will appear in your transaction history and Vault records


- Under the**Options**section, select eitherStore and Pass BackorPass Thru
- Click the**Add Custom Field**button


## Editing a custom field

In order to edit custom fields in the Control Panel, your user's role must have the Add/Edit Processing Options [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-addedit-processing-options-including-avscvv) enabled. To edit a custom field:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Account Settings**from the drop-down menu
- Scroll to the**Transactions**section
- Next to**Custom Fields**, click the**Options**link
- Click the link located in theDisplay Namecolumn of the field you'd like to edit
- From here, you can:
- Change the field's display name
- Toggle betweenStore and Pass BackandPass Thrufield types


- Click the**Save**button


## Deleting a custom field


**NOTE**
 You can only delete custom fields that have never been used to collect customer or transaction data.

 

In order to delete custom fields in the Control Panel, your user's role must have the Add/Edit Processing Options [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-addedit-processing-options-including-avscvv) enabled. To delete a custom field from the Control Panel:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Account Settings**from the drop-down menu
- Scroll to the**Transactions**section
- Next to**Custom Fields**, click the**Options**link
- Click the**X**icon located to the right of the field you'd like to remove
- Click the**Yes**button to confirm


## Viewing the custom fields created through Fraud Protection Advanced

If you are using Fraud Protection Advanced, you can add a specific set of custom fields that pertain to your business in certain filter conditions to mitigate fraud. For more information, see [Fraud Protection Advanced](/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced).

To use these custom fields, you will need to add them via the Fraud Protection Advanced Dashboard. After new fields are added in the Dashboard, you will also see these fields in the Control Panel.

To find these custom fields in the Control Panel:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Account Settings**from the drop-down menu
- Scroll to the**Transactions**section
- Next to**Custom Fields**, click the**Options**link
- From here, you can see all your**ACTIVE**custom fields added through the Fraud Protection Advanced dashboard

