import unittest

from . import split


class TestSplit(unittest.TestCase):
    def test_split_group(self):
        split.split_group()
        self.assertTrue(True)
