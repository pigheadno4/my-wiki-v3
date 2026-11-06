> [!IMPORTANT]
> **CocoaPods**
>
> * This is the **last release available through CocoaPods**. From this release onward, the Checkout iOS SDK (v5) will be distributed only through **Swift Package Manager (SPM)** and **Carthage**, as CocoaPods is being discontinued. For more information, see the [CocoaPods announcement](https://blog.cocoapods.org/CocoaPods-Specs-Repo/)

## Fixed
    
- Fixed VoiceOver reading the store payment method toggle without a label; it is now a single labeled switch.
- Fixed VoiceOver no longer reading the expiry date and security code formats after typing or after a validation error.
- Fixed card brand logos being selectable and focusable instead of being read as images.
- Fixed the billing address title and the Drop-in toolbar title not being announced as headers.
- Fixed the Drop-in cancel button missing a VoiceOver label when using a custom image. All cancel button styles are now read as "Cancel".

## External contributors:
Thanks to @srussier-luna and @jeevan-cata for their contributions.



