import unittest2 as unittest
import al.strings.alphabet as alphabet

import string
import random

class TestAlphabet(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_len(self):
        for s in [string.uppercase, string.lowercase, string.digits]:
             self.assertEquals(len(s), alphabet.Alphabet(s).R())

    def test_index(self):
        for s in [string.uppercase, string.lowercase, string.digits]:
             a = alphabet.Alphabet(s)
             for index, char in enumerate(s):
                 self.assertEqual(index, a.toIndex(char), 'testing toIndex %s at index %d' % (char, index))
                 self.assertEqual(char, a.toChar(index), 'testing toChar %d with char %s' % (index, char))


    def test_contains(self):
        for s in [string.uppercase, string.lowercase, string.digits]:
            a = alphabet.Alphabet(s)
            for c in s:
                self.assertTrue(a.contains(c), 'Checking membership of %s' % c)

    def test_indices(self):
        for s in [string.uppercase, string.lowercase, string.digits]:
            a = alphabet.Alphabet(s)
            self.assertTrue(a.toIndices(s), range(len(s)))

    def test_chars(self):
        for s in [string.uppercase, string.lowercase, string.digits]:
            a = alphabet.Alphabet(s)
            self.assertTrue(a.toChars(range(len(s))), list(s))

                 
        