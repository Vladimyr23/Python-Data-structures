#-------------------------------------------------------------------------------
# Name:        StackLinkedList
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

	# Inserting new data at the end of the list
	# Iterate through the list till we encounter the last node.
	# A new node is created for this data element
	# And the last pointer points to this
    def insert(self):
        answer=""
        while answer != "n":
            data=input("enter a value")
            if (self.head == None):
                self.head = Node(data)
            else:
                current = self.head
                while (current.next != None) :
                    current = current.next
                current.next = Node(data)
            answer=raw_input("Add another value? n - to finish")

	# Deleting last element from the list

    def delete(self):
        current = self.head

        if current == None:
			return False
        else:
            while (current.next.next != None):
                current = current.next
            print current.next, "Item removed"
            current.next = None



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

#if list is empty returns "0" else returns the stack length
    def length(self):
        current=self.head
        count=0
        while(current):
            count+=1
            current=current.next
        if count ==0:
            print "Stack is empty"
        else:
            print "Stack contains ",count," element(s)"

# Initialize a new linked list
print "Initializing linked list"
ll = LinkedList()

#start of main program
choice=""
while choice !="6":  #controls menu
    print """Menu
        1) Add to stack
        2) Pop item from stack
        3) Check if the stack is empty
        4) List stack contents
        5) Display number of items in the stack
        6) Exit"""
    choice = raw_input("Make your selection> ")   # user input

    if choice=="1": ll.insert()
    if choice=="2": ll.delete()
    if choice=="3": ll.length()
    if choice=="4": ll.display()
    if choice=="5": ll.length()
    if choice=="6": print "Bye"

