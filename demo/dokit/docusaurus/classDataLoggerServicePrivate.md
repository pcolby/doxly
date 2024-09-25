---
id: classDataLoggerServicePrivate
title: DataLoggerServicePrivate Class
description: The [DataLoggerServicePrivate](classDataLoggerServicePrivate) class provides private implementation for [DataLoggerService](classDataLoggerService).
tags:
---
The [DataLoggerServicePrivate](classDataLoggerServicePrivate) class provides private implementation for [DataLoggerService](classDataLoggerService).



## Public Static Functions



DataLoggerServicePrivate::encodeSettings
Returns settings in the format Pokit devices expect.
If updateIntervalIs32bit is true then the Update Interval field will be encoded in 32-bit instead of 16.



DataLoggerServicePrivate::parseMetadata
Parses the Metadata value into a DataLoggerService::Metatdata struct.




DataLoggerServicePrivate::parseSamples
Parses the Reading value into a [DataLoggerService::Samples](classDataLoggerService_1a59612dc26aa6b9a6d57be1014b04581b) vector.




