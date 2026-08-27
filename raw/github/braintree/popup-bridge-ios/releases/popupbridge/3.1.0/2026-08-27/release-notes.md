* Add `init(webView:returnURLScheme:prefersEphemeralWebBrowserSession:)` for the Venmo app switch flow. When a `returnURLScheme` is provided and the Venmo app is installed, PopupBridge sends that scheme to the web SDK as the return URL prefix (`window.popupBridge.getReturnUrlPrefix()`) so the Venmo app can deep-link back into your app.

