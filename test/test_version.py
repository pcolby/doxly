# SPDX-FileCopyrightText: 2024 Paul Colby <git@colby.id.au>
# SPDX-License-Identifier: GPL-3.0-or-later

import unittest

import doxly
from doxly import version

class TestVersion(unittest.TestCase):

    def test_kind_plural(self):
        self.assertEqual(doxly.__version__, version.__version__)
        self.assertRegex(version.__version__, '(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(-(a|b|post|rc)[1-9]\d*)?')

if __name__ == '__main__':
    unittest.main()
