---
id: classAbstractCommand
title: AbstractCommand Class
description: The [AbstractCommand](classAbstractCommand) class provides a consistent base for the classes that implement CLI commands.
tags:
---
The [AbstractCommand](classAbstractCommand) class provides a consistent base for the classes that implement CLI commands.



## Public Static Functions



AbstractCommand::escapeCsvField
Returns an RFC 4180 compliant version of field.
That is, if field contains any of the the below four characters, than any double quotes are escaped (by addition double-quotes), and the string itself surrounded in double-quotes. Otherwise, field is returned verbatim.
Some examples: <listingType>



AbstractCommand::parseNumber
Returns value as an integer multiple of the ratio R.
The string value may end with the optional unit, such as V or s, which may also be preceded with a SI unit prefix such as m for milli. If value contains no SI unit prefix, then the result will be multiplied by 1,000 enough times to be greater than sensibleMinimum. This allows for convenient use like:
<listingType>
So that an unqalified period like "300" will be assumed to be 300 milliseconds, and not 300 microseconds, while a period like "1000" will be assume to be 1 second.
If conversion fails for any reason, 0 is returned.



