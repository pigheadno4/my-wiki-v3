<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/reporting/settlement-batch-summary -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Settlement Batch Summary
slug: /articles/control-panel/reporting/settlement-batch-summary/
createTime: '2025-04-02T00:34:41.840Z'
updateTime: '2025-04-02T00:34:41.862Z'
---



# Settlement Batch Summary

Transactions that have been [submitted for settlement](/braintree/articles/get-started/transaction-lifecycle#submitted-for-settlement) are sent to processors in groups known as settlement batches. The Settlement Batch Summary displays the total sales and credits for each batch. You can limit the scope of your Settlement Batch Summary by setting a date range, selecting specific merchant accounts, and excluding certain payment types.


## Running a Settlement Batch Summary

Only users with the Create, Run, and Download Reports [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-create-run-and-download-reports) can access the Settlement Batch Summary. To run a Settlement Batch Summary:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Next to**Settlement Batch Summary**, click the**Run Report**button
- If necessary, specify a[merchant account](/braintree/articles/control-panel/important-gateway-credentials#merchant-account-id)
- Select your desired date range
- Select any desired payment method exclusions (if applicable);[learn more](#excluding-paypal-or-american-express-transactions)
- Click the**Run Settlement Batch Summary**button
- Click the**Download**button if you'd like to export your results as a CSV (maximum 40,000 rows)


**NOTE**
 Settlement Batch Summaries are not available for marketplace sub-merchant accounts.

 


### Excluding PayPal or American Express transactions

If you are set up to accept PayPal transactions, you can better reconcile Settlement Batch Summaries with your Braintree disbursements by excluding PayPal from this report. Similarly, if you use your own Amex account, it may be helpful to exclude Amex transactions, because Amex funds won’t be included in Braintree deposits.


### Settlement batch cutoff times

The cutoff time that determines which transactions are included in each settlement batch depends on your account setup and can’t be changed. [Contact us](/braintree/help) if you have any questions about your specific setup.


## Emailing Settlement Batch Summaries

Each user in your Control Panel can opt to receive daily Settlement Batch Summary emails to keep up with transaction activity. To enable this feature:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on your user icon in the top right corner
- Click**My User**from the drop-down menu
- Scroll to the**Notifications**section
- Check the box next toEmail Daily Settlement Batch Summary
- To include a breakdown of transactions by card type, check the box next toInclude payment type details
- Click the**Save**button

If your user has the Manage Users [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-manage-users-addeditdeletereset-password), you can enable this for others. To do so:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Team**from the drop-down menu
- Click the**Edit**link in the far right column of the desired user
- Scroll to the**Notifications**section
- Check the box next toEmail Daily Settlement Batch Summary
- Click the**Save**button

