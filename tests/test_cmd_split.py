import unittest
from unittest.mock import patch

from karnbot import cmd_split


class TestSplit(unittest.TestCase):
    def test_split_group(self):
        expected_order = ["Anson", "Eric", "Glen"]
        with patch("random.sample", return_value=expected_order):
            result = cmd_split.split_group(["Glen", "Eric", "Anson"])
            self.assertListEqual(result[0], expected_order)

    def test_get_num_tables(self):
        self.assertEqual(cmd_split.get_num_tables(10), 3)
        self.assertEqual(cmd_split.get_num_tables(0), 1)

    def test_randomize_people(self):
        expected_order = ["Anson", "Eric", "Glen"]
        with patch("random.sample", return_value=expected_order):
            self.assertEqual(
                cmd_split.randomize_people(["Glen", "Anson", "Eric"]),
                expected_order,
            )

    def test_assign_tables__even(self):
        people = ["Anson", "Eric", "Glen", "Ben", "Zac", "Chris"]
        assigned = cmd_split.assign_tables(people, [[], []])
        self.assertListEqual(assigned[0], ["Anson", "Glen", "Zac"])
        self.assertListEqual(assigned[1], ["Eric", "Ben", "Chris"])

        assigned = cmd_split.assign_tables(people, [[], [], []])
        self.assertListEqual(assigned[0], ["Anson", "Ben"])
        self.assertListEqual(assigned[1], ["Eric", "Zac"])
        self.assertListEqual(assigned[2], ["Glen", "Chris"])

    def test_assign_tables__odd(self):
        people = ["Anson", "Eric", "Glen", "Ben", "Zac", "Chris", "Mike"]
        assigned = cmd_split.assign_tables(people, [[], []])
        self.assertListEqual(assigned[0], ["Anson", "Glen", "Zac", "Mike"])
        self.assertListEqual(assigned[1], ["Eric", "Ben", "Chris"])

        assigned = cmd_split.assign_tables(people, [[], [], []])
        self.assertListEqual(assigned[0], ["Anson", "Ben", "Mike"])
        self.assertListEqual(assigned[1], ["Eric", "Zac"])
        self.assertListEqual(assigned[2], ["Glen", "Chris"])
