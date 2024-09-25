---
id: classDataLoggerService
title: DataLoggerService Class
description: The [DataLoggerService](classDataLoggerService) class accesses the Data Logger service of Pokit devices.
tags:
---
The [DataLoggerService](classDataLoggerService) class accesses the Data Logger service of Pokit devices.



## Public Static Functions



DataLoggerService::toString
Returns mode as a user-friendly string.




DataLoggerService::toString
Returns range as a user-friendly string, or a null QString if mode has no ranges.




DataLoggerService::maxValue
Returns the maximum value for range, or the string "Auto".
If range is not a known valid enumeration value for product's mode, then a null QVariant is returned.



