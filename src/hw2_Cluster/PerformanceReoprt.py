from src.hw2_Cluster.DBSCAN2 import *


def perfromance(eps, min_pts_list, two_point_dinstance):
    two_point_dinstance_flag = list(map(lambda a: list(map(lambda b: b <= eps, a)), two_point_dinstance))
    for min_pts in min_pts_list:
        result = dbscan_algroithm(min_pts, point_set, min_len ,two_point_dinstance_flag, label_set_tmp)
        print("%s,%s,%s,%s,%s" %(str(eps), str(min_pts), str(result[2]), str(result[3]), str(result[1])))
    pass


if __name__ == "__main__":
    # point_set_tmp = read_data_from_file("../../data/hw2/dataset2.dat", DATA_FILE_SPILTOR)
    # label_set_tmp = read_data_from_file( "../../data/hw2/dataset2-label.dat", NO_SPILTOR)

    point_set_tmp = read_data_from_file("../../data/hw2/dataset1.dat", DATA_FILE_SPILTOR)
    label_set_tmp = read_data_from_file( "../../data/hw2/dataset1-label.dat", NO_SPILTOR)

    min_len = min(len(point_set_tmp), len(label_set_tmp))
    point_set = []
    for i in range(0, min_len):
        point_set.append((point_set_tmp[i], i, label_set_tmp[i]))

    two_point_dinstance = []

    for i in range(0, min_len):
        two_point_dinstance.append([0] * (min_len - i))
        for j in range(i, min_len):
            two_point_dinstance[i][j - i] = calculate_euclidean_distance(point_set[i][0], point_set[j][0])

    # for eps in [i / 10 for i in range(5,30)]:
    #     perfromance(eps, list(range(1, 55)),two_point_dinstance)

    for eps in [30000 + i * 2000 for i in range(0, 21)]:
        perfromance(eps, [50 + i * 10 for i in range(0, 21)], two_point_dinstance)
    pass