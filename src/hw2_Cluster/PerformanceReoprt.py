from src.hw2_Cluster.DBSCAN2 import *


def perfromance(eps, min_pts_list, data_file_path, label_file_path):
    point_set_tmp = read_data_from_file(data_file_path, DATA_FILE_SPILTOR)
    label_set_tmp = read_data_from_file(label_file_path, NO_SPILTOR)

    min_len = min(len(point_set_tmp), len(label_set_tmp))
    point_set = []
    for i in range(0, min_len):
        point_set.append((point_set_tmp[i], i, label_set_tmp[i]))

    two_point_dinstance = []

    for i in range(0, min_len):
        two_point_dinstance.append([False] * (min_len - i))
        for j in range(i, min_len):
            flag = calculate_euclidean_distance(point_set[i][0], point_set[j][0]) <= eps
            two_point_dinstance[i][j - i] = flag

    for min_pts in min_pts_list:
        print(str(eps) + " -- "+str(min_pts)+" -- "+str(dbscan_algroithm(min_pts, point_set, min_len ,two_point_dinstance, label_set_tmp)))
    pass


if __name__ == "__main__":
    # for eps in [i / 10 for i in range(15,25)]:
    #     perfromance(eps, list(range(13,18)), "../../data/hw2/dataset2.dat", "../../data/hw2/dataset2-label.dat")
    for eps in [40000 + i * 2000 for i in range(0, 11)]:
        perfromance(eps, [100 + i * 10 for i in range(0, 11)], "../../data/hw2/dataset1.dat", "../../data/hw2/dataset1-label.dat")
    pass