from src.hw2_Cluster.Utils import *
import random
from functools import reduce


def rand_centroids(point_set, k):
    '''
    at the begining, pick random k point as centroids
    :param point_set:
    :param k:
    :return:
    '''
    rand_index = random.sample(range(0, len(point_set)), k)
    return list(map(lambda x: point_set[x], rand_index))
    pass


def calcalate_centroid_for_group(point_set):
    '''
    point_set is something like [[1, 2], [2, 3], [3, 4]]
    input_list is something like [[1, 1, 2, 1], [2, 1, 3, 1], [3, 1, 4, 1]]
    output_list is something like [6, 3, 9, 3]
    result = [6/3=2 ,9/3=3]
    :param point_set: input vector list
    :return:
    '''
    input_list = map(lambda a: [x for j in list(map(lambda x: [x, 1], a)) for x in j], point_set)
    output_list = list(reduce(lambda a, b: map(lambda x: x[0] + x[1], zip(a, b)), input_list))

    output_list_len = len(output_list)
    result = []
    index = 0
    while index < output_list_len:
        result.append(output_list[index] / output_list[index + 1])
        index += 2
    return result
    pass


def arrange_group(point_set, centroids, k):
    '''
    arrange every point in point_set to one of k groups according to nearest centroid in centroids
    point_set is something like [[1, 2], [2, 3], [3, 4]]
    centroids is something like [[1, 2], [2, 3]]
    suppose k = 2
    result = [[[1, 2]], [[2, 3], [3, 4]]]
    :param point_set:
    :param centroids:
    :param k:
    :return:
    '''
    result = [[] for i in range(0, k)]
    for (origin_point, group_index) in list(
            map(lambda point: [point, calculate_nearest_centroid(point, centroids)], point_set)):
        result[group_index].append(origin_point)
    return result
    pass


def calculate_nearest_centroid(point, centroids):
    '''
    find the nearest centroid index for given point
    :param point:
    :param centroids:
    :return: centroid index
    '''
    centroids_distance = list(map(lambda centroid: calculate_euclidean_distance(centroid, point), centroids))
    return centroids_distance.index(min(centroids_distance))
    pass


def calculate_centroids_from_group(groups):
    return sorted(list(map(lambda group: calcalate_centroid_for_group(group), groups)),key=lambda item:item[0])
    pass


def is_centroids_equal(centroids_1,centroids_2):
    return (centroids_1 > centroids_2) - (centroids_2 > centroids_1)

if __name__ == "__main__":
    k = 10
    point_set = read_data_from_file("../../data/hw2/dataset1.dat")
    origin_centroids = rand_centroids(point_set, k)
    new_centroids = calculate_centroids_from_group(arrange_group(point_set,origin_centroids,k))
    count = 0
    while is_centroids_equal(origin_centroids, new_centroids) != 0:
        origin_centroids = new_centroids
        new_centroids = calculate_centroids_from_group(arrange_group(point_set,origin_centroids,k))
        count += 1
        print(count)


    # data_point = [[1, 2], [2, 3], [3, 4]]
    # print(calcalate_centroid_for_group([[1, 2], [2, 3], [3, 4]]))
    # print(arrange_group(data_point, [[1, 2], [2, 3]], 2))
    # print(calculate_centroids_from_group(arrange_group(data_point, [[1, 2], [2, 3]], 2)))
    pass
