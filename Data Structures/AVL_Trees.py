class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.right_node = None
        self.left_node = None
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:

            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node...%d" % node.data)

                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None

                if parent is None:
                    self.root = None

                del node

                self.handle_violation(parent)

            elif node.left_node is None and node.right_node is not None:  # node !!!
                print("Removing a node with single right child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.rightChild == node:
                        parent.right_node = node.right_node
                else:
                    self.root = node.right_node

                node.right_node.parent = parent
                del node

                self.handle_violation(parent)

            elif node.right_node is None and node.left_node is not None:
                print("Removing a node with single left child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node

                self.handle_violation(parent)

            else:
                print('Removing node with two children....')

                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)

        return node

    def insert(self, data):
        if not self.root:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                node.height = max(self.calculate_height(
                    node.left_node), self.calculate_height(node.right_node))+1
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                node.height = max(self.calculate_height(
                    node.left_node), self.calculate_height(node.right_node))+1

        self.handle_violation(node)

    def handle_violation(self, node):
        while node is not None:
            node.height = max(self.calculate_height(
                node.left_node), self.calculate_height(node.right_node)) + 1
            self.violation_helper(node)
            node = node.parent

    def violation_helper(self, node):
        balance = self.calculate_balance(node)

        if balance > 1:
            if self.calculate_balance(node.left_node) < 0:
                self.rotate_left(node.left_node)

            self.rotate_right(node)

        if balance < -1:
            if self.calculate_balance(node.right_node) > 0:
                self.rotate_right(node.right_node)

            self.rotate_left(node)

    def rotate_right(self, node):
        print(f"Rotating right on {node.data}.")

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

        node.height = max(self.calculate_height(node.left_node),
                          self.calculate_height(node.right_node))+1
        temp_left_node.height = max(self.calculate_height(
            temp_left_node.left_node), self.calculate_height(temp_left_node.right_node))+1

    def rotate_left(self, node):
        print(f"Rotating left on {node.data}.")

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node

        node.height = max(self.calculate_height(node.left_node),
                          self.calculate_height(node.right_node))+1
        temp_right_node.height = max(self.calculate_height(
            temp_right_node.left_node), self.calculate_height(temp_right_node.right_node))+1

    def calculate_height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def calculate_balance(self, node):
        if node is None:
            return 0

        return self.calculate_height(node.left_node) - self.calculate_height(node.right_node)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)

        if node.left_node is not None:
            l = node.left_node.data
        else:
            l = "NULL"

        if node.right_node is not None:
            r = node.right_node.data
        else:
            r = "NULL"

        if node.parent is not None:
            p = node.parent.data
        else:
            p = "NULL"

        print(f"{node.data} left: {l} right: {r} parent: {p} height: {node.height}.")

        if node.right_node:
            self.traverse_in_order(node.right_node)


if __name__ == "__main__":
    avl = AVLTree()
    avl.insert(32)
    avl.insert(16)
    avl.insert(48)
    avl.insert(8)
    avl.insert(24)
    avl.insert(40)
    avl.insert(56)
    avl.insert(36)
    avl.insert(44)
    avl.insert(44)
    avl.insert(52)
    avl.insert(60)
    avl.insert(4)
    avl.insert(58)
    avl.insert(62)
    avl.remove(4)

    avl.traverse()
