"""
Name: Michael Shieh
Section: CSE 163 AB
"""


def species_count(df):
    """
    This function takes on a DataFrame as data
    and returns how many unique number of names, i.e.,
    species found inside the list.
    """
    lst = list(df['name'].unique())
    return len(lst)


def max_level(df):
    """
    This function takes on a DataFrame as data
    and returns a tuple containing the name
    and level of the Pokemon with the highest level.
    """
    if len(df) == 0:
        return None

    level = df.groupby('name')['level'].max().max()
    name = df.groupby('name')['level'].max().idxmax()

    return (name, level)


def filter_range(df, a, b):
    """
    This function takes on a DataFrame as data
    and returns a list of names of Pokemon
    whose level in within the range between a (inclusive) and b (exclusive).
    The sequence of names should be identical to those appeared in the data.
    """
    larger_than_a = df['level'] >= a
    smaller_than_b = df['level'] < b
    name = df[larger_than_a & smaller_than_b]['name']

    if len(name) == 0:
        return []

    return list(name)


def mean_attack_for_type(df, type_name):
    """
    This function takes on a DataFrame as data
    along with a name of a specific Pokemon type
    and returns the mean of the attack stats of the specified type of Pokemons.

    If none of the Pokemon belongs to the specified type,
    this function should return None
    """
    groupby = df.groupby('type')['atk'].mean()

    if type_name not in groupby:
        return None
    else:
        return groupby[type_name]


def count_types(df):
    """
    This function takes on a DataFrame as data
    and returns a dictionary with all the type names as its keys
    and the number of times that type appears in the dataset.
    """
    types = df.groupby('type')['type'].count()
    return dict(types)


def highest_stage_per_type(df):
    """
    This function takes on a DataFrame as data
    and returns dictionary with all the type names as its key
    and the highest stage as the value.
    """
    stages = df.groupby('type')['stage'].max()
    return dict(stages)


def mean_attack_per_type(df):
    """
    This function takes on a DataFrame as data
    and returns dictionary with all the type names as its key
    and the mean value for attack stats as the value.
    """
    groupby = df.groupby('type')['atk'].mean()
    return dict(groupby)
