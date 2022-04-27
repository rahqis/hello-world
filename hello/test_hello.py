"""sample test"""
import unittest
from __init__ import addx, subx, multx, divx
from hello import hello


class TestHello(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        self.assertEqual(hello('world'), 'hello world')

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(hello(u'world'), u'hello world')

    def test_addx(self):
        self.assertEqual(addx(1, 1), 2)

    def test_addx_neg(self):
        self.assertEqual(addx(1, -2), -1)

    def test_subx(self):
        self.assertEqual(subx(1, 1), 0)

    def test_multx(self):
        self.assertEqual(multx(2, 2), 4)

    def test_divx(self):
        self.assertEqual(divx(6, 2), 3)
