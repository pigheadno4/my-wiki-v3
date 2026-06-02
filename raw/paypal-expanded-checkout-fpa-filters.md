<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/fraud-protection/fraud-protection-advanced/filters/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Create and set up filters
slug: >-
  /docs/checkout/advanced/customize/fraud-protection/fraud-protection-advanced/filters/
createTime: '2025-01-29T14:28:56.903Z'
updateTime: '2025-02-05T22:31:48.416Z'
---


# Create and set up filters

Filters are the rules that decide whether Fraud Protection Advanced (FPA) approves, rejects, or puts a transaction into a review queue.

The **Filters** tab displays customized filters that you can choose to enable or adjust, or you can create your own. You'll also see simulations based on your current filter settings applied to your historical data for a selected time period.


**info**
All customized filter recommendations are disabled by default. To activate them for fraud detection, you must manually enable each one.


![Filters tab overview](assets/Create_setup_filter.png)



## Create a new filter 
To add a new filter, use the following steps:

- Select **Add Filter** on the **Filters** tab. A popup window will open.
- Enter the **Filter Name** and provide a **Description** for the filter. The **Decision Label** will automatically be set to one of the following options based on the type of filter you create: **Approve** , **Reject,** or **Review** .
![Setup Filters — Create dialog](assets/Setup_Filters_Create.png)

- To add conditions to the filter, select **+Condition** and specify the desired fields. For example, you can specify conditions on transaction attributes or risk scores.
- Select **Add** . The popup window will close. To apply the filter, you must click **Test** and **Save** , else the filter changes will not be saved.
![Setup Filters — Test and Save](assets/Setup_Filters_CreateTestAndSave.png)


## Enable customized filters 
To enable customized filters, use the following steps:

- On the **Filters** tab, locate the filter you want to enable, then select the pencil icon in the **Actions** column. This will open the filter configuration in a popup window for editing.
![Enable customized filters — pencil icon](assets/Enable_Cust_Filters.png)

- Toggle the Status to **On** then select **Change** button. The popup window will close. To apply the change, you must select **Save** and then confirm your changes.
![Setup Filters — Edit filter dialog](assets/Setup_Filters_EditFilter.png)

![Setup Filters — Edit Test and Save](assets/Setup_Filters_EditTestAndSave.png)


## Edit filters 
- Select the pencil icon available in the **Actions** column for each filter. The filter configuration will open in a popup window, where you can make changes to the filter. Once done, select **Change** . The pop-up window will close.
![Edit filter dialog](assets/Edit_filter.png)

- To apply the change, you must select **Save** and then confirm your changes. If you don't select **Save** , your changes will not be saved as indicated in the message shown in the following screenshot.
![Email address filter — unsaved changes warning](assets/Email_address_filter.png)

![Confirm filter changes dialog](assets/Confirm_filter.png)


## Related resources 

### Manage lists
Use the lists feature to manage information and work with their rules
to help prevent fraud.


### Review transactions
Review transactions that are flagged for review.


### Monitor FPA activity
You can track which users made changes and when these changes occurred.
