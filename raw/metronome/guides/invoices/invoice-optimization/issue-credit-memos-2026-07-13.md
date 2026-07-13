<!-- Source URL: https://docs.metronome.com/guides/invoices/invoice-optimization/issue-credit-memos.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Issue credit memos

This use case describes how to issue customer credit memos for future and historical billings.

Metronome focuses on the complexities of usage-based rating at scale, in real time. For most Metronome clients, accounts receivable (A/R) functions are handled upstream or downstream from Metronome in an Enterprise Resource Platform (ERP) or Customer Relationship Management (CRM) application. While Metronome provides an invoice that represents the charges and commitment draw-downs related to usage, there's no corresponding credit memo entity that you'd typically see in an ERP. That said, there are a variety of ways to handle adjusting a customer's A/R using Metronome.

This doc explores some scenarios that explain how to adjust a customer's A/R in Metronome or in your A/R system.

## Credit future billings

Credit memos can help resolve customer disputes. Rather than adjusting a past transaction or invoice with a credit memo, you can issue the customer a credit towards future billings. To accomplish this, first decide if you want to offer a customer-level credit or a contract-specific credit. The distinction between the two is that customer-level credits can be used against any existing contract associated with their account instead of a single contract.

### Example: Customer satisfaction credit

Companies give customer satisfaction credits to appease an unsatisfied customer. Typical reasons for this include a poor in-app customer experience, customer complaints, or to credit for downtime and unavailability.

As an example, assume that your application, which provides access to an AI model, was unavailable for an hour during the past billing period. A customer calls to express their frustration with the unavailability, explaining how it led to a loss of revenue and potential customer churn.

To satisfy the customer, you agree to provide a \$100 credit towards future billings.

#### Create a credit

To create a customer-level credit with the Metronome API, use the [Create a Credit](/api-reference/credits-and-commits/create-a-credit) action.

As the customer agreed to receive a \$100 credit for the hour of downtime, create the credit for an *amount* of 10000 (for USD, amounts are in **cents**, so 10000 = \$100.00). Use today's date as the starting date and the date you want the customer to use this credit by as the ending date. To grant them a recurring credit, create a separate `schedule_item` element for each billing period you want to grant them credit for.

<Info>
  USD amounts are always in cents. Other supported currencies use whole units. See [currency denomination](/guides/pricing-packaging/make-pricing-changes/use-currency-custompricingunits#currency-denomination) for details.
</Info>

This call shows an example of the create a credit action:

```json theme={null}
{  
  "customer_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",  
  "name": "My Credit",  
  "priority": 5,  
  "product_id": "f14d6729-6a44-4b13-9908-9387f1918790",  
  "access_schedule": {  
    "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2",  
    "schedule_items": [  
      {  
        "amount": 10000,  
        "starting_at": "2024-09-01T00:00:00.000Z",  
        "ending_before": "2020-09-30T00:00:00.000Z"  
      }  
    ]  
  }  
}
```

If a customer has multiple active credits on their account/contract, set an appropriate `priority`. The priority dictates which credits get burned down first. To learn more, see [Manage credits and commits](/guides/pricing-packaging/apply-credits-and-commits/create-a-pre-paid-commit).

`credit_type_id` is the currency that the credit should be entered in. Find the list of currency IDs in the [Metronome app](https://app.metronome.com/) under **General Settings → Pricing Units.**

<Note>
  **INFO**

  The ID for USD is `2714e483-4ff1-48e4-9e25-ac732e8f24f2`.
</Note>

`product_id` is the ID of the product you want to **show** on the invoice. In the example, you have a product called `Customer Satisfaction Credit`. If you want the credit to apply to specific products on the account instead of any and all products, include those IDs in the `applicable_product_ids` container.

## Credit historical billings

If the customer isn't amenable to a credit against future billings, you have different ways to correct the recorded revenue, outlined in these examples.

### Example: Invoice correction (and reduction in revenue)

You may find yourself in a situation where billings are incorrect. You need to fully reverse the charges AND reduce the revenue associated with those charges. For example, a customer gets set up incorrectly to receive and get billed for products they didn't order. In other situations, the customer becomes completely unsatisfied with the service or product shortly after signing up. They want you to relieve them of any outstanding charges for that service. The end result is to reverse the charges and revenue as if they never occurred in the first place.

In this case, since Metronome is not the management system for customer A/R, create a credit memo directly in the system that manages your A/R. As a result, the adjusted customer invoice and the invoice line amount in Metronome will vary from that in the invoicing system. This discrepancy is acceptable from an audit perspective as the credit memo provides the necessary audit record(s) to justify the difference.

### Example: Customer has incorrect usage (current billing period)

If you notice that a customer has incorrect usage for the current billing period with an invoice in the `DRAFT` state, you can correct this in Metronome by passing in an event that negates the original usage. To do so, pass an event with a *negative* quantity/value that matches the the billable metric of the product you want to credit.

For example, if your billable metric aggregates by a property of `token_count`, where you normally pass positive values, negate the relevant usage by passing a negative value to `token_count`. For example:

```json theme={null}
{  
  "timestamp": "2024-07-30T23:46:24.343000+00:00",  
  "transaction_id": "e88c64c4-7b14-4703-8d5b-df514506cba9",  
  "customer_id": "43ae3f41-480b-412b-9b05-1c4d11169c08",  
  "event_type": "output_tokens",  
  "properties": {  
    "project_id": "Project 1",  
    "token_count": "-50"  
  }  
}
```

### Example: Customer has incorrect usage (previous billing period)

If you notice that a customer has incorrect usage for a previous billing period with an invoice in the `finalized` state, you can grant the customer a credit towards future billings or create a credit memo directly in your customer A/R management system. Metronome doesn't allow the correction/adjustment of usage events for finalized invoices.

### Example: Credit and re-bill

In situations where the *entire* invoice is incorrect, you should credit and re-bill. If your A/R system doesn't support invoice voiding or cancellations, you need to create a credit memo. To do this in Metronome:

1. Negate the incorrect usage following the steps in the previous example.

2. After you negate the original usage, submit the corrected usage records.

3. Void the incorrect invoice with the API ([Void Invoice](/api-reference/invoices/void-an-invoice)) or in the Metronome app. To void with the Metronome app, navigate to the invoice in question, select the overflow menu, and choose **Void Invoice.** Take note of the Invoice ID.

<Frame>
  <img src="https://mintcdn.com/metronome-b35a6a36/TrrblT2KR7zYyGbN/images/docs/Invoices/void-invoice-2327efe6cbdb93c2eb421a9b5d5fa25d.png?fit=max&auto=format&n=TrrblT2KR7zYyGbN&q=85&s=63663fb1d89867cd7764eeb7f5b60c05" alt="Void invoice screenshot" width="3308" height="1660" data-path="images/docs/Invoices/void-invoice-2327efe6cbdb93c2eb421a9b5d5fa25d.png" />
</Frame>

<Warning>
  **VOIDING IN METRONOME DOESN’T VOID DOWNSTREAM**

  Voiding the invoice in Metronome does **not** automatically void invoices in any downstream application. You must perform a similar function in that application manually.
</Warning>

4. After the previous invoice gets voided, regenerate a new invoice with the API [(Regenerate Invoice)](/api-reference/invoices/regenerate-an-invoice) or in the Metronome app. This causes Metronome to recalculate a new invoice based on the associated usage sent. If using the Metronome Stripe integration, this new invoice gets sent to Stripe automatically.

<Note>
  **34 DAY WINDOW**

  Metronome has a limit of **34 Days** where you can submit historical usage. If the credit and re-bill action you want to take is *beyond* 34 days in the past, your only option is to complete the voiding, canceling, and regeneration of invoices directly within your invoicing and customer A/R application.
</Note>

### How Metronome handles refunds

Customer refunds, defined as the act of sending back all or a portion of a customer's payment, are outside the scope of current Metronome functionality. The exact steps to refund a customer depend on your existing technology stack. They typically get handled through your ERP, CRM or directly within your chosen payment processor application.
