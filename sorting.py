import random
import concurrent.futures
import logging
import time

logging.basicConfig(filename='sorting.log',
                    level=logging.INFO)


def bubble_sort(u_list=None):
    """
    bubble sort algorithm
    :param u_list: unsorted list of numbers
    :return:
    """
    logging.debug('Inside bubble_sort')
    start_time = time.perf_counter()

    if u_list is None:
        u_list = [random.randint(1, 100) for _ in range(10)]
    logging.debug(u_list)

    n = len(u_list)
    for i in range(n, 0, -1):
        fully_sorted = True
        for j in range(0, i - 1):
            if u_list[j] > u_list[j + 1]:
                u_list[j], u_list[j + 1] = u_list[j + 1], u_list[j]
                fully_sorted = False
        if fully_sorted:
            break

    logging.debug(u_list)

    finish_time = time.perf_counter()
    exec_time = finish_time - start_time

    # return f'bubble_sort: completed in {exec_time:.5f}s'
    return {
        'name': 'bubble_sort',
        'u_list': u_list,
        'exec_time': f'{exec_time:.5f}'
    }


def insertion_sort(u_list=None):
    """
    insertion sort algorithm
    :param u_list: unsorted list of numbers
    :return:
    """
    logging.debug('Inside insertion_sort')
    start_time = time.perf_counter()

    if u_list is None:
        u_list = [random.randint(1, 100) for _ in range(10)]
    logging.debug(u_list)

    n = len(u_list)
    for i in range(1, n):
        key_value = u_list[i]  # save key value to be inserted
        moved = False
        pos = -1
        for j in range(i - 1, -1, -1):
            if key_value < u_list[j]:
                u_list[j + 1] = u_list[j]
                moved = True
                pos = j
            else:
                break
        if moved:
            u_list[pos] = key_value

    logging.debug(u_list)
    finish = time.perf_counter()

    finish_time = time.perf_counter()
    exec_time = finish_time - start_time

    return {
        'name': 'insertion_sort',
        'u_list': u_list,
        'exec_time': f'{exec_time:.5f}'
    }


def selection_sort(u_list=None):
    """
    selection sort algorithm
    :param u_list: unsorted list of numbers
    :return:
    """
    logging.debug('Inside selection_sort')
    start_time = time.perf_counter()

    if u_list is None:
        u_list = [random.randint(1, 100) for _ in range(10)]
    logging.debug(u_list)

    n = len(u_list)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if u_list[j] < u_list[min_index]:
                min_index = j
        u_list[i], u_list[min_index] = u_list[min_index], u_list[i]

    logging.debug(u_list)
    finish = time.perf_counter()

    finish_time = time.perf_counter()
    exec_time = finish_time - start_time

    return {
        'name': 'selection_sort',
        'u_list': u_list,
        'exec_time': f'{exec_time:.5f}'
    }


def merge(left, right):
    """
    merge left and right lists into a sorted list
    :param left: left sorted list
    :param right: right sorted list
    :return: sorted merged list
    """
    #  if left is empty, return right
    if len(left) == 0:
        return right

    # if right is empty, return left
    if len(right) == 0:
        return left

    left_index = right_index = 0
    result = []

    while len(result) < len(left) + len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

        if left_index == len(left):
            result += right[right_index:]
            break

        if right_index == len(right):
            result += left[left_index:]
            break

    return result


def m_sort(u_list=None):
    """
    recursive merge sort algorithm
    :param u_list: unsorted list of numbers
    :return:
    """
    if len(u_list) < 2:
        return u_list

    mid = len(u_list) // 2

    return merge(
        m_sort(u_list[:mid]),
        m_sort(u_list[mid:])
    )


def merge_sort(u_list=None):
    """
    merge sort algorithm (wrapper for m_sort)
    :param u_list: unsorted list of numbers
    :return:
    """
    logging.debug('Inside merge_sort')
    start_time = time.perf_counter()

    if u_list is None:
        u_list = [random.randint(1, 100) for _ in range(10)]
    logging.debug(u_list)

    u_list = m_sort(u_list)

    logging.debug(u_list)
    finish = time.perf_counter()

    finish_time = time.perf_counter()
    exec_time = finish_time - start_time

    # return f'merge_sort: completed in {exec_time:.5f}s'
    return {
        'name': 'merge_sort',
        'u_list': u_list,
        'exec_time': f'{exec_time:.5f}'
    }


def q_sort(u_list=None):
    """
    recursive quick sort algorithm
    :param u_list: unsorted list of numbers
    :return:
    """

    if len(u_list) < 2:
        return u_list

    low, mid, high = [], [], []

    pivot = u_list[random.randint(0, len(u_list) - 1)]

    for num in u_list:
        if num < pivot:
            low.append(num)
        elif num == pivot:
            mid.append(num)
        else:
            high.append(num)

    return q_sort(low) + mid + q_sort(high)


def quick_sort(u_list=None):
    """
    quick sort algorithm (wrapper for q_sort)
    :param u_list: unsorted list of numbers
    :return:
    """
    logging.debug('Inside quick_sort')
    start_time = time.perf_counter()

    if u_list is None:
        u_list = [random.randint(1, 100) for _ in range(10)]
    logging.debug(u_list)

    u_list = q_sort(u_list)

    logging.debug(u_list)
    finish_time = time.perf_counter()
    exec_time = finish_time - start_time

    # return f'quick_sort: completed in {exec_time:.5f}s'
    return {
        'name': 'quick_sort',
        'u_list': u_list,
        'exec_time': f'{exec_time:.5f}'
    }


def main():
    """
    main entry point for sorting algorithms module
    :return:
    """
    sorting_algorithms = ['bubble_sort', 'insertion_sort', 'selection_sort', 'merge_sort', 'quick_sort']  # list of sorting algorithms

    unsorted_list = [random.randint(1, 100) for _ in range(1000)]
    logging.debug(unsorted_list)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(eval(algorithm), unsorted_list) for algorithm in sorting_algorithms]

        for f in concurrent.futures.as_completed(results):
            logging.info('{0} algorithm completed in {1}s.'.format(f.result()['name'], f.result()['exec_time']))


if __name__ == '__main__':
    logging.info('Sorting Algorithms!')
    main()
