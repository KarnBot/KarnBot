import random


def roll_dice(num_dice: int, num_sides: int, bonus: int = 0):
    rolls = [random.randint(1, num_sides) for _ in num_dice]
    result = sum(rolls) + bonus
    rolls_msg = ", ".join(rolls)
    bonus_msg = ""
    if bonus > 0:
        bonus_msg = f"+{bonus}"
    elif bonus < 0:
        bonus_msg = f"-{bonus}"
    message = f"{result} ({num_dice}d{num_sides}{bonus_msg}, [{rolls_msg}])"
    return message
