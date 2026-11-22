<!-- Source URL: https://docs.stripe.com/changelog/dahlia/2026-03-25/updates-available-checkout-session-ui-modes -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Updates Checkout Session UI mode enum values

## What’s new

Updates the [ui_mode](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode) parameter for [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md?api-version=2026-03-25.dahlia#checkout_session_object-ui_mode) to use the following clearer, more descriptive enum values:

- `hosted_page`: Displays the Checkout Session on a hosted page that customers get redirected to (replaces `hosted`)
- `embedded_page`: Displays the Checkout Session as an embedded page on your website (replaces `embedded`)
- `elements`: Displays the Checkout Session using embedded components on your website (replaces `custom`)

Also adds the `form` value, which enables you to use the [Checkout form](https://docs.stripe.com/checkout/form/quickstart.md) UI mode. It provides default [Adaptive Pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md) support and improved payment method handling.

## Why is this a breaking change?

Attempting to set a Checkout Session’s `ui_mode` to `hosted`, `embedded`, or `custom` will fail. If your integration uses any of those values, you must update your code to use the new `ui_mode` values.

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `custom`, `embedded`, `hosted` | Removed | [Checkout.Session#create](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode), [Checkout.Session](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode) |
| `elements`, `embedded_page`, `hosted_page` | Added | [Checkout.Session#create](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode), [Checkout.Session](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode) |

#### Ruby

| Values | Change | Enums |
| --- | --- | --- |
| `custom`, `embedded`, `hosted` | Removed | [Checkout::Session::CreateParams](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode), [Checkout::Session](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode) |
| `elements`, `embedded_page`, `hosted_page` | Added | [Checkout::Session::CreateParams](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode), [Checkout::Session](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode) |

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `custom`, `embedded`, `hosted` | Removed | [checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode), [Checkout.Session](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode) |
| `elements`, `embedded_page`, `hosted_page` | Added | [checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode), [Checkout.Session](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode) |

#### PHP

| Values | Change | Enums |
| --- | --- | --- |
| `custom`, `embedded`, `hosted` | Removed | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-03-25.dahlia#checkout_session_object-ui_mode) |
| `elements`, `embedded_page`, `hosted_page` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-03-25.dahlia#checkout_session_object-ui_mode) |

#### Java

| Values | Change | Enums |
| --- | --- | --- |
| `custom`, `embedded`, `hosted` | Removed | [checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-uiMode) |
| `elements`, `embedded_page`, `hosted_page` | Added | [checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-uiMode) |

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `custom`, `embedded`, `hosted` | Removed | [Checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode), [Checkout.Session](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode) |
| `elements`, `embedded_page`, `hosted_page` | Added | [Checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode), [Checkout.Session](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode) |

#### Go

| Values | Change | Enums |
| --- | --- | --- |
| `custom`, `embedded`, `hosted` | Removed | [CheckoutSession](/api/checkout/sessions/object?api-version=2026-03-25.dahlia#checkout_session_object-UIMode) |
| `elements`, `embedded_page`, `hosted_page` | Added | [CheckoutSession](/api/checkout/sessions/object?api-version=2026-03-25.dahlia#checkout_session_object-UIMode) |

#### .NET

| Values | Change | Enums |
| --- | --- | --- |
| `custom`, `embedded`, `hosted` | Removed | [Checkout.SessionCreateOptions](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode), [Checkout.Session](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode) |
| `elements`, `embedded_page`, `hosted_page` | Added | [Checkout.SessionCreateOptions](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode), [Checkout.Session](/api/checkout/sessions/create?api-version=2026-03-25.dahlia#create_checkout_session-ui_mode) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-03-25.dahlia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds pending invoice item interval parameter to create Checkout Sessions](https://docs.stripe.com/changelog/dahlia/2026-03-25/adds-pending-invoice-item-interval-parameter-to-checkout-sessions.md)
- [Adds integration identifier parameter to Checkout Sessions](https://docs.stripe.com/changelog/dahlia/2026-03-25/adds-integration-identifier-parameter-to-checkout-sessions.md)
