import unittest

import cmd_split


class TestSplit(unittest.TestCase):
    def test_split_group(self):
        cmd_split.split_group()
        self.assertTrue(True)
