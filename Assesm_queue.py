#-------------------------------------------------------------------------------
# Name:        Queue operations
# Purpose:
#
# Author:      Vladimir Yesipov
#
# Created:     11/10/2016
# Copyright:   (c) Vladimir Yesipov 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

queue=[]

#function to test if queue is empty
def isempty(queue):
    if len(queue) == 0:
        print ("The queue is empty")
        return bool(1)
    else:
       print (queue)
       return bool(0)


#function to delete data from queue
def popfromqueue(queue):
   if isempty(queue):
        print ("Empty queue")

   else:
        object = queue.pop(0) # pop first entry in queue
        print ("Item removed")

#function to add data to queue
def addtoqueue(queue):
    answer=""
    while answer != "n":
        queue.append((input("enter a value")))
        print (queue)
        answer=raw_input("Add another value? n - to finish")
    return queue

#function to display queue length
def display_queue_length(queue):
    print("Number of items in the queue:")
    print len(queue)


#start of main program
choice=""
while choice !="6":  #controls menu
    print """Menu
        1) Add to queue
        2) Pop item from queue
        3) Check if the queue is empty
        4) List queue contents
        5) Display number of items in the queue
        6) Exit"""
    choice = raw_input("Make a selection> ")   # user input

    if choice=="1": addtoqueue(queue)
    if choice=="2": popfromqueue(queue)
    if choice=="3": isempty(queue)
    if choice=="4": isempty(queue)
    if choice=="5": display_queue_length(queue)
    if choice=="6": print "Bye"
