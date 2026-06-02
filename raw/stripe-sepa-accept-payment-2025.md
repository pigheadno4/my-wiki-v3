<!-- Source URL: https://docs.stripe.com/payments/sepa-debit/accept-a-payment -->
<!-- Fetched: 2026-05-03 -->

# Accept a SEPA Direct Debit payment

Learn to accept SEPA Direct Debit payments.

# Checkout

> This is a Checkout for when payment-ui is checkout. View the full page at https://docs.stripe.com/payments/sepa-debit/accept-a-payment?payment-ui=checkout.

> Stripe can automatically present the relevant payment methods to your customers by evaluating currency, payment method restrictions, and other parameters.
>
> - Follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) guide to build a Checkout integration that uses [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md).

- If you don’t want to use dynamic payment methods, follow the steps below to manually configure the payment methods in your Checkout integration.

Accepting SEPA Direct Debit payments on your website consists of creating an object to track a payment, collecting payment method information and mandate acknowledgement, and submitting the payment to Stripe for processing. Stripe uses this payment object, the PaymentIntent, to track and handle all the states of the payment until the payment completes.

> SEPA Direct Debit is a **delayed notification payment method**, which means that funds aren’t immediately available after payment. A payment typically takes **5 business days** to arrive in your account.

## Determine compatibility

**Supported business locations**: Europe, US, CA, NZ, SG, HK, JP, AU, MX

**Supported currencies**: `eur`

**Presentment currencies**: `eur`

**Payment mode**: Yes

**Setup mode**: Yes

**Subscription mode**: Yes

To support SEPA Direct Debit payments in Checkout, *Prices* (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions) for all line items must be expressed in Euro (currency code `eur`).

## Accept a payment

> This guide builds on the foundational [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?ui=stripe-hosted) Checkout integration.

Use this guide to learn how to enable SEPA Direct Debit—it shows the differences between accepting payments using dynamic payment methods and manually configuring payment methods.

### Enable SEPA Direct Debit as a payment method

When creating a new [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md), you need to:

1. Add `sepa_debit` to the list of `payment_method_types`.
1. Make sure all your `line_items` use the `eur` currency.

#### Stripe-hosted page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: 'eur',
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  payment_method_types: ["card", "sepa_debit"],
  success_url: 'https://example.com/success',
});
```

#### Full embedded page

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        currency: 'eur',
        product_data: {
          name: "T-shirt",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  payment_method_types: ["card", "sepa_debit"],
  return_url: 'https://example.com/return',
  ui_mode: 'embedded_page',
});
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill orders](https://docs.stripe.com/checkout/fulfillment.md).

## Test your integration

Stripe provides several test numbers you can use to make sure your integration is ready for production.

##### Test IBANs

Use these test IBANs with the Payment Element to test your SEPA Direct Debit integration. The Payment Element automatically validates the IBAN and displays the mandate when you enter one of these test values.

### AT

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| AT611904300234573201 | pm_success_at                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| AT321904300235473204 | pm_successDelayed_at                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| AT861904300235473202 | pm_failed_at                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| AT051904300235473205 | pm_failedDelayed_at                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| AT591904300235473203 | pm_disputed_at                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| AT981904300000343434 | pm_exceedsWeeklyVolumeLimit_at      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| AT601904300000121212 | pm_exceedsWeeklyTransactionLimit_at | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| AT981904300002222227 | pm_insufficientFunds_at             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### BE

| Account Number   | Token                               | Description                                                                                                                                          |
| ---------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| BE62510007547061 | pm_success_be                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| BE78510007547064 | pm_successDelayed_be                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| BE68539007547034 | pm_failed_be                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| BE51510007547065 | pm_failedDelayed_be                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| BE08510007547063 | pm_disputed_be                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| BE90510000343434 | pm_exceedsWeeklyVolumeLimit_be      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| BE52510000121212 | pm_exceedsWeeklyTransactionLimit_be | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| BE90510002222227 | pm_insufficientFunds_be             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### HR

| Account Number        | Token                               | Description                                                                                                                                          |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| HR7624020064583467589 | pm_success_hr                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| HR6323600002337876649 | pm_successDelayed_hr                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| HR2725000096983499248 | pm_failed_hr                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| HR6723600004878117427 | pm_failedDelayed_hr                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| HR8724840081455523553 | pm_disputed_hr                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| HR7424020060000343434 | pm_exceedsWeeklyVolumeLimit_hr      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| HR3624020060000121212 | pm_exceedsWeeklyTransactionLimit_hr | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| HR7424020060002222227 | pm_insufficientFunds_hr             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### EE

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| EE382200221020145685 | pm_success_ee                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| EE222200221020145682 | pm_successDelayed_ee                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| EE762200221020145680 | pm_failed_ee                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| EE922200221020145683 | pm_failedDelayed_ee                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| EE492200221020145681 | pm_disputed_ee                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| EE672200000000343434 | pm_exceedsWeeklyVolumeLimit_ee      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| EE292200000000121212 | pm_exceedsWeeklyTransactionLimit_ee | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| EE672200000002222227 | pm_insufficientFunds_ee             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### FI

| Account Number     | Token                               | Description                                                                                                                                          |
| ------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| FI2112345600000785 | pm_success_fi                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| FI3712345600000788 | pm_successDelayed_fi                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| FI9112345600000786 | pm_failed_fi                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| FI1012345600000789 | pm_failedDelayed_fi                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| FI6412345600000787 | pm_disputed_fi                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| FI6712345600343434 | pm_exceedsWeeklyVolumeLimit_fi      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| FI2912345600121212 | pm_exceedsWeeklyTransactionLimit_fi | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| FI6712345602222227 | pm_insufficientFunds_fi             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### FR

| Account Number              | Token                               | Description                                                                                                                                          |
| --------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| FR1420041010050500013M02606 | pm_success_fr                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| FR3020041010050500013M02609 | pm_successDelayed_fr                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| FR8420041010050500013M02607 | pm_failed_fr                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| FR7920041010050500013M02600 | pm_failedDelayed_fr                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| FR5720041010050500013M02608 | pm_disputed_fr                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| FR9720041010050000000343434 | pm_exceedsWeeklyVolumeLimit_fr      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| FR5920041010050000000121212 | pm_exceedsWeeklyTransactionLimit_fr | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| FR9720041010050000002222227 | pm_insufficientFunds_fr             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### DE

| Account Number         | Token                               | Description                                                                                                                                          |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| DE89370400440532013000 | pm_success_de                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| DE08370400440532013003 | pm_successDelayed_de                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| DE62370400440532013001 | pm_failed_de                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| DE78370400440532013004 | pm_failedDelayed_de                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| DE35370400440532013002 | pm_disputed_de                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| DE65370400440000343434 | pm_exceedsWeeklyVolumeLimit_de      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| DE27370400440000121212 | pm_exceedsWeeklyTransactionLimit_de | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| DE65370400440002222227 | pm_insufficientFunds_de             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### GI

| Account Number          | Token                               | Description                                                                                                                                          |
| ----------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| GI60MPFS599327643783385 | pm_success_gi                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| GI08RRNW626436291644533 | pm_successDelayed_gi                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| GI41SAFA461293238477751 | pm_failed_gi                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| GI50LROG772261344693297 | pm_failedDelayed_gi                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| GI26KJBC361883934534696 | pm_disputed_gi                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| GI14NWBK000000000343434 | pm_exceedsWeeklyVolumeLimit_gi      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| GI73NWBK000000000121212 | pm_exceedsWeeklyTransactionLimit_gi | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| GI14NWBK000000002222227 | pm_insufficientFunds_gi             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### IE

| Account Number         | Token                               | Description                                                                                                                                          |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| IE29AIBK93115212345678 | pm_success_ie                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| IE24AIBK93115212345671 | pm_successDelayed_ie                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| IE02AIBK93115212345679 | pm_failed_ie                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| IE94AIBK93115212345672 | pm_failedDelayed_ie                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| IE51AIBK93115212345670 | pm_disputed_ie                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| IE10AIBK93115200343434 | pm_exceedsWeeklyVolumeLimit_ie      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| IE69AIBK93115200121212 | pm_exceedsWeeklyTransactionLimit_ie | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| IE10AIBK93115202222227 | pm_insufficientFunds_ie             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### LI

| Account Number        | Token                               | Description                                                                                                                                          |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| LI0508800636123378777 | pm_success_li                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| LI4408800387787111369 | pm_successDelayed_li                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| LI1208800143823175626 | pm_failed_li                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| LI4908800356441975566 | pm_failedDelayed_li                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| LI7708800125525347723 | pm_disputed_li                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| LI2408800000000343434 | pm_exceedsWeeklyVolumeLimit_li      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| LI8308800000000121212 | pm_exceedsWeeklyTransactionLimit_li | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| LI2408800000002222227 | pm_insufficientFunds_li             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### LT

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| LT121000011101001000 | pm_success_lt                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| LT281000011101001003 | pm_successDelayed_lt                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| LT821000011101001001 | pm_failed_lt                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| LT981000011101001004 | pm_failedDelayed_lt                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| LT551000011101001002 | pm_disputed_lt                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| LT591000000000343434 | pm_exceedsWeeklyVolumeLimit_lt      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| LT211000000000121212 | pm_exceedsWeeklyTransactionLimit_lt | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| LT591000000002222227 | pm_insufficientFunds_lt             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### LU

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| LU280019400644750000 | pm_success_lu                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| LU440019400644750003 | pm_successDelayed_lu                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| LU980019400644750001 | pm_failed_lu                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| LU170019400644750004 | pm_failedDelayed_lu                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| LU710019400644750002 | pm_disputed_lu                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| LU900010000000343434 | pm_exceedsWeeklyVolumeLimit_lu      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| LU520010000000121212 | pm_exceedsWeeklyTransactionLimit_lu | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| LU900010000002222227 | pm_insufficientFunds_lu             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### NL

| Account Number     | Token                               | Description                                                                                                                                          |
| ------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| NL39RABO0300065264 | pm_success_nl                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| NL55RABO0300065267 | pm_successDelayed_nl                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| NL91ABNA0417164300 | pm_failed_nl                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| NL28RABO0300065268 | pm_failedDelayed_nl                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| NL82RABO0300065266 | pm_disputed_nl                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| NL27RABO0000343434 | pm_exceedsWeeklyVolumeLimit_nl      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| NL86RABO0000121212 | pm_exceedsWeeklyTransactionLimit_nl | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| NL55RABO0300065267 | pm_insufficientFunds_nl             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### NO

| Account Number  | Token                               | Description                                                                                                                                          |
| --------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| NO9386011117947 | pm_success_no                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| NO8886011117940 | pm_successDelayed_no                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| NO6686011117948 | pm_failed_no                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| NO6186011117941 | pm_failedDelayed_no                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| NO3986011117949 | pm_disputed_no                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| NO0586010343434 | pm_exceedsWeeklyVolumeLimit_no      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| NO0586010343434 | pm_exceedsWeeklyTransactionLimit_no | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| NO0586012222227 | pm_insufficientFunds_no             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### PT

| Account Number            | Token                               | Description                                                                                                                                          |
| ------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| PT50000201231234567890154 | pm_success_pt                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| PT66000201231234567890157 | pm_successDelayed_pt                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| PT23000201231234567890155 | pm_failed_pt                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| PT39000201231234567890158 | pm_failedDelayed_pt                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| PT93000201231234567890156 | pm_disputed_pt                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| PT05000201230000000343434 | pm_exceedsWeeklyVolumeLimit_pt      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| PT64000201230000000121212 | pm_exceedsWeeklyTransactionLimit_pt | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| PT05000201230000002222227 | pm_insufficientFunds_pt             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### ES

| Account Number           | Token                               | Description                                                                                                                                          |
| ------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| ES0700120345030000067890 | pm_success_es                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| ES2300120345030000067893 | pm_successDelayed_es                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| ES9121000418450200051332 | pm_failed_es                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| ES9300120345030000067894 | pm_failedDelayed_es                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| ES5000120345030000067892 | pm_disputed_es                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| ES1700120345000000343434 | pm_exceedsWeeklyVolumeLimit_es      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| ES7600120345000000121212 | pm_exceedsWeeklyTransactionLimit_es | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| ES1700120345000002222227 | pm_insufficientFunds_es             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### SE

| Account Number           | Token                               | Description                                                                                                                                          |
| ------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| SE3550000000054910000003 | pm_success_se                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| SE5150000000054910000006 | pm_successDelayed_se                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| SE0850000000054910000004 | pm_failed_se                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| SE2450000000054910000007 | pm_failedDelayed_se                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| SE7850000000054910000005 | pm_disputed_se                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| SE2850000000000000343434 | pm_exceedsWeeklyVolumeLimit_se      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| SE8750000000000000121212 | pm_exceedsWeeklyTransactionLimit_se | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| SE2850000000000002222227 | pm_insufficientFunds_se             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### CH

| Account Number        | Token                               | Description                                                                                                                                          |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| CH9300762011623852957 | pm_success_ch                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| CH8656663438253651553 | pm_successDelayed_ch                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| CH5362200119938136497 | pm_failed_ch                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| CH1843597160341964438 | pm_failedDelayed_ch                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| CH1260378413965193069 | pm_disputed_ch                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| CH1800762000000343434 | pm_exceedsWeeklyVolumeLimit_ch      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| CH7700762000000121212 | pm_exceedsWeeklyTransactionLimit_ch | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| CH1800762000002222227 | pm_insufficientFunds_ch             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### GB

| Account Number         | Token                               | Description                                                                                                                                          |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| GB82WEST12345698765432 | pm_success_gb                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| GB98WEST12345698765435 | pm_successDelayed_gb                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| GB55WEST12345698765433 | pm_failed_gb                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| GB71WEST12345698765436 | pm_failedDelayed_gb                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| GB28WEST12345698765434 | pm_disputed_gb                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| GB70WEST12345600343434 | pm_exceedsWeeklyVolumeLimit_gb      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| GB32WEST12345600121212 | pm_exceedsWeeklyTransactionLimit_gb | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| GB70WEST12345602222227 | pm_insufficientFunds_gb             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

## Handle refunds and disputes

The refund period for SEPA Direct Debit is up to 180 days after the original payment.

*Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) can dispute a payment through their bank up to 13 months after the original payment and there’s no appeal process.

Learn more about [SEPA Direct Debit disputes](https://docs.stripe.com/payments/sepa-debit.md#disputed-payments).

## Optional: Customize mandate references with a prefix

You can customize SEPA Direct Debit mandate references to simplify mandate identification. To do this, provide the optional `payment_method_options.sepa_debit.mandate_options.reference_prefix` value. We add the `reference_prefix` to the beginning of a unique sequence to ensure the entire reference remains unique.

The `reference_prefix` must meet these requirements:

- Maximum length: 12 characters
- Must begin with a number or an uppercase letter
- Allowed characters:
  - Uppercase letters
  - Numbers
  - Spaces
  - Special characters: `.`, `/`, `&`, `-`, `_`
- Can’t begin with `STRIPE`

Include any desired delimiter in the prefix, as we don’t add one by default. We trim trailing spaces to a maximum of one space. With a valid prefix, the resulting reference is always 24 characters long.

#### Payment Intent

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  currency: 'eur',
  amount: 100,
  payment_method_types: ["sepa_debit"],
  payment_method_options: {
    sepa_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

#### Setup Intent

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["sepa_debit"],
  payment_method_options: {
    sepa_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

#### Checkout Session in Payment Mode

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'payment',
  currency: 'eur',
  line_items: [
    {
      price_data: {
        currency: 'eur',
        product_data: {
          name: "Llama",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  payment_method_types: ["sepa_debit"],
  payment_method_options: {
    sepa_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

#### Checkout Session in Setup Mode

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'setup',
  payment_method_types: ["sepa_debit"],
  payment_method_options: {
    sepa_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

The generated reference looks like `EX4MPL3-19CNCI920C2M02O3`.

| Error Code                                     | Message                                                                                                                                                                                                 |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `invalid_sepa_mandate_reference_prefix_format` | The `reference_prefix` must be at most 12 characters long and can only contain uppercase letters, numbers, spaces, or the special characters `/`, `_`, `-`, `&`, and `.`. It can’t begin with `STRIPE`. |

## Optional: Configure customer debit date

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-payment_method_options-sepa_debit-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date.

Target dates that meet one of the following criteria delay the debit until the next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/sepa-debit/accept-a-payment?payment-ui=mobile&platform=react-native.

> We recommend that you follow the [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) guide unless you need to use manual server-side confirmation, or your integration requires presenting payment methods separately. If you’ve already integrated with Elements, see the [Payment Element migration guide](https://docs.stripe.com/payments/payment-element/migration.md).

Accepting SEPA Direct Debit payments on your website consists of creating an object to track a payment, collecting payment method information and mandate acknowledgement, and submitting the payment to Stripe for processing. Stripe uses this payment object, the PaymentIntent, to track and handle all the states of the payment until the payment completes.

You can also set up a SEPA Direct Debit *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) by having your customer authenticate their bank details with [Bancontact](https://docs.stripe.com/payments/bancontact/save-during-payment.md) or [iDEAL](https://docs.stripe.com/payments/ideal/save-during-payment.md).

## Set up Stripe [Server-side] [Client-side]

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [React Native SDK](https://github.com/stripe/stripe-react-native) is open source and fully documented. Internally, it uses the [native iOS](https://github.com/stripe/stripe-ios) and [Android](https://github.com/stripe/stripe-android) SDKs. To install Stripe’s React Native SDK, run one of the following commands in your project’s directory (depending on which package manager you use):

#### yarn

```bash
yarn add @stripe/stripe-react-native
```

#### npm

```bash
npm install @stripe/stripe-react-native
```

Next, install some other necessary dependencies:

- For iOS, go to the **ios** directory and run `pod install` to ensure that you also install the required native dependencies.
- For Android, there are no more dependencies to install.

> We recommend following the [official TypeScript guide](https://reactnative.dev/docs/typescript#adding-typescript-to-an-existing-project) to add TypeScript support.

### Stripe initialization

To initialize Stripe in your React Native app, either wrap your payment screen with the `StripeProvider` component, or use the `initStripe` initialization method. Only the API [publishable key](https://docs.stripe.com/keys.md#obtain-api-keys) in `publishableKey` is required. The following example shows how to initialize Stripe using the `StripeProvider` component.

```jsx
import { useState, useEffect } from "react";
import { StripeProvider } from "@stripe/stripe-react-native";

function App() {
  const [publishableKey, setPublishableKey] = useState("");

  const fetchPublishableKey = async () => {
    const key = await fetchKey(); // fetch key from your server here
    setPublishableKey(key);
  };

  useEffect(() => {
    fetchPublishableKey();
  }, []);

  return (
    <StripeProvider
      publishableKey={publishableKey}
      merchantIdentifier="merchant.identifier" // required for Apple Pay
      urlScheme="your-url-scheme" // required for 3D Secure and bank redirects
    >
      {/* Your app code here */}
    </StripeProvider>
  );
}
```

> Use your API [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Create or retrieve a Customer [Server-side]

#### Accounts v2

To reuse a SEPA Direct Debit account for future payments, you must attach it to a customer-configured `Account`.

Create a customer-configured `Account` object when your customer creates an account with your business. Store the `Account` ID in your internal customer record so you can retrieve and use the saved payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  configuration: {
    customer: {},
  },
});
```

#### Customers v1

To reuse a SEPA Direct Debit account for future payments, you must attach it to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a `Customer` object when your customer creates an account with your business. Store the `Customer` ID in your internal customer record so you can retrieve and use the saved payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create();
```

## Create a PaymentIntent [Server-side] [Client-side]

### Server-side

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage. First, create a `PaymentIntent` on your server and specify the amount to collect and the `eur` currency. (SEPA Direct Debit doesn’t support other currencies.) If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `sepa_debit` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntents`.

To save the SEPA Direct Debit account for reuse, set the [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) parameter to `off_session`. SEPA Direct Debit only accepts an `off_session` value for this parameter.

#### Accounts v2

Specify the ID of the `Account` in the `customer_account` parameter.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'eur',
  setup_future_usage: 'off_session',
  customer_account: "{{ACCOUNT_ID}}",
  payment_method_types: ["sepa_debit"],
  metadata: {
    integration_check: 'sepa_debit_accept_a_payment',
  },
});
```

#### Customers v1

Specify the ID of the `Customer` in the `customer` parameter.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'eur',
  setup_future_usage: 'off_session',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ["sepa_debit"],
  metadata: {
    integration_check: 'sepa_debit_accept_a_payment',
  },
});
```

### Client-side

On the client, request a PaymentIntent from your server and store its *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)).

```javascript
const fetchPaymentIntentClientSecret = async () => {
  const response = await fetch(`${API_URL}/create-payment-intent`, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      email,
      currency: 'eur',
      payment_method_types: ["sepa_debit"],
    }),
  });
  const { clientSecret, error } = await response.json();

  return { clientSecret, error };
};
```

## Collect payment method details and mandate acknowledgment [Client-side]

Collect the customer’s IBAN in your payment form and display the following standard authorization text for your customer to implicitly sign the mandate.

Display the following standard authorization text for your customer to implicitly sign the mandate.

Replace *Rocket Rides* with your company name.

#### de

Durch Angabe Ihrer Zahlungsinformationen und der Bestätigung der vorliegenden Zahlung ermächtigen Sie (A) und Stripe, unseren Zahlungsdienstleister, Ihrem Kreditinstitut Anweisungen zur Belastung Ihres Kontos zu erteilen, und (B) Ihr Kreditinstitut, Ihr Konto gemäß diesen Anweisungen zu belasten. Im Rahmen Ihrer Rechte haben Sie, entsprechend den Vertragsbedingungen mit Ihrem Kreditinstitut, Anspruch auf eine Rückerstattung von Ihrem Kreditinstitut. Eine Rückerstattung muss innerhalb von 8 Wochen ab dem Tag, an dem Ihr Konto belastet wurde, geltend gemacht werden. Eine Erläuterung Ihrer Rechte können Sie von Ihrem Kreditinstitut anfordern. Sie erklären sich einverstanden, Benachrichtigungen über künftige Belastungen bis spätestens 2 Tage vor dem Buchungsdatum zu erhalten.

#### en

By providing your payment information and confirming this payment, you authorise (A) and Stripe, our payment service provider, to send instructions to your bank to debit your account and (B) your bank to debit your account in accordance with those instructions. As part of your rights, you’re entitled to a refund from your bank under the terms and conditions of your agreement with your bank. A refund must be claimed within 8 weeks starting from the date on which your account was debited. Your rights are explained in a statement that you can obtain from your bank. You agree to receive notifications for future debits up to 2 days before they occur.

#### es

Al proporcionar sus datos de pago y confirmar este pago, usted autoriza a (A) y Stripe, nuestro proveedor de servicios de pago, a enviar instrucciones a su banco para realizar un débito en su cuenta y (B) a su banco a realizar un cargo en su cuenta de conformidad con dichas instrucciones. Como parte de sus derechos, usted tiene derecho a un reembolso de su banco conforme a los términos y condiciones del contrato con su banco. El reembolso debe reclamarse en un plazo de 8 semanas a partir de la fecha en la que se haya efectuado el cargo en su cuenta. Sus derechos se explican en un extracto que puede obtener en su banco. Usted acepta recibir notificaciones de futuros débitos hasta 2 días antes de que se produzcan.

#### fi

Antamalla maksutiedot ja vahvistamalla tämän maksun, valtuutat (A) ja Stripen, maksupalveluntarjoajamme, lähettämään ohjeet pankille tilisi veloittamiseksi ja (B) pankkisi veloittamaan tiliäsi kyseisten ohjeiden mukaisesti. Oikeuksiesi mukaisesti olet oikeutettu maksun palautukseen pankilta, kuten heidän kanssaan tekemässäsi sopimuksessa ja sen ehdoissa on kuvattu. Maksun palautus on lunastettava 8 viikon aikana alkaen päivästä, jolloin tiliäsi veloitettiin. Oikeutesi on selitetty pankilta saatavissa olevassa lausunnossa. Hyväksyt vastaanottamaan ilmoituksia tulevista veloituksista jopa kaksi päivää ennen niiden tapahtumista.

#### fr

En fournissant vos informations de paiement et en confirmant ce paiement, vous autorisez (A) et Stripe, notre prestataire de services de paiement et/ou PPRO, son prestataire de services local, à envoyer des instructions à votre banque pour débiter votre compte et (B) votre banque à débiter votre compte conformément à ces instructions. Vous avez, entre autres, le droit de vous faire rembourser par votre banque selon les modalités et conditions du contrat conclu avec votre banque. La demande de remboursement doit être soumise dans un délai de 8 semaines à compter de la date à laquelle votre compte a été débité. Vos droits sont expliqués dans une déclaration disponible auprès de votre banque. Vous acceptez de recevoir des notifications des débits à venir dans les 2 jours précédant leur réalisation.

#### it

Fornendo i dati di pagamento e confermando il pagamento, l’utente autorizza (A) e Stripe, il fornitore del servizio di pagamento locale, a inviare alla sua banca le istruzioni per eseguire addebiti sul suo conto e (B) la sua banca a effettuare addebiti conformemente a tali istruzioni. L’utente, fra le altre cose, ha diritto a un rimborso dalla banca, in base a termini e condizioni dell’accordo sottoscritto con l’istituto. Il rimborso va richiesto entro otto settimane dalla data dell’addebito sul conto. I diritti dell’utente sono illustrati in una comunicazione riepilogativa che è possibile richiedere alla banca. L’utente accetta di ricevere notifiche per i futuri addebiti fino a due giorni prima che vengano effettuati.

#### nl

Door je betaalgegevens door te geven en deze betaling te bevestigen, geef je (A) en Stripe, onze betaaldienst, toestemming om instructies naar je bank te verzenden om het bedrag van je rekening af te schrijven, en (B) geef je je bank toestemming om het bedrag van je rekening af te schrijven conform deze aanwijzingen. Als onderdeel van je rechten kom je in aanmerking voor een terugbetaling van je bank conform de voorwaarden van je overeenkomst met de bank. Je moet terugbetalingen binnen acht weken claimen vanaf de datum waarop het bedrag is afgeschreven van je rekening. Je rechten worden toegelicht in een overzicht dat je bij de bank kunt opvragen. Je gaat ermee akkoord meldingen te ontvangen voor toekomstige afschrijvingen tot twee dagen voordat deze plaatsvinden.

​​Setting up a payment method or confirming a PaymentIntent creates the accepted mandate. As the customer has implicitly signed the mandate, you must communicate these terms in your form or through email.

```javascript
export default function SepaPaymentScreen() {
  const [email, setEmail] = useState("");
  const [iban, setIban] = useState("");

  return (
    <Screen>
      <TextInput
        placeholder="E-mail"
        keyboardType="email-address"
        onChange={(value) => setEmail(value.nativeEvent.text)}
        style={styles.input}
      />
      <TextInput
        placeholder="Iban"
        onChange={(value) => setIban(value.nativeEvent.text.toLowerCase())}
        style={styles.input}
      />
      <Button
        variant="primary"
        onPress={handlePayPress}
        title="Save IBAN"
        loading={loading}
      />
    </Screen>
  );
}
```

## Submit the payment to Stripe [Client-side]

Retrieve the client secret from the PaymentIntent you created and call `confirmPayment`.

The client secret should be handled carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

> `addressCountry` and `addressLine1` must be provided in the `billingDetails` for IBANs with the following country codes: AD, PF, TF, GI, GB, GG, VA, IM, JE, MC, NC, BL, PM, SM, CH, WF. See the [React Native SDK reference](https://stripe.dev/stripe-react-native/api-reference/interfaces/Address.html) for a complete list of address fields.

```javascript
export default function SepaPaymentScreen() {
  const [iban, setIban] = useState('');
  const {confirmPayment, loading} = useConfirmPayment();

  const handlePayPress = async () => {
    const {
      clientSecret,
      error: clientSecretError,
    } = await fetchPaymentIntentClientSecret();

    if (clientSecretError) {
      Alert.alert(`Error`, clientSecretError);
      return;
    }

    const billingDetails: PaymentMethodCreateParams.BillingDetails = {
      name: 'Jenny Rosen',
      email: 'jenny.rosen@example.com',
    };

    const {error, paymentIntent} = await confirmPayment(clientSecret, {
      paymentMethodType: 'SepaDebit',
      paymentMethodData: {
        billingDetails,
        iban,
      },
    });

    if (error) {
      Alert.alert(`Error code: ${error.code}`, error.message);
    } else if (paymentIntent) {
      if (paymentIntent.status === PaymentIntents.Status.Processing) {
        Alert.alert(
          'Processing',
          `The debit has been successfully submitted and is now processing.`,
        );
      } else if (paymentIntent.status === PaymentIntents.Status.Succeeded) {
        Alert.alert(
          'Success',
          `The payment was confirmed successfully! currency: ${paymentIntent.currency}`,
        );
      } else {
        Alert.alert('Payment status:', paymentIntent.status);
      }
    }
  };

  return <Screen>{/* ... */}</Screen>;
}
```

## Confirm the PaymentIntent succeeded

SEPA Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, so funds aren’t immediately available. When the payment has been submitted successfully, the PaymentIntent status is updated from `requires_confirmation` to `processing`. After the payment has succeeded, the PaymentIntent status is updated from `processing` to `succeeded`.

The following events are sent when the PaymentIntent status is updated:

| Event                           | Description                                                  | Next steps                                                                                  |
| ------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| `payment_intent.processing`     | The customer’s payment was submitted to Stripe successfully. | Wait for the initiated payment to succeed or fail.                                          |
| `payment_intent.succeeded`      | The customer’s payment succeeded.                            | Fulfill the goods or services that the customer purchased.                                  |
| `payment_intent.payment_failed` | The customer’s payment was declined.                         | Contact the customer through email or push notification and request another payment method. |

We recommend [using webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the charge has succeeded and to notify the customer that the payment is complete.

Note that because [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) and [customer](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) were set, the PaymentMethod will be attached to the Customer object once the payment enters the `processing` state. This attachment happens regardless of whether payment eventually succeeds or fails.

## Test the integration

You can test your form using the [SEPA Direct Debit test account numbers](https://docs.stripe.com/testing.md?payment-method=sepa-direct-debit) with your [confirmPayment](https://stripe.dev/stripe-react-native/api-reference/functions/confirmPayment.html) request. The payment method details are successfully collected for each IBAN, but exhibit different behavior when charged.

## Optional: Customize mandate references with a prefix

You can customize SEPA Direct Debit mandate references to simplify mandate identification. To do this, provide the optional `payment_method_options.sepa_debit.mandate_options.reference_prefix` value. We add the `reference_prefix` to the beginning of a unique sequence to ensure the entire reference remains unique.

The `reference_prefix` must meet these requirements:

- Maximum length: 12 characters
- Must begin with a number or an uppercase letter
- Allowed characters:
  - Uppercase letters
  - Numbers
  - Spaces
  - Special characters: `.`, `/`, `&`, `-`, `_`
- Can’t begin with `STRIPE`

Include any desired delimiter in the prefix, as we don’t add one by default. We trim trailing spaces to a maximum of one space. With a valid prefix, the resulting reference is always 24 characters long.

#### Payment Intent

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  currency: 'eur',
  amount: 100,
  payment_method_types: ["sepa_debit"],
  payment_method_options: {
    sepa_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

#### Setup Intent

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["sepa_debit"],
  payment_method_options: {
    sepa_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

#### Checkout Session in Payment Mode

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'payment',
  currency: 'eur',
  line_items: [
    {
      price_data: {
        currency: 'eur',
        product_data: {
          name: "Llama",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  payment_method_types: ["sepa_debit"],
  payment_method_options: {
    sepa_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

#### Checkout Session in Setup Mode

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'setup',
  payment_method_types: ["sepa_debit"],
  payment_method_options: {
    sepa_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

The generated reference looks like `EX4MPL3-19CNCI920C2M02O3`.

| Error Code                                     | Message                                                                                                                                                                                                 |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `invalid_sepa_mandate_reference_prefix_format` | The `reference_prefix` must be at most 12 characters long and can only contain uppercase letters, numbers, spaces, or the special characters `/`, `_`, `-`, `&`, and `.`. It can’t begin with `STRIPE`. |

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/sepa-debit/accept-a-payment?payment-ui=elements.

> When processing SEPA Direct Debit payments using the Stripe [Creditor ID](https://docs.stripe.com/payments/sepa-debit.md#creditor-identifiers-creditor-id), we recommend you use the [prebuilt checkout page](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md?platform=checkout) to collect SEPA Direct Debit mandates.

Accepting SEPA Direct Debit payments on your website consists of creating an object to track a payment, collecting payment method information and mandate acknowledgement, and submitting the payment to Stripe for processing. Stripe uses this payment object, the PaymentIntent, to track and handle all the states of the payment until the payment completes.

You can also set up a SEPA Direct Debit *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) by having your customer authenticate their bank details with [Bancontact](https://docs.stripe.com/payments/bancontact/save-during-payment.md) or [iDEAL](https://docs.stripe.com/payments/ideal/save-during-payment.md).

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a Customer [Server-side]

#### Accounts v2

To reuse a SEPA Direct Debit account for future payments, you must attach it to a customer-configured `Account`.

Create a customer-configured `Account` object when your customer creates an account with your business. Associating the ID of the `Account` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  configuration: {
    customer: {},
  },
});
```

#### Customers v1

To reuse a SEPA Direct Debit account for future payments, you must attach it to a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments).

Create a `Customer` object when your customer creates an account with your business. Associating the ID of the `Customer` object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create();
```

## Create a PaymentIntent [Server-side]

A [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage. First, create a PaymentIntent on your server and specify the amount to collect and the `eur` currency (SEPA Direct Debit doesn’t support other currencies). If you already have an integration using the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), add `sepa_debit` to the list of [payment method types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_types) for your `PaymentIntents`.

To save the SEPA Direct Debit account for reuse, set the [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) parameter to `off_session`. SEPA Direct Debit only accepts an `off_session` value for this parameter.

#### Accounts v2

Specify the ID of the `Account` in the `customer_account` parameter.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'eur',
  setup_future_usage: 'off_session',
  customer_account: "{{ACCOUNT_ID}}",
  payment_method_types: ["sepa_debit"],
  metadata: {
    integration_check: 'sepa_debit_accept_a_payment',
  },
});
```

#### Customers v1

Specify the ID of the `Customer` in the `customer` parameter.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1099,
  currency: 'eur',
  setup_future_usage: 'off_session',
  customer: '{{CUSTOMER_ID}}',
  payment_method_types: ["sepa_debit"],
  metadata: {
    integration_check: 'sepa_debit_accept_a_payment',
  },
});
```

## Collect payment method details and mandate acknowledgment [Client-side]

You’re ready to collect payment information on the client with [Stripe Elements](https://docs.stripe.com/payments/elements.md). Elements is a set of prebuilt UI components for collecting payment details.

A Stripe Element contains an iframe that securely sends the payment information to Stripe over an HTTPS connection. The checkout page address must also start with https:// rather than http:// for your integration to work.

You can test your integration without using HTTPS. [Enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

### Set up Stripe Elements

#### HTML + JS

Stripe Elements is automatically available as a feature of Stripe.js. Include the Stripe.js script on your payment page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Submit Payment</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Elements with the following JavaScript on your payment page. Pass the `mode`, `currency`, and `amount` to enable the Payment Element to collect SEPA Direct Debit payment details:

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
const options = {
  mode: 'payment',
  currency: 'eur',
  amount: 1099,
  // Automatically save the payment method for future payments
  setup_future_usage: 'off_session',
};
const elements = stripe.elements(options);
```

### Add the Payment Element

The Payment Element needs a place to live in your payment form. Create an empty DOM node (container) with a unique ID in your payment form. The Payment Element automatically displays the SEPA Direct Debit form and mandate acceptance text when SEPA Debit is enabled

```html
<form action="/charge" method="post" id="payment-form">
  <div id="payment-element">
    <!-- The Payment Element will be inserted here. -->
  </div>

  <!-- Add the client_secret from the PaymentIntent as a data attribute   -->
  <button id="submit-button" data-secret="{{CLIENT_SECRET}}">
    Submit Payment
  </button>

  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>
</form>
```

When the form loads, [create an instance](https://docs.stripe.com/js/elements_object/create_element?type=payment) of the Payment Element and mount it to the Element container. The Payment Element automatically collects the customer’s name, email, IBAN, and displays the mandate acceptance text:

```javascript
// Create and mount the Payment Element
const paymentElement = elements.create('payment');
paymentElement.mount("#payment-element");
```

#### React

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry:

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

Pass the payment details (`mode`, `currency`, `amount`) to the [Elements Provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider):

```jsx
import React from "react";
import { loadStripe } from "@stripe/stripe-js";
import { Elements } from "@stripe/react-stripe-js";
import CheckoutForm from "./CheckoutForm";

// Make sure to call `loadStripe` outside of a component's render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

export default function App() {
  const options = {
    mode: 'payment',
    currency: 'eur',
    amount: 1099,
    // Automatically save the payment method for future payments
    setup_future_usage: 'off_session',
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm />
    </Elements>
  );
}
```

Create a checkout form component that renders the [PaymentElement](https://docs.stripe.com/sdks/stripejs-react.md#element-components):

```jsx
import React from "react";
import { PaymentElement } from "@stripe/react-stripe-js";

export default function CheckoutForm() {
  return (
    <form id="payment-form">
      <PaymentElement />
      <button type="submit">Submit Payment</button>
      <div id="error-message" role="alert"></div>
    </form>
  );
}
```

## Submit the payment to Stripe [Client-side]

Rather than sending the entire PaymentIntent object to the client, use its [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) from [step 3](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md#web-create-payment-intent). This is different from your API keys that authenticate Stripe API requests.

The client secret should still be handled carefully because it can complete the charge. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

#### HTML + JS

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to complete the payment when the user submits the form. The Payment Element automatically collects the customer’s name, email, IBAN, and handles mandate acceptance:

```javascript
const form = document.getElementById('payment-form');
const submitButton = document.getElementById('submit-button');
const clientSecret = submitButton.dataset.secret;

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const { error } = await stripe.confirmPayment({
    elements,
    clientSecret,
    confirmParams: {
      return_url: 'https://example.com/order/complete',
    },
  });

  if (error) {
    // Show error to your customer (for example, payment details incomplete)
    const errorMessage = document.getElementById('error-message');
    errorMessage.textContent = error.message;
  } else {
    // Your customer will be redirected to your `return_url`.
  }
});
```

#### React

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to complete the payment when the user submits the form. The Payment Element automatically collects and validates all required information.

Update your `CheckoutForm` component to handle form submission with the [useStripe](https://docs.stripe.com/sdks/stripejs-react.md#usestripe-hook) and [useElements](https://docs.stripe.com/sdks/stripejs-react.md#useelements-hook) hooks:

```jsx
import React, { useState } from "react";
import {
  useStripe,
  useElements,
  PaymentElement,
} from "@stripe/react-stripe-js";

export default function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();
  const [errorMessage, setErrorMessage] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    const { error } = await stripe.confirmPayment({
      elements,
      confirmParams: {
        return_url: 'https://example.com/order/complete',
      },
    });

    if (error) {
      // Show error to your customer (for example, payment details incomplete)
      setErrorMessage(error.message);
    } else {
      // Your customer will be redirected to your `return_url`.
    }
  };

  return (
    <form id="payment-form" onSubmit={handleSubmit}>
      <PaymentElement />
      <button type="submit" disabled={!stripe}>
        Submit Payment
      </button>
      {errorMessage && (
        <div id="error-message" role="alert">
          {errorMessage}
        </div>
      )}
    </form>
  );
}
```

## Confirm the PaymentIntent succeeded

SEPA Direct Debit is a [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method, so funds aren’t immediately available. When the payment has been submitted successfully, the `PaymentIntent` status is updated from `requires_confirmation` to `processing`. After the payment has succeeded, the PaymentIntent status is updated from `processing` to `succeeded`.

The following events are sent when the PaymentIntent status is updated:

| Event                           | Description                                                  | Next steps                                                                                  |
| ------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| `payment_intent.processing`     | The customer’s payment was submitted to Stripe successfully. | Wait for the initiated payment to succeed or fail.                                          |
| `payment_intent.succeeded`      | The customer’s payment succeeded.                            | Fulfill the goods or services that the customer purchased.                                  |
| `payment_intent.payment_failed` | The customer’s payment was declined.                         | Contact the customer through email or push notification and request another payment method. |

We recommend [using webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status.md#webhooks) to *confirm* (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) the charge has succeeded and to notify the customer that the payment is complete.

#### Accounts v2

Because [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) and [customer_account](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer_account) are set, Stripe attaches the `PaymentMethod` to the `Account` object when the payment enters the `processing` state. This attachment happens whether the payment later succeeds or fails.

#### Customers v1

Because [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage) and [customer](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-customer) are set, Stripe attaches the `PaymentMethod` to the `Customer` object when the payment enters the `processing` state. This attachment happens whether the payment later succeeds or fails.

## Test the integration

Stripe provides several test numbers you can use to make sure your integration is ready for production. Use the SEPA Direct Debit test numbers when testing your Checkout integration with SEPA Direct Debit.

##### Test IBANs

Use these test IBANs with the Payment Element to test your SEPA Direct Debit integration. The Payment Element automatically validates the IBAN and displays the mandate when you enter one of these test values.

### AT

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| AT611904300234573201 | pm_success_at                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| AT321904300235473204 | pm_successDelayed_at                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| AT861904300235473202 | pm_failed_at                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| AT051904300235473205 | pm_failedDelayed_at                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| AT591904300235473203 | pm_disputed_at                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| AT981904300000343434 | pm_exceedsWeeklyVolumeLimit_at      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| AT601904300000121212 | pm_exceedsWeeklyTransactionLimit_at | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| AT981904300002222227 | pm_insufficientFunds_at             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### BE

| Account Number   | Token                               | Description                                                                                                                                          |
| ---------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| BE62510007547061 | pm_success_be                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| BE78510007547064 | pm_successDelayed_be                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| BE68539007547034 | pm_failed_be                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| BE51510007547065 | pm_failedDelayed_be                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| BE08510007547063 | pm_disputed_be                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| BE90510000343434 | pm_exceedsWeeklyVolumeLimit_be      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| BE52510000121212 | pm_exceedsWeeklyTransactionLimit_be | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| BE90510002222227 | pm_insufficientFunds_be             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### HR

| Account Number        | Token                               | Description                                                                                                                                          |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| HR7624020064583467589 | pm_success_hr                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| HR6323600002337876649 | pm_successDelayed_hr                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| HR2725000096983499248 | pm_failed_hr                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| HR6723600004878117427 | pm_failedDelayed_hr                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| HR8724840081455523553 | pm_disputed_hr                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| HR7424020060000343434 | pm_exceedsWeeklyVolumeLimit_hr      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| HR3624020060000121212 | pm_exceedsWeeklyTransactionLimit_hr | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| HR7424020060002222227 | pm_insufficientFunds_hr             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### EE

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| EE382200221020145685 | pm_success_ee                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| EE222200221020145682 | pm_successDelayed_ee                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| EE762200221020145680 | pm_failed_ee                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| EE922200221020145683 | pm_failedDelayed_ee                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| EE492200221020145681 | pm_disputed_ee                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| EE672200000000343434 | pm_exceedsWeeklyVolumeLimit_ee      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| EE292200000000121212 | pm_exceedsWeeklyTransactionLimit_ee | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| EE672200000002222227 | pm_insufficientFunds_ee             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### FI

| Account Number     | Token                               | Description                                                                                                                                          |
| ------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| FI2112345600000785 | pm_success_fi                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| FI3712345600000788 | pm_successDelayed_fi                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| FI9112345600000786 | pm_failed_fi                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| FI1012345600000789 | pm_failedDelayed_fi                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| FI6412345600000787 | pm_disputed_fi                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| FI6712345600343434 | pm_exceedsWeeklyVolumeLimit_fi      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| FI2912345600121212 | pm_exceedsWeeklyTransactionLimit_fi | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| FI6712345602222227 | pm_insufficientFunds_fi             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### FR

| Account Number              | Token                               | Description                                                                                                                                          |
| --------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| FR1420041010050500013M02606 | pm_success_fr                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| FR3020041010050500013M02609 | pm_successDelayed_fr                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| FR8420041010050500013M02607 | pm_failed_fr                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| FR7920041010050500013M02600 | pm_failedDelayed_fr                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| FR5720041010050500013M02608 | pm_disputed_fr                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| FR9720041010050000000343434 | pm_exceedsWeeklyVolumeLimit_fr      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| FR5920041010050000000121212 | pm_exceedsWeeklyTransactionLimit_fr | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| FR9720041010050000002222227 | pm_insufficientFunds_fr             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### DE

| Account Number         | Token                               | Description                                                                                                                                          |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| DE89370400440532013000 | pm_success_de                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| DE08370400440532013003 | pm_successDelayed_de                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| DE62370400440532013001 | pm_failed_de                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| DE78370400440532013004 | pm_failedDelayed_de                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| DE35370400440532013002 | pm_disputed_de                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| DE65370400440000343434 | pm_exceedsWeeklyVolumeLimit_de      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| DE27370400440000121212 | pm_exceedsWeeklyTransactionLimit_de | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| DE65370400440002222227 | pm_insufficientFunds_de             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### GI

| Account Number          | Token                               | Description                                                                                                                                          |
| ----------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| GI60MPFS599327643783385 | pm_success_gi                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| GI08RRNW626436291644533 | pm_successDelayed_gi                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| GI41SAFA461293238477751 | pm_failed_gi                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| GI50LROG772261344693297 | pm_failedDelayed_gi                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| GI26KJBC361883934534696 | pm_disputed_gi                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| GI14NWBK000000000343434 | pm_exceedsWeeklyVolumeLimit_gi      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| GI73NWBK000000000121212 | pm_exceedsWeeklyTransactionLimit_gi | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| GI14NWBK000000002222227 | pm_insufficientFunds_gi             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### IE

| Account Number         | Token                               | Description                                                                                                                                          |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| IE29AIBK93115212345678 | pm_success_ie                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| IE24AIBK93115212345671 | pm_successDelayed_ie                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| IE02AIBK93115212345679 | pm_failed_ie                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| IE94AIBK93115212345672 | pm_failedDelayed_ie                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| IE51AIBK93115212345670 | pm_disputed_ie                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| IE10AIBK93115200343434 | pm_exceedsWeeklyVolumeLimit_ie      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| IE69AIBK93115200121212 | pm_exceedsWeeklyTransactionLimit_ie | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| IE10AIBK93115202222227 | pm_insufficientFunds_ie             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### LI

| Account Number        | Token                               | Description                                                                                                                                          |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| LI0508800636123378777 | pm_success_li                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| LI4408800387787111369 | pm_successDelayed_li                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| LI1208800143823175626 | pm_failed_li                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| LI4908800356441975566 | pm_failedDelayed_li                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| LI7708800125525347723 | pm_disputed_li                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| LI2408800000000343434 | pm_exceedsWeeklyVolumeLimit_li      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| LI8308800000000121212 | pm_exceedsWeeklyTransactionLimit_li | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| LI2408800000002222227 | pm_insufficientFunds_li             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### LT

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| LT121000011101001000 | pm_success_lt                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| LT281000011101001003 | pm_successDelayed_lt                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| LT821000011101001001 | pm_failed_lt                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| LT981000011101001004 | pm_failedDelayed_lt                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| LT551000011101001002 | pm_disputed_lt                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| LT591000000000343434 | pm_exceedsWeeklyVolumeLimit_lt      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| LT211000000000121212 | pm_exceedsWeeklyTransactionLimit_lt | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| LT591000000002222227 | pm_insufficientFunds_lt             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### LU

| Account Number       | Token                               | Description                                                                                                                                          |
| -------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| LU280019400644750000 | pm_success_lu                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| LU440019400644750003 | pm_successDelayed_lu                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| LU980019400644750001 | pm_failed_lu                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| LU170019400644750004 | pm_failedDelayed_lu                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| LU710019400644750002 | pm_disputed_lu                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| LU900010000000343434 | pm_exceedsWeeklyVolumeLimit_lu      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| LU520010000000121212 | pm_exceedsWeeklyTransactionLimit_lu | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| LU900010000002222227 | pm_insufficientFunds_lu             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### NL

| Account Number     | Token                               | Description                                                                                                                                          |
| ------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| NL39RABO0300065264 | pm_success_nl                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| NL55RABO0300065267 | pm_successDelayed_nl                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| NL91ABNA0417164300 | pm_failed_nl                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| NL28RABO0300065268 | pm_failedDelayed_nl                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| NL82RABO0300065266 | pm_disputed_nl                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| NL27RABO0000343434 | pm_exceedsWeeklyVolumeLimit_nl      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| NL86RABO0000121212 | pm_exceedsWeeklyTransactionLimit_nl | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| NL55RABO0300065267 | pm_insufficientFunds_nl             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### NO

| Account Number  | Token                               | Description                                                                                                                                          |
| --------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| NO9386011117947 | pm_success_no                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| NO8886011117940 | pm_successDelayed_no                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| NO6686011117948 | pm_failed_no                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| NO6186011117941 | pm_failedDelayed_no                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| NO3986011117949 | pm_disputed_no                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| NO0586010343434 | pm_exceedsWeeklyVolumeLimit_no      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| NO0586010343434 | pm_exceedsWeeklyTransactionLimit_no | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| NO0586012222227 | pm_insufficientFunds_no             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### PT

| Account Number            | Token                               | Description                                                                                                                                          |
| ------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| PT50000201231234567890154 | pm_success_pt                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| PT66000201231234567890157 | pm_successDelayed_pt                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| PT23000201231234567890155 | pm_failed_pt                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| PT39000201231234567890158 | pm_failedDelayed_pt                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| PT93000201231234567890156 | pm_disputed_pt                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| PT05000201230000000343434 | pm_exceedsWeeklyVolumeLimit_pt      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| PT64000201230000000121212 | pm_exceedsWeeklyTransactionLimit_pt | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| PT05000201230000002222227 | pm_insufficientFunds_pt             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### ES

| Account Number           | Token                               | Description                                                                                                                                          |
| ------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| ES0700120345030000067890 | pm_success_es                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| ES2300120345030000067893 | pm_successDelayed_es                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| ES9121000418450200051332 | pm_failed_es                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| ES9300120345030000067894 | pm_failedDelayed_es                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| ES5000120345030000067892 | pm_disputed_es                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| ES1700120345000000343434 | pm_exceedsWeeklyVolumeLimit_es      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| ES7600120345000000121212 | pm_exceedsWeeklyTransactionLimit_es | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| ES1700120345000002222227 | pm_insufficientFunds_es             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### SE

| Account Number           | Token                               | Description                                                                                                                                          |
| ------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| SE3550000000054910000003 | pm_success_se                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| SE5150000000054910000006 | pm_successDelayed_se                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| SE0850000000054910000004 | pm_failed_se                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| SE2450000000054910000007 | pm_failedDelayed_se                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| SE7850000000054910000005 | pm_disputed_se                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| SE2850000000000000343434 | pm_exceedsWeeklyVolumeLimit_se      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| SE8750000000000000121212 | pm_exceedsWeeklyTransactionLimit_se | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| SE2850000000000002222227 | pm_insufficientFunds_se             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### CH

| Account Number        | Token                               | Description                                                                                                                                          |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| CH9300762011623852957 | pm_success_ch                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| CH8656663438253651553 | pm_successDelayed_ch                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| CH5362200119938136497 | pm_failed_ch                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| CH1843597160341964438 | pm_failedDelayed_ch                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| CH1260378413965193069 | pm_disputed_ch                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| CH1800762000000343434 | pm_exceedsWeeklyVolumeLimit_ch      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| CH7700762000000121212 | pm_exceedsWeeklyTransactionLimit_ch | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| CH1800762000002222227 | pm_insufficientFunds_ch             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

### GB

| Account Number         | Token                               | Description                                                                                                                                          |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| GB82WEST12345698765432 | pm_success_gb                       | The PaymentIntent status transitions from `processing` to `succeeded`.                                                                               |
| GB98WEST12345698765435 | pm_successDelayed_gb                | The PaymentIntent status transitions from `processing` to `succeeded` after at least three minutes.                                                  |
| GB55WEST12345698765433 | pm_failed_gb                        | The PaymentIntent status transitions from `processing` to `requires_payment_method`.                                                                 |
| GB71WEST12345698765436 | pm_failedDelayed_gb                 | The PaymentIntent status transitions from `processing` to `requires_payment_method` after at least three minutes.                                    |
| GB28WEST12345698765434 | pm_disputed_gb                      | The PaymentIntent status transitions from `processing` to `succeeded`, but a dispute is immediately created.                                         |
| GB70WEST12345600343434 | pm_exceedsWeeklyVolumeLimit_gb      | The payment fails with a `charge_exceeds_source_limit` failure code due to payment amount causing account to exceed its weekly payment volume limit. |
| GB32WEST12345600121212 | pm_exceedsWeeklyTransactionLimit_gb | The payment fails with a `charge_exceeds_weekly_limit` failure code due to payment amount exceeding account's transaction volume limit.              |
| GB70WEST12345602222227 | pm_insufficientFunds_gb             | The payment fails with an `insufficient_funds` failure code.                                                                                         |

> The Payment Element automatically validates the IBAN and other payment details as the customer types. Error messages are displayed inline within the Payment Element, so you don’t need to handle validation manually.

## Optional: Configure customer debit date

You can control the date that Stripe debits a customer’s bank account using the [target date](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_options-sepa_debit-target_date). The target date must be at least three days in the future and no more than 15 days from the current date.

The target date schedules money to leave the customer’s account on the target date. You can [cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel.md) created with a target date up to three business days before the configured date.

Target dates that meet one of the following criteria delay the debit until next available business day:

- Target date falls on a weekend, a bank holiday, or other non-business day.
- Target date is fewer than three business days in the future.

This parameter operates on a best-effort basis. Each customer’s bank might process debits on different dates, depending on local bank holidays or other reasons.

## Optional: Customize mandate references with a prefix

You can customize SEPA Direct Debit mandate references to simplify mandate identification. To do this, provide the optional `payment_method_options.sepa_debit.mandate_options.reference_prefix` value. We add the `reference_prefix` to the beginning of a unique sequence to ensure the entire reference remains unique.

The `reference_prefix` must meet these requirements:

- Maximum length: 12 characters
- Must begin with a number or an uppercase letter
- Allowed characters:
  - Uppercase letters
  - Numbers
  - Spaces
  - Special characters: `.`, `/`, `&`, `-`, `_`
- Can’t begin with `STRIPE`

Include any desired delimiter in the prefix, as we don’t add one by default. We trim trailing spaces to a maximum of one space. With a valid prefix, the resulting reference is always 24 characters long.

#### Payment Intent

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  currency: 'eur',
  amount: 100,
  payment_method_types: ["sepa_debit"],
  payment_method_options: {
    sepa_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

#### Setup Intent

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["sepa_debit"],
  payment_method_options: {
    sepa_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

#### Checkout Session in Payment Mode

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'payment',
  currency: 'eur',
  line_items: [
    {
      price_data: {
        currency: 'eur',
        product_data: {
          name: "Llama",
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  payment_method_types: ["sepa_debit"],
  payment_method_options: {
    sepa_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

#### Checkout Session in Setup Mode

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const session = await stripe.checkout.sessions.create({
  mode: 'setup',
  payment_method_types: ["sepa_debit"],
  payment_method_options: {
    sepa_debit: {
      mandate_options: {
        reference_prefix: 'EX4MPL3-',
      },
    },
  },
});
```

The generated reference looks like `EX4MPL3-19CNCI920C2M02O3`.

| Error Code                                     | Message                                                                                                                                                                                                 |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `invalid_sepa_mandate_reference_prefix_format` | The `reference_prefix` must be at most 12 characters long and can only contain uppercase letters, numbers, spaces, or the special characters `/`, `_`, `-`, `&`, and `.`. It can’t begin with `STRIPE`. |

## See also

- [Save SEPA Direct Debit details for future payments](https://docs.stripe.com/payments/sepa-debit/set-up-payment.md)
- [Connect payments](https://docs.stripe.com/connect/charges.md)
