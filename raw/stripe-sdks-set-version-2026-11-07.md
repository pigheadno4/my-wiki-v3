<!-- Source URL: https://docs.stripe.com/sdks/set-version -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Set a Stripe API version

Follow these guidelines to target a different API version than your SDKs use.

Your default API version gets set the first time you make an API request. If your API requests don’t specify an API version with the `Stripe-Version` header, Stripe uses your account’s default API version, which you can view and upgrade in [Workbench](https://dashboard.stripe.com/workbench/overview).

Sandboxes that copy settings instead inherit the live account’s default API version during setup. See [sandbox API versions](https://docs.stripe.com/sandboxes/dashboard/sandbox-settings.md#api-version).

You can choose a sandbox’s default API version during creation.

When you retrieve an event through the API, the structure of the event that Stripe returns is defined by the account’s default API version at the time the event occurred.

When using our [server-side SDKs](https://docs.stripe.com/sdks.md#server-side-libraries), your API calls to Stripe use the API version that was current when the SDK was released. You can’t target a different version when using a strongly typed language such as Java, Go, or .NET.

### Set the API version

#### Ruby

The [stripe-ruby](https://github.com/stripe/stripe-ruby) library allows you to set the API version globally or on a per-request basis.

If you don’t set an API version, recent versions of stripe-ruby use the API version that was latest at the time your version of stripe-ruby was released. Versions of stripe-ruby before [v9](https://github.com/stripe/stripe-ruby/blob/master/CHANGELOG.md#900---2023-08-16) use your account’s default API version.

To set the API version **globally** with the SDK, assign the version to the `Stripe.api_version` property:

```ruby
require 'stripe'
# Don't put any keys in code. See /keys-best-practices.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>', stripe_version: '2026-10-28.endive')
```

Or set the version per-request:

```ruby
require 'stripe'
# Don't put any keys in code. See /keys-best-practices.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>')
intent = client.v1.payment_intents.retrieve(
  'pi_1DlIVK2eZvKYlo2CW4yj5l2C',
  {
    stripe_version: '2026-10-28.endive',
  },
)
intent.capture
```

> When you override the version globally or per-request, the API response objects are also returned in that version.

#### Python

The [stripe-python](https://github.com/stripe/stripe-python) library allows you to set the API version globally or on a per-request basis.

If you don’t set an API version, recent versions of stripe-python use the API version that was latest at the time your version of stripe-python was released. Versions of stripe-python before [v6](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md#600---2023-08-16) use your account’s default API version.

To set the API version **globally** with the SDK, assign the version to the `stripe.api_version` property:

```python
import stripe
# Don't put any keys in code. See /keys-best-practices.
stripe.api_key = <<YOUR_SECRET_KEY>>
stripe.api_version = '2026-10-28.endive'
```

Or set the version per-request:

```python
import stripe
intent = stripe.PaymentIntent.retrieve(
  "pi_1DlIVK2eZvKYlo2CW4yj5l2C",
  stripe_version="2026-10-28.endive",
)
intent.capture()
```

> When you override the version globally or per-request, the API response objects are also returned in that version.

#### PHP

The [stripe-php](https://github.com/stripe/stripe-php) library allows you to set the API version globally or on a per-request basis.

If you don’t set an API version, recent versions of stripe-php use the API version that was latest at the time your version of stripe-php was released. Versions of stripe-php before [v11](https://github.com/stripe/stripe-php/blob/master/CHANGELOG.md#1100---2023-08-16) use your account’s default API version.

To set the API version **globally** with the SDK, pass the version to the `\Stripe\Stripe::setApiVersion()` method:

```php
$stripe = new \Stripe\StripeClient([
  // Don't put any keys in code. See /keys-best-practices.
  "api_key" => "<<YOUR_SECRET_KEY>>",
  "stripe_version" => "2026-10-28.endive"
]);
```

Or set the version per-request:

```php
$intent = $stripe->paymentIntents->capture(
  'pi_1DlIVK2eZvKYlo2CW4yj5l2C',
  [],
  ['stripe_version' => '2026-10-28.endive']
);
```

> When you override the version globally or per-request, the API response objects are also returned in that version.

#### Java

Because Java is a strongly-typed programming language, the API version used in the SDK is *fixed* and is the latest API version at the time of the SDK release.

We don’t recommend setting a different API version for strongly-typed programming languages, because the response objects might not match the strong types in the SDK and result in request failures. For example, if the API version you’re targeting requires parameters that aren’t present in the SDK types, the request fails.

#### Node

The [stripe-node](https://github.com/stripe/stripe-node) library allows you to set the API version globally or on a per-request basis.

If you don’t set an API version, recent versions of stripe-node will use the API version that was latest at the time your version of stripe-node was released. Versions of stripe-node before [v12](https://github.com/stripe/stripe-node/blob/master/CHANGELOG.md#1200---2023-04-06) use your account’s default API version.

To set the API version **globally** with the SDK, provide the `apiVersion` option:

```javascript
// Don't put any keys in code. See /keys-best-practices.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>', {
  apiVersion: '2026-10-28.endive',
});
```

Or set the version per-request:

```javascript
const intent = await stripe.paymentIntents.retrieve('pi_1DlIVK2eZvKYlo2CW4yj5l2C', {
  apiVersion: '2026-10-28.endive',
});
```

#### Typescript usage

The TypeScript types reflect the latest API version at the time of release. This version is encoded in the [API_VERSION file](https://github.com/stripe/stripe-node/blob/master/API_VERSION).

Import Stripe as a default import and instantiate it as `new Stripe()` with the latest API version.

```javascript
import Stripe from 'stripe';
const stripe = new Stripe('<<YOUR_PUBLISHABLE_KEY>>', {
  apiVersion: '2026-10-28.endive'
});
```

#### Go

Because Go is a strongly-typed programming language, the API version used in the SDK is *fixed* and is the latest API version at the time of the SDK release.

We don’t recommend setting a different API version for strongly-typed programming languages, because the response objects might not match the strong types in the SDK and result in request failures. For example, if the API version you’re targeting requires parameters that aren’t present in the SDK types, the request fails.

#### .NET

Because C# is a strongly-typed programming language, the API version used in the .NET SDK is *fixed* and is the latest API version at the time of the SDK release.

We don’t recommend setting a different API version for strongly-typed programming languages, because the response objects might not match the strong types in the SDK and result in request failures. For example, if the API version you’re targeting requires parameters that aren’t present in the SDK types, the request fails.

#### cURL

```sh
curl https://api.stripe.com/v1/charges \
  -u <<YOUR_SECRET_KEY>>: \
  -H "Stripe-Version: 2026-10-28.endive"
```

#### Stripe CLI

```sh
stripe charges create --stripe-version 2026-10-28.endive
```

### Upgrading your API version

To upgrade your account’s default API version, follow the steps in our [API upgrades guide](https://docs.stripe.com/upgrades.md). Before upgrading, review the [API changelog](https://docs.stripe.com/changelog.md) and [view the API versions used by API requests](https://docs.stripe.com/workbench/guides.md#view-api-versions).

## See also

Stripe SDKs follow their own versioning policy. See the link below to learn more.

- [Stripe versioning and support policies](https://docs.stripe.com/sdks/versioning.md)
