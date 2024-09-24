---
id: pokit
title: pokit Page
tags:
---

## Member [DataLoggerServicePrivate::encodeSettings](classDataLoggerServicePrivate_1a774d21863bf83168171143ec8492a736)  (const [DataLoggerService::Settings](structDataLoggerService_1_1Settings) &settings, const bool updateIntervalIs32bit)

* <a id="pokit_1_pokit000001"></a> For Pokit Meter, updateInterval is uint16 seconds (as per the Pokit API 1.00), however for Pokit Pro it's uint32 milliseconds, even though that's not officially documented anywhere.

## Member [DataLoggerServicePrivate::parseMetadata](classDataLoggerServicePrivate_1aed59b28db53cea0757289a0960bed3fd)  (const QByteArray &value)

* <a id="pokit_1_pokit000002"></a> For Pokit Meter, updateInterval is uint16 (as per the Pokit API 1.00), however for Pokit Pro it's uint32, even though that's not officially documented anywhere. Also note, the doc claims 'microseconds' (ie 10^-6), but clearly the value is 'milliseconds' (ie 10^-3) for Pokit Pro, and whole seconds for Pokit Meter.

## Member [DeviceInfoService::serialNumber](classDeviceInfoService_1a006859d13f7c3d7f4179a0ad9cc04213)  () const

* <a id="pokit_1_pokit000003"></a> Unlike other string characteristics, Pokit (Pro) devices always appear to add a trailing null byte to serial number strings. So here we strip any that are present.

## Member [MultimeterService::Mode](classMultimeterService_1a51f66d0b81dace3115c5c68bc931eaea)

* <a id="pokit_1_pokit000004"></a> The following enumeration values are as-yet undocumented by Pokit Innovations. [@pcolby](https://github.com/pcolby) reverse-engineered them as part of the [dokit](https://github.com/pcolby/dokit) project.
* [Mode::Capacitance](classMultimeterService_1a51f66d0b81dace3115c5c68bc931eaeaa22bef5ff8cc5db9cc862164e779f29dc)
* [Mode::ExternalTemperature](classMultimeterService_1a51f66d0b81dace3115c5c68bc931eaeaa8d6937c3adb213bd7b7beb575aa17687)

## Member [PokitPro::CapacitanceRange](namespacePokitPro_1adc67ba31bcd650dd7535939e42cec17a)

* <a id="pokit_1_pokit000005"></a> These Pokit Pro enumeration values are as-yet undocumented by Pokit Innovations. [@pcolby](https://github.com/pcolby) reverse-engineered them as part of the [dokit](https://github.com/pcolby/dokit) project.

## Member [PokitPro::CurrentRange](namespacePokitPro_1ac51059eb5a52fa362da01d4e2f44de21)

* <a id="pokit_1_pokit000006"></a> These Pokit Pro enumeration values are as-yet undocumented by Pokit Innovations. [@pcolby](https://github.com/pcolby) reverse-engineered them as part of the [dokit](https://github.com/pcolby/dokit) project.

## Member [PokitPro::ResistanceRange](namespacePokitPro_1ac6fedf42d1268613f25da2b7c82832a7)

* <a id="pokit_1_pokit000007"></a> These Pokit Pro enumeration values are as-yet undocumented by Pokit Innovations. [@pcolby](https://github.com/pcolby) reverse-engineered them as part of the [dokit](https://github.com/pcolby/dokit) project.

## Member [PokitPro::VoltageRange](namespacePokitPro_1a68ddba45fec73a3391f241f2da38e78a)

* <a id="pokit_1_pokit000008"></a> These Pokit Pro enumeration values are as-yet undocumented by Pokit Innovations. [@pcolby](https://github.com/pcolby) reverse-engineered them as part of the [dokit](https://github.com/pcolby/dokit) project.

## Member [StatusService::flashLed](classStatusService_1a425bf65d42b24c4a621b312fcd152708)  ()

* <a id="pokit_1_pokit000011"></a> The Android app can turn Pokit Pro LEDs on/off. Perhaps that is handled by an undocumented use of this characteristic. Or perhaps its via some other service.

## Struct [StatusService::ServiceUuids](structStatusService_1_1ServiceUuids)

* <a id="pokit_1_pokit000009"></a> Pokit API 1.00 (and 0.02) states the [Status](structStatusService_1_1Status) Service UUID as 57d3a771-267c-4394-8872-78223e92aec4 which is correct for the Pokit Meter, but Pokit Pro uses 57d3a771-267c-4394-8872-78223e92aec5 instead, that is the last digit is a 5 not 4.

## Member [StatusService::SwitchPosition](classStatusService_1a6bb2f85b6df9942ee108c341f4162e1f)

* <a id="pokit_1_pokit000010"></a> These enum values are undocumented, but easily testable with a physical Pokit Pro device. Internally, Pokit's Android app calls these: SWITCH_MODE_VOLTAGE, SWITCH_MODE_ALL and SWITCH_MODE_CURRENT.

## Member [StatusServicePrivate::parseButtonPress](classStatusServicePrivate_1a90d78c3261bea8f23ddf9804ada203c1)  (const QByteArray &value)

* <a id="pokit_1_pokit000013"></a> The button event is the second byte, but no idea what the first byte is. In all examples I've see it's always 0x02. It appears that the Pokit Android app only ever looks at bytes[1].<a id="pokit_1_pokit000014"></a> Note, we can actually write to the Button Press characteristic too. If we do, then whatever we set as the first byte persists, and (unsurprisingly) the second byte reverts to the current button state. So still no idea what that first byte is for.

## Member [StatusServicePrivate::parseStatus](classStatusServicePrivate_1a3a6ff8ca3e9d7c884b269e52dd43aeb0)  (const QByteArray &value)

* <a id="pokit_1_pokit000012"></a> Pokit API 0.02 says the Status characteristic is 5 bytes. API 1.00 then added an additional byte for Battery Status, for 6 bytes in total. However, Pokit Pro devices return 8 bytes here. It appears that the first of those 2 extra bytes (ie the 7th byte) is used to indicate the physical switch position, while the other extra byte (ie the 8th byte) indicates the device's current charging status.