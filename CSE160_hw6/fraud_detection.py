import csv
import matplotlib.pyplot as plt
import random as rd


def extract_election_vote_counts(filename, column_names):
    vote_csv = open(filename)
    input_file = csv.DictReader(vote_csv)

    vote = []

    for row in input_file:
        for name in column_names:
            if len(row[name]) > 0:
                vote.append(int(row[name].replace(",", "")))

    vote_csv.close()
    return vote


def ones_and_tens_digit_histogram(numbers):
    freq = [0] * 10
    total_digits = len(numbers) * 2

    for num in numbers:
        num = num % 100

        if num < 10:
            freq[0] = freq[0] + 1
        else:
            freq[num // 10] = freq[num // 10] + 1

        freq[num % 10] = freq[num % 10] + 1

    for i in range(len(freq)):
        freq[i] = freq[i]/total_digits

    return freq


def plot_iranian_least_digits_histogram(histogram):
    line1, = plt.plot([0.1]*10, label='Line 1')
    line2, = plt.plot(histogram, label='Line 2')
    plt.legend([line1, line2], ['Ideal', 'Iran'], loc='upper right')

    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.axis([0, 10, 0.06, 0.16])

    plt.savefig('iran-digits.png')
    # plt.show()
    plt.clf()

    return None


def plot_distribution_by_sample_size():
    size = [10, 50, 100, 1000, 10000]
    x = [i for i in range(0, 10)]

    plt.plot(x, [0.1]*10)
    plt.title("Distribution of last two digits")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.axis([0, 10, 0, 0.25])

    for num in size:
        numbers = random_uniform_samples(num)
        y = ones_and_tens_digit_histogram(numbers)
        plt.plot(x, y)

    plt.gca().legend(('Ideal', '10 random numbers',
                      '50 random numbers', '100 random numbers',
                      '1000 random numbers', '10000 random numbers'),
                     loc='upper right')

    plt.savefig('random-digits.png')
    # plt.show()
    plt.clf()

    return None


def mean_squared_error(numbers1, numbers2):
    mse = 0
    if len(numbers1) != len(numbers2):
        return "No MSE"
    else:
        for i in range(len(numbers1)):
            mse += (numbers1[i] - numbers2[i]) ** 2

    mse = mse/len(numbers1)

    return mse


def calculate_mse_with_uniform(histogram):
    uniform = [0.1] * 10
    mse = mean_squared_error(histogram, uniform)

    return mse


def compare_iranian_mse_to_samples(iranian_mse, number_of_iranian_samples):
    larger = 0
    smaller = 0

    for i in range(0, 10000):
        sample = random_uniform_samples(number_of_iranian_samples)
        histogram = ones_and_tens_digit_histogram(sample)
        mse = calculate_mse_with_uniform(histogram)

        if mse >= iranian_mse:
            larger += 1
        else:
            smaller += 1

    write_result("2009 Iranian", iranian_mse, larger, smaller)

    return None


def compare_us_mse_to_samples(us_mse, number_of_us_samples):
    larger = 0
    smaller = 0

    for i in range(0, 10000):
        sample = random_uniform_samples(number_of_us_samples)
        histogram = ones_and_tens_digit_histogram(sample)
        mse = calculate_mse_with_uniform(histogram)

        if mse >= us_mse:
            larger += 1
        else:
            smaller += 1

    write_result("2008 United States", us_mse, larger, smaller)

    return None


def random_uniform_samples(number_of_samples):
    sample = []

    for i in range(0, number_of_samples):
        sample.append(rd.randint(1, 99))

    return sample


def p_val(number1, number2):

    return number1/(number1 + number2)


def write_result(string, mse, larger, smaller):
    print(string + " election MSE:", mse)
    print("Quantity of MSEs larger than or equal to the", string,
          "election MSE:", larger)
    print("Quantity of MSEs smaller than the", string,
          "election MSE:", smaller)
    print(string, "election null hypothesis rejection level p:",
          p_val(larger, smaller))

    return None


def iranian_election():
    filename = "election-iran-2009.csv"
    column_names = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]

    numbers = extract_election_vote_counts(filename, column_names)
    histogram = ones_and_tens_digit_histogram(numbers)

    plot_iranian_least_digits_histogram(histogram)
    plot_distribution_by_sample_size()

    mse = calculate_mse_with_uniform(histogram)
    compare_iranian_mse_to_samples(mse, len(numbers))

    return None


def us_eletion():
    filename = "election-us-2008.csv"
    column_names = ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"]

    numbers = extract_election_vote_counts(filename, column_names)
    histogram = ones_and_tens_digit_histogram(numbers)

    mse = calculate_mse_with_uniform(histogram)
    compare_us_mse_to_samples(mse, len(numbers))

    return None


def main():
    iranian_election()
    print("")
    us_eletion()

    return None


if __name__ == "__main__":
    main()
