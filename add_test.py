import unittest
from add import *

class TestCuboid(unittest.TestCase):
    def test_add(self):
        self.assertAlmostEqual(add(2,6),8)
        self.assertAlmostEqual(add(1.0,0.0),1.0)
        self.assertAlmostEqual(add(1.0,1.0),1.0)
