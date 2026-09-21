class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [0] * size
        self.top = -1

    # Push
    def push(self, value):
        if self.top == self.size - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = value

    # Pop
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            value = self.stack[self.top]
            self.top -= 1
            print("Popped:", value)

    # Peek
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Top:", self.stack[self.top])

    # Display
    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            for i in range(self.top + 1):
                print(self.stack[i], end="")

                if i < self.top:
                    print(" -> ", end="")

            print(" -> TOP")


# Main
s = Stack(5)

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        s.push(value)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        break

    else:
        print("Invalid choice")