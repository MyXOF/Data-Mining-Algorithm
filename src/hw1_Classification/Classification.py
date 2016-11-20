from sklearn import tree, svm
from src.hw1_Classification import *


def read_from_file(path):
    feature_list = []
    label_list = []
    with open(path, 'r') as f:
        while True:
            line = f.readline()
            if not line or len(line) == 1:
                break
            info = list(map(lambda x: x.strip(' '), line.strip('\n').split(',')))
            feature_list.append(generate_feature(info))
            label_list.append(generate_value(info[14].strip('.'), income))
        f.close()
    return (feature_list, label_list)
    pass


def generate_feature(input_args):
    feature = list()
    feature.append(int(input_args[0]))
    feature.append(generate_value(input_args[1], workclass))
    feature.append(int(input_args[2]))
    feature.append(generate_value(input_args[3], education))
    feature.append(int(input_args[4]))
    feature.append(generate_value(input_args[5], marital_status))
    feature.append(generate_value(input_args[6], occupation))
    feature.append(generate_value(input_args[7], relationship))
    feature.append(generate_value(input_args[8], race))
    feature.append(generate_value(input_args[9], sex))
    feature.append(int(input_args[10]))
    feature.append(int(input_args[11]))
    feature.append(int(input_args[12]))
    feature.append(generate_value(input_args[13], native_country))
    return feature
    pass


def generate_value(name, known_list):
    if name not in known_list:
        return 0
    else:
        return known_list.index(name) + 1


if __name__ == "__main__":
    clf = tree.DecisionTreeClassifier()
    # clf = svm.SVC()

    train_set = read_from_file("../../data/hw1/adult.data.txt")
    clf = clf.fit(train_set[0], train_set[1])
    test_set = read_from_file("../../data/hw1/adult.test.txt")

    num = 0
    correct = 0
    for i in clf.predict(test_set[0]):
        if i == test_set[1][num]:
            correct += 1
        num += 1
    print(correct)
    print(num)
    print(correct / num)
    pass
