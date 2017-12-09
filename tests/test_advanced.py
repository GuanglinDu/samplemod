# -*- coding: utf-8 -*-
# If test_suite="tests" was not set in setup.py: python setup.test -s tests
# If test_suite="tests" was set in setup.py: python setup.test

from .context import sample # package
import sample.core          # package.module

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""
    def setUp(self):
        self.addition = sample.core.Addition(1, 1)
        
    def test_thoughts(self):
        self.assertIsNone(sample.hmm())

    def test_addition_add(self):
        self.assertEqual(self.addition.add(), 2)
        self.assertNotEqual(self.addition.add(), 3)


if __name__ == '__main__':
    unittest.main()
