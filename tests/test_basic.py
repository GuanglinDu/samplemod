# -*- coding: utf-8 -*-
# If test_suite="tests" was not set in setup.py: python setup.test -s tests
# If test_suite="tests" was set in setup.py: python setup.test

from .context import sample # package
import sample.core          # package.module

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def test_absolute_truth_and_meaning(self):
        assert True

    def test_add(self):
        self.assertEqual(sample.core.add(1, 1), 2)
        self.assertNotEqual(sample.core.add(1, 1), 3)
        
        
if __name__ == '__main__':
    unittest.main()
