#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week4 algorithm module."""


import time
import random


def insertion_sort(lists):
    """This function sort list."""
    init_time = time.time()
    for i in range(1, len(lists)):
        current_value = lists[i]
        position = i
        while position > 0 and lists[position - 1] > current_value:
            lists[position] = lists[position - 1]
            position = position - 1
        lists[position] = current_value
    end_time = time.time()
    return (end_time - init_time, lists)


def gap_insertion_sort(lists, start, gap):
    """Insertion function."""

    for i in range(start + gap, len(lists), gap):
        current_value = lists[i]
        position = i
        while position >= gap and lists[position - gap] > current_value:
            lists[position] = lists[position - gap]
            position = position - gap
        lists[position] = current_value


def shell_sort(lists):
    """A shell function."""
    init_time = time.time()
    sublist_count = len(lists) // 2
    while sublist_count > 0:
        for init_position in range(sublist_count):
            gap_insertion_sort(lists, init_position, sublist_count)
        sublist_count = sublist_count // 2
    end_time = time.time()
    return (end_time - init_time, lists)


def python_sort(lists):
    """sort function."""
    init_time = time.time()
    lists = lists.sort()
    end_time = time.time()
    return (end_time - init_time, lists)


def random_list(ran_num):
    """Random Function."""
    my_list = []
    for i in range(ran_num):
        my_list.append(random.randint(1,ran_num))
    return my_list


def main():
    """This function will compare and test."""
    test_num = [500, 1000, 10000]

    for num in test_num:
        list_num = 100
        result = [0, 0, 0]

        while list_num > 0:
            my_list = random_list(num)
            result[0] += insertion_sort(my_list)[0]
            result[1] += shell_sort(my_list)[0]
            result[2] += python_sort(my_list)[0]
            list_num -= 1
        print ('For the sample number of {}... '.format(num))
        print ('Insertion Sort took %10.7f seconds to run, on average.' % (result[0] / 100))
        print ('Shell Sort ' + 'took %10.7f seconds to run, on average.' % (result[1] / 100))
        print ('Python Sort ' + 'took %10.7f seconds to run, on average.' % (result[2] / 100))

if __name__ == "__main__":
    main()
