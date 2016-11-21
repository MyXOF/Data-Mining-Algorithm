from src.hw2_Cluster import *
from src.hw2_Cluster.Utils import *
from datetime import datetime


def dbscan_algroithm(eps, min_pts, data_file_path, label_file_path):
    point_set = read_data_from_file(data_file_path, DATA_FILE_SPILTOR)
    label_set = read_data_from_file(label_file_path, NO_SPILTOR)
    label_dict = generate_point_label_dict(point_set, label_set)
    min_len = min(len(point_set), len(label_set))
    point_set = point_set[0:min_len]
    label_set = label_set[0:min_len]

    start_time = datetime.now().timestamp()


    pass

if __name__ == "__main__":
    pass