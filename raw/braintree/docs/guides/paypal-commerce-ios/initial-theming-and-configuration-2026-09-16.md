<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/initial-theming-and-configuration -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Initial Theming and Configuration
slug: /docs/guides/paypal-commerce-ios/initial-theming-and-configuration/
createTime: '2025-04-01T23:30:52.484Z'
updateTime: '2025-04-01T23:30:52.502Z'
---



# Initial Theming and Configuration

Most of these values will be overridden by what you have set up in the[Theming section](https://commerce.paypal.com/settings/theme)of the PayPal Commerce
Panel, but by including the**PayPalCommerce-Config.plist**and**PayPalCommerce-Assets.xcassets**, you can include an initial setup.
**NOTE**
Initial setup is optional.


### PayPalCommerce-Config.plist

| Key | Values |
| --- | --- |
| skip_initial_onboarding | NO: The store will initially present an onboarding flow including: login, name, email, shipping address, and billing info. The user will still be allowed to skip this and go directly to your store.`YES`: The store will skip initial onboarding and present the products list immediately. If a user tries to purchase something without having fully onboarded, they will complete onboarding at that point. |
| font | A dictionary of font names based on weight (default is system font). regular_font thin_font light_font medium_font bold_font |
| enable_barcode_scanning | **boolean**that allows the app to scan barcodes and QR codes. |
| colors | A dictionary of colors we use in the app. Colors are denoted as hex values (e.g.**#0FA0FA**). They will be dynamically updated based on the settings in your theme in the[PayPal Commerce Panel](https://commerce.paypal.com/settings/theme).| primary_button_color | Onboarding button background, "continue shopping" buttons. |
| accent_color | Used in product detail, variant selection, receipts, etc as a way to highlight certain elements. |
| buy_button_color | Buy button backgound color. |
| header_background_color | Navigation bar background color. |
| header_action_color | The color of the buttons in the navigation bar. |
| category_background_color | The background color of the category selection bar. |
| banner_color | The background color of the header banner in the receipt. |
| modal_color | The background color of the sidebar menu, as well as modal overlays. |
| checkmark_color | The checkmark color across the app. | |


### PayPalCommerce-Assets.xcassets

These will be overridden by what you set in the PayPal Commerce Panel.| login_background | Used in the onboarding login prompt screen. Required size: 320x568 and 640x1136 |
| logo_header | Used in the navigation bar on the main products list. Suggested size: 167x30 and 328x60 |

