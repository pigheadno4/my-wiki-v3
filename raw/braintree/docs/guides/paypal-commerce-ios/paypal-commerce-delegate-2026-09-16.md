<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/paypal-commerce-delegate -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: PayPalCommerceDelegate
slug: /docs/guides/paypal-commerce-ios/paypal-commerce-delegate/
createTime: '2025-04-01T22:24:14.385Z'
updateTime: '2025-04-01T22:24:14.418Z'
---



# PayPalCommerceDelegate

There are currently two cases where you might want to set the**PayPalCommerceDelegate**:
- If you present the store modally, and you would like to be notified when the store is dismissed by the user. Then after you configure the client, call:


### Objective-C
```objectivec
[PayPalCommerce setDelegate:self];
```
And then implement one or both of these protocol methods:
### Objective-C
```objectivec
-(void)paypalCommerceWillDismissWithTransitionDuration:(NSTimeInterval)transitionDuration;
-(void)paypalCommerceDidDismiss;
```

- If you present the store within a tab bar controller or other such embedded system, and you have custom buttons to trigger purchases, then you’re responsible for displaying the store. After you configure the client, call:


### Objective-C
```objectivec
[PayPalCommerce setDelegate:self];
```
And then implement this protocol method:
### Objective-C
```objectivec
-(void)paypalCommerceShouldBeVisible;
```
Within that call, make sure the store is visible. For example, if you have embedded the store within
a tab bar controller, you would make sure the store’s view controller is theselectedViewController.