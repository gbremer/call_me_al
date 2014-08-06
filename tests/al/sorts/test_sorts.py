import os
import sys
import string
import random
import unittest2 as unittest

import al.sorts.sort

class TestSortManipulator(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_less(self):
        sm = al.sorts.sort.SortManipulator()
        self.assertTrue(sm.less(1, 2))
        self.assertTrue(sm.less('a', 'b'))
        self.assertTrue(sm.less('First', 'Second'))
        self.assertTrue(sm.less(1.0, 1.1))
        self.assertTrue(sm.less('01', 'a'))

        self.assertFalse(sm.less(2, 1))
        self.assertFalse(sm.less('b', 'a'))
        self.assertFalse(sm.less('Second', 'First'))
        self.assertFalse(sm.less(1.1, 1.0))
        self.assertFalse(sm.less('a', '01'))

        self.assertFalse(sm.less(1, 1))
        self.assertFalse(sm.less('ABC', 'ABC'))

    def test_exchange(self):
        sm = al.sorts.sort.SortManipulator()
        items = range(10)

        sm.exchange(items, 0, 1)
        self.assertEqual(items, [1, 0, 2, 3, 4, 5, 6, 7, 8, 9])
        sm.exchange(items, 1, 9)
        self.assertEqual(items, [1, 9, 2, 3, 4, 5, 6, 7, 8, 0])
        
class TestSort(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _sort(self, sort_function):

        for items in string.uppercase, string.lowercase, string.digits:
            self.assertEqual(sort_function(list(items)), list(items))

        for items in string.uppercase, string.lowercase, string.digits:
            compare = list(items)
            sort_items = compare[:]
            random.shuffle(sort_items)
            self.assertEqual(sort_function(sort_items), compare)
    
    def test_selection(self):
        self._sort(al.sorts.sort.selection_sorted)

    def test_insertion(self):
        self._sort(al.sorts.sort.insertion_sorted)

    def test_shell(self):
        self._sort(al.sorts.sort.shell_sorted)

