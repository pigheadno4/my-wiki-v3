# GET /transfers/{id} - Get a transfer

Returns the details of a specified transfer.

## Servers
- https://balanceplatform-api-test.adyen.com/btl/v4

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | Unique identifier of the transfer. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| accountHolder | object | No | The account holder associated with the balance account involved in the transfer. |
|   - description | string | No | The description of the resource. |
|   - id | string | No | The unique identifier of the resource. |
|   - reference | string | No | The reference for the resource. |
| amount | object | Yes | The amount of the transfer. |
|   - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|   - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
| balanceAccount | object | No | Contains information about the balance account involved in the transfer. |
|   - description | string | No | The description of the resource. |
|   - id | string | No | The unique identifier of the resource. |
|   - reference | string | No | The reference for the resource. |
| balancePlatform | string | No | The unique identifier of the balance platform. |
| balances | array of object | No | The list of the latest balance statuses in the transfer. |
|   - balance | integer | No | The amount in the payment's currency that is debited or credited on the balance accounting register. |
|   - currency | string | No | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
|   - received | integer | No | The amount in the payment's currency that is debited or credited on the received accounting register. |
|   - reserved | integer | No | The amount in the payment's currency that is debited or credited on the reserved accounting register. |
| category | string | Yes | The category of the transfer.  Possible values:  **bank**: A transfer involving a [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id) or a bank account.  **card**: A transfer involving a third-party card.  **grants**: A transfer related to a capital grant, such as a disbursement or a repayment.  **interest**: A transfer that settles accrued [interest](https://docs.adyen.com/business-accounts/earn-returns) on a business account.  **internal**: A transfer between [balance accounts](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id) within your platform.  **issuedCard**: A transfer initiated by an Adyen-issued card.  **platformPayment**: Funds movements related to payments that are acquired for your users.  **topUp**: An incoming transfer initiated by your user to top up their balance account. |
| categoryData |  | No | The relevant data according to the transfer category. |
| counterparty | object | No | The other party in the transfer. |
|   - balanceAccountId | string | No | The unique identifier of the counterparty [balance account](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id). |
|   - bankAccount | object | No | Contains information about the counterparty bank account. |
|     - accountHolder | object | Yes | Information about the owner of the bank account. |
|     - accountIdentification |  | Yes | Contains the bank account details. The fields required in this object depend on the country of the bank account and the currency of the transfer. |
|     - storedPaymentMethodId | string | No | The unique token that identifies the stored bank account details of the counterparty for a payout. |
|   - card | object | No | Contains information about the counterparty card. |
|     - cardHolder | object | Yes | Contains information about the cardholder. |
|     - cardIdentification | object | Yes | Contains the identification details of the card. |
|   - merchant | object | No | Contains information about the merchant. |
|     - acquirerId | string | No | The unique identifier of the merchant's acquirer. |
|     - city | string | No | The city where the merchant is located. |
|     - country | string | No | The country where the merchant is located. |
|     - countryCode | string | No | The two-character country code of the merchant's location, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. |
|     - mcc | string | No | The merchant category code. |
|     - merchantId | string | No | The unique identifier of the merchant. |
|     - name | string | No | The name of the merchant's shop or service. |
|     - postalCode | string | No | The postal code of the merchant. |
|   - transferInstrumentId | string | No | The unique identifier of the counterparty [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id). |
| createdAt | string | No | The date and time when the transfer was created, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |
| creationDate | string | No | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |
| description | string | No | Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.  Supported characters: **[a-z] [A-Z] [0-9] / - ?** **: ( ) . , ' + Space**  Supported characters for **regular** and **fast** transfers to a US counterparty: **[a-z] [A-Z] [0-9] & $ % # @** **~ = + - _ ' " ! ?** |
| directDebitInformation | object | No | The details of the direct debit. |
|   - dateOfSignature | string | No | The date when the direct debit mandate was accepted by your user, in [ISO-8601](https://www.w3.org/TR/NOTE-datetime) format. |
|   - dueDate | string | No | The date when the funds are deducted from your user's balance account. |
|   - mandateId | string | No | Your unique identifier for the direct debit mandate. |
|   - sequenceType | string | No | Identifies the direct debit transfer's type. Possible values: **OneOff**, **First**, **Recurring**, **Final**. |
| direction | string | No | The direction of the transfer.  Possible values: **incoming**, **outgoing**. |
| eventId | string | No | The unique identifier of the latest transfer event. Included only when the `category` is **issuedCard**. |
| events | array of object | No | The list of events leading up to the current status of the transfer. |
|   - amount | object | No | The original journal amount. Only applicable for [issuing](https://docs.adyen.com/issuing/) integrations. |
|     - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|     - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
|   - amountAdjustments | array of object | No | The amount adjustments in this transfer. Only applicable for [issuing](https://docs.adyen.com/issuing/) integrations. |
|     - amount | object | No | The adjustment amount. |
|     - amountAdjustmentType | string | No | The type of markup that is applied to an authorised payment.  Possible values: **exchange**, **forexMarkup**, **authHoldReserve**, **atmMarkup**. |
|     - basepoints | integer | No | The basepoints associated with the applied markup. |
|   - arn | string | No | Scheme unique arn identifier useful for tracing captures, chargebacks, refunds, etc. |
|   - bookingDate | string | No | The date when the transfer request was sent. |
|   - estimatedArrivalTime | string | No | The estimated time when the beneficiary should have access to the funds. |
|   - eventsData | array | No | A list of event data. |
|   - externalReason | object | No | The external reason for the transfer status. |
|     - code | string | No | The reason code. |
|     - description | string | No | The description of the reason code. |
|     - namespace | string | No | The namespace for the reason code. |
|   - id | string | No | The unique identifier of the transfer event. |
|   - modification | object | No | The payment modification. Only applicable for [returned internal transfers](https://docs.adyen.com/platforms/internal-fund-transfers/internal-transfer-webhooks/#returned-internal-transfer). |
|     - direction | string | No | The direction of the money movement. |
|     - id | string | No | Our reference for the modification. |
|     - reference | string | No | Your reference for the modification, used internally within your platform. |
|     - status | string | No | The status of the transfer event. |
|     - type | string | No | The type of transfer modification. |
|   - mutations | array of object | No | The list of balance mutations per event. |
|     - balance | integer | No | The amount in the payment's currency that is debited or credited on the balance accounting register. |
|     - currency | string | No | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
|     - received | integer | No | The amount in the payment's currency that is debited or credited on the received accounting register. |
|     - reserved | integer | No | The amount in the payment's currency that is debited or credited on the reserved accounting register. |
|   - originalAmount | object | No | The amount in the original currency. Only applicable for [issuing](https://docs.adyen.com/issuing/) integrations. |
|     - currency | string | Yes | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount. |
|     - value | integer | Yes | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |
|   - reason | string | No | The reason for the transfer status. |
|   - status | string | No | The status of the transfer event. |
|   - tracingData |  | No | Additional tracing information for the tracing event. |
|   - trackingData |  | No | Additional information for the tracking event. |
|   - transactionId | string | No | The id of the transaction that is related to this accounting event. Only sent for events of type **accounting** where the balance changes. |
|   - type | string | No | The type of the transfer event. Possible values: **accounting**, **tracing**, **tracking**. |
|   - updateDate | string | No | The date when the tracking status was updated. |
|   - valueDate | string | No | The date when the funds are expected to be deducted from or credited to the balance account. This date can be in either the past or future. |
| executionDate | object | No | Contains information about the date when the transfer will be processed. The execution date must be within 30 days of the current date.  Until the execution date:  - The `status` of the transfer remains as **received**.  - The `reason` of the transfer remains as **pending**. |
|   - date | string | No | The date when the transfer will be processed. This date must be:  - Within 30 days of the current date.  - In the [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html) **YYYY-MM-DD**. For example: 2025-01-31 |
|   - timezone | string | No | The timezone that applies to the execution date. Use a timezone identifier from the [tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).  Example: **America/Los_Angeles**. Default value: **Europe/Amsterdam**. |
| externalReason | object | No | The external reason of this transfer. |
|   - code | string | No | The reason code. |
|   - description | string | No | The description of the reason code. |
|   - namespace | string | No | The namespace for the reason code. |
| id | string | No | The ID of the resource. |
| networkReason | object | No | Contains information that explains why the transfer was rejected or returned by the network. |
|   - code | string | No | The network-specific reason code. Use `namespace` to identify the code set. |
|   - description | string | No | A human-readable description of the reason code. |
|   - namespace | string | No | The category of codes that `code` belongs to. The `namespace` identifies the payment network and the type of reason  Possible values:  - **ukFpsRejectionCode** : Reason code for a rejected Faster Payments transfer.  - **ukFpsReturnReasonCode** : Reason code for a returned Faster Payments transfer.  - **usAchReturnReasonCode** : Reason code for a returned ACH transfer.  - **usAchCorrectionReasonCode** : Reason code for an ACH Notification of Change.  - **iso8583ResponseCode** : ISO 8583 response code for a card transfer. |
| paymentInstrument | object | No | Contains information about the payment instrument used in the transfer. |
|   - description | string | No | The description of the resource. |
|   - id | string | No | The unique identifier of the resource. |
|   - reference | string | No | The reference for the resource. |
|   - tokenType | string | No | The type of wallet that the network token is associated with. |
| reason | string | No | Additional information about the status of the transfer. |
| reference | string | No | Your reference for the transfer, used internally within your platform. If you don't provide this in the request, Adyen generates a unique reference. |
| referenceForBeneficiary | string | No | A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of funds.  Supported characters: **a-z**, **A-Z**, **0-9**.The maximum length depends on the `category`.  **internal**: 80 characters  **bank**: 35 characters when transferring to an IBAN, 15 characters for others. |
| review | object | No | Contains status updates related to additional reviews. |
|   - numberOfApprovalsRequired | integer | No | Shows the number of [approvals](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers/approve) required to process the transfer. |
|   - scaOnApproval | string | No | Shows the status of the Strong Customer Authentication (SCA) process.  Possible values: **required**, **notApplicable**. |
| sequenceNumber | integer | No | The sequence number of the transfer webhook. The numbers start from 1 and increase with each new webhook for a specific transfer.  The sequence number can help you restore the correct sequence of events even if they arrive out of order. |
| status | string | Yes | The result of the transfer.  For example:  - **received**: an outgoing transfer request is created.  **refused**: the transfer request is rejected by Adyen for one of the following reasons:  - Transfer limit exceeded.  - Transaction rule requirements violated.  - **authorised**: the transfer request is authorized and the funds are reserved.  - **booked**: the funds are deducted from your user's balance account.  - **failed**: the transfer is rejected by the counterparty's bank.  - **returned**: the transfer is returned by the counterparty's bank. |
| tracing |  | No | Contains information for tracing the transfer after Adyen forwards it to the network. |
| tracking |  | No | The latest tracking information of the transfer. |
| transactionRulesResult | object | No | Contains the results of the evaluation of the transaction rules. |
|   - advice | string | No | The advice given by the Risk analysis. |
|   - allHardBlockRulesPassed | boolean | No | Indicates whether the transaction passed the evaluation for all hardblock rules |
|   - score | integer | No | The score of the Risk analysis. |
|   - triggeredTransactionRules | array of object | No | Array containing all the transaction rules that the transaction triggered. |
|     - reason | string | No | An explanation about why the transaction rule failed. |
|     - transactionRule | object | No | Contains information about the transaction rule. |
|     - transactionRuleSource | object | No | Contains information about the resource to which the transaction rule applies. |
| type | string | No | The type of transfer or transaction. For example, **refund**, **payment**, **internalTransfer**, **bankTransfer**. |
| ultimateParty | object | No | The ultimate sender of the funds of the transfer (ultimate debtor). |
|   - address | object | No | The address of the bank account or card owner. |
|     - city | string | No | The name of the city.  Supported characters: **[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ \|** and Space.  Required when the `category` is **card**. |
|     - country | string | Yes | The two-character ISO 3166-1 alpha-2 country code. For example, **US**, **NL**, or **GB**. |
|     - line1 | string | No | The first line of the street address.  Supported characters: **[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ \|** and Space.  Required when the `category` is **card**. |
|     - line2 | string | No | The second line of the street address.  Supported characters: **[a-z] [A-Z] [0-9] . - — / # , ’ ° ( ) : ; [ ] & \ \|** and Space.  Required when the `category` is **card**. |
|     - postalCode | string | No | The postal code. Maximum length:  - 5 digits for an address in the US.  - 10 characters for an address in all other countries.  Supported characters: **[a-z] [A-Z] [0-9]** and Space.  Required for addresses in the US. |
|     - stateOrProvince | string | No | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US or **ON** in Canada.  Required for the US and Canada. |
|   - dateOfBirth | string | No | The date of birth of the individual in [ISO-8601](https://www.w3.org/TR/NOTE-datetime) format. For example, **YYYY-MM-DD**.  Allowed only when `type` is **individual**. |
|   - email | string | No | The email address of the organization or individual. Maximum length: 254 characters. |
|   - firstName | string | No | The first name of the individual.  Supported characters: [a-z] [A-Z] - . / — and space.  This parameter is:  - Allowed only when `type` is **individual**.  - Required when `category` is **card**. |
|   - fullName | string | No | The full name of the entity that owns the bank account or card.  Supported characters: [a-z] [A-Z] [0-9] , . ; : - — / \ + & ! ? @ ( ) " ' and space.  Required when `category` is **bank**. |
|   - fundingInstrument | object | No | Details of the card or token used to fund the pay-in transaction. |
|     - cardIdentification | object | No | Card details used for the transfer, such as the Primary Account Number (PAN) or stored payment method ID. Required if `sourceOfFunds` is **DEBIT**. Provide either:  - `storedPaymentMethodId` or  - `expiryMonth`, `expiryYear`, and `number`. |
|     - networkPaymentReference | string | No | The unique reference assigned by the card network for the pay-in transaction. |
|     - reference | string | No | Your internal reference that identifies this funding instrument. Required if `sourceOfFunds` is **DEPOSIT_ACCOUNT**. |
|     - sourceOfFunds | string | No | Indicates where the funds used for the transfer originated. Possible values are:  - **DEBIT** for card-to-card transfers.  - **DEPOSIT_ACCOUNT** for wallet-to-card transfers. |
|   - lastName | string | No | The last name of the individual.  Supported characters: [a-z] [A-Z] - . / — and space.  This parameter is:  - Allowed only when `type` is **individual**.  - Required when `category` is **card**. |
|   - reference | string | No | A unique reference to identify the party or counterparty involved in the transfer. For example, your client's unique wallet or payee ID.  Required when you include `cardIdentification.storedPaymentMethodId`. |
|   - type | string | No | The type of entity that owns the bank account or card.  Possible values: **individual**, **organization**, or **unknown**.  Required when `category` is **card**. In this case, the value must be **individual**. |
|   - url | string | No | The URL of the organization or individual. Maximum length: 255 characters. |
| updatedAt | string | No | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |


### 401 Client Error
Authentication required.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | Yes | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | Yes | A code that identifies the problem type. |
| instance | string | No | A unique URI that identifies the specific occurrence of the problem. |
| invalidFields | array of object | No | Detailed explanation of each validation error, when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | A unique reference for the request, essentially the same as `pspReference`. |
| response | object | No | JSON response payload. |
| routingDetails | array of object | No | Detailed explanation of each attempt to route the transfer with the priorities from the request. |
|   - detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
|   - errorCode | string | No | A code that identifies the problem type. |
|   - priority | string | No | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with `category` **bank**.  Possible values:  **regular**: For normal, low-value transactions.  **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.  **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.  **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).  **crossBorder**: For high-value transfers to a recipient in a different country.  **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN). |
|   - title | string | No | A short, human-readable summary of the problem type. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |


### 403 Client Error
Insufficient permissions to process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | Yes | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | Yes | A code that identifies the problem type. |
| instance | string | No | A unique URI that identifies the specific occurrence of the problem. |
| invalidFields | array of object | No | Detailed explanation of each validation error, when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | A unique reference for the request, essentially the same as `pspReference`. |
| response | object | No | JSON response payload. |
| routingDetails | array of object | No | Detailed explanation of each attempt to route the transfer with the priorities from the request. |
|   - detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
|   - errorCode | string | No | A code that identifies the problem type. |
|   - priority | string | No | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with `category` **bank**.  Possible values:  **regular**: For normal, low-value transactions.  **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.  **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.  **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).  **crossBorder**: For high-value transfers to a recipient in a different country.  **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN). |
|   - title | string | No | A short, human-readable summary of the problem type. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |


### 422 Client Error
A request validation error.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | Yes | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | Yes | A code that identifies the problem type. |
| instance | string | No | A unique URI that identifies the specific occurrence of the problem. |
| invalidFields | array of object | No | Detailed explanation of each validation error, when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | A unique reference for the request, essentially the same as `pspReference`. |
| response | object | No | JSON response payload. |
| routingDetails | array of object | No | Detailed explanation of each attempt to route the transfer with the priorities from the request. |
|   - detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
|   - errorCode | string | No | A code that identifies the problem type. |
|   - priority | string | No | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with `category` **bank**.  Possible values:  **regular**: For normal, low-value transactions.  **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.  **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.  **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).  **crossBorder**: For high-value transfers to a recipient in a different country.  **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN). |
|   - title | string | No | A short, human-readable summary of the problem type. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |


### 500 Server Error
The server could not process the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| detail | string | Yes | A human-readable explanation specific to this occurrence of the problem. |
| errorCode | string | Yes | A code that identifies the problem type. |
| instance | string | No | A unique URI that identifies the specific occurrence of the problem. |
| invalidFields | array of object | No | Detailed explanation of each validation error, when applicable. |
|   - message | string | Yes | Description of the validation error. |
|   - name | string | Yes | The field that has an invalid value. |
|   - value | string | Yes | The invalid value. |
| requestId | string | No | A unique reference for the request, essentially the same as `pspReference`. |
| response | object | No | JSON response payload. |
| routingDetails | array of object | No | Detailed explanation of each attempt to route the transfer with the priorities from the request. |
|   - detail | string | No | A human-readable explanation specific to this occurrence of the problem. |
|   - errorCode | string | No | A code that identifies the problem type. |
|   - priority | string | No | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with `category` **bank**.  Possible values:  **regular**: For normal, low-value transactions.  **fast**: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.  **wire**: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.  **instant**: For instant funds transfers within the United States and in [SEPA locations](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).  **crossBorder**: For high-value transfers to a recipient in a different country.  **internal**: For transfers to an Adyen-issued business bank account (by bank account number/IBAN). |
|   - title | string | No | A short, human-readable summary of the problem type. |
| status | integer | Yes | The HTTP status code. |
| title | string | Yes | A short, human-readable summary of the problem type. |
| type | string | Yes | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. |

## Response examples

### 200 Success

**success**
```json
{
  "balancePlatform": "YOUR_BALANCE_PLATFORM",
  "creationDate": "2021-05-03T15:20:06+02:00",
  "id": "1W1UG35QQEBJLHZ8",
  "accountHolder": {
    "description": "S. Eller - Staff 123",
    "id": "AH32272223222B5CZW6QZ2V34"
  },
  "amount": {
    "currency": "EUR",
    "value": 5400
  },
  "balanceAccount": {
    "description": "My Balance Account",
    "id": "BA3227C223222B5B9SCR82TMV"
  },
  "category": "internal",
  "categoryData": {
    "type": "internal"
  },
  "counterparty": {
    "balanceAccountId": "BA00000000000000000000001"
  },
  "description": "Your description",
  "direction": "outgoing",
  "reason": "approved",
  "reference": "312M2060T6S4UOIF",
  "status": "booked",
  "balances": [
    {
      "balance": -5400,
      "currency": "EUR",
      "received": 0,
      "reserved": 0
    }
  ],
  "events": [
    {
      "bookingDate": "2021-05-03T14:53:39+01:00",
      "id": "EVJN4233Q22322375JQ72V55G92ZXF",
      "mutations": [
        {
          "currency": "EUR",
          "received": -5400
        }
      ],
      "status": "received",
      "type": "accounting",
      "valueDate": "2021-05-03T14:53:39+01:00"
    },
    {
      "bookingDate": "2021-05-03T14:53:39+01:00",
      "id": "EVJN4233Q22322375JQ72V55GB4TPV",
      "mutations": [
        {
          "currency": "EUR",
          "received": 5400,
          "reserved": -5400
        }
      ],
      "status": "authorised",
      "type": "accounting",
      "valueDate": "2021-05-03T14:53:39+01:00"
    },
    {
      "bookingDate": "2021-05-03T14:53:39+01:00",
      "id": "EVJN4233Q22322375JQ72V55GD53HZ",
      "mutations": [
        {
          "balance": -5400,
          "currency": "EUR",
          "received": 0,
          "reserved": 5400
        }
      ],
      "status": "booked",
      "transactionId": "EVJN4233Q22322375JQ72V55GD53HZEUR",
      "type": "accounting",
      "valueDate": "2021-05-03T14:53:39+01:00"
    }
  ],
  "sequenceNumber": 3,
  "type": "internalTransfer"
}
```