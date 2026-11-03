# GET /legalEntities/{id} - Get a legal entity

Returns a legal entity.

Requests to this endpoint are subject to rate limits:

Live environments: 700 requests per 5 seconds.

Test environments: 200 requests per 5 seconds.

Failed requests are subject to a limit of 5 failures per 10 seconds.

## Servers
- https://kyc-test.adyen.com/lem/v4

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the legal entity. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| capabilities | object (object) | No | Contains key-value pairs that specify the actions that the legal entity can do in your platform.The key is a capability required for your integration. For example, **issueCard** for Issuing. The value is an object containing the settings for the capability. |
|   - allowed | boolean | No | Indicates whether the capability is allowed. Adyen sets this to **true** if the verification is successful. |
|   - allowedLevel | string | No | The capability level that is allowed for the legal entity.  Possible values: **notApplicable**, **low**, **medium**, **high**. |
|   - allowedSettings | object | No | The settings that are allowed for the legal entity. |
|     - amountPerIndustry | object (object) | No | The maximum amount a card holder can spend per industry. |
|     - authorizedCardUsers | boolean | No | The number of card holders who can use the card. |
|     - fundingSource | array of string | No | The funding source of the card, for example **debit**. |
|     - interval | string | No | The period when the rule conditions apply. |
|     - maxAmount | object | No | The maximum amount a card holder can withdraw per day. |
|   - requested | boolean | No | Indicates whether the capability is requested. To check whether the legal entity is permitted to use the capability, refer to the `allowed` field. |
|   - requestedLevel | string | No | The requested level of the capability. Some capabilities, such as those used in [card issuing](https://docs.adyen.com/issuing/add-capabilities#capability-levels), have different levels. Levels increase the capability, but also require additional checks and increased monitoring.  Possible values: **notApplicable**, **low**, **medium**, **high**. |
|   - requestedSettings | object | No | The settings that are requested for the legal entity. |
|     - amountPerIndustry | object (object) | No | The maximum amount a card holder can spend per industry. |
|     - authorizedCardUsers | boolean | No | The number of card holders who can use the card. |
|     - fundingSource | array of string | No | The funding source of the card, for example **debit**. |
|     - interval | string | No | The period when the rule conditions apply. |
|     - maxAmount | object | No | The maximum amount a card holder can withdraw per day. |
|   - transferInstruments | array of object | No | The capability status of transfer instruments associated with the legal entity. |
|     - allowed | boolean | No | Indicates whether the capability is allowed for the supporting entity.  If a capability is allowed for a supporting entity but not for the parent legal entity, this means the legal entity has other supporting entities that failed verification.  **You can use the allowed supporting entity** regardless of the verification status of other supporting entities. |
|     - id | string | No | Supporting entity reference |
|     - requested | boolean | No | Indicates whether the supporting entity capability is requested. |
|     - verificationStatus | string | No | The status of the verification checks for the capability of the supporting entity.  Possible values:  **pending**: Adyen is running the verification.  **invalid**: The verification failed. Check if the `errors` array contains more information.  **valid**: The verification has been successfully completed.  **rejected**: Adyen has verified the information, but found reasons to not allow the capability. |
|   - verificationStatus | string | No | The status of the verification checks for the capability.  Possible values:  **pending**: Adyen is running the verification.  **invalid**: The verification failed. Check if the `errors` array contains more information.  **valid**: The verification has been successfully completed.  **rejected**: Adyen has verified the information, but found reasons to not allow the capability. |
| documentDetails | array of object | No | List of documents uploaded for the legal entity. |
|   - active | boolean | No | Identifies whether the document is active and used for checks. |
|   - description | string | No | Your description for the document. |
|   - fileName | string | No | Document name. |
|   - id | string | No | The unique identifier of the resource. |
|   - modificationDate | string | No | The modification date of the document. |
|   - pages | array of object | No | List of document pages |
|     - pageName | string | No |  |
|     - pageNumber | integer | No |  |
|     - type | string | No |  |
|   - type | string | No | Type of document, used when providing an ID number or uploading a document. |
| documents | array of object | No | List of documents uploaded for the legal entity. |
|   - id | string | No | The unique identifier of the resource. |
| entityAssociations | array of object | No | List of legal entities associated with the current legal entity. For example, ultimate beneficial owners associated with an organization through ownership or control, or as signatories. |
|   - associatorId | string | No | The unique identifier of another legal entity with which the `legalEntityId` is associated. When the `legalEntityId` is associated to legal entities other than the current one, the response returns all the associations. |
|   - entityType | string | No | The legal entity type of associated legal entity.  For example, **organization**, **soleProprietorship** or **individual**. |
|   - jobTitle | string | No | The individual's job title if the `type` is **uboThroughControl** or **signatory**. |
|   - legalEntityId | string | Yes | The unique identifier of the associated [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id). |
|   - name | string | No | The name of the associated [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id).  - For **individual**, `name.firstName` and `name.lastName`.  - For **organization**, `legalName`.  - For **soleProprietorship**, `name`. |
|   - nominee | boolean | No | Default value: **false** Set to **true** if the entity association `type` **director**, **secondaryPartner** or **shareholder** is also a nominee. Only applicable to New Zealand. |
|   - relationship | string | No | The individual's relationship to a legal representative if the `type` is **legalRepresentative**. Possible values: **parent**, **guardian**. |
|   - settlorExemptionReason | array of string | No | Defines the KYC exemption reason for a settlor associated with a trust. Only applicable to trusts in Australia.  For example, **professionalServiceProvider**, **deceased**, or **contributionBelowThreshold**. |
|   - type | string | Yes | Defines the relationship of the legal entity to the current legal entity.  Possible value for individuals: **legalRepresentative**.  Possible values for organizations: **director**, **signatory**, **trustOwnership**, **uboThroughOwnership**, **uboThroughControl**, **ultimateParentCompany**, or **immediateParentCompany**.  Possible values for sole proprietorships: **soleProprietorship**.  Possible value for trusts: **trust**.  Possible values for trust members: **definedBeneficiary**, **protector**, **secondaryTrustee**, **settlor**, **uboThroughControl**, or **uboThroughOwnership**.  Possible value for unincorporated partnership: **unincorporatedPartnership**.  Possible values for unincorporated partnership members: **secondaryPartner**, **uboThroughControl**, **uboThroughOwnership** |
| id | string | Yes | The unique identifier of the legal entity. |
| individual | object | No | Information about the individual. Required if `type` is **individual**. |
|   - birthData | object | No | The individual's birth information. |
|     - dateOfBirth | string | No | The individual's date of birth, in YYYY-MM-DD format. |
|   - email | string | No | The email address of the legal entity. |
|   - identificationData | object | No | Information about the individual's identification document. |
|     - cardNumber | string | No | The card number of the document that was issued (AU only). |
|     - expiryDate | string | No | The expiry date of the document, in YYYY-MM-DD format. |
|     - issuerCountry | string | No | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the document was issued. For example, **US**. |
|     - issuerState | string | No | The state or province where the document was issued (AU only). |
|     - nationalIdExempt | boolean | No | Applies only to individuals in the US. Set to **true** if the individual does not have an SSN. To verify their identity, Adyen will require them to upload an ID document. |
|     - number | string | No | The number in the document. |
|     - type | string | Yes | Type of identity data. For individuals, the following types are supported. See our [onboarding guide](https://docs.adyen.com/platforms/onboard-users/onboarding-steps/?onboarding_type=custom) for other supported countries.  Australia: **driversLicense**, **passport**  Hong Kong: **driversLicense**, **nationalIdNumber**, **passport**  New Zealand: **driversLicense**, **passport**  Singapore: **driversLicense**, **nationalIdNumber**, **passport**  All other supported countries: **nationalIdNumber** |
|   - name | object | Yes | The individual's name. The combined length of `firstName` and `lastName` must be at least 3 characters.  Only **-**, **—**, **.**, **/** are allowed as special characters.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - firstName | string | Yes | The individual's first name. Must not be blank.  The combined length of `firstName` and `lastName` must be at least 3 characters. For example, a `firstName` of N and `lastName` of Ha is accepted.  Only the following special characters are allowed: **-**, **—**, **.**, **/**. Accents and non-Latin scripts are allowed.  The field cannot contain emojis, only one repeated character (unless two characters long), only symbols, only numbers, only spaces, or **fictitious names** such as **John Doe** or **N/A**.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - infix | string | No | The infix in the individual's name, if any.  Only the following special characters are allowed: **-**, **—**, **.**, **/**. Accents and non-Latin scripts are allowed.  The field cannot contain emojis, only symbols, only numbers, or only spaces.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - lastName | string | Yes | The individual's last name. Must not be blank.  The combined length of `firstName` and `lastName` must be at least 3 characters.  Only the following special characters are allowed: **-**, **—**, **.**, **/**. Accents and non-Latin scripts are allowed.  The field cannot contain emojis, only one repeated character (unless two characters long), only symbols, only numbers, only spaces, or **fictitious names** such as **John Doe** or **N/A**.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|   - nationality | string | No | The individual's nationality. |
|   - phone | object | No | The phone number of the legal entity. |
|     - number | string | Yes | The full phone number, including the country code. For example, **+3112345678**. |
|     - phoneCountryCode | string | No | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code prefix of the phone number. For example, **US** or **NL**.  The value of the `phoneCountryCode` is determined by the country code digit(s) of `phone.number` |
|     - type | string | No | The type of phone number. Possible values: **mobile**, **landline**, **sip**, **fax.** |
|   - residentialAddress | object | Yes | The residential address of the individual. Individuals cannot use a PO box as their residential address.  Address fields cannot contain emojis, only one repeated character (unless two characters long), only symbols, only numbers, only spaces, or **fictitious values** such as **John Doe** or **N/A**. All parts of the address must be different. For example, Spain, Spain, Spain is not allowed.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - city | string | No | The name of the city. Required if `stateOrProvince` is provided.  If you specify the city, you must also send `postalCode` and `street`.  The city name must be at least 3 characters. If the city name contains only repeated characters, the minimum length is two characters. For example, Aa is accepted, but Aaaa is not.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - country | string | Yes | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - postalCode | string | No | The postal code. Required if `stateOrProvince` and/or `city` is provided.  When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA. |
|     - stateOrProvince | string | No | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US. Required for Australia and New Zealand.  If you specify the state or province, you must also send `city`, `postalCode`, and `street`. |
|     - street | string | No | The name of the street, and the house or building number. Must be at least 3 characters. Required if `stateOrProvince` and/or `city` is provided. For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - street2 | string | No | The apartment, unit, or suite number. |
|   - support | object | No | Support information for the legal entity. Required if you have a platform setup. |
|     - email | string | No | The support email address of the legal entity. Required if you have a platform setup. |
|     - phone | object | No | The support phone number of the legal entity. Required if you have a platform setup. |
|   - taxInformation | array of object | No | The tax information of the individual. |
|     - country | string | No | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - number | string | No | The tax ID number (TIN) of the organization or individual. |
|     - numberAbsent | boolean | No | Set this to **true** if the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia. |
|     - type | string | No | The TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provide **SSN**, **EIN**, or **ITIN** for the US. |
|   - webData | object | No | The website and app URL of the legal entity. |
|     - webAddress | string | No | The URL of the website or the app store URL. |
|     - webAddressId | string | No | The unique identifier of the web address. |
| organization | object | No | Information about the organization. Required if `type` is **organization**. |
|   - countryOfGoverningLaw | string | No | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the governing country. |
|   - dateOfIncorporation | string | No | The date when the organization was incorporated in YYYY-MM-DD format. |
|   - dateOfInitiationOfLegalProceeding | string | No | Required if the value of `statusOfLegalProceeding` is one of the following:  **underJudicialAdministration**, **bankruptcyInsolvency**, **otherLegalMeasures**  The date at which a legal proceeding was initiated, in **YYYY-MM-DD** format. Example: **2000-02-12** |
|   - description | string | No | Your description for the organization. |
|   - doingBusinessAs | string | No | The organization's trading name, if different from the registered legal name. |
|   - doingBusinessAsAbsent | boolean | No | Set this to **true** if the organization or legal arrangement does not have a `Doing business as` name. |
|   - economicSector | string | No | The sector of the economy the legal entity operates within, represented by a 2-4 digit code that may include a ".". Example: 45.11  You can locate economic sector codes for your area by referencing codes defined by the NACE (Nomenclature of Economic Activities) used in the European Union. |
|   - email | string | No | The email address of the legal entity. |
|   - financialReports | array of object | No | The financial report information of the organization. |
|     - annualTurnover | string | No | The annual turnover of the business. |
|     - balanceSheetTotal | string | No | The balance sheet total of the business. |
|     - currencyOfFinancialData | string | No | The currency used for the financial data. |
|     - dateOfFinancialData | string | No | The date the financial data were provided, in YYYY-MM-DD format. |
|     - employeeCount | string | No | The number of employees of the business. |
|     - netAssets | string | No | The net assets of the business. |
|   - globalLegalEntityIdentifier | string | No | The global legal entity identifier for the organization.  This field is not required if the `registrationNumber` for the organization has been provided. |
|   - headOfficeIndicator | boolean | No | Indicates that the registered business address is also the company's headquarters. |
|   - institutionalSector | string | No | The institutional sector the organization operates within. |
|   - legalForm | string | No | The type of business entity as defined in the national legal system. Use a legal form listed within the accepted legal forms compiled by the Central Bank of Europe. |
|   - legalName | string | Yes | The organization's legal name. Must be at least 3 characters.  Only the following special characters are allowed: **,**, **-**, **—**, **.**, **;**, **:**, **&**, **?**, **@**, **(**, **)**, **"**, **'**, **!**, ****, **+**, **/**. Accents and non-Latin scripts are allowed.  The field cannot contain emojis, only one repeated character (unless two characters long), only symbols, only numbers, only spaces, or **fictitious names** such as **John Doe** or **N/A**.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|   - phone | object | No | The phone number of the legal entity. |
|     - number | string | Yes | The full phone number, including the country code. For example, **+3112345678**. |
|     - phoneCountryCode | string | No | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code prefix of the phone number. For example, **US** or **NL**.  The value of the `phoneCountryCode` is determined by the country code digit(s) of `phone.number` |
|     - type | string | No | The type of phone number. Possible values: **mobile**, **landline**, **sip**, **fax.** |
|   - principalPlaceOfBusiness | object | No | The address where the organization operates from. Provide this if the principal place of business is different from the `registeredAddress`. |
|     - city | string | No | The name of the city. Required if `stateOrProvince` is provided.  If you specify the city, you must also send `postalCode` and `street`.  The city name must be at least 3 characters. If the city name contains only repeated characters, the minimum length is two characters. For example, Aa is accepted, but Aaaa is not.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - country | string | Yes | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - postalCode | string | No | The postal code. Required if `stateOrProvince` and/or `city` is provided.  When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA. |
|     - stateOrProvince | string | No | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US. Required for Australia and New Zealand.  If you specify the state or province, you must also send `city`, `postalCode`, and `street`. |
|     - street | string | No | The name of the street, and the house or building number. Must be at least 3 characters. Required if `stateOrProvince` and/or `city` is provided. For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - street2 | string | No | The apartment, unit, or suite number. |
|   - registeredAddress | object | Yes | The address of the organization registered at their registrar (such as the Chamber of Commerce). If you use a PO box, you must also provide a `principalPlaceOfBusiness`. The principal place of business cannot be a PO box.  Address fields cannot contain emojis, only one repeated character (unless two characters long), only symbols, only numbers, only spaces, or **fictitious values** such as **John Doe** or **N/A**. All parts of the address must be different. For example, Spain, Spain, Spain is not allowed.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - city | string | No | The name of the city. Required if `stateOrProvince` is provided.  If you specify the city, you must also send `postalCode` and `street`.  The city name must be at least 3 characters. If the city name contains only repeated characters, the minimum length is two characters. For example, Aa is accepted, but Aaaa is not.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - country | string | Yes | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - postalCode | string | No | The postal code. Required if `stateOrProvince` and/or `city` is provided.  When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA. |
|     - stateOrProvince | string | No | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US. Required for Australia and New Zealand.  If you specify the state or province, you must also send `city`, `postalCode`, and `street`. |
|     - street | string | No | The name of the street, and the house or building number. Must be at least 3 characters. Required if `stateOrProvince` and/or `city` is provided. For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - street2 | string | No | The apartment, unit, or suite number. |
|   - registrationNumber | string | No | The organization's registration number. |
|   - registrationNumberAbsent | boolean | No | Set this to **true** if the organization does not have a registration number available. Only applicable for organizations in New Zealand, and incorporated partnerships and government organizations in Australia. |
|   - residentialAddressIndicator | boolean | No | Indicates if the `registeredAddress` is a place of residence, instead of a business address.  Set to **true** if the address is a place of residence. The default value is **false**. |
|   - statusOfLegalProceeding | string | No | The status of any current or past legal action taken against the legal entity.  Possible values: **noLegalActionsTaken**, **underJudicialAdministration**, **bankruptcyInsolvency**, **otherLegalMeasures**  If the value of this field is **noLegalActionsTaken**, then `dateOfInitiationOfLegalProceeding` is not required. Otherwise, it is required. |
|   - stockData | object | No | Information about the organization's publicly traded stock. Provide this object only if `type` is **listedPublicCompany**. |
|     - marketIdentifier | string | No | The four-digit [Market Identifier Code](https://en.wikipedia.org/wiki/Market_Identifier_Code) of the stock market where the organization's stocks are traded. |
|     - stockNumber | string | No | The 12-digit International Securities Identification Number (ISIN) of the company, without dashes (-). |
|     - tickerSymbol | string | No | The stock ticker symbol. |
|   - support | object | No | Support information for the legal entity. Required if you have a platform setup. |
|     - email | string | No | The support email address of the legal entity. Required if you have a platform setup. |
|     - phone | object | No | The support phone number of the legal entity. Required if you have a platform setup. |
|   - taxInformation | array of object | No | The tax information of the organization. |
|     - country | string | No | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - number | string | No | The tax ID number (TIN) of the organization or individual. |
|     - numberAbsent | boolean | No | Set this to **true** if the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia. |
|     - type | string | No | The TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provide **SSN**, **EIN**, or **ITIN** for the US. |
|   - taxReportingClassification | object | No | The tax reporting classification (FATCA/CRS self-certification) of the organization. Not required if your organization is US-based and requests business bank account capabilities. |
|     - businessType | string | No | The organization's business type.  Possible values: **other**, **listedPublicCompany**, **subsidiaryOfListedPublicCompany**, **governmentalOrganization**, **internationalOrganization**, **financialInstitution**. |
|     - financialInstitutionNumber | string | No | The Global Intermediary Identification Number (GIIN) required for FATCA. Only required if the organization is a US financial institution and the `businessType` is **financialInstitution**. |
|     - mainSourceOfIncome | string | No | The organization's main source of income. Only required if `businessType` is **other**.  Possible values: **businessOperation**, **realEstateSales**, **investmentInterestOrRoyalty**, **propertyRental**, **other**. |
|     - type | string | No | The tax reporting classification type.  Possible values: **nonFinancialNonReportable**, **financialNonReportable**, **nonFinancialActive**, **nonFinancialPassive**. |
|   - type | string | No | Type of organization.  Possible values: **associationIncorporated**, **governmentalOrganization**, **listedPublicCompany**, **nonProfit**, **partnershipIncorporated**, **privateCompany**. |
|   - vatAbsenceReason | string | No | The reason the organization has not provided a VAT number.  Possible values: **industryExemption**, **belowTaxThreshold**. |
|   - vatNumber | string | No | The organization's VAT number. |
|   - webData | object | No | The website and app URL of the legal entity. |
|     - webAddress | string | No | The URL of the website or the app store URL. |
|     - webAddressId | string | No | The unique identifier of the web address. |
| problems | array of object | No | List of verification errors related to capabilities for the legal entity. |
|   - entity | object | No |  |
|     - documents | array of string | No | List of document IDs corresponding to the verification errors from capabilities. |
|     - id | string | No |  |
|     - owner | object | No |  |
|     - type | string | No |  |
|   - verificationErrors | array of object | No |  |
|     - capabilities | array of string | No | Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example, **issueCard** for Issuing.The value is an object containing the settings for the capability. |
|     - code | string | No | The general error code. |
|     - message | string | No | The general error message. |
|     - remediatingActions | array of object | No | An object containing possible solutions to fix a verification error. |
|     - subErrors | array of object | No | An array containing more granular information about the cause of the verification error. |
|     - type | string | No | The type of error.  Possible values:  - **invalidInput**  - **dataMissing**  - **pendingStatus**  - **rejected**  - **dataReview** |
| reference | string | No | Your reference for the legal entity, maximum 150 characters. |
| soleProprietorship | object | No | Information about the sole proprietorship. Required if `type` is **soleProprietorship**. |
|   - countryOfGoverningLaw | string | No | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the governing country. |
|   - dateOfIncorporation | string | No | The date when the legal arrangement was incorporated in YYYY-MM-DD format. |
|   - doingBusinessAs | string | No | The registered name, if different from the `name`. |
|   - doingBusinessAsAbsent | boolean | No | Set this to **true** if the legal arrangement does not have a `Doing business as` name. |
|   - financialReports | array of object | No | The information from the financial report of the sole proprietorship. |
|     - annualTurnover | string | No | The annual turnover of the business. |
|     - balanceSheetTotal | string | No | The balance sheet total of the business. |
|     - currencyOfFinancialData | string | No | The currency used for the financial data. |
|     - dateOfFinancialData | string | No | The date the financial data were provided, in YYYY-MM-DD format. |
|     - employeeCount | string | No | The number of employees of the business. |
|     - netAssets | string | No | The net assets of the business. |
|   - name | string | Yes | The legal name. Must be at least 3 characters.  Only the following special characters are allowed: **,**, **-**, **—**, **.**, **;**, **:**, **&**, **?**, **@**, **(**, **)**, **"**, **'**, **!**, ****, **+**, **/**. Accents and non-Latin scripts are allowed.  The field cannot contain emojis, only one repeated character (unless two characters long), only symbols, only numbers, only spaces, or **fictitious names** such as **John Doe** or **N/A**.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|   - principalPlaceOfBusiness | object | No | The business address. Required if the principal place of business is different from the `registeredAddress`. |
|     - city | string | No | The name of the city. Required if `stateOrProvince` is provided.  If you specify the city, you must also send `postalCode` and `street`.  The city name must be at least 3 characters. If the city name contains only repeated characters, the minimum length is two characters. For example, Aa is accepted, but Aaaa is not.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - country | string | Yes | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - postalCode | string | No | The postal code. Required if `stateOrProvince` and/or `city` is provided.  When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA. |
|     - stateOrProvince | string | No | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US. Required for Australia and New Zealand.  If you specify the state or province, you must also send `city`, `postalCode`, and `street`. |
|     - street | string | No | The name of the street, and the house or building number. Must be at least 3 characters. Required if `stateOrProvince` and/or `city` is provided. For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - street2 | string | No | The apartment, unit, or suite number. |
|   - registeredAddress | object | Yes | The address registered at the registrar, such as the Chamber of Commerce. If you use a PO box, you must also provide a `principalPlaceOfBusiness`. The principal place of business cannot be a PO box.  Address fields cannot contain emojis, only one repeated character (unless two characters long), only symbols, only numbers, only spaces, or **fictitious values** such as **John Doe** or **N/A**. All parts of the address must be different. For example, Spain, Spain, Spain is not allowed.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - city | string | No | The name of the city. Required if `stateOrProvince` is provided.  If you specify the city, you must also send `postalCode` and `street`.  The city name must be at least 3 characters. If the city name contains only repeated characters, the minimum length is two characters. For example, Aa is accepted, but Aaaa is not.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - country | string | Yes | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - postalCode | string | No | The postal code. Required if `stateOrProvince` and/or `city` is provided.  When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA. |
|     - stateOrProvince | string | No | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US. Required for Australia and New Zealand.  If you specify the state or province, you must also send `city`, `postalCode`, and `street`. |
|     - street | string | No | The name of the street, and the house or building number. Must be at least 3 characters. Required if `stateOrProvince` and/or `city` is provided. For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - street2 | string | No | The apartment, unit, or suite number. |
|   - registrationNumber | string | No | The registration number. |
|   - residentialAddressIndicator | boolean | No | Indicates if the `registeredAddress` is a place of residence, instead of a business address.  Set to **true** if the address is a place of residence. The default value is **false**. |
|   - taxAbsent | boolean | No | The tax information is absent. |
|   - taxInformation | array of object | No | The tax information of the entity. |
|     - country | string | No | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - number | string | No | The tax ID number (TIN) of the organization or individual. |
|     - numberAbsent | boolean | No | Set this to **true** if the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia. |
|     - type | string | No | The TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provide **SSN**, **EIN**, or **ITIN** for the US. |
|   - vatAbsenceReason | string | No | The reason for not providing a VAT number.  Possible values: **industryExemption**, **belowTaxThreshold**. |
|   - vatNumber | string | No | The VAT number. |
| transferInstruments | array of object | No | List of transfer instruments that the legal entity owns. |
|   - accountIdentifier | string | Yes | The masked IBAN or bank account number. |
|   - id | string | Yes | The unique identifier of the resource. |
|   - realLastFour | string | No | Four last digits of the bank account number. If the transfer instrument is created using [instant bank account verification](https://docs.adyen.com/release-notes/platforms-and-financial-products#releaseNote=2023-05-08-hosted-onboarding), and it is a virtual bank account, these digits may be different from the last four digits of the masked account number. |
|   - trustedSource | boolean | No | Identifies if the bank account was created through [instant bank verification](https://docs.adyen.com/release-notes/platforms-and-financial-products#releaseNote=2023-05-08-hosted-onboarding). |
| trust | object | No | Information about the trust. Required if `type` is **trust**. |
|   - countryOfGoverningLaw | string | Yes | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the governing country. |
|   - dateOfIncorporation | string | No | The date when the legal arrangement was incorporated in YYYY-MM-DD format. |
|   - description | string | No | A short description about the trust. Only applicable for charitable trusts in New Zealand. |
|   - doingBusinessAs | string | No | The registered name, if different from the `name`. |
|   - doingBusinessAsAbsent | boolean | No | Set this to **true** if the legal arrangement does not have a `Doing business as` name. |
|   - name | string | Yes | The legal name. Must be at least 3 characters.  Only the following special characters are allowed: **,**, **-**, **—**, **.**, **;**, **:**, **&**, **?**, **@**, **(**, **)**, **"**, **'**, **!**, ****, **+**, **/**. Accents and non-Latin scripts are allowed.  The field cannot contain emojis, only one repeated character (unless two characters long), only symbols, only numbers, only spaces, or **fictitious names** such as **John Doe** or **N/A**.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|   - principalPlaceOfBusiness | object | No | The business address. Required if the principal place of business is different from the `registeredAddress`. |
|     - city | string | No | The name of the city. Required if `stateOrProvince` is provided.  If you specify the city, you must also send `postalCode` and `street`.  The city name must be at least 3 characters. If the city name contains only repeated characters, the minimum length is two characters. For example, Aa is accepted, but Aaaa is not.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - country | string | Yes | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - postalCode | string | No | The postal code. Required if `stateOrProvince` and/or `city` is provided.  When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA. |
|     - stateOrProvince | string | No | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US. Required for Australia and New Zealand.  If you specify the state or province, you must also send `city`, `postalCode`, and `street`. |
|     - street | string | No | The name of the street, and the house or building number. Must be at least 3 characters. Required if `stateOrProvince` and/or `city` is provided. For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - street2 | string | No | The apartment, unit, or suite number. |
|   - registeredAddress | object | Yes | The address registered at the registrar, such as the Chamber of Commerce. If you use a PO box, you must also provide a `principalPlaceOfBusiness`. The principal place of business cannot be a PO box.  Address fields cannot contain emojis, only one repeated character (unless two characters long), only symbols, only numbers, only spaces, or **fictitious values** such as **John Doe** or **N/A**. All parts of the address must be different. For example, Spain, Spain, Spain is not allowed.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - city | string | No | The name of the city. Required if `stateOrProvince` is provided.  If you specify the city, you must also send `postalCode` and `street`.  The city name must be at least 3 characters. If the city name contains only repeated characters, the minimum length is two characters. For example, Aa is accepted, but Aaaa is not.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - country | string | Yes | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - postalCode | string | No | The postal code. Required if `stateOrProvince` and/or `city` is provided.  When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA. |
|     - stateOrProvince | string | No | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US. Required for Australia and New Zealand.  If you specify the state or province, you must also send `city`, `postalCode`, and `street`. |
|     - street | string | No | The name of the street, and the house or building number. Must be at least 3 characters. Required if `stateOrProvince` and/or `city` is provided. For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - street2 | string | No | The apartment, unit, or suite number. |
|   - registrationNumber | string | No | The registration number. |
|   - residentialAddressIndicator | boolean | No | Indicates if the `registeredAddress` is a place of residence, instead of a business address.  Set to **true** if the address is a place of residence. The default value is **false**. |
|   - taxInformation | array of object | No | The tax information of the entity. |
|     - country | string | No | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - number | string | No | The tax ID number (TIN) of the organization or individual. |
|     - numberAbsent | boolean | No | Set this to **true** if the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia. |
|     - type | string | No | The TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provide **SSN**, **EIN**, or **ITIN** for the US. |
|   - type | string | Yes | Type of trust.  See possible values for trusts in [Australia](https://docs.adyen.com/platforms/verification-requirements/?tab=trust_3_4#trust-types-in-australia) and [New Zealand](https://docs.adyen.com/platforms/verification-requirements/?tab=trust_3_4#trust-types-in-new-zealand). |
|   - undefinedBeneficiaryInfo | array of object | No | The undefined beneficiary information of the entity. |
|     - description | string | No | The details of the undefined beneficiary. |
|     - reference | string | No | The reference of the undefined beneficiary. |
|   - vatAbsenceReason | string | No | The reason for not providing a VAT number.  Possible values: **industryExemption**, **belowTaxThreshold**. |
|   - vatNumber | string | No | The VAT number. |
| type | string | No | The type of legal entity.  Possible values: **individual**, **organization**, **soleProprietorship**, or **trust**. |
| unincorporatedPartnership | object | No | Information about the unincorporated partnership. Required if `type` is **unincorporatedPartnership**. |
|   - countryOfGoverningLaw | string | Yes | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the governing country. |
|   - dateOfIncorporation | string | No | The date when the legal arrangement was incorporated in YYYY-MM-DD format. |
|   - description | string | No | Short description about the Legal Arrangement. |
|   - doingBusinessAs | string | No | The registered name, if different from the `name`. |
|   - doingBusinessAsAbsent | boolean | No | Set this to **true** if the legal arrangement does not have a `Doing business as` name. |
|   - name | string | Yes | The legal name. Must be at least 3 characters.  Only the following special characters are allowed: **,**, **-**, **—**, **.**, **;**, **:**, **&**, **?**, **@**, **(**, **)**, **"**, **'**, **!**, ****, **+**, **/**. Accents and non-Latin scripts are allowed.  The field cannot contain emojis, only one repeated character (unless two characters long), only symbols, only numbers, only spaces, or **fictitious names** such as **John Doe** or **N/A**.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|   - principalPlaceOfBusiness | object | No | The business address. Required if the principal place of business is different from the `registeredAddress`. |
|     - city | string | No | The name of the city. Required if `stateOrProvince` is provided.  If you specify the city, you must also send `postalCode` and `street`.  The city name must be at least 3 characters. If the city name contains only repeated characters, the minimum length is two characters. For example, Aa is accepted, but Aaaa is not.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - country | string | Yes | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - postalCode | string | No | The postal code. Required if `stateOrProvince` and/or `city` is provided.  When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA. |
|     - stateOrProvince | string | No | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US. Required for Australia and New Zealand.  If you specify the state or province, you must also send `city`, `postalCode`, and `street`. |
|     - street | string | No | The name of the street, and the house or building number. Must be at least 3 characters. Required if `stateOrProvince` and/or `city` is provided. For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - street2 | string | No | The apartment, unit, or suite number. |
|   - registeredAddress | object | Yes | The address registered at the registrar, such as the Chamber of Commerce. If you use a PO box, you must also provide a `principalPlaceOfBusiness`. The principal place of business cannot be a PO box.  Address fields cannot contain emojis, only one repeated character (unless two characters long), only symbols, only numbers, only spaces, or **fictitious values** such as **John Doe** or **N/A**. All parts of the address must be different. For example, Spain, Spain, Spain is not allowed.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - city | string | No | The name of the city. Required if `stateOrProvince` is provided.  If you specify the city, you must also send `postalCode` and `street`.  The city name must be at least 3 characters. If the city name contains only repeated characters, the minimum length is two characters. For example, Aa is accepted, but Aaaa is not.  For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - country | string | Yes | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - postalCode | string | No | The postal code. Required if `stateOrProvince` and/or `city` is provided.  When using alphanumeric postal codes, all letters must be uppercase. For example, 1234 AB or SW1A 1AA. |
|     - stateOrProvince | string | No | The two-letter ISO 3166-2 state or province code. For example, **CA** in the US. Required for Australia and New Zealand.  If you specify the state or province, you must also send `city`, `postalCode`, and `street`. |
|     - street | string | No | The name of the street, and the house or building number. Must be at least 3 characters. Required if `stateOrProvince` and/or `city` is provided. For more information, see [validations on fields](https://docs.adyen.com/platforms/onboard-users/onboarding-versions/onboarding-v4/#validations). |
|     - street2 | string | No | The apartment, unit, or suite number. |
|   - registrationNumber | string | No | The registration number. |
|   - residentialAddressIndicator | boolean | No | Indicates if the `registeredAddress` is a place of residence, instead of a business address.  Set to **true** if the address is a place of residence. The default value is **false**. |
|   - taxInformation | array of object | No | The tax information of the entity. |
|     - country | string | No | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. |
|     - number | string | No | The tax ID number (TIN) of the organization or individual. |
|     - numberAbsent | boolean | No | Set this to **true** if the legal entity or legal arrangement does not have a tax ID number (TIN). Only applicable in Australia. |
|     - type | string | No | The TIN type depending on the country where it was issued. Only provide if the country has multiple tax IDs: Singapore, Sweden, the UK, or the US. For example, provide **SSN**, **EIN**, or **ITIN** for the US. |
|   - type | string | No | Type of Partnership.  Possible values:  - **limitedPartnership**  - **generalPartnership**  - **familyPartnership**  - **commercialPartnership**  - **publicPartnership**  - **otherPartnership**  - **gbr**  - **gmbh**  - **kgaa**  - **cv**  - **vof**  - **maatschap**  - **privateFundLimitedPartnership**  - **businessTrustEntity**  - **businessPartnership**  - **limitedLiabilityPartnership**  - **eg**  - **cooperative**  - **vos**  - **comunidadDeBienes**  - **herenciaYacente**  - **comunidadDePropietarios**  - **sep**  - **sca**  - **bt**  - **kkt**  - **scs**  - **snc** |
|   - vatAbsenceReason | string | No | The reason for not providing a VAT number.  Possible values: **industryExemption**, **belowTaxThreshold**. |
|   - vatNumber | string | No | The VAT number. |
| verificationDeadlines | array of object | No | List of verification deadlines and the capabilities that will be disallowed if verification errors are not resolved. |
|   - capabilities | array of string | Yes | The list of capabilities that will be disallowed if information is not reviewed by the time of the deadline |
|   - entityIds | array of string | No | The unique identifiers of the legal entity or supporting entities that the deadline applies to |
|   - expiresAt | string | Yes | The date that verification is due by before capabilities are disallowed. |
| verificationPlan | string | No | A key-value pair that specifies the verification process for a legal entity. Set to **upfront** for upfront verification for [marketplaces](https://docs.adyen.com/marketplaces/verification-overview/verification-types/#upfront-verification). |


### 400 Client Error
A problem reading or understanding the request.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
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
| errorCode | string | No | The error code mapped to the error message. |
| errorType | string | No | The category of the error. |
| message | string | No | A short explanation of the issue. |
| pspReference | string | No | The PSP reference of the payment. |
| status | integer | No | The HTTP response status. |

## Response examples

### 200 Success

**success**
```json
{
  "capabilities": {
    "sendToTransferInstrument": {
      "allowed": false,
      "requested": true,
      "transferInstruments": [
        {
          "allowed": false,
          "id": "SE322KH223222F5GXZFNM3BGP",
          "requested": true,
          "verificationStatus": "pending"
        }
      ],
      "verificationStatus": "pending"
    },
    "receivePayments": {
      "allowed": false,
      "requested": true,
      "verificationStatus": "pending"
    },
    "sendToBalanceAccount": {
      "allowed": false,
      "requested": true,
      "verificationStatus": "pending"
    },
    "receiveFromPlatformPayments": {
      "allowed": false,
      "requested": true,
      "verificationStatus": "pending"
    },
    "receiveFromBalanceAccount": {
      "allowed": false,
      "requested": true,
      "verificationStatus": "pending"
    }
  },
  "individual": {
    "email": "s.hopper@example.com",
    "birthData": {
      "dateOfBirth": "1990-06-21"
    },
    "name": {
      "firstName": "Simone",
      "lastName": "Hopper"
    },
    "phone": {
      "number": "+31858888138",
      "phoneCountryCode": "NL",
      "type": "mobile"
    },
    "residentialAddress": {
      "city": "Amsterdam",
      "country": "NL",
      "postalCode": "1011DJ",
      "street": "Simon Carmiggeltstraat 6 - 50",
      "street2": "274"
    }
  },
  "type": "individual",
  "id": "YOUR_LEGAL_ENTITY",
  "transferInstruments": [
    {
      "id": "SE322KH223222F5GXZFNM3BGP",
      "accountIdentifier": "NL**ABNA******0123",
      "trustedSource": false
    }
  ]
}
```