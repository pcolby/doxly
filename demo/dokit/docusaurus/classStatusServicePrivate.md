---
id: classStatusServicePrivate
title: StatusServicePrivate Class
description: The [StatusServicePrivate](classStatusServicePrivate) class provides private implementation for [StatusService](classStatusService).
tags:
---
The [StatusServicePrivate](classStatusServicePrivate) class provides private implementation for [StatusService](classStatusService).



## Public Static Functions



StatusServicePrivate::parseDeviceCharacteristics
Parses the Device Characteristics value into a DeviceCharacteristics struct.




StatusServicePrivate::parseStatus
Parses the Status value into a Status struct.
Note, not all Pokit devices support all members in Status. Specifically, the batteryStatus member is not usually set by Pokit Meter devices, so will be an invlalid BatteryStatus enum value (255) in that case.



StatusServicePrivate::parseTorchStatus
Parses the torch status value, and returns the corresponding TorchStatus.




StatusServicePrivate::parseButtonPress
Parses the button press value, and returns the corresponding ButtonStatus.




