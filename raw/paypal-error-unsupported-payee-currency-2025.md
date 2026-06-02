<!-- Source URL: https://docs.paypal.ai/developer/how-to/api/troubleshooting/common-errors/unsupported-payee-currency -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Unsupported payee currency

Returns from the Payments V1 API.

`UNSUPPORTED_PAYEE_CURRENCY` indicates that the payee's PayPal account does not support the currency specified in the transaction, and the payee cannot accept payments.

| Cause                                                                                                                                                                                                                                                                                                                                                                                 | Impact                                                                                                                                                                                                      | Resolution                                                                                                                                                                                                                                                                                                                           |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - Account restrictions: The payee account restrictions permit only transactions in certain currencies. <br /> - Disabled currency: The payee did not enable the specified currency in their account settings. <br /> - Region limitations: Certain regions do not make available specific currencies for the merchant account, resulting in a currency mismatch during a transaction. | - Failed payment attempt: The transaction cannot be completed using the specified currency. <br /> - Customer dissatisfaction: Unprocessable payments can cause inconvenience for both the payer and payee. | - Verify supported currencies: Change the currency code in your API request to a [supported currency](https://developer.paypal.com/docs/reports/reference/paypal-supported-currencies/) for the payee account. <br /> - Contact payee: Communicate with the payee to confirm their account settings and the currencies they enabled. |
