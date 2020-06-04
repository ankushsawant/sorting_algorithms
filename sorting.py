import random
import concurrent.futures
import logging

logging.basicConfig(filename='sorting.log',
                    level=logging.INFO)


def bubble_sort(u_list=None):
    """
    bubble sort algorithm
    :return:
    """
    logging.info('Inside bubble_sort')
    return 'bubble_sort'


def insertion_sort(u_list=None):
    """
    insertion sort algorithm
    :return:
    """
    logging.info('Inside insertion_sort')
    return 'insertion_sort'


def main():
    """
    main entry point for sorting algorithms module
    :return:
    """
    sorting_algorithms = ['bubble_sort', 'insertion_sort']  # list of sorting algorithms

    unsorted_list = [random.randint(1, 100) for _ in range(100)]
    logging.debug(unsorted_list)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(eval(algorithm), unsorted_list) for algorithm in sorting_algorithms]

        for f in concurrent.futures.as_completed(results):
            print(f.result())


if __name__ == '__main__':
    print('Sorting Algorithms!')
    main()
