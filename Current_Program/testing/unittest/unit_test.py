# -*- coding: utf-8 -*-
import unittest
from unit import bro

class TestFactorial(unittest.TestCase):
    def test_bro(self):
        nyan = bro
        self.assertEqual(nyan,bro)


if __name__ == '__main__':
    unittest.main()