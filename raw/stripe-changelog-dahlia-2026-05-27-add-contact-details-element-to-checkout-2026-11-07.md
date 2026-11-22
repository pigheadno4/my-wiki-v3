<!-- Source URL: https://docs.stripe.com/changelog/dahlia/2026-05-27/add-contact-details-element-to-checkout -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Adds the ability to collect email in Checkout Sessions with Contact Details Element

## What’s new

You can now use the [Contact Details Element](https://docs.stripe.com/payments/elements/contact-details-element.md) when integrating with [Elements](https://docs.stripe.com/payments/elements.md) and the [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md?api-version=2026-05-27.dahlia) API. The Contact Details Element collects and validates your customer’s email address, and helps them sign in to Link.

## Impact

Previously, collecting a customer’s email with the Checkout Sessions API required building and validating your own email input using [updateEmail](https://docs.stripe.com/js/custom_checkout/update_email). You can now use the Contact Details Element to handle email collection and validation without building your own form. The element also helps customers sign in to Link for faster checkout.

To use it, mount the element in your HTML or render the React component. See [Build a checkout page with the Checkout Sessions API](https://docs.stripe.com/payments/quickstart.md) to learn more.

## Related changes

- [Renames Link Authentication Element to Contact Details Element](https://docs.stripe.com/changelog/dahlia/2026-05-27/link-authentication-element-rename.md)
