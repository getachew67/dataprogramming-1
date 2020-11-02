"""
Name: Michael Shieh
Section: CSE 163 AB

This file contains all the tests to examine
if the functions defined are valid.
If passed, each function should print nothing.
"""
import pandas as pd

# Don't worry about this import syntax, we will talk about it later
# You can call the method using
#    assert_equals(expected, received)
#    parse(file)
from cse163_utils import assert_equals, parse

import hw2_manual as hm
import hw2_pandas as hp


def test_species_count(data, df):
    """
    This function tests the "specific_count" function from both
    hw2_manual and hw2_pandas
    """
    assert_equals(3, hm.species_count(data))
    assert_equals(3, hp.species_count(df))
    print("species_count test passed.")


def test_max_level(data, df):
    """
    This function tests the "max_level" function from both
    hw2_manual and hw2_pandas
    """
    assert_equals(('Lapras', 72), hm.max_level(data))
    assert_equals(('Lapras', 72), hp.max_level(df))
    print("max_level test passed.")


def test_filter_range(data, df):
    """
    This function tests the "filter_range" function from both
    hw2_manual and hw2_pandas
    """
    assert_equals(
        ['Arcanine', 'Arcanine', 'Starmie'], hm.filter_range(data, 30, 70))
    assert_equals(
        ['Arcanine', 'Arcanine', 'Starmie'], hp.filter_range(df, 30, 70))
    print("filter_range test passed.")


def test_mean_attack_for_type(data, df):
    """
    This function tests the "mean_attack_for_type" function from both
    hw2_manual and hw2_pandas
    """
    assert_equals(47.5, hm.mean_attack_for_type(data, 'fire'))
    assert_equals(47.5, hp.mean_attack_for_type(df, 'fire'))
    print("mean_attack_for_type test passed.")


def test_count_types(data, df):
    """
    This function tests the "count_type" function from both
    hw2_manual and hw2_pandas
    """
    assert_equals({'water': 2, 'fire': 2}, hm.count_types(data))
    assert_equals({'water': 2, 'fire': 2}, hp.count_types(df))
    print("count_types test passed.")


def test_highest_stage_per_type(data, df):
    """
    This function tests the "highest_stage_per_type" function from both
    hw2_manual and hw2_pandas
    """
    assert_equals({'water': 2, 'fire': 2}, hm.highest_stage_per_type(data))
    assert_equals({'water': 2, 'fire': 2}, hp.highest_stage_per_type(df))
    print("highest_stage_per_type test passed.")


def test_mean_attack_per_type(data, df):
    """
    This function tests the "highest_stage_per_type" function from both
    hw2_manual and hw2_pandas
    """
    assert_equals(
        {'water': 140.5, 'fire': 47.5}, hm.mean_attack_per_type(data))
    assert_equals(
        {'water': 140.5, 'fire': 47.5}, hp.mean_attack_per_type(df))
    print("mean_attack_per_type test passed.")


def main():
    data = parse('pokemon_test.csv')
    df = pd.read_csv('pokemon_test.csv')
    test_species_count(data, df)
    test_max_level(data, df)
    test_filter_range(data, df)
    test_mean_attack_for_type(data, df)
    test_count_types(data, df)
    test_highest_stage_per_type(data, df)
    test_mean_attack_per_type(data, df)


if __name__ == "__main__":
    main()
