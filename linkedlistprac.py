# singly linked list 

class Node:
	def __init__ (self, data):
		self.data = data
		self.next = None

class LinkedList :
	def __init__(self):
		self.head = None
# insert at front
	def insert_front (self, value2bin):
		new_node = Node(value2bin)
		new_node.next = self.head
		self.head = new_node 

# insert after value2bin
	def insert_after(self, prev_value, value2bin):
		if prev_value is None :
			print ("insert prev value first")
		new_node = Node(value2bin)
		new_node.next = prev_value.next 
		prev_value.next = new_node	
# insert at end 
	def insert_at_end (self, data):
		pass
# print list
	def printlist (self):
		ptr = self.head
		while ptr :
			print (ptr.data),
			ptr = ptr.next


actual_list = LinkedList()
actual_list.insert_front(69)
actual_list.insert_front(66)
actual_list.insert_after(actual_list.head.next, 12)
actual_list.insert_at_end(45)
actual_list.printlist()