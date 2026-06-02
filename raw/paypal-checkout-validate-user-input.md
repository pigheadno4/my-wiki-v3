---
title: Validate user input
slug: /docs/checkout/standard/customize/validate-user-input/
createTime: '2024-02-23T23:37:40.032Z'
updateTime: '2025-05-14T10:34:21.480Z'
---

# Validate user input

Validate payer input when payment buttons are clicked. For example, your page might contain a web form that must be validated before starting the transaction.

For an optimal payer experience, complete validation before rendering the buttons. For validation that you can't complete before rendering the buttons, run synchronous or asynchronous validation when clicking the PayPal buttons.

## Know before you code

### PayPal Checkout

Complete the steps in Get started to get your sandbox account login information and access token from the Developer Dashboard.

This feature modifies an existing PayPal Checkout integration and uses the following:

- PayPal JavaScript SDK
- Orders REST API — Create order endpoint

## Validation approaches

Use synchronous validation when possible because it provides a better user experience. Use asynchronous validation only for server-side or asynchronous channels.

### Synchronous validation

Use `onInit` to disable the button on render, and `onClick` to show errors. Enable/disable based on form state changes:

```javascript
<p id="error" class="hidden">Please check the checkbox</p>
<label><input id="check" type="checkbox"> Check here to continue</label>
<script>
  paypal.Buttons({
    // onInit is called when the button first renders
    onInit: function(data, actions) {
      // Disable the buttons
      actions.disable();
      // Listen for changes to the checkbox
      document.querySelector('#check')
        .addEventListener('change', function(event) {
          // Enable or disable the button when it is checked or unchecked
          if (event.target.checked) {
            actions.enable();
          } else {
            actions.disable();
          }
        });
    },
    // onClick is called when the button is clicked
    onClick: function() {
      // Show a validation error if the checkbox is not checked
      if (!document.querySelector('#check').checked) {
        document.querySelector('#error').classList.remove('hidden');
      }
    }
  }).render('#paypal-button-container');
</script>
```

### Asynchronous validation

Return a Promise from `onClick`. Call `actions.reject()` to block checkout or `actions.resolve()` to proceed:

```javascript
<p id="error" class="hidden">Please check your information to continue</p>
<script>
  paypal.Buttons({
    // onClick is called when the button is clicked
    onClick: function(data, actions) {
      // Return a promise from onClick for async validation
      return fetch('/my-api/validate', {
        method: 'post',
        headers: { 'content-type': 'application/json' }
      }).then(function(res) {
        return res.json();
      }).then(function(data) {
        // If there is a validation error, reject, otherwise resolve
        if (data.validationError) {
          document.querySelector('#error').classList.remove('hidden');
          return actions.reject();
        } else {
          return actions.resolve();
        }
      });
    }
  }).render('#paypal-button-container');
</script>
```
