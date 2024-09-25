---
id: classPokitDevice
title: PokitDevice Class
description: The [PokitDevice](classPokitDevice) class simplifies Pokit device access.
tags:
---
The [PokitDevice](classPokitDevice) class simplifies Pokit device access.
It does this by wrapping QLowEnergyController to provide:
* convenient Pokit service factory methods ([dataLogger()](classPokitDevice_1a77d94b8b0cf19bdbbd8f994e3c66c961), [deviceInformation()](classPokitDevice_1a1e04571a74d06fcc4608e70437b5fa5d), [dso()](classPokitDevice_1a3ded76591f3ec2b0620a2fbc617ed117), [multimeter()](classPokitDevice_1a7b4467f667ace65992a8fd152e9799ce) and [status()](classPokitDevice_1adaaaedcb434b3dda9608ad58192e9142)); and
* consistent debug logging of QLowEnergyController events.But this class is entirely optional, in that all features of all other QtPokit classes can be used wihtout this class. It's just a (meaningful) convenience.


## Public Static Functions



PokitDevice::serviceToString



PokitDevice::charcteristicToString



