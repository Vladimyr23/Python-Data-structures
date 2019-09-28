#Queue Operations
#Vladimir Yesipov
#17 January 2010

import sys

max=6
queue=[]


#function to test if queue is empty
def isempty():
    if len(queue) == 0:
        return bool(1)
    else:
        return bool(0)


#function to test if queue is full
def isfull():
    if len(queue)==max:
        return bool(1)
    else:
        return bool(0)

#function to delete data from queue
def deletefromqueue(queue):
   if isempty():
        print ("Empty queue")
   else:
        object = queue.pop(0) # pop first entry in queue

#function to add data to stack
def addtoqueue(queue):
   if isfull():
        print ("Queue is full")
   else:
        queue.append((input("enter a value")))

#function to display data
def display_queue(queue):
    print("The contents of the queue are:")
    print (queue)

#start of main program
answer=0
while answer !="4":  #controls menu
    print """Menu
        1) Add to queue
        2) Pop item from queue
        3) Display number of items in queue
        4) Exit"""
    choice = raw_input("Make a selection> ")   # user input

    if "1" in answer: addtoqueue(queue)
    if "2" in answer: deletefromqueue(queue)
    if "3" in answer: display_queue_length(queue)
    if "4" in answer: print "Bye"


