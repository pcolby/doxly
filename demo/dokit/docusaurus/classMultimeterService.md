---
id: classMultimeterService
title: MultimeterService Class
description: The [MultimeterService](classMultimeterService) class accesses the Multimeter service of Pokit devices.
tags:
---
The [MultimeterService](classMultimeterService) class accesses the Multimeter service of Pokit devices.



## Public Static Functions



MultimeterService::toString
Returns mode as a user-friendly string.




MultimeterService::toString
Returns range as a user-friendly string, or a null QString if mode has no ranges.




MultimeterService::maxValue
Returns the maximum value for range, or the string "Auto".
If range is not a known valid enumeration value for product's mode, then a null QVariant is returned.



