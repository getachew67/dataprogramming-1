"""
Name: Michael Shieh
Section: AB

This file contains tests for all functions from hw1
"""

import hw1

from cse163_utils import assert_equals


def test_total():
    """
    Tests the total method
    """
    # The regular case
    assert_equals(15, hw1.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw1.total(1))
    assert_equals(0, hw1.total(0))

    # Test the None case
    assert_equals(None, hw1.total(-1))


def test_count_divisible_digits():
    """
    Tests the count_divisible_digit function.
    Should show nothing if all tests passed.
    """
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(0, hw1.count_divisible_digits(24, 5))
    assert_equals(0, hw1.count_divisible_digits(1, 0))


def test_is_relatively_prime():
    """
    Tests the is_relative_prime function.
    Should show nothing if all tests passed.
    """
    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(4, 24))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 1))


def test_travel():
    """
    Tests the test function.
    Should show nothing if all tests passed.
    """
    assert_equals((-1, 4), hw1.travel('NW!ewnW', 1, 2))
    assert_equals((4, 1), hw1.travel('seEnhsN', 2, 1))
    assert_equals((0, 0), hw1.travel('testNWA', 0, 0))
    assert_equals((12, 9), hw1.travel('Seattle', 10, 10))
    assert_equals((7, 0), hw1.travel('cse163test', 5, 2))


def test_swip_swap():
    """
    Tests the swip_swap function.
    Should show nothing if all tests passed.
    """
    assert_equals('offbar', hw1.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', hw1.swip_swap('foobar', 'b', 'c'))
    assert_equals('foobar', hw1.swip_swap('foobar', 'z', 'c'))
    assert_equals('cython', hw1.swip_swap('python', 'p', 'c'))
    assert_equals('pmogmarring', hw1.swip_swap('programming', 'r', 'm'))


def test_compress():
    """
    Tests the compress function.
    Should show nothing if all tests passed.
    """
    assert_equals('c1o17l1k1a1n1g1a1r1o2', hw1.compress(
        'cooooooooooooooooolkangaroo'))
    assert_equals('a3', hw1.compress('aaa'))
    assert_equals('s2e3a2t2l1m1r2i1n1', hw1.compress('SeattleMariners'))
    assert_equals('', hw1.compress(''))


def test_longest_line_length():
    """
    Tests the longest_line_length function.
    Should show nothing if all tests passed.
    """
    assert_equals(13, hw1.longest_line_length('/home/poem.txt'))
    assert_equals(None, hw1.longest_line_length('/home/empty.txt'))


def test_longest_word():
    """
    Tests the longest_word function.
    Should show nothing if all tests passed.
    """
    assert_equals('3: shells', hw1.longest_word('/home/poem.txt'))
    assert_equals(None, hw1.longest_word('/home/empty.txt'))


def test_mode_digit():
    """
    Tests the mode_digit function.
    Should show nothing if all tests passed.
    """
    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))
    assert_equals(7, hw1.mode_digit(916320389459324777777777))


def main():
    test_total()
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_travel()
    test_swip_swap()
    test_longest_line_length()
    test_longest_word()
    test_mode_digit()
    print("All tests passed!")


if __name__ == '__main__':
    main()
