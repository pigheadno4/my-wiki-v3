<!-- Source URL: https://docs.paypal.ai/developer/how-to/api/troubleshooting/common-errors/validation-error -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Validation error

You get a validation error when the API request contains invalid, missing, or incorrectly formatted data. This error can return from the [Orders v2](https://developer.paypal.com/docs/api/orders/v2/) or [Payments v1](https://developer.paypal.com/docs/api/payments/v1/) APIs.

If an issue persists or you have further questions, contact [PayPal support](https://www.paypal.com/us/cshelp/technical).

| Cause                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Impact                                                                                                                     | Resolution                                                                                                                                                                                                                                                                         |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - Required fields are missing or contain incorrect values. <br /> - Field values do not match expected data types. <br /> - Currency codes are invalid or the amount formatting is incorrect. <br /> - The request body is not properly formatted as JSON. <br /> - The transaction is blocked based on the account's status or configuration. <br /> - An incorrect or outdated API version is used. Some validation rules may change between versions. | The payment process stops, and the payer cannot complete the purchase. This can result in lost sales if not fixed quickly. | - Check the error details in the API response to find the exact field and issue. <br /> - Ensure all required fields are there and contain valid data in the correct format and type. <br /> - Update the request with correct data and resend it to allow the payment to process. |
