<!-- Source: PPRiskMagnes_5.5.0_XCF.dmg -->
<!-- Downloaded from: https://www.paypalobjects.com/magnes-repository/iOS/PPRiskMagnes_5.5.0_XCF.zip -->
<!-- Password: j5FAn5G5rsXD -->
<!-- Checksum (SHA-512): f4c0842dd9ad17fe0c1ead76d0fc3c4fc5189be224322203db42bfcb3549ac4ef93a28649e8c6ef8c6f3fd4074432b860fbd0f6ba24e583a41d5d3230c9e87d7 -->
<!-- Reviewed: 2026-04-15 -->
<!-- Detail directory: raw/magnes-ios-550/ -->
<!-- Files saved (read directly from these paths):
  raw/magnes-ios-550/README.md
  raw/magnes-ios-550/PPRiskMagnes.xcframework/Info.plist
  raw/magnes-ios-550/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Info.plist
  raw/magnes-ios-550/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Headers/PPRiskMagnes.h
  raw/magnes-ios-550/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Headers/PPRiskMagnes-Swift.h
  raw/magnes-ios-550/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Headers/MagnesCryptoUtil.h
  raw/magnes-ios-550/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Headers/MagnesSystemConfigUtils.h
  raw/magnes-ios-550/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Modules/module.modulemap
  raw/magnes-ios-550/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/arm64-apple-ios.swiftinterface
  raw/magnes-ios-550/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/Modules/PPRiskMagnes.swiftmodule/arm64-apple-ios.abi.json
  raw/magnes-ios-550/PPRiskMagnes.xcframework/ios-arm64/PPRiskMagnes.framework/PrivacyInfo.xcprivacy
-->
<!-- Deep-dive fallback: re-mount PPRiskMagnes_5.5.0_XCF.dmg from ~/Downloads using password j5FAn5G5rsXD -->

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/magnes-ios-550/README.md` | "Compiled with Xcode 12; XCFramework; minimum deployment target iOS 11.0" |
| `raw/magnes-ios-550/PPRiskMagnes.xcframework/Info.plist` | XCFramework manifest: two slices (ios-arm64 device + ios-arm64_x86_64-simulator) |
| `.../ios-arm64/PPRiskMagnes.framework/Info.plist` | Framework bundle metadata |
| `.../Headers/PPRiskMagnes.h` | Umbrella ObjC header; imports MagnesCryptoUtil + MagnesSystemConfigUtils |
| `.../Headers/PPRiskMagnes-Swift.h` | ObjC-compatible Swift API bridge (generated); MagnesSDK + MagnesResult interfaces |
| `.../Headers/MagnesCryptoUtil.h` | `getDCIdWithAppGuid:withTimestamp:` and `getMGIdWithAppGuid:withTimeStamp:withPairingId:withMGIDKey:` |
| `.../Headers/MagnesSystemConfigUtils.h` | `getCPUType`, `getCPUName`, `getHardwareModel`, `getKernelVersion` |
| `.../Modules/module.modulemap` | Clang module map; exports PPRiskMagnes + PPRiskMagnes.Swift |
| `.../Modules/PPRiskMagnes.swiftmodule/arm64-apple-ios.swiftinterface` | **Primary source of truth for public Swift API**: MagnesSDK enums, setUp, collect, collectAndSubmit, telemetry APIs |
| `.../Modules/PPRiskMagnes.swiftmodule/arm64-apple-ios.abi.json` | ABI stability manifest for library evolution |
| `.../PPRiskMagnes.framework/PrivacyInfo.xcprivacy` | Apple Privacy Manifest: UserDefaults (CA92.1), CoarseLocation, PreciseLocation, PerformanceData collected |

## Key findings from binary inspection

### Build info
- Swift 5.9, Xcode 12 compiled, target `arm64-apple-ios12.0` (README says 11.0 — swiftinterface is authoritative)
- Library evolution enabled (`-enable-library-evolution`)
- Slices: `ios-arm64` (device) + `ios-arm64_x86_64-simulator`
- Framework-level code signature present (`_CodeSignature/`) — satisfies Apple Privacy Manifest requirement

### Discrepancies vs documentation

| Aspect | Docs | Binary |
| --- | --- | --- |
| `MagnesSource.DEFAULT` raw value | `-1` | `19` |
| `MagnesSource` cases | PAYPAL/EBAY/BRAINTREE/DEFAULT | Adds `SIMILITY=17`, `VENMO=18` |
| `setUp` parameters | No `disableBeacon` | Has `disableBeacon: Bool = false` |
| Min deployment target | iOS 11.0 (README) | iOS 12.0 (swiftinterface) |
| Telemetry APIs | Not documented | `registerTelemetry`, `unregisterTelemetry`, `collectTouchData`, `collectTelemetryData` |

### Privacy manifest declares
- `NSPrivacyAccessedAPICategoryUserDefaults` (reason: CA92.1)
- Collects: CoarseLocation, PreciseLocation, PerformanceData — all linked, not for tracking, purpose: App Functionality
