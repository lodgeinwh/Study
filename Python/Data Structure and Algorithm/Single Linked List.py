# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Author: lodge
# @Contact: lodgeinwh@gmail.com
# @File: Linked List.py
# @Time: 2019/2/21 20:05
# @Software: PyCharm


class Node():
    def __init__(self, data, next=None):
        self._data = data
        self._next = next

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, new_data):
        self._data = new_data

    def set_next(self, new_next):
        self._next = new_next


class SingleLinkedList():
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def size(self):
        current = self._head
        count = 0
        while current._next != None:
            count += 1
            current = current.get_next()
        return count

    def travel(self):
        current = self._head
        while current._next != None:
            print(current.get_data())
            current = current.get_next()
        print(current.get_data())

    def add_node(self, data):
        temp = Node(data)
        temp.set_next(self._head)
        self._head = temp

    def append_node(self, data):
        temp = Node(data)
        if self.is_empty():
            self._head = temp
        else:
            current = self._head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(temp)

    def search(self, data):
        current = self._head
        while current != None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False

    def find(self, data):
        current = self._head
        pos = 0
        while current != None:
            if current.get_data() == data:
                return pos
            else:
                current = current.get_next()
                pos += 1
        return -1

    def remove(self, data):
        current = self._head
        prev = None
        while current != None:
            if current.get_data() == data:
                if not prev:
                    self._head = current.get_next()
                else:
                    prev.set_next(current.get_next())
                    break
            else:
                prev = current
                current = current.get_next()

    def insert(self, data, pos):
        if pos <= 1:
            self.add_node(data)
        elif pos > self.size():
            self.append_node(data)
        else:
            temp = Node(data)
            count = 0
            current = self._head
            prev = None
            while count < pos:
                count += 1
                prev = current
                current = current.get_next()
            prev.set_next(temp)
            temp.set_next(current)
