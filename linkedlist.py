class Node:
  def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
  def __init__(self, data):
      self.head = Node(data)

  def add(self, data):
      current = self.head
      while current.next is not None:
          current = current.next
      current.next = Node(data)

  def traverse(self):
      current = self.head
      while current.next is not None:
          print(current.data, end="->")
          current = current.next
      print(current.data)

# Usage
li = LinkedList(10)
li.add(20)
li.add(30)

li.traverse()
