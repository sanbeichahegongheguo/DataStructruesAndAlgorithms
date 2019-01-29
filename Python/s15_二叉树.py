class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None
        