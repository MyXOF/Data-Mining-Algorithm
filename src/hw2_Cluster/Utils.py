from numpy import *

SPILTOR = '    '


def calculate_euclidean_distance(point1, point2):
    return sqrt(sum(power(list(map(lambda x: x[0] - x[1], zip(point1, point2))), 2)))


def calculate_fscore(recall, precision):
    return (2 * recall * precision) / (recall + precision)


def read_data_from_file(path):
    data = []
    with open(path, 'r') as f:
        while True:
            line = f.readline()
            if not line or len(line) == 1:
                break
            data_pair = list(map(lambda x: float(x), line.strip('\n').split(SPILTOR)))
            data.append(data_pair)
        f.close()
    return data


if __name__ == "__main__":
    print(calculate_euclidean_distance([0, 1], [3, 5]))

    pass
