<!-- Source URL: https://docs.stripe.com/payments/payment-methods/payment-method-connect-support -->
<!-- Fetched: 2026-05-08 -->

# Payment method support for platforms and marketplaces

Learn about requirements and limitations when enabling payment methods for platforms and marketplaces.

When using [Connect](https://docs.stripe.com/connect.md) for platforms and marketplaces, different payment methods are available depending on factors such as country location, business type, account type, and charge type. Select a payment method to learn about its level of Connect support.

For more information about enabling payment methods with Connect, refer to the following:

- [Account capabilities](https://docs.stripe.com/connect/account-capabilities.md#payment-methods)
- [Adding payment method capabilities](https://docs.stripe.com/connect/payment-methods.md)
- [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md)

## Payment methods

#### Payment method - ACH Direct Debit

If you use _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you must take the following into consideration before you enable and use ACH Direct Debits.

### Request ACH Debit capabilities for your connected accounts

Set the `us_bank_account_ach_payments` capability to `active` on your platform account, and for any connected accounts you want to enable for ACH debits. You can also [request more account capabilities](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

> Stripe automatically refunds the application fee to your platform account when the [destination charge](https://docs.stripe.com/connect/charges.md#destination) for an ACH debit fails. Learn about [fees for failed payments](https://stripe.com/pricing/local-payment-methods#ach-direct-debit).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s bank statement. The charge type can also change:

- The _merchant of record_ (The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account) shown on the mandate
- The business shown on confirmation emails
- The business shown on microdeposit reminder emails

The merchant of record determines the Stripe account authorized to create payments with a particular [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md). To learn more about sharing this authorization across multiple connected accounts, see [PaymentMethod and Mandate cloning](https://docs.stripe.com/payments/payment-methods/payment-method-connect-support.md#payment-method-and-mandate-cloning).

| Charge type                                        | Descriptor taken from |
| -------------------------------------------------- | --------------------- |
| Direct                                             | Connected Account     |
| Destination                                        | Platform              |
| Separate charge and transfer                       | Platform              |
| Destination (with `on_behalf_of`)                  | Connected Account     |
| Separate charge and transfer (with `on_behalf_of`) | Connected Account     |

### PaymentMethod and mandate cloning

You can collect customer bank accounts on the platform account and [clone](https://docs.stripe.com/connect/direct-charges-multiple-accounts.md#clone-and-create-direct-charges) ACH Direct Debit payment methods. Cloning these methods allows you to save customer bank accounts for later use on connected accounts. When you clone ACH Direct Debit payment methods, Stripe duplicates the mandate authorization to the connected account, but we don’t send any new mandate confirmation emails.

> If a mandate is authorized for a PaymentIntent or SetupIntent [on_behalf_of](https://docs.stripe.com/connect/charges.md#on_behalf_of) a connected account, you can’t use that mandate with a different connected account.

When collecting a bank account that you intend to clone to connected accounts, you must communicate to the customer that their authorization extends to connected accounts on your platform. For example, you can communicate this message to a customer through the mandate terms. Failure to communicate this message to your customers could result in customer confusion and increase the risk of disputed payments.

### Connect and settlement

Settlement speed is generally controlled at the platform level. The table below shows a comprehensive view of settlement timing by account and charge type.

| Account Type                          | Direct Charges                                       | Destination Charges                                  | Separate Charges and Transfers              |
| ------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------- |
| **Standard with Platform Control**    | The platform controls the settlement speed.          | The platform controls the settlement speed.          | The platform controls the settlement speed. |
| **Standard without Platform Control** | The connected account controls the settlement speed. | The connected account controls the settlement speed. | The platform controls the settlement speed. |
| **Express**                           | The platform controls the settlement speed.          | The platform controls the settlement speed.          | The platform controls the settlement speed. |
| **Custom**                            | The platform controls the settlement speed.          | The platform controls the settlement speed.          | The platform controls the settlement speed. |

#### Payment method - Affirm

You can use [Stripe Connect](https://docs.stripe.com/connect.md) with Affirm to process payments on behalf of a connected account. _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) users can use Affirm with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate Charges and Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

### Request Affirm capability

You must turn on the Affirm payment method in [your platform settings](https://dashboard.stripe.com/settings/payment_methods) and [request](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting) the `affirm_payments` capability for your connected accounts that will accept Affirm payments.

### Set correct MCC

Stripe and Affirm rely on merchant category codes (MCC) to determine eligibility of the connected accounts against the Affirm [prohibited business categories](https://docs.stripe.com/payments/affirm.md#prohibited-and-restricted-business-categories). Make sure that you set [correct MCCs](https://docs.stripe.com/connect/setting-mcc.md) for your connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe.

### Merchant of record

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the merchant name that appears on Affirm’s website or app during the redirect. The merchant of record determines the Stripe account authorized to create payments with a particular [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md).

#### Payment method - Afterpay / Clearpay

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with Afterpay to process payments on behalf of a connected account. _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) users can use Afterpay with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate Charges and Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

Stripe and Afterpay rely on merchant category codes (MCC) to determine eligibility of the connected accounts against the Afterpay [prohibited business categories](https://docs.stripe.com/payments/payment-methods/payment-method-connect-support.md#prohibited-business-categories). Make sure that you set [correct MCCs](https://docs.stripe.com/connect/setting-mcc.md) for your connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe.

#### Payment method - Alipay

Alipay has partial [Connect](https://stripe.com/connect) support depending on the [charge type](https://docs.stripe.com/connect/charges.md).

| Destination charges | Separate charges and transfers | Direct charges    | `on_behalf_of`    |
| ------------------- | ------------------------------ | ----------------- | ----------------- |
| ✓ Supported         | ✓ Supported                    | ⚠ Private preview | ⚠ Private preview |

For connected accounts with standard Dashboard access, individual connected accounts can enable Alipay in the Dashboard.

For connected accounts without standard Dashboard access, the platform needs to request the `alipay_payments` capability. This is a private preview feature; contact Stripe Support to request access.

#### Payment method - Alma

Alma is available for online marketplaces using [Stripe Connect](https://stripe.com/connect). These online marketplaces include businesses such as Deliveroo and ManoMano that collect payments from customers, and later pay out to sub-accounts or service providers. Alma isn’t available for platforms that onboard other businesses and enable them to accept payments directly, such as Shopify or Squarespace.

> Online marketplaces need to submit an onboarding request from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) to get access to Alma. Stripe sends email updates about the progress of all requests, and the current status is also reflected on the [Payment methods settings page](https://dashboard.stripe.com/settings/payment_methods).

The following [Connect charges](https://docs.stripe.com/connect/charges.md) types, typically used by online marketplaces, are available to businesses using Alma.

| Destination charges | Separate charges and transfers | Direct charges | `on_behalf_of` |
| ------------------- | ------------------------------ | -------------- | -------------- |
| ✓ Supported         | ✓ Supported                    | ✓ Supported    | ✓ Supported    |

#### Payment method - Bank transfers

[Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) can be used with bank transfers to process payments on behalf of connected accounts. _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) platforms can use bank transfers with [any type of charges](https://docs.stripe.com/connect/charges.md#types).

The [on_behalf_of attribute](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-on_behalf_of) isn’t supported.

### Accepting bank transfer payments as the connected account

[Direct charges](https://docs.stripe.com/connect/direct-charges.md) require the connected account itself (not the platform) to have activated the bank transfers payment method—Connect platforms can use the [relevant bank transfers capability](https://docs.stripe.com/connect/account-capabilities.md#payment-methods) to determine whether this is the case for a connected account. [Standard Connect accounts](https://docs.stripe.com/connect/standard-accounts.md) can request the relevant capability from their Stripe Dashboard.

### Activation process

The process varies by country, but in general for bank transfer payments, the [required information](https://docs.stripe.com/connect/required-verification-information.md) is the same as what’s necessary to activate a Stripe account for payments. If the account doesn’t fulfill all the required information, the capability remains `inactive` with any issues highlighted on the [capability object](https://docs.stripe.com/api/capabilities/object.md) in the `requirements.currently_due` and `requirements.disabled_reason` fields until these issues have been addressed. After all the highlighted issues are resolved, the capability’s `status` changes to `active`, unless there are issues activating the account in general, in which case Stripe sends the Connect platform owner an email.

#### Payment method - Billie

If you use _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you must consider the following before you enable and use Billie.

### Request Billie capabilities for your connected accounts

Set the `billie_payments` capability to `active` on your platform account, and on any connected accounts you want to enable Billie for. You can also [request more account capabilities](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s banking application and confirmation emails.

| Charge type                                        | Descriptor taken from |
| -------------------------------------------------- | --------------------- |
| Direct                                             | Connected account     |
| Destination                                        | Platform              |
| Separate charge and transfer                       | Platform              |
| Destination (with `on_behalf_of`)                  | Connected account     |
| Separate charge and transfer (with `on_behalf_of`) | Connected account     |

To check or update your statement descriptor, go to your [account settings](https://docs.stripe.com/get-started/account/statement-descriptors.md). For Connect integrations, see [setting statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

#### Payment method - BLIK

If you use _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you must consider the following before you enable and use BLIK.

### Request BLIK capabilities for your connected accounts

Set the `blik_payments` capability to `active` on your platform account, and on any connected accounts you want to enable BLIK for. You can also [request more account capabilities](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s banking application and confirmation emails.

| Charge type                                        | Descriptor taken from |
| -------------------------------------------------- | --------------------- |
| Direct                                             | Connected Account     |
| Destination                                        | Platform              |
| Separate charge and transfer                       | Platform              |
| Destination (with `on_behalf_of`)                  | Connected Account     |
| Separate charge and transfer (with `on_behalf_of`) | Connected Account     |

#### Payment method - Cash App Pay

If you use [Connect](https://docs.stripe.com/connect.md), take the following into consideration before you enable and use Cash App Pay:

### Request Cash App Pay capabilities for your connected accounts

Set the `cashapp_payments` capability to `active` on your platform account, and for any connected accounts you want to enable for Cash App Pay. You can do this without code by navigating to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and making sure Cash App Pay is on by default for your connected accounts, or you can [request the account capability](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

### Business of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the default statement descriptor and the business name that appears on the customer’s bank statement. The charge type can also change the business of record shown on:

- The Cash App customer interface
- Customer confirmation emails from Cash App
- The mandate when [saving payment details](https://docs.stripe.com/payments/cash-app-pay/set-up-payment.md)

| Charge type                                                                                  | Descriptor taken from |
| -------------------------------------------------------------------------------------------- | --------------------- |
| Direct                                                                                       | Connected Account     |
| Destination                                                                                  | Platform              |
| Separate charge and transfer                                                                 | Platform              |
| Destination (with `on_behalf_of` using a platform saved payment method)                      | Platform              |
| Separate charge and transfer (with `on_behalf_of` using a platform saved payment method)     | Platform              |
| Destination (with `on_behalf_of` not using a platform saved payment method)                  | Connected Account     |
| Separate charge and transfer (with `on_behalf_of` not using a platform saved payment method) | Connected Account     |

A “platform saved payment method” is a payment method created through PaymentIntent or SetupIntent without using the `on_behalf_of` parameter. Thus, the saved payment method belongs to the platform account.

To save a customer from repeated authentications for Destination `on_behalf_of` charges, platforms often save a payment method for the customer, then use it for off session Destination `on_behalf_of` charges.

### PaymentMethod cloning

You can save a customer’s Cash App Pay payment method for recurring purchases but the saved Cash App Pay payment method can only be used with the business of record that the customer authorized _off-session_ (A payment is described as off-session if it occurs without the direct involvement of the customer, using previously-collected payment information) use for. This means that Connect users can’t [clone](https://docs.stripe.com/connect/direct-charges-multiple-accounts.md#clone-and-create-direct-charges) Cash App Pay payment methods across different connected accounts when the connected accounts act as the business of record.

#### Payment method - iDEAL

When using iDEAL | Wero with _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), the connected account’s name must map to its actual business, not to the platform. This is important for regulatory compliance and customer trust, because customers will see this business name during the iDEAL | Wero payment flow.

#### Payment method - Indonesian bank transfers

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with Indonesia bank transfers to process payments on behalf of your connected accounts.

Connect platforms can use Indonesia bank transfers with [any type of charges](https://docs.stripe.com/connect/charges.md#types).

### Connect limitations

The following limitations apply when using Connect with Indonesia bank transfers.

- Destination charges with `on_behalf_of` aren’t supported
- Cross-border funds flows to and from Indonesia (for example, an Indonesian platform taking an application fee from a non-Indonesian connected account) aren’t supported.

#### Payment method - Klarna

A Connect platform can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with Klarna to process connected account payments of all [charge types](https://docs.stripe.com/connect/charges.md).

### Connected accounts with full Stripe Dashboard access

Connected accounts with access to the full Stripe Dashboard, including Standard accounts, can enable Klarna through their Dashboard. To check which accounts have enabled Klarna, use the `capabilities` hash in the [accounts webhooks or APIs](https://docs.stripe.com/api/accounts/object.md#account_object-capabilities-klarna_payments) to see if the `klarna_payments` capability is set to `active`.

### Connected accounts without full Stripe Dashboard access

To enable Klarna for connected accounts without full access to the Stripe Dashboard, including Express and Custom accounts, request the `klarna_payments` [capability](https://docs.stripe.com/connect/account-capabilities.md). Customers see the name of your connected account during checkout and in the Klarna app.

#### Payment method - Kriya

If you use _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you must consider the following before you enable and use Kriya.

### Request Kriya capabilities for your connected accounts

Set the `kriya_payments` capability to `active` on your platform account, and on any connected accounts you want to enable Kriya for. You can also [request more account capabilities](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s banking application and confirmation emails.

| Charge type                                        | Descriptor taken from |
| -------------------------------------------------- | --------------------- |
| Direct                                             | Connected account     |
| Destination                                        | Platform              |
| Separate charge and transfer                       | Platform              |
| Destination (with `on_behalf_of`)                  | Connected account     |
| Separate charge and transfer (with `on_behalf_of`) | Connected account     |

To check or update your statement descriptor, go to your [account settings](https://docs.stripe.com/get-started/account/statement-descriptors.md). For Connect integrations, see [setting statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

#### Payment method - MB Way

A Connect platform can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with MB WAY to process connected account payments of all [charge types](https://docs.stripe.com/connect/charges.md).

### Connected accounts with full Stripe Dashboard access

Connected accounts with access to the full Stripe Dashboard, including Standard accounts, can enable MB WAY through their Dashboard. To check which accounts have enabled MB WAY, use the `capabilities` hash in the [accounts webhooks or APIs](https://docs.stripe.com/api/accounts/object.md#account_object-capabilities-mb_way_payments) to see if the `mb_way_payments` capability is set to `active`.

### Connected accounts without full Stripe Dashboard access

To onboard connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe, request the `mb_way_payments` capability using the [Capabilities API](https://docs.stripe.com/api/capabilities.md). For more details, follow the instructions to [enable payment methods for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md).

#### Payment method - Mexican installments

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with installments to process payments on behalf of connected accounts. As a platform, you can set the default installment configuration for your connected accounts in Mexico. Standard connected accounts can override these settings in the Dashboard.

#### Payment method - MobilePay

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with MobilePay to process payments. Connect users can use MobilePay with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

### Enable MobilePay for connected accounts

Connected accounts with access to the full Stripe Dashboard can enable MobilePay in their [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods). To check which accounts have enabled MobilePay, use the `capabilities` hash in our [accounts webhooks or APIs](https://docs.stripe.com/api/accounts/object.md#account_object-capabilities-mobilepay_payments) to see if the `mobilepay_payments` capability is set to `active`.

For connected accounts that don’t have access to the full Stripe Dashboard, see [enable payment methods for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md). The name of the connected account is the name customers see during checkout and in the MobilePay app.

#### Payment method - Mondu

If you use _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you must consider the following before you enable and use Mondu.

### Request Mondu capabilities for your connected accounts

Set the `mondu_payments` capability to `active` on your platform account, and on any connected accounts you want to enable Mondu for. You can also [request more account capabilities](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s banking application and confirmation emails.

| Charge type                                        | Descriptor taken from |
| -------------------------------------------------- | --------------------- |
| Direct                                             | Connected account     |
| Destination                                        | Platform              |
| Separate charge and transfer                       | Platform              |
| Destination (with `on_behalf_of`)                  | Connected account     |
| Separate charge and transfer (with `on_behalf_of`) | Connected account     |

To check or update your statement descriptor, go to your [account settings](https://docs.stripe.com/get-started/account/statement-descriptors.md). For Connect integrations, see [setting statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

#### Payment method - Multibanco

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with Multibanco to process payments on behalf of a connected account. Connect users can use Multibanco with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

### Enable Multibanco for connected accounts that use the Stripe Dashboard

Connected accounts that use the Stripe Dashboard can enable Multibanco in their [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard.

### Enable Multibanco for connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe

Request the `multibanco_payments` capability on any connected account you want to enable Multibanco for. Follow the instructions to [enable payment methods for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md).

#### Payment method - Pay by Bank

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with Pay by Bank to process payments on behalf of a connected account. Connect users can use Pay by Bank with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

### Enable Pay by Bank for connected accounts that use the Stripe Dashboard

Connected accounts that use the Stripe Dashboard can enable Pay by Bank in their [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard. To check which accounts have enabled Pay by Bank, use the `capabilities` hash in our [accounts webhooks or APIs](https://docs.stripe.com/api/accounts/object.md#account_object-capabilities-pay_by_bank_payments) to see if the `pay_by_bank_payments` capability is set to `active`.

### Enable Pay by Bank for connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe

To onboard connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe, request the `pay_by_bank_payments` capability using the [Capabilities API](https://docs.stripe.com/api/capabilities.md) For more details, follow the instructions to [enable payment methods for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md).

#### Payment method - PayNow

You can use [Stripe Connect](https://docs.stripe.com/connect.md) with PayNow to process payments on behalf of a connected account. _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) users can use PayNow with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate Charges and Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

### Request PayNow capability

You must turn on the PayNow payment method in [your platform settings](https://dashboard.stripe.com/settings/payment_methods) and [request](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting) the `paynow_payments` capability for your connected accounts that will accept PayNow payments.

### Set correct MCC

Stripe and PayNow rely on merchant category codes (MCC) to determine eligibility of the connected accounts against the PayNow [prohibited business categories](https://docs.stripe.com/payments/paynow.md#prohibited-business-categories). Make sure that you set [correct MCCs](https://docs.stripe.com/connect/setting-mcc.md) for your connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe.

### Merchant of record

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the merchant name that appears on PayNow’s website or app during the redirect. The merchant of record determines the Stripe account authorized to create payments with a particular [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md).

#### Payment method - PayPal

PayPal is available for online marketplaces using [Stripe Connect](https://stripe.com/connect). These online marketplaces include businesses such as Deliveroo and ManoMano that collect payments from customers, and later pay out to sub-accounts or service providers. PayPal isn’t available for platforms that onboard other businesses and enable them to accept payments directly, such as Shopify or Squarespace.

> Online marketplaces need to submit an onboarding request from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) to get access to PayPal. Stripe sends email updates about the progress of all requests, and the current status is also reflected on the [Payment Method Settings page](https://dashboard.stripe.com/settings/payment_methods).

The following [Connect charges](https://docs.stripe.com/connect/charges.md) types, typically used by online marketplaces, are available to businesses using PayPal.

| Destination charges | Separate charges and transfers | Direct charges   | on_behalf_of     |
| ------------------- | ------------------------------ | ---------------- | ---------------- |
| ✓ Supported         | ✓ Supported                    | ❌ Not supported | ❌ Not supported |

#### Payment method - PayTo

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with PayTo to process payments on behalf of a connected account. Connect users can use PayTo with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

### Enable PayTo for connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe

To onboard connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe, request the `payto_payments` capability using the [Capabilities API](https://docs.stripe.com/api/capabilities.md). For more details, see [Enable payment methods for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md).

#### Payment method - Pix

Use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with Pix to process payments on behalf of connected accounts. _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) users use Pix with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

Pix availability on Connect depends on the [merchant of record](https://docs.stripe.com/connect/merchant-of-record.md) (MoR) for the payment. The MoR is determined by the [charge type](https://docs.stripe.com/connect/charges.md) you use:

- **Connected account is the MoR** (for example, [direct charges](https://docs.stripe.com/connect/direct-charges.md), or charges using the [`on_behalf_of`](https://docs.stripe.com/connect/separate-charges-and-transfers.md#settlement-merchant) parameter): Pix is supported if the connected account is in a supported country for Pix.
- **Platform is the MoR** (for example, [destination charges](https://docs.stripe.com/connect/destination-charges.md) or [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md) without `on_behalf_of`): Pix is supported if the platform account is in a supported country for Pix.

### Accept Pix payments as the connected account

[Direct charges](https://docs.stripe.com/connect/direct-charges.md) and charge types using the [on_behalf_of](https://docs.stripe.com/connect/separate-charges-and-transfers.md#settlement-merchant) parameter require the connected account itself (not the platform) to have activated the Pix payment method. Connect platforms can use the [`pix_payments` capability](https://docs.stripe.com/connect/account-capabilities.md#payment-methods) to determine whether that’s the case for a connected account:

- In the case of connected accounts that use the Stripe Dashboard, the owner of the account needs to activate the payment method in their [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard.
- In the case of connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe, the platform needs to request the `pix_payments` capability.

#### Payment method - Scalapay

If you use _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you must consider the following before you enable and use Scalapay.

### Request Scalapay capabilities for your connected accounts

Set the `scalapay_payments` capability to `active` on your platform account, and on any connected accounts you want to enable Scalapay for. You can also [request more account capabilities](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s banking application and confirmation emails.

| Charge type                                        | Descriptor taken from |
| -------------------------------------------------- | --------------------- |
| Direct                                             | Connected account     |
| Destination                                        | Platform              |
| Separate charge and transfer                       | Platform              |
| Destination (with `on_behalf_of`)                  | Connected account     |
| Separate charge and transfer (with `on_behalf_of`) | Connected account     |

To check or update your statement descriptor, go to your [account settings](https://docs.stripe.com/get-started/account/statement-descriptors.md). For Connect integrations, see [setting statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

#### Payment method - SeQura

If you use _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you must consider the following before you enable and use SeQura.

### Request SeQura capabilities for your connected accounts

Set the `sequra_payments` capability to `active` on your platform account, and on any connected accounts you want to enable SeQura for. You can also [request more account capabilities](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s banking application and confirmation emails.

| Charge type                                        | Descriptor taken from |
| -------------------------------------------------- | --------------------- |
| Direct                                             | Connected account     |
| Destination                                        | Platform              |
| Separate charge and transfer                       | Platform              |
| Destination (with `on_behalf_of`)                  | Connected account     |
| Separate charge and transfer (with `on_behalf_of`) | Connected account     |

To check or update your statement descriptor, go to your [account settings](https://docs.stripe.com/get-started/account/statement-descriptors.md). For Connect integrations, see [setting statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

#### Payment method - Sunbit

If you use _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients), you must consider the following before you enable and use Sunbit.

### Request Sunbit capabilities for your connected accounts

Set the `sunbit_payments` capability to `active` on your platform account, and on any connected accounts you want to enable Sunbit for. You can also [request more account capabilities](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s banking application and confirmation emails.

| Charge type                                        | Descriptor taken from |
| -------------------------------------------------- | --------------------- |
| Direct                                             | Connected account     |
| Destination                                        | Platform              |
| Separate charge and transfer                       | Platform              |
| Destination (with `on_behalf_of`)                  | Connected account     |
| Separate charge and transfer (with `on_behalf_of`) | Connected account     |

To check or update your statement descriptor, go to your [account settings](https://docs.stripe.com/get-started/account/statement-descriptors.md). For Connect integrations, see [setting statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

#### Payment method - Sepa Direct Debit

To use SEPA Direct Debits in a _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) integration, you must enable SEPA Direct Debit on your platform and request the `sepa_debit_payments` capability for your connected accounts.

#### Payment method - Swish

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with Swish to process payments on behalf of a connected account. Connect users can use Swish with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

#### Payment method - TWINT

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works.md) with TWINT to process payments on behalf of a connected account. Connect users can use TWINT with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges.md)
- [Destination](https://docs.stripe.com/connect/destination-charges.md)
- [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)

### Enable TWINT for connected accounts that use the Stripe Dashboard

Connected accounts that use the Stripe Dashboard can enable TWINT in their [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods) in the Dashboard. To check which accounts have enabled TWINT, use the `capabilities` hash in our [accounts webhooks or APIs](https://docs.stripe.com/api/accounts/object.md#account_object-capabilities-twint_payments) to see if the `twint_payments` capability is set to `active`.

### Enable TWINT for connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe

Follow the instructions to [enable payment methods for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md). The name of your connected account is the name customers see during checkout and in the TWINT app.

#### Payment method - Wechat Pay

Wechat Pay has partial [Connect](https://stripe.com/connect) support depending on the [charge type](https://docs.stripe.com/connect/charges.md).

The following charge types are generally available.

- Destination charges
- Separate charges and transfers

The following charge types are in private preview.

- Direct charges
- `on_behalf_of`

For connected accounts with standard Dashboard access, individual connected accounts can enable Wechat Pay in the Dashboard.

For connected accounts without standard Dashboard access, the platform needs to request the `wechat_pay_payments` capability. This is a private preview feature. Contact Stripe Support to request access.
