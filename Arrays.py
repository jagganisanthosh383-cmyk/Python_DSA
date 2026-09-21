# Array Operations in Python - DSA

arr = []

# 1. Create Array
n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)


# 2. Display / Traverse
def display():
    print("Array:", arr)


# 3. Insert Element
def insert():
    value = int(input("Enter element: "))
    position = int(input("Enter position: "))

    if position < 0 or position > len(arr):
        print("Invalid position")
    else:
        arr.insert(position, value)
        print("Element inserted successfully")


# 4. Delete Element
def delete():
    position = int(input("Enter position to delete: "))

    if position < 0 or position >= len(arr):
        print("Invalid position")
    else:
        deleted = arr.pop(position)
        print("Deleted element:", deleted)


# 5. Search Element
def search():
    value = int(input("Enter element to search: "))

    if value in arr:
        print("Element found at index:", arr.index(value))
    else:
        print("Element not found")


# 6. Update Element
def update():
    position = int(input("Enter position: "))

    if position < 0 or position >= len(arr):
        print("Invalid position")
    else:
        value = int(input("Enter new value: "))
        arr[position] = value
        print("Element updated successfully")


# 7. Maximum
def maximum():
    if len(arr) == 0:
        print("Array is empty")
    else:
        print("Maximum:", max(arr))


# 8. Minimum
def minimum():
    if len(arr) == 0:
        print("Array is empty")
    else:
        print("Minimum:", min(arr))


# 9. Reverse
def reverse():
    arr.reverse()
    print("Array reversed")


# 10. Count Elements
def count():
    print("Number of elements:", len(arr))


# Menu
while True:

    print("\n========== ARRAY OPERATIONS ==========")
    print("1. Display")
    print("2. Insert")
    print("3. Delete")
    print("4. Search")
    print("5. Update")
    print("6. Maximum")
    print("7. Minimum")
    print("8. Reverse")
    print("9. Count")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display()

    elif choice == 2:
        insert()

    elif choice == 3:
        delete()

    elif choice == 4:
        search()

    elif choice == 5:
        update()

    elif choice == 6:
        maximum()

    elif choice == 7:
        minimum()

    elif choice == 8:
        reverse()

    elif choice == 9:
        count()

    elif choice == 10:
        print("Program ended.")
        break

    else:
        print("Invalid choice")