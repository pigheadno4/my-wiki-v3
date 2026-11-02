# POST /payments/{paymentPspReference}/refunds - Refund a captured payment

Refunds a payment that has been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/%7BpaymentPspReference%7D/captures), and returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**REFUND** webhook](https://docs.adyen.com/online-payments/refund#refund-webhook).

You can refund either the full captured amount or a part of the captured amount. You can also perform multiple partial refunds, as long as their sum doesn't exceed the captured amount.

Some payment methods do not support partial refunds. To learn if a payment method supports partial refunds, refer to the payment method page such as [cards](https://docs.adyen.com/payment-methods/cards#supported-cards), [iDEAL](https://docs.adyen.com/payment-methods/ideal), or [Klarna](https://docs.adyen.com/payment-methods/klarna).

If you want to refund a payment but are not sure whether it has been captured, use the [`/payments/{paymentPspReference}/reversals`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/%7BpaymentPspReference%7D/reversals) endpoint instead.

For more information, refer to [Refund](https://docs.adyen.com/online-payments/refund).

## Servers
- https://checkout-test.adyen.com/v72

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| paymentPspReference | string | Yes | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment that you want to refund. |


### Header parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| Idempotency-Key | string | No | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |


### Request body
| Name | Type | Required | Description |
|------|------|----------|-------------|
| amount | object | Yes | The amount that you want to refund. The `currency` must match the currency used in authorisation, the `value` must be smaller than or equal to the authorised amount. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| applicationInfo | object | No | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). |
|   - adyenLibrary | object | No | Adyen-developed software, such as libraries and plugins, used to interact with the Adyen API. For example, Magento plugin, Java API library, etc. |
|     - name | string | No | Name of the field. For example, Name of External Platform. |
|     - version | string | No | Version of the field. For example, Version of External Platform. |
|   - adyenPaymentSource | object | No | Adyen-developed software to get payment details. For example, Checkout SDK, Secured Fields SDK, etc. |
|     - name | string | No | Name of the field. For example, Name of External Platform. |
|     - version | string | No | Version of the field. For example, Version of External Platform. |
|   - externalPlatform | object | No | Third-party developed platform used to initiate payment requests. For example, Magento, Zuora, etc. |
|     - integrator | string | No | External platform integrator. |
|     - name | string | No | Name of the field. For example, Name of External Platform. |
|     - version | string | No | Version of the field. For example, Version of External Platform. |
|   - merchantApplication | object | No | Merchant developed software, such as cashier application, used to interact with the Adyen API. |
|     - name | string | No | Name of the field. For example, Name of External Platform. |
|     - version | string | No | Version of the field. For example, Version of External Platform. |
|   - merchantDevice | object | No | Merchant device information. |
|     - os | string | No | Operating system running on the merchant device. |
|     - osVersion | string | No | Version of the operating system on the merchant device. |
|     - reference | string | No | Merchant device reference. |
|   - shopperInteractionDevice | object | No | Shopper interaction device, such as terminal, mobile device or web browser, to initiate payment requests. |
|     - locale | string | No | Locale on the shopper interaction device. |
|     - os | string | No | Operating system running on the shopper interaction device. |
|     - osVersion | string | No | Version of the operating system on the shopper interaction device. |
| capturePspReference | string | No | This is only available for PayPal refunds. The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the specific capture to refund. |
| enhancedSchemeData | object | No | Enhanced scheme data that may be required for processing the payment. For example, airline information. |
|   - airline | object | No | [Airline enhanced scheme data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/airline/) that may be required for processing the transaction and/or for interchange savings. |
|     - agency | object | No |  |
|     - boardingFee | integer | No | The amount charged for boarding the plane, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - Encoding: Numeric  - minLength: 1 character  - maxLength: 11 characters  - **additionalData key:** `airline.boarding_fee` |
|     - code | string | No | The [IATA](https://www.iata.org/services/pages/codes.aspx) 3-digit accounting code (PAX) that identifies the carrier.  - Format: IATA 3-digit accounting code (PAX)  - Example: KLM = 074  - minLength: 3 characters  - maxLength: 3 characters  - Must not start with a space or be all spaces.  - Must not be all zeros.  - **additionalData key:** `airline.airline_code` |
|     - computerizedReservationSystem | string | No | The [CRS](https://en.wikipedia.org/wiki/Computer_reservation_system) used to make the reservation and purchase the ticket.  - Encoding: ASCII  - minLength: 4 characters  - maxLength: 4 characters  - **additionalData key:** `airline.computerized_reservation_system` |
|     - customerReferenceNumber | string | No | The alphanumeric customer reference number.  - Encoding: ASCII  - maxLength: 20 characters  - If you send more than 20 characters, the customer reference number is truncated  - Must not start with a space or be all spaces.  - **additionalData key:** `airline.customer_reference_number` |
|     - designatorCode | string | No | The [IATA](https://www.iata.org/services/pages/codes.aspx) 2-letter accounting code (PAX) that identifies the carrier.  - Encoding: ASCII  - Example: KLM = KL  - minLength: 2 characters  - maxLength: 2 characters  - Must not start with a space or be all spaces.  - **additionalData key:** `airline.airline_designator_code` |
|     - documentType | string | No | A code that identifies the type of item bought. The description of the code can appear on credit card statements.  - Encoding: ASCII  - Example: Passenger ticket = 01  - minLength: 2 characters  - maxLength: 2 characters  - **additionalData key:** `airline.document_type` |
|     - flightDate | string | No | The flight departure date. Time is optional.  - Format for date only: `yyyy-MM-dd`  - Format for date and time: `yyyy-MM-ddTHH:mm`  - Use local time of departure airport.  - minLength: 10 characters  - maxLength: 16 characters  - **additionalData key:** `airline.flight_date` |
|     - legs | array of object | No |  |
|     - passengerName | string | Yes | The passenger's name, initials, and title.  - Format: last name + first name or initials + title  - Example: *FLYER / MARY MS*  - minLength: 1 character  - maxLength: 20 characters  - If you send more than 20 characters, the name is truncated  - Must not start with a space or be all spaces.  - Must not be all zeros.  - **additionalData key:** `airline.passenger_name` |
|     - passengers | array of object | No |  |
|     - ticket | object | No |  |
|     - travelAgency | object | No |  |
|   - carRental | object | No | [Car rental enhanced scheme data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/car-rental/) that may be required for processing the transaction and/or for interchange savings. |
|     - customerServicePhoneNumber | string | No | The customer service phone number of the car rental company.  - Format: Alphanumeric  - maxLength: 17  - For US and CA numbers must be 10 characters in length  - Must not contain any special characters such as + or -  - Must not start with a space or be all spaces.  - Must not be all zeros.  - **additionalData key:** `carRental.customerServiceTollFreeNumber` |
|     - noShow | boolean | No | Indicates if the customer didn't pick up their rental car.  - **additionalData key:** `carRental.noShowIndicator` |
|     - pickupInfo | object | No |  |
|     - rateType | string | No | Indicates whether the rental rate is daily or weekly.  - **additionalData key:** `carRental.rateIndicator` |
|     - rentalAgreementNumber | string | No | The rental agreement number for the car rental.  - Format: ASCII  - maxLength: 9 characters  - Must not start with a space or be all spaces.  - Must not be all zeros.  - **additionalData key:** `carRental.rentalAgreementNumber` |
|     - rentalClassId | string | No | The classification of the rental car.  - Format: Alphanumeric  - maxLength: 4 characters  - Must not start with a space or be all spaces.  - Must not be all zeros.  - **additionalData key:** `carRental.rentalClassId` |
|     - rentalDays | integer | No | The number of days the car is rented for.  - Format: Numeric  - Max value: 9999  - **additionalData key:** `carRental.daysRented` |
|     - rentalRate | integer | No | Rental rate, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000  - Frequency of the rental rate is specified in the rateType field.  - **additionalData key:** `carRental.rate` |
|     - rentalSurcharges | object | No |  |
|     - renterName | string | Yes | The name of the person renting the car.  - Format: ASCII  - Must not start with a space or be all spaces.  - Must not be all zeros.  - **additionalData key:** `carRental.renterName` |
|     - returnInfo | object | No |  |
|     - taxExempt | boolean | No | Indicates if the goods or services were tax-exempt, or if tax was not collected.  - **additionalData key:** `carRental.taxExemptIndicator` |
|   - healthcare | object | No | Healthcare auto-substantiation amounts for FSA/HSA card transactions. The amounts are used to qualify for reduced interchange rates on healthcare-eligible cards. |
|     - dentalValue | integer | No | The dental amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000 |
|     - otherMedicalValue | integer | No | The other medical amount not covered by the specific categories, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000 |
|     - prescriptionValue | integer | No | The prescription/Rx amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000 |
|     - totalHealthcareValue | integer | Yes | The total healthcare amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000 |
|     - visionPrescriptionValue | integer | No | The vision/optical prescription amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000 |
|   - levelTwoThree | object | No | [Level 2 and Level 3 enhanced scheme data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/l2-l3/) that may be required for processing the transaction and/or for interchange savings. |
|     - customerReferenceNumber | string | No | The reference number to identify the customer and their order.  - Format: ASCII  - Max length: 25 characters  - Must not start with a space or be all spaces.  - Must not be all zeros.  - **additionalData key:** `enhancedSchemeData.customerReference` |
|     - destination | object | No | The destination address information. |
|     - dutyAmount | integer | No | The duty tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000  - **additionalData key:** `enhancedSchemeData.dutyAmount` |
|     - freightAmount | integer | No | The shipping amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000  - **additionalData key:** `enhancedSchemeData.freightAmount` |
|     - itemDetailLines | array of object | No | The list of item detail lines. |
|     - orderDate | string | No | The date of the order.  - Min Length: 10 characters  - Max Length: 10 characters  - Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): yyyy-MM-dd  - **additionalData key:** `enhancedSchemeData.orderDate` |
|     - shipFromPostalCode | string | No | The postal code of the address where the item is shipped from.  - Encoding: ASCII  - Max length: 10 characters  - For the US, it must be in five or nine digits format. For example, 10001 or 10001-0000.  - For Canada, it must be in 6 digits format. For example, M4B 1G5.  - **additionalData key:** `enhancedSchemeData.shipFromPostalCode` |
|     - totalTaxAmount | integer | No | The amount of state or provincial [tax included in the total transaction amount](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/l2-l3#requirements-to-send-level-2-3-esd), in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000  - For L2 data: must not be all zeroes.  - For L3 data: can be zero.  - **additionalData key:** `enhancedSchemeData.totalTaxAmount` |
|   - lodging | object | No | [Lodging enhanced scheme data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/lodging/) that may be required for processing the transaction and/or for interchange savings. |
|     - checkInDate | string | No | The check-in date.  - Min Length: 10 characters  - Max Length: 10 characters  - Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): yyyy-MM-dd  - **additionalData key:** `lodging.checkInDate` |
|     - checkOutDate | string | No | The check-out date.  - Min Length: 10 characters  - Max Length: 10 characters  - Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): yyyy-MM-dd  - **additionalData key:** `lodging.checkOutDate` |
|     - customerServicePhoneNumber | string | No | The toll-free phone number for the lodging customer service.  - Format: Alphanumeric  - For US and CA numbers must be 10 characters in length  - Must not start with a space  - Must not contain any special characters such as + or -  - Must not be all zeros.  - **additionalData key:** `lodging.customerServiceTollFreeNumber` |
|     - fireSafetyCompliance | boolean | No | Indicates that the facility complies with the Hotel and Motel Fire Safety Act of 1990.  - **additionalData key:** `lodging.fireSafetyActIndicator` |
|     - folio | object | No | The folio information for the booking. |
|     - foodBeverageCharges | integer | No | Any charges for food and beverages associated with the booking, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000  - **additionalData key:** `lodging.foodBeverageCharges` |
|     - lodgingChargeType | string | No | The category of lodging charges for the payment.  - **additionalData key:** `lodging.specialProgramCode` |
|     - noShow | boolean | No | Indicates if the customer didn't check in for their booking.  - **additionalData key:** `lodging.noShowIndicator` |
|     - prepaidExpenses | integer | No | The prepaid expenses for the booking, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000  - **additionalData key:** `lodging.prepaidExpenses` |
|     - propertyPhoneNumber | string | No | The lodging property location's phone number.  - Format: Alphanumeric  - Min length: 10 characters  - For US and CA numbers must be 10 characters in length  - Must not start with a space  - Must not contain any special characters such as + or -  - Must not be all zeros.  - **additionalData key:** `lodging.propertyPhoneNumber` |
|     - renterName | string | No | The name of the person renting the room.  - Format: ASCII  - Must not start with a space or be all spaces.  - Must not be all zeros.  - **additionalData key:** `lodging.renterName` |
|     - rooms | array of object | No | The list of rooms booked. |
|     - totalRoomTax | integer | No | The total room tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000  - **additionalData key:** `lodging.totalRoomTax` |
|     - totalTax | integer | No | The total tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000  - **additionalData key:** `lodging.totalTax` |
|   - temporaryServices | object | No | [Temporary services enhanced scheme data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/temporary-services/) that may be required for processing the transaction and/or for interchange savings. |
|     - employeeName | string | No | The name or ID of the person working in a temporary capacity.  - Format: ASCII  - Must not start with a space or be all spaces.  - Must not be all zeros.  - **additionalData key:** `enhancedSchemeData.employeeName` |
|     - endDate | string | No | The billing period end date.  - Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): yyyy-MM-dd  - **additionalData key:** `enhancedSchemeData.tempWeekEnding` |
|     - hourRate | integer | No | The hourly rate for the temporary services, in [minor units](https://docs.adyen.com/development-resources/currency-codes).  - For example, 2000 means USD 20.00.  - Encoding: Numeric  - Max value: 10000000000  - **additionalData key:** `enhancedSchemeData.regularHoursRate` |
|     - hoursWorked | integer | No | The number of hours worked during the billing period.  - Format: Numeric  - **additionalData key:** `enhancedSchemeData.regularHoursWorked` |
|     - jobDescription | string | No | The job description of the person working in a temporary capacity.  - Format: ASCII  - Must not start with a space or be all spaces.  - Must not be all zeros.  - **additionalData key:** `enhancedSchemeData.jobDescription` |
|     - serviceRequestor | string | No | The name of the person requesting the temporary services.  - Format: ASCII  - Must not start with a space or be all spaces.  - Must not be all zeros.  - **additionalData key:** `enhancedSchemeData.requestName` |
|     - startDate | string | No | The billing period start date.  - Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): yyyy-MM-dd  - **additionalData key:** `enhancedSchemeData.tempStartDate` |
| lineItems | array of object | No | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment).  This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. |
|   - amountExcludingTax | integer | No | Item amount excluding the tax, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
|   - amountIncludingTax | integer | No | Item amount including the tax, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
|   - brand | string | No | Brand of the item. |
|   - color | string | No | Color of the item. |
|   - description | string | No | Description of the line item. |
|   - id | string | No | ID of the line item. |
|   - imageUrl | string | No | Link to the picture of the purchased item. |
|   - itemCategory | string | No | Item category, used by the payment methods PayPal and Ratepay. |
|   - manufacturer | string | No | Manufacturer of the item. |
|   - marketplaceSellerId | string | No | Marketplace seller id. |
|   - productUrl | string | No | Link to the purchased item. |
|   - quantity | integer | No | Number of items. |
|   - receiverEmail | string | No | Email associated with the given product in the basket (usually in electronic gift cards). |
|   - returnShippingCompany | string | No | Shipping company handling the return of the item. |
|   - returnTrackingNumber | string | No | Tracking number for the return of the item. |
|   - returnTrackingUri | string | No | Tracking URI for the return of the item. |
|   - riskCategory | string | No | An optional, free-text category for the item to be used in the risk evaluation. When provided, Protect uses this value to evaluate custom risk rules. |
|   - shippingCompany | string | No | Shipping company handling the delivery of the item. |
|   - shippingMethod | string | No | Shipping method used to deliver the item. |
|   - size | string | No | Size of the item. |
|   - sku | string | No | Stock keeping unit. |
|   - taxAmount | integer | No | Tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
|   - taxPercentage | integer | No | Tax percentage, represented as a [basis point](https://en.wikipedia.org/wiki/Basis_point) integer. For example:  - **530** for 5.3% (five point three percent)  - **2100** for 21% (twenty-one percent) |
|   - trackingNumber | string | No | Tracking number for the delivery of the item. |
|   - trackingUri | string | No | Tracking URI for the delivery of the item. |
|   - upc | string | No | Universal Product Code. |
| merchantAccount | string | Yes | The merchant account that is used to process the payment. |
| merchantRefundReason | string | No | The reason for the refund request.  Possible values:  **FRAUD**  **CUSTOMER REQUEST**  **RETURN**  **DUPLICATE**  **OTHER** |
| reference | string | No | Your reference for the refund request. Maximum length: 80 characters. |
| splits | array of object | No | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments for [marketplaces](https://docs.adyen.com/marketplaces/split-payments) or [platforms](https://docs.adyen.com/platforms/online-payments/split-payments/). |
|   - account | string | No | The unique identifier of the account to which the split amount is booked. Required if `type` is **MarketPlace** or **BalanceAccount**.  - [Classic Platforms integration](https://docs.adyen.com/classic-platforms): The [`accountCode`](https://docs.adyen.com/api-explorer/Account/latest/post/updateAccount#request-accountCode) of the account to which the split amount is booked.  - [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model): The [`balanceAccountId`](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/_id_#path-id) of the account to which the split amount is booked. |
|   - amount | object | No | The amount of the split item.  - Required for all split types in the [Classic Platforms integration](https://docs.adyen.com/classic-platforms).  - Required if `type` is **BalanceAccount**, **Commission**, **Surcharge**, **Default**, or **VAT** in your [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model) integration. |
|     - currency | string | No | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). By default, this is the original payment currency. |
|     - value | integer | Yes | The value of the split amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
|   - description | string | No | Your description for the split item. |
|   - reference | string | No | Your unique reference for the part of the payment booked to the specified `account`.  This is required if `type` is **MarketPlace** ([Classic Platforms integration](https://docs.adyen.com/classic-platforms)) or **BalanceAccount** ([Balance Platform](https://docs.adyen.com/adyen-for-platforms-model)).  For the other types, we also recommend providing a **unique** reference so you can reconcile the split and the associated payment in the transaction overview and in the reports. |
|   - type | string | Yes | The part of the payment you want to book to the specified `account`.  Possible values for the [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model):  - **BalanceAccount**: Books part of the payment (specified in `amount`) to the specified `account`.  Transaction fees types that you can book to the specified `account`:  - **AcquiringFees**: The aggregated amount of the interchange and scheme fees.  - **PaymentFee**: The aggregated amount of all transaction fees.  - **AdyenFees**: The aggregated amount of Adyen's commission and markup fees.  - **AdyenCommission**: The transaction fees due to Adyen under [blended rates](https://www.adyen.com/knowledge-hub/interchange-fees-explained).  - **AdyenMarkup**: The transaction fees due to Adyen under [Interchange ++ pricing](https://www.adyen.com/knowledge-hub/interchange-fees-explained).  - **Interchange**: The fees paid to the issuer for each payment made with the card network.  - **SchemeFee**: The fees paid to the card scheme for using their network.  - **Commission**: Your platform's commission on the payment (specified in `amount`), booked to your liable balance account.  - **Remainder**: The amount left over after a currency conversion, booked to the specified `account`.  - **Surcharge**: The payment acceptance fee imposed by the card scheme or debit network provider, paid by your user's customer.  - **TopUp**: Allows you and your users to top up balance accounts using direct debit, card payments, or other payment methods.  - **VAT**: The value-added tax charged on the payment, booked to your platforms liable balance account.  - **Default**: In very specific use cases, allows you to book the specified `amount` to the specified `account`. For more information, contact Adyen support.  Possible values for the [Classic Platforms integration](https://docs.adyen.com/classic-platforms): **Commission**, **Default**, **MarketPlace**, **PaymentFee**, **VAT**. |
| store | string | No | The online store or [physical store](https://docs.adyen.com/point-of-sale/design-your-integration/determine-account-structure/#create-stores) that is processing the refund. This must be the same as the store name configured in your Customer Area.  Otherwise, you get an error and the refund fails. |

## Request examples

### refund
```json
{
  "amount": {
    "currency": "EUR",
    "value": 2500
  },
  "reference": "YOUR_UNIQUE_REFERENCE",
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
}
```
## Responses

### 201 Success
The request has been fulfilled and has resulted in one or more new resources being created.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| amount | object | Yes | The refund amount. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| capturePspReference | string | No | This is only available for PayPal refunds. The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the specific capture to refund. |
| lineItems | array of object | No | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment).  This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. |
|   - amountExcludingTax | integer | No | Item amount excluding the tax, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
|   - amountIncludingTax | integer | No | Item amount including the tax, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
|   - brand | string | No | Brand of the item. |
|   - color | string | No | Color of the item. |
|   - description | string | No | Description of the line item. |
|   - id | string | No | ID of the line item. |
|   - imageUrl | string | No | Link to the picture of the purchased item. |
|   - itemCategory | string | No | Item category, used by the payment methods PayPal and Ratepay. |
|   - manufacturer | string | No | Manufacturer of the item. |
|   - marketplaceSellerId | string | No | Marketplace seller id. |
|   - productUrl | string | No | Link to the purchased item. |
|   - quantity | integer | No | Number of items. |
|   - receiverEmail | string | No | Email associated with the given product in the basket (usually in electronic gift cards). |
|   - returnShippingCompany | string | No | Shipping company handling the return of the item. |
|   - returnTrackingNumber | string | No | Tracking number for the return of the item. |
|   - returnTrackingUri | string | No | Tracking URI for the return of the item. |
|   - riskCategory | string | No | An optional, free-text category for the item to be used in the risk evaluation. When provided, Protect uses this value to evaluate custom risk rules. |
|   - shippingCompany | string | No | Shipping company handling the delivery of the item. |
|   - shippingMethod | string | No | Shipping method used to deliver the item. |
|   - size | string | No | Size of the item. |
|   - sku | string | No | Stock keeping unit. |
|   - taxAmount | integer | No | Tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes/#minor-units). |
|   - taxPercentage | integer | No | Tax percentage, represented as a [basis point](https://en.wikipedia.org/wiki/Basis_point) integer. For example:  - **530** for 5.3% (five point three percent)  - **2100** for 21% (twenty-one percent) |
|   - trackingNumber | string | No | Tracking number for the delivery of the item. |
|   - trackingUri | string | No | Tracking URI for the delivery of the item. |
|   - upc | string | No | Universal Product Code. |
| merchantAccount | string | Yes | The merchant account that is used to process the payment. |
| merchantRefundReason | string | No | Your reason for the refund request. |
| paymentPspReference | string | Yes | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment to refund. |
| pspReference | string | Yes | Adyen's 16-character reference associated with the refund request. |
| reference | string | No | Your reference for the refund request. |
| splits | array of object | No | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments for [marketplaces](https://docs.adyen.com/marketplaces/split-payments) or [platforms](https://docs.adyen.com/platforms/online-payments/split-payments/). |
|   - account | string | No | The unique identifier of the account to which the split amount is booked. Required if `type` is **MarketPlace** or **BalanceAccount**.  - [Classic Platforms integration](https://docs.adyen.com/classic-platforms): The [`accountCode`](https://docs.adyen.com/api-explorer/Account/latest/post/updateAccount#request-accountCode) of the account to which the split amount is booked.  - [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model): The [`balanceAccountId`](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/_id_#path-id) of the account to which the split amount is booked. |
|   - amount | object | No | The amount of the split item.  - Required for all split types in the [Classic Platforms integration](https://docs.adyen.com/classic-platforms).  - Required if `type` is **BalanceAccount**, **Commission**, **Surcharge**, **Default**, or **VAT** in your [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model) integration. |
|     - currency | string | No | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). By default, this is the original payment currency. |
|     - value | integer | Yes | The value of the split amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
|   - description | string | No | Your description for the split item. |
|   - reference | string | No | Your unique reference for the part of the payment booked to the specified `account`.  This is required if `type` is **MarketPlace** ([Classic Platforms integration](https://docs.adyen.com/classic-platforms)) or **BalanceAccount** ([Balance Platform](https://docs.adyen.com/adyen-for-platforms-model)).  For the other types, we also recommend providing a **unique** reference so you can reconcile the split and the associated payment in the transaction overview and in the reports. |
|   - type | string | Yes | The part of the payment you want to book to the specified `account`.  Possible values for the [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model):  - **BalanceAccount**: Books part of the payment (specified in `amount`) to the specified `account`.  Transaction fees types that you can book to the specified `account`:  - **AcquiringFees**: The aggregated amount of the interchange and scheme fees.  - **PaymentFee**: The aggregated amount of all transaction fees.  - **AdyenFees**: The aggregated amount of Adyen's commission and markup fees.  - **AdyenCommission**: The transaction fees due to Adyen under [blended rates](https://www.adyen.com/knowledge-hub/interchange-fees-explained).  - **AdyenMarkup**: The transaction fees due to Adyen under [Interchange ++ pricing](https://www.adyen.com/knowledge-hub/interchange-fees-explained).  - **Interchange**: The fees paid to the issuer for each payment made with the card network.  - **SchemeFee**: The fees paid to the card scheme for using their network.  - **Commission**: Your platform's commission on the payment (specified in `amount`), booked to your liable balance account.  - **Remainder**: The amount left over after a currency conversion, booked to the specified `account`.  - **Surcharge**: The payment acceptance fee imposed by the card scheme or debit network provider, paid by your user's customer.  - **TopUp**: Allows you and your users to top up balance accounts using direct debit, card payments, or other payment methods.  - **VAT**: The value-added tax charged on the payment, booked to your platforms liable balance account.  - **Default**: In very specific use cases, allows you to book the specified `amount` to the specified `account`. For more information, contact Adyen support.  Possible values for the [Classic Platforms integration](https://docs.adyen.com/classic-platforms): **Commission**, **Default**, **MarketPlace**, **PaymentFee**, **VAT**. |
| status | string | Yes | The status of your request. This will always have the value **received**. |
| store | string | No | The online store or [physical store](https://docs.adyen.com/point-of-sale/design-your-integration/determine-account-structure/#create-stores) that is processing the refund. This must be the same as the store name configured in your Customer Area.  Otherwise, you get an error and the refund fails. |


### 400 Client Error
A problem reading or understanding the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| additionalData | object (string) | No | Contains additional information about the payment. Some data fields are included only if you select them first. Go to **Customer Area** > **Developers** > **Additional data**. |
| errorCode | string | No | The error code mapped to the error message. |
| errorType | string | No | The category of the error. |
| message | string | No | A short explanation of the issue. |
| pspReference | string | No | The PSP reference of the payment. |
| status | integer | No | The HTTP response status. |


### 401 Client Error
Authentication required.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| additionalData | object (string) | No | Contains additional information about the payment. Some data fields are included only if you select them first. Go to **Customer Area** > **Developers** > **Additional data**. |
| errorCode | string | No | The error code mapped to the error message. |
| errorType | string | No | The category of the error. |
| message | string | No | A short explanation of the issue. |
| pspReference | string | No | The PSP reference of the payment. |
| status | integer | No | The HTTP response status. |


### 403 Client Error
Insufficient permissions to process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| additionalData | object (string) | No | Contains additional information about the payment. Some data fields are included only if you select them first. Go to **Customer Area** > **Developers** > **Additional data**. |
| errorCode | string | No | The error code mapped to the error message. |
| errorType | string | No | The category of the error. |
| message | string | No | A short explanation of the issue. |
| pspReference | string | No | The PSP reference of the payment. |
| status | integer | No | The HTTP response status. |


### 422 Client Error
A request validation error.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| additionalData | object (string) | No | Contains additional information about the payment. Some data fields are included only if you select them first. Go to **Customer Area** > **Developers** > **Additional data**. |
| errorCode | string | No | The error code mapped to the error message. |
| errorType | string | No | The category of the error. |
| message | string | No | A short explanation of the issue. |
| pspReference | string | No | The PSP reference of the payment. |
| status | integer | No | The HTTP response status. |


### 500 Server Error
The server could not process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| additionalData | object (string) | No | Contains additional information about the payment. Some data fields are included only if you select them first. Go to **Customer Area** > **Developers** > **Additional data**. |
| errorCode | string | No | The error code mapped to the error message. |
| errorType | string | No | The category of the error. |
| message | string | No | A short explanation of the issue. |
| pspReference | string | No | The PSP reference of the payment. |
| status | integer | No | The HTTP response status. |

## Response examples

### 201 Success

**refund**
```json
{
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "paymentPspReference": "993617894903480A",
  "reference": "YOUR_UNIQUE_REFERENCE",
  "pspReference": "993617894906488A",
  "status": "received",
  "amount": {
    "currency": "EUR",
    "value": 2500
  }
}
```

### 400 Client Error

**generic**
```json
{
  "status": 400,
  "errorCode": "702",
  "message": "Unexpected input: \", expected: }",
  "errorType": "validation"
}
```

### 401 Client Error

**generic**
```json
{
  "status": 401,
  "errorCode": "000",
  "message": "HTTP Status Response - Unauthorized",
  "errorType": "security"
}
```

### 403 Client Error

**generic**
```json
{
  "status": 403,
  "errorCode": "901",
  "message": "Invalid Merchant Account",
  "errorType": "security",
  "pspReference": "881611827877203B"
}
```

### 422 Client Error

**generic**
```json
{
  "status": 422,
  "errorCode": "14_030",
  "message": "Return URL is missing.",
  "errorType": "validation",
  "pspReference": "8816118280275544"
}
```

### 500 Server Error

**generic**
```json
{
  "status": 500,
  "errorCode": "905",
  "message": "Payment details are not supported",
  "errorType": "configuration",
  "pspReference": "8516091485743033"
}
```