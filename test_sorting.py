import unittest
from sorting_algorithms.sorting import bubble_sort


class MyTestCase(unittest.TestCase):
    def test_bubble_sort(self):
        u_list = [8, 2, 6, 4, 5]
        s_list = [2, 4, 5, 6, 8]
        self.assertEqual(bubble_sort(u_list)['u_list'], s_list)


if __name__ == '__main__':
    unittest.main()
