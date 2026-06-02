<!-- Source URL: https://docs.paypal.ai/developer/how-to/api/troubleshooting/common-errors/cannot-pay-self -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cannot pay self

Returns from the Payments V1 API.

`CANNOT_PAY_SELF` indicates that the payment request is attempting to send money to the same account initiating the transaction.

| Cause                                                                                                                                                      | Impact                                                                                                                                        | Resolution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - Duplicate reference: The transaction or billing agreement attempts to reference the sender and receiver of payment as the same entity, which is invalid. | - Disrupted transactions: PayPal prevents the transaction from being processed to avoid misuse or fraud stemming from potential self-payment. | - Confirm separation: Ensure that the sender and receiver are different entities. <br /> - Review API request: Ensure you use distinct PayPal account IDs or email addresses for the sender and receiver. <br /> - Implement validation checks: Ensure that your application checks to prevent users from setting up billing agreements with duplicate entities. <br /> - Debug application code: Review and debug the code to correct issues leading to payer and payee using the same account. |
