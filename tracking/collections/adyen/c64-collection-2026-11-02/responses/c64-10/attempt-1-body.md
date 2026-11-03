# GET /accountHolders/{id}/taxFormSummary - Get summary of tax forms for an account holder

Returns a summary of all tax forms for an account holder.

## Servers
- https://balanceplatform-api-test.adyen.com/bcl/v2

## Parameters

### Path parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | The unique identifier of the account holder. |


### Query parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| formType | string | Yes | The type of tax form you want a summary for. Accepted values are **US1099k** and **US1099nec**. |

## Responses

### 200 Success
The request has succeeded.

**Response body**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| data | array of object | Yes | A list of tax form summaries, where each summary consists of the legal entity and the tax years in which the legal entity has a tax form. |
|   - legalEntityId | string | Yes | The unique identifier of the legal entity. |
|   - taxYears | array of integer | Yes | The tax years for which the legal entity has a tax form. |

## Response examples

### 200 Success

**get-tax-form-summary-200**
```json
{
  "data": [
    {
      "legalEntityId": "LE123",
      "taxYears": [
        2023
      ]
    },
    {
      "legalEntityId": "LE987",
      "taxYears": [
        2024,
        2025
      ]
    }
  ]
}
```