# Library commands for decklists
from enum import Enum


class Players(str, Enum):
    Glen = "glen"
    TestUser = "__IGNORE_TEST_USER"


class ColorCombination(str, Enum):
    Colorless = "C"
    White = "W"
    Blue = "U"
    Black = "B"
    Red = "R"
    Green = "G"
    Azorius = "WU"
    Boros = "RW"
    Dimir = "UB"
    Golgari = "BG"
    Gruul = "RG"
    Izzet = "UR"
    Orzhov = "WB"
    Rakdos = "BR"
    Selesnya = "WG"
    Simic = "UG"
    Abzan = "WBG"
    Bant = "WUG"
    Esper = "WUB"
    Grixis = "UBR"
    Jeskai = "WUR"
    Jund = "BRG"
    Mardu = "WBR"
    Naya = "WRG"
    Sultai = "BUG"
    Temur = "BRG"
    Glint = "UBRG"
    Dune = "WBRG"
    Ink = "WURG"
    Witch = "WUBG"
    Yore = "WUBR"
    FiveColor = "WUBRG"


class _Entry:
    def __init__(self, name: str, link: str) -> None:
        self.name = name
        self.link = link

    def to_message(self) -> str:
        return f"{self.name} - {self.link}"


__database = {
    Players.Glen: {
        ColorCombination.Yore: _Entry(
            "Breya Bling", "https://tappedout.net/mtg-decks/midrange-breya-1/"
        )
    }
}


def get_deck(player: Players, combination: ColorCombination):
    msg = "No deck found"
    player_data = __database.get(player)
    if player_data:
        entry = player_data.get(combination)
        if entry:
            msg = f"{player.value} - {combination.value}: {entry.to_message()}"
    return msg
