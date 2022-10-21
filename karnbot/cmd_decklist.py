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
        ColorCombination.Colorless: None,
        ColorCombination.White: _Entry(
            "Perfectly Fair",
            "https://tappedout.net/mtg-decks/teshar-is-perfectly-fair/",
        ),
        ColorCombination.Blue: _Entry(
            "Cosmic Control",
            "https://tappedout.net/mtg-decks/cosmic-control-3/",
        ),
        ColorCombination.Black: _Entry(
            "Yaheeni's Plan", "https://tappedout.net/mtg-decks/yaheenis-plan/"
        ),
        ColorCombination.Red: _Entry(
            "Norin the Troll",
            "https://tappedout.net/mtg-decks/norin-the-troll-2/",
        ),
        ColorCombination.Green: _Entry(
            "Zone Eater", "https://tappedout.net/mtg-decks/zone-eater/"
        ),
        ColorCombination.Azorius: _Entry(
            "Brago, Blinking Shanegians",
            "https://tappedout.net/mtg-decks/brago-blinking-shanegians/",
        ),
        ColorCombination.Boros: _Entry(
            "Scarlet Feathers",
            "https://tappedout.net/mtg-decks/scarlet-feathers/",
        ),
        ColorCombination.Dimir: _Entry(
            "Welsh It", "https://tappedout.net/mtg-decks/welsh-it/"
        ),
        ColorCombination.Golgari: _Entry(
            "Hogaak, Discard Engine",
            "https://tappedout.net/mtg-decks/hogaak-discard-engine/",
        ),
        ColorCombination.Gruul: _Entry(
            "Outrun my Gun", "https://tappedout.net/mtg-decks/outrun-my-gun/"
        ),
        ColorCombination.Izzet: _Entry(
            "Izzet Scramble", "https://tappedout.net/mtg-decks/izzet-scramble/"
        ),
        ColorCombination.Orzhov: _Entry(
            "Aristocrat Tokens",
            "https://tappedout.net/mtg-decks/31-10-20-aristocrat-tokens/",
        ),
        ColorCombination.Rakdos: _Entry(
            "Welcome to the Dungeon",
            "https://tappedout.net/mtg-decks/welcome-to-the-dungeon-4/",
        ),
        ColorCombination.Selesnya: _Entry(
            "Gabriel Garbagefire",
            "https://tappedout.net/mtg-decks/gabriel-garbagefire/",
        ),
        ColorCombination.Simic: _Entry(
            "Edric, Hugmaster",
            "https://tappedout.net/mtg-decks/edric-hugmaster-1/",
        ),
        ColorCombination.Abzan: None,
        ColorCombination.Bant: None,
        ColorCombination.Esper: _Entry(
            "Odd Control Fun",
            "https://tappedout.net/mtg-decks/odd-control-fun/",
        ),
        ColorCombination.Grixis: _Entry(
            "Tresserhorn Thriller",
            "https://tappedout.net/mtg-decks/tresserhorn-thriller/",
        ),
        ColorCombination.Jeskai: _Entry(
            "Sevinne's Storm", "https://tappedout.net/mtg-decks/sevinnes-storm/"
        ),
        ColorCombination.Jund: None,
        ColorCombination.Mardu: _Entry(
            "Isshin Combat Theory",
            "https://tappedout.net/mtg-decks/isshin-combat-theory/",
        ),
        ColorCombination.Naya: None,
        ColorCombination.Sultai: _Entry(
            "Big Sultai Mill Energy",
            "https://tappedout.net/mtg-decks/big-sultai-mill-energy/",
        ),
        ColorCombination.Temur: _Entry(
            "Temur Math problems [Not finished]",
            "https://tappedout.net/mtg-decks/temur-math-problems/",
        ),
        ColorCombination.Glint: _Entry(
            "Dragon Planeswalkers [Not finished]",
            "https://tappedout.net/mtg-decks/dragon-planeswalkers-2/",
        ),
        ColorCombination.Dune: None,
        ColorCombination.Ink: None,
        ColorCombination.Witch: _Entry(
            "Yet another Atraxa Superfriends",
            "https://tappedout.net/mtg-decks/yet-another-atraxa-superfriends-2/",
        ),
        ColorCombination.Yore: _Entry(
            "Breya Bling", "https://tappedout.net/mtg-decks/midrange-breya-1/"
        ),
        ColorCombination.FiveColor: _Entry(
            "Spell Engine", "https://tappedout.net/mtg-decks/spell-engine-1/"
        ),
    }
}


def get_combination(
    white: bool, blue: bool, black: bool, red: bool, green: bool
) -> ColorCombination:
    s = ""
    if white or blue or black or red or green:
        if white:
            s += "W"
        if blue:
            s += "U"
        if black:
            s += "B"
        if red:
            s += "R"
        if green:
            s += "G"
        return ColorCombination(s)
    else:
        return ColorCombination.Colorless


def get_deck(player: Players, combination: ColorCombination):
    msg = "No deck found"
    player_data = __database.get(player)
    if player_data:
        entry = player_data.get(combination)
        if entry:
            msg = f"{player} - {combination}: {entry.to_message()}"
    return msg
