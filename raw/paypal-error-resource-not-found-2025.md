<!-- Source URL: https://docs.paypal.ai/developer/how-to/api/troubleshooting/common-errors/resource-not-found -->
<!-- Fetched: 2026-04-19 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Resource not found

A `RESOURCE_NOT_FOUND` error occurs when the specified resource does not exist. The following issues can cause this error.
If an issue persists or you have further questions, contact [PayPal Support](https://www.paypal.com/us/cshelp/technical).

<Heading level={2} id="invalid_resource_id">
  INVALID\_RESOURCE\_ID
</Heading>

Returns from the Payments v1 or Orders v2 APIs.

| Cause                                                                                                                                                                                                                                                       | Impact                                                                                 | Resolution                                                                                                                                                                                                             |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - You entered an incorrect or malformed resource ID, so the system cannot find the resource. <br /> - You used a resource ID in the API request that does not exist in the system. <br /> - The API caller does not have permission to access the resource. | PayPal stops the payment and does not process the order. This slows down the purchase. | - Check that the resource ID in the API request is correct and exists in the system. Fix any typos or mistakes. <br /> - Make sure the API caller has permission to access the resource. Update permissions if needed. |
