class stack:
  def __init__(self,size):
    self._a=[]
    self._top=None
    self._size=size

  def push(self,data):
    if self._top is not None:
      if self._top+1==self._size:
        print('stack overflow')
        return

    if self._top is None:
      ar=[0]
      self._top=0
      ar[self._top]=data
      self._a=ar
    else:
      ar=[0 for i in range(self._top+2)]

      for i in range(self._top+1):
        ar[i]=self._a[i]

      ar[-1]=data
      self._top+=1
      self._a=ar

  def peek(self):
    if self._top is None:
      return "we dont have any elements"

    return self._a[self._top]

  def pop(self):
    if self._top is None:
      print('stack underflow')
      return

    temp=self._a[-1]

    ar=[0 for i in range(self._top)]

    for i in range(self._top):
      ar[i]=self._a[i]

    self._top-=1

    if self._top<0:
      self._top=None

    self._a=ar

    return temp

  def display(self):
    if self._top is None:
      print("stack is empty")
      return

    for i in range(self._top,-1,-1):
      print(self._a[i],end=" ")
    print()

  def search(self,data):
    if self._top is None:
      print("stack is empty")
      return

    for i in range(self._top,-1,-1):
      if self._a[i]==data:
        print(f"data is at {i} found")
        return

    print("data is not found")

  def length(self):
    if self._top is None:
      print(0)
    else:
      print(self._top+1)

  def isEmpty(self):
    if self._top is None:
      print("stack is empty")
    else:
      print("stack is not empty")

  def isFull(self):
    if self._top is not None:
      if self._top+1==self._size:
        print("stack is full")
        return

    print("stack is not full")

  def clear(self):
    self._a=[]
    self._top=None
    print("stack is cleared")


stack=stack(5)

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print(stack.peek())

stack.search(20)

stack.length()

stack.isEmpty()

stack.isFull()

print(stack.pop())

stack.display()

stack.push(40)
stack.push(50)
stack.push(60)

stack.display()

stack.isFull()

stack.search(100)

stack.length()

stack.clear()

stack.display()

print(stack.peek())

stack.pop()