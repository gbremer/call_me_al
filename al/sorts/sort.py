import os
import sys

class SortManipulator(object):

    def __init__(self):
        pass

    def less(self, a, b):
        return a < b

    def exchange(self, items, index_a, index_b):
        items[index_a], items[index_b] = items[index_b], items[index_a]

class CountingSortManipulator(SortManipulator):

    def __init__(self):
        super(SortManipulator, self).__init__()
        self._compare_count = 0
        self._exchange_count = 0

    def less(self, a, b):
        self._compare_count = self._compare_count + 1
        super(SortManipulator, self).less(a, b)
        
    def exchange(items, index_a, index_b):
        self._exchange_count = self._exchange_count + 1
        super(SortManipulator, self).exchange(items, index_a, index_b)
        
def selection_sort(items):
    n = len(items)
    for i in range(n):
        min = i
        for j in range(i, n):
            if items[j] < items[min]:
                min = j
        items[i], items[min] = items[min], items[i]

def _sorted(items, sort_function):
    local_items = items[:]
    sort_function(local_items)
    return local_items
    
def insertion_sort(items):
    for i in range(0, len(items)):
        for j in range(i, 0, -1):
            if items[j - 1] < items[j]:
                break
            items[j - 1], items[j] = items[j], items[j - 1]

def gap_tripleplusone(n):
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1 # 1, 4, 13, 40, 121, 364, 1093
    while gap > 0:
        yield gap
        gap = gap // 3

def gap_halve(n):
    gap = n // 2
    while gap > 0:
        yield gap
        gap = gap // 2
        
def shell_sort(items):
    n = len(items)
    gen = gap_halve(n)
    for gap in gen:
        for i in range(gap, n):
            j = i
            comp_index = i
            while j >= gap and items[j - gap] > items[comp_index]:
                items[j], items[j - gap] = items[j - gap], items[j]
                comp_index = j - gap
                j = j - gap

def merge(items, lo=None, mid=None, hi=None):
    # Merge a[ lo.. mid ] with a[ mid + 1.. hi]
    lo = lo if lo else 0
    mid = mid if mid else len(items) // 2
    hi = hi if hi else len(items)
    i = lo
    j = mid
    
    print lo, mid, hi, i, j
    aux = items[:]
    print aux
    for k in range(lo, hi): # Merge back to a[ lo.. hi]
        print 'in loop', k, i, j, lo, hi, mid, items, aux[k], aux[i], aux[j],
        if i >= mid:
            print 'i exhausted'
            items[k] = aux[j]
            j = j + 1
        elif j > hi:
            print 'j exhausted'
            items[k] = aux[i]
            i = i + 1
        elif aux[j] < aux[i]:
            print 'swap', aux[i], aux[j]
            items[k] = aux[j]
            j = j + 1
        else:
            print 'stable'
            items[k] = aux[i]
            i = i + 1
    print items

def selection_sorted(items):
    return _sorted(items, selection_sort)

def insertion_sorted(items):
    return _sorted(items, insertion_sort)

def shell_sorted(items):
    return _sorted(items, shell_sort)