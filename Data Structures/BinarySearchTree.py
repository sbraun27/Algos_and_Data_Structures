class Node():
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert_node(self, node, data):
        if data < node.data:  # Go to the left subtree
            if node.leftChild:
                self.insert_node(node.leftChild, data)
            else:
                node.leftChild = Node(data, node)
        else:  # Go to the right subtree
            if node.rightChild:
                self.insert_node(node.rightChild, data)
            else:
                node.rightChild = Node(data, node)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)

        else:
            self.insert_node(self.root, data)

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)
        print(f"{node.data}")

        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.rightChild:
            self.get_max(node.rightChild)
        else:
            print(node.data)
            return node.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.leftChild:
            self.get_min(node.leftChild)
        else:
            print(node.data)
            return node.data

    def remove_node(self, data, node):
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.leftChild)
        elif data > node.data:
            self.remove_node(data, node.rightChild)
        else:
            if node.leftChild is None and node.rightChild is None:
                print(f"Removing a leaf node... {node.data}")

                parent = node.parent

                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None

                if parent is None:
                    self.root = None

                del node

            elif node.leftChild is None and node.rightChild is not None:
                print(
                    f"Removing a node with a single right child... {node.data}")

                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                else:
                    self.root = node.rightChild

                node.rightChild.parent = parent
                del node

            elif node.rightChild is None and node.leftChild is not None:
                print(
                    f"Removing a node with a single left child... {node.data}")

                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild
                else:
                    self.root = node.leftChild

                node.leftChild.parent = parent
                del node

            else:
                print(f"Removing node with two children... {node.data}")

                predecessor = self.get_predecessor(node.leftChild)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)

        return node

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)


if __name__ == "__main__":
    BST = BinarySearchTree()
    BST.insert(10)
    BST.insert(5)
    BST.insert(66)
    BST.insert(-5)
    BST.insert(1)
    BST.insert(99)
    BST.insert(34)
    BST.insert(1000)
    BST.traverse()

    print("--------------------------\nmax and min values are:")
    BST.get_max_value()
    BST.get_min_value()

    BST.remove(15)
    BST.traverse()
    BST.remove(34)
    BST.traverse()
    BST.remove(1000)
    BST.traverse()
    BST.remove(66)
    BST.traverse()
    BST.remove(5)
    BST.traverse()
    BST.remove(10)
    BST.traverse()
