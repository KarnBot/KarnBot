import cmd
import unittest

from karnbot import cmd_decklist


class TestDecklist(unittest.TestCase):
    def test_get_decklist(self):
        result = cmd_decklist.get_deck(
            cmd_decklist.Players.Glen, cmd_decklist.ColorCombination.Yore
        )
        self.assertEqual(
            result,
            "glen - WUBR: Breya Bling - https://tappedout.net/mtg-decks/midrange-breya-1/",
        )

    def test_get_decklist_fail(self):
        result = cmd_decklist.get_deck(
            cmd_decklist.Players.TestUser, cmd_decklist.ColorCombination.Yore
        )
        self.assertEqual(result, "No deck found")
