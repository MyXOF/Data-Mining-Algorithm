from src.hw2_Cluster import *
from src.hw2_Cluster.Utils import *
from datetime import datetime


def find_neighbours(point, point_set, two_point_dinstance):
    another_neighbours = []

    for anther_point in point_set:
        if point[1] > anther_point[1]:
            if two_point_dinstance[anther_point[1]][point[1] - anther_point[1]]:
                another_neighbours.append(anther_point)
        elif two_point_dinstance[point[1]][anther_point[1] - point[1]]:
            another_neighbours.append(anther_point)
    return another_neighbours


def expand_cluster(point, neighbours, new_cluster, min_pts, two_point_dinstance, point_set, is_visited_info,
                   point_type_info, point_all_len):
    new_cluster.append(point)

    neighbour_static = [False] * point_all_len
    for neighbour_point in neighbours:
        neighbour_static[neighbour_point[1]] = True

    # i = 0
    for neighbour_point in neighbours:
        # i += 1
        if not is_visited_info[neighbour_point[1]]:
            # print("%d: %d" % (i, len(neighbours)))

            is_visited_info[neighbour_point[1]] = True
            new_cluster.append(neighbour_point)

            another_neighbours = find_neighbours(neighbour_point, point_set, two_point_dinstance)
            if len(another_neighbours) >= min_pts:
                for another_neighbour in another_neighbours:
                    if not neighbour_static[another_neighbour[1]]:
                        neighbour_static[another_neighbour[1]] = True
                        neighbours.append(another_neighbour)
            if point_type_info[neighbour_point[1]] < 2:
                point_type_info[neighbour_point[1]] = 2
    return new_cluster
    pass


def dbscan_algroithm(min_pts, point_set, min_len, two_point_dinstance, label_set_tmp):
    start_time = datetime.now().timestamp()
    is_visited_info = [False] * min_len
    point_type_info = [1] * min_len
    noise_group = []
    group_arranged = []
    for point in point_set:
        if is_visited_info[point[1]]:
            continue
        is_visited_info[point[1]] = True
        neighbours = find_neighbours(point, point_set, two_point_dinstance)
        if len(neighbours) < min_pts:
            point_type_info[point[1]] = 0
            # noise_group.append(point[0])
        else:
            new_cluster = expand_cluster(point, neighbours, [], min_pts, two_point_dinstance, point_set,
                                         is_visited_info, point_type_info, min_len)
            group_arranged.append(new_cluster)

    end_time = datetime.now().timestamp()
    label_statics = generate_occurrence_of_label(label_set_tmp[0:min_len])

    label_group = []
    for point_group in group_arranged:
        if len(point_group) > 0:
            label_group.append(list(map(lambda a: a[2], point_group)))

    purity = calculate_total_purity(label_group, min_len)
    fscore = calculate_total_fscore(label_group, min_len, label_statics)
    return (len(noise_group), end_time - start_time, purity, fscore)
    pass


if __name__ == "__main__":
    point_set_tmp = read_data_from_file("../../data/hw2/dataset2.dat", DATA_FILE_SPILTOR)
    label_set_tmp = read_data_from_file("../../data/hw2/dataset2-label.dat", NO_SPILTOR)

    min_len = min(len(point_set_tmp), len(label_set_tmp))
    point_set = []

    for i in range(0, min_len):
        point_set.append((point_set_tmp[i], i, label_set_tmp[i]))

    two_point_dinstance = []

    for i in range(0, min_len):
        two_point_dinstance.append([False] * (min_len - i))
        for j in range(i, min_len):
            flag = calculate_euclidean_distance(point_set[i][0], point_set[j][0]) <= 2
            two_point_dinstance[i][j - i] = flag

    print(dbscan_algroithm(13, point_set, min_len, two_point_dinstance, label_set_tmp))

    pass
