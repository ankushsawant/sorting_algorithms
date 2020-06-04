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
    logging.info('Inside bubble_sort')
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

    return f'bubble_sort: completed in {exec_time:.5f}s'


def insertion_sort(u_list=None):
    """
    insertion sort algorithm
    :return:
    """
    logging.info('Inside insertion_sort')
    start_time = time.perf_counter()

    finish_time = time.perf_counter()
    exec_time = finish_time - start_time

    return f'insertion_sort: completed in {exec_time:.5f}s'


def main():
    """
    main entry point for sorting algorithms module
    :return:
    """
    sorting_algorithms = ['bubble_sort', 'insertion_sort']  # list of sorting algorithms

    unsorted_list = [random.randint(1, 100) for _ in range(10)]
    logging.debug(unsorted_list)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(eval(algorithm), unsorted_list) for algorithm in sorting_algorithms]

        for f in concurrent.futures.as_completed(results):
            logging.info(f.result())


if __name__ == '__main__':
    logging.info('Sorting Algorithms!')
    main()
