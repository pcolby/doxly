---
id: classDsoService
title: DsoService Class
description: The [DsoService](classDsoService) class accesses the DSO (Digital Storage Oscilloscope) service of Pokit devices.
tags:
---
The [DsoService](classDsoService) class accesses the DSO (Digital Storage Oscilloscope) service of Pokit devices.



## Public Static Functions



DsoService::toString
Returns mode as a user-friendly string.




DsoService::toString
Returns range as a user-friendly string, or a null QString if mode has no ranges.




DsoService::maxValue
Returns the maximum value for range, or the string "Auto".
If range is not a known valid enumeration value for product's mode, then a null QVariant is returned.



