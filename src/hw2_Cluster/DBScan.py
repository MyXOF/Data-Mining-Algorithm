from src.hw2_Cluster import *
from src.hw2_Cluster.Utils import *
from datetime import datetime


def find_neighbours(eps, point, point_set):
    return list(filter(lambda a: calculate_euclidean_distance(a, point) <= eps, point_set))


def generate_point_dict(point_set):
    point_dict = {}
    for point in point_set:
        point_dict[geneate_point_name(point)] = [False, 1]  # False: unvisited, 1: un classification
    return point_dict
    pass


def expand_cluster(point, neighbours, new_cluster, eps, min_pts, point_dict, point_set):
    new_cluster.append(point)
    point_dict[geneate_point_name(point)][1] = 2
    for neighbour_point in neighbours:
        if not point_dict[geneate_point_name(neighbour_point)][0]:
            point_dict[geneate_point_name(neighbour_point)][0] = True
            another_neighbours = find_neighbours(eps, neighbour_point, point_set)
            if len(another_neighbours) >= min_pts:
                neighbours.extend(list(filter(lambda x: not point_dict[geneate_point_name(x)][0],another_neighbours)))
            if point_dict[geneate_point_name(neighbour_point)][1] == 1:
                new_cluster.append(neighbour_point)
                point_dict[geneate_point_name(neighbour_point)][1] = 2
    return new_cluster
    pass


def dbscan_algroithm(eps, min_pts, data_file_path, label_file_path):
    point_set = read_data_from_file(data_file_path, DATA_FILE_SPILTOR)
    label_set = read_data_from_file(label_file_path, NO_SPILTOR)
    label_dict = generate_point_label_dict(point_set, label_set)
    min_len = min(len(point_set), len(label_set))
    point_set = point_set[0:min_len]
    label_set = label_set[0:min_len]

    point_dict = generate_point_dict(point_set)
    noise_group = []
    group_arranged = []
    start_time = datetime.now().timestamp()

    for point in point_set:
        if point_dict[geneate_point_name(point)][0]:
            continue
        point_dict[geneate_point_name(point)][0] = True
        neighbours = find_neighbours(eps, point, point_set)
        if len(neighbours) < min_pts:
            point_dict[geneate_point_name(point)][0] = True
            point_dict[geneate_point_name(point)][1] = 0
            noise_group.append(point)
        else:
            new_cluster = expand_cluster(point, neighbours, [], eps, min_pts, point_dict, point_set)
            group_arranged.append(new_cluster)

    group_arranged.append(noise_group)
    end_time = datetime.now().timestamp()
    label_statics = generate_occurrence_of_label(label_set)
    label_group = convert_point_to_label(label_dict, group_arranged)
    purity = calculate_total_purity(label_group, min_len)
    fscore = calculate_total_fscore(label_group, min_len, label_statics)
    return (len(noise_group), end_time - start_time, purity, fscore)
    pass


if __name__ == "__main__":
    print(dbscan_algroithm(2, 13, "../../data/hw2/dataset2.dat", "../../data/hw2/dataset2-label.dat"))

    pass
