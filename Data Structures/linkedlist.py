class Node():
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class DoubleNode():
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.previousNode = None


# This is exactly why we like linked lists
class LinkedList():
    def __init__(self):
        self.head = None  # There is no head node
        self.numOfNodes = 0  # There are no nodes

    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1  # Increment the number of nodes by 1
        new_node = Node(data)  # Create a new node with the passed data

        if not self.head:  # If there is no head node yet,
            self.head = new_node  # Then we want to make the head the newly created node. The linked list has one node now, and that node is the head
        else:  # If there is an existing head node
            # Then we want to create a pointer from the newly created node to the previous head node
            new_node.nextNode = self.head
            self.head = new_node  # Reassign the head node to be the newly created node

    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1  # Increment the number of nodes by 1
        new_node = Node(data)  # Create a new node

        actual_node = self.head  # Start at the head node

        while actual_node.nextNode is not None:  # Loop through the nodes until the next node is None
            actual_node = actual_node.nextNode  # If it's not None, move to the next node

        # AFter weve found the last node, update the reference to the new node
        actual_node.nextNode = new_node

    def size_of_linked_list(self):
        return self.numOfNodes

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode

    def remove_item(self, item):
        if self.head is None:  # If the linked list is empty, there is nothing to remove
            return

        actual_node = self.head
        previous_node = None

        # While the current node has data and its data isn't what we are searching for, move to the next node
        while actual_node is not None and actual_node.data != item:
            previous_node = actual_node
            actual_node = actual_node.nextNode

        if actual_node is None:  # If we reach the end of the list, we have a search miss, so return
            return

        if previous_node is None:  # If the head node is the one we want to get rid of, we have to update the head node to the current node
            self.head = actual_node
        else:
            # Get rid of the actual_node since it contains the data we want and update the pointers
            previous_node.nextNode = actual_node.nextNode
        self.numOfNodes = self.numOfNodes - 1


class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.numOfNodes = 0

    def insert_beginning(self, data):
        self.numOfNodes = self.numOfNodes + 1
        node = DoubleNode(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.previousNode = node
            node.nextNode = self.head
            self.head = node

    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1
        node = DoubleNode(data)

        if self.numOfNodes == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.nextNode = node
            node.previousNode = self.tail
            self.tail = node

    def traverse_forward(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.nextNode

    def traverse_backward(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.previousNode

    def remove_item(self, data):
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                previous_node = current_node.previousNode
                next_node = current_node.nextNode

                if next_node is None:
                    previous_node.nextNode = None
                    self.tail = previous_node

                elif previous_node is None:
                    next_node.previous_node = None
                    self.head = next_node

                else:
                    next_node.previousNode = previous_node
                    previous_node.nextNode = next_node

                self.numOfNodes = self.numOfNodes - 1
                return
            else:
                current_node = current_node.nextNode


if __name__ == "__main__":
    new_list = LinkedList()
    new_list.insert_start(10)
    new_list.insert_start(4)
    new_list.insert_start(3)
    new_list.insert_end(8)
    new_list.insert_end('Adam')
    new_list.insert_end(10)
    new_list.insert_end(100)
    new_list.insert_end(1000)
    new_list.insert_end(10000)

    print(f"Size of list is {new_list.size_of_linked_list()}")
    print("------------------")
    new_list.remove_item('Adam')
    new_list.remove_item(3000)
    new_list.traverse()
    print(f"Size of list is {new_list.size_of_linked_list()}")
    print("------------------")

    print("\nDoubleList")
    doubleList = DoubleLinkedList()
    doubleList.insert_beginning(1)
    doubleList.insert_end(10)
    doubleList.insert_end(100)
    doubleList.insert_end("Adam")
    doubleList.insert_beginning(0)
    print(f"Size of list is {doubleList.numOfNodes}")
    doubleList.traverse_forward()
    print("------------------")

    doubleList.remove_item(12)
    print(f"Size of list is {doubleList.numOfNodes}")
    doubleList.traverse_forward()
    print("------------------")
