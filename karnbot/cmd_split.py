# Library commands for split
import math
import random

def split_group(people):
    num_tables = get_num_tables(len(people))
    tables = [[] for _ in range(num_tables)]
    random_order = randomize_people(people)
    return assign_tables(random_order, tables)


def randomize_people(people):
    return random.sample(people, k=len(people))


def get_num_tables(num_people):
    return max(int(math.ceil(num_people / 4.0)), 1)


def assign_tables(people, tables):
    for (i, person) in enumerate(people):
        tables[i % len(tables)].append(person)
    return tables
