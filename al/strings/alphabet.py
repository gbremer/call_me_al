import math
import string

UPPERCASE = string.uppercase
LOWERCASE = string.lowercase
DIGITS    = string.digits
DECIMAL   = string.digits

BINARY      = '01'
DNA         = 'ACTG'
OCTAL       = DECIMAL[:8]
HEXADECIMAL = DECIMAL + UPPERCASE[:6]
PROTEIN     = 'ACDEFGHIKLMNPQRSTVWY'
BASE64      = UPPERCASE + LOWERCASE + DECIMAL + '+/'
ASCII       = ''.join([ chr(c) for c in range(2 ** 7)])
EXTENDED_ASCII = ''.join([ chr(c) for c in range(2 ** 8)])


class Alphabet(object):

    def __init__(self, alphabet):
        self._alphabet = alphabet
        self._len = len(alphabet)
        self._lgR = int(math.ceil(math.log(self._len, 2)))

    def toChar(self, index):
        return self._alphabet[index]

    def toIndex(self, char):
        return self._alphabet.index(char)

    def contains(self, char):
        return char in self._alphabet

    def R(self):
        return self._len

    def lgR(self):
        return self._lgR

    def toIndices(self, alphabet):
        return [ self.toIndex(a) for a in alphabet ]

    def toChars(self, indices):
        return [ self.toChar(i) for i in indices ]
