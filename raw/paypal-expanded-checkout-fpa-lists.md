<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/fraud-protection/fraud-protection-advanced/lists/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Manage lists
slug: >-
  /docs/checkout/advanced/customize/fraud-protection/fraud-protection-advanced/lists/
createTime: '2025-01-29T20:56:00.409Z'
updateTime: '2025-02-05T23:13:30.672Z'
---


# Manage lists

The **Lists** tab shows the attributes for which you can create lists, the number of items on each attribute list, and whether an active filter is associated with each list.

You can use **Blocklists** to prevent known bad actors and **Allowlists** to ensure your trusted customers can check out smoothly. **Reviewlists** automatically queue transactions with specific attributes for manual review, allowing your team to decide whether to approve or reject them.

![Lists tab overview](assets/FPA_Home_Lists.png)

## Default lists 
Fraud Protection Advanced (FPA) provides **Blocklists** , **Allowlists** , and **Reviewlists** by default for each of the following attributes:

- Billing Country
- Billing ZIP
- Card Hash
- Email
- Email Domain
- Billing Address
- Shipping Address
- Phone
- Shipping Country
- Shipping ZIP
- Cardholder Name



## Add items to lists 
You can add items to lists using the following steps:

- On the **Lists** tab, select one of the following categories you want to add items to: **Blocklists** , **Allowlists** , or **Reviewlists** .
- Choose the specific list you want to add items to, such as **Email** , and then select **+Add Items** .
![Add Items to list](assets/FPA_Add_items_to_lists.png)

- A pop-up window will appear, where you can enter comma-separated individual email addresses or upload a .csv file to add multiple emails in bulk. Select **Add** to proceed.
![Add Items dialog](assets/FPA_Add_Items.png)

- You'll see another pop-up window. Select **Confirm** . Your data will get added to your chosen list. You will then see the list updated on the **Lists** tab.
![Confirm list addition](assets/FPA_Confirm_lists.png)


**info**
Adding an item to the list does not ensure that the filter for the list will work for the newly added item. You need to create a filter again and specify the necessary conditions. Select **Create Filter** to set up the filter as shown below.

![Create Filter for list](assets/FPA_Create_filter.png)



## Delete items from lists 
You can delete items as well by selecting an item from the respective list and then selecting **Delete Items** .

![Delete Items from list](assets/FPA_Delete_Items.png)

## Related resources 

### Create and set up filters
Use filters to decide whether FPA approves, rejects, or puts a transaction into a review queue.


### Review transactions
Review transactions that are flagged for review.


### Monitor FPA activity
You can track which users made changes and when these changes occurred.
