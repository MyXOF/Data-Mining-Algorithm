from src.hw2_Cluster import *
from src.hw2_Cluster.Utils import *
import random
from functools import reduce
from datetime import datetime


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
    return sorted(list(map(lambda group: calcalate_centroid_for_group(group), groups)), key=lambda item: item[0])
    pass


def is_centroids_equal(centroids_1, centroids_2):
    return (centroids_1 > centroids_2) - (centroids_2 > centroids_1)


def kmeans_algroithm(k, data_file_path, label_file_path):
    point_set = read_data_from_file(data_file_path, DATA_FILE_SPILTOR)
    label_set = read_data_from_file(label_file_path, NO_SPILTOR)
    label_dict = generate_point_label_dict(point_set, label_set)
    min_len = min(len(point_set), len(label_set))
    point_set = point_set[0:min_len]
    label_set = label_set[0:min_len]

    start_time = datetime.now().timestamp()
    origin_centroids = rand_centroids(point_set, k)
    group_arranged = arrange_group(point_set, origin_centroids, k)
    new_centroids = calculate_centroids_from_group(group_arranged)
    count = 0
    while is_centroids_equal(origin_centroids, new_centroids) != 0:
        origin_centroids = new_centroids
        group_arranged = arrange_group(point_set, origin_centroids, k)
        new_centroids = calculate_centroids_from_group(group_arranged)
        count += 1

    end_time = datetime.now().timestamp()

    label_statics = generate_occurrence_of_label(label_set)
    label_group = convert_point_to_label(label_dict, group_arranged)
    purity = calculate_total_purity(label_group, min_len)
    fscore = calculate_total_fscore(label_group, min_len, label_statics)
    return (count, end_time - start_time, purity, fscore)


if __name__ == "__main__":

    print(kmeans_algroithm(15,"../../data/hw2/dataset1.dat","../../data/hw2/dataset1-label.dat"))
    pass
