#!/usr/bin/python3
# 100-singly_linked_list.py
"""Defines a node"""


class Node:
    """A class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance with data and next_node.

        Args:
            data (int): The data of the node.
            next_node (Node, optional): The reference to the next node.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.

        Returns:The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.

        Args:
            value (int): The data of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the reference to the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the reference to the next node.

        Args:
            value (Node): The reference to the next node.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list.

    Attributes:
        head: The head node of the linked list.
    """

    def __init__(self):
        """Initializes an empty SinglyLinkedList instance."""

        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the linked list.

        Args:
            value (int): The value of the new Node.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and 
	    current.next_node.data < value:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns:The string representation of the linked list."""

        current = self.head
        linked_list_str = ""
        while current is not None:
            linked_list_str += str(current.data) + "\n"
            current = current.next_node
        return linked_list_str.strip()
