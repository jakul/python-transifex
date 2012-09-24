python-transifex
----------------
A python API to the Transifex translation service (www.transifex.com). This API wrapper makes it easier to communicate with Transifex. The wrapper does not expose all of the underlying functionality of the Transifex API.

This wrapper is compatible with both www.transifex.com and Transifex Community Edition (self hosted).

ChangeLog
---------
0.1.7
=====
* Downgrade requests version to ensure compatibility with current code

0.1.6
=====
* Update setup.py to only include the actual requirements needed to install. Thanks to Toshio Kuratomi (https://github.com/jakul/python-transifex/pull/3)
* Fix tests which now throw InvalidSlugException. Thanks to Toshio Kuratmi (https://github.com/jakul/python-transifex/pull/4)

0.1.5
=====
* add new InvalidSlugException; make exceptions share a base class
