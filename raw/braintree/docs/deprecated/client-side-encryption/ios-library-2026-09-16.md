<!-- Source URL: https://developer.paypal.com/braintree/docs/deprecated/client-side-encryption/ios-library -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: iOS
slug: /docs/deprecated/client-side-encryption/ios-library/
createTime: '2025-04-02T01:16:44.068Z'
updateTime: '2025-04-02T01:16:44.084Z'
---



# iOS


**NOTE**
The integration method outlined below is deprecated. [Learn more about upgrading to the Braintree SDKs.](/braintree/docs/reference/general/upgrade) 


## Overview

The legacy iOS SDK consists of two main components:[Payment Form](#payment-form): A beautiful, polished credit card entry form complete with
built-in validations, ready for you to drop into your app.[Encryption](#encryption):
Client-side encryption allowing you to encrypt credit card data before sending it to your servers
and on to the gateway, making PCI compliance a breeze. These components are designed to work
together, but can be used independently of each other. The iOS SDK is designed to be used in
conjunction with a web server using one of Braintree’s server-side client libraries. The iOS SDK
does not support interacting with the gateway directly.
## Payment form

To initialize yourBtPaymentViewControllerin your payment form view controller’s .h
file,
- Import BTPaymentViewController.h
- Adopt the BTPaymentViewControllerDelegate protocol

Create and present a BTPaymentViewController to collect a user’s credit card information. The
following code initializes the payment form:```language-ios
BTPaymentViewController *paymentViewController = [BTPaymentViewController paymentViewControllerWithVenmoTouchEnabled:NO];
paymentViewController.delegate = self;
```
In this example we present the payment form modally, but you could also push it on a navigation
controller as well. Before we push the paymentViewController modally, we make it the
rootViewController of a UINavigationController to get default navigation bar styling and so users
can see a "Cancel" button:```language-ios
// Add paymentViewController to a navigation controller.
UINavigationController *paymentNavigationController =
[[UINavigationController alloc] initWithRootViewController:self.paymentViewController]; // Add a cancel button to the modal
self.paymentViewController.navigationItem.leftBarButtonItem =
[[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemCancel target:paymentNavigationController action:@selector(dismissModalViewControllerAnimated:)]; // Now, display the navigation controller that contains the payment form, eg modally:
[myViewController presentViewController:paymentNavigationController animated:YES completion:nil];
```
Now that we have the interface we need to handle user interactions. Venmo Touch handles two types of
user interaction: a save card flow where the user types their card in by hand and stores it in Venmo
Touch for later user (often by piggybacking on top of a transaction), and the use card flow where
the user uses a previously saved card without retyping their card information.
### Save card flow

Once the user enters their credit card information into the BTPaymentView, your app can access the
input via the BTPaymentViewControllerDelegate methods. In general, you should immediately be passing
this information to your server, so that you can then send it on to Braintree. When the user types
in their card information by hand the
paymentViewController:didSubmitCardWithInfo:andCardInfoEncrypted delegate method will be called.
Note that you receive raw, unencrypted info in the cardInfo dictionary, but for easy PCI Compliance,
you should use the cardInfoEncrypted dictionary to securely pass data through your servers to the
Braintree gateway:```language-ios
- (void)paymentViewController:(BTPaymentViewController *)paymentViewController didSubmitCardWithInfo:(NSDictionary *)cardInfo andCardInfoEncrypted:(NSDictionary *)cardInfoEncrypted { [self savePaymentInfoToServer:cardInfoEncrypted];
}
```

### Use card flow

When the user uses a card they already have stored in Venmo Touch, the
paymentViewController:didAuthorizeCardWithPaymentMethodCode delegate method will be called:```language-ios
- (void)paymentViewController:(BTPaymentViewController *)paymentViewController didAuthorizeCardWithPaymentMethodCode:(NSString *)paymentMethodCode { NSMutableDictionary *paymentInfo = [NSMutableDictionary dictionaryWithObject:paymentMethodCode forKey:@"venmo_sdk_payment_method_code"]; [self savePaymentInfoToServer:paymentInfo];
}
```

### Putting it all together

The following example code demonstrates how to pass encrypted card data from the app to your server,
and then to the Braintree gateway. For a fully working example of how to proxy data through your
server to the Braintree gateway, see the sample-checkout-heroku project on GitHub. (See also, the
server-side documentation). Below is a sample implementation of a method, savePaymentInfoToServer,
which passes card data from the client to your server (and then to the Braintree gateway). If card
data is valid and added to your Vault, display a success message, and dismiss the
BTPaymentViewController. You should then call the cleanup method, prepareForDismissal, before
dismissing the BTPaymentViewController.```language-ios
- (void) savePaymentInfoToServer:(NSDictionary *)paymentInfo { NSURL *url = [NSURL URLWithString: @"http://localhost:5000/card"]; NSMutableURLRequest *request = [[NSMutableURLRequest alloc] initWithURL:url]; // You need a customer id in order to save a card to the Braintree vault. // Here, for the sake of example, we set customer_id to device id. // In practice, this is probably whatever user_id your app has assigned to this user. NSString *customerId = [[UIDevice currentDevice] identifierForVendor].UUIDString; [paymentInfo setValue:customerId forKey:@"customer_id"]; request.HTTPBody = [self postDataFromDictionary:paymentInfo]; request.HTTPMethod = @"POST"; [NSURLConnection sendAsynchronousRequest:request queue:[NSOperationQueue mainQueue] completionHandler:^(NSURLResponse *response, NSData *body, NSError *requestError) { NSError *err = nil; NSDictionary *responseDictionary = [NSJSONSerialization JSONObjectWithData:body options:kNilOptions error:&err]; NSLog(@"saveCardToServer: paymentInfo: %@ response: %@, error: %@", paymentInfo, responseDictionary, requestError); if ([[responseDictionary valueForKey:@"success"] isEqualToNumber:@1]) { // Success! // Don't forget to call the cleanup method, // `prepareForDismissal`, on your `BTPaymentViewController` [self.paymentViewController prepareForDismissal]; // Now you can dismiss and tell the user everything worked. [self dismissViewControllerAnimated:YES completion:^(void) { [[[UIAlertView alloc] initWithTitle:@"Success" message:@"Saved your card!" delegate:nil cancelButtonTitle:@"OK" otherButtonTitles:nil] show]; }]; } else { // Card did not save correctly, so show server error using `showErrorWithTitle` [self.paymentViewController showErrorWithTitle:@"Error saving your card" message:[self messageStringFromResponse:responseDictionary]]; } }];
}
```
The above example assumes you have implemented some boiler-plate networking code such as
messageStringFromResponse, postDataFromDictionary, and URLEncodedStringFromString. You can find
example implementations of these methods in the Braintree sample code on GitHub.
### Error handling

The user’s credit card is declined, you should display an error message to the user via the
convenience method BTPaymentViewController showErrorWithTitle. Using the credit card may fail when,
for example:
- CVV verification does not pass.
- AVS verification does not pass.
- The card number was invalid.
- For more on card verification, see the list of possible processor responses.


## Encryption


### Configuration

Retrieve your client side encryption key from either the[Braintree gateway](https://www.braintreegateway.com/)or the[Braintree sandbox](https://sandbox.braintreegateway.com/login). Configure the library to
use your public key:```language-ios
BTEncryption *braintree = [[BTEncryption alloc] initWithPublicKey:@"YOUR_CLIENT_SIDE_ENCRYPTION_KEY"];
```
And call the encrypt method passing in the data you wish to be encrypted.```language-ios
NSString *encryptedValue = [braintree encryptString: @"sensitiveValue"];
```
Braintree client side encryption is asymmetric. Once you encrypt the data, the Braintree gateway
will be able to decrypt it but you will not. This means that encryptedValue is now safe to pass
through your servers and use in API calls with one of our server client libraries.
### Example

The normal use case is to encrypt a credit card number and CVV code before data is submitted to your
servers. A simple example of a UIViewController might look something like this:```language-ios
// MainViewController.h @interface MainViewController : UIViewController &lt;uitableviewdelegate, UITableViewDataSource&gt; { UITableView *formTable; UITableViewCell *ccNumberCell; UITableViewCell *ccExpirationCell; UITextField *ccNumberField; UITextField *ccExpirationField; NSDictionary *cells;
} extern NSString* const PUBLIC_KEY; @property(nonatomic, retain) IBOutlet UITableView *formTable;
@property(nonatomic, retain) IBOutlet UITableViewCell *ccNumberCell;
@property(nonatomic, retain) IBOutlet UITableViewCell *ccExpirationCell;
@property(nonatomic, retain) IBOutlet UITextField *ccNumberField;
@property(nonatomic, retain) IBOutlet UITextField *ccExpirationField; @property(nonatomic, retain) NSDictionary *cells; -(IBAction) formSubmitted:(id) sender;
-(void) showAlertWithMessage:(NSString *) message;
-(NSDictionary *) getFormData;
-(NSDictionary *) encryptFormData:(NSDictionary *) formData; @end
```
```language-ios
// MainViewController.m #import "MainViewController.h"
#import "BTEncryption.h"
#import "HTTPClient.h"
#import "JSONKit.h" @implementation MainViewController NSString * const PUBLIC_KEY = @"your-client-side-encryption-key"; @synthesize formTable, ccNumberField, ccExpirationField, ccNumberCell, ccExpirationCell, cells; - (IBAction) formSubmitted:(id) sender { HTTPClient * http = [[[HTTPClient alloc] init] autorelease]; [http postPath: @"/" parameters: [self encryptFormData: [self getFormData]] success: ^(AFHTTPRequestOperation *operation, id responseObject) { NSDictionary *response = [[JSONDecoder decoder] objectWithData: responseObject]; [self showAlertWithMessage: [NSString stringWithFormat: @"%@", response]]; } failure: ^(AFHTTPRequestOperation *operation, NSError *error) { [self showAlertWithMessage: [NSString stringWithFormat: @"%@", error]]; }];
} -(void) showAlertWithMessage: (NSString *) message { [[[[ UIAlertView alloc] initWithTitle: @"Submitted!" message: message delegate: self cancelButtonTitle: @"Ok! Thanks!" otherButtonTitles: nil] autorelease] show];
} -(NSDictionary *) encryptFormData:(NSDictionary *) formData { BTEncryption *braintree = [[[BTEncryption alloc] initWithPublicKey: PUBLIC_KEY] autorelease]; NSMutableDictionary *encryptedParams = [[[NSMutableDictionary alloc] init] autorelease]; [formData enumerateKeysAndObjectsUsingBlock:^(id key, id object, BOOL *stop) { [encryptedParams setObject: [braintree encryptString: object] forKey: key]; }]; return encryptedParams;
} -(NSDictionary *) getFormData { NSMutableDictionary *formData = [[[NSMutableDictionary alloc] init] autorelease]; [formData setObject: ccNumberField.text forKey: @"cc_number"]; [formData setObject: ccExpirationField.text forKey: @"cc_exp_date"]; return formData;
} - (UITableViewCell *) tableView:(UITableView *) tableview cellForRowAtIndexPath:(NSIndexPath *)indexPath { return [[cells allValues] objectAtIndex: [indexPath row]];
} - (BOOL) shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation { return (interfaceOrientation == UIInterfaceOrientationPortrait);
} - (void) didReceiveMemoryWarning { [super didReceiveMemoryWarning];
} - (void) viewDidUnload { [super viewDidUnload]; [formTable release]; [ccNumberField release]; [ccNumberCell release]; [ccExpirationField release]; [ccExpirationCell release]; [cells release];
} - (NSInteger) numberOfSectionsInTableView:(UITableView *)tableView { return 1; }
- (NSInteger) tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section { return [cells count]; }
- (NSString *) tableView:(UITableView *)tableView titleForHeaderInSection:(NSInteger)section { return nil; }
- (NSString *) tableView:(UITableView *)tableView titleForFooterInSection:(NSInteger)section { return nil; } - (void) viewDidLoad { cells = [[NSDictionary alloc] initWithObjectsAndKeys: ccNumberCell, @"creditCardNumber", ccExpirationCell, @"creditCardExpiration", nil]; [super viewDidLoad];
} @end
```
