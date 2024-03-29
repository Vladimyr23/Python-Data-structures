#-------------------------------------------------------------------------------
# Name:        OrderedLinkedList
# Purpose:
#
# Author:      Osnovnoy
#
# Created:     01/11/2016
# Copyright:   (c) Osnovnoy 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Node:

	def __init__(self,data=None,next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return "Node[Data=" + `self.data` + "]"



class LinkedList:

    def __init__(self):
		self.head = None

	# Inserting new data at the sorted list
	# A new node is created for this data element
    def insert(self,data):
        new_node = Node(data)

        # for the empty linked list
        if self.head is None:
            new_node.next = self.head
            self.head = new_node

        # for head at end
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node

        else :

            # Locate the node before the point of insertion
            current = self.head
            while(current.next is not None and
                 current.next.data < new_node.data):
                current = current.next

            new_node.next = current.next
            current.next = new_node

	# Deleting a given data value from the linked list
	# If the head contains this data value
	# Set head = node which comes next after the current head
	# Otherwise go to the node such that the node after it (next to it) contains the value we're looking for
	# set node.next = node.next.next
	# so, the node which contains the specified value/data; is skipped
    def delete(self,data):
        current = self.head
        if current.data == data:
			self.head = current.next
        if current == None:
			return False
        else:
			while (current != None) and (current.next != None) and (current.next.data != data):
				current = current.next
			if (current != None) and (current.next != None) :
				current.next = current.next.next
	# Find a given data value in the linked list
	# Traverse the linked list till you either find the data value or you come to the end of the list

    def find(self,data):
		found = False
		current = self.head
		while ((current != None) and (current.data != data) and ( current.next != None)):
			current = current.next
 		if ((current.data == data)):
			found = True
		return found

	# Display the linked list
	# Traverse the linked list till you reach its end
	# Display each node which you traverse
    def display(self):
		current = self.head
		string_representation = " "
		while current != None:
			string_representation +=  str(current) + "--->"
			current = current.next
		print string_representation

# Initialize a new linked list
print "Initializing linked list"
ll = LinkedList()

# Insert values in the linked list
print "Inserting values 1,2,3,9 in the Linked List"
ll.insert(9)
ll.insert(2)
ll.insert(3)
ll.insert(1)

# Display the linked list
print "Displaying the linked list"
ll.display()

# Delete an element from the linked list. Demonstrate the Delete function
print "Delete an element (data = 3) from the linked list"
ll.delete(3)

print "Display the linked list again. The value 3 is deleted. "
ll.display()

# Try to find the value 2 in the linked list (Demonstrating the Find function)
print "Try to find the value 2 in the linked list"
found = ll.find(2)
if found == True:
	print "The value 2 is present in the Linked List"
else:
	print "The value 2 is not present in the linked list"

# Try to find the value 20 in the linked list
print "Try to find the value 20 in the linked list"
found = ll.find(20)
if found == True:
	print "The value 20 is present in the Linked List"
else:
	print "The value 20 is not present in the linked list"

# Try to find the value 9 in the linked list
print "Try to find the value 9 in the linked list"
found = ll.find(9)
if found == True:
	print "The value 9 is present in the Linked List"
else:
	print "The value 9 is not present in the linked list"