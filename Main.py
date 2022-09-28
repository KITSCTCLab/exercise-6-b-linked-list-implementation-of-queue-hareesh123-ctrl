class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    Newnode = Node(data)
    if front == None and rear == None:
      front = Newnode
      rear = Newnode
    else:
      rear->next = Newnode
      rear = Newnode
    

  def dequeue(self) -> None:
    if front == None:
      print("the queue is empty")
    elif front == rear:
      element = front.data
      front = rear = None
    else:
      element = front.data
      front = front.next
     return element
   

  def status(self) -> None:
    if front  == None:
      print("the queue is empty")
      return
    p = front
    while(p!=None):
      print(p.data)
      p = p.next


# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
