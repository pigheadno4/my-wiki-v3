<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/sdk/ -->
<!-- Fetched: 2026-04-13 -->

Online / Checkout / Expanded / Customize / 3D Secure / Integrate 3D Secure using Card Fields

# Integrate 3D Secure using Card Fields

Enable 3D Secure for advanced credit and debit cards. This integration uses the JavaScript SDK.

If you have a standard checkout integration, you don't need to integrate 3D Secure. PayPal handles 3D secure authentication for standard checkout integrations.

> **Important:** These 3D Secure instructions apply to the JavaScript SDK component **CardFields**. If your integration uses the HostedFields component, see Integrate 3D Secure using Hosted Fields instead.

## Know before you code

### If you are based in Europe, you may be subject to PSD2

- Include 3D Secure as part of your integration.
- Pass the cardholder's billing address as part of the transaction processing.

To trigger the authentication, pass the verification method in the create order payload. The verification method can be a `contingencies` parameter with `SCA_ALWAYS` or `SCA_WHEN_REQUIRED`.

- `SCA_ALWAYS` triggers an authentication for every transaction.
- `SCA_WHEN_REQUIRED` triggers an authentication only when a regional compliance mandate such as PSD2 is required. 3D Secure is supported only in countries with a PSD2 compliance mandate.

## Integration

```javascript
// Create the CardFields component and define callbacks and contingencies
const cardField = paypal.CardFields({
  createOrder: function(data) {
    return fetch("myserver.com/api/paypal/order/create/", {
      method: "post",
      body: JSON.stringify({
        // ...
        payment_source: { // wrap 3D Secure preference in `payment_source`
          card: {
            attributes: {
              verification: {
                method: "SCA_ALWAYS"
              },
            },
            experience_context: {
              shipping_preference: "NO_SHIPPING",
              return_url: "https://example.com/returnUrl",
              cancel_url: "https://example.com/cancelUrl",
            },
          },
        }
      })
    }).then((res) => {
      return res.json();
    }).then((orderData) => {
      return orderData.id;
    });
  },
  onApprove: function(data) {
    const { liabilityShift, orderID } = data;
    if (liabilityShift) {
      /* Handle liability shift. More information in 3D Secure response parameters */
    }
    return fetch(`myserver.com/api/paypal/orders/${orderID}/capture/`, {
      method: "post",
    }).then((res) => {
      return res.json();
    }).then((orderData) => {
      // Redirect to a success page
    });
  },
  onError: function(error) {
    // Do something with the error from the SDK
  }
});

// Render each field after checking for eligibility
if (cardField.isEligible()) {
  const nameField = cardField.NameField();
  nameField.render('#card-name-field-container');
  const numberField = cardField.NumberField();
  numberField.render('#card-number-field-container');
  const cvvField = cardField.CVVField();
  cvvField.render('#card-cvv-field-container');
  const expiryField = cardField.ExpiryField();
  expiryField.render('#card-expiry-field-container');

  // Add a click listener to submit button and call the submit function on the CardField component
  document.getElementById("multi-card-field-button").addEventListener("click", () => {
    cardField.submit().then(() => {
      // Submit is successful
    });
  });
}
```

## See Also

- **Response parameters** — Learn more about handling 3D Secure responses.
- **Test scenarios** — Simulate 3D Secure scenarios and responses.
