import time
import random


def sequential_search(lists, item):
    """search function.
    Args:
        lists(list): list of  data.
        item(mix): search value.
    Returns:
        Returns tuple.
    Examples:
        >>> search(lists, 10)
        (True, 2.2172927856445312e-05)
    """
    init_time = time.time()
    position = 0
    found = False

    while position < len(lists) and not found:
        if lists[position] == item:
            found = True
        else:
            position = position + 1
    end_time = time.time()
    return (end_time - init_time, found)


def ordered_sequential_search(lists, item):
    """"An ordered sequential search.
    Args:
        lists(list): search data.
        item(mix): searched list.
    Returns:
        Returns tuple.
    """
    lists.sort()
    init_time = time.time()
    position = 0
    found = False
    stop = False

    while position < len(lists) and not found and not stop:
        if lists[position] == item:
            found = True
        else:
            if lists[position] > item:
                stop = True
            else:
                position = position + 1
    end_time = time.time()
    return (end_time - init_time, found)


def binary_search_iterative(lists, item):
    """binary search function.
    Args:
        lists(list): list with data.
        item(mix): item from list.
    Returns:
        Returns tuple.
    Examples:
        >>> binary_search_iterative(lists, 5)
        (False, 1.71661376953125e-05)
    """
    lists.sort()
    init_time = time.time()
    first = 0
    last = len(lists) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if lists[midpoint] == item:
            found = True
        else:
            if item < lists[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end_time = time.time()
    return (end_time - init_time, found)


def binary_search_recursive(lists, item):
    """binary search function.
    Args:
        lists(list): lists with data.
        item(mix): item from list.
    Returns:
        returns tuple.
    Examples:
        >>> binary_search_recursive(lists, 2)
        (True, 6.9141387939453125e-06)
    """
    lists.sort()
    init_time = time.time()
    if len(lists) == 0:
        found = False
    else:
        midpoint = len(lists) // 2
        if lists[midpoint] == item:
            found = True
        else:
            if item < lists[midpoint]:
                return binary_search_recursive(lists[:midpoint], item)
            else:
                return binary_search_recursive(lists[midpoint + 1:], item)
    end_time = time.time()
    return (end_time - init_time, found)


def random_list(ran_num):
    """Function for random list."""
    my_list = []
    for number in range(ran_num):
        my_list.append(random.randint(1, ran_num))
    return my_list


def main():
    """function that search and copmare."""
    test_num = [500, 1000, 10000]

    for i in test_num:
        counter = 100
        results = [0, 0, 0, 0]
        while counter > 0:
            my_list = random_list(i)
            results[0] += sequential_search(my_list, -1)[0]
            results[1] += ordered_sequential_search(my_list, -1)[0]
            results[2] += binary_search_iterative(my_list, -1)[0]
            results[3] += binary_search_recursive(my_list, -1)[0]
            counter -= 1
        print('For the sample number of {}... '.format(i))
        print('The sequential search took %10.7f seconds to run, on average.') % (
            results[0] / 100)
        print('The ordered sequential search ' +
              'took %10.7f seconds to run, on average.') % (results[1] / 100)
        print('The iterative binary search ' +
              'took %10.7f seconds to run, on average.') % (results[2] / 100)
        print('The recursive binary search ' +
              'took %10.7f seconds to run, on average.') % (results[3] / 100)


if __name__ == "__main__":
    main()
