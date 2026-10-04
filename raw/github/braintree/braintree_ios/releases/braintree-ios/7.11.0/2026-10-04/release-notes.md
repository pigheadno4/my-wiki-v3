* BraintreeDataCollector
  * Fix bug with revoked Magnes certificate (fixes #1857) - Error: The signature of "PPRiskMagnes.xcframework" cannot be validated and may have been compromised. Validation Error: The signing certificate has been revoked (CSSMERR_TP_CERT_REVOKED)
  * Migrate PPRiskMagnes from a locally vendored xcframework to a remotely hosted binary artifact at https://github.com/paypal/paypal-risk-ios (v5.6.0)
  * This version of the PPRiskMagnes framework is dynamic (previously static) to support package managers
  * SPM: Package.swift now depends on the `paypal-risk-ios` package and references its `PayPalRisk` product -- no consumer action required
  * CocoaPods: DataCollector subspec now depends on the `PayPalRisk` pod instead of vendoring the xcframework locally
    * If your Podfile uses `use_frameworks! :linkage => :static` (or omits `use_frameworks!` entirely), note that PPRiskMagnes is now a dynamic framework and will be embedded in your app
  * Carthage: Cartfile now references the JSON manifest from the paypal-risk-ios repository instead of a local xcframework
    * Run `carthage update --use-xcframeworks` after upgrading
    * **Action required:** Because PPRiskMagnes is now dynamic, add `PPRiskMagnes.xcframework` to your target's "Embed Frameworks" build phase (copy-frameworks Input Files) -- this was not required when the framework was static
  * No source code changes required -- `import PPRiskMagnes` remains unchanged

