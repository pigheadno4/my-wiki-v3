<!-- Source URL: https://docs.metronome.com/integrations/platform-integrations/sfdc-integration.md -->
<!-- Fetched: 2026-08-28 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sync into Salesforce

To help power your sales-driven workflows, Metronome offers a native integration that syncs Metronome data back to your Salesforce instance daily. As sales and revenue operations teams are deeply embedded within Salesforce, it’s critical that Metronome data about how much spend a customer has committed to, how much of the products they’ve purchased access to are being used, and how much of their commitments have been burned down as a result makes its way back into Salesforce. Signals from this data can then be used to help these teams initiate upsells, cross sells, and downgrade motions in a timely fashion.

The Salesforce integration can empower your customer-facing teams to quickly answer questions like:

* What are the terms of my customer's current contract(s)?
* What are their outstanding credits and commits?
* How much of those credits and commits have been used up to date?
* How has that consumption trended through the lifetime of the contract?
* What is my customer's usage in the current month? What is their current month's spend (invoice total)?
* How has that usage and spend trended through the lifetime of the contract?

## How the Salesforce integration works​

The Metronome → Salesforce integration is powered by a tool called Census. Census acts as an ETL service to push data from Metronome to your Salesforce instance daily.

Setting up the integration in Metronome takes four steps:

1. Install the Metronome ↔ Salesforce package.
2. Set up your Census workspace.
3. Link Census to your Salesforce destination.
4. Determine what data to sync.

You need to repeat this process in every Metronome environment (like Staging and Production) where you want data synced back to Salesforce.

## Set up the integration​

To set up the Salesforce integration:

1. In the [Metronome app](https://app.metronome.com/), click **Developer** in the left sidebar.

2. Click **Get Started** on the Salesforce card found under **Available Integrations**.

3. On Step 1 of the menu, click **Install Now** to download the Metronome ↔ Salesforce package.

   <Warning>
     **CAUTION**

     Make sure that you install the package in the Salesforce instance that you intend to authenticate with in step 7.

     Clicking this link inside any non-production Metronome environment takes you to [test.salesforce.com](http://test.salesforce.com), whereas clicking this link inside the Metronome production environment takes you to [login.salesforce.com](http://login.salesforce.com). You can update the URL to ensure that you install the package in the desired Salesforce instance.
   </Warning>

   * The page prompts you to select which Salesforce users you want to install this package for: Admins Only, All Users, or Specific Profiles. Give access to the user who will grant Census access to Salesforce in step 7.
   * After confirming your selection, click **Install**. The installation process may take a few seconds.

4. Once the Metronome ↔ Salesforce package successfully installs, return to Metronome.

5. On step 2 of the Salesforce card menu, click **Activate Now** to set up a Census workspace.

6. On step 3 of the menu, click **Link Salesforce** to grant Census access to Salesforce. Clicking this link takes you to Census.

   * Select which Salesforce domains you'd like to sync data to (Production or Sandbox).
   * Grant Census access to proceed by clicking **Allow**. This process may take a few seconds to complete.
   * Click **Finish** to return to Metronome and complete the integration set-up.

7. On step 4 of the Salesforce card menu, choose whether you want data synced for all customers in Metronome or just those linked to a Salesforce account.

<Tip>
  **TIP**

  To link a Metronome customer to a Salesforce account, navigate to that customer’s page in Metronome, click **Settings,** find the Salesforce card under Linked Accounts, click **Connect** , and enter the Salesforce account ID you’d like to associate to that customer. You can also do this programmatically when creating customers in Metronome.
</Tip>

8. Click **Complete Setup** to complete the integration setup. Metronome then begins setting up your Census workspace and associated syncs. This process may take a few minutes.

Once the setup process completes, the menu closes automatically and Salesforce appears listed under the **Active Integrations** section. The first set of data syncs kick off automatically. The syncs may take a couple of hours to complete and are scheduled to happen once a day. At this time, syncs cannot be configured to happen more frequently.

## Monitor the integration​

Once Census begins syncing data to your Salesforce instance, you can monitor the status of your daily syncs.

To monitor the integration:

1. Go to **Developer** on the left sidebar and open the **Integrations** tab.
2. Click on the **Salesforce** row under the **Active Integrations** section.

There are two tabs: one for **Completed** syncs and one for **Incomplete** (in progress) syncs. The **Completed** syncs tab shows by object type how many rows were attempted to be synced last and, of those rows, how many were successful versus how many failed.

<Info>
  **INFO**

  The total row count reflects the number of rows that *changed* and therefore needed to be re-synced since the time of the last sync. It doesn’t reflect the total count of that record type. For example, if you have 1,000 customers listed in Metronome, but only three changed since the last sync, you should only see three total in the row listed under `metronome_Customer_c`.
</Info>

To troubleshoot any row sync failures, download a CSV file of the row sync errors. To do this, click the download button next to where the errors appear in the **Status** column. This file gives you a sampling of up to 100 failures from that sync for that object type to help you troubleshoot the issue.

## Available data types​

After setting up the integration, these data objects get synced from Metronome to your Salesforce instance on a daily basis.

**metronome\_\_Credit\_Type\_\_c**

| Columns               | **Type** | **Description**                                                  |
| --------------------- | -------- | ---------------------------------------------------------------- |
| `Credit_Type_ID__c`   | text     | The unique identifier associated with the credit type (currency) |
| `Name__c`             | text     | The name of the credit type                                      |
| `Environment_Type__c` | picklist | The name of the Metronome environment where this object lives    |

**metronome\_\_Customer\_\_c**

| Columns               | Type     | **Description**                                                                                              |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------------------ |
| `Customer_ID__c`      | text     | The unique identifier associated with the customer                                                           |
| `Name__c`             | text     | The name of the customer                                                                                     |
| `Account__c`          | lookup   | References the associated Salesforce account for this customer if one has added to the customer in Metronome |
| `Environment_Type__c` | picklist | The name of the Metronome environment where this object lives                                                |

**metronome\_\_Customer\_Ingest\_Alias\_\_c**

| **Columns**                   | Type     | **Description**                                               |
| ----------------------------- | -------- | ------------------------------------------------------------- |
| `Customer_Ingest_Alias_ID__c` | text     | The unique identifier associated with the ingest alias        |
| `Customer__c`                 | lookup   | References the associated customer for this ingest alias      |
| `Ingest_Alias__c`             | text     | The ingest alias associated with the customer                 |
| `Environment_Type__c`         | picklist | The name of the Metronome environment where this object lives |

**metronome\_\_Rate\_Card\_\_c**

| **Columns**           | **Type**       | **Description**                                               |
| --------------------- | -------------- | ------------------------------------------------------------- |
| `Rate_Card_ID__c`     | text           | The unique identifier associated with the rate card           |
| `Name__c`             | text           | The name of the rate card                                     |
| `Description__c`      | text area long | The description of the rate card                              |
| `Environment_Type__c` | picklist       | The name of the Metronome environment where this object lives |

**metronome\_\_Contract\_\_c**

| **Columns**                             | **Type**         | **Description**                                                    |
| --------------------------------------- | ---------------- | ------------------------------------------------------------------ |
| `Contract_ID__c`                        | text             | The unique identifier associated with the contract                 |
| `Customer__c`                           | lookup           | References the associated customer for this contract               |
| `Rate_Card__c`                          | lookup           | References the associated rate card for this contract              |
| `Name__c`                               | text             | The name of the contract                                           |
| `Starting_On__c`                        | datetime         | The inclusive starting time of the contract (UTC)                  |
| `Ending_Before__c`                      | datetime or NULL | The exclusive ending time of the contract (UTC)                    |
| `Usage_Statement_Schedule_Frequency__c` | pick list        | The frequency with which usage statements are sent to the customer |
| `Environment_Type__c`                   | picklist         | The name of the Metronome environment where this object lives      |

**metronome\_\_Commit\_\_c**

| **Columns**           | **Type**               | **Description**                                                                                                                                                          |
| --------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Commit_ID__c`        | text                   | The unique identifier associated with the commit or credit                                                                                                               |
| `Customer__c`         | lookup                 | References the associated customer for this commit or credit                                                                                                             |
| `Contract__c`         | lookup                 | References the associated contract for this commit or credit                                                                                                             |
| `Name__c`             | text or NULL           | The name of the commit or credit                                                                                                                                         |
| `Type__c`             | PickList               | The type of commit or credit (one of prepaid, postpaid, or credit)                                                                                                       |
| `Priority__c`         | number                 | The priority assigned to the commit or credit                                                                                                                            |
| `Description__c`      | text area long or NULL | The description of the commit or credit                                                                                                                                  |
| `Starting_On__c`      | datetime               | The inclusive starting time of the commit or credit (UTC)                                                                                                                |
| `Ending_Before__c`    | datetime               | The exclusive ending time of the commit or credit (UTC)                                                                                                                  |
| `Total_Amount__c`     | number                 | The total dollar amount of the commit or credit. If the commit or credit is broken out over multiple access segments, this represents the sum across all access segments |
| `Current_Balance__c`  | number                 | The current balance on the commit or credit as determined subtracting any burn down, including the current draft invoice, from the total amount                          |
| `Total_Cost__c`       | number                 | The total cost of the commit or credit. If the commit or credit is broken out over multiple invoice segments, this represents the sum across all invoice segments        |
| `Cost_Basis__c`       | formula                | The total cost / the total amount of the commit or credit                                                                                                                |
| `Environment_Type__c` | picklist               | The name of the Metronome environment where this object lives                                                                                                            |

**metronome\_\_Invoice\_\_c**

This includes draft and finalized invoices.

| **Columns**           | **Type**  | **Description**                                                     |
| --------------------- | --------- | ------------------------------------------------------------------- |
| `Invoice_ID__c`       | text      | The unique identifier associated with the invoice                   |
| `Contract__c`         | lookup    | References the associated contract for this invoice                 |
| `Customer__c`         | lookup    | References the associated customer for this invoice                 |
| `Credit_Type__c`      | lookup    | References the associated credit type for this invoice              |
| `Type__c`             | pick list | The invoice type (Scheduled, Usage, Refund, True-up, Adhoc)         |
| `Starting_On__c`      | datetime  | The inclusive starting time of the period this invoice covers (UTC) |
| `Ending_Before__c`    | datetime  | The exclusive ending time of the period this invoice covers (UTC)   |
| `Total__c`            | number    | The invoice total                                                   |
| `Status__c`           | picklist  | The Metronome invoice status (One of Draft, Finalized, Void)        |
| `Issued_At__c`        | datetime  | The time at which the invoice was issued (UTC)                      |
| `Environment_Type__c` | picklist  | The name of the Metronome environment where this object lives       |

**metronome\_\_Invoice\_Line\_Item\_\_c**

This includes draft and finalized invoices.

| **Columns**               | **Type** | **Description**                                                           |
| ------------------------- | -------- | ------------------------------------------------------------------------- |
| `Invoice_Line_Item_ID__c` | text     | The unique identifier associated with the invoice line item               |
| `Invoice__c`              | lookup   | References the associated invoice for this line item                      |
| `Credit_Type__c`          | lookup   | References the associated credit type for this line item                  |
| `Commit__c`               | lookup   | References the associated commit for this line item                       |
| `Name__c`                 | text     | The line item description                                                 |
| `Quantity__c`             | number   | The quantity associated with the line item                                |
| `Unit_Price__c`           | number   | The unit price with the line item                                         |
| `Product_Type__c`         | text     | The product ID associated with the line item                              |
| `Total__c`                | number   | The line item total                                                       |
| `Starting_On__c`          | datetime | The inclusive starting time of when the line item is effective from (UTC) |
| `Ending_Before__c`        | datetime | The exclusive ending time of when the line item is effective from (UTC)   |
| `Environment_Type__c`     | picklist | The name of the Metronome environment where this object lives             |

**metronome\_\_InvoiceLineItemPricingDimensionAssoc\_\_c**

| Columns                      | Type     | **Description**                                                                                    |
| ---------------------------- | -------- | -------------------------------------------------------------------------------------------------- |
| `External_Association_ID__c` | text     | The unique identifier for the many to many mapping between invoice line item and pricing dimension |
| `Invoice_Line_Item__c`       | lookup   | References the associated line item for the many to many mapping                                   |
| `Pricing_Dimension__c`       | lookup   | References the associated pricing dimension for the many to many mapping                           |
| `Environment_Type__c`        | picklist | The name of the Metronome environment where this object lives                                      |

**metronome\_\_Pricing\_Dimension\_\_c**

| Columns                   | Type     | **Description**                                                                          |
| ------------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `Pricing_Dimension_ID__c` | text     | The unique identifier associated with the pricing dimension set on the invoice line item |
| `Name__c`                 | text     | The key of the pricing dimension set on the invoice line item                            |
| `Value__c`                | text     | The value of the pricing dimension set on the invoice line item                          |
| `Environment_Type__c`     | picklist | The name of the Metronome environment where this object lives                            |

**metronome\_\_InvoiceLineItemInvoicingGroupAssoc\_\_c**

| Columns                      | Type     | **Description**                                                                                  |
| ---------------------------- | -------- | ------------------------------------------------------------------------------------------------ |
| `External_Association_ID__c` | text     | The unique identifier for the many to many mapping between invoice line item and invoicing group |
| `Invoice_Line_Item__c`       | lookup   | References the associated line item for the many to many mapping                                 |
| `Invoicing_Group__c`         | lookup   | References the associated invoicing group for the many to many mapping                           |
| `Environment_Type__c`        | picklist | The name of the Metronome environment where this object lives                                    |

**metronome\_\_Invoicing\_Group\_\_c**

| Columns                 | Type     | **Description**                                                                                           |
| ----------------------- | -------- | --------------------------------------------------------------------------------------------------------- |
| `Invoicing_Group_ID__c` | text     | The unique identifier associated with the presentation (invoicing) group key set on the invoice line item |
| `Name__c`               | text     | The key of the presentation (invoicing) group key set on the invoice line item                            |
| `Value__c`              | text     | The value of the presentation (invoicing) group key set on the invoice line item                          |
| `Environment_Type__c`   | picklist | The name of the Metronome environment where this object lives                                             |
