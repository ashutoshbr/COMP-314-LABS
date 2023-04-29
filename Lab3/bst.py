class Node:
    """
    Representation of a Node in the BST in the form of key value pair
    """

    def __init__(self, key: int, value: str, left=None, right=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def _set(self, key, value, left, right) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def _reset(self) -> None:
        self.key = None
        self.value = None
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"Node({self.key}, {self.value})"


class BinarySearchTree:
    def __init__(self) -> None:
        self.node_count = 0
        self.root_node = None

    def size(self):
        # Returns total number of node in the BST
        return self.node_count

    def add(self, key: int, value: str):
        # Adds a new node to the BST
        new_node = Node(key, value)
        if self.node_count == 0:
            self.root_node = new_node
            self.node_count += 1
        else:
            current_node = self.root_node
            while True:
                # Left sub-tree
                if key <= current_node.key:
                    if current_node.left is None:
                        current_node.left = new_node
                        self.node_count += 1
                        return
                    else:
                        current_node = current_node.left
                # Right sub-tree
                elif key > current_node.key:
                    if current_node.right is None:
                        current_node.right = new_node
                        self.node_count += 1
                        return
                    else:
                        current_node = current_node.right

    def search(self, key) -> str | None:
        # Returns the value for the provided key
        current_node = self.root_node
        while current_node:
            if key == current_node.key:
                return current_node.value
            elif key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
        return None

    def smallest(self) -> tuple[int, str]:
        node = self.root_node
        while node.left:
            node = node.left
        return (node.key, node.value)

    def largest(self) -> tuple[int, str]:
        node = self.root_node
        while node.right:
            node = node.right
        return (node.key, node.value)

    def inorder_walk(self):
        arr = []
        stack = []
        current_node = self.root_node
        # Loop until both stack and current_node are not null
        while stack or current_node:
            # If left child exists push the current node to the stack
            # And go to its left left child.
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            # If no left child, pop from stack
            # Add the key of node popped from stack to return value
            # Set the current node to right child of the popped node
            else:
                current_node = stack.pop()
                arr.append(current_node.key)
                current_node = current_node.right
        return [x for x in arr if x is not None]

    def preorder_walk(self):
        arr = []
        stack = []
        # Visit the root node at first pop
        stack.append(self.root_node)
        while stack:
            current_node = stack.pop()
            arr.append(current_node.key)

            # Push to right node first such that
            # it can be traversed only after all its left nodes are traversed
            if current_node.right:
                stack.append(current_node.right)
            # Push the left node to the top of the stack
            # It gets visited right after the push
            if current_node.left:
                stack.append(current_node.left)
        return [x for x in arr if x is not None]

    def postorder_walk(self):
        arr = []
        stack = []
        stack.append(self.root_node)
        while stack:
            # Pop the parent
            # Push left child to the stack
            # Push right child to the stack
            current_node = stack.pop()
            arr.append(current_node.key)
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
        # Reverse the array
        return arr[::-1]

    def remove(self, key):
        parent_node = None
        current_node = self.root_node
        while current_node.key != key and current_node:
            parent_node = current_node
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        # Case 1: Node to be deleted has no children
        if not current_node.left and not current_node.right:
            if current_node == self.root_node:
                self.root_node = None
            elif current_node == parent_node.left:
                parent_node.left = None
            else:
                parent_node.right = None

        # Case 2: Node to be deleted has one child
        elif not current_node.left or not current_node.right:
            if current_node.left:
                child_node = current_node.left
            else:
                child_node = current_node.right

            if current_node == self.root_node:
                self.root_node = child_node
            elif current_node == parent_node.left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

        # Case 3: Node to be deleted has two children
        else:
            # Node with the largest key in the left subtree
            max_left = current_node.left
            while max_left.right:
                max_left = max_left.right

            # Copy the key and value of the node with the largest key
            # in the left subtree to the node to be deleted
            current_node.key = max_left.key
            current_node.value = max_left.value

            # Remove the node with the largest key in the left subtree
            parent_node = current_node
            current_node = current_node.left
            while current_node.right:
                parent_node = current_node
                current_node = current_node.right

            if current_node == parent_node.left:
                parent_node.left = current_node.left
            else:
                parent_node.right = current_node.left

        # Decrease the node count
        self.node_count -= 1
