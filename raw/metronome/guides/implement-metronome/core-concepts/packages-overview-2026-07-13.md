<!-- Source URL: https://docs.metronome.com/guides/implement-metronome/core-concepts/packages-overview.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create packages

A package is a reusable, time-relative set of contract terms. Packages enable you to maintain only one rate card while supporting a variety of pricing plans to optimize for simplicity and flexibility.

Define a package in Metronome to encode a standardized set of contract terms once and then provision many customers against that same package, making it easy to manage cohorts with identical contract structures. Use packages to model standard pay-as-you-go motions with Good/Better/Best plans (see the [Pay as you go guide](https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/pay-as-you-go)) to provision customers in a consistent and scalable way.

## Prerequisites

Before creating a package, you must have:

* Your [**usage events**](https://docs.metronome.com/guides/events/design-usage-events) connected to Metronome
* A [**billable metric**](https://docs.metronome.com/guides/get-started/core-concepts/create-billable-metrics)
* A [**product**](https://docs.metronome.com/guides/get-started/core-concepts/create-products-contracts)
* A [**rate card**](https://docs.metronome.com/guides/get-started/core-concepts/create-manage-rate-cards)

## Create a package

Create packages using the `/packages/create` endpoint. Package creation is nearly identical to [contract creation](https://docs.metronome.com/guides/get-started/core-concepts/provision-contract), with the following exceptions:

* **Packages are customer agnostic.** Do not pass a `customer_id` or a customer billing configuration when creating a package
* **Packages are time-relative.** Set `starting_at_offset` and `duration` for relative lengths instead of `starting_at` and `ending_before` dates.
* **Packages support aliases.** Similar to rate card aliases, packages support aliases that aid in programmatically managing new package rollouts.

Consider an example AI company, Gnome AI, with a Starter Plan that includes:

* a \$10 recurring sign-up credit applied to input and output tokens for the first 3 months
* a \$10 monthly subscription fee
* Standard input and output token rates

To create this package in the Metronome app, go to Offering → Packages → Add package.

1. Give the package an internally meaningful **Name** (for example, *Starter Plan - October 2025*)
2. Add an optional **Description** (for example, *Standard Starter Plan pricing as of October 1, 2025*)
3. Optionally **Add aliases.** Aliases can be used in place of Metronome-generated package ID when provisioning contracts via API. [Read more](https://docs.metronome.com/guides/pricing-packaging/make-pricing-changes/make-a-pricing-change) about how aliases help you launch new pricing while maintaining your integration infrastructure.
4. **Set billing terms.** Set the default duration of the contract, net payment terms, and billing provider.
5. **Choose a rate card.** This will determine the rates used for each package.
6. **Add terms**. Add commits, credits, subscriptions, threshold billing, or scheduled charges to the package. All contracts provisioned with a package will contain the defined terms. For the above Starter Plan, add a recurring sign-up credit and monthly subscription fee.
7. **Add overrides.** Add overrides to any rate associated with the selected rate card. You can set overrides with relative or absolute dates. All contracts provisioned with a package will contain the defined overrides.
8. Review the rate card and click **Save** to create the completed card.

To create this package using the API, execute the following call:

```json theme={null}
curl https://api.metronome.com/v1/packages/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
	  "name": "Starter Plan (as of Oct 2025)",
	  "rate_card_alias": "Tokens rate card",
	  "aliases": [{
	    "name": "Starter Plan",
		"starting_at": "2025-10-01T00:00:00.000Z"
	  }],
	  "net_payment_terms_days": 15,
	  "duration": {
		"value": 12,
		"unit": "MONTHS"
	  },
	  "recurring_credits": [{
	    "product_id": "5cd945a1-7a70-4875-b2b3-f9e3b28c647c",
		"access_amount": {
		  "unit_price": 1000,
		  "credit_type_id": "2714e483-4ff1-48e4-9e25-ac732e8f24f2"
		},
		"priority": 1,
		"commit_duration": {
		  "value": 1,
		  "unit": "PERIODS"
		},
		"starting_at_offset": {
		  "value": 0,
		  "unit": "MONTHS"
		},
		"duration": {
		  "value": 3,
		  "unit": "MONTHS"
		}
	  }],
	  "subscriptions":[{
	    "collection_schedule": "advance",
        "initial_quantity": 1,
        "proration": {
          "invoice_behavior": "BILL_IMMEDIATELY",
          "is_prorated": true
        },
        "subscription_rate": {
          "billing_frequency": "monthly",
          "product_id": "76f29162-7f5c-4ee6-89ed-ebbd592d767e"
        },
	}]
  }'
```

<Info>
  **INFO**

  Use `starting_at_offset` on package terms to define `starting_at`
  relative to contract start date and `duration` to define `ending_before` relative
  to the `starting_at_offset`. For terms with point-in-time dates without a
  duration, use `date_offset`
</Info>

## Provision customers with a package

Provision a customer using the `/contracts/create` endpoint.

To provision a customer with the example Starter Plan package, execute the following API call:

```json theme={null}
curl https://api.metronome.com/v1/contracts/create \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "aa58107d-162f-407e-9f09-940f16adbb1c",
    "starting_at": "2025-10-01T00:00:00.000Z",
    "package_alias": "Starter Plan"
   }'
```

The customer is now provisioned with a Starter Plan contract beginning October 1, 2025, with a \$10 monthly subscription for the contract duration and a \$10 recurring credit that ends on Jan 1, 2026. Contracts provisioned with a package have an attached package ID that is viewable in the Metronome app, data export, and API.

<Warning>
  **STANDARD PACKAGES ONLY**

  Metronome currently only accepts `package_id` (or `package_alias`) and `transition` when provisioning a customer with a package. Passing in any additional terms to the createContract call will return a 400 error when used in conjunction with packages.
</Warning>

## Update package pricing

Packages currently cannot be edited after creation. To introduce a new package version, create a new package and set the alias schedule.

For example, Gnome AI decides to update their Starter Plan packaging so that new customers no longer receive the /\$10 sign-up credit as of Feb 1, 2026.

To model this scenario in Metronome, create a new package with the same *Starter Plan* alias:

```json theme={null}
curl https://api.metronome.com/v1/packages/create \  
  -H "Authorization: Bearer <TOKEN>" \  
  -H "Content-Type: application/json" \  
  -d '{ 
		"name": "Starter Plan - Feb 2025",
		"rate_card_alias": "Tokens rate card",
		"aliases": [{
		  "name": "Starter Plan",
		  "starting_at": "2026-02-01T00:00:00.000Z"
		}],
		"net_payment_terms_days": 15,
		"duration": {
		  "value": 12,
		  "unit": "MONTHS"
		},
		"subscriptions":[{
		  "collection_schedule": "advance",  
	      "initial_quantity": 1,  
	      "proration": {  
	        "invoice_behavior": "BILL_IMMEDIATELY",  
	        "is_prorated": true  
	      },  
	      "subscription_rate": {  
	        "billing_frequency": "monthly",  
	        "product_id": "76f29162-7f5c-4ee6-89ed-ebbd592d767e"  
	      }  
		}]
  	}'
```

Since Gnome AI is already provisioning customers using the *Starter Plan* alias, all new clients signing up after February 1, 2026 at midnight UTC will automatically be provisioned on the new package without needing to make any changes to existing logic.

## View and manage packages

To view existing packages, go to Offering → Packages in the Metronome app or call `/packages/list` in the API.

For easier cohort management, view customers associated with a given package in the Metronome app or call `/packages/listContractsonPackage` in the API.

<Warning>
  **PACKAGES CANNOT BE EDITED**

  Create a new package and provision a customer with the new package or edit the underlying contract using editContract.
</Warning>

## Set custom fields on package terms

When creating a package, users can set [custom fields](https://docs.metronome.com/api-reference/custom-fields#custom-fields) on package terms. Custom fields on package terms will be passed down to associated contracts. Package custom fields cannot be updated after set, but custom fields set by packages at the contract-level can be updated using `/customFields/setValues`.

Currently, Metronome supports custom fields for: `package_commit`, `package_credit`, `package_scheduled_charge`, and `package_subscription`.
