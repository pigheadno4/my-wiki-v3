<!-- Source URL: https://docs.stripe.com/js/elements/submit -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

## Submit 

`elements.submit()`

Use `elements.submit()` when creating the [Elements object without an Intent](#stripe_elements_no_intent).

Before confirming a payment, call `elements.submit()` to validate the form fields and collect any data required for [wallets](#payment_element_create-options-wallets). You must wait for this function's promise to resolve (using `async` or `.then`) before performing any other operations.

### Example

```title
Submit Elements
```
