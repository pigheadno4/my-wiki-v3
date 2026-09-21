<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/barcode-scanning -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Barcode Scanning
slug: /docs/guides/paypal-commerce-ios/barcode-scanning/
createTime: '2025-04-02T00:14:12.430Z'
updateTime: '2025-04-02T00:14:12.446Z'
---



# Barcode Scanning

If your store supports UPC search, you can enable UPC and QR scanning. In the[Config plist](/braintree/docs/guides/paypal-commerce-ios/initial-theming-and-configuration), addenable_barcode_scanningset totrue. In your app, you can ask[PayPalCommerce deviceSupportsBarcodeScanning]to see if the device supports barcode
scanning. If it does, you can trigger it directly from your app using[PayPalCommerce scanForBarcodes]. This will present the scanning interface. If it finds
any matches, it will present the product detail page, or if there were multiple matches, then a list
of products. If you want to use QR codes, please use this format:
- http://m.example.com/search/ninja
- http://m.example.com/product/123456

