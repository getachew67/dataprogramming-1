from fraud_detection import extract_election_vote_counts,\
    ones_and_tens_digit_histogram, mean_squared_error,\
    calculate_mse_with_uniform


def test_extract_election_vote_counts():
    filename = "election-iran-2009.csv"
    colnames = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]

    assert extract_election_vote_counts(filename, colnames) == [
        1131111, 16920, 7246, 837858, 623946, 12199, 21609, 656508,
        325911, 6578, 2319, 302825, 1799255, 51788, 14579, 746697,
        199654, 5221, 7471, 96826, 299357, 7608, 3563, 177268, 3819495,
        147487, 67334, 3371523, 359578, 22689, 4127, 106099, 285984,
        3962, 928, 90363, 2214801, 44809, 13561, 884570, 341104, 4129,
        2478, 113218, 1303129, 139124, 15934, 552636, 444480, 7276, 2223,
        126561, 295177, 4440, 2147, 77754, 450269, 6616, 12504, 507946,
        1758026, 23871, 16277, 706764, 498061, 7978, 2690, 177542, 422457,
        16297, 2314, 148467, 315689, 7140, 13862, 261772, 1160446, 12016,
        4977, 318250, 573568, 11258, 10798, 374188, 253962, 8542, 4274,
        98937, 515211, 5987, 10097, 325806, 998573, 12022, 7183, 453806,
        677829, 14920, 44036, 219156, 1289257, 19587, 10050, 585373, 572988,
        10057, 4675, 190349, 482990, 7237, 5126, 241988, 765723, 13117, 12032,
        218481, 337178, 8406, 2565, 255799]

    print("test_extract_election_vote_counts passed.")


def test_ones_and_tens_digit_histogram():
    numbers1 = [127, 426, 28, 9, 90]
    numbers2 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

    assert ones_and_tens_digit_histogram(
        numbers1) == [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    assert ones_and_tens_digit_histogram(numbers2) == [
            0.21428571428571427, 0.14285714285714285,
            0.047619047619047616, 0.11904761904761904, 0.09523809523809523,
            0.09523809523809523, 0.023809523809523808, 0.09523809523809523,
            0.11904761904761904, 0.047619047619047616]

    print("test_ones_and_tens_digit_histogram passed.")


def test_mean_squared_error():
    assert mean_squared_error([2], [5, 3]) == "No MSE"
    assert mean_squared_error([1, 4, 9], [6, 5, 4]) == 17.0

    print("test_mean_squared_error passed.")


def test_calculate_mse_with_uniform():
    filename = "election-iran-2009.csv"
    column_names = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]
    numbers = extract_election_vote_counts(filename, column_names)
    histogram = ones_and_tens_digit_histogram(numbers)

    assert calculate_mse_with_uniform(histogram) - 0.000739583333333 <= 1e+12

    print("test_calculate_mse_with_uniform passed.")


if __name__ == '__main__':
    test_extract_election_vote_counts()
    test_ones_and_tens_digit_histogram()
    test_mean_squared_error()
    test_calculate_mse_with_uniform()
    print("All test passed.")
