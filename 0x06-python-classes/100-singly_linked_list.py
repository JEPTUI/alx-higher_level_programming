#!/usr/bin/python3
""" Module -100-singly_linked_list
Defines a node of a singly linked list """


class Node:
    """
    Defines class Node
    Args: data(int)
        next_node
    """

    def __init__(self, data, next_node=None):
        """
        Initializes Node
        Private instance attributes:
            data
            next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        getter
        Retrieves data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets data to value
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        getter
        Retrieves next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets next_node to value
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Defines class SinglyLinkedList
    Args: head
    """

    def __init__(self):
        """
        Initializes class SinglyLinkedList
        Private instance attribute: head
        """
        self.__head = None

    def __str__(self):
        """
        print the entire list in stdout
        """
        string = ""
        temp = self.__head
        while temp is not None:
            string += str(temp.data)
            temp = temp.next_node
            if temp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        temp = self.__head
        if new.data < temp.data:
            new.next_node = self.__head
            self.__head = new
            return
        while ((temp.next_node is not None)
                and (new.data > temp.next_node.data)):
            temp = temp.next_node
        new.next_node = temp.next_node
        temp.next_node = new
        return
