---
id: classAbstractPokitServicePrivate
title: AbstractPokitServicePrivate Class
description: The [AbstractPokitServicePrivate](classAbstractPokitServicePrivate) class provides private implementation for [AbstractPokitService](classAbstractPokitService).
tags:
---
The [AbstractPokitServicePrivate](classAbstractPokitServicePrivate) class provides private implementation for [AbstractPokitService](classAbstractPokitService).



## Public Static Functions



AbstractPokitServicePrivate::Q_LOGGING_CATEGORY
Logging category.




AbstractPokitServicePrivate::checkSize
Returns false if data is smaller than minSize, otherwise returns failOnMax if data is bigger than maxSize, otherwise returns true.
A warning is logged if either minSize or maxSize is violated, regardless of the returned value; ie this funcion can be used to simply warn if data is too big, or it can be used to failed (return false) in that case.



AbstractPokitServicePrivate::toHexString
Returns up to maxSize bytes of data as a human readable hexadecimal string.
If data exceeds maxSize, then data is elided in the middle. For example:
<listingType>



