#class of node
class TreeNode:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

#class of BST
class BinarySearchTree:
    #basic function
    def __init__(self):
        self.root = None

    #add a node
    def add(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._add(self.root, value)


    def _add(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value, parent=node)
            else:
                self._add(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value, parent=node)
            else:
                self._add(node.right, value)

    def find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def delete(self, value):
        if self.root is None:
            print("NULL NULL NULL")
            return

        node = self._find_node(self.root, value)
        if node is None:
            print("NULL NULL NULL")
            return

        replacement = self._delete_node(node)
        self._print_replacement(replacement)

    def _find_node(self, node, value):
        if node is None:
            return None
        if value < node.value:
            return self._find_node(node.left, value)
        elif value > node.value:
            return self._find_node(node.right, value)
        else:
            return node

    def _delete_node(self, node):
        if node.left is None and node.right is None:
            replacement = None
            self._replace_node(node, None)
        elif node.left is None:
            replacement = node.right
            self._replace_node(node, node.right)
        elif node.right is None:
            replacement = node.left
            self._replace_node(node, node.left)
        else:
            successor = self.find_max(node.left)
            node.value = successor.value
            replacement = successor
            self._delete_node(successor)
            return node

        return replacement

    def _replace_node(self, node, new_node):
        if node.parent is None:
            self.root = new_node
        else:
            if node == node.parent.left:
                node.parent.left = new_node
            else:
                node.parent.right = new_node
        if new_node is not None:
            new_node.parent = node.parent

    def _print_replacement(self, node):
        if node is None:
            print("NULL NULL NULL")
        else:
            left_val = node.left.value if node.left else "NULL"
            right_val = node.right.value if node.right else "NULL"
            print(f"{node.value} {left_val} {right_val}")


def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        values = list(map(int, input[ptr:ptr + n]))
        ptr += n
        bst = BinarySearchTree()
        for val in values:
            bst.add(val)

        m = int(input[ptr])
        ptr += 1
        delete_values = list(map(int, input[ptr:ptr + m]))
        ptr += m
        for val in delete_values:
            bst.delete(val)


if __name__ == "__main__":
    main()