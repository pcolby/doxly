# SPDX-FileCopyrightText: 2024 Paul Colby <git@colby.id.au>
# SPDX-License-Identifier: GPL-3.0-or-later

import unittest

from doxly import doxly

class TestDoxly(unittest.TestCase):

    def test_kind_plural(self):
        self.assertEqual(doxly._kind_plural('category'), 'categories')
        self.assertEqual(doxly._kind_plural('class'), 'classes')
        self.assertEqual(doxly._kind_plural('property'), 'properties')
        self.assertEqual(doxly._kind_plural(''), 's')
        self.assertEqual(doxly._kind_plural('abc'), 'abcs')

if __name__ == '__main__':
    unittest.main()
