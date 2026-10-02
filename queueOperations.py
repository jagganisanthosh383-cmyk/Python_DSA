class Queue:
  def __init__(self):
    self.queue=[]
    self.size=0

  def enqueue(self,data):
    self.queue.append(data)
    self.size+=1

  def dequeue(self):
    if self.size==0:
      print("queue is empty")
      return
    data=self.queue[0]
    for i in range(self.size-1):
      self.queue[i]=self.queue[i+1]
    self.queue.pop()
    self.size-=1
    print(data)

  def peek(self):
    if self.size==0:
      print("queue is empty")
      return
    print(self.queue[0])

  def traverse(self):
    if self.size==0:
      print("queue is empty")
      return
    for i in range(self.size):
      print(self.queue[i],end=" ")
    print()

  def search(self,data):
    for i in range(self.size):
      if self.queue[i]==data:
        print(f"data is at {i} found")
        return
    print("data is not found")

  def length(self):
    print(self.size)

  def insertatbeg(self,data):
    self.queue.append(0)

    for i in range(self.size,0,-1):
      self.queue[i]=self.queue[i-1]

    self.queue[0]=data
    self.size+=1

  def insertatposition(self,data,position):
    if position<0 or position>self.size:
      print("invalid position")
      return

    self.queue.append(0)

    for i in range(self.size,position,-1):
      self.queue[i]=self.queue[i-1]

    self.queue[position]=data
    self.size+=1

  def deletebyvalue(self,data):
    if self.size==0:
      print("queue is empty")
      return

    for i in range(self.size):
      if self.queue[i]==data:
        for j in range(i,self.size-1):
          self.queue[j]=self.queue[j+1]

        self.queue.pop()
        self.size-=1
        return

    print("data is not found")

  def deleteat(self,position):
    if self.size==0:
      print("queue is empty")
      return

    if position<0 or position>=self.size:
      print("invalid position")
      return

    for i in range(position,self.size-1):
      self.queue[i]=self.queue[i+1]

    self.queue.pop()
    self.size-=1

  def clear(self):
    self.queue=[]
    self.size=0


q=Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.traverse()

q.peek()

q.search(30)

q.dequeue()

q.length()

q.insertatbeg(5)
q.traverse()

q.insertatposition(25,2)
q.traverse()

q.deletebyvalue(25)
q.traverse()

q.deleteat(2)
q.traverse()

q.length()