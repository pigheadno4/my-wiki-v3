<!-- Source URL: https://docs.stripe.com/payments/customer-balance/funding-instructions -->
<!-- Fetched: 2026-05-05 -->

# Funding instructions

Provide customer balance funding instructions without creating a PaymentIntent.

You can show bank account details to your customer before they make their first payment through the Dashboard or API.

## Create or retrieve funding instructions

#### Dashboard

### Create funding instructions

To create funding instructions for your customers:

1. Go to the [customer’s page](https://dashboard.stripe.com/customers).
1. Under **Payment methods**, click **+** > **Add a bank transfer account**.
1. Select the currency and country you want to create a bank transfer account for, then click **Add**. Stripe creates a cash balance with the appropriate currency for your customer.

### Retrieve funding instructions

1. Go to the [customer’s page](https://dashboard.stripe.com/customers).
1. Under **Payment methods**, select the cash balance with the relevant currency, then click **View balance details**.
1. Review the **Bank transfer funding instructions**.

#### API

Use the Customer Balance Funding Instructions API to retrieve a set of `financial_addresses` that can receive funds from the customer. Provide these bank account details to your customer so that they can initiate a bank transfer using any of the `supported_networks`.

> In *live mode* (Use this mode when you’re ready to launch your app. Card networks or payment providers process payments), Stripe supplies each customer with a unique set of bank transfer details. In contrast, Stripe offers invalid bank transfer details to all customers in testing environments. Unlike live mode, these invalid details might not always be unique.

#### US

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const fundingInstructions = await stripe.customers.createFundingInstructions(
  "{{CUSTOMER_ID}}",
  {
    funding_type: "bank_transfer",
    bank_transfer: {
      type: "us_bank_transfer",
    },
    currency: "usd",
  },
);
```

#### UK

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const fundingInstructions = await stripe.customers.createFundingInstructions(
  "{{CUSTOMER_ID}}",
  {
    funding_type: "bank_transfer",
    bank_transfer: {
      type: "gb_bank_transfer",
    },
    currency: "gbp",
  },
);
```

#### EU

For funding instructions in the Single Euro Payments Area (SEPA) set `bank_transfer[eu_bank_transfer][country]` to one of to display the localized IBAN to your customer.

Stripe’s [bank transfer fees](https://stripe.com/pricing/local-payment-methods) in SEPA countries include up to 1000 virtual bank account numbers (VBANs). [Contact us](https://stripe.com/contact/sales) if you require more than 1000 unique VBANs.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const fundingInstructions = await stripe.customers.createFundingInstructions(
  "{{CUSTOMER_ID}}",
  {
    funding_type: "bank_transfer",
    bank_transfer: {
      type: "eu_bank_transfer",
      eu_bank_transfer: {
        country: "NL",
      },
    },
    currency: "eur",
  },
);
```

> Creating new localized virtual bank account numbers is currently unavailable for Spain (ES). Use any of the other EU VBAN countries instead.

#### JP

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const fundingInstructions = await stripe.customers.createFundingInstructions(
  "{{CUSTOMER_ID}}",
  {
    funding_type: "bank_transfer",
    bank_transfer: {
      type: "jp_bank_transfer",
    },
    currency: "jpy",
  },
);
```

#### MX

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const fundingInstructions = await stripe.customers.createFundingInstructions(
  "{{CUSTOMER_ID}}",
  {
    funding_type: "bank_transfer",
    bank_transfer: {
      type: "mx_bank_transfer",
    },
    currency: "mxn",
  },
);
```

The response contains the following fields:

#### US

### Bank transfer hash

| Field                 | Values                                                                                         | Description                                                     |
| --------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| `type`                | `us_bank_transfer`                                                                             | The type of bank transfer to use.                               |
| `currency`            | `usd`                                                                                          | The supported currency for the bank transfer.                   |
| `country`             | `US`                                                                                           | The two-letter country code of the bank account to transfer to. |
| `financial_addresses` | - `aba` hash                                                                                   |
| - `swift` hash        | The list of financial addresses. Funds sent to any address are routed to the customer balance. |

### ABA hash

| Field                | Values                                          | Description                    |
| -------------------- | ----------------------------------------------- | ------------------------------ |
| `type`               | `aba`                                           | The type of financial address. |
| `supported_networks` | - `ach`                                         |
| - `domestic_wire_us` | The list of networks supported by this address. |
| `aba.account_number` | 111222333444                                    | The ABA account number.        |
| `aba.account_type`   | `checking`, `savings`                           | The type of the bank account.  |
| `aba.routing_number` | 444555666                                       | The ABA routing number.        |
| `aba.bank_name`      | Wells Fargo Bank, NA                            | The name of the bank.          |
| `aba.bank_address`   | - `city`                                        |

- `country`
- `line1`
- `line2`
- `postal_code`
- `state` | The address of the bank. |
  | `aba.account_holder_name` | Powdur | The name of the person or business that owns the bank account. |
  | `aba.account_holder_address` | - `city`
- `country`
- `line1`
- `line2`
- `postal_code`
- `state` | The address of the person or business that owns the bank account. |

### SWIFT hash

| Field                  | Values                | Description                                     |
| ---------------------- | --------------------- | ----------------------------------------------- |
| `type`                 | `swift`               | The type of financial address.                  |
| `supported_networks`   | `swift`               | The list of networks supported by this address. |
| `swift.account_number` | 111222333444          | The SWIFT account number.                       |
| `swift.account_type`   | `checking`, `savings` | The type of the bank account.                   |
| `swift.swift_code`     | AAAA-BB-CC-123        | The SWIFT code.                                 |
| `swift.bank_name`      | Wells Fargo Bank, NA  | The name of the bank.                           |
| `swift.bank_address`   | - `city`              |

- `country`
- `line1`
- `line2`
- `postal_code`
- `state` | The address of the bank. |
  | `swift.account_holder_name` | Powdur | The name of the person or business that owns the bank account. |
  | `swift.account_holder_address` | - `city`
- `country`
- `line1`
- `line2`
- `postal_code`
- `state` | The address of the person or business that owns the bank account. |

#### UK

### Bank transfer hash

| Field                 | Values             | Description                                                                                    |
| --------------------- | ------------------ | ---------------------------------------------------------------------------------------------- |
| `type`                | `gb_bank_transfer` | The type of bank transfer to use.                                                              |
| `currency`            | `gbp`              | The supported currency for the bank transfer.                                                  |
| `country`             | `GB`               | The two-letter country code of the bank account to transfer to.                                |
| `financial_addresses` | `sort_code` hash   | The list of financial addresses. Funds sent to any address are routed to the customer balance. |

### Sort code hash

| Field                      | Values                                          | Description                    |
| -------------------------- | ----------------------------------------------- | ------------------------------ |
| `type`                     | `sort_code`                                     | The type of financial address. |
| `supported_networks`       | - `bacs`                                        |
| - `fps`                    | The list of networks supported by this address. |
| `sort_code.account_number` | 98765432                                        | The 8 digit account number.    |
| `sort_code.sort_code`      | 200000                                          | The 6 digit sort code.         |
| `sort_code.bank_name`      | Barclays Bank PLC                               | The name of the bank.          |
| `sort_code.bank_address`   | - `city`                                        |

- `country`
- `line1`
- `line2`
- `postal_code`
- `state` | The address of the bank. |
  | `sort_code.account_holder_name` | Powdur. | The name of the person or business that owns the bank account. |
  | `sort_code.account_holder_address` | - `city`
- `country`
- `line1`
- `line2`
- `postal_code`
- `state` | The address of the person or business that owns the bank account. |

#### EU

### Bank transfer hash

| Field                 | Values             | Description                                                                                    |
| --------------------- | ------------------ | ---------------------------------------------------------------------------------------------- |
| `type`                | `eu_bank_transfer` | The type of bank transfer to use.                                                              |
| `currency`            | `eur`              | The supported currency for the bank transfer.                                                  |
| `country`             | `NL`               | The two-letter country code of the bank account to transfer to.                                |
| `financial_addresses` | `iban` hash        | The list of financial addresses. Funds sent to any address are routed to the customer balance. |

### IBAN hash

| Field                | Values          | Description                                                                                                                   |
| -------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `type`               | `iban`          | The type of financial address.                                                                                                |
| `supported_networks` | `sepa`          | The list of networks supported by this address.                                                                               |
| `iban.iban`          | NL123456789     | The IBAN the customer needs to pay to. The IBAN’s country is selected based on the `country` parameter passed in the request. |
| `iban.bic`           | 1234            | The BIC for this IBAN.                                                                                                        |
| `iban.country`       | `NL`            | The two-letter country code of the bank account to transfer to.                                                               |
| `iban.bank_name`     | Citibank Europe | The name of the bank.                                                                                                         |
| `iban.bank_address`  | - `city`        |

- `country`
- `line1`
- `line2`
- `postal_code`
- `state` | The address of the bank. |
  | `iban.account_holder_name` | Powdur. | The name of the person or business that owns the bank account. |
  | `iban.account_holder_address` | - `city`
- `country`
- `line1`
- `line2`
- `postal_code`
- `state` | The address of the person or business that owns the bank account. |

#### JP

### Bank transfer hash

| Field                 | Values             | Description                                                                                                                                                           |
| --------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                | `jp_bank_transfer` | The type of bank transfer to use.                                                                                                                                     |
| `currency`            | `jpy`              | The supported currency for the bank transfer.                                                                                                                         |
| `country`             | `JP`               | The two-letter country code of the bank account to transfer to.                                                                                                       |
| `financial_addresses` | `zengin` hash      | The list of financial addresses. Funds sent to any address are routed to the customer balance. In Japan, the `zengin` hash is the only financial address in the list. |

### Zengin hash

| Field                 | Values       | Description                                     |
| --------------------- | ------------ | ----------------------------------------------- |
| `type`                | `zengin`     | The type of financial address.                  |
| `supported_networks`  | `zengin`     | The list of networks supported by this address. |
| `zengin.bank_code`    | 0009         | The 4 digit bank code.                          |
| `zengin.bank_name`    | 三井住友銀行 | The bank name.                                  |
| `zengin.bank_address` | - `city`     |

- `country`
- `line1`
- `line2`
- `postal_code`
- `state` | The address of the bank. |
  | `zengin.branch_code` | 950 | The 3 digit branch code. |
  | `zengin.branch_name` | 東京第二 | The branch name. |
  | `zengin.account_type` | `futsu`, `toza` | The account type. |
  | `zengin.account_holder_name` | ストライプジャパン（カ　シュウノウダイコウ | The account holder name. |
  | `zengin.account_holder_address` | - `city`
- `country`
- `line1`
- `line2`
- `postal_code`
- `state` | The address of the person or business that owns the bank account. |
  | `zengin.account_number` | 1234567 | The 7 digit account number. |

#### MX

### Bank transfer hash

| Field                 | Values             | Description                                                                                                                                                          |
| --------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                | `mx_bank_transfer` | The type of bank transfer to use.                                                                                                                                    |
| `currency`            | `mxn`              | The supported currency for the bank transfer.                                                                                                                        |
| `country`             | `MX`               | The two-letter country code of the bank account to transfer to.                                                                                                      |
| `financial_addresses` | `spei` hash        | The list of financial addresses. Funds sent to any address are routed to the customer balance. In Mexico, the `spei` hash is the only financial address in the list. |

### SPEI hash

| Field                | Values             | Description                                     |
| -------------------- | ------------------ | ----------------------------------------------- |
| `type`               | `spei`             | The type of financial address.                  |
| `supported_networks` | `spei`             | The list of networks supported by this address. |
| `spei.clabe`         | 002180650612345670 | The 18 digit CLABE number.                      |
| `spei.bank_code`     | 002                | The three-digit bank code.                      |
| `spei.bank_name`     | BANAMEX            | The short name of the banking institution       |
| `spei.bank_address`  | - `city`           |

- `country`
- `line1`
- `line2`
- `postal_code`
- `state` | The address of the bank. |
  | `spei.account_holder_name` | Powdur | The name of the person or business that owns the bank account. |
  | `spei.account_holder_address` | - `city`
- `country`
- `line1`
- `line2`
- `postal_code`
- `state` | The address of the person or business that owns the bank account. |

## Download confirmation of account ownership

Some customers might request additional assurance that the account they’re transferring money into is yours, because the account might be listed as owned by Stripe. To provide this assurance, you can generate a letter confirming your ownership of the account to the customer. In this letter, Stripe confirms that you’re the owner of the virtual bank account corresponding to the account details you have passed to that customer.

To download a letter confirming account ownership:

1. Go to the [Customers page](https://dashboard.stripe.com/customers) in the Dashboard.

1. Select the customer who has requested additional verification that you own the account.

1. Go to their cash balance details. This page shows the account details that the customer must use to pay you by bank transfer.

1. Click the button to download a confirmation letter in a PDF format with today’s date.
   ![Button to download confirmation of account ownership](assets/stripe-vban-confirmation-letter-button.png)

Download confirmation of account ownership
