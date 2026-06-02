<!-- Source URL: https://docs.stripe.com/terminal/features/collect-inputs -->
<!-- Fetched: 2026-05-01 -->

# Collect on-screen inputs

Use Terminal to collect inputs from your customers.

**Readers:** [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) and [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md)

With Terminal smart readers, you can display input forms and collect information from your customers. You can choose from six input types and they can be used in a variety of use cases.

- Collect your customer identifier for loyalty redemption with the `phone` or `email` input and process it on your backend.
- Have your customer acknowledge a waiver or agreement with the `signature` input.
- Ask your customer to fill out a questionnaire with the `selection` or `text` input.

You can display input forms anytime before payment, post payment and outside of a payment cycle.
![Supported input types](assets/stripe-terminal-collect-inputs-form-types.png)

Supported input types.

> Don’t use `collect_inputs` to collect sensitive data (including protected health information and customer payment card information), or any information restricted by law.

# Server-driven

> This is a Server-driven for when terminal-sdk-platform is server-driven. View the full page at https://docs.stripe.com/terminal/features/collect-inputs?terminal-sdk-platform=server-driven.

## Collect inputs

To collect inputs using Terminal’s smart readers, use the [collect_inputs](https://docs.stripe.com/api/terminal/readers/collect_inputs.md) command. The API communicates with the reader to display a prebuilt UI.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.collectInputs(
  '{{TERMINALREADER_ID}}',
  {
    inputs: [
      {
        type: 'signature',
        custom_text: {
          title: 'Rental Agreement',
          description: 'Please sign below to indicate that you agree to the rental agreement.',
          submit_button: 'Submit',
        },
        required: true,
      },
      {
        type: 'selection',
        selection: {
          choices: [
            {
              style: 'primary',
              text: 'Email',
              id: 'email_id',
            },
            {
              style: 'primary',
              text: 'Printed',
              id: 'printed_id',
            },
            {
              style: 'secondary',
              text: 'No thanks',
              id: 'no_thanks_id',
            },
          ],
        },
        custom_text: {
          title: 'Receipt',
          description: 'How would you like your receipt?',
        },
        required: true,
      },
      {
        type: 'email',
        custom_text: {
          title: 'Enter your email',
          description: 'We\'ll send updates on your order and occasional deals',
        },
        required: true,
        toggles: [
          {
            title: 'Opt-in for marketing emails',
            default_value: 'enabled',
          },
        ],
      },
    ],
    metadata: {
      order_number: '12345',
    },
  }
);
```

### Customization

You can customize the appearance and behavior of all input types:

- Set important inputs as [required](https://docs.stripe.com/api/terminal/readers/collect_inputs.md#collect_inputs-inputs-required) to ensure they’re collected. For required inputs, the **Skip** button is hidden.
- Provide context to your customer by specifying the text you want to display on the reader screen for each input using [custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs.md#collect_inputs-inputs-custom_text).

| Field name      | Field location                                                                                                                | Maximum characters                                                          |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --- |
| `title`         | [custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs.md#collect_inputs-inputs-custom_text-title)         | 40                                                                          |     |
| `description`   | [custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs.md#collect_inputs-inputs-custom_text-description)   | 500 when used with the `selection` form, 100 when used with other form type |
| `submit_button` | [custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs.md#collect_inputs-inputs-custom_text-submit_button) | 30                                                                          |     |
| `skip_button`   | [custom_text](https://docs.stripe.com/api/terminal/readers/collect_inputs.md#collect_inputs-inputs-custom_text-skip_button)   | 14                                                                          |     |

- Use line breaks `\n` in your text for better formatting.
- Add up to 4 [toggles](https://docs.stripe.com/api/terminal/readers/collect_inputs.md#collect_inputs-inputs-toggles) that customers can enable or disable for Boolean options, agreements, or opt-ins.
  ![Toggles in email and selection form](assets/stripe-terminal-collect-inputs-toggle.png)

Email and selection form with toggle

| Field name    | Field location                                                                                                      | Maximum characters                       |
| ------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `title`       | [toggles](https://docs.stripe.com/api/terminal/readers/collect_inputs.md#collect_inputs-inputs-toggles-title)       | 50, 25 when used with toggle description |
| `description` | [toggles](https://docs.stripe.com/api/terminal/readers/collect_inputs.md#collect_inputs-inputs-toggles-description) | 50, 25 when used with toggle title       |

- Additional customization is available for [selection](https://docs.stripe.com/api/terminal/readers/collect_inputs.md#collect_inputs-inputs-selection) inputs. When specifying the [choices](https://docs.stripe.com/api/terminal/readers/collect_inputs.md#collect_inputs-inputs-selection-choices), you can emphasize or de-emphasize choices using the [style](https://docs.stripe.com/api/terminal/readers/collect_inputs.md#collect_inputs-inputs-selection-choices-style) parameter.
  ![Selection choice styles](assets/stripe-terminal-collect-inputs-choice-style.png)

Primary and secondary selection choice styles

### Metadata

You can include [metadata](https://docs.stripe.com/api/terminal/readers/collect_inputs.md#collect_inputs-metadata), like a customer or order ID, in your request. The request payload includes the specified metadata, which appears in both the synchronous response and the success or failure events. By including a unique identifier, you can more easily identify and handle the incoming event.

## Customer interaction

When the reader begins collecting inputs, it displays the first input from the list. The customer must make a selection, provide a signature, or use the keyboard to proceed with required inputs. For optional inputs, the customer has the option to skip to the next requested input.

After the customer has completed all the inputs, the reader changes to a transitional state for 3 seconds, waiting for a subsequent request. If there is no subsequent request after 3 seconds, the reader changes back to the splash screen.

> You are fully responsible for being aware of, and complying with all applicable laws and regulations governing your use of this feature, and must in relation to such use, obtain, as applicable, all necessary consents, authorizations, licenses, rights, and permissions. If you use input collected by, or output displayed from a Terminal smart reader to enter into contracts with, or provide notices to your customers, you are fully responsible for ensuring the legal validity and enforceability of such contracts or notices.

## Receive input data

When all inputs have been collected or skipped, Stripe sends a request to your webhook endpoint. The request payload is identical to the response when calling [collect_inputs](https://docs.stripe.com/api/terminal/readers/collect_inputs.md), but adds a few additional parameters:

- For signature type inputs, the [value](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-collect_inputs-inputs-signature-value) is a [file ID](https://docs.stripe.com/api/files/object.md#file_object-id) that [retrieves](https://docs.stripe.com/api/files/retrieve.md) the signature image as an SVG.
- For selection type inputs, the [id](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-collect_inputs-inputs-selection-id) and [text](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-collect_inputs-inputs-selection-text) correspond to the selected choice’s `id` and `text`.
- For phone, email, text, and numeric inputs, the value is the string of the customer’s response.
- If an optional input is skipped by the customer, the [skipped](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-collect_inputs-inputs-skipped) parameter is set to `true`.
- The [value](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-collect_inputs-inputs-toggles-value) of each toggle is populated with `enabled` or `disabled`.

Use the curl command below as an example to create a webhook endpoint to receive the collected inputs.

```bash
curl https://api.stripe.com/v1/webhook_endpoints \
  -u <<YOUR_SECRET_KEY>>: \
  --header "Stripe-Version: 2025-05-28.basil;" \
  --data-urlencode "url"="https://example.com/webhook/endpoint" \
  --data-urlencode "api_version"="2025-05-28.basil;" \
  --data-urlencode "enabled_events[]"="terminal.reader.action_succeeded" \
  --data-urlencode "enabled_events[]"="terminal.reader.action_failed"
```

Subscribe to events to receive collected inputs as soon as they’re available. Alternatively, you can [retrieve the events](https://docs.stripe.com/api/terminal/readers/retrieve.md) from the reader as a backup if your backend fails to consume the event. Stripe sends two webhooks to notify your backend of the reader’s status:

- `terminal.reader.action_succeeded`: Sent when a `collect_inputs` action succeeds.
- `terminal.reader.action_failed`: Sent when a `collect_inputs` action fails. This includes timeouts, which occur after the reader screen isn’t touched for 2 minutes.

## Download signature images

To download the collected signature image, [retrieve the file](https://docs.stripe.com/api/files/retrieve.md) and use your _secret key_ (Stripe APIs use your secret API key to authenticate requests from your server; you can use this key to make any API call on behalf of your account, such as creating a charge or performing a refund) to access its [url](https://docs.stripe.com/api/files/object.md#file_object-url).

> Stripe stores the signature images you collect for 7 days. If you need to use signature images more than 7 days after collecting them, download the file and store it. You are fully responsible for being aware of and complying with all laws that apply to your use, storage, and disclosure of your customers’ signatures.

# Javascript

> This is a Javascript for when terminal-sdk-platform is js. View the full page at https://docs.stripe.com/terminal/features/collect-inputs?terminal-sdk-platform=js.

## Collect Inputs

- [collectInputs (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#collect-inputs)

To collect inputs using Terminal’s smart readers, call `collectInputs` with the Terminal SDK, the SDK communicates with the reader to display a prebuilt UI. You can specify up to 5 inputs at a time, and the reader collects them in sequence. After the customer inputs their data, the SDK returns the collected data with a promise.

```js
const collectInputsParameters = {
  inputs: [
    {
      formType: 'signature',
      title: 'Please sign',
      description: 'Please sign if you agree to the terms and conditions',
      skipButtonText: 'skip',
      submitButtonText: 'Submit signature',
    },
    {
      formType: 'selection',
      title: 'Choose an option',
      description: 'Were you happy with our customer service?',
      required: true,
      selectionButtons: [
        {
          style: 'primary',
          text: 'Yes',
        },
        {
          style: 'secondary',
          text: 'No',
        },
      ],
      toggles: [
        {
          title: 'Sign up for promotional emails',
          defaultValue: 'enabled',
        },
      ],
    },
  ],
};

const result = await this.terminal.collectInputs(collectInputsParameters);
if ('error' in result) {
// Placeholder for handling exception
}
// Placeholder for handling collected inputs
```

### Customization

You can customize the appearance and behavior of all input types:

- Set important inputs as `required` to ensure they’re collected. For required inputs, the **Skip** button is hidden.
- Provide context to your customer by specifying the text you want to display on the reader screen for each input using `title` and `description`.

| Field name      | Maximum characters                                                              |
| --------------- | ------------------------------------------------------------------------------- |
| `title`         | 40                                                                              |
| `description`   | 500 when used with the `selection` form, 100 when used with any other form type |
| `submit_button` | 30                                                                              |
| `skip_button`   | 14                                                                              |

- Use line breaks `\n` in your text for better formatting.
- Add up to 4 toggles that customers can enable or disable for Boolean options, agreements, or opt-ins.
  ![Toggles in email and selection form](assets/stripe-terminal-collect-inputs-toggle.png)

Email and selection form with toggle

| Field name    | Maximum characters                       |
| ------------- | ---------------------------------------- |
| `title`       | 50, 25 when used with toggle description |
| `description` | 50, 25 when used with toggle title       |

- For `selection` type inputs, you can emphasize or de-emphasize `choices` using the `style` parameter.
  ![Selection choice styles](assets/stripe-terminal-collect-inputs-choice-style.png)

Primary and secondary selection choice styles.

## Customer interaction

When the reader begins collecting inputs, it displays the first input from the list.

After the customer has completed all the inputs, the reader changes to a transitional state for 3 seconds, waiting for a subsequent request. If there is no subsequent request after 3 seconds, the reader changes back to the splash screen.

> You are fully responsible for being aware of, and complying with all applicable laws and regulations governing your use of this feature, and must in relation to such use, obtain, as applicable, all necessary consents, authorizations, licenses, rights, and permissions. If you use input collected by, or output displayed from a Terminal smart reader to enter into contracts with, or provide notices to your customers, you are fully responsible for ensuring the legal validity and enforceability of such contracts or notices.

## Receive input data

When all inputs have been collected or skipped, the Terminal SDK returns the collected data.

- For signature type inputs, the returned data is a string in SVG format.
- For selection type inputs, the returned data are the selected button’s `text` and `id` fields.
- For phone, email, text, and numeric inputs, the returned data is the string of the customer’s response.
- If an optional input is skipped by the customer, the `skipped` Boolean is set to `true`.
- For each toggle, `enabled`, `disabled` or `skipped` is returned corresponding to the index of the input toggles list.

The Terminal SDK returns an error in the event of a canceled action, timed out collection, or other error.

## Test your integration

You can test your integration by using the SDK’s simulated reader. Before you can test input collection, you must first [connect to a simulated reader](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=simulated&terminal-sdk-platform=js).

The simulated reader supports simulating the following scenarios:

- Successful input collection without skipping any inputs
- Successful input collection with skipping all non-required inputs
- Failed input collection because of a timeout

When simulating successful input collection, the SDK returns a hard-coded value for each input based on the type.

```js
// Simulated internet reader must already be connected
collectInputsResult = {
    resultType: 'succeeded' as SimulatedCollectInputsResultType,
    skipBehavior: 'none' as SimulatedCollectInputsSkipBehavior,
} as ISimulatedCollectInputsResultSucceeded;
this.terminal.setSimulatorConfiguration({ collectInputsResult });
const collectInputsParameters = {
    inputs: // Placeholder for specifying the inputs you want to simulate collecting
};
const result = await this.terminal.collectInputs(collectInputsParameters);
if ('error' in result) {
    // Placeholder for handling exception
} else {
    // Placeholder for handling collected inputs
}
```

# iOS

> This is a iOS for when terminal-sdk-platform is ios. View the full page at https://docs.stripe.com/terminal/features/collect-inputs?terminal-sdk-platform=ios.

## Collect Inputs

- [collectInputs (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)collectInputs:completion:>)
- [iOS SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=ios) `4.4.0` and up

You can collect customer information even when the smart reader is [operating offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=internet).

To collect inputs using Terminal’s smart readers, call `collectInputs` with the Terminal SDK, the SDK communicates with the reader to display a prebuilt UI. You can specify up to 5 inputs at a time, and the reader collects them in sequence. After the customer inputs their data, the SDK returns the collected data with a callback.

#### Swift

```swift
let signatureInput = try SignatureInputBuilder(title: "Please sign")
    .setStripeDescription("Please sign if you agree to the terms and conditions")
    .setSkipButtonText("skip form")
    .setSubmitButtonText("Submit signature")
    .build()


let firstSelectionButton = try SelectionButtonBuilder(style: .primary, text: "Yes", id: "yes_id")
    .build()

let secondSelectionButton = try SelectionButtonBuilder(style: .secondary, text: "No", id: "no_id")
    .build()

let firstToggle = try ToggleBuilder(defaultValue: .enabled)
    .setTitle("Sign up for promotional emails")
    .build()

let selectionInput = try SelectionInputBuilder(title: "Choose an option")
    .setStripeDescription("Were you happy with our customer service?")
    .setRequired(true)
    .setSelectionButtons([firstSelectionButton, secondSelectionButton])
    .setToggles([firstToggle])
    .build()

let collectInputsParams = try CollectInputsParametersBuilder(
    inputs: [signatureInput, selectionInput]
).build()

let cancelable = Terminal.shared.collectInputs(collectInputsParams) { (collectInputsResult, error) in
    if let error = error {
        // Placeholder for handling error
    } else if let result = collectInputsResult {
        // Placeholder for handling collected inputs
    }
}
```

### Customization

You can customize the appearance and behavior of all input types:

- Set important inputs as `required` to ensure they’re collected. For required inputs, the **Skip** button is hidden.
- Provide context to your customer by specifying the text you want to display on the reader screen for each input using `title` and `description`.

| Field name      | Maximum characters                                                              |
| --------------- | ------------------------------------------------------------------------------- |
| `title`         | 40                                                                              |
| `description`   | 500 when used with the `selection` form, 100 when used with any other form type |
| `submit_button` | 30                                                                              |
| `skip_button`   | 14                                                                              |

- Use line breaks `\n` in your text for better formatting.
- Add up to 4 toggles that customers can enable or disable for Boolean options, agreements, or opt-ins.
  ![Toggles in email and selection form](assets/stripe-terminal-collect-inputs-toggle.png)

Email and selection form with toggle

| Field name    | Maximum characters                       |
| ------------- | ---------------------------------------- |
| `title`       | 50, 25 when used with toggle description |
| `description` | 50, 25 when used with toggle title       |

- For `selection` type inputs, you can emphasize or de-emphasize `choices` using the `style` parameter.
  ![Selection choice styles](assets/stripe-terminal-collect-inputs-choice-style.png)

Primary and secondary selection choice styles.

## Customer interaction

When the reader begins collecting inputs, it displays the first input from the list.

After the customer has completed all the inputs, the reader changes to a transitional state for 3 seconds, waiting for a subsequent request. If there is no subsequent request after 3 seconds, the reader changes back to the splash screen.

> You are fully responsible for being aware of, and complying with all applicable laws and regulations governing your use of this feature, and must in relation to such use, obtain, as applicable, all necessary consents, authorizations, licenses, rights, and permissions. If you use input collected by, or output displayed from a Terminal smart reader to enter into contracts with, or provide notices to your customers, you are fully responsible for ensuring the legal validity and enforceability of such contracts or notices.

## Receive input data

When all inputs have been collected or skipped, the Terminal SDK returns the collected data.

- For signature type inputs, the returned data is a string in SVG format.
- For selection type inputs, the returned data are the selected button’s `text` and `id` fields.
- For phone, email, text, and numeric inputs, the returned data is the string of the customer’s response.
- If an optional input is skipped by the customer, the `skipped` Boolean is set to `true`.
- For each toggle, `enabled`, `disabled` or `skipped` is returned corresponding to the index of the input toggles list.

The Terminal SDK returns an error in the event of a canceled action, timed out collection, or other error.

## Test your integration

You can test your integration by using the SDK’s simulated reader. Before you can test input collection, you must first [connect to a simulated internet reader](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=simulated&terminal-sdk-platform=ios).

The simulated reader supports simulating the following scenarios:

- Successful input collection without skipping any inputs
- Successful input collection with skipping all non-required inputs
- Failed input collection because of a timeout

When simulating successful input collection, the SDK returns a hard-coded value for each input based on the type.

#### Swift

```swift
// Simulated internet reader must already be connected
Terminal.shared.simulatorConfiguration.simulatedCollectInputsResult = SimulatedCollectInputsResultSucceeded(
  simulatedCollectInputsSkipBehavior: .none
)

let collectInputsParams = try CollectInputsParametersBuilder(
    inputs: // Placeholder for specifying the inputs you want to simulate collecting
).build()

let cancelable = Terminal.shared.collectInputs(collectInputsParams) { (collectInputsResult, error) in
    if let error = error {
        // Placeholder for handling error
    } else if let result = collectInputsResult {
        // Placeholder for handling collected inputs
    }
}
```

# Android

> This is a Android for when terminal-sdk-platform is android. View the full page at https://docs.stripe.com/terminal/features/collect-inputs?terminal-sdk-platform=android.

## Collect Inputs

- [collectInputs (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/collect-inputs.html)
- [Android SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=android) `4.3.0` and up

You can collect customer information even when the smart reader is [operating offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=internet).

To collect inputs using Terminal’s smart readers, call `collectInputs` with the Terminal SDK, the SDK communicates with the reader to display a prebuilt UI. You can specify up to 5 inputs at a time, and the reader collects them in sequence. After the customer inputs their data, the SDK returns the collected data with a callback.

#### Kotlin

```kotlin
val collectInputsParameters = CollectInputsParameters(
    inputs = listOf(
        SignatureInput.Builder(title = "Please sign")
            .setDescription("Please sign if you agree to the terms and conditions")
            .setSkipButtonText("skip")
            .setSubmitButtonText("Submit signature")
            .build(),
        SelectionInput.Builder(title = "Choose an option")
            .setDescription("Were you happy with our customer service?")
            .setRequired(true)
            .setSelectionButtons(
                listOf(
                    SelectionButton(
                        style = SelectionButtonStyle.PRIMARY,
                        text = "Yes",
                        id = "yes_id"
                    ),
                    SelectionButton(
                        style = SelectionButtonStyle.SECONDARY,
                        text = "No",
                        id = "no_id"
                    )
                )
            )
            .setToggles(
                listOf(
                    Toggle(
                        title = "Sign up for promotional emails",
                        defaultValue = ToggleValue.ENABLED
                    )
                )
            )
            .build()
    )
)

val cancelable = Terminal.getInstance().collectInputs(
    collectInputsParameters,
    object : CollectInputsResultCallback {
        override fun onSuccess(results: List<CollectInputsResult>) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

### Customization

You can customize the appearance and behavior of all input types:

- Set important inputs as `required` to ensure they’re collected. For required inputs, the **Skip** button is hidden.
- Provide context to your customer by specifying the text you want to display on the reader screen for each input using `title` and `description`.

| Field name      | Maximum characters                                                              |
| --------------- | ------------------------------------------------------------------------------- |
| `title`         | 40                                                                              |
| `description`   | 500 when used with the `selection` form, 100 when used with any other form type |
| `submit_button` | 30                                                                              |
| `skip_button`   | 14                                                                              |

- Use line breaks `\n` in your text for better formatting.
- Add up to 4 toggles that customers can enable or disable for Boolean options, agreements, or opt-ins.
  ![Toggles in email and selection form](assets/stripe-terminal-collect-inputs-toggle.png)

Email and selection form with toggle

| Field name    | Maximum characters                       |
| ------------- | ---------------------------------------- |
| `title`       | 50, 25 when used with toggle description |
| `description` | 50, 25 when used with toggle title       |

- For `selection` type inputs, you can emphasize or de-emphasize `choices` using the `style` parameter.
  ![Selection choice styles](assets/stripe-terminal-collect-inputs-choice-style.png)

Primary and secondary selection choice styles.

## Customer interaction

When the reader begins collecting inputs, it displays the first input from the list.

After the customer has completed all the inputs, the reader changes to a transitional state for 3 seconds, waiting for a subsequent request. If there is no subsequent request after 3 seconds, the reader changes back to the splash screen.

> You are fully responsible for being aware of, and complying with all applicable laws and regulations governing your use of this feature, and must in relation to such use, obtain, as applicable, all necessary consents, authorizations, licenses, rights, and permissions. If you use input collected by, or output displayed from a Terminal smart reader to enter into contracts with, or provide notices to your customers, you are fully responsible for ensuring the legal validity and enforceability of such contracts or notices.

## Receive input data

When all inputs have been collected or skipped, the Terminal SDK returns the collected data.

- For signature type inputs, the returned data is a string in SVG format.
- For selection type inputs, the returned data are the selected button’s `text` and `id` fields.
- For phone, email, text, and numeric inputs, the returned data is the string of the customer’s response.
- If an optional input is skipped by the customer, the `skipped` Boolean is set to `true`.
- For each toggle, `enabled`, `disabled` or `skipped` is returned corresponding to the index of the input toggles list.

The Terminal SDK returns an error in the event of a canceled action, timed out collection, or other error.

## Test your integration

You can test your integration using the SDK’s simulated reader. Before you can test input collection, you must first [connect to a simulated internet reader](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=simulated&terminal-sdk-platform=android).

The simulated reader supports simulating the following scenarios:

- Successful input collection without skipping any inputs
- Successful input collection with skipping all non-required inputs
- Failed input collection because of a timeout

When simulating successful input collection, the SDK returns a hard-coded value for each input based on the type.

#### Kotlin

```kotlin
// Simulated internet reader must already be connected
Terminal.getInstance().simulatorConfiguration = SimulatorConfiguration(
    simulatedCollectInputsResult = SimulatedCollectInputsResult.SimulatedCollectInputsResultSucceeded(
        simulatedCollectInputsSkipBehavior = SimulatedCollectInputsSkipBehavior.NONE,
    )
)
val collectInputsParameters = CollectInputsParameters(
    // Placeholder for specifying the inputs you want to simulate collecting
)

val cancelable = Terminal.getInstance().collectInputs(
    collectInputsParameters,
    object : CollectInputsResultCallback {
        override fun onSuccess(results: List<CollectInputsResult>) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

# React Native

> This is a React Native for when terminal-sdk-platform is react-native. View the full page at https://docs.stripe.com/terminal/features/collect-inputs?terminal-sdk-platform=react-native.

## Collect Inputs

- [collectInputs (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#collectInputs)

You can collect customer information even when the smart reader is [operating offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md?reader-type=internet).

To collect inputs using Terminal’s smart readers, call `collectInputs` with the Terminal SDK, the SDK communicates with the reader to display a prebuilt UI. You can specify up to 5 inputs at a time, and the reader collects them in sequence. After the customer inputs their data, the SDK returns the collected data with a promise.

```tsx
const { collectInputs } = useStripeTerminal();

const collectInputsParameters = {
  inputs: [
    {
      formType: FormType.SIGNATURE,
      title: 'Please sign',
      required: false,
      description: 'Please sign if you agree to the terms and conditions',
      skipButtonText: 'skip',
      submitButtonText: 'Submit signature',
    },
    {
      formType: FormType.SELECTION,
      title: 'Choose an option',
      required: true,
      description: 'Were you happy with our customer service?',
      selectionButtons: [
        { style: SelectionButtonStyle.PRIMARY, text: 'Yes' },
        { style: SelectionButtonStyle.SECONDARY, text: 'No' },
      ],
      toggles: [
        {
          title: 'Sign up for promotional emails',
          defaultValue: ToggleValue.ENABLED,
        },
      ],
    },
  ],
};

const response = await collectInputs(collectInputsParameters);

if (response.error) {
// Placeholder for handling exception
}
// Placeholder for handling collected inputs
```

### Customization

You can customize the appearance and behavior of all input types:

- Set important inputs as `required` to ensure they’re collected. For required inputs, the **Skip** button is hidden.
- Provide context to your customer by specifying the text you want to display on the reader screen for each input using `title` and `description`.

| Field name      | Maximum characters                                                              |
| --------------- | ------------------------------------------------------------------------------- |
| `title`         | 40                                                                              |
| `description`   | 500 when used with the `selection` form, 100 when used with any other form type |
| `submit_button` | 30                                                                              |
| `skip_button`   | 14                                                                              |

- Use line breaks `\n` in your text for better formatting.
- Add up to 4 toggles that customers can enable or disable for Boolean options, agreements, or opt-ins.
  ![Toggles in email and selection form](assets/stripe-terminal-collect-inputs-toggle.png)

Email and selection form with toggle

| Field name    | Maximum characters                       |
| ------------- | ---------------------------------------- |
| `title`       | 50, 25 when used with toggle description |
| `description` | 50, 25 when used with toggle title       |

- For `selection` type inputs, you can emphasize or de-emphasize `choices` using the `style` parameter.
  ![Selection choice styles](assets/stripe-terminal-collect-inputs-choice-style.png)

Primary and secondary selection choice styles.

## Customer interaction

When the reader begins collecting inputs, it displays the first input from the list.

After the customer has completed all the inputs, the reader changes to a transitional state for 3 seconds, waiting for a subsequent request. If there is no subsequent request after 3 seconds, the reader changes back to the splash screen.

> You are fully responsible for being aware of, and complying with all applicable laws and regulations governing your use of this feature, and must in relation to such use, obtain, as applicable, all necessary consents, authorizations, licenses, rights, and permissions. If you use input collected by, or output displayed from a Terminal smart reader to enter into contracts with, or provide notices to your customers, you are fully responsible for ensuring the legal validity and enforceability of such contracts or notices.

## Receive input data

When all inputs have been collected or skipped, the Terminal SDK returns the collected data.

- For signature type inputs, the returned data is a string in SVG format.
- For selection type inputs, the returned data are the selected button’s `text` and `id` fields.
- For phone, email, text, and numeric inputs, the returned data is the string of the customer’s response.
- If an optional input is skipped by the customer, the `skipped` Boolean is set to `true`.
- For each toggle, `enabled`, `disabled` or `skipped` is returned corresponding to the index of the input toggles list.

The Terminal SDK returns an error in the event of a canceled action, timed out collection, or other error.
