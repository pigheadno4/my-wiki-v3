> [!IMPORTANT]
> **iPhone Duo**
>
> * This release supports **iPhone Duo**.

## Changed

* Improved the layout of Drop-in and Components for iPhone Duo.

## Fixed

* **Apple Pay:** Fixed missing partial payment order for Apple Pay in Drop-in, which caused the remaining amount payment to be submitted without the order and fail after a partial payment (e.g. gift card).

* **Card Component:** Fixed the card security code (CVC/CVV) field accepting more than the allowed number of digits, which could submit an over-length code while only showing the truncated value.

* **Accessibility:** Changed the default inactive text-input title and underline colors to improve accessibility. The defaults now use `UIColor.Adyen.formTextItemInactive`, which resolves to the following:

  * Light mode: **#757575**
  * Dark mode: **#8E8E93**

  If you customize the following, your styling is not affected:

  * `FormTextItemStyle.title.color`
  * `FormTextItemStyle.separatorColor`

  The following have not been changed:

  * `UIColor.Adyen.componentSecondaryLabel`
  * `UIColor.Adyen.componentSeparator`
