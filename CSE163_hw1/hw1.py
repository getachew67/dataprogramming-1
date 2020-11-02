"""
Name: Michael Shieh
Section: AB

This file contains all functions that answers all problems in hw1
"""


def total(n):
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def count_divisible_digits(n, m):
    """
    Given a number n,
    this fuction returns the total number of digits in n divisible by m.
    If m = 0, this function should return 0 since no number is divisible by 0
    """
    count = 0

    if m > 0:
        n = abs(n)
        while n > 0:
            if (n % 10) % m == 0:
                count += 1

            n //= 10

    return count


def is_relatively_prime(n, m):
    """
    Given two numbers n and m,
    this function returns True if n and m are relatively prime to reach other.
    Otherwise, return False
    """
    for i in range(2, min(n, m) + 1):
        if (n % i) == 0 and (m % i) == 0:
            return False

    return True


def travel(str, x, y):
    """
    This function takes on a string and two numbers as the origin coordinate.
    For every word in the string,
    if the word is 'N', the y-coordinate increase by 1
    if the word is 'S', the y-coordinate decrease by 1
    if the word is 'E', the x-coordinate increase by 1
    if the word is 'W', the x-coordinate decrease by 1
    all other words are ignored.

    The functiion returns the final coordinate.
    If the string is empty, the final coordnate should be the origin one.
    """
    for ele in str:
        if ele.upper() == 'N':
            y += 1
        elif ele.upper() == 'S':
            y -= 1
        elif ele.upper() == 'W':
            x -= 1
        elif ele.upper() == 'E':
            x += 1
        else:
            pass

    return x, y


def swip_swap(source, c1, c2):
    """
    This function takes on a string and two characters.
    If the character in the string matches one of the character selected,
    it will be replaced by the other character.

    The function returns the result of the swap.
    If the source string is empty, the return should be an empty string.
    """
    new_source = ''
    for ele in source:
        if ele == c1:
            new_source += c2
        elif ele == c2:
            new_source += c1
        else:
            new_source += ele

    return new_source


def compress(string):
    """
    This function takes on a string and shortens it.
    It returns a string that distinct character appeared in order,
    and each character is followed by
    how many time the character appears in the string.
    The function returns the compressed string.

    If the string is empty, the return should be an empty string.
    """
    word_count = {}
    for ele in string:
        # ele = ele.lower()
        if ele in word_count:
            word_count[ele] += 1
        else:
            word_count[ele] == 1
    word = ''
    for key in word_count.keys():
        word += key
        word += word_count[key]

    return word


def longest_line_length(file_name):
    """
    This function reads a specified file line by line
    and returns the length of the longest line within.
    If the file is empty,
    this function returns None.
    """
    length = None
    max = 0

    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            tmp = len(line.strip("\n"))
            if tmp > max:
                max = tmp

    if max > 0:
        length = max

    return length


def longest_word(file_name):
    """
    This function reads a specified file word by word
    and returns a string contain the longest word in the file
    with which line the word is located.

    If the file is empty,
    this function returns None
    """
    max = 0
    i = 0
    longest = None
    string = ''

    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            i += 1
            for word in line.strip("\n").split():
                if len(word) > max:
                    max = len(word)
                    loc = i
                    longest = word

    if longest is not None:
        string += (str(loc) + ': ' + longest)

        return string
    else:
        return None


def mode_digit(n):
    """
    This function takes an integer number n
    and returns which digit (0 ~ 9) appears most frequently in n

    If n is 0, this functoin should return 0
    """
    n = abs(n)
    if n <= 9:
        return n

    else:
        count = [0] * 10

        while n > 0:
            digit = n % 10
            count[digit] += 1
            n //= 10

        count.reverse()
        idx = 9 - count.index(max(count))

        return idx
