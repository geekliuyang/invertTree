class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Foo():
    def __init__(self):
        self.node = TreeNode('#')
        self.node.left = 0
        self.node.right = 1

    def foo(self):
        left = self.node.left
        right = self.node.right
        temp = left

        left = right
        right = temp

        print self.node.left, self.node.right

f=Foo()
f.foo()