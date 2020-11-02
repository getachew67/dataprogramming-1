import os
import math
from utils import converged, plot_2d, plot_centroids, read_data, \
    load_centroids, write_centroids_tofile
import matplotlib.pyplot as plt


# problem for students
def euclidean_distance_between_data(dp1, dp2):
    """Calculate the Euclidean distance between two data points.

    Arguments:
        dp1: a list of floats representing a data point
        dp2: a list of floats representing a data point

    Returns: the Euclidean distance between two data points
    """
    dist = 0
    if len(dp1) == len(dp2):
        for num in range(len(dp1)):
            dist = dist + (dp1[num] - dp2[num])**2

        return math.sqrt(dist)
    else:
        return None


# problem for students
def assign_data_to_closest_centroid(data_point, centroids):
    """Assign a single data point to the closest centroid. You should use
    euclidean_distance_between_data function (that you previously implemented).

    Arguments:
        data_point: a list of floats representing a data point
        centroids: a dictionary representing the centroids where the keys are
                   strings (centroid names) and the values are lists of
                   centroid locations

    Returns: a string as the key name of the closest centroid to the data point
    """
    dist = float("inf")

    for key in centroids.keys():
        if euclidean_distance_between_data(data_point, centroids[key]) < dist:
            dist = euclidean_distance_between_data(data_point, centroids[key])
            closest = key

    return str(closest)


# problem for students
def update_assignment(data, centroids):
    """Assign all data points to the closest centroids. You should use
    assign_data_to_closest_centroid fucntion (that you previously
    implemented).

    Arguments:
        data: a list of lists representing all data points
        centroids: a dictionary representing the centroids where the keys are
                   strings (centroid names) and the values are lists of
                   centroid locations

    Returns: a new dictionary whose keys are the centroids' key names and
             values are lists of points that belong to the centroid
    """

    new_cluster = {}
    for data_point in data:
        assignment = assign_data_to_closest_centroid(data_point, centroids)
        if assignment not in new_cluster:
            new_cluster[assignment] = [data_point]
        else:
            new_cluster[assignment].append(data_point)

    return new_cluster


# problem for students
def mean_of_points(data):
    """Calculate the mean of a given group of data points. You should NOT hard
    -code the dimensionality of the data points).

    Arguments:
        data: a list of lists representing a group of data points

    Returns: a list of floats as the mean of the given data points
    """
    rtn = []
    for i in range(len(data[1])):
        tmp = 0
        for j in range(len(data)):
            tmp = tmp + data[j][i]
        rtn.append(tmp/len(data))

    return rtn


# problem for students
def update_centroids(assignment_dict):
    """Update centroid locations as the mean of all data points that belong
    to the cluster. You should use mean_of_points function (that you previously
    implemented).

    Arguments:
        assignment_dict: the dictionary returned by update_assignment function

    Returns: A new dictionary representing the updated centroids
    """

    new_centroids = {}
    for key in assignment_dict.keys():
        new_centroids[key] = mean_of_points(assignment_dict[key])

    return new_centroids


def main_2d(data, init_centroids):
    #######################################################
    # You do not need to change anything in this function #
    #######################################################
    centroids = init_centroids
    old_centroids = None
    step = 0
    while not converged(centroids, old_centroids):
        # save old centroid
        old_centroids = centroids
        # new assignment
        assignment_dict = update_assignment(data, old_centroids)
        # update centroids
        centroids = update_centroids(assignment_dict)
        # plot centroid
        fig = plot_2d(assignment_dict, centroids)
        plt.title(f"step{step}")
        fig.savefig(os.path.join("results", "2D", f"step{step}.png"))
        plt.clf()
        step += 1
    print(f"K-means converged after {step} steps.")
    return centroids


def main_mnist(data, init_centroids):
    #######################################################
    # You do not need to change anything in this function #
    #######################################################
    centroids = init_centroids
    # plot initial centroids
    plot_centroids(centroids, "init")
    old_centroids = None
    step = 0
    while not converged(centroids, old_centroids):
        # save old centroid
        old_centroids = centroids
        # new assignment
        assignment_dict = update_assignment(data, old_centroids)
        # update centroids
        centroids = update_centroids(assignment_dict)
        step += 1
    print(f"K-means converged after {step} steps.")
    # plot final centroids
    plot_centroids(centroids, "final")
    return centroids


if __name__ == '__main__':
    data, label = read_data("data/mnist.csv")
    init_c = load_centroids("data/mnist_init_centroids.csv")
    final_c = main_mnist(data, init_c)
    write_centroids_tofile("mnist_final_centroids.csv", final_c)
