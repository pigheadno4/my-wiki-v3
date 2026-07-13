<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/create-a-trial.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a free trial

export const List = ({marker, children}) => {
  return <>
            <style>
                {`
          .custom-list-from-snippet li {
            list-style-type: var(--marker-style);
            
            padding-left: 0 !important;

          }
          .custom-list-from-snippet li::marker {
            color: rgb(var(--gray-600));

          }
          .custom-list-from-snippet li::before {
            display: none;
          }
        `}
            </style>

            <ul className="custom-list-from-snippet" style={{
    '--marker-style': marker,
    'padding-inline-start': '1.5rem'
  }}>
                {children}
            </ul>
        </>;
};

This use case explores how Metronome's billing platform enables you to effectively manage free trials by tracking usage metrics and duration.

Free trials are a cornerstone of self-service and product-led growth strategies, allowing potential customers to experience the value of a product before committing to a purchase. However, configuring free trials in a usage-based billing model presents unique challenges. While traditional subscription models often rely on simple time-limited trials, usage-based services must carefully balance customer experience with potential costs. The definition of "free" becomes complex when users can potentially accumulate significant charges during their trial period. To solve this, Metronome can help your business offer compelling trial experiences while safeguarding margins and controlling COGS.

This use case walks through two free trial scenarios in Metronome:

* Create a capped free trial on a limited set of products using time-bound credits, alerts, and entitlement overrides.
* Create an uncapped free trial using time-bound contract overrides.

## Create a credit-based free trial​

A credit-based free trial involves allocating a specific amount of usage credits to new users, allowing them to explore your product within predefined limits. Many Metronome customers opt for this approach as a strategic way to balance generous product exposure with controlled risk. This method allows you to offer a substantial trial experience while preventing runaway usage that could impact your bottom line.

In this example, learn how to create a trial for a customer with the following conditions:

* The customer has free access to the platform for up to one week after sign-up.
* The customer trial ends if they reach up to \$100 of usage in the platform.
* The customer trial only includes a certain set of products. For example, the user is allowed to access the *Language models* functionality, but not *Fine tuning* or *Image generation* features.
* When the trial ends (due to time or usage) you receive a real-time notification from Metronome. This allows you to manage a customer's state based on their usage in Metronome—for instance, send them an email that their trial has ended, or disable their account until they purchase further usage.

### Pre-requisites​

Before getting started, make sure you have a [rate card](/guides/get-started/core-concepts/create-manage-rate-cards) and an example [customer](/guides/customers-billing/manage-customers/provision-a-customer) to sign up for the trial.

Our example uses a newly created customer, **AcmeCorp** , with a rate card based on some example **GenAI List Prices**.

### Configure a contract with free trial credits​

To create and configure a contract with free trial credits:

1. On the **Customers** page, click on your customer.

2. Click New contract or plan -> **New contract...**

3. Configure the contract for your customer.
   <List marker="lower-roman">
     * Add a contract name.
     * Select the rate card.
     * Set the contract start and end dates.
     * Set the contract billing frequency.
   </List>
   <Frame>
     <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/docs/pricing-packaging/manage-contracts/create-trial/configure-contract-8eeddc4bffabcb6d4d5e32bdfdf3d02b.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=52906d6c821a8ac8c3a4ad77ab386130" alt="Configure contract" width="1059" height="360" data-path="images/docs/pricing-packaging/manage-contracts/create-trial/configure-contract-8eeddc4bffabcb6d4d5e32bdfdf3d02b.png" />
   </Frame>

4. Click **Add a credit** to configure the trial terms.
   <List marker="lower-roman">
     * Select an existing **Credit product** or create a new fixed product called **Trial credits**. The name of the fixed product selected is the name displayed to your customer.
     * Add an optional description. This is not displayed to your customer. Think of this as useful metadata for users of Metronome, like you.
     * Leave **Applicable products** and **Applicable tags** blank. This configures the credits to track all usage for your customer.
     * Under **Access schedule** , set these terms:

         <List marker="lower-alpha">
           * Set **Starting at** to match your contract start date.

           * Set **Ending before** to be one week after your **Starting at** date. This way, if a customer doesn't use all of their free credits by the end of the trial period, the credits expire and customers pay for subsequent usage.

           * Set the **Amount** to be \$100.

           * If you've included any other commits or credits in your contract, ensure that the **Priority** is set lower than the others.

             > In general, Metronome recommends using whole numbers for priority. For free trials, set a low number like 1 so they clearly take precedence over any other grants. Learn more on how priority is used to [orchestrate burn-down](/guides/pricing-packaging/apply-credits-and-commits/prioritization-rules).

           * When complete, click **Add**.

           <Frame>
             <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/docs/pricing-packaging/manage-contracts/create-trial/set-credit-terms-847c0264a13088bc1ab517648bfd6323.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=bccb7aba9ac4fbef9c3d4429a170e924" alt="Set credit terms" width="1788" height="1912" data-path="images/docs/pricing-packaging/manage-contracts/create-trial/set-credit-terms-847c0264a13088bc1ab517648bfd6323.png" />
           </Frame>
         </List>
   </List>

5. (Optional) To help gate access to certain features while your customer is in the trial phase, set an override on the entitlement state for the particular rate. You can then read from this override to restrict access inside of your product.

   <List marker="lower-roman">
     * Click **+ Add an override**
         <List marker="lower-alpha">
           * Select the product or product tags that you want to disable. In this example, you disable any products with the tags *Fine tuning* and *Images modeled*.
           * Set **Starting at** to match your contract start date.
           * Set **Ending before** to be one week after your **Starting at** date.
           * Set **Entitlement** to **Disable** .
           * When complete, click **Create**.
         </List>

     <Frame>
       <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/docs/pricing-packaging/manage-contracts/create-trial/add-override-5fb455b73cb2850a7677c0f691f2f3f4.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=812a83bd6686952587943bf399f21f3e" alt="Add an override" width="1792" height="1904" data-path="images/docs/pricing-packaging/manage-contracts/create-trial/add-override-5fb455b73cb2850a7677c0f691f2f3f4.png" />
     </Frame>
   </List>

6. Save your changes to create and submit the contract.

If you prefer to use the API, this example payload shows how to create the credit-based free trial contract from the example with one request:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
    "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
    "starting_at": "2024-09-01T00:00:00.000Z",
    "ending_before": "2025-09-01T00:00:00.000Z",
    "name": "AcmeCorp List Prices",
    "credits": [
      {
        "name": "Trial credits",
        "product_id": "609e4cf2-6ea2-4b07-a46c-6596f041b69e",
        "access_schedule": {
          "schedule_items": [
            {
              "amount": 10000,
              "starting_at": "2024-09-01T00:00:00.000Z",
              "ending_before": "2024-09-08T00:00:00.000Z"
            }
          ]
        },
        "description": "Free usage as part of trial",
        "priority": 1
      }
    ],
    "overrides": [
      {
        "starting_at": "2024-09-01T00:00:00.000Z",
        "ending_before": "2024-09-08T00:00:00.000Z",
        "entitled": false,
        "applicable_product_tags": [
          "Fine tuning",
          "Images modeled"
        ]
      }
    ]
  }'
```

After you submit the contract, you can un-gate your customer’s access to your product and observe how they use it.

### Track customer usage​

To track customer usage of your product, use Metronome APIs to create a [customer usage dashboard](/guides/customers-billing/optimize-customer-experience/customer-dashboards-and-reporting). This provides visibility into consumption in real-time and can be exposed directly to your customer.

Once the customer spends the full \$100 of allotted credits, or once the trial week has passed, any subsequent usage is rated and charged in arrears based on your list pricing and billing frequency.

### Create an alert to signal the end of the trial period​

Your system likely needs to know in real-time once a customer’s trial period ends. You can configure alerts in Metronome to notify you when the customer’s credit balance has reached 0, either due to usage or credit expiration. You can use this notification as a signal to disable a customer’s access to your platform, or to re-enable the full suite of features now that their trial has ended.

To configure alerting:

1. Define an alert to notify you upon expiration or full usage of the trial credits.
   <List marker="lower-roman">
     * Go to **Alerts** in the Metronome [app](https://app.metronome.com/alerts) and click **+ Create alert**.
     * Name your alert **Trial Usage - AcmeCorp**.
     * Select the alert type **Contract credit balance**.
     * Set alert threshold to **reaches \$0 USD**.
     * In **Step 3: Select customers** , specify that the alert should only apply to customer **AcmeCorp**.
     * Ensure that you have a [webhook endpoint](/guides/platform-configuration/setup-webhooks) configured to receive the notification from Metronome.
     * When finished, click **Save**.
   </List>

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/docs/pricing-packaging/manage-contracts/create-trial/create-alert-672e2222c683e7ec8697bfebc4109ed8.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=bba37a016a28910c299cff57c0658219" alt="Create an alert" width="1520" height="1196" data-path="images/docs/pricing-packaging/manage-contracts/create-trial/create-alert-672e2222c683e7ec8697bfebc4109ed8.png" />
</Frame>

1. Receive the webhook from Metronome when the credit balance reaches 0.
   <List marker="lower-roman">
     * Ensure that you have a webhook destination set up in Metronome.

     * When a customer's trial expires or their usage cap is reached, you receive a request from Metronome at the webhook destination with this body:

       ```json theme={null}
       {
       "id": "02d8d086-38cb-468e-ab7b-927d16cff708",
       "properties": {
           "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
           "alert_id": "de83d270-f518-4cee-bb15-12f453b303df",
           "threshold": 0,
           "alert_name": "Trial Usage - AcmeCorp",
           "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",
           "remaining_balance": 0,
           "triggered_by": "usage"
       },
       "type": "alerts.low_remaining_contract_credit_and_commit_balance_reached"
       }
       ```

     * Upon receiving this request, take action on the customer within your product. Either send them an email or cut off their access until they upgrade their subscription.
   </List>

## Create an uncapped free trial​

While credit-based trials offer precise control over usage limits, you might prefer to offer uncapped access for a fixed duration to showcase your product's full potential. This approach is particularly effective for products with high perceived value or complex features that require more exploration time. Metronome's billing system also accommodates this strategy, allowing you to set up time-limited trials without usage restrictions while still maintaining visibility into consumption patterns.

In this example, learn how to create a trial for a customer with the following conditions:

* The customer has free access to the platform for up to one week after sign-up.
* The customer can use as much of the product as they want with no capped usage.
* The customer trial only includes a certain set of products. For example, the user is allowed to use the *Language models* functionality, but not *Fine tuning* or *Image generation* features.
* When the trial ends, the customer is automatically transitioned into a paid user.

### Configure a contract with time-bound price overrides​

To create and configure a contract with time-bound price overrides:

1. Follow steps 1 and 2 described in the section **Configure a contract with free trial credits** to create a contract for your customer.
2. Click **+ Add an override** to create your free trial with a time-bound price override.

   <List marker="lower-roman">
     * Select the relevant products or product tags that you want to offer for the free trial. In this example, apply the override to all products with the tag *Language models*.
     * Set **Starting at** to match your contract start date.
     * Set **Ending before** to be one week after your **Starting at** date.
     * Set **Adjustment type** to be **Multiplier** with a value of 0.
     * When finished, click **Create**.

     <Frame>
       <img src="https://mintcdn.com/metronome-b35a6a36/C_lGxKgdkdHt6xoX/images/docs/pricing-packaging/manage-contracts/create-trial/time-bound-override-798f4c6cc2d31e7395a2774594917040.png?fit=max&auto=format&n=C_lGxKgdkdHt6xoX&q=85&s=2aa538ba7180167f5e45eaa2fcf30f9f" alt="Configure a time-bound override" width="898" height="1319" data-path="images/docs/pricing-packaging/manage-contracts/create-trial/time-bound-override-798f4c6cc2d31e7395a2774594917040.png" />
     </Frame>
   </List>
3. (Optional) To restrict access to certain products during the trial period, follow the entitlement override steps from step 5 in the section **Configure contract with free trial credits** .
4. Save your changes to create the contract.

If you prefer to use the API, this example payload shows how to create the time-bound price override contract from the example with one request.

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
    "rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
    "starting_at": "2024-09-01T00:00:00.000Z",
    "ending_before": "2025-09-01T00:00:00.000Z",
    "name": "AcmeCorp List Prices",
    "overrides": [
      {
        "starting_at": "2024-09-01T00:00:00.000Z",
        "ending_before": "2024-09-08T00:00:00.000Z",
        "type": "multiplier",
        "multiplier": 0,
        "applicable_product_tags": [
          "Language models"
        ]
      },
      {
        "starting_at": "2024-09-01T00:00:00.000Z",
        "ending_before": "2024-09-08T00:00:00.000Z",
        "entitled": false,
        "applicable_product_tags": [
          "Fine tuning",
          "Images modeled"
        ]
      }
    ]
  }'
```

At this point, the customer can begin using the platform as part of the free trial. You have visibility into their usage during the trial period. Once the trial completes, subsequent usage automatically charges in arrears at your list prices.
