<!-- Source: Stripe Checkout — Compliant promotional emails -->
<!-- Fetched: 2026-04-20 -->

# Compliant promotional emails

Follow these best practices to ensure compliant promotional emails.

[Promotional emails](https://docs.stripe.com/payments/checkout/promotional-emails-consent.md) promote a product or service (for example, recovery emails, newsletters, or promotions) and represent an opportunity to strengthen and expand your relationship with customers. Read through these best practices for enabling compliance, but be aware of laws that restrict your ability to use your customers’ personal data for promotional content—check with your legal counsel if you’re unsure.

Privacy and marketing laws require companies to notify or gain consent from customers before sending promotional emails and promptly honor unsubscribe requests.

> Review the callouts which may require specific updates to your documentation or practices.

## Customer consent

Checkout helps you optimize collection of customer opt-in and opt-out permissions.

The laws around consent to use personal data such as emails to send promotional messages differ by country. For US businesses and customers, laws generally allow sending promotional messages as long as you offer an opt-out opportunity and honor any unsubscribe requests that you’ve received. Many rest of world jurisdictions require an affirmative consent flow.

When you enable promotional emails, Checkout presents a checkbox beneath the email field that reads “Keep me updated with news and personalized offers.” It can be unclear which country’s laws apply to a particular transaction. Because of this, Stripe uses logic that considers both the jurisdiction of your Stripe account and the IP address of the customer to determine whether the default is for the checkbox to be checked or unchecked. When our logic determines that either your Stripe account or the customer is located in a jurisdiction that requires (or is otherwise advisable to obtain) affirmative consent, by default, we present such customers with the unchecked checkbox.

This feature can also help you send [abandoned cart or “recovery"](https://docs.stripe.com/payments/checkout/abandoned-carts.md) emails, which are encouraging emails sent to customers who almost made a purchase. In the case of recovery emails, you only receive the email addresses of prospective customers who’ve entered their email addresses into your checkout form and have given permission to receive promotional emails (that is, the email address is validated and the checkbox is checked when the checkout session expires). We recommend that you use these emails only for sending recovery emails and limit targeting broader marketing campaigns to customers who have successfully completed a purchase and provided consent.

In either case, if the customer notifies you that they don’t want to receive promotional content or you have another reason to believe they don’t want their personal data used to send promotional emails, don’t send the emails, despite the permission provided from Checkout.

## Customer unsubscribe requests

> Ensure consumers can unsubscribe and requests are promptly honored.

All promotional emails must include information about the sender and a way for customers to unsubscribe, and you must promptly honor all unsubscribe requests. _Customers_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) who have unsubscribed shouldn’t receive promotional emails unless they subsequently express consent. To make sure you meet requirements in your jurisdiction, provide customers the opportunity to withdraw their consent or unsubscribe to future marketing content directly from your website or an easily-accessible customer service process. The process for withdrawing consent should be as easy as providing consent.

If a customer reaches out to Stripe with a request to delete their personal information or to stop using it for promotional purposes, Stripe won’t act on that request. Stripe acts as a service provider/processor to you, and will treat these unsubscribe requests like other “data subject requests” that Stripe receives regarding your customers. Stripe will redirect the customer back to you to respond to, and honor, their requests.

## Privacy policy update

> Update your privacy to disclose data collection and usage for promotional emails.

As outlined in our [Terms of Service](https://stripe.com/legal), you must disclose the collection and use of your customers’ data for sending promotional emails in your privacy policy or other privacy notices. Because of the limited use rights obtained in this checkbox, you may not use the information provided through this feature for any purposes beyond sending news and promotional emails unless you explicitly obtain those rights outside of this feature in Checkout.

Checkout’s privacy policy, which is linked on every Checkout session, discloses that Stripe collects information solely as a service provider to the business and isn’t an independent controller of customer data. We recommend that you also review your privacy policy before using this feature. Your privacy policy should disclose to customers all the ways you collect, retain, use, and share data—this includes the data you collect through Checkout from prospective customers who visit your webpage but don’t complete a transaction. It would be advisable to also disclose that you may send them promotional emails based on their opt-in or opt-out selection during checkout. See the [Stripe Privacy Center](https://stripe.com/privacy-center/legal) for more information.
