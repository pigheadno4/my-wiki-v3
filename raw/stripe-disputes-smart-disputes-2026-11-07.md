<!-- Source URL: https://docs.stripe.com/disputes/smart-disputes -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Smart Disputes

Automate evidence collection and submission for eligible card disputes.

Smart Disputes saves you time by automating evidence collection, compilation, and submission for eligible disputes on card transactions. To get started with Smart Disputes, see [Set up and configure Smart Disputes](https://docs.stripe.com/disputes/set-up-smart-disputes.md).

## Automate dispute management 

Smart Disputes uses an AI rules engine to analyze incoming disputes. It extracts relevant evidence from Stripe internal data, your transaction data, and cardholder data. The system tailors this evidence to the dispute reason to help you win.  We determine Smart Disputes eligibility using multiple factors, including the dispute reason code, payment method, evidence availability, evidence relevance, and cost. 

|  |
| ![Help save time](https://b.stripecdn.com/docs-statics-srv/assets/save-time.f510099858fb56db1483080a8a0324df.png) | ![Help recover revenue](https://b.stripecdn.com/docs-statics-srv/assets/recover-revenue.af6bf2a5c9b0e7d2926d051d186c0c8d.png) | ![No integration required](https://b.stripecdn.com/docs-statics-srv/assets/no-integration.26a884bdb47ec61f137f824b51f4e165.png) |
| **Save time**

Smart Disputes automatically assembles evidence packets for eligible disputes when you receive a dispute and submits them before the dispute deadline, so you don’t have to contest them. | **Recover revenue**

We use artificial intelligence and insights from the Stripe network to tailor evidence packets that help you recover disputed revenue. | **No integration required**

Smart Disputes is built into Stripe and requires no additional integration work if you already use Stripe. |

## How it works 

When you receive a Smart Disputes eligible dispute, Stripe notifies you by email and in the Dashboard. If you don’t take any action, Smart Disputes automatically submits the pre-filled evidence packet just before the dispute times out. This ensures you don’t miss any deadlines. If you don’t want to use Smart Disputes, you can respond to the dispute by countering manually, or accepting the dispute before the deadline. You can turn off auto-submit in your [Dashboard settings](https://dashboard.stripe.com/settings/disputes).
![The dispute lifecycle](https://b.stripecdn.com/docs-statics-srv/assets/dispute-flow.a082c69dafa1503c33d5f7bc7c92cdf4.png)

Each evidence packet contains data available to Stripe at the time we generate the packet, and you’re responsible for making sure that data is accurate and complete.

We don’t guarantee that disputes countered with Smart disputes will be resolved in your favor, because the final decision lies with the issuer. However, we only bill you a Smart Disputes fee if you win. You incur no Smart Dispute fee on lost disputes.

[See pricing details here](https://stripe.com/pricing).

Smart Disputes can assist you, but it’s not a replacement for professional advice on handling disputes. Look into each dispute individually to determine how to respond to it.

## Testing 

To test responses to Smart Disputes eligible disputes, use the following test card, which creates a Smart Disputes eligible dispute:

| Testing method | Token |
| --- | --- |
| Card number | 4000000001000043 |
| PaymentMethod | `pm_card_createAutoRepresentmentEligibleDispute` |
| Token | `tok_createAutoRepresentmentEligibleDispute` |
