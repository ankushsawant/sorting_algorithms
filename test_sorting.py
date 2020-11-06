import unittest
from sorting import bubble_sort, insertion_sort, selection_sort, merge, m_sort, q_sort


class MyTestCase(unittest.TestCase):
    def test_bubble_sort(self):
        u_list = [8, 2, 6, 4, 5]
        s_list = [2, 4, 5, 6, 8]
        self.assertEqual(bubble_sort(u_list)['u_list'], s_list)

    def test_insertion_sort(self):
        u_list = [8, 2, 6, 4, 5]
        s_list = [2, 4, 5, 6, 8]
        self.assertEqual(insertion_sort(u_list)['u_list'], s_list)

    def test_selection_sort(self):
        u_list = [8, 2, 6, 4, 5]
        s_list = [2, 4, 5, 6, 8]
        self.assertEqual(selection_sort(u_list)['u_list'], s_list)

    def test_merge(self):
        list_a = [3, 5, 7]
        list_b = [2, 4, 6, 8, 10]
        self.assertEqual(merge(list_a, list_b), [2, 3, 4, 5, 6, 7, 8, 10])

    def test_m_sort(self):
        u_list = [8, 2, 6, 4, 5]
        s_list = [2, 4, 5, 6, 8]
        self.assertEqual(m_sort(u_list), s_list)

    def test_q_sort(self):
        u_list = [8, 2, 6, 4, 5]
        s_list = [2, 4, 5, 6, 8]
        self.assertEqual(q_sort(u_list), s_list)


if __name__ == '__main__':
    unittest.main()
