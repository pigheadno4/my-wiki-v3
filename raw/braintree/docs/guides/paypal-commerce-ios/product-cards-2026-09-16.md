<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/product-cards -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Product Cards
slug: /docs/guides/paypal-commerce-ios/product-cards/
createTime: '2025-04-01T22:35:40.236Z'
updateTime: '2025-04-01T22:35:40.287Z'
---



# Product Cards


## Embed products in your own user interface

A product card is a simple view that easily allows users to find and buy products within the
existing structure of your app. It displays the product name, image, description, cost, and a buy
button that initiates a purchase. The SDK fetches up-to-date product information from our API and
populates the view.
## Add a product card to your app

These are views that take a search term as input. To embed a product card into your app:
### Objective-C
```objectivec
CGRect rect = CGRectMake(0, 0, 320, 80);
NSString *searchTerm = @"ninja cats";
PPCProductCardView *productCardView = [PayPalCommerce productCardViewWithFrame:rect
                                                                    searchTerm:searchTerm
                                                                    completion:^(BOOL success, NSError *error) {

}];
[self.view addSubview:productCardView];
```
Alternatively, if you want to find a product by its group ID:
### Objective-C
```objectivec
CGRect rect = CGRectMake(0, 0, 320, 80);
NSString *productGroupID = @""; //use one of your product group IDs
PPCProductCardView *productCardView = [PayPalCommerce productCardViewWithFrame:rect
                                                                productGroupID:productGroupID
                                                                    completion:^(BOOL success, NSError *error) {

}];
[self.view addSubview:productCardView];
```

### Purchase flow from a product card in a content-based app

You can render a product view within your own app, which allows your users to initiate a purchase.[![Product,Card](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/commerce/thumbs/product_card.png)](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/commerce/thumbs/product_card.png)[![Purchase,Confirmation](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/commerce/thumbs/purchase_confirmation.png)](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/commerce/thumbs/purchase_confirmation.png)[![Receipt](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/commerce/thumbs/purchase_confirmation.png)](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/commerce/thumbs/purchase_confirmation.png)
## Display and purchase a product from your app with your own UI

You can also display product information and initiate a purchase using your own UI by fetching aPPCProductobject and executing a purchase on it per some user action.
### Objective-C
```objectivec
[PayPalCommerce fetchProductWithGroupID:@""
                             completion:^(PPCProduct *product, NSError *error){
        //display something notifying what they're buying
}];
```
Then once the user initiates a purchase, you would call:
### Objective-C
```objectivec
[PayPalCommerce purchaseProduct:product];
```

### Purchase flow from your own UI in a content-based app

[![Custom,UI,Purchase](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/commerce/thumbs/purchase_custom_ui.png)](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/commerce/thumbs/purchase_custom_ui.png)[![Purchase,Confirmation](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/commerce/thumbs/purchase_confirmation.png)](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/commerce/thumbs/purchase_confirmation.png)[![Receipt](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/commerce/thumbs/receipt.png)](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/commerce/thumbs/receipt.png)