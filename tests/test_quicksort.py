# content of test_quicksort.py
from kata.quicksort import sort_utils

def max_item(source_list):
    max_num = source_list
    for item in source_list:
        if item > max_item:
            max_num = item
    return max_num

def test_sort():
    raw_list = [1, 44, 5, 356, 65, 9, 24, 17]
    expect_list = raw_list[:]
    expect_list.sort()

    target_list = sort_utils.quicksort(raw_list)
    for index, _ in enumerate(target_list):
        target_item = target_list[index]
        expect_item = expect_list[index]
        assert expect_item == target_item
