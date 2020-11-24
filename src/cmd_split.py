# Library commands for split
import math
import random


def split_group(people):
    print("Starting split")
    num_tables = get_num_tables(len(people))
    tables = [[] for _ in range(num_tables)]
    print(f"Determined I need {num_tables} tables")


def get_num_tables(num_people):
    return max(int(math.ceil(num_people / 4.0)), 1)
