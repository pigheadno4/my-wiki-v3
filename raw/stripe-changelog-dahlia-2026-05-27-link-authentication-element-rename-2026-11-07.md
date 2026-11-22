<!-- Source URL: https://docs.stripe.com/changelog/dahlia/2026-05-27/link-authentication-element-rename -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Renames Link Authentication Element to Contact Details Element

## What’s new

You can now use the [Contact Details Element](https://docs.stripe.com/payments/elements/contact-details-element.md) in Stripe Elements for the same contact collection and Link authentication flows. Previously, this element was called the Link Authentication Element. You don’t need to change existing integrations—we still support `elements.create('linkAuthentication')` alongside `elements.create('contactDetails')`.

## Impact

See [Contact Details Element](https://docs.stripe.com/payments/elements/contact-details-element.md) to implement or update your integration. The existing behavior remains unchanged, and you can continue using `linkAuthentication` or update your integration to use `contactDetails` when you create the element.

## Related changes

- [Adds the ability to collect email in Checkout Sessions with Contact Details Element](https://docs.stripe.com/changelog/dahlia/2026-05-27/add-contact-details-element-to-checkout.md)
