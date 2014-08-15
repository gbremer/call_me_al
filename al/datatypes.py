
class Node(object):

    def __init__(self, item, next=None):
        self.item = item
        self.next = next
    
class Bag(object):

    def __init__(self):
        self._contents = []

    def add(self, item):
        self._contents.append(item)

    def isEmpty(self):
        return len(self._contents) == 0

    def size(self):
        return len(self._contents)

class Queue(object):

    def __init__(self):
        self._contents = []

    def enqueue(self, item):
        self._contents.insert(0, index)

    def dequeue(self):
        returnn self._contents.pop()

    def isEmpty(self):
        return len(self._contents) == 0

    def size(self):
        return len(self._contents)

class Stack(object):

    def __init__(self):
        self._contents = []

    def push(self, item):
        self._contents.append(item)

    def pop(self):
        return self._contents.pop()

    def isEmpty(self):
        return len(self._contents) == 0

    def size(self):
        return len(self._contents)

        