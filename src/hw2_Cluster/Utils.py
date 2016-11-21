from numpy import *


def calculate_euclidean_distance(point1, point2):
    return sqrt(sum(power(list(map(lambda x: x[0] - x[1], zip(point1, point2))), 2)))


def calculate_fscore(recall, precision):
    return (2 * recall * precision) / (recall + precision)


def read_data_from_file(path, splitor):
    data = []
    with open(path, 'r') as f:
        while True:
            line = f.readline()
            if not line or len(line) == 1:
                break
            if splitor is None or len(splitor) == 0:
                data_pair = line.strip('\n')
            else:
                data_pair = list(map(lambda x: float(x), line.strip('\n').split(splitor)))
            data.append(data_pair)
        f.close()
    return data


def convert_point_to_label(dictionary, group_list):
    label_group = []
    for group in group_list:
        lable_list = []
        for point in group:
            lable_list.append(dictionary[geneate_point_name(point)])
        label_group.append(lable_list)
    return label_group
    pass


def calculate_total_fscore(label_list, label_num, label_statics):
    return sum(list(map(lambda x: len(x) * calculate_single_fscore(x, label_statics), label_list))) / label_num
    pass


def calculate_single_fscore(label_list, label_statics):
    (label_name, label_num) = calculate_single_purity_pair(label_list)
    precision = label_num / len(label_list)
    recall = label_num / label_statics[label_name]
    # print("%s--%s"%([precision,recall]))
    return calculate_fscore(recall, precision)
    pass


def calculate_total_purity(label_list, label_num):
    return sum(list(map(calculate_single_purity, label_list))) / label_num
    pass


def calculate_single_purity_pair(label_list):
    label_num = len(label_list)
    if label_num == 0:
        return (0, 0)
    static = {}
    for label in label_list:
        if label not in static:
            static[label] = 1
        else:
            static[label] += 1
    max_index = max(static, key=static.get)
    return (max_index, static[max_index])
    pass


def calculate_single_purity(label_list):
    return calculate_single_purity_pair(label_list)[1]


def generate_point_label_dict(point_set, label_set):
    statics = {}
    for item in list(zip(point_set, label_set)):
        statics[geneate_point_name(item[0])] = item[1]
    return statics
    pass

def geneate_point_name(point):
    return "-".join(list(map(lambda x:str(x), point)))

def generate_occurrence_of_label(label_set):
    statics = {}
    for label in label_set:
        if label not in statics:
            statics[label] = 1
        else:
            statics[label] += 1
    return statics
    pass


if __name__ == "__main__":
    point_set = read_data_from_file("../../data/hw2/dataset2.dat", "    ")
    label_set = read_data_from_file("../../data/hw2/dataset2-label.dat", "")
    print(generate_point_label_dict(point_set, label_set))

    pass
