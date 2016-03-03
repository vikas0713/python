class Node:
 def __init__(self):
  self.data = None
  self.next = None
 def setData(self, data):
  self.data = data
 def setNext(self, next):
  self.next = next
 def getData(self):
  return self.data
 def getNext(self):
  return self.next
 def hasNext(self):
  return self.next!= None
 def length(self):
  current = self.head
  count = 0

  while current !=None:
   count = count + 1
   current = current.getNext()
  return count
 def getHead(self):
 def insertAtBegining(self,data):
 	newNode = Node()
 	newNode.setData(data)
 	if self.length() == 0:
 		self.head = newNode
 	else:
 		newNode.setNext(self.head)
 		self.head = newNode
 	self.length+=1
