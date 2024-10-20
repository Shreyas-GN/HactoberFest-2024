class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node or node.key == key:
            return node
        return self._search(node.left, key) if key < node.key else self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node: return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left: return node.right
            if not node.right: return node.left
            temp = self._find_min(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self):
        return self._traverse(self.root, [])

    def _traverse(self, node, result, order="in"):
        if node:
            if order == "pre": result.append(node.key)
            self._traverse(node.left, result, order)
            if order == "in": result.append(node.key)
            self._traverse(node.right, result, order)
            if order == "post": result.append(node.key)
        return result

# Usage example:
bst = BinarySearchTree()
for key in [50, 30, 20, 40, 70, 60, 80]:
    bst.insert(key)

print("In-order:", bst.inorder())  # Output: [20, 30, 40, 50, 60, 70, 80]
bst.delete(20)
print("In-order after delete:", bst.inorder())  # Output: [30, 40, 50, 60, 70, 80]
