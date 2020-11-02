from kmeans import assign_data_to_closest_centroid
from utils import load_centroids, read_data


def update_assignment(data, labels, centroids):
    """Assign all data points to the closest centroids and keep track of their
    labels. The i-th point in "data" corresponds to the i-th label in "label".

    Arguments:
        data: a list of lists representing all data points
        labels: a list of ints representing all data labels
        centroids: the centroid dictionary

    Returns: a new dictionary whose keys are the centroids' key names and
             values are a list of labels of the data points that are assigned
             to that centroid.
    """

    new_cluster = {}
    for i in range(len(data)):
        assignment = assign_data_to_closest_centroid(data[i], centroids)
        if assignment not in new_cluster:
            new_cluster[assignment] = [labels[i]]
        else:
            new_cluster[assignment].append(labels[i])

    return new_cluster


def majority_count(labels):
    """Return the count of the majority labels in the label list

    Arguments:
        labels: a list of labels

    Returns: the count of the majority labels in the list
    """
    lst = [0 for i in range(max(labels) + 1)]

    for element in labels:
        lst[element] = lst[element] + 1

    return max(lst)


def accuracy(data, labels, centroids):
    """Calculate the accuracy of the algorithm. You should use
    update_assignment and majority_count (that you previously implemented)

    Arguments:
        data: a list of lists representing all data points
        labels: a list of ints representing all data labels
        centroids: the centroid dictionary

    Returns: a float representing the accuracy of the algorithm
    """

    new_labels = update_assignment(data, labels, centroids)
    count = 0
    total = 0
    for label in new_labels.values():
        count = count + majority_count(label)
        total = total + len(label)

    return count/total


if __name__ == '__main__':
    centroids = load_centroids("mnist_final_centroids.csv")
    data, label = read_data("data/mnist.csv")
    print(accuracy(data, label, centroids))


# LEAVE YOUR ANSWERS HERE...
# 1. What happened to the centroids? Why are there fewer than 10?
# I think it's perhaps because there are same number in our samples.
# 2. What's the accuracy of the algorithm on MNIST? By looking at the
# centroids, which digits are easier to be distinguished by the algorithm,
# and which are harder?
# The accuracy is 0.582.
# I think 0 is easier to distinguish in my opinion, while number 6 are harder.
