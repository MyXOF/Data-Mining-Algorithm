from src.hw1_Classification.Classification import *
from datetime import datetime

_REPEAT_NUM_IN_PERFORMANCE = 10


def svm_statistics(_train_set, _test_set):
    time_cost = []
    correct_cost = []
    for i in range(0, _REPEAT_NUM_IN_PERFORMANCE):
        result = svm_model(_train_set, _test_set)
        time_cost.append(result[0])
        correct_cost.append(result[1])
    print("svm time avg :"+ str(sum(time_cost) / len(time_cost)))
    print("svm correct avg :"+ str(sum(correct_cost) / len(correct_cost)))
    pass


def svm_model(_train_set, _test_set):
    _start_time = datetime.now().timestamp()
    clf = svm.SVC()
    clf = clf.fit(_train_set[0], _train_set[1])
    num = 0
    correct = 0
    for i in clf.predict(_test_set[0]):
        if i == _test_set[1][num]:
            correct += 1
        num += 1
    _end_time = datetime.now().timestamp()
    return (_end_time - _start_time, correct / num)
    pass


def random_forest_statistics(_train_set, _test_set):
    time_cost = []
    correct_cost = []
    for i in range(0, _REPEAT_NUM_IN_PERFORMANCE):
        result = random_forest_model(_train_set, _test_set)
        time_cost.append(result[0])
        correct_cost.append(result[1])
    print("random_fores time avg :" + str(sum(time_cost) / len(time_cost)))
    print("random_fores correct avg :" + str(sum(correct_cost) / len(correct_cost)))
    pass


def random_forest_model(_train_set, _test_set):
    _start_time = datetime.now().timestamp()
    clf = RandomForestClassifier(n_estimators=10)
    clf = clf.fit(_train_set[0], _train_set[1])

    num = 0
    correct = 0
    for i in clf.predict(_test_set[0]):
        if i == _test_set[1][num]:
            correct += 1
        num += 1
    _end_time = datetime.now().timestamp()
    return (_end_time - _start_time, correct / num)
    pass


def decision_tree_statistics(_train_set, _test_set):
    time_cost = []
    correct_cost = []
    for i in range(0, _REPEAT_NUM_IN_PERFORMANCE):
        result = decision_tree_model(_train_set, _test_set)
        time_cost.append(result[0])
        correct_cost.append(result[1])
    print("decision_tree time avg :" + str(sum(time_cost) / len(time_cost)))
    print("decision_tree correct avg :" + str(sum(correct_cost) / len(correct_cost)))
    pass


def decision_tree_model(_train_set, _test_set):
    _start_time = datetime.now().timestamp()
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(_train_set[0], _train_set[1])

    num = 0
    correct = 0
    for i in clf.predict(_test_set[0]):
        if i == _test_set[1][num]:
            correct += 1
        num += 1
    _end_time = datetime.now().timestamp()
    return (_end_time - _start_time, correct / num)
    pass


if __name__ == "__main__":
    train_set = read_from_file("../../data/hw1/adult.data.txt")
    test_set = read_from_file("../../data/hw1/adult.test.txt")
    decision_tree_statistics(train_set, test_set)
    random_forest_statistics(train_set, test_set)
    svm_statistics(train_set, test_set)

    pass
