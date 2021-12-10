from typing import Any, Callable, List

import binarytree as BinaryTree

def horizontal_sum(tree: BinaryTree) -> List[Any]:
    wynik: List[Any] = []

    def przypisanie_poziomow(node: 'TreeNode', level: int = 0) -> None:
        if len(wynik) <= level:
            wynik.append(node.value)
        else:
            wynik[level] += node.value
        for i in node.left_child, node.right_child:
            if i is not None:
                przypisanie_poziomow(i, level + 1)
    przypisanie_poziomow(tree.root)
    return wynik


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

    def show(self, level):
        if self.right_child is not None:
            self.right_child.show(level+1)
        print('  ' * 4 * level + '-->', self.value)
        if self.left_child is not None:
            self.left_child.show(level+1)

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

    def show(self):
        self.root.show(0)


tree = BinaryTree(10)

assert tree.root.value == 10

tree.root.add_right_child(2)
tree.root.right_child.add_right_child(3)
tree.root.add_left_child(1)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(9)

print(horizontal_sum(tree))


#asserty
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True

tree.show()
