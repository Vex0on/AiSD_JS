from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

    def show(self, gap_size = 0):
        pre1 = 4 * " " + "   " * gap_size + "|_"
        str1 = pre1[:-2]
        str2 = pre1[:-2]
        print(pre1, self.value)
        if self.left_child:
            print(str2)
            self.left_child.show(gap_size = gap_size + 1)
        if self.right_child:
            print(str1)
            self.right_child.show(gap_size = gap_size + 1)

    def __str__(self):
        return str(self.value)


class BinaryTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def show(self, gap_size=0):
        pre1 = " |_"
        str1 = " " * 7
        str2 = "    " * 7
        print(str(self.root.value))
        print (pre1[:-2])
        if self.root.left_child:
            print(str2)
            self.root.left_child.show(gap_size=gap_size + 1)
        if self.root.right_child:
            print(str1)
            self.root.right_child.show(gap_size=gap_size + 1)


tree = BinaryTree(10)

assert tree.root.value == 10

tree.root.add_right_child(2)
tree.root.right_child.add_right_child(3)
tree.root.add_left_child(1)
tree.root.left_child.add_left_child(1)


assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False


assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True

tree.show()
