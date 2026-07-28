class TreeNode:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BST:
    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, val: int) -> None:
        self.root = self._insert(self.root, val)

    def inorder_traverse(self) -> None:
        self._inorder_traverse(self.root)
        print()

    def contains(self, val: int) -> bool:
        return self._contains(self.root, val)

    def remove(self, val: int) -> None:
        self.root = self._remove(self.root, val)

    def _contains(self, node: TreeNode | None, val: int) -> bool:
        if node is None:
            return False
        if node.val == val:
            return True
        return self._contains(node.left, val) if val < node.val else self._contains(node.right, val)

    def _inorder_traverse(self, node: TreeNode | None) -> None:
        if node is None:
            return
        self._inorder_traverse(node.left)
        print(node.val, end=" ")
        self._inorder_traverse(node.right)

    def _insert(self, node: TreeNode | None, val: int) -> TreeNode:
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def _remove(self, node: TreeNode | None, val: int) -> TreeNode | None:
        if node is None:
            return None
        if val < node.val:
            node.left = self._remove(node.left, val)
        elif val > node.val:
            node.right = self._remove(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                right_min_node = node.right
                while right_min_node.left is not None:
                    right_min_node = right_min_node.left
                node.val = right_min_node.val
                node.right = self._remove(node.right, right_min_node.val)
        return node


if __name__ == "__main__":
    bst = BST()

    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    bst.inorder_traverse()

    key = 40
    print(bst.contains(key))

    bst.remove(30)
    bst.inorder_traverse()
