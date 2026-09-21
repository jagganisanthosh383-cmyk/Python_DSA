class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # 3. Insert at Specific Position
    def insert_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(1, position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return

        self.head = self.head.next

    # 5. Delete from End
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
            return

        # Only one node
        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    # 6. Delete from Specific Position
    def delete_position(self, position):
        if self.head is None:
            print("Linked List is empty")
            return

        if position == 1:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(1, position - 1):
            if temp.next is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp.next is None:
            print("Position out of range")
            return

        temp.next = temp.next.next

    # 7. Search an Element
    def search(self, key):
        temp = self.head
        position = 1

        while temp is not None:
            if temp.data == key:
                print("Element found at position:", position)
                return

            temp = temp.next
            position += 1

        print("Element not found")

    # 8. Display / Traverse
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 9. Count Nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # 10. Reverse Linked List
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


# Main Program

ll = LinkedList()

while True:

    print("\n===== LINKED LIST =====")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Specific Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete from Specific Position")
    print("7. Search an Element")
    print("8. Display")
    print("9. Count Nodes")
    print("10. Reverse Linked List")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        ll.insert_beginning(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        ll.insert_end(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        ll.insert_position(data, position)

    elif choice == 4:
        ll.delete_beginning()

    elif choice == 5:
        ll.delete_end()

    elif choice == 6:
        position = int(input("Enter position: "))
        ll.delete_position(position)

    elif choice == 7:
        key = int(input("Enter element to search: "))
        ll.search(key)

    elif choice == 8:
        ll.display()

    elif choice == 9:
        ll.count_nodes()

    elif choice == 10:
        ll.reverse()

    elif choice == 11:
        print("Program ended.")
        break

    else:
        print("Invalid choice")