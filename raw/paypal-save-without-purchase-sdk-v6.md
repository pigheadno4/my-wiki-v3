<!-- Source URL: https://docs.paypal.ai/payments/methods/paypal/save-without-purchase -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Save PayPal without purchase with the JavaScript SDK

This guide demonstrates how to integrate PayPal save payment functionality using the JavaScript SDK v6. Customers can securely save their PayPal payment methods for future transactions without making an immediate purchase. A common use case is offering a free trial and charging customers after the trial period ends.

The PayPal Save Payment integration enables you to:

- Collect and securely store PayPal payment methods without charging the customer.
- Create payment tokens for future use in subsequent transactions.
- Maintain PCI compliance by leveraging PayPal's secure vault system.

## Prerequisites

Obtain your **client ID** and **secret**, and enable vaulting:

1. Log in to the [PayPal Developer Dashboard](https://developer.paypal.com/dashboard/).
2. Under **Apps & Credentials** > **REST API apps**, select your app name.
3. Under **API credentials**, obtain the **Client ID** and **Secret**.
4. Under **Features** > **Payment capabilities**, confirm that **Save payment methods** is selected.

Configure your environment:

In your root folder, create an `.env` file with your PayPal credentials:

```bash theme={null}
PAYPAL_SANDBOX_CLIENT_ID=your_client_id
PAYPAL_SANDBOX_CLIENT_SECRET=your_client_secret
```

## Key concepts

Setup token vs payment token:

- **Setup Token**: Temporary token used during the save payment flow
- **Payment Token**: Permanent token stored in PayPal's vault for future use
- **Conversion**: Setup tokens are converted to payment tokens after customer approval

Payment flows:

- **VAULT_WITHOUT_PAYMENT**: Save payment method without making a purchase
- **VAULT_WITH_PAYMENT**: Save payment method while making a purchase (not covered in this doc)

Usage patterns:

- **IMMEDIATE**: Token will be used right away
- **DEFERRED**: Token will be used at a future date

## Integration flow

The PayPal save payment integration follows a specific flow:

1. Initialize PayPal SDK with your browser-safe client token.
2. Check eligibility for save payment functionality.
3. Create save payment session using vault-specific session options.
4. Create setup token on your server.
5. Start save payment session to collect payment method.
6. Create payment token from vault setup token for future use.

## Set up your front end

Build an HTML page and a JavaScript file to set up your front end.

### Build an HTML page

```html lines expandable theme={null}
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Save Payment - PayPal JavaScript SDK</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style>
      .buttons-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
      }
    </style>
  </head>
  <body>
    <h1>Save Payment Integration</h1>

    <div class="buttons-container">
      <!-- PayPal save payment button, initially hidden -->
      <paypal-button id="paypal-button" hidden></paypal-button>
    </div>

    <script src="app.js"></script>

    <!-- Load PayPal SDK -->
    <script
      async
      src="https://www.sandbox.paypal.com/web-sdk/v6/core"
      onload="onPayPalWebSdkLoaded()"
    ></script>
  </body>
</html>
```

### Initialize the SDK to save payment methods

```javascript lines expandable theme={null}
async function onPayPalWebSdkLoaded() {
  try {
    // Get client token for authentication
    const clientToken = await getBrowserSafeClientToken();

    // Create PayPal SDK instance
    const sdkInstance = await window.paypal.createInstance({
      clientToken,
      components: ["paypal-payments"],
      pageType: "checkout",
    });

    // Check eligibility for save payment with vault flow
    const paymentMethods = await sdkInstance.findEligibleMethods({
      currencyCode: "USD",
      paymentFlow: "VAULT_WITHOUT_PAYMENT", // Specify vault flow without payment
    });

    // Set up save payment button if eligible
    if (paymentMethods.isEligible("paypal")) {
      setupPayPalButton(sdkInstance);
    } else {
      console.log("PayPal save payment is not eligible for this session");
    }
  } catch (error) {
    console.error(error);
  }
}

async function getBrowserSafeClientToken() {
  const response = await fetch("/paypal-api/auth/browser-safe-client-token", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const { accessToken } = await response.json();
  return accessToken;
}
```

### Configure the payment session

```javascript lines expandable theme={null}
const paymentSessionOptions = {
  // Called when customer approves saving their payment method
  async onApprove(data) {
    console.log("Save payment approved:", data);

    try {
      // Create payment token from vault setup token and store payment token ID securely (server-side recommended)
      const createPaymentTokenResponse = await createPaymentToken(
        data.vaultSetupToken,
      );

      console.log("Payment token created:", createPaymentTokenResponse);

      // Handle successful save payment: show success message, etc.
    } catch (error) {
      console.error("Payment token creation failed:", error);
      // Show user-friendly error messages, optionally provide retry mechanism, etc.
    }
  },

  // Called when customer cancels the save payment flow
  onCancel(data) {
    console.log("Save payment cancelled:", data);
    // Show cancellation message, return user to appropriate flow, etc.
  },

  // Called when an error occurs during save payment
  onError(error) {
    console.error("Save payment error:", error);
  },
};

async function createPaymentToken(vaultSetupToken) {
  const response = await fetch("/paypal-api/vault/payment-token/create", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ vaultSetupToken }),
  });
  const data = await response.json();

  return data;
}
```

### Set up button to save payments

```javascript lines expandable theme={null}
async function setupPayPalButton(sdkInstance) {
  // Create PayPal save payment session
  const paypalPaymentSession = sdkInstance.createPayPalSavePaymentSession(
    paymentSessionOptions,
  );

  // Get reference to PayPal button
  const paypalButton = document.querySelector("#paypal-button");
  paypalButton.removeAttribute("hidden");

  // Add click handler to start save payment flow
  paypalButton.addEventListener("click", async () => {
    try {
      // Get the promise reference by invoking createVaultSetupToken()
      // Do not await this async function - it can cause transient activation issues
      // Read about transient activation at https://developer.mozilla.org/en-US/docs/Glossary/Transient_activation
      const createVaultSetupTokenPromise = createVaultSetupToken();

      // Start the save payment session
      await paypalPaymentSession.start(
        {
          presentationMode: "auto", // Auto-detects best presentation mode
        },
        createVaultSetupTokenPromise,
      );
    } catch (error) {
      console.error("Save payment start error:", error);
    }
  });
}

async function createVaultSetupToken() {
  const response = await fetch("/paypal-api/vault/setup-token/create", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  });
  const { id } = await response.json();

  return { setupToken: id };
}
```

## Set up your backend

PayPal APIs can either be called directly, or by using the [PayPal TypeScript Server SDK](https://github.com/paypal/PayPal-TypeScript-Server-SDK). The following examples use the `@paypal/paypal-server-sdk` npm package.

### Set up the PayPal TypeScript Server SDK

Step 1: Install the package.

```javascript theme={null}
npm install @paypal/paypal-server-sdk
```

Step 2: Get your PayPal credentials.

- Log in to the [PayPal Developer Dashboard](https://developer.paypal.com/dashboard/).
- Navigate to **Apps & Credentials**.
- Create or select an app to get your **client ID** and **secret**.

Step 3: Create and initialize the client and controllers.

```typescript lines expandable theme={null}
import {
  ApiError,
  Client,
  CustomError,
  Environment,
  OAuthAuthorizationController,
  PaypalPaymentTokenUsageType,
  VaultController,
  VaultInstructionAction,
  VaultTokenRequestType,
} from "@paypal/paypal-server-sdk";

import type {
  OAuthProviderError,
  PaymentTokenResponse,
  SetupTokenRequest,
} from "@paypal/paypal-server-sdk";

const client = new Client({
  clientCredentialsAuthCredentials: {
    oAuthClientId: PAYPAL_SANDBOX_CLIENT_ID,
    oAuthClientSecret: PAYPAL_SANDBOX_CLIENT_SECRET,
  },
  environment: Environment.Sandbox, // Use Environment.Production for live
});

const oAuthAuthorizationController = new OAuthAuthorizationController(client);
const vaultController = new VaultController(client);
```

### Client token endpoint

```typescript lines expandable theme={null}
app.get(
  "/paypal-api/auth/browser-safe-client-token",
  async (_req: Request, res: Response) => {
    try {
      const { jsonResponse, httpStatusCode } =
        await getBrowserSafeClientToken();
      res.status(httpStatusCode).json(jsonResponse);
    } catch (error) {
      console.error("Failed to create browser safe access token:", error);
      res
        .status(500)
        .json({ error: "Failed to create browser safe access token." });
    }
  },
);

export async function getBrowserSafeClientToken() {
  try {
    const auth = Buffer.from(
      `${PAYPAL_SANDBOX_CLIENT_ID}:${PAYPAL_SANDBOX_CLIENT_SECRET}`,
    ).toString("base64");

    const fieldParameters = {
      response_type: "client_token",
    };

    const { result, statusCode } =
      await oAuthAuthorizationController.requestToken(
        {
          authorization: `Basic ${auth}`,
        },
        fieldParameters,
      );

    // this interface is specific to the "client_token" response type
    interface ClientToken {
      accessToken: string;
      expiresIn: number;
      scope: string;
      tokenType: string;
    }

    const { accessToken, expiresIn, scope, tokenType } = result;
    const transformedResult: ClientToken = {
      accessToken,
      // expiresIn is a BigInt and must be converted to a Number
      expiresIn: Number(expiresIn),
      scope: String(scope),
      tokenType,
    };

    return {
      jsonResponse: transformedResult,
      httpStatusCode: statusCode,
    };
  } catch (error) {
    if (error instanceof ApiError) {
      const { result, statusCode } = error;
      type OAuthError = {
        error: OAuthProviderError;
        error_description?: string;
      };
      return {
        jsonResponse: result as OAuthError,
        httpStatusCode: statusCode,
      };
    } else {
      throw error;
    }
  }
}
```

### Create setup token endpoint

```typescript lines expandable theme={null}
app.post(
  "/paypal-api/vault/setup-token/create",
  async (_req: Request, res: Response) => {
    try {
      const { jsonResponse, httpStatusCode } =
        await createSetupTokenWithSampleDataForPayPal();
      res.status(httpStatusCode).json(jsonResponse);
    } catch (error) {
      console.error("Failed to create setup token:", error);
      res.status(500).json({ error: "Failed to create setup token." });
    }
  },
);

export async function createSetupTokenWithSampleDataForPayPal() {
  const defaultSetupTokenRequestBody = {
    paymentSource: {
      paypal: {
        experienceContext: {
          cancelUrl: "https://example.com/cancelUrl",
          returnUrl: "https://example.com/returnUrl",
          vaultInstruction: VaultInstructionAction.OnPayerApproval,
        },
        usageType: PaypalPaymentTokenUsageType.Merchant,
      },
    },
  };

  return createSetupToken(defaultSetupTokenRequestBody, Date.now().toString());
}

export async function createSetupToken(
  setupTokenRequestBody: SetupTokenRequest,
  paypalRequestId?: string,
) {
  try {
    const { result, statusCode } = await vaultController.createSetupToken({
      body: setupTokenRequestBody,
      paypalRequestId,
    });

    return {
      jsonResponse: result,
      httpStatusCode: statusCode,
    };
  } catch (error) {
    if (error instanceof ApiError) {
      const { result, statusCode } = error;

      return {
        jsonResponse: result as CustomError,
        httpStatusCode: statusCode,
      };
    } else {
      throw error;
    }
  }
}
```

### Create payment token endpoint

Payment tokens are long-lived values for making future payments. PayPal recommends storing them in your database. Do not pass them to the browser.

```typescript lines expandable theme={null}
app.post(
  "/paypal-api/vault/payment-token/create",
  async (req: Request, res: Response) => {
    try {
      const { jsonResponse, httpStatusCode } = await createPaymentToken(
        req.body.vaultSetupToken as string,
      );

      const paymentTokenResponse = jsonResponse as PaymentTokenResponse;

      if (paymentTokenResponse.id) {
        // This payment token id is a long-lived value for making future payments.
        // PayPal recommends storing this value in your database
        // and NOT returning it back to the browser.
        await savePaymentTokenToDatabase(paymentTokenResponse);
        res.status(httpStatusCode).json({
          status: "SUCCESS",
          description:
            "Payment token saved to database for future transactions",
        });
      } else {
        res.status(httpStatusCode).json({
          status: "ERROR",
          description: "Failed to create payment token",
        });
      }
    } catch (error) {
      console.error("Failed to create payment token:", error);
      res.status(500).json({ error: "Failed to create payment token." });
    }
  },
);

export async function createPaymentToken(
  vaultSetupToken: string,
  paypalRequestId?: string,
) {
  try {
    const { result, statusCode } = await vaultController.createPaymentToken({
      paypalRequestId: paypalRequestId ?? Date.now().toString(),
      body: {
        paymentSource: {
          token: {
            id: vaultSetupToken,
            type: VaultTokenRequestType.SetupToken,
          },
        },
      },
    });

    return {
      jsonResponse: result,
      httpStatusCode: statusCode,
    };
  } catch (error) {
    if (error instanceof ApiError) {
      const { result, statusCode } = error;

      return {
        jsonResponse: result as CustomError,
        httpStatusCode: statusCode,
      };
    } else {
      throw error;
    }
  }
}

async function savePaymentTokenToDatabase(
  paymentTokenResponse: PaymentTokenResponse,
) {
  // example function to teach saving the paymentToken to a database
  // to be used for future transactions
  return Promise.resolve();
}
```

## Advanced features

The following code sample demonstrates how to configure a custom setup token.

### Configure custom setup token

```javascript lines expandable theme={null}
async function createCustomSetupToken(customerInfo = {}) {
  const customSetupTokenRequestBody = {
    payment_source: {
      paypal: {
        description: customerInfo.description || "Save PayPal payment method",
        usagePattern: customerInfo.usagePattern || "IMMEDIATE",
        usageType: customerInfo.usageType || "MERCHANT",
        customerType: customerInfo.customerType || "CONSUMER",
        permitMultiplePaymentTokens: customerInfo.allowMultiple || false,
      },
    },
    // Optional: Add customer information
    ...(customerInfo.customerId && {
      customer: {
        id: customerInfo.customerId,
      },
    }),
  };

  const response = await fetch("/paypal-api/vault/setup-token/create", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    // set up endpoint to parse request body
    body: JSON.stringify(customSetupTokenRequestBody),
  });

  const { id } = await response.json();
  return { setupToken: id };
}
```

## Resources

- [PayPal Payment Method Tokens (vault) API reference](https://developer.paypal.com/docs/api/payment-tokens/v3/)
- [PayPal Developer Dashboard](https://developer.paypal.com/dashboard/)
- [PCI Compliance Guidelines](https://www.pcisecuritystandards.org/)

## Support

For additional support and questions:

- Visit [PayPal Developer Community](https://developer.paypal.com/community/)
- Check [PayPal Developer Documentation](https://developer.paypal.com/docs/)
- Review the complete implementation:
  - [Client code](https://github.com/paypal-examples/v6-web-sdk-sample-integration/tree/main/client/components/paypalPayments/savePayment/html)
  - [Server code](https://github.com/paypal-examples/v6-web-sdk-sample-integration/tree/main/server/node)
