"""
Name: Michael Shieh
Section: CSE 163 AB
"""


def species_count(data):
    """
    This function takes on the list as data
    where the elements of the list are dicionaries
    and returns how many unique number of names, i.e.,
    species found inside the list.
    """
    unique_species = set()
    for ele in data:
        unique_species.add(ele['name'])

    return len(unique_species)


def max_level(data):
    """
    This function takes on the list as data
    where the elements of the list are dictionaries
    and returns a tuple containing the name
    and level of the Pokemon with the highest level.
    """
    level = 0
    name = None

    for ele in data:
        if ele['level'] > level:
            level = ele['level']
            name = ele['name']

    return (name, level)


def filter_range(data, a, b):
    """
    This function takes on the list as data
    where the elements of the list are dictionaries
    and returns a list of names of Pokemon
    whose level in within the range between a (inclusive) and b (exclusive).
    The sequence of names should be identical to those appeared in the data.
    """
    lst = []
    for ele in data:
        if ele['level'] >= a and ele['level'] < b:
            lst.append(ele['name'])

    return lst


def mean_attack_for_type(data, type_name):
    """
    This function takes on the list as data
    where the elements of the list are dictionaries
    along with a name of a specific Pokemon type
    and returns the mean of the attack stats of the specified type of Pokemons.

    If none of the Pokemon belongs to the specified type,
    this function should return None
    """
    total = 0
    count = 0

    for ele in data:
        if ele['type'] == type_name:
            total += ele['atk']
            count += 1

    if total == 0:
        return None
    else:
        return total/count

    # mean = mean_attacl_per_type(data)[type_name]
    # if mean >= 0:
    #    return mean
    # else:
    #    return None


def count_types(data):
    """
    This function takes on the list as data
    where the elements of the list are dictionaries
    and returns a dictionary with all the type names as its keys
    and the number of times that type appears in the dataset.
    """
    type_dict = {}
    for ele in data:
        if ele['type'] not in type_dict:
            type_dict[ele['type']] = 1
        else:
            type_dict[ele['type']] += 1

    return type_dict


def highest_stage_per_type(data):
    """
    This function takes on the list as data
    where the elements of the list are dictionaries
    and returns dictionary with all the type names as its key
    and the highest stage as the value.
    """
    highest_stage = {}
    for ele in data:
        if ele['type'] not in highest_stage:
            highest_stage[ele['type']] = ele['stage']
        elif ele['stage'] > highest_stage[ele['type']]:
            highest_stage[ele['type']] = ele['stage']

    return highest_stage


def mean_attack_per_type(data):
    """
    This function takes on the list as data
    where the elements of the list are dictionaries
    and returns dictionary with all the type names as its key
    and the mean value for attack stats as the value.
    """
    poke_type = {}

    for ele in data:
        if ele['type'] not in poke_type:
            poke_type[ele['type']] = [ele['atk']]
        else:
            poke_type[ele['type']].append(ele['atk'])

    for key in poke_type.keys():
        poke_type[key] = sum(poke_type[key]) / len(poke_type[key])

    return poke_type
