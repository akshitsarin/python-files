# singly linked list final
class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

class LinkedList:
    def __init__(self):
        self.head = None # initialise head

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print "The given previous node must inLinkedList."
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next =  new_node

    def printList(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.next

if __name__=='__main__':
    llist = LinkedList()
    # inserting  6, updated linked list : 6->None
    llist.append(6)
    # inserting  7 at the beginning, updated linked list : 7->6->None
    llist.push(7)
    # inserting 1 at the beginning, updated linked list : 1->7->6->None
    llist.push(1)
    # inserting 4 at the end, updated linked list : 1->7->6->4->None
    llist.append(4)
    # inserting 8 after 7, updated linked list : 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)
    print 'Linked List :',
    llist.printList()