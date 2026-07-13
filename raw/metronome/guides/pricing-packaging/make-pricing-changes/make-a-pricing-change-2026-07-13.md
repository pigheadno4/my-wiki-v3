<!-- Source URL: https://docs.metronome.com/guides/pricing-packaging/make-pricing-changes/make-a-pricing-change.md -->
<!-- Fetched: 2026-07-13 -->
<!-- Discovery: llms.txt,sitemap.xml -->

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.metronome.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Launch new pricing​

In traditional billing systems, preparing for a new product or pricing launch can require significant cross-functional coordination and months of work to ensure the change takes place at the right moment for the right customers.

Metronome’s unique model streamlines this process by allowing you to schedule changes for a specified time period, with the ability to flexibly introduce new pricing across all customers, specific cohorts, or to individual customers, depending on your needs.

## Make a pricing change for all customers

Use the rate card to easily introduce new products or schedule rate changes for all customers.

### Schedule a rate change

To introduce a new product or schedule a rate change for all customers through the API, make a POST request to `/contract-pricing/rate-cards/addRates`. This is the same endpoint used to create new rates.

Imagine you are launching a new product to all customers, and you know that you will need to increase prices after a year. The example below showcases how you can use Metronome to easily add a new product and schedule a pricing change in a year, in a single API call. This allows you to make pricing changes across all your customers in advance, so your teams can focus on your customers rather than on billing.

```bash theme={null}
curl https://api.metronome.com/v1/contract-pricing/rate-cards/addRates \  
-H "Authorization: Bearer <TOKEN>" \  
-H "Content-Type: application/json" \  
-d '{  
"rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",  
"rates": [  
  {  
    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",  
    "starting_at": "2024-01-01T00:00:00.000Z",  
    "entitled": true,  
    "rate_type": "FLAT",  
    "price": 100,  
    "pricing_group_values": {  
      "region": "us-west-2",  
      "cloud": "aws"  
    }  
  },  
  {  
    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",  
    "starting_at": "2024-01-01T00:00:00.000Z",  
    "entitled": true,  
    "rate_type": "FLAT",  
    "price": 120,  
    "pricing_group_values": {  
      "region": "us-east-2",  
      "cloud": "aws"  
    }  
  }  
]  
}'
      
```

## Make a pricing change for specific cohorts

Use [packages](https://docs.metronome.com/guides/get-started/core-concepts/packages-overview) to easily introduce new pricing to specific cohorts of new customers. This is especially useful in scenarios where you are rolling out consistently defined pricing packages for new customers and want existing customers to maintain grandfathered prices.

### Grandfather in existing customers

Imagine that instead of launching to all customers, you want to launch your new product for new customers only. Legacy customers can opt in to the new product as needed. To do this, you can add the new product to the rate card but default the entitlement to `false`.

```bash theme={null}
curl https://api.metronome.com/v1/contract-pricing/rate-cards/addRates \  
-H "Authorization: Bearer <TOKEN>" \  
-H "Content-Type: application/json" \  
-d '{  
"rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
"rates": [
  {
    "product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
    "starting_at": "2024-01-01T00:00:00.000Z",
    "entitled": false,
    "rate_type": "FLAT",
    "price": 100,
    "pricing_group_values": {
      "region": "us-west-2",
      "cloud": "aws"
    }
  }
]
}'
      
```

Create a package with the default rates for new customers with the new product entitled:

```bash theme={null}
curl <https://api.metronome.com/v1/packages/create> \
-H "Authorization: Bearer <TOKEN>" \
-H "Content-Type: application/json" \
-d '{
	"name": "2024 Compute Pricing",
	"rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
	"aliases": [{
	  "name": "New Customer Pricing",
	  "starting_at": "2024-01-01T00:00:00.000Z"
	}],
	"net_payment_terms_days": 15,
	"duration": {
	  "value": 12,
	  "unit": "MONTHS"
	},
	"overrides": [{
	  "starting_offset": {
		"value": 0,
		"unit": "MONTHS"
		},
	  "override_specifiers": [{
		"product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
		"pricing_group_values": {
		  "region": "us-west-2",
		  "cloud": "aws"
		}
	  }],
	  "entitled": true
	}]
}'
```

Provision your customers with the '/contracts/create' endpoint:

```bash theme={null}
curl https://api.metronome.com/v1/contracts/create \  
  -H "Authorization: Bearer <TOKEN>" \  
  -H "Content-Type: application/json" \  
  -d '{  
    "customer_id": "aa58107d-162f-407e-9f09-940f16adbb1c",  
    "starting_at": "2025-10-01T00:00:00.000Z",
    "package_alias": "New Customer Pricing"
   }'
```

New customers will be provisioned with the new product while existing customers see no change to their contracted pricing.

<Info>
  **INFO**

  Package rates are applied on top of rate card changes. Customers provisioned on a package with a rate card will still inherit most pricing changes made to the rate card. This enables flexibility in being able to launch pricing changes both at the rate card level for all customers, and at the package level for specific cohorts. The only exception is if the package contains an overwrite override, in which case [standard override rules](https://docs.metronome.com/guides/pricing-packaging/make-pricing-changes/edit-or-override-a-contract#override-types​) apply.
</Info>

### Make pricing changes easy with package aliases

Use package aliases to future-proof pricing changes without updating your provisioning infrastructure. For example, imagine you want to update the price of your new compute product in a year and want to continue grandfathering existing clients to their original price.

To do this, you can create a new package with the same alias:

```bash theme={null}
curl <https://api.metronome.com/v1/packages/create> \\
-H "Authorization: Bearer <TOKEN>" \\
-H "Content-Type: application/json" \\
-d '{
	"name": "2025 Compute Pricing",
	"rate_card_id": "d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
	"aliases": [
	  {
	  "name": "New Customer Pricing",
	  "starting_at": "2025-01-01T00:00:00.000Z"
	  }
	],
	"net_payment_terms_days": 15,
	"duration": {
	  "value": 12,
	  "unit": "MONTHS"
	 },
	"overrides": [
	{
	  "starting_offset": {
	    "value": 0,
		"unit": "MONTHS"
	  },
	  "override_specifiers": [
	  {
		"product_id": "13117714-3f05-48e5-a6e9-a66093f13b4d",
		"pricing_group_values": {
		  "region": "us-west-2",
		  "cloud": "aws"
		}
	  }
	  ],
	  "type": "OVERWRITE",
	  "overwrite_rate": {
		"rate_type": "FLAT",
		"price": 120
	  }
	}
  ]
}'

```

The “New Customer Pricing” package now points to the newly created package with an increase in price from \$1 → \$1.20. The original package will automatically show an alias schedule of “New Customer Pricing” from Jan. 1, 2024 - Jan 1, 2025. New customers will automatically be provisioned on the updated package starting on Jan. 1, 2025 without any need to change the above provisioning flow, since Metronome manages the transition of aliases across packages.

## Make a pricing change for individual customers

If any of your grandfathered customers want to migrate to the new package, you can either end their contract and re-provision their contract with the new pricing, or edit the contract directly to make changes scoped individually. In many cases, individual customers may negotiate specific pricing changes that you will want to reflect separately from your standard rate card or package. Metronome’s contract flexibility allows you to introduce custom overrides to contracts to enable individually-scoped changes. See the following page on [contract editing](https://docs.metronome.com/guides/pricing-packaging/make-pricing-changes/edit-or-override-a-contract) for more details.
