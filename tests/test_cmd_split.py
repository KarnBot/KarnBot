import unittest

from karnbot import cmd_split


class TestSplit(unittest.TestCase):
    def test_split_group(self):
        cmd_split.split_group([])
        self.assertTrue(True)

    def test_get_num_tables(self):
        self.assertEqual(cmd_split.get_num_tables(10), 3)
        self.assertEqual(cmd_split.get_num_tables(0), 1)
